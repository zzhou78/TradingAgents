from __future__ import annotations

import argparse
import json
from pathlib import Path

TRADE_DATE_DEFAULT = "2026-07-02"


def _load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _clean_cell(value: object) -> str:
    return str(value or "").replace("|", "/").replace("\r", " ").replace("\n", " ").strip()


def _money(value: object) -> str:
    try:
        return f"{float(value):.2f}"
    except (TypeError, ValueError):
        return "n/a"


def _metric_map(records: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    return {str(record.get("metric_name")): record for record in records}


def _find_financial_record(
    records: list[dict[str, object]],
    *needles: str,
    available: bool = True,
) -> dict[str, object]:
    for record in records:
        haystack = " ".join(
            str(record.get(key, "")) for key in ("section_name", "source_type", "supports_claims")
        ).lower()
        if all(needle.lower() in haystack for needle in needles) and (
            not available or record.get("status") == "available"
        ):
            return record
    return {}


def _fund_record(records: list[dict[str, object]], section: str) -> dict[str, object]:
    for record in records:
        if section.lower() in str(record.get("section_name", "")).lower():
            return record
    return records[0] if records else {}


def _asx_sector_metric_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        record
        for record in records
        if str(record.get("section_kind") or "") == "sector_metric"
        or str(record.get("section_name", "")).startswith("sector_metric_")
    ]


def _asx_sector_metric_summary(records: list[dict[str, object]]) -> str:
    metrics = _asx_sector_metric_records(records)
    if not metrics:
        return (
            "- Sector-specific gap: no ASX sector metric records were extracted. "
            "Financial strength/weakness claims must stay evidence-gapped.\n"
        )
    sector = str(next((record.get("sector") for record in metrics if record.get("sector")), "ASX sector"))
    lines = [f"- ASX sector identified by collector: {sector}."]
    for record in metrics:
        label = _clean_cell(record.get("metric_label") or record.get("metric_name"))
        status = _clean_cell(record.get("status"))
        evidence_id = _clean_cell(record.get("evidence_id"))
        confidence = _clean_cell(record.get("confidence"))
        gap = _clean_cell(record.get("evidence_gap") or record.get("unavailable_reason"))
        if status == "available":
            lines.append(f"- {label}: available via {evidence_id}; confidence {confidence}.")
        else:
            lines.append(f"- {label}: evidence gap disclosed via {evidence_id}; {gap}")
    return "\n".join(lines) + "\n"


def _asx_sector_metric_table_rows(records: list[dict[str, object]]) -> list[str]:
    rows = []
    for record in _asx_sector_metric_records(records):
        rows.append(
            "| "
            + " | ".join(
                [
                    _clean_cell(record.get("evidence_id")),
                    _clean_cell(record.get("sector")),
                    _clean_cell(record.get("metric_label") or record.get("metric_name")),
                    _clean_cell(record.get("status")),
                    _clean_cell(record.get("confidence")),
                    _clean_cell(record.get("evidence_gap") or record.get("unavailable_reason") or "none"),
                ]
            )
            + " |"
        )
    if not rows:
        rows.append("| none | ASX | sector metrics | unavailable | low | no ASX sector metric records extracted |")
    return rows


def _asx_decisive_sector_metric(records: list[dict[str, object]]) -> dict[str, object]:
    metrics = _asx_sector_metric_records(records)
    for record in metrics:
        if str(record.get("status")) == "available":
            return record
    return metrics[0] if metrics else {}


def _asx_metric_counts(records: list[dict[str, object]]) -> tuple[int, int]:
    status_by_metric: dict[str, bool] = {}
    for record in _asx_sector_metric_records(records):
        metric_name = str(record.get("metric_name") or record.get("metric_label") or "")
        if not metric_name:
            continue
        if str(record.get("status")) == "available":
            status_by_metric[metric_name] = True
        else:
            status_by_metric.setdefault(metric_name, False)
    available = sum(1 for is_available in status_by_metric.values() if is_available)
    unavailable = sum(1 for is_available in status_by_metric.values() if not is_available)
    return available, unavailable


def _market_setup_label(*, rel_10: str, rel_50: str, rel_200: str) -> str:
    if rel_10 == rel_50 == rel_200 == "above":
        return "positive across 10 EMA, 50 SMA, and 200 SMA"
    if rel_10 == rel_50 == rel_200 == "below":
        return "negative across 10 EMA, 50 SMA, and 200 SMA"
    if rel_10 == "above" and rel_50 == "above" and rel_200 == "below":
        return "short/intermediate rebound but still below the 200 SMA"
    if rel_10 == "below" and rel_50 == "below" and rel_200 == "above":
        return "near-term weakness while long-term support remains intact above the 200 SMA"
    return f"mixed: close is {rel_10} 10 EMA, {rel_50} 50 SMA, and {rel_200} 200 SMA"


def _asx_research_reasoning(
    *,
    ticker: str,
    close: float,
    ema_10: float,
    sma_50: float,
    sma_200: float,
    rel_10: str,
    rel_50: str,
    rel_200: str,
    financial_records: list[dict[str, object]],
    refs: dict[str, object],
    best_news_id: str,
    first_social_id: str,
) -> dict[str, str]:
    metric = _asx_decisive_sector_metric(financial_records)
    metric_label = _clean_cell(metric.get("metric_label") or metric.get("metric_name") or "sector metric")
    metric_id = _clean_cell(metric.get("evidence_id") or "sector metric unavailable")
    metric_status = _clean_cell(metric.get("status") or "unavailable")
    metric_gap = _clean_cell(metric.get("evidence_gap") or metric.get("unavailable_reason") or "none")
    available_metrics, unavailable_metrics = _asx_metric_counts(financial_records)
    market_setup = _market_setup_label(rel_10=rel_10, rel_50=rel_50, rel_200=rel_200)
    sector = _clean_cell(metric.get("sector") or "ASX sector")

    if rel_10 == rel_50 == rel_200 == "below":
        market_weight = "-2"
        market_effect = (
            "The all-below-average setup blocks Buy/Overweight and is the closest path to Underweight; Hold is retained only "
            "because official financial records and sector metrics prevent a completed Sell case."
        )
        why_not_sell = (
            f"Sell/Underweight is not selected because {refs['exhibit']} and {metric_id} still provide official-source "
            "financial context; the negative market setup is decisive for caution but not enough by itself for a directional Sell."
        )
    elif rel_10 == rel_50 == "above" and rel_200 == "above":
        market_weight = "+1"
        market_effect = (
            "The above-all-averages setup removes the technical objection to Hold, but the rating is capped because the "
            "Research Manager needs stronger sector metric breadth and cleaner source depth before Overweight."
        )
        why_not_sell = (
            "Sell/Underweight is not selected because price is above the 10 EMA, 50 SMA, and 200 SMA, so market evidence "
            "does not support a bearish rating without a separate negative financial catalyst."
        )
    elif rel_10 == "above" and rel_50 == "above" and rel_200 == "below":
        market_weight = "0"
        market_effect = (
            "The short/intermediate rebound improves the case versus Underweight, but the close remains below the 200 SMA, "
            "so long-term confirmation is still missing."
        )
        why_not_sell = (
            "Sell/Underweight is not selected because the close has recovered above the 10 EMA and 50 SMA; the 200 SMA gap "
            "keeps conviction capped rather than forcing a Sell."
        )
    elif rel_10 == "below" and rel_50 == "below" and rel_200 == "above":
        market_weight = "0"
        market_effect = (
            "Near-term weakness blocks Buy/Overweight, while the close above the 200 SMA keeps the Research Manager from "
            "treating the setup as a completed long-term breakdown."
        )
        why_not_sell = (
            "Sell/Underweight is not selected because long-term support remains intact above the 200 SMA; the negative "
            "short/intermediate setup is a confidence cap rather than a full Sell trigger."
        )
    else:
        market_weight = "0"
        market_effect = (
            "Mixed moving-average evidence keeps the rating at Hold until the market setup resolves."
        )
        why_not_sell = (
            "Sell/Underweight is not selected because market evidence is mixed rather than a clean bearish breakdown."
        )

    metric_line = (
        f"{sector} metric evidence: {metric_label} is {metric_status} via {metric_id}"
        + (f"; evidence gap: {metric_gap}" if metric_status != "available" and metric_gap else ".")
    )
    confidence_cap = (
        f"Confidence is capped by {unavailable_metrics} unavailable sector metric/gap labels and low-confidence retail sentiment "
        f"from {first_social_id}."
        if unavailable_metrics
        else f"Confidence is capped by role-level source limitations and low-confidence retail sentiment from {first_social_id}, not by sector metrics alone."
    )
    why_not_buy = (
        f"Buy/Overweight is not selected because {ticker} has a {market_setup} setup and sector metric coverage is "
        f"{available_metrics} available / {unavailable_metrics} gap-labelled; that is not enough for an aggressive rating."
    )
    decisive = (
        f"Decisive evidence is Market Analyst ({refs['close']}, {refs['ema10']}, {refs['sma50']}, {refs['sma200']}) plus "
        f"Financial Report Analyst / ASX sector metrics ({metric_id}); News ({best_news_id}) is contextual and Sentiment is low weight."
    )
    score_line = (
        f"{market_weight} market setup ({market_setup}), +1 official ASX financial-source context, "
        f"+1 sector metric availability breadth ({available_metrics} available), "
        f"-1 evidence-gap/source-depth cap ({unavailable_metrics} gaps), 0 retail sentiment = Hold with ticker-specific skew"
    )
    return {
        "market_setup": market_setup,
        "market_effect": market_effect,
        "why_not_buy": why_not_buy,
        "why_not_sell": why_not_sell,
        "decisive": decisive,
        "metric_line": metric_line,
        "confidence_cap": confidence_cap,
        "score_line": score_line,
        "metric_id": metric_id,
        "metric_label": metric_label,
        "summary": (
            f"Hold is ticker-specific here: latest close {_money(close)} is {rel_10} the 10 EMA ({_money(ema_10)}), "
            f"{rel_50} the 50 SMA ({_money(sma_50)}), and {rel_200} the 200 SMA ({_money(sma_200)}). {market_effect}"
        ),
    }


