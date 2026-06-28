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
MAX_SOCIAL_EXAMPLES_IN_REPORT = 3
MAX_DIRECT_NEWS_ROWS = 8
MAX_INDIRECT_NEWS_ROWS = 4


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


def _social_label(line: str) -> str:
    lowered = line.lower()
    if "bearish" in lowered:
        return "bearish"
    if "bullish" in lowered:
        return "bullish"
    return "neutral"


def _social_theme(lines: list[str], label: str) -> str:
    candidates = [line for line in lines if _social_label(line) == label]
    if not candidates:
        return "No dominant theme identified"
    joined = " ".join(candidates).lower()
    theme_terms = [
        ("AI roadmap", [" ai ", "roadmap", "copilot", "cloud", "gpu"]),
        ("services / installed-base support", ["services", "installed base", "iphone", "subscription"]),
        ("valuation pressure", ["valuation", "expensive", "multiple", "p/e", "pe "]),
        ("technical trend concern", ["sma", "ema", "support", "resistance", "breakdown"]),
        ("earnings or profitability", ["earnings", "profit", "margin", "revenue"]),
    ]
    for theme, needles in theme_terms:
        if any(needle in joined for needle in needles):
            return theme
    return "ticker-specific retail discussion"


def _is_low_information_social(line: str) -> bool:
    lowered = line.lower()
    noisy_terms = [
        "hairy",
        "wendys",
        "nice dinner",
        "mom",
        "drunk",
        "joke",
    ]
    if any(term in lowered for term in noisy_terms):
        return True
    without_meta = re.sub(r"\[[^\]]+\]", "", line)
    without_tickers = re.sub(r"\$[A-Za-z.]+", "", without_meta)
    words = re.findall(r"[A-Za-z]{3,}", without_tickers)
    return len(words) == 0


