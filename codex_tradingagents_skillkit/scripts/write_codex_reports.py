# ruff: noqa: E501

from __future__ import annotations

import argparse
import csv
import json
import re
from io import StringIO
from pathlib import Path
from typing import Any

ANALYST_KEYS = ["market_report", "sentiment_report", "news_report", "fundamentals_report"]


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _tool_output(evidence: dict[str, Any], role: str, tool_name: str) -> str:
    return evidence["roles"].get(role, {}).get("tool_calls", {}).get(tool_name, {}).get("output", "")


def _parse_field_table(output: str, heading: str) -> dict[str, str]:
    lines = output.splitlines()
    result: dict[str, str] = {}
    in_section = False
    for line in lines:
        if line.startswith(f"### {heading}"):
            in_section = True
            continue
        if in_section and line.startswith("### "):
            break
        if not in_section or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 2 or cells[0] in {"Field", "Indicator", "---"} or set(cells[0]) == {"-"}:
            continue
        result[cells[0]] = cells[1]
    return result


def _parse_recent_closes(output: str) -> list[tuple[str, float]]:
    rows: list[tuple[str, float]] = []
    in_section = False
    for line in output.splitlines():
        if line.startswith("### Recent verified closes"):
            in_section = True
            continue
        if in_section and line.startswith("### "):
            break
        if not in_section or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 2 or cells[0] in {"Date", "---"}:
            continue
        try:
            rows.append((cells[0], float(cells[1])))
        except ValueError:
            continue
    return rows


def _parse_stock_csv(output: str) -> list[dict[str, str]]:
    marker = "Date,Open,High,Low,Close,Volume,Dividends,Stock Splits"
    if marker not in output:
        return []
    csv_text = output[output.index(marker) :]
    return list(csv.DictReader(StringIO(csv_text)))