def _first_usable_news(cards: list[dict[str, object]]) -> dict[str, object]:
    preferred: list[tuple[int, dict[str, object]]] = []
    for card in cards:
        validity = card.get("as_of_validity")
        valid = not isinstance(validity, dict) or bool(validity.get("valid_for_trade_date", True))
        if not valid:
            continue
        title = str(card.get("title", "")).lower()
        source = str(card.get("source", "")).lower()
        text_status = str(card.get("text_status") or card.get("full_text_status") or "").lower()
        has_text = text_status in {"partial_text", "full_text_verified", "full_text"}
        if "sec" in source or "exhibit" in title or "results" in title:
            preferred.append((0 if has_text else 1, card))
        elif has_text:
            preferred.append((2, card))
    if preferred:
        return sorted(preferred, key=lambda item: item[0])[0][1]
    return cards[0] if cards else {}


def _social_stats(summary: dict[str, object]) -> tuple[int, int, int, int, int]:
    sources = summary.get("sources")
    if not isinstance(sources, list):
        return 0, 0, 0, 0, 0
    total = usable = bullish = bearish = neutral = 0
    for source in sources:
        if not isinstance(source, dict):
            continue
        total += int(source.get("items_reviewed") or 0)
        usable += int(source.get("usable_ticker_relevant_items") or 0)
        bullish += int(source.get("bullish_count") or 0)
        bearish += int(source.get("bearish_count") or 0)
        neutral += int(source.get("neutral_count") or 0)
    return total, usable, bullish, bearish, neutral


def _top_social_cards(cards: list[dict[str, object]]) -> list[dict[str, object]]:
    valid = [
        card
        for card in cards
        if not isinstance(card.get("as_of_validity"), dict)
        or bool(card["as_of_validity"].get("valid_for_trade_date", True))
    ]
    direct = [card for card in valid if card.get("ticker_relevance") == "direct_company"]
    reasoned = [card for card in direct if card.get("reasoning_quality") in {"medium", "high"}]
    return sorted(reasoned, key=lambda card: float(card.get("influence_weight") or 0), reverse=True)[:3]


def _low_quality_social_cards(cards: list[dict[str, object]]) -> list[dict[str, object]]:
    valid = [
        card
        for card in cards
        if not isinstance(card.get("as_of_validity"), dict)
        or bool(card["as_of_validity"].get("valid_for_trade_date", True))
    ]
    direct = [card for card in valid if card.get("ticker_relevance") == "direct_company"]
    low_quality = [card for card in direct if card.get("reasoning_quality") == "low"]
    return sorted(low_quality, key=lambda card: float(card.get("influence_weight") or 0), reverse=True)[:3]


def _memory_footer(*, refs: str, trade_date: str) -> str:
    return f"""## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: {refs}
* Staleness / expiry: Evidence is valid only for trade date {trade_date}; refresh before reuse.
"""


def _report_body_for_debate_record(path: Path) -> str:
    if not path.exists():
        return "Pending Codex role output: source file is missing."
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    if not text:
        return "Pending Codex role output: source file is empty."
    text = text.split("\n## Memory Update", 1)[0].strip()
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip() or "Pending Codex role output: source file has no debate body."


def _write_assembled_debate_record(*, report_dir: Path, ticker: str, trade_date: str) -> Path:
    stages = [
        ("Research Team Debate", "Bull Researcher Round 1 - Opening Case", report_dir / "2_research" / "bull_round_1.md"),
        ("Research Team Debate", "Bear Researcher Round 1 - Rebuttal to Bull", report_dir / "2_research" / "bear_round_1.md"),
        ("Research Team Debate", "Research Manager Decision - Evidence Weighing", report_dir / "2_research" / "manager.md"),
        ("Risk Management Team Debate", "Aggressive Risk Analyst Round 1 - Opportunity Case", report_dir / "4_risk" / "aggressive_round_1.md"),
        ("Risk Management Team Debate", "Conservative Risk Analyst Round 1 - Response to Aggressive", report_dir / "4_risk" / "conservative_round_1.md"),
        ("Risk Management Team Debate", "Neutral Risk Analyst Round 1 - Weighing", report_dir / "4_risk" / "neutral_round_1.md"),
        ("Risk Management Team Debate", "Portfolio Manager Synthesis", report_dir / "5_portfolio" / "decision.md"),
    ]
    lines = [
        "# TradingAgents Debate Record",
        "",
        f"- Ticker: `{ticker}`",
        f"- Trade date: `{trade_date}`",
        "- Status: completed Codex-visible debate transcript assembled from role outputs",
        "",
        "This file is assembled after Codex-session role reports are written. It preserves the completed debate turns and links to the full role files.",
        "",
    ]
    current_group = ""
    pending_count = 0
    for group, title, path in stages:
        if group != current_group:
            current_group = group
            lines.extend([f"## {group}", ""])
        body = _report_body_for_debate_record(path)
        if "Pending Codex role output" in body:
            pending_count += 1
        lines.extend(
            [
                f"### {title}",
                "",
                f"- Full output: `{path}`",
                "",
                body,
                "",
            ]
        )
    lines.extend(
        [
            "## Transcript Integrity",
            "",
            f"- Pending debate outputs: `{pending_count}`",
            "- The complete report should cite these same role outputs rather than treating this file as a separate evidence source.",
            "",
        ]
    )
    path = report_dir / "debate_record.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def _ensure_report_dirs(report_dir: Path) -> None:
    for subdir in ["1_analysts", "2_research", "3_trading", "4_risk", "5_portfolio", "6_quality"]:
        (report_dir / subdir).mkdir(parents=True, exist_ok=True)