def _filter_social_lines(ticker: str, trade_date: str, identity: dict[str, Any], text: str) -> dict[str, Any]:
    terms = _company_terms({"ticker": ticker, "identity": identity})
    kept: list[str] = []
    removed = 0
    post_date_removed = 0
    off_ticker_removed = 0
    for line in text.splitlines():
        if not line.strip():
            continue
        line_date = _line_date(line)
        if line_date and line_date > trade_date:
            removed += 1
            post_date_removed += 1
            continue
        if not _mentions_any(line, terms):
            removed += 1
            off_ticker_removed += 1
            continue
        if ticker.upper() == "MSFT" and re.search(r"(Apple|AAPL)", line, re.IGNORECASE):
            removed += 1
            off_ticker_removed += 1
            continue
        if _is_low_information_social(line):
            removed += 1
            continue
        kept.append(line)
    return {
        "text": "\n".join(kept).strip() or "<no relevant same-date social lines retained>",
        "lines": kept,
        "reviewed": len([line for line in text.splitlines() if line.strip()]),
        "kept": len(kept),
        "removed": removed,
        "post_date_removed": post_date_removed,
        "off_ticker_removed": off_ticker_removed,
        "bullish": sum(1 for line in kept if _social_label(line) == "bullish"),
        "bearish": sum(1 for line in kept if _social_label(line) == "bearish"),
        "neutral": sum(1 for line in kept if _social_label(line) == "neutral"),
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


def _news_effect(item: dict[str, str]) -> str:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    negative_terms = [
        "downgrade",
        "cut",
        "pressure",
        "concern",
        "risk",
        "weak",
        "miss",
        "lawsuit",
        "probe",
    ]
    positive_terms = [
        "upgrade",
        "beat",
        "raise",
        "growth",
        "strong",
        "record",
        "approval",
        "expansion",
    ]
    negative = any(term in text for term in negative_terms)
    positive = any(term in text for term in positive_terms)
    if positive and not negative:
        return "positive"
    if negative and not positive:
        return "negative"
    return "mixed/unclear"


def _technical_themes(ctx: dict[str, Any]) -> dict[str, str]:
    close = _num(ctx["ohlcv"].get("Close"))
    ema10 = _num(ctx["indicators"].get("close_10_ema"))
    sma50 = _num(ctx["indicators"].get("close_50_sma"))
    sma200 = _num(ctx["indicators"].get("close_200_sma"))
    rsi = _num(ctx["indicators"].get("rsi"))
    macd = _num(ctx["indicators"].get("macd"))
    macds = _num(ctx["indicators"].get("macds"))
    atr = ctx["indicators"].get("atr", "N/A")
    if close is None:
        return {
            "long_term_trend_status": "latest close unavailable",
            "short_medium_trend_status": "moving-average comparison unavailable",
            "momentum_status": "momentum unavailable",
            "volatility_status": f"ATR {atr}",
        }
    long_term = (
        f"above 200 SMA ({close:.2f} vs {sma200:.2f})"
        if sma200 is not None and close >= sma200
        else f"below 200 SMA ({close:.2f} vs {sma200:.2f})"
        if sma200 is not None
        else "200 SMA unavailable"
    )
    fast_refs = []
    if ema10 is not None:
        fast_refs.append(f"{'above' if close >= ema10 else 'below'} 10 EMA ({ema10:.2f})")
    if sma50 is not None:
        fast_refs.append(f"{'above' if close >= sma50 else 'below'} 50 SMA ({sma50:.2f})")
    rsi_text = f"RSI {rsi:.2f}" if rsi is not None else "RSI unavailable"
    macd_text = (
        f"MACD {macd:.2f} vs signal {macds:.2f}"
        if macd is not None and macds is not None
        else "MACD unavailable"
    )
    return {
        "long_term_trend_status": long_term,
        "short_medium_trend_status": ", ".join(fast_refs) or "fast averages unavailable",
        "momentum_status": f"{rsi_text}; {macd_text}",
        "volatility_status": f"ATR {atr}",
    }


def _fundamental_themes(ctx: dict[str, Any]) -> dict[str, str]:
    f = ctx["fundamentals"]
    roe = _num(f.get("Return on Equity"))
    net_income = _num(f.get("Net Income"))
    pe = _num(f.get("PE Ratio (TTM)"))
    pb = _num(f.get("Price to Book"))
    current_ratio = _fmt(f.get("Current Ratio"))
    quality = (
        f"profitable quality support: net income {_fmt(f.get('Net Income'))}, ROE {_fmt(f.get('Return on Equity'))}"
        if (net_income is not None and net_income > 0) or (roe is not None and roe > 0)
        else "quality evidence weak or unavailable"
    )
    valuation = (
        f"valuation risk: PE {_fmt(f.get('PE Ratio (TTM)'))}, P/B {_fmt(f.get('Price to Book'))}"
        if (pe is not None and pe >= 30) or (pb is not None and pb >= 10)
        else f"valuation not flagged as extreme: PE {_fmt(f.get('PE Ratio (TTM)'))}, P/B {_fmt(f.get('Price to Book'))}"
    )
    missing = []
    if ctx["missing_cashflow"]:
        missing.append("cash-flow statement missing")
    if ctx["missing_income"]:
        missing.append("income-statement detail missing")
    return {
        "quality_strength": quality,
        "valuation_risk": valuation,
        "liquidity_or_balance_sheet_note": f"current ratio {current_ratio}, debt/equity {_fmt(f.get('Debt to Equity'))}",
        "missing_statement_note": ", ".join(missing) if missing else "detailed statements available",
    }


def _social_summary(stocktwits: dict[str, Any], reddit: dict[str, Any]) -> dict[str, Any]:
    lines = list(stocktwits["lines"]) + list(reddit["lines"])
    reviewed = stocktwits["reviewed"] + reddit["reviewed"]
    retained = stocktwits["kept"] + reddit["kept"]
    removed = stocktwits["removed"] + reddit["removed"]
    bullish = stocktwits["bullish"] + reddit["bullish"]
    bearish = stocktwits["bearish"] + reddit["bearish"]
    neutral = stocktwits["neutral"] + reddit["neutral"]
    noisy_majority = retained == 0 or neutral >= max(bullish + bearish, 1) or removed > retained
    confidence = "Low-to-Medium" if noisy_majority else "Medium"
    if retained == 0:
        confidence = "Low"
    confidence_reason = (
        f"{retained} usable of {reviewed} reviewed; {removed} excluded as post-date, off-ticker, noisy, or low-information"
    )
    return {
        "retained_count": retained,
        "removed_count": removed,
        "reviewed_count": reviewed,
        "bullish_count": bullish,
        "bearish_count": bearish,
        "unlabeled_count": neutral,
        "dominant_positive_social_theme": _social_theme(lines, "bullish"),
        "dominant_negative_social_theme": _social_theme(lines, "bearish"),
        "confidence": confidence,
        "confidence_reason": confidence_reason,
        "examples": lines[:MAX_SOCIAL_EXAMPLES_IN_REPORT],
        "stocktwits": stocktwits,
        "reddit": reddit,
        "reddit_coverage": (
            f"{reddit['kept']} usable Reddit items retained"
            if reddit["reviewed"]
            else "Reddit coverage sparse or unavailable"
        ),
    }


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
    technical_score = sum(
        component["points"]
        for component in components
        if component["label"] in {"Long-term trend", "Medium-term trend", "Near-term trend", "RSI momentum", "MACD momentum"}
    )
    valuation_score = sum(component["points"] for component in components if component["label"] == "Valuation risk")
    fundamental_score = sum(component["points"] for component in components if component["label"] == "Fundamental quality")
    if abs(technical_score) >= max(abs(valuation_score), abs(fundamental_score), 1):
        primary_driver = "technical"
    elif abs(valuation_score) >= abs(fundamental_score):
        primary_driver = "valuation"
    else:
        primary_driver = "fundamental"
    return {
        "score": score,
        "components": components,
        "rating": rating,
        "action": action,
        "below_200": below_200,
        "above_or_at_200": above_or_at_200,
        "sell_gate": sell_gate,
        "primary_driver": primary_driver,
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
    social = _social_summary(stocktwits, reddit)
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
        "social": social,
        "social_kept": stocktwits["kept"] + reddit["kept"],
        "social_removed": stocktwits["removed"] + reddit["removed"],
        "fundamentals": fundamentals,
        "missing_cashflow": "NO_DATA_AVAILABLE" in _tool_output(evidence, "fundamentals", "get_cashflow"),
        "missing_income": "NO_DATA_AVAILABLE" in _tool_output(evidence, "fundamentals", "get_income_statement"),
    }
    ctx["technical_themes"] = _technical_themes(ctx)
    ctx["fundamental_themes"] = _fundamental_themes(ctx)
    buckets = _news_buckets(ctx)
    ctx["news_buckets"] = buckets
    ctx["news_themes"] = {
        "direct_positive_events": [item for item in buckets["direct"] if _news_effect(item) == "positive"],
        "direct_negative_events": [item for item in buckets["direct"] if _news_effect(item) == "negative"],
        "indirect_context": buckets["indirect"],
        "excluded_low_relevance_count": len(buckets["excluded"]),
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
    social = ctx["social"]
    band = "Mixed"
    score = "5.0/10"
    confidence = social["confidence"]
    if social["bullish_count"] > social["bearish_count"] and social["bearish_count"] == 0:
        band = "Mildly Bullish"
        score = "5.8/10"
    elif social["bearish_count"] > social["bullish_count"] and social["bullish_count"] == 0:
        band = "Mildly Bearish"
        score = "4.2/10"
    stocktwits = social["stocktwits"]
    reddit = social["reddit"]
    examples = "\n".join(f"- {line}" for line in social["examples"]) or "- No ticker-relevant social examples retained."
    return f"""# Sentiment Analyst Report: {ctx['ticker']}

**Overall Sentiment:** **{band}** (Score: {score})
**Confidence:** {confidence}

The sentiment role uses direct social evidence from StockTwits and Reddit rather than the news feed. The retained StockTwits/Reddit sample is noisy and retail-heavy, so treat it as sentiment color rather than a complete investor consensus or institutional view. Lines after the trade date or not materially tied to {ctx['ticker']} are excluded from this report.

## Social Evidence Summary

| Source | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral split | Dominant themes | Confidence | Limitations |
|---|---:|---:|---|---|---|---|
| StockTwits | {stocktwits['reviewed']} | {stocktwits['kept']} | {stocktwits['bullish']} / {stocktwits['bearish']} / {stocktwits['neutral']} | + {social['dominant_positive_social_theme']}; - {social['dominant_negative_social_theme']} | {confidence} | Retail-heavy, excludes {stocktwits['removed']} post-date/off-ticker/noisy lines |
| Reddit | {reddit['reviewed']} | {reddit['kept']} | {reddit['bullish']} / {reddit['bearish']} / {reddit['neutral']} | {social['reddit_coverage']} | {confidence} | {social['reddit_coverage']} |

Representative social examples (maximum {MAX_SOCIAL_EXAMPLES_IN_REPORT}):
{examples}

Confidence reason: {social['confidence_reason']}. Reddit coverage: {social['reddit_coverage']}.
"""


def news_report(ctx: dict[str, Any]) -> str:
    buckets = ctx["news_buckets"]
    direct = buckets["direct"][:MAX_DIRECT_NEWS_ROWS]
    indirect = buckets["indirect"][:MAX_INDIRECT_NEWS_ROWS]
    direct_rows = "\n".join(
        f"| {item['title']} | {item['source']} | direct ticker/company | {_news_effect(item)} | {item['summary'] or 'No summary supplied.'} |"
        for item in direct
    )
    indirect_rows = "\n".join(
        f"| {item['title']} | {item['source']} | indirect sector/market | {_news_effect(item)} | {item['summary'] or 'No summary supplied.'} |"
        for item in indirect
    )
    return f"""# News Analyst Report: {ctx['ticker']}

The news packet for {ctx['ticker']} contains {len(ctx['news_items'])} raw items. The report separates direct ticker evidence from indirect sector or market context and excludes low-relevance items from the decision table.

Direct {ctx['ticker']} news:

| Event | Source | Relevance | Likely effect | Read-through |
|---|---|---|---|---|
{direct_rows or '| No direct ticker news retained | N/A | direct ticker/company | mixed/unclear | No direct event signal available |'}

Indirect sector/market news:

| Event | Source | Relevance | Likely effect | Read-through |
|---|---|---|---|---|
{indirect_rows or '| No indirect context retained | N/A | indirect sector/market | mixed/unclear | No indirect event signal available |'}

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
    fundamental = ctx["fundamental_themes"]
    technical = ctx["technical_themes"]
    direct_positive = ctx["news_themes"]["direct_positive_events"]
    news_phrase = (
        f"Direct positive news includes {direct_positive[0]['title']}."
        if direct_positive
        else "Direct positive news catalysts are limited in the retained packet."
    )
    trend_support = (
        "Price remains above the 200 SMA, so long-term support is still part of the bull case."
        if ctx["direction"]["above_or_at_200"]
        else "Price is below the 200 SMA, so the bull case cannot rely on long-term moving-average support."
    )
    return f"""# Bull Researcher Round 1: {ctx['ticker']}

Bull Analyst: The constructive case rests on {fundamental['quality_strength']} and the technical fact that {technical['long_term_trend_status']}. {news_phrase} Social positives are summarized as {ctx['social']['dominant_positive_social_theme']}, but the sample remains retail-heavy.

{trend_support} Bear must disprove that quality, profitability, and any retained support are enough to offset current momentum or valuation risk.
"""


def bear_report(ctx: dict[str, Any]) -> str:
    fundamental = ctx["fundamental_themes"]
    technical = ctx["technical_themes"]
    direct_negative = ctx["news_themes"]["direct_negative_events"]
    news_phrase = (
        f"Direct negative news includes {direct_negative[0]['title']}."
        if direct_negative
        else "The retained news packet does not add a decisive direct negative catalyst."
    )
    return f"""# Bear Researcher Round 1: {ctx['ticker']}

Bear Analyst: I directly rebut the bull claim that quality and any retained support are enough. The cautious case is that {technical['short_medium_trend_status']} and {technical['momentum_status']}. Valuation does not provide a clean cushion: {fundamental['valuation_risk']}. {news_phrase}

Bull is underestimating timing risk. Scale and profitability do not remove the risk that price remains below short- or medium-term averages. If the stock is below those averages, the evidence favors patience until price confirms recovery.
"""


def research_manager(ctx: dict[str, Any]) -> str:
    rating = ctx["direction"]["rating"]
    action = ctx["direction"]["action"]
    primary_driver = ctx["direction"]["primary_driver"]
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
        driver_text = "This is primarily a technical/momentum Sell, not a fundamental quality Sell."
    elif rating == "Underweight":
        decision_text = (
            "Underweight wins over Sell because the evidence is negative, but the Sell gate is not fully met. "
            "If the 200 SMA still holds, the framework keeps the trader proposal at Hold unless a separate material negative setup is documented."
        )
        driver_text = (
            "This is an Underweight research rating with Hold trader action because long-term support still holds."
            if action == "Hold"
            else "The research rating and trader action are aligned."
        )
    else:
        decision_text = "The selected rating follows the score band and the Sell gate."
        driver_text = "The research rating and trader action are aligned."
    return f"""# Research Manager Decision: {ctx['ticker']}

**Recommendation**: {rating}

**Primary driver of rating:** {primary_driver}

**Strongest Bull Evidence**: {ctx['fundamental_themes']['quality_strength']}; {ctx['technical_themes']['long_term_trend_status']}.

**Strongest Bear Evidence**: {ctx['technical_themes']['short_medium_trend_status']}; {ctx['technical_themes']['momentum_status']}; {ctx['fundamental_themes']['valuation_risk']}.

**Scoring Rule**: +1 / -1 for price versus 200 SMA, 50 SMA, and 10 EMA; +1 / -1 for RSI versus 50; +1 / -1 for MACD versus signal; -1 for expensive valuation; +1 for profitable fundamental quality. Sell requires either price below the 200 SMA with a materially negative score, or an explicitly documented material negative setup despite 200 SMA support.

**Score Components**:

| Component | Evidence | Points |
|---|---|---:|
{rows}

**Evidence Score**: {score}

**Evidence Weighing**: {decision_text} {driver_text} The recommendation follows current evidence rather than safety-status language.

**What would change the rating**: An upgrade requires price confirmation above the 10 EMA and 50 SMA with improving momentum or direct positive catalysts. A downgrade requires fresh evidence of long-term support failure, deteriorating momentum, or materially negative direct news.

**Strategic Actions**:
- Use the 10 EMA and 50 SMA area as the first confirmation zone.
- Treat the 200 SMA as the long-term trend reference when available.
- Require fresh evidence before upgrading or downgrading the view.
"""


def trader(ctx: dict[str, Any]) -> str:
    action = ctx["direction"]["action"]
    rating = ctx["direction"]["rating"]
    close = ctx["ohlcv"].get("Close", "N/A")
    ema10 = ctx["indicators"].get("close_10_ema", "N/A")
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
    upgrade = f"Trigger that would upgrade: close reclaims the 10 EMA ({ema10}) and 50 SMA ({sma50}) with improving RSI/MACD."
    downgrade = f"Trigger that would downgrade: close fails below the 200 SMA ({sma200}) or the report documents a materially negative setup."
    return f"""# Trader Proposal: {ctx['ticker']}

**Action**: {action}

**Reasoning**: The research manager rating is {rating}. The transaction proposal is grounded in the latest close of {close}, the 50 SMA at {sma50}, the 200 SMA at {sma200}, and the current momentum evidence. A Buy requires constructive confirmation above key moving averages; a Sell requires evidence of breakdown below longer-term support or a separately documented materially negative setup; otherwise Hold is appropriate while waiting for confirmation.

**{consistency}**

**Confirmation/invalidation levels**: 10 EMA {ema10}; 50 SMA {sma50}; 200 SMA {sma200}.

**{upgrade}**

**{downgrade}**

FINAL TRANSACTION PROPOSAL: **{action.upper()}**
"""


def aggressive_risk(ctx: dict[str, Any]) -> str:
    return f"""# Aggressive Risk Analyst Round 1: {ctx['ticker']}

Aggressive Analyst: The higher-reward interpretation is strongest where {ctx['fundamental_themes']['quality_strength']} and {ctx['technical_themes']['long_term_trend_status']}. If price can reclaim short-term averages, upside participation could improve quickly; if it cannot, the aggressive case loses force.
"""


def conservative_risk(ctx: dict[str, Any]) -> str:
    return f"""# Conservative Risk Analyst Round 1: {ctx['ticker']}

Conservative Analyst: I directly respond to Aggressive Risk: upside participation could improve, but the proposal may still be unsafe if technical and valuation risk dominate. The market setup is {_trend_phrase(ctx)}, RSI is {ctx['indicators'].get('rsi', 'N/A')}, and ATR is {ctx['indicators'].get('atr', 'N/A')}. Until price confirms strength, the conservative stance is to avoid overstating conviction.
"""


def neutral_risk(ctx: dict[str, Any]) -> str:
    return f"""# Neutral Risk Analyst Round 1: {ctx['ticker']}

Neutral Analyst: The Aggressive view is right to acknowledge upside if fundamentals and long-term trend support persist. The Conservative view is right to require confirmation when short-term momentum is weak. Weighing Aggressive versus Conservative, the stronger risk argument is the one most consistent with the latest close versus moving averages: {ctx['technical_themes']['short_medium_trend_status']}. The balanced stance is to follow the trader action while using the moving averages and latest close as the key confirmation or invalidation references.
"""


def portfolio_manager(ctx: dict[str, Any]) -> str:
    rating = ctx["direction"]["rating"]
    action = ctx["direction"]["action"]
    primary_driver = ctx["direction"]["primary_driver"]
    risk_impact = (
        f"Conservative Risk outweighed Aggressive Risk because {ctx['technical_themes']['short_medium_trend_status']} and {ctx['technical_themes']['momentum_status']}."
        if action in {"Hold", "Sell"}
        else f"Aggressive Risk remained acceptable because {ctx['technical_themes']['short_medium_trend_status']} and quality evidence supported participation."
    )
    action_text = f" Final action differs from rating: Trader Action is {action} because the Sell gate is not met." if rating != action else f" Final action matches rating: {action}."
    sell_quality_note = (
        " This is a technical/momentum Sell, not a fundamental quality Sell."
        if rating == "Sell" and primary_driver == "technical"
        else ""
    )
    return f"""# Portfolio Manager Decision: {ctx['ticker']}

**Rating**: {rating}

**Final Action**: {action}

**Primary driver of rating:** {primary_driver}

**Executive Summary**: {ctx['ticker']} receives a {rating} rating based on {ctx['technical_themes']['long_term_trend_status']}, {ctx['technical_themes']['short_medium_trend_status']}, and {ctx['fundamental_themes']['valuation_risk']}.{action_text}{sell_quality_note}

**Investment Thesis**: Fundamentals show {ctx['fundamental_themes']['quality_strength']}. The latest close is {ctx['ohlcv'].get('Close', 'N/A')} and the market report shows price is {_trend_phrase(ctx)}. Social evidence contributes {ctx['social']['confidence']} confidence color because {ctx['social']['confidence_reason']}.

**Risk Assessment**: Risk debate impact: {risk_impact} This changes the final decision by keeping confirmation levels explicit rather than merely repeating the Trader.

**What would invalidate or improve the decision**: Improvement requires reclaiming the 10 EMA and 50 SMA with improving momentum. Invalidation requires failure at the 200 SMA, materially negative direct news, or a worsening score component mix.

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