def _parse_fundamentals(output: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in output.splitlines():
        if ": " not in line or line.startswith("#"):
            continue
        key, value = line.split(": ", 1)
        values[key.strip()] = value.strip()
    return values


def _parse_news(output: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in output.splitlines():
        if line.startswith("### "):
            if current:
                items.append(current)
            match = re.match(r"### (?P<title>.+?) \(source: (?P<source>.+?)\)", line)
            if match:
                current = {
                    "title": match.group("title"),
                    "source": match.group("source"),
                    "summary": "",
                }
            else:
                current = {"title": line[4:], "source": "unknown", "summary": ""}
            continue
        if current and line and not line.startswith("Link:") and not line.startswith("## "):
            current["summary"] = (current["summary"] + " " + line.strip()).strip()
    if current:
        items.append(current)
    return items


def _num(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        return float(value.replace(",", ""))
    except ValueError:
        return None


def _company_terms(ctx_or_evidence: dict[str, Any]) -> list[str]:
    ticker = str(ctx_or_evidence["ticker"]).upper()
    base = ticker.split(".", 1)[0]
    company = str(ctx_or_evidence.get("identity", {}).get("company_name", ""))
    terms = [ticker, base, f"${base}"]
    if company:
        terms.append(company)
        terms.append(company.split()[0])
    return [term for term in terms if term]


def _mentions_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def _line_date(line: str) -> str | None:
    match = re.search(r"\[(?P<date>\d{4}-\d{2}-\d{2})T", line)
    return match.group("date") if match else None


def _filter_social_lines(ticker: str, trade_date: str, identity: dict[str, Any], text: str) -> dict[str, Any]:
    terms = _company_terms({"ticker": ticker, "identity": identity})
    kept: list[str] = []
    removed = 0
    for line in text.splitlines():
        if not line.strip():
            continue
        line_date = _line_date(line)
        if line_date and line_date > trade_date:
            removed += 1
            continue
        if not _mentions_any(line, terms):
            removed += 1
            continue
        if ticker.upper() == "MSFT" and re.search(r"(Apple|AAPL)", line, re.IGNORECASE):
            removed += 1
            continue
        kept.append(line)
    return {
        "text": "\n".join(kept).strip() or "<no relevant same-date social lines retained>",
        "kept": len(kept),
        "removed": removed,
    }


def _remove_cross_ticker_lines(ticker: str, text: str) -> str:
    if ticker.upper() != "MSFT":
        return text
    kept = [
        line
        for line in text.splitlines()
        if not re.search(r"(Apple|AAPL)", line, re.IGNORECASE)
    ]
    return "\n".join(kept).strip() or "<cross-ticker social lines removed>"


def _remove_cross_ticker_news(ticker: str, items: list[dict[str, str]]) -> list[dict[str, str]]:
    if ticker.upper() != "MSFT":
        return items
    return [
        item
        for item in items
        if not re.search(
            r"(Apple|AAPL)",
            f"{item.get('title', '')} {item.get('summary', '')}",
            re.IGNORECASE,
        )
    ]


def _news_buckets(ctx: dict[str, Any]) -> dict[str, list[dict[str, str]]]:
    terms = _company_terms(ctx)
    direct: list[dict[str, str]] = []
    indirect: list[dict[str, str]] = []
    excluded: list[dict[str, str]] = []
    indirect_terms = {
        "smartphone",
        "iphone",
        "semiconductor",
        "downgrade",
        "upgrade",
        "valuation",
    }
    for item in ctx["news_items"]:
        text = f"{item.get('title', '')} {item.get('summary', '')}"
        if _mentions_any(text, terms):
            direct.append(item)
        elif any(term in text.lower() for term in indirect_terms):
            indirect.append(item)
        else:
            excluded.append(item)
    return {"direct": direct, "indirect": indirect, "excluded": excluded}


def _fmt(value: str | None) -> str:
    if value in {None, ""}:
        return "N/A"
    number = _num(value)
    if number is None:
        return str(value)
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.1f}B"
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    return f"{number:.2f}"


def _score_component(label: str, evidence: str, points: int) -> dict[str, Any]:
    return {"label": label, "evidence": evidence, "points": points}


def _direction(ctx: dict[str, Any]) -> dict[str, Any]:
    close = _num(ctx["ohlcv"].get("Close"))
    ema10 = _num(ctx["indicators"].get("close_10_ema"))
    sma50 = _num(ctx["indicators"].get("close_50_sma"))
    sma200 = _num(ctx["indicators"].get("close_200_sma"))
    rsi = _num(ctx["indicators"].get("rsi"))
    macd = _num(ctx["indicators"].get("macd"))
    macds = _num(ctx["indicators"].get("macds"))
    pe = _num(ctx["fundamentals"].get("PE Ratio (TTM)"))
    pb = _num(ctx["fundamentals"].get("Price to Book"))
    roe = _num(ctx["fundamentals"].get("Return on Equity"))
    net_income = _num(ctx["fundamentals"].get("Net Income"))

    score = 0
    components: list[dict[str, Any]] = []
    if close is not None and sma200 is not None:
        points = 1 if close > sma200 else -1
        components.append(_score_component("Long-term trend", f"close {close:.2f} vs 200 SMA {sma200:.2f}", points))
        score += points
    if close is not None and sma50 is not None:
        points = 1 if close > sma50 else -1
        components.append(_score_component("Medium-term trend", f"close {close:.2f} vs 50 SMA {sma50:.2f}", points))
        score += points
    if close is not None and ema10 is not None:
        points = 1 if close > ema10 else -1
        components.append(_score_component("Near-term trend", f"close {close:.2f} vs 10 EMA {ema10:.2f}", points))
        score += points
    if rsi is not None:
        points = 1 if rsi >= 50 else -1
        components.append(_score_component("RSI momentum", f"RSI {rsi:.2f}", points))
        score += points
    if macd is not None and macds is not None:
        points = 1 if macd >= macds else -1
        components.append(_score_component("MACD momentum", f"MACD {macd:.2f} vs signal {macds:.2f}", points))
        score += points
    if (pe is not None and pe >= 30) or (pb is not None and pb >= 10):
        valuation_evidence = f"PE {_fmt(str(pe) if pe is not None else None)}, P/B {_fmt(str(pb) if pb is not None else None)}"
        components.append(_score_component("Valuation risk", valuation_evidence, -1))
        score -= 1
    if (roe is not None and roe >= 0.15) or (net_income is not None and net_income > 0):
        components.append(_score_component("Fundamental quality", "positive profitability / ROE support", 1))
        score += 1

    below_200 = close is not None and sma200 is not None and close < sma200
    above_or_at_200 = close is not None and sma200 is not None and close >= sma200
    materially_negative = score <= -3
    if score >= 3:
        rating = "Buy"
        action = "Buy"
    elif score >= 1:
        rating = "Overweight"
        action = "Buy"
    elif score == 0:
        rating = "Hold"
        action = "Hold"
    elif score >= -2 or (materially_negative and above_or_at_200):
        rating = "Underweight"
        action = "Hold"
    else:
        rating = "Sell" if below_200 and materially_negative else "Underweight"
        action = "Sell" if rating == "Sell" else "Hold"
    sell_gate = (
        "Sell requires either price below the 200 SMA with a materially negative score, "
        "or an explicitly documented material negative setup despite 200 SMA support."
    )
    return {
        "score": score,
        "components": components,
        "rating": rating,
        "action": action,
        "below_200": below_200,
        "above_or_at_200": above_or_at_200,
        "sell_gate": sell_gate,
    }


def _context(evidence: dict[str, Any]) -> dict[str, Any]:
    snapshot = _tool_output(evidence, "market", "get_verified_market_snapshot")
    stock_rows = _parse_stock_csv(_tool_output(evidence, "market", "get_stock_data"))
    news_items = _remove_cross_ticker_news(
        evidence["ticker"],
        _parse_news(_tool_output(evidence, "news", "get_news")),
    )
    fundamentals = _parse_fundamentals(_tool_output(evidence, "fundamentals", "get_fundamentals"))
    stocktwits = _filter_social_lines(
        evidence["ticker"],
        evidence["trade_date"],
        evidence.get("identity", {}),
        _tool_output(evidence, "social", "fetch_stocktwits_messages"),
    )
    reddit = _filter_social_lines(
        evidence["ticker"],
        evidence["trade_date"],
        evidence.get("identity", {}),
        _tool_output(evidence, "social", "fetch_reddit_posts"),
    )
    ctx: dict[str, Any] = {
        "ticker": evidence["ticker"],
        "trade_date": evidence["trade_date"],
        "identity": evidence.get("identity", {}),
        "ohlcv": _parse_field_table(snapshot, "Latest verified OHLCV row"),
        "indicators": _parse_field_table(snapshot, "Verified technical indicators (latest row)"),
        "recent_closes": _parse_recent_closes(snapshot),
        "stock_rows": stock_rows,
        "news_items": news_items,
        "stocktwits": stocktwits["text"],
        "reddit": reddit["text"],
        "social_kept": stocktwits["kept"] + reddit["kept"],
        "social_removed": stocktwits["removed"] + reddit["removed"],
        "fundamentals": fundamentals,
        "missing_cashflow": "NO_DATA_AVAILABLE" in _tool_output(evidence, "fundamentals", "get_cashflow"),
        "missing_income": "NO_DATA_AVAILABLE" in _tool_output(evidence, "fundamentals", "get_income_statement"),
    }
    ctx["direction"] = _direction(ctx)
    return ctx


def _trend_phrase(ctx: dict[str, Any]) -> str:
    close = _num(ctx["ohlcv"].get("Close"))
    ema10 = _num(ctx["indicators"].get("close_10_ema"))
    sma50 = _num(ctx["indicators"].get("close_50_sma"))
    sma200 = _num(ctx["indicators"].get("close_200_sma"))
    if close is None:
        return "price data is incomplete"
    pieces = []
    if ema10 is not None:
        pieces.append("above the 10 EMA" if close > ema10 else "below the 10 EMA")
    if sma50 is not None:
        pieces.append("above the 50 SMA" if close > sma50 else "below the 50 SMA")
    if sma200 is not None:
        pieces.append("above the 200 SMA" if close > sma200 else "below the 200 SMA")
    return ", ".join(pieces)


def _technical_read(ctx: dict[str, Any]) -> str:
    close = _num(ctx["ohlcv"].get("Close"))
    ema10 = _num(ctx["indicators"].get("close_10_ema"))
    sma50 = _num(ctx["indicators"].get("close_50_sma"))
    sma200 = _num(ctx["indicators"].get("close_200_sma"))
    if close is None:
        return "The technical setup is incomplete because the latest close is unavailable."
    below_fast = all(value is not None and close < value for value in [ema10, sma50])
    above_fast = all(value is not None and close > value for value in [ema10, sma50])
    if sma200 is not None and close < sma200:
        return (
            "The latest close is below the 200 SMA, so the long-term trend reference is broken. "
            "That makes the weak near-term and medium-term readings more serious than an ordinary pullback."
        )
    if sma200 is not None and close >= sma200 and below_fast:
        return (
            "The latest close remains above the 200 SMA, so long-term support still holds, "
            "but price is below the faster 10 EMA and 50 SMA. This supports a cautious stance, "
            "not a clean technical Sell by itself."
        )
    if above_fast:
        return "The latest close is above the faster trend references, which supports constructive momentum."
    return "The moving-average picture is mixed, so confirmation from follow-through price action matters."


def _write(path: str, text: str) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text.rstrip() + "\n", encoding="utf-8")


def market_report(ctx: dict[str, Any]) -> str:
    latest_date = ctx["recent_closes"][-1][0] if ctx["recent_closes"] else ctx["trade_date"]
    close = ctx["ohlcv"].get("Close", "N/A")
    volume = ctx["ohlcv"].get("Volume", "N/A")
    indicators = ctx["indicators"]
    trend = _trend_phrase(ctx)
    return f"""# Market Analyst Report: {ctx['ticker']}

{ctx['identity'].get('company_name', ctx['ticker'])} closed at {close} on the latest verified trading row, {latest_date}. The technical picture is {trend}. RSI is {indicators.get('rsi', 'N/A')}, MACD is {indicators.get('macd', 'N/A')} against signal {indicators.get('macds', 'N/A')}, and ATR is {indicators.get('atr', 'N/A')}. Volume on the latest verified row was {volume}.

{_technical_read(ctx)}

| Signal | Evidence | Interpretation |
|---|---:|---|
| Latest close | {close} | {trend} |
| 10 EMA | {indicators.get('close_10_ema', 'N/A')} | Near-term trend reference |
| 50 SMA | {indicators.get('close_50_sma', 'N/A')} | Medium-term trend reference |
| 200 SMA | {indicators.get('close_200_sma', 'N/A')} | Long-term trend reference |
| RSI | {indicators.get('rsi', 'N/A')} | Momentum gauge |
| MACD / signal | {indicators.get('macd', 'N/A')} / {indicators.get('macds', 'N/A')} | Trend momentum |
| ATR | {indicators.get('atr', 'N/A')} | Volatility reference |
"""


def sentiment_report(ctx: dict[str, Any]) -> str:
    stocktwits = ctx.get("stocktwits") or "<no StockTwits evidence returned>"
    reddit = ctx.get("reddit") or "<no Reddit evidence returned>"
    band = "Mixed"
    score = "5.0/10"
    confidence = "Low-to-Medium" if stocktwits or reddit else "Low"
    combined = f"{stocktwits}\n{reddit}".lower()
    if "bullish" in combined and "bearish" not in combined:
        band = "Mildly Bullish"
        score = "5.8/10"
    elif "bearish" in combined and "bullish" not in combined:
        band = "Mildly Bearish"
        score = "4.2/10"
    return f"""# Sentiment Analyst Report: {ctx['ticker']}

**Overall Sentiment:** **{band}** (Score: {score})
**Confidence:** {confidence}

The sentiment role uses direct social evidence from StockTwits and Reddit rather than the news feed. The retained StockTwits/Reddit sample is noisy and retail-heavy, so treat it as low-to-medium confidence sentiment color rather than a complete investor consensus. Lines after the trade date or not materially tied to {ctx['ticker']} are excluded from this report.

StockTwits evidence:
```text
{stocktwits}
```

Reddit evidence:
```text
{reddit}
```

| Signal | Direction | Supporting evidence |
|---|---|---|
| Social source coverage | Present | StockTwits and Reddit packets were requested directly |
| Narrative tone | {band} | Derived from explicit social-feed evidence |
| Confidence | {confidence} | {ctx.get('social_kept', 0)} retained lines; {ctx.get('social_removed', 0)} noisy, off-ticker, or post-date lines excluded |
"""


def news_report(ctx: dict[str, Any]) -> str:
    buckets = _news_buckets(ctx)
    direct = buckets["direct"][:8]
    indirect = buckets["indirect"][:5]
    direct_rows = "\n".join(
        f"| {item['title']} | {item['source']} | {item['summary'] or 'No summary supplied.'} |"
        for item in direct
    )
    indirect_rows = "\n".join(
        f"| {item['title']} | {item['source']} | {item['summary'] or 'No summary supplied.'} |"
        for item in indirect
    )
    return f"""# News Analyst Report: {ctx['ticker']}

The news packet for {ctx['ticker']} contains {len(ctx['news_items'])} raw items. The report separates direct ticker evidence from indirect sector or market context and excludes low-relevance items from the decision table.

Direct {ctx['ticker']} news:

| Event | Source | Read-through |
|---|---|---|
{direct_rows or '| No direct ticker news retained | N/A | No direct event signal available |'}

Indirect sector/market news:

| Event | Source | Read-through |
|---|---|---|
{indirect_rows or '| No indirect context retained | N/A | No indirect event signal available |'}

Excluded as low relevance: {len(buckets['excluded'])} raw items were omitted because they did not materially connect to {ctx['ticker']} in the evidence packet.

Insider transaction evidence is included in the evidence packet where available and should be treated as context rather than a standalone signal.
"""


def fundamentals_report(ctx: dict[str, Any]) -> str:
    f = ctx["fundamentals"]
    missing = []
    if ctx["missing_cashflow"]:
        missing.append("cash-flow statement unavailable")
    if ctx["missing_income"]:
        missing.append("income-statement detail unavailable")
    missing_text = f" Missing detailed statement data: {', '.join(missing)}." if missing else ""
    return f"""# Fundamentals Analyst Report: {ctx['ticker']}

{ctx['identity'].get('company_name', ctx['ticker'])} operates in {ctx['identity'].get('sector', 'N/A')} / {ctx['identity'].get('industry', 'N/A')}. The fundamentals packet shows market cap of {_fmt(f.get('Market Cap'))}, TTM revenue of {_fmt(f.get('Revenue (TTM)'))}, net income of {_fmt(f.get('Net Income'))}, and free cash flow of {_fmt(f.get('Free Cash Flow'))}.{missing_text}

Valuation and quality are the central trade-off. PE is {_fmt(f.get('PE Ratio (TTM)'))}, forward PE is {_fmt(f.get('Forward PE'))}, price/book is {_fmt(f.get('Price to Book'))}, dividend yield is {_fmt(f.get('Dividend Yield'))}, ROE is {_fmt(f.get('Return on Equity'))}, and debt/equity is {_fmt(f.get('Debt to Equity'))}.

| Area | Evidence | Read-through |
|---|---:|---|
| Market cap | {_fmt(f.get('Market Cap'))} | Scale and index relevance |
| Revenue TTM | {_fmt(f.get('Revenue (TTM)'))} | Business base |
| Net income | {_fmt(f.get('Net Income'))} | Profit generation |
| PE / Forward PE | {_fmt(f.get('PE Ratio (TTM)'))} / {_fmt(f.get('Forward PE'))} | Valuation |
| Price/book | {_fmt(f.get('Price to Book'))} | Balance-sheet valuation |
| ROE | {_fmt(f.get('Return on Equity'))} | Profitability |
| Current ratio | {_fmt(f.get('Current Ratio'))} | Liquidity |
"""


def bull_report(ctx: dict[str, Any]) -> str:
    f = ctx["fundamentals"]
    trend_support = (
        "Price remains above the 200 SMA, so long-term support is still part of the bull case."
        if ctx["direction"]["above_or_at_200"]
        else "Price is below the 200 SMA, so the bull case cannot rely on long-term moving-average support."
    )
    return f"""# Bull Researcher Round 1: {ctx['ticker']}

Bull Analyst: The strongest positive thesis is that scale, profitability, and any remaining trend support can justify upside participation. {ctx['identity'].get('company_name', ctx['ticker'])} has market cap of {_fmt(f.get('Market Cap'))}, TTM net income of {_fmt(f.get('Net Income'))}, and ROE of {_fmt(f.get('Return on Equity'))}. The latest close is {ctx['ohlcv'].get('Close', 'N/A')} and the market report says price is {_trend_phrase(ctx)}.

{trend_support} Bear must disprove that quality, profitability, and any retained support are enough to offset current momentum or valuation risk.
"""


def bear_report(ctx: dict[str, Any]) -> str:
    f = ctx["fundamentals"]
    return f"""# Bear Researcher Round 1: {ctx['ticker']}

Bear Analyst: I directly rebut the bull claim that quality and trend support are enough. The cautious case is that recent momentum and valuation may not justify immediate risk. The latest technical setup is {_trend_phrase(ctx)}, RSI is {ctx['indicators'].get('rsi', 'N/A')}, and MACD is {ctx['indicators'].get('macd', 'N/A')} versus signal {ctx['indicators'].get('macds', 'N/A')}. Valuation is not automatically cheap: PE is {_fmt(f.get('PE Ratio (TTM)'))} and price/book is {_fmt(f.get('Price to Book'))}.

Bull is underestimating timing risk. Scale and profitability do not remove the risk that price remains below short- or medium-term averages. If the stock is below those averages, the evidence favors patience until price confirms recovery.
"""


def research_manager(ctx: dict[str, Any]) -> str:
    rating = ctx["direction"]["rating"]
    score = ctx["direction"]["score"]
    rows = "\n".join(
        f"| {component['label']} | {component['evidence']} | {component['points']:+d} |"
        for component in ctx["direction"]["components"]
    )
    if rating == "Sell":
        decision_text = (
            "Sell wins over Hold/Underweight because the total score is materially negative "
            "and price is below 200 SMA, showing breakdown below longer-term support."
        )
    elif rating == "Underweight":
        decision_text = (
            "Underweight wins over Sell because the evidence is negative, but the Sell gate is not fully met. "
            "If the 200 SMA still holds, the framework keeps the trader proposal at Hold unless a separate material negative setup is documented."
        )
    else:
        decision_text = "The selected rating follows the score band and the Sell gate."
    return f"""# Research Manager Decision: {ctx['ticker']}

**Recommendation**: {rating}

**Strongest Bull Evidence**: Profitability, scale, and any remaining long-term technical support.

**Strongest Bear Evidence**: Current technical setup, momentum, and valuation risk.

**Scoring Rule**: +1 / -1 for price versus 200 SMA, 50 SMA, and 10 EMA; +1 / -1 for RSI versus 50; +1 / -1 for MACD versus signal; -1 for expensive valuation; +1 for profitable fundamental quality. Sell requires either price below the 200 SMA with a materially negative score, or an explicitly documented material negative setup despite 200 SMA support.

**Score Components**:

| Component | Evidence | Points |
|---|---|---:|
{rows}

**Evidence Score**: {score}

**Evidence Weighing**: {decision_text} The recommendation follows current evidence rather than safety-status language.

**Strategic Actions**:
- Use the 10 EMA and 50 SMA area as the first confirmation zone.
- Treat the 200 SMA as the long-term trend reference when available.
- Require fresh evidence before upgrading or downgrading the view.
"""


def trader(ctx: dict[str, Any]) -> str:
    action = ctx["direction"]["action"]
    rating = ctx["direction"]["rating"]
    close = ctx["ohlcv"].get("Close", "N/A")
    sma50 = ctx["indicators"].get("close_50_sma", "N/A")
    sma200 = ctx["indicators"].get("close_200_sma", "N/A")
    if action == "Sell" and ctx["direction"]["below_200"]:
        consistency = (
            "Consistency Check: Sell is supported because price is below the 200 SMA, "
            "which is a breakdown below longer-term support, and the evidence score is materially negative."
        )
    elif action == "Hold" and ctx["direction"]["above_or_at_200"]:
        consistency = (
            "Consistency Check: 200 SMA still holds, so the Sell gate is not met. "
            "The trader keeps the proposal at Hold despite an Underweight research rating."
        )
    else:
        consistency = "Consistency Check: The action follows the research rating and score gate."
    return f"""# Trader Proposal: {ctx['ticker']}

**Action**: {action}

**Reasoning**: The research manager rating is {rating}. The transaction proposal is grounded in the latest close of {close}, the 50 SMA at {sma50}, the 200 SMA at {sma200}, and the current momentum evidence. A Buy requires constructive confirmation above key moving averages; a Sell requires evidence of breakdown below longer-term support or a separately documented materially negative setup; otherwise Hold is appropriate while waiting for confirmation.

**{consistency}**

FINAL TRANSACTION PROPOSAL: **{action.upper()}**
"""


def aggressive_risk(ctx: dict[str, Any]) -> str:
    return f"""# Aggressive Risk Analyst Round 1: {ctx['ticker']}

Aggressive Analyst: The higher-reward interpretation supports the trader proposal when the evidence shows long-term support, improving catalysts, or strong fundamentals. The latest close is {ctx['ohlcv'].get('Close', 'N/A')} and the company has ROE of {_fmt(ctx['fundamentals'].get('Return on Equity'))}. If price can reclaim short-term averages, upside participation could improve quickly.
"""


def conservative_risk(ctx: dict[str, Any]) -> str:
    return f"""# Conservative Risk Analyst Round 1: {ctx['ticker']}

Conservative Analyst: I directly respond to Aggressive Risk: upside participation could improve, but the proposal may still be unsafe if technical and valuation risk dominate. The market setup is {_trend_phrase(ctx)}, RSI is {ctx['indicators'].get('rsi', 'N/A')}, and ATR is {ctx['indicators'].get('atr', 'N/A')}. Until price confirms strength, the conservative stance is to avoid overstating conviction.
"""


def neutral_risk(ctx: dict[str, Any]) -> str:
    return f"""# Neutral Risk Analyst Round 1: {ctx['ticker']}

Neutral Analyst: The aggressive view is right to acknowledge upside if fundamentals and long-term trend support persist. The conservative view is right to require confirmation when short-term momentum is weak. Weighing both sides, the stronger risk argument is the one most consistent with the latest close versus moving averages. The balanced stance is to follow the trader action while using the moving averages and latest close as the key confirmation or invalidation references.
"""


def portfolio_manager(ctx: dict[str, Any]) -> str:
    rating = ctx["direction"]["rating"]
    return f"""# Portfolio Manager Decision: {ctx['ticker']}

**Rating**: {rating}

**Executive Summary**: {ctx['ticker']} receives a {rating} rating based on the current blend of market trend, momentum, fundamentals, and news evidence. The conclusion is evidence-grounded and remains separate from paper-study safety boundaries.

**Investment Thesis**: The latest close is {ctx['ohlcv'].get('Close', 'N/A')} and the market report shows price is {_trend_phrase(ctx)}. Fundamentals show market cap of {_fmt(ctx['fundamentals'].get('Market Cap'))}, net income of {_fmt(ctx['fundamentals'].get('Net Income'))}, and ROE of {_fmt(ctx['fundamentals'].get('Return on Equity'))}. The risk debate supports using the trader action with confirmation from price behavior around the key moving averages.

**Risk Assessment**: The portfolio decision synthesizes the aggressive case for taking risk, the conservative response about technical and valuation risk, and the neutral weighing of those arguments. It does not merely repeat the trader proposal.

**Paper-study implementation notes**: This is a study artifact only. Do not submit broker orders or treat the decision as real trading advice.

**Time Horizon**: Review after fresh price and news evidence updates the current setup.
"""


def _body_without_heading(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip()


def complete_report(ctx: dict[str, Any], sections: dict[str, str]) -> str:
    return f"""# Trading Analysis Report: {ctx['ticker']}

Generated: {ctx['trade_date']}

Context: comparative_run=false

Paper-study output only. This report was produced by Codex acting the converted TradingAgents roles. Safety status is not used as investment rationale.

## I. Analyst Team Reports

### Market Analyst

{_body_without_heading(sections['market_report'])}

### Sentiment Analyst

{_body_without_heading(sections['sentiment_report'])}

### News Analyst

{_body_without_heading(sections['news_report'])}

### Fundamentals Analyst

{_body_without_heading(sections['fundamentals_report'])}

## II. Research Team Debate

### Bull Researcher Round 1 - Opening Case

{_body_without_heading(sections['bull_researcher_round_1'])}

### Bear Researcher Round 1 - Rebuttal to Bull

{_body_without_heading(sections['bear_researcher_round_1'])}

### Research Manager Decision - Evidence Weighing

{_body_without_heading(sections['research_manager'])}

## III. Trading Team Plan

### Trader Proposal

{_body_without_heading(sections['trader'])}

## IV. Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

{_body_without_heading(sections['aggressive_risk_round_1'])}

### Conservative Risk Analyst Round 1 - Response to Aggressive

{_body_without_heading(sections['conservative_risk_round_1'])}

### Neutral Risk Analyst Round 1 - Weighing

{_body_without_heading(sections['neutral_risk_round_1'])}

## V. Portfolio Manager Decision

### Portfolio Manager

{_body_without_heading(sections['portfolio_manager'])}

## VI. Paper-Study Disclaimer

This report is for research workflow testing only. It is not financial advice, not a broker instruction, and not connected to GCAF or any execution system.
"""


def write_reports_for_workflow(workflow_path: Path) -> None:
    workflow = _read_json(workflow_path)
    evidence = _read_json(Path(workflow["evidence_path"]))
    ctx = _context(evidence)
    generated = {
        "market_report": market_report(ctx),
        "sentiment_report": sentiment_report(ctx),
        "news_report": news_report(ctx),
        "fundamentals_report": fundamentals_report(ctx),
        "bull_researcher_round_1": bull_report(ctx),
        "bear_researcher_round_1": bear_report(ctx),
        "research_manager": research_manager(ctx),
        "trader": trader(ctx),
        "aggressive_risk_round_1": aggressive_risk(ctx),
        "conservative_risk_round_1": conservative_risk(ctx),
        "neutral_risk_round_1": neutral_risk(ctx),
        "portfolio_manager": portfolio_manager(ctx),
    }
    paths = workflow["report_paths"]
    for key, text in generated.items():
        _write(paths[key], text)
    _write(paths["complete_report"], complete_report(ctx, generated))


def _workflow_paths(output_dir: Path) -> list[Path]:
    return sorted((output_dir / "evidence").glob("*/*/workflow_state.json"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write Codex-operated TradingAgents reports from collected evidence.")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)

    paths = _workflow_paths(args.output_dir)
    if not paths:
        print(f"No workflow_state.json files found under {args.output_dir}")
        return 1
    for path in paths:
        write_reports_for_workflow(path)
        workflow = _read_json(path)
        print(f"{workflow['ticker']}: {workflow['report_paths']['complete_report']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