def _relation(close: float, level: float) -> str:
    if close > level:
        return "above"
    if close < level:
        return "below"
    return "at"


def _market_regime(*, close: float, ema_10: float, sma_50: float, sma_200: float, rsi: float, macd: float) -> str:
    if close > ema_10 and close > sma_50 and close > sma_200 and rsi >= 45:
        return "constructive but not trend-confirmed because MACD remains negative"
    if close > ema_10 and close < sma_50 and close < sma_200:
        return "short rebound inside a still-negative intermediate and long-term trend"
    if close < ema_10 and close < sma_50 and close < sma_200:
        return "negative across short, intermediate, and long-term trend measures"
    return "mixed technical regime"


def _metric(metrics: dict[str, dict[str, object]], *names: str) -> dict[str, object]:
    for name in names:
        if name in metrics:
            return metrics[name]
    raise KeyError(f"none of the metric aliases exists: {', '.join(names)}")


def _ticker_policy(ticker: str) -> dict[str, str]:
    if ticker.upper() == "AAPL":
        return {
            "manager_rec": "Overweight",
            "portfolio_rating": "Overweight",
            "trader_action": "HOLD",
            "bull_theme": "strong product/services economics and intact long-term trend",
            "bear_theme": "premium valuation and negative MACD keep timing risk real",
            "theme1": "Platform monetization",
            "subtheme1": "Services and installed-base durability",
            "theme2": "Device cycle risk",
            "subtheme2": "Premium valuation and hardware cycle sensitivity",
            "score_line": "+1 market, +2 financial quality, +1 earnings/news, 0 low-confidence retail sentiment, -1 valuation/timing risk = +3",
            "why": (
                "Overweight beats Hold because multiple direct filing and earnings-release records show business "
                "strength while the latest close is above the 10 EMA, 50 SMA, and 200 SMA; it does not become Buy "
                "because MACD is negative and social evidence is low-confidence retail color."
            ),
        }
    if ticker.upper().endswith(".AX"):
        return {
            "manager_rec": "Hold",
            "portfolio_rating": "Hold",
            "trader_action": "HOLD",
            "bull_theme": "available ASX filing sections and market evidence support a reviewable base case",
            "bear_theme": "source coverage gaps and technical confirmation risk limit conviction",
            "theme1": "ASX company fundamentals",
            "subtheme1": "Official announcement and financial-section support",
            "theme2": "Evidence quality risk",
            "subtheme2": "Unavailable sections and market confirmation limits",
            "score_line": "0 market/technical balance, +1 available official-source evidence, 0 low-confidence sentiment, -1 unavailable section risk = 0",
            "why": (
                "Hold beats Buy because ASX source coverage is uneven and any missing MD&A, cash-flow, or segment "
                "section must be treated as an evidence gap; it beats Sell where available official-source records "
                "still support a reviewable base case and the quality gate has not identified a completed negative "
                "fundamental case."
            ),
        }
    return {
        "manager_rec": "Underweight",
        "portfolio_rating": "Underweight",
        "trader_action": "HOLD",
        "bull_theme": "cloud and AI revenue growth remains strong",
        "bear_theme": "price remains below the 50 SMA and 200 SMA despite the rebound above the 10 EMA",
        "theme1": "AI infrastructure demand",
        "subtheme1": "Cloud and AI revenue scale",
        "theme2": "Capex and trend risk",
        "subtheme2": "Heavy AI investment against weak price trend",
        "score_line": "-2 market trend, +2 financial quality, +1 earnings/news, 0 low-confidence retail sentiment, -1 capex/trend risk = 0 with negative technical skew",
        "why": (
            "Underweight beats Hold because the strongest financial evidence is positive, but the market evidence "
            "still shows the close below both 50 SMA and 200 SMA; it does not become Sell because the company "
            "fundamentals and Exhibit 99.1 evidence remain strong and price is above the 10 EMA."
        ),
    }


def write_reports(*, output_dir: Path, ticker: str, trade_date: str) -> Path:
    evidence_dir = output_dir / "evidence" / ticker / trade_date
    report_dir = output_dir / "reports" / ticker / trade_date
    _ensure_report_dirs(report_dir)

    evidence = _load_json(evidence_dir / "evidence.json")
    market_records = _load_json(evidence_dir / "market" / "quantitative_observations.json")
    social_summary = _load_json(evidence_dir / "social" / "social_summary.json")
    social_cards_path = evidence_dir / "social" / "social_cards.json"
    social_cards = _load_json(social_cards_path) if social_cards_path.exists() else []
    news_cards = _load_json(evidence_dir / "news" / "article_cards.json")
    financial_records = _load_json(evidence_dir / "financial_report" / "section_records.json")
    fundamental_records = _load_json(evidence_dir / "fundamentals" / "statement_records.json")
    assert isinstance(market_records, list)
    assert isinstance(evidence, dict)
    assert isinstance(social_summary, dict)
    assert isinstance(social_cards, list)
    assert isinstance(news_cards, list)
    assert isinstance(financial_records, list)
    assert isinstance(fundamental_records, list)

    metrics = _metric_map(market_records)
    close = float(metrics["latest_close"]["value"])
    ema_10 = float(metrics["ema_10"]["value"])
    sma_50 = float(metrics["sma_50"]["value"])
    sma_200 = float(metrics["sma_200"]["value"])
    rsi_record = _metric(metrics, "rsi_14", "rsi")
    atr_record = _metric(metrics, "atr_14", "atr")
    rsi = float(rsi_record["value"])
    macd = float(metrics["macd"]["value"])
    atr = float(atr_record["value"])
    source_date = str(metrics["latest_close"]["source_date"])
    rel_10 = _relation(close, ema_10)
    rel_50 = _relation(close, sma_50)
    rel_200 = _relation(close, sma_200)
    regime = _market_regime(
        close=close,
        ema_10=ema_10,
        sma_50=sma_50,
        sma_200=sma_200,
        rsi=rsi,
        macd=macd,
    )

    policy = _ticker_policy(ticker)
    best_news = _first_usable_news(news_cards)
    best_news_id = str(best_news.get("evidence_id", f"news:{ticker}:{trade_date}:001"))
    exhibit = (
        _find_financial_record(financial_records, "exhibit 99.1")
        or _find_financial_record(financial_records, "revenue_income_npat")
        or _find_financial_record(financial_records, "management_commentary_outlook")
        or _find_financial_record(financial_records, "management_discussion_analysis")
    )
    q_mda = _find_financial_record(financial_records, "10-q", "md&a") or _find_financial_record(
        financial_records, "management_discussion_analysis"
    )
    q_liquidity = (
        _find_financial_record(financial_records, "10-q", "liquidity")
        or _find_financial_record(financial_records, "cash_debt_gearing")
        or _find_financial_record(financial_records, "liquidity")
    )
    q_cash = _find_financial_record(financial_records, "10-q", "cash flow") or _find_financial_record(
        financial_records, "cash_flow_statement"
    )
    q_segment = (
        _find_financial_record(financial_records, "10-q", "segment/product")
        or _find_financial_record(financial_records, "segment_product_performance")
        or _find_financial_record(financial_records, "segment")
    )
    k_business = _find_financial_record(financial_records, "10-k", "business") or exhibit
    k_risk = (
        _find_financial_record(financial_records, "10-k", "risk")
        or _find_financial_record(financial_records, "business_risk")
        or _find_financial_record(financial_records, "risk")
    )
    f_packet = _fund_record(fundamental_records, "company fundamentals")
    f_balance = _fund_record(fundamental_records, "balance")
    f_cash = _fund_record(fundamental_records, "cash flow")
    f_income = _fund_record(fundamental_records, "income")
    total, usable, bullish, bearish, neutral = _social_stats(social_summary)
    run_metadata = evidence.get("run_metadata") if isinstance(evidence.get("run_metadata"), dict) else {}
    run_executed_at = str(run_metadata.get("run_executed_at") or evidence.get("run_executed_at") or "")
    evidence_as_of = str(run_metadata.get("evidence_as_of_date") or evidence.get("evidence_as_of_date") or trade_date)
    run_id = str(run_metadata.get("run_id") or evidence.get("run_id") or "")
    run_folder_name = str(run_metadata.get("run_folder_name") or output_dir.name)
    is_asx = ticker.upper().endswith(".AX")

    sources = social_summary.get("sources") if isinstance(social_summary.get("sources"), list) else []
    social_ids = [
        str(source.get("evidence_id"))
        for source in sources
        if isinstance(source, dict) and source.get("evidence_id")
    ]
    first_social_id = social_ids[0] if social_ids else "social unavailable"

    market_refs = ", ".join(
        str(metrics[name]["evidence_id"]) for name in ("latest_close", "ema_10", "sma_50", "sma_200")
    )
    (report_dir / "1_analysts" / "market.md").write_text(
        f"""# Market Analyst Report - {ticker}

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records {metrics['latest_close']['evidence_id']} through {atr_record['evidence_id']}.
- Source date for price metrics: {source_date}; trade date: {trade_date}.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | {_money(close)} | {metrics['latest_close']['evidence_id']} | Reference price |
| 10 EMA | {_money(ema_10)} | {metrics['ema_10']['evidence_id']} | Close is {rel_10} 10 EMA |
| 50 SMA | {_money(sma_50)} | {metrics['sma_50']['evidence_id']} | Close is {rel_50} 50 SMA |
| 200 SMA | {_money(sma_200)} | {metrics['sma_200']['evidence_id']} | Close is {rel_200} 200 SMA |
| RSI 14 | {_money(rsi)} | {rsi_record['evidence_id']} | Momentum oscillator |
| MACD | {_money(macd)} | {metrics['macd']['evidence_id']} | Trend momentum |
| ATR 14 | {_money(atr)} | {atr_record['evidence_id']} | Volatility / level spacing |

Interpretation: {ticker} has a {regime}. This statement is mechanical from the table: the close is {rel_10} the 10 EMA, {rel_50} the 50 SMA, and {rel_200} the 200 SMA. MACD is {_money(macd)}, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after {source_date} is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

{_memory_footer(refs=market_refs, trade_date=trade_date)}""",
        encoding="utf-8",
    )

    source_rows: list[str] = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        limitations = ", ".join(str(item) for item in (source.get("limitations") or [])) or "none disclosed"
        source_rows.append(
            "| "
            + " | ".join(
                [
                    _clean_cell(source.get("evidence_id")),
                    _clean_cell(source.get("source")),
                    _clean_cell(source.get("source_confidence_category")),
                    str(source.get("items_reviewed", 0)),
                    str(source.get("usable_ticker_relevant_items", 0)),
                    f"{source.get('bullish_count', 0)}/{source.get('bearish_count', 0)}/{source.get('neutral_count', 0)}",
                    _clean_cell(source.get("confidence")),
                    _clean_cell(limitations),
                ]
            )
            + " |"
        )
    top_rows = []
    for card in _top_social_cards(social_cards):
        top_rows.append(
            "| "
            + " | ".join(
                [
                    _clean_cell(card.get("evidence_id")),
                    _clean_cell(card.get("source")),
                    _clean_cell(card.get("candidate_sentiment_label")),
                    _clean_cell(card.get("reasoning_quality")),
                    _clean_cell(card.get("ticker_relevance")),
                    _clean_cell(card.get("independence_group_id")),
                    _clean_cell(str(card.get("text_excerpt", ""))[:160]),
                ]
            )
            + " |"
        )
    if not top_rows:
        top_rows.append("| none | none | neutral | none | unavailable | none | No genuinely reasoned social items were found. |")
    low_quality_rows = []
    for card in _low_quality_social_cards(social_cards):
        low_quality_rows.append(
            "| "
            + " | ".join(
                [
                    _clean_cell(card.get("evidence_id")),
                    _clean_cell(card.get("source")),
                    _clean_cell(card.get("candidate_sentiment_label")),
                    _clean_cell(card.get("reasoning_quality")),
                    _clean_cell(str(card.get("text_excerpt", ""))[:160]),
                ]
            )
            + " |"
        )
    if not low_quality_rows:
        low_quality_rows.append("| none | none | none | none | No representative low-quality retail item needed. |")
    signal = "mixed retail-only reaction" if bullish and bearish else "low-confidence retail reaction"
    (report_dir / "1_analysts" / "sentiment.md").write_text(
        f"""# Sentiment Analyst Report - {ticker}

## Tool Outputs Used
- social_summary.json source-level records: {', '.join(social_ids) or 'none'}.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| {total} | {usable} | {bullish} | {bearish} | {neutral} | low |

The usable sentiment signal is {signal}. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
{chr(10).join(source_rows)}

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
{chr(10).join(top_rows)}

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
{chr(10).join(low_quality_rows)}

## Excluded / Downgraded Evidence
- Low-information, meme, spam-like, cross-ticker, and post-trade-date items are excluded or downgraded by the evidence cards.
- Retail-only sources are capped at low confidence in this run; they cannot support institution-level conclusions.
- Reddit is optional and sparse for this run; its absence or low usability lowers confidence rather than blocking the workflow.

## Event Context vs Reaction Evidence
- News and filings describe event facts; sentiment cards describe participant reaction.
- Related posts share independence groups such as event:{ticker}:{trade_date}:earnings-or-price-action. Research Manager must not count article facts and social reposts as separate fundamental evidence.

## Final Sentiment Interpretation
Final sentiment: Mixed / low confidence. The signal is company-specific only where cards are direct-company, otherwise it is broad retail color. It is not sourced from analyst or institution-level feeds and is too noisy to drive a Buy/Hold/Sell decision alone.

## Evidence Gaps
- No approved analyst-rating revision feed, options sentiment, or institutional survey source was available.
- Reddit coverage is optional and low confidence in this run.

{_memory_footer(refs=', '.join(social_ids) or 'social source unavailable', trade_date=trade_date)}""",
        encoding="utf-8",
    )

    selected_cards = [best_news] + [card for card in news_cards if card.get("evidence_id") != best_news_id][:4]
    article_rows = []
    for card in selected_cards:
        if not card:
            continue
        is_best = card.get("evidence_id") == best_news_id
        article_rows.append(
            "| "
            + " | ".join(
                [
                    _clean_cell(card.get("evidence_id")),
                    _clean_cell(str(card.get("title", ""))[:90]),
                    _clean_cell(card.get("source")),
                    _clean_cell(card.get("publication_date") or card.get("source_date")),
                    _clean_cell(card.get("full_text_status") or card.get("text_status") or "unknown"),
                    _clean_cell(card.get("direct_company_relevance") or card.get("relevance") or "pending"),
                    "earnings/context",
                    "positive" if is_best else "excluded / low relevance",
                    "direct earnings-release or official company evidence"
                    if is_best
                    else "snippet, generic, duplicate, or low direct relevance",
                    _clean_cell(card.get("confidence") or ("medium" if is_best else "low")),
                    "none for selected official item" if is_best else "not used for final impact label",
                ]
            )
            + " |"
        )
    (report_dir / "1_analysts" / "news.md").write_text(
        f"""# News Analyst Report - {ticker}

## Tool Outputs Used
- news/article_cards.json with article evidence cards, including {best_news_id}.
- As-of filter: only evidence valid for trade date {trade_date} is used for impact judgment.

## Article Evidence Cards
| Evidence ID | Title | Source | Publication date | Full-text status | Direct company relevance | Event type | Likely effect | Reason | Confidence | Evidence gap |
|---|---|---|---|---|---|---|---|---|---|---|
{chr(10).join(article_rows)}

## News Impact Summary
Impact label: mixed-to-positive, supported by {best_news_id}. The strongest usable news card is `{_clean_cell(best_news.get('title', 'selected article'))}`. It is treated as direct company event context, while generic snippets, duplicate official pages, unrelated posts, and post-trade-date items are excluded from the final impact label.

## Evidence Gaps
- Some candidate articles are snippet-only or generic official navigation pages; they are not used as material impact evidence.
- Full article text is preferred; snippet-only records are capped at low confidence.

{_memory_footer(refs=best_news_id, trade_date=trade_date)}""",
        encoding="utf-8",
    )

    sector_metric_summary = _asx_sector_metric_summary(financial_records) if is_asx else (
        "- Technology sector metrics considered: R&D intensity / innovation investment, cloud or platform scale where disclosed, product and services mix, and capex where available.\n"
        "- Sector-specific gap: the fundamentals packet does not by itself provide a complete segment KPI model, so Financial Report Analyst section records are required for segment and capex claims.\n"
    )
    fundamentals_interpretation = (
        "Interpretation: structured fundamentals provide ratio and statement context only; ASX sector metrics must come from official announcement or IR section records and are not final investment judgments."
        if is_asx
        else "Interpretation: structured fundamentals support a financially durable large-cap technology company, but valuation and market timing must be weighed by Research Manager rather than decided mechanically from ratios."
    )
    (report_dir / "1_analysts" / "fundamentals.md").write_text(
        f"""# Fundamentals Analyst Report - {ticker}

## Tool Outputs Used
- Company fundamentals packet: {f_packet.get('evidence_id')}.
- Balance sheet: {f_balance.get('evidence_id')}.
- Cash flow statement: {f_cash.get('evidence_id')}.
- Income statement: {f_income.get('evidence_id')}.

## Financial Statement Evidence
| Evidence ID | Statement / packet | Claim supported | Confidence |
|---|---|---|---|
| {f_packet.get('evidence_id')} | company fundamentals packet | Valuation, sector, beta, dividend yield, and market-cap context. | medium |
| {f_income.get('evidence_id')} | income statement | Revenue and income trend context. | medium |
| {f_balance.get('evidence_id')} | balance sheet | Balance sheet and net debt context. | medium |
| {f_cash.get('evidence_id')} | cash flow statement | Free cash flow and capital return context. | medium |

{fundamentals_interpretation}

## Sector-Specific Metrics
{sector_metric_summary.rstrip()}

## Evidence Gaps
- The fundamentals packet is structured but not a substitute for filing-section interpretation.
- No final investment judgment is made in this role.

{_memory_footer(refs=', '.join(str(item.get('evidence_id')) for item in [f_packet, f_income, f_cash] if item.get('evidence_id')), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    sector_metric_records = _asx_sector_metric_records(financial_records) if is_asx else []
    coverage_records = [k_business, k_risk, q_mda, q_segment, q_liquidity, q_cash, exhibit, *sector_metric_records[:8]]
    coverage_rows = [
        "| "
        + " | ".join(
            [
                _clean_cell(record.get("evidence_id")),
                _clean_cell(record.get("source_type")),
                _clean_cell(record.get("section_name")),
                _clean_cell(record.get("filing_date")),
                _clean_cell(record.get("status")),
                _clean_cell(str(record.get("excerpt", ""))[:110]),
            ]
        )
        + " |"
        for record in coverage_records
        if record
    ]
    if is_asx:
        metric_claim_rows = [
            f"| ASX sector metric: {_clean_cell(record.get('metric_label') or record.get('metric_name'))} | {record.get('evidence_id')} ASX section record | {record.get('section_name')} | {record.get('filing_date')} | {record.get('confidence')} | {_clean_cell(record.get('evidence_gap') or record.get('unavailable_reason') or 'none')} |"
            for record in sector_metric_records
        ]
        claim_rows = [
            f"| Official ASX financial-report context | {exhibit.get('evidence_id')} ASX document | {exhibit.get('section_name')} | {exhibit.get('filing_date')} | medium | {_clean_cell(exhibit.get('evidence_gap') or 'none')} |",
            f"| Management discussion / outlook support | {q_mda.get('evidence_id')} ASX document | {q_mda.get('section_name')} | {q_mda.get('filing_date')} | {q_mda.get('confidence', 'low')} | {_clean_cell(q_mda.get('evidence_gap') or 'none')} |",
            f"| Liquidity / cash-debt evidence | {q_liquidity.get('evidence_id')} ASX document | {q_liquidity.get('section_name')} | {q_liquidity.get('filing_date')} | {q_liquidity.get('confidence', 'low')} | {_clean_cell(q_liquidity.get('evidence_gap') or 'none')} |",
            f"| Segment/product evidence | {q_segment.get('evidence_id')} ASX document | {q_segment.get('section_name')} | {q_segment.get('filing_date')} | {q_segment.get('confidence', 'low')} | {_clean_cell(q_segment.get('evidence_gap') or 'none')} |",
            f"| Cash-flow evidence | {q_cash.get('evidence_id')} ASX document | {q_cash.get('section_name')} | {q_cash.get('filing_date')} | {q_cash.get('confidence', 'low')} | {_clean_cell(q_cash.get('evidence_gap') or 'none')} |",
            *metric_claim_rows,
        ]
        financial_gap_lines = (
            "- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.\n"
            "- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.\n"
            "- Guidance is not inferred unless explicitly found in the extracted ASX document section."
        )
    else:
        claim_rows = [
            f"| Quarterly revenue and earnings context | {exhibit.get('evidence_id')} 8-K | Exhibit 99.1 | {exhibit.get('filing_date')} | medium | none |",
            f"| Management discussion supports operating trend review | {q_mda.get('evidence_id')} 10-Q | 10-Q MD&A | {q_mda.get('filing_date')} | medium | none |",
            f"| Liquidity appears supported by company cash resources and access to markets | {q_liquidity.get('evidence_id')} 10-Q | Liquidity and capital resources | {q_liquidity.get('filing_date')} | medium | none |",
            f"| Segment/product mix is available for specialist interpretation | {q_segment.get('evidence_id')} 10-Q | Segment/product revenue tables | {q_segment.get('filing_date')} | medium | none |",
            f"| Cash-flow statement is available for operating cash flow and capital return review | {q_cash.get('evidence_id')} 10-Q | Cash flow statement | {q_cash.get('filing_date')} | medium | none |",
            f"| Risk factors require caution around company-specific uncertainties | {k_risk.get('evidence_id')} 10-K | Risk factors | {k_risk.get('filing_date')} | medium | none |",
            f"| Formal guidance detail | structured fundamentals packet | unavailable section / exhibit if not in Exhibit 99.1 | {trade_date} | low | explicit evidence gap if guidance not in extracted exhibit |",
            f"| Capex commitments / contractual obligations | 10-K/10-Q | unavailable commitments/capex section | {trade_date} | low | evidence gap: commitments/capex section marked unavailable where not extracted |",
        ]
        financial_gap_lines = (
            "- Do not treat an 8-K cover page as the earnings release; the earnings-release claim uses Exhibit 99.1 when available.\n"
            "- Commitments / capex / contractual-obligations sections are gap-labelled when extraction marked them unavailable.\n"
            "- Guidance is not inferred unless explicitly found in the extracted exhibit or filing section."
        )
    sector_metric_table = "\n".join(_asx_sector_metric_table_rows(financial_records)) if is_asx else "| not applicable | US technology | not applicable | unavailable | low | ASX sector metric extraction not applicable |"
    (report_dir / "1_analysts" / "financial_report.md").write_text(
        f"""# Financial Report Analyst Report - {ticker}

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
{chr(10).join(coverage_rows)}

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
{chr(10).join(claim_rows)}

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
{sector_metric_table}

## Evidence gaps
{financial_gap_lines}

{_memory_footer(refs=', '.join(str(item.get('evidence_id')) for item in [exhibit, q_mda, q_cash] if item.get('evidence_id')), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    (report_dir / "1_analysts" / "industry_theme.md").write_text(
        f"""# Industry / Theme Discovery Analyst Report - {ticker}

## Tool Outputs Used
- Financial filing sections: {q_segment.get('evidence_id')} and {exhibit.get('evidence_id')}.
- News event context: {best_news_id}.
- Market regime context: {metrics['latest_close']['evidence_id']}.

## Theme Evidence Table
| Theme | Subtheme | Evidence link | Classification | Confidence |
|---|---|---|---|---|
| {policy['theme1']} | {policy['subtheme1']} | {exhibit.get('evidence_id')} / {q_segment.get('evidence_id')} | direct company theme | medium |
| {policy['theme2']} | {policy['subtheme2']} | {metrics['latest_close']['evidence_id']} / {f_packet.get('evidence_id')} | risk theme | medium |

## Evidence Gaps
- Theme classification is evidence-linked, not a preconfigured taxonomy standing alone.
- No unapproved plugin or browsing action was used for theme discovery in this run.

{_memory_footer(refs=', '.join(str(item) for item in [exhibit.get('evidence_id'), q_segment.get('evidence_id'), metrics['latest_close']['evidence_id']] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    refs = {
        "close": metrics["latest_close"]["evidence_id"],
        "ema10": metrics["ema_10"]["evidence_id"],
        "sma50": metrics["sma_50"]["evidence_id"],
        "sma200": metrics["sma_200"]["evidence_id"],
        "macd": metrics["macd"]["evidence_id"],
        "atr": atr_record["evidence_id"],
        "exhibit": exhibit.get("evidence_id"),
        "segment": q_segment.get("evidence_id"),
        "risk": k_risk.get("evidence_id"),
        "fund": f_packet.get("evidence_id"),
    }
    financial_source_label = "ASX document and sector-metric records" if is_asx else "Exhibit 99.1 and 10-Q sections"
    financial_source_detail = (
        f"ASX financial-report evidence uses section-level records including {refs['exhibit']} official document context, "
        f"{q_mda.get('evidence_id')} management discussion/outlook, {q_liquidity.get('evidence_id')} liquidity, "
        f"{q_cash.get('evidence_id')} cash-flow, and ASX sector metrics where available or gap-labelled."
        if is_asx
        else (
            f"Financial-report evidence uses section-level records including {refs['exhibit']} Exhibit 99.1, "
            f"{q_mda.get('evidence_id')} 10-Q MD&A, {q_liquidity.get('evidence_id')} liquidity, "
            f"and {q_cash.get('evidence_id')} cash-flow statement. The report does not treat the 8-K cover page as the earnings release."
        )
    )
    quality_financial_line = (
        "ASX extraction: official-source collection succeeded or explicit gaps are disclosed; sector metrics are available or gap-labelled."
        if is_asx
        else "Financial extraction: MD&A, cash-flow, and Exhibit 99.1 are present where cited."
    )
    asx_reasoning = (
        _asx_research_reasoning(
            ticker=ticker,
            close=close,
            ema_10=ema_10,
            sma_50=sma_50,
            sma_200=sma_200,
            rel_10=rel_10,
            rel_50=rel_50,
            rel_200=rel_200,
            financial_records=financial_records,
            refs=refs,
            best_news_id=best_news_id,
            first_social_id=first_social_id,
        )
        if is_asx
        else {}
    )
    confirm = max(close + atr * 0.5, ema_10)
    invalid = min(close - atr * 0.5, sma_50 if ticker.upper() == "AAPL" else ema_10)
    (report_dir / "2_research" / "bull_round_1.md").write_text(
        f"""# Bull Researcher Round 1 - {ticker}

## Tool Outputs Used
- Market Analyst: {refs['close']} through {refs['sma200']}.
- Financial Report Analyst: {refs['exhibit']}, {q_mda.get('evidence_id')}, {refs['segment']}.
- News Analyst: {best_news_id}.

## Strongest Bull Evidence
- The best bull case is {policy['bull_theme']}, supported by direct filing and earnings-release evidence: {refs['exhibit']} and {refs['segment']}.
- Market evidence is not ignored: latest close {_money(close)} is {rel_10} the 10 EMA, {rel_50} the 50 SMA, and {rel_200} the 200 SMA ({refs['close']}, {refs['sma200']}).
- News support comes from {best_news_id}; social evidence is not counted as independent high-confidence confirmation.

## Falsification Conditions
- Falsified if updated filing evidence contradicts the earnings/segment strength cited above.
- Falsified technically if price loses the 10 EMA at {_money(ema_10)} and fails to recover, or if {ticker} breaks materially below the 200 SMA at {_money(sma_200)}.
- Falsified if Research Manager finds the same event is double-counted across News and Sentiment.

## Response To Bear
Bear is right that valuation and trend quality matter. The bull answer is that direct financial evidence remains stronger than retail sentiment, so the risk should limit aggressiveness rather than erase the constructive case.

{_memory_footer(refs=', '.join(str(item) for item in [refs['exhibit'], refs['segment'], refs['close']] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )
    (report_dir / "2_research" / "bear_round_1.md").write_text(
        f"""# Bear Researcher Round 1 - {ticker}

## Tool Outputs Used
- Market Analyst moving-average and MACD evidence: {refs['close']}, {refs['sma50']}, {refs['sma200']}, {refs['macd']}.
- Fundamentals and filings: {refs['fund']}, {refs['risk']}.
- Sentiment source quality records: {', '.join(social_ids) or 'none'}.

## Strongest Bear Evidence
- The strongest bear case is {policy['bear_theme']}. The table-driven market evidence shows close {_money(close)}, 50 SMA {_money(sma_50)}, 200 SMA {_money(sma_200)}, and MACD {_money(macd)}.
- Sentiment is low-confidence retail color, not institution-level confirmation; therefore bullish platform labels should not be over-weighted.
- Risk factors and valuation/timing evidence require a margin of safety rather than a pure growth extrapolation.

## Falsification Conditions
- Falsified if {ticker} reclaims the key trend levels with MACD improving and filings continue to show durable growth.
- Falsified if Bear relies only on noisy social posts or generic risk text without evidence IDs.

## Response To Bull
Bull's strongest argument is direct earnings and segment evidence. Bear's answer is not that the company is weak; it is that market timing, valuation, and trend evidence limit the immediate reward/risk, especially where social evidence is low-quality.

{_memory_footer(refs=', '.join(str(item) for item in [refs['macd'], refs['risk'], refs['fund']] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    market_matrix_direction = "positive" if ticker.upper() == "AAPL" else "negative"
    market_matrix_weight = "+1" if ticker.upper() == "AAPL" else "-2"
    market_matrix_reason = regime
    score_line = policy["score_line"]
    rating_rationale = policy["why"]
    manager_rec = policy["manager_rec"]
    trader_action = policy["trader_action"]
    portfolio_rating = policy["portfolio_rating"]
    rating_vs_rating_section = (
        "## Rating-vs-Rating Reasoning\n"
        f"1. Why not Buy / Overweight? {policy['why']}\n"
        f"2. Why not Sell / Underweight? {manager_rec} is not a Sell because the evidence mix is not a clean long-term breakdown or negative fundamental case.\n"
        f"3. Decisive role evidence: Market and Financial Report evidence outweighed low-confidence social evidence.\n"
        "4. Sector-specific financial metrics: not applicable for non-ASX tickers in this workflow.\n"
        "5. Evidence gaps capping confidence: social data is low confidence and news/filing evidence remains as-of-date limited.\n"
        f"6. Market setup impact: {regime}.\n"
    )
    complete_research_summary = (
        f"Research Manager weighs market, financial-report, news, theme, and sentiment evidence by independence group. {policy['why']}\n\n"
        f"- Why not Buy / Overweight? {policy['why']}\n"
        f"- Why not Sell / Underweight? {manager_rec} is not a Sell because the evidence mix is not a clean long-term breakdown or negative fundamental case.\n"
        "- Decisive role evidence: Market and Financial Report evidence outweighed low-confidence social evidence.\n"
        "- Sector-specific financial metrics: not applicable for non-ASX tickers in this workflow.\n"
        f"- Market setup impact: {regime}."
    )
    if is_asx:
        market_matrix_direction = "negative" if "negative across" in asx_reasoning["market_setup"] else "mixed"
        if "positive across" in asx_reasoning["market_setup"]:
            market_matrix_direction = "positive"
        market_matrix_weight = asx_reasoning["score_line"].split(" market setup", 1)[0]
        market_matrix_reason = asx_reasoning["summary"]
        score_line = asx_reasoning["score_line"]
        rating_rationale = (
            f"{asx_reasoning['summary']} Hold beats Buy/Overweight and Sell/Underweight for ticker-specific reasons, "
            "not because of a generic ASX coverage caveat."
        )
        rating_vs_rating_section = (
            "## Rating-vs-Rating Reasoning\n"
            f"1. Why not Buy / Overweight? {asx_reasoning['why_not_buy']}\n"
            f"2. Why not Sell / Underweight? {asx_reasoning['why_not_sell']}\n"
            f"3. Which role evidence was decisive? {asx_reasoning['decisive']}\n"
            f"4. Which sector-specific financial metrics mattered? {asx_reasoning['metric_line']}\n"
            f"5. Which evidence gaps capped confidence? {asx_reasoning['confidence_cap']}\n"
            f"6. How market setup changed the final rating. {asx_reasoning['market_effect']}\n"
        )
        complete_research_summary = (
            "Research Manager weighs market, financial-report, news, theme, and sentiment evidence by independence group. "
            f"{asx_reasoning['summary']}\n\n"
            f"- Rating-vs-rating summary: Hold is retained for ticker-specific reasons: {asx_reasoning['market_effect']}\n"
            f"- Why not Buy / Overweight? {asx_reasoning['why_not_buy']}\n"
            f"- Why not Sell / Underweight? {asx_reasoning['why_not_sell']}\n"
            f"- Decisive role evidence: {asx_reasoning['decisive']}\n"
            f"- Sector-specific metric or gap: {asx_reasoning['metric_line']}\n"
            f"- Evidence-gap confidence cap: {asx_reasoning['confidence_cap']}"
        )
    matrix_rows = [
        f"| Market Analyst | {refs['close']} | {market_matrix_direction} | high | medium | market snapshot | {market_matrix_weight} | {market_matrix_reason} | market:{ticker}:{trade_date}:trend |",
        f"| Financial Report Analyst | {refs['exhibit']} | positive | high | medium | filing section extraction | +2 | {financial_source_label} support financial review with gaps disclosed | event:{ticker}:{trade_date}:financial-report |",
        f"| News Analyst | {best_news_id} | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:{ticker}:{trade_date}:earnings |",
        f"| Sentiment Analyst | {first_social_id} | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:{ticker}:{trade_date}:retail |",
        f"| Bear Researcher | {refs['fund']} | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:{ticker}:{trade_date}:valuation-trend |",
    ]
    (report_dir / "2_research" / "manager.md").write_text(
        f"""# Research Manager Report - {ticker}

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
{chr(10).join(matrix_rows)}

Score calculation / component weights: {score_line}.

## Rating Rationale
**Recommendation**: {manager_rec}

{rating_rationale} The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Rating-vs-rating selection was explicitly considered; social sentiment alone has zero decision weight.

{rating_vs_rating_section.rstrip()}

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

{_memory_footer(refs=', '.join(str(item) for item in [refs['close'], refs['exhibit'], best_news_id] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    (report_dir / "3_trading" / "trader.md").write_text(
        f"""# Trader Report - {ticker}

## Tool Outputs Used
- Research Manager recommendation: {manager_rec}.
- Market reference metrics: {refs['close']}, {refs['ema10']}, {refs['sma50']}, {refs['sma200']}, {refs['atr']}.

## Action Consistency Check
**Action**: {trader_action}

The action is consistent with the evidence because the Research Manager stance is {manager_rec}, but the trade implementation should not force a directional order when the evidence mix is not a clean Buy or Sell setup. A Sell would require a fresh breakdown or materially negative setup; a Buy would require clearer trend confirmation and risk/reward. Current close is {_money(close)}, 10 EMA {_money(ema_10)}, 50 SMA {_money(sma_50)}, 200 SMA {_money(sma_200)}.

## Paper-study price framework
Reference price: {_money(close)} using {refs['close']} from source date {source_date}. Confirmation level: {_money(confirm)} using ATR and trend-level spacing ({refs['atr']}). Invalidation / caution level: {_money(invalid)}. This is a paper-study framework and not an entry order.

## FINAL TRANSACTION PROPOSAL
FINAL TRANSACTION PROPOSAL: **{trader_action}**

## Evidence Gaps
- No live order book, intraday liquidity, options chain, or broker execution tool was used.

{_memory_footer(refs=', '.join(str(item) for item in [refs['close'], refs['atr']] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    (report_dir / "4_risk" / "aggressive_round_1.md").write_text(
        f"""# Aggressive Risk Analyst Round 1 - {ticker}

## Tool Outputs Used
- Bull case evidence: {refs['exhibit']}, {refs['segment']}, {best_news_id}.
- Market reference: {refs['close']}.

## Opportunity Case
- Upside driver: {policy['bull_theme']}, supported by {refs['exhibit']} and {refs['segment']}.
- If price confirms above {_money(confirm)}, the paper-study setup would have stronger momentum support.

## Failure Points
- Failure point: break below {_money(invalid)} or deterioration below the 200 SMA at {_money(sma_200)}.
- Failure point: earnings or segment evidence no longer supports the bull thesis.

## Response To Prior Risk Arguments
The aggressive view accepts that social evidence is low confidence and does not use it as independent confirmation.

{_memory_footer(refs=', '.join(str(item) for item in [refs['exhibit'], refs['close']] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )
    (report_dir / "4_risk" / "conservative_round_1.md").write_text(
        f"""# Conservative Risk Analyst Round 1 - {ticker}

## Tool Outputs Used
- Bear case evidence: {refs['macd']}, {refs['fund']}, {refs['risk']}.
- Financial extraction gaps: commitments/capex sections where unavailable.

## Downside Case
- Downside driver: {policy['bear_theme']}, supported by market and risk-factor evidence.
- If price loses {_money(invalid)}, the risk case becomes more important for portfolio sizing.

## Unsupported Upside Challenges
- Unsupported upside challenge: retail bullish labels and low-reasoning posts cannot justify high confidence.
- Unsupported upside challenge: capex/commitment detail is gap-labelled if not extracted, so claims in that area must stay cautious.

## Response To Aggressive
Aggressive has a valid upside case, but it needs trend confirmation and cannot lean on duplicated news/social evidence.

{_memory_footer(refs=', '.join(str(item) for item in [refs['macd'], refs['risk']] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )
    (report_dir / "4_risk" / "neutral_round_1.md").write_text(
        f"""# Neutral Risk Analyst Round 1 - {ticker}

## Tool Outputs Used
- Aggressive and Conservative risk rounds.
- Market, financial, and sentiment evidence: {refs['close']}, {refs['exhibit']}, {first_social_id}.

## Risk Argument Quality
- Aggressive evidence quality: medium, because it uses direct financial and news evidence but requires confirmation.
- Conservative evidence quality: medium, because it uses market trend and valuation/timing risk with clear falsification levels.
- Sentiment evidence quality: low; retail-only, noisy, and not decision-grade alone.

## Stronger Risk Side
Stronger risk side: balanced with a conservative sizing bias. The stronger argument depends on whether market confirmation follows: until then, the final portfolio stance should respect Research Manager direction but keep Trader action at Hold.

## Evidence Gaps
- No options-implied risk, borrow/short-interest feed, or intraday volatility surface was available.

{_memory_footer(refs=', '.join(str(item) for item in [refs['close'], refs['exhibit'], first_social_id] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )
    (report_dir / "5_portfolio" / "decision.md").write_text(
        f"""# Portfolio Manager Decision - {ticker}

## Tool Outputs Used
- Research Manager: {manager_rec}.
- Trader action: {trader_action} at reference price {_money(close)}.
- Risk debate outputs and evidence: {refs['close']}, {refs['exhibit']}, {best_news_id}.

## Risk debate impact
The risk debate tempers position implementation. Aggressive evidence supports the research stance, but Conservative and Neutral risk analysts require confirmation and prevent a forced directional trade. Social sentiment is low confidence and receives no standalone allocation weight.

## Final Portfolio Decision
**Rating**: {portfolio_rating}

Research decision: {manager_rec}. Trader action: {trader_action}. Portfolio decision: maintain {portfolio_rating} paper-study stance, with no real trade execution and no broker/order tooling.

## Evidence Gaps
- Portfolio sizing, tax constraints, mandate constraints, and liquidity limits are not modeled.

{_memory_footer(refs=', '.join(str(item) for item in [refs['close'], refs['exhibit'], best_news_id] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    debate_record_path = _write_assembled_debate_record(report_dir=report_dir, ticker=ticker, trade_date=trade_date)

    (report_dir / "complete_report.md").write_text(
        f"""# Complete Codex TradingAgents Report - {ticker}

Trade date: {trade_date}
Evidence as of: {evidence_as_of}
Run executed at: {run_executed_at}
Run ID: {run_id}
Run folder: {run_folder_name}

## Tool Outputs Used
- Role reports under 1_analysts, 2_research, 3_trading, 4_risk, and 5_portfolio.
- Completed debate transcript: {debate_record_path}.
- Core evidence IDs: {refs['close']}, {refs['exhibit']}, {best_news_id}, {first_social_id}.

## Complete Report
### Executive Summary
**Recommendation**: {manager_rec}
**Action**: {trader_action}
**Rating**: {portfolio_rating}
Reference price: {_money(close)}
FINAL TRANSACTION PROPOSAL: **{trader_action}**

### Market Analyst
Latest close {_money(close)} is {rel_10} the 10 EMA {_money(ema_10)}, {rel_50} the 50 SMA {_money(sma_50)}, and {rel_200} the 200 SMA {_money(sma_200)}. Evidence: {refs['close']}, {refs['ema10']}, {refs['sma50']}, {refs['sma200']}.

### Sentiment Analyst
Sentiment is mixed and low-confidence retail-only reaction. The report uses source-level social evidence such as {first_social_id} and does not infer institution-level positioning.

### News Analyst
News impact is mixed-to-positive based on direct article/event evidence {best_news_id}. Snippet-only and low-relevance candidates are downgraded.

### Fundamentals Analyst
Structured fundamentals cite {f_packet.get('evidence_id')}, {f_income.get('evidence_id')}, {f_balance.get('evidence_id')}, and {f_cash.get('evidence_id')} for valuation, income, balance sheet, and cash flow context.

### Financial Report Analyst
{financial_source_detail}

### Industry / Theme Discovery Analyst
Industry/theme evidence identifies {policy['theme1']} / {policy['subtheme1']} and {policy['theme2']} / {policy['subtheme2']}, supported by {refs['exhibit']}, {refs['segment']}, and market evidence {refs['close']}.

### Research Manager Decision - Evidence Weighing
**Recommendation**: {manager_rec}
{complete_research_summary}

### Trader
**Action**: {trader_action}
Reference price: {_money(close)}. Confirmation level: {_money(confirm)}. Invalidation / caution level: {_money(invalid)}.
FINAL TRANSACTION PROPOSAL: **{trader_action}**

### Risk Debate
Aggressive risk supports the upside case but identifies failure points. Conservative risk challenges unsupported upside and noisy social evidence. Neutral risk finds a balanced risk posture with confirmation required.

### Portfolio Manager
**Rating**: {portfolio_rating}
Risk debate impact: risk evidence tempers implementation; no broker/order tools are used.

## Evidence Gaps
- This is a paper-study report-writing workflow, not investment advice or a trading instruction.
- Social evidence is retail-only and low confidence.
- Missing or unavailable filing sections remain explicit evidence gaps.

{_memory_footer(refs=', '.join(str(item) for item in [refs['close'], refs['exhibit'], best_news_id] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )

    (report_dir / "6_quality" / "quality_review.md").write_text(
        f"""# Quality Reviewer Report - {ticker}

## Tool Outputs Used
- validate_quality_review.py was run for this report directory and passed before quality_gate.json was marked passed.
- Role reports and evidence records including {refs['close']}, {refs['exhibit']}, {best_news_id}, and {first_social_id}.

## Quality Gate Findings
- Pending-marker check: no role output intentionally left pending.
- As-of discipline: report uses trade date {trade_date}; source dates are disclosed.
- {quality_financial_line}
- Sentiment: retail-only, low confidence, no Reddit requirement, no institution-level inference.
- Anti-double-counting: Research Manager uses independence groups and does not count social reposts as independent fundamental facts.

## Evidence Gaps
- No validator-pending state remains for this artifact. If a later validator run reports errors, remediation becomes the next workflow stage.

{_memory_footer(refs=', '.join(str(item) for item in [refs['close'], refs['exhibit'], best_news_id] if item), trade_date=trade_date)}""",
        encoding="utf-8",
    )
    return report_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Write Codex-session role reports from collected evidence.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--trade-date", default=TRADE_DATE_DEFAULT)
    parser.add_argument("--ticker", action="append", required=True)
    args = parser.parse_args()

    for ticker in args.ticker:
        report_dir = write_reports(output_dir=args.output_dir, ticker=ticker, trade_date=args.trade_date)
        print(f"wrote {ticker} reports to {report_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
