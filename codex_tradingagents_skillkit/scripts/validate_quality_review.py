from __future__ import annotations

import argparse
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROLE_REQUIRED_SECTIONS = {
    ("1_analysts", "market.md"): ["Tool Outputs Used", "Quantitative Regime / Tool Outputs"],
    ("1_analysts", "sentiment.md"): [
        "Tool Outputs Used",
        "Sentiment Evidence Quality Summary",
        "Source Quality Table",
        "Top Reasoned Items",
        "Excluded / Downgraded Evidence",
        "Event Context vs Reaction Evidence",
        "Final Sentiment Interpretation",
    ],
    ("1_analysts", "news.md"): ["Tool Outputs Used", "Article Evidence Cards"],
    ("1_analysts", "fundamentals.md"): ["Tool Outputs Used", "Financial Statement Evidence", "Sector-Specific Metrics"],
    ("1_analysts", "financial_report.md"): ["Tool Outputs Used", "Claim-Source Table"],
    ("1_analysts", "industry_theme.md"): ["Tool Outputs Used", "Theme Evidence Table"],
    ("2_research", "bull_round_1.md"): ["Tool Outputs Used", "Strongest Bull Evidence", "Falsification Conditions"],
    ("2_research", "bear_round_1.md"): ["Tool Outputs Used", "Strongest Bear Evidence", "Falsification Conditions", "Response To Bull"],
    ("2_research", "manager.md"): ["Tool Outputs Used", "Structured Evidence Matrix", "Rating-vs-Rating Reasoning"],
    ("3_trading", "trader.md"): ["Tool Outputs Used", "Action Consistency Check", "Paper-study price framework"],
    ("4_risk", "aggressive_round_1.md"): ["Tool Outputs Used", "Opportunity Case", "Failure Points"],
    ("4_risk", "conservative_round_1.md"): ["Tool Outputs Used", "Downside Case", "Unsupported Upside Challenges"],
    ("4_risk", "neutral_round_1.md"): ["Tool Outputs Used", "Risk Argument Quality", "Stronger Risk Side"],
    ("5_portfolio", "decision.md"): ["Tool Outputs Used", "Risk debate impact", "Final Portfolio Decision"],
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _section(text: str, heading: str) -> str:
    match = re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^#{2,3}\s+", rest, re.MULTILINE)
    return rest[: next_heading.start()] if next_heading else rest


def _has_section(text: str, section_name: str) -> bool:
    return re.search(rf"^#+\s+{re.escape(section_name)}\s*$", text, re.MULTILINE) is not None


def _is_pending(text: str) -> bool:
    return "Pending Codex role output" in text


def _asx_source_collection_failed(evidence_path: Path | None) -> bool:
    if not evidence_path:
        return False
    try:
        evidence = json.loads(_read(evidence_path))
    except (OSError, json.JSONDecodeError):
        return False
    ticker = str(evidence.get("ticker", "")).upper()
    if not ticker.endswith(".AX"):
        return False
    financial = evidence.get("roles", {}).get("financial_report", {})
    calls = financial.get("tool_calls", {})
    source_call = calls.get("collect_financial_document_sources", {})
    status = str(source_call.get("status", "")).lower()
    output = str(source_call.get("output", "")).lower()
    blocker = bool(source_call.get("external_blocker_documented")) or "external blocker" in output
    if blocker:
        return False
    return status in {"error", "unavailable"} or "asx_announcements | error" in output


def _is_asx_evidence(evidence_path: Path | None) -> bool:
    if not evidence_path:
        return False
    try:
        evidence = json.loads(_read(evidence_path))
    except (OSError, json.JSONDecodeError):
        return False
    return str(evidence.get("ticker", "")).upper().endswith(".AX")


def _structured_evidence_dir(evidence_path: Path | None) -> Path | None:
    if not evidence_path:
        return None
    return evidence_path.parent


def _read_json_file(path: Path) -> object | None:
    try:
        return json.loads(_read(path))
    except (OSError, json.JSONDecodeError):
        return None


def _status_is_available(record: dict[str, object]) -> bool:
    return str(record.get("status", "")).lower() == "available"


def _record_mentions(record: dict[str, object], *needles: str) -> bool:
    haystack_parts = [
        str(record.get("section_name", "")),
        str(record.get("source_type", "")),
        " ".join(str(item) for item in record.get("supports_claims", []) or []),
    ]
    haystack = " ".join(haystack_parts).lower()
    return any(needle.lower() in haystack for needle in needles)


def _structured_evidence_quality_errors(evidence_path: Path | None) -> list[str]:
    evidence_dir = _structured_evidence_dir(evidence_path)
    if not evidence_dir:
        return []

    errors: list[str] = []
    source_attempts = _read_json_file(evidence_dir / "news" / "source_attempts.json")
    if isinstance(source_attempts, list) and source_attempts:
        attempted = [attempt for attempt in source_attempts if isinstance(attempt, dict)]
        if attempted and all(bool(attempt.get("fallback_used")) for attempt in attempted):
            errors.append("upstream fallback is the only attempted news source; review-grade quality gate cannot pass")

    news_candidates = _read_json_file(evidence_dir / "news" / "candidates.json")
    if isinstance(news_candidates, list) and news_candidates:
        candidate_rows = [candidate for candidate in news_candidates if isinstance(candidate, dict)]
        if candidate_rows and all(str(candidate.get("source_type", "")).lower() == "upstream_fallback" for candidate in candidate_rows):
            errors.append("upstream fallback is the only available news candidate; review-grade quality gate cannot pass")
    elif isinstance(source_attempts, list) and source_attempts:
        errors.append("news source discovery found no usable news candidates; review-grade quality gate cannot pass")

    article_cards = _read_json_file(evidence_dir / "news" / "article_cards.json")
    if isinstance(article_cards, list) and article_cards:
        if not isinstance(source_attempts, list) or not source_attempts:
            errors.append("news source attempts are missing; review-grade quality gate cannot pass")
        usable_text_count = 0
        for card in [card for card in article_cards if isinstance(card, dict)]:
            text_status = str(card.get("text_status") or card.get("full_text_status") or "").lower()
            legacy_status = str(card.get("full_text_status", "")).lower()
            confidence = str(card.get("confidence", "")).lower()
            quality_score = int(card.get("content_quality_score") or 0)
            quality_flags = {str(flag) for flag in card.get("quality_flags", []) or []}
            key_facts = card.get("key_facts_for_codex") or card.get("key_facts") or []
            entity_hits = card.get("company_entity_hits") or []
            valid_for_trade_date = bool((card.get("as_of_validity") or {}).get("valid_for_trade_date", True))
            if valid_for_trade_date and (text_status in {"full_text_verified", "partial_text"} or legacy_status == "full_text"):
                usable_text_count += 1
            if text_status in {"error_page", "blocked_or_paywalled", "video_without_transcript", "invalid_or_irrelevant"} and legacy_status == "full_text":
                errors.append("weak or blocked news article is treated as full text; review-grade quality gate cannot pass")
                break
            if text_status in {"snippet_only", "metadata_only", "blocked_or_paywalled", "error_page", "video_without_transcript"} and confidence == "high":
                errors.append("weak news article evidence cannot be high confidence")
                break
            if quality_score and quality_score < 50 and confidence in {"medium", "high"}:
                errors.append("low-quality news article evidence cannot be medium or high confidence")
                break
            if "no_company_entity_match" in quality_flags and confidence in {"medium", "high"}:
                errors.append("news article with no company entity match cannot be medium or high confidence")
                break
            if "generic_landing_or_navigation_page" in quality_flags and str(card.get("materiality", "")).lower() != "context_only":
                errors.append("generic official or navigation page must be context-only news evidence")
                break
            if (
                str(card.get("materiality_readiness", "")) == "ready_for_codex_interpretation"
                and not key_facts
                and not entity_hits
            ):
                errors.append("material-ready news evidence needs key facts or a company entity match")
                break
            if not valid_for_trade_date and (
                legacy_status == "full_text"
                or confidence in {"medium", "high"}
                or str(card.get("materiality_readiness", "")) == "ready_for_codex_interpretation"
            ):
                errors.append("post-trade-date news article cannot support review-grade evidence")
                break
        if usable_text_count == 0:
            errors.append("news evidence has no full-text articles; review-grade quality gate cannot pass")

    social_cards = _read_json_file(evidence_dir / "social" / "social_cards.json")
    social_summary = _read_json_file(evidence_dir / "social" / "social_summary.json")
    if isinstance(social_cards, list) and social_cards:
        cards = [card for card in social_cards if isinstance(card, dict)]
        if any(not bool((card.get("as_of_validity") or {}).get("valid_for_trade_date", True)) for card in cards):
            errors.append("post-trade-date social item cannot support sentiment evidence")
        direct_cards = [card for card in cards if str(card.get("ticker_relevance", "")) == "direct_company"]
        reasoned_cards = [card for card in direct_cards if str(card.get("reasoning_quality", "")) in {"medium", "high"}]
        if isinstance(social_summary, dict):
            sources = social_summary.get("sources", [])
            if isinstance(sources, list):
                for source in sources:
                    if not isinstance(source, dict):
                        continue
                    confidence = str(source.get("confidence", "")).lower()
                    if confidence in {"medium", "high"} and direct_cards and not reasoned_cards:
                        errors.append("sentiment source confidence is unsupported by social item quality")
                        break
                    source_category = str(source.get("source_confidence_category", ""))
                    if confidence == "high" and source_category in {
                        "ticker_specific_retail_platform",
                        "broad_social_discussion",
                        "anonymous_forum_or_comment",
                    }:
                        errors.append("retail-only or broad-social sentiment cannot be high confidence")
                        break
    if isinstance(social_summary, dict):
        sources = social_summary.get("sources", [])
        if isinstance(sources, list):
            for source in sources:
                if not isinstance(source, dict):
                    continue
                if str(source.get("status", "")).lower() == "rate_limited" and "reddit" in str(source.get("source", "")).lower():
                    run_root = evidence_dir.parents[2]
                    ticker = evidence_dir.parent.name
                    trade_date = evidence_dir.name
                    sentiment_path = run_root / "reports" / ticker / trade_date / "1_analysts" / "sentiment.md"
                    sentiment_text = _read(sentiment_path)
                    if sentiment_text and not re.search(r"reddit[_ -]?rate[_ -]?limited|rate limit", sentiment_text, re.IGNORECASE):
                        errors.append("reddit rate limit is hidden from sentiment report")
                    if re.search(r"reddit.*(?:neutral|no impact)|neutral.*reddit", sentiment_text, re.IGNORECASE):
                        errors.append("reddit unavailable or rate-limited state is treated as neutral sentiment")
                    break

    section_records = _read_json_file(evidence_dir / "financial_report" / "section_records.json")
    if isinstance(section_records, list) and section_records:
        records = [record for record in section_records if isinstance(record, dict)]
        has_available_mda = any(_status_is_available(record) and _record_mentions(record, "md&a", "management discussion") for record in records)
        if not has_available_mda:
            errors.append("financial evidence lacks extracted MD&A; review-grade quality gate cannot pass")

        has_earnings_cover = any(_record_mentions(record, "earnings_release_8k_cover_page", "8-k cover page") for record in records)
        has_available_exhibit = any(
            _status_is_available(record) and _record_mentions(record, "earnings_release_exhibit", "exhibit 99.1")
            for record in records
        )
        if has_earnings_cover and not has_available_exhibit:
            errors.append("earnings 8-K exhibit is unavailable; cover page cannot support earnings-release detail")

        has_available_cash_flow = any(
            _status_is_available(record) and _record_mentions(record, "cash flow statement")
            for record in records
        )
        if not has_available_cash_flow:
            errors.append("financial evidence lacks extracted cash-flow statement section; review-grade quality gate cannot pass")

        errors.extend(_asx_sector_metric_quality_errors(evidence_path, records))

    return errors


ASX_REQUIRED_SECTOR_METRICS = {
    "banks": {"net_interest_margin", "cet1", "loan_growth", "arrears", "impairment", "dividend", "roe"},
    "miners": {"production", "realised_price", "unit_cost_aisc", "capex", "reserves_resources", "commodity_exposure"},
    "healthcare": {"segment_revenue", "r_and_d", "plasma_collections", "margins", "debt", "guidance"},
    "health_insurers": {"premium_growth", "claims_ratio", "membership", "capital_adequacy"},
    "retailers": {"sales_growth", "ebit_margin", "inventory", "capex", "dividends"},
}


def _asx_sector_metric_quality_errors(evidence_path: Path | None, records: list[dict[str, object]]) -> list[str]:
    if not _is_asx_evidence(evidence_path):
        return []
    metric_records = [
        record
        for record in records
        if str(record.get("section_kind") or record.get("section_type") or "") == "sector_metric"
        or str(record.get("section_name", "")).startswith("sector_metric_")
    ]
    if not metric_records:
        return ["ASX sector-specific metrics are missing without evidence-gap disclosure"]
    sector = str(next((record.get("sector") for record in metric_records if record.get("sector")), "") or "")
    required = ASX_REQUIRED_SECTOR_METRICS.get(sector, set())
    if not required:
        return []
    by_metric = {str(record.get("metric_name") or "").lower(): record for record in metric_records}
    errors: list[str] = []
    for metric in sorted(required):
        record = by_metric.get(metric)
        if not record:
            errors.append(f"ASX sector metric {metric} is missing without evidence-gap disclosure")
            break
        if str(record.get("status", "")).lower() != "available" and not (
            record.get("evidence_gap") or record.get("unavailable_reason")
        ):
            errors.append(f"ASX sector metric {metric} is unavailable without evidence-gap disclosure")
            break
    return errors


def _news_quality_errors(news_path: Path) -> list[str]:
    if not news_path.exists():
        return []
    text = _read(news_path)
    if _is_pending(text):
        return []

    errors: list[str] = []
    article_cards = _section(text, "## Article Evidence Cards")
    for line in article_cards.splitlines():
        normalized = line.lower().replace("-", "_")
        if "snippet_only" in normalized and re.search(r"\|\s*high\s*(?:\||$)", normalized):
            errors.append("snippet-only news evidence cannot be high confidence")
            break

    impact_summary = _section(text, "## News Impact Summary")
    if not impact_summary:
        impact_summary = _section(text, "### News Impact Summary")
    if re.search(
        r"\b(material positive|material negative|positive|negative|mixed)\b",
        impact_summary,
        re.IGNORECASE,
    ) and not re.search(r"\bnews:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}\b", impact_summary):
        errors.append("news impact label lacks article evidence citation")
    return errors


def _markdown_table_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def _financial_quality_errors(financial_path: Path) -> list[str]:
    if not financial_path.exists():
        return []
    text = _read(financial_path)
    if _is_pending(text):
        return []

    errors: list[str] = []
    table = _section(text, "## Claim-Source Table")
    if not table:
        table = _section(text, "### Claim-Source Table")
    rows = _markdown_table_rows(table)
    if len(rows) < 2:
        return errors
    header = [cell.lower() for cell in rows[0]]
    for row in rows[1:]:
        if len(row) < len(header):
            row = [*row, *([""] * (len(header) - len(row)))]
        cells = dict(zip(header, row, strict=False))
        claim = cells.get("claim", "")
        if not claim:
            continue
        source_document = cells.get("source document", "")
        section = cells.get("section / exhibit", "") or cells.get("section", "")
        evidence_gap = cells.get("evidence gap", "") or cells.get("evidence gap if section/exhibit is missing", "")
        source_blob = f"{source_document} {section} {claim}"
        has_citation = bool(
            re.search(r"\bfinancial:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}\b", source_blob)
            or re.search(
                r"10-K|10-Q|8-K|Exhibit\s+99\.1|ASX|structured fundamentals packet",
                source_blob,
                re.IGNORECASE,
            )
        )
        unavailable_section = bool(
            re.search(r"unavailable|missing|not extracted|not available", f"{section} {source_document}", re.IGNORECASE)
        )
        if not has_citation and not evidence_gap:
            errors.append("financial claim lacks section evidence citation")
            break
        if unavailable_section and not evidence_gap:
            errors.append("financial evidence gap missing for unavailable section")
            break
    return errors


METRIC_VALUE_PATTERNS = {
    "latest_close": [
        r"\bLatest\s+close\s*[:|]\s*\$?(-?\d+(?:\.\d+)?)",
        r"\bClose\s*[:|]\s*\$?(-?\d+(?:\.\d+)?)",
    ],
    "ema_10": [r"\b10\s*EMA\s*[:|]\s*\$?(-?\d+(?:\.\d+)?)"],
    "sma_50": [r"\b50\s*SMA\s*[:|]\s*\$?(-?\d+(?:\.\d+)?)"],
    "sma_200": [r"\b200\s*SMA\s*[:|]\s*\$?(-?\d+(?:\.\d+)?)"],
}

METRIC_CONFLICT_PHRASES = {
    "ema_10": {
        "above": [r"\babove\s+(?:the\s+)?10\s*EMA\b"],
        "below": [r"\bbelow\s+(?:the\s+)?10\s*EMA\b"],
    },
    "sma_50": {
        "above": [r"\babove\s+(?:the\s+)?50\s*SMA\b", r"\babove\s+(?:the\s+)?50-day\b"],
        "below": [r"\bbelow\s+(?:the\s+)?50\s*SMA\b", r"\bbelow\s+(?:the\s+)?50-day\b"],
    },
    "sma_200": {
        "above": [r"\babove\s+(?:the\s+)?200\s*SMA\b", r"\babove\s+(?:the\s+)?200-day\b"],
        "below": [r"\bbelow\s+(?:the\s+)?200\s*SMA\b", r"\bbelow\s+(?:the\s+)?200-day\b"],
    },
}


def _metric_values(text: str) -> dict[str, float]:
    values: dict[str, float] = {}
    for metric, patterns in METRIC_VALUE_PATTERNS.items():
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                values[metric] = float(match.group(1))
                break
    return values


def _contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def _market_quality_errors(market_path: Path) -> list[str]:
    if not market_path.exists():
        return []
    text = _read(market_path)
    if _is_pending(text):
        return []

    values = _metric_values(text)
    latest_close = values.get("latest_close")
    if latest_close is None:
        return []

    errors: list[str] = []
    for metric in ("ema_10", "sma_50", "sma_200"):
        metric_value = values.get(metric)
        if metric_value is None:
            continue
        actual_relation = "above" if latest_close > metric_value else "below" if latest_close < metric_value else "equal"
        phrases = METRIC_CONFLICT_PHRASES[metric]
        if actual_relation == "below" and _contains_any(text, phrases["above"]):
            errors.append("market moving-average claim conflicts with metric evidence")
            break
        if actual_relation == "above" and _contains_any(text, phrases["below"]):
            errors.append("market moving-average claim conflicts with metric evidence")
            break
    return errors


def _sentiment_quality_errors(sentiment_path: Path) -> list[str]:
    if not sentiment_path.exists():
        return []
    text = _read(sentiment_path)
    if _is_pending(text):
        return []
    errors: list[str] = []
    raw_social_lines = re.findall(r"^\[\d{4}-\d{2}-\d{2}T.*?@.*?\]", text, re.MULTILINE)
    if len(raw_social_lines) > 3:
        errors.append("sentiment report includes raw social feed instead of summary")
    if re.search(r"institutional sentiment", text, re.IGNORECASE) and re.search(
        r"StockTwits|Reddit|retail", text, re.IGNORECASE
    ):
        errors.append("retail social feed cannot support institutional sentiment")
    if "Social Evidence Processing Rules" in text and not re.search(r"usable .*items|usable ticker", text, re.IGNORECASE):
        errors.append("sentiment report lacks usable social item summary")
    if (
        re.search(r"\b\d+%|bullish\s*/\s*bearish|bullish_count|bearish_count|platform labels?", text, re.IGNORECASE)
        and re.search(r"\bhigh\b", text, re.IGNORECASE)
        and not re.search(r"reasoned|reasoning quality|low-information|source limitation", text, re.IGNORECASE)
    ):
        errors.append("sentiment conclusion is based only on raw social counts or platform labels")
    if re.search(r"news[/\\]article_cards\.json|News Analyst article cards", text, re.IGNORECASE) and re.search(
        r"independent(?:ly)?\s+(?:bearish|bullish|negative|positive)|independent sentiment",
        text,
        re.IGNORECASE,
    ):
        errors.append("Sentiment Analyst treats News Analyst article cards as independent sentiment evidence")
    if re.search(r"reddit.*required|required.*reddit", text, re.IGNORECASE):
        errors.append("Reddit is treated as required sentiment evidence")
    if re.search(r"StockTwits|Reddit", text, re.IGNORECASE) and re.search(r"\bhigh confidence\b", text, re.IGNORECASE):
        errors.append("high confidence is assigned to retail-only sentiment")
    top_reasoned = _section(text, "## Top Reasoned Items")
    if top_reasoned:
        rows = _markdown_table_rows(top_reasoned)
        if len(rows) >= 2:
            header = [cell.lower() for cell in rows[0]]
            quality_index = next((index for index, cell in enumerate(header) if "reasoning quality" in cell), None)
            if quality_index is not None:
                for row in rows[1:]:
                    if len(row) > quality_index and row[quality_index].strip().lower() == "low":
                        errors.append("Top Reasoned Items cannot include low reasoning-quality social items")
                        break
    return errors


def _fundamentals_quality_errors(fundamentals_path: Path) -> list[str]:
    if not fundamentals_path.exists():
        return []
    text = _read(fundamentals_path)
    if _is_pending(text):
        return []
    errors: list[str] = []
    if not re.search(r"fundamentals:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}", text):
        errors.append("fundamentals claim lacks statement evidence citation")
    if "Sector-Specific Metrics" in text and not re.search(
        r"gap|NIM|CET1|production|capex|premium|claims ratio|inventory|plasma|same-store|R&D",
        text,
        re.IGNORECASE,
    ):
        errors.append("fundamentals sector metrics are not sector-specific or gap-labelled")
    return errors


def _complete_report_trade_date_errors(report_dir: Path, complete_text: str) -> list[str]:
    if not complete_text:
        return []
    trade_date_match = re.search(r"^Trade date:\s*(\d{4}-\d{2}-\d{2})\s*$", complete_text, re.MULTILINE)
    if not trade_date_match:
        return []
    report_folder_date = report_dir.name
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", report_folder_date) and report_folder_date != trade_date_match.group(1):
        return ["report folder trade_date and complete_report.md trade_date disagree"]
    return []


def _asx_financial_claim_support_errors(report_dir: Path, evidence_path: Path | None) -> list[str]:
    if not _is_asx_evidence(evidence_path):
        return []
    errors: list[str] = []
    for path in [report_dir / "complete_report.md", report_dir / "1_analysts" / "financial_report.md"]:
        text = _read(path)
        if not text or _is_pending(text):
            continue
        if re.search(
            r"financial (?:strength|weakness)|balance sheet strength|cash flow strength",
            text,
            re.IGNORECASE,
        ) and not re.search(r"\bfinancial:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}\b|evidence gap", text, re.IGNORECASE):
            errors.append("ASX financial strength/weakness claim lacks source section or metric evidence")
            break
    return errors


def _market_setup_from_evidence(evidence_path: Path | None) -> tuple[str, dict[str, float]]:
    evidence_dir = _structured_evidence_dir(evidence_path)
    if not evidence_dir:
        return "", {}
    records = _read_json_file(evidence_dir / "market" / "quantitative_observations.json")
    if not isinstance(records, list):
        return "", {}
    values: dict[str, float] = {}
    for record in records:
        if not isinstance(record, dict):
            continue
        name = str(record.get("metric_name") or "")
        if name in {"latest_close", "ema_10", "sma_50", "sma_200"}:
            try:
                values[name] = float(record.get("value"))
            except (TypeError, ValueError):
                continue
    required = {"latest_close", "ema_10", "sma_50", "sma_200"}
    if not required.issubset(values):
        return "", values
    close = values["latest_close"]
    setup = (
        ("above" if close > values["ema_10"] else "below" if close < values["ema_10"] else "at"),
        ("above" if close > values["sma_50"] else "below" if close < values["sma_50"] else "at"),
        ("above" if close > values["sma_200"] else "below" if close < values["sma_200"] else "at"),
    )
    return "/".join(setup), values


def _asx_research_specificity_errors(research_path: Path, evidence_path: Path | None) -> list[str]:
    if not research_path.exists() or not _is_asx_evidence(evidence_path):
        return []
    text = _read(research_path)
    if _is_pending(text):
        return []
    errors: list[str] = []
    setup, _values = _market_setup_from_evidence(evidence_path)
    if setup and not all(term in text for term in ["10 EMA", "50 SMA", "200 SMA"]):
        errors.append("ASX Research Manager report lacks ticker-specific market moving-average facts")
    if "Rating-vs-Rating Reasoning" not in text:
        errors.append("ASX Research Manager report lacks rating-vs-rating reasoning")
    sector_section = _section(text, "## Rating-vs-Rating Reasoning") or text
    has_sector_metric = bool(
        re.search(
            r"sector-specific financial metrics|sector metric|NIM|CET1|loan growth|arrears|impairment|ROE|production|realised price|unit cost|AISC|reserves|commodity exposure|segment revenue|R&D|plasma collections|premium growth|claims ratio|membership|capital adequacy|sales growth|EBIT margin|inventory|capex|dividends?",
            sector_section,
            re.IGNORECASE,
        )
    )
    has_gap = "evidence gap" in sector_section.lower()
    has_financial_id = re.search(r"financial:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}", sector_section) is not None
    if not (has_sector_metric and (has_financial_id or has_gap)):
        errors.append("ASX Research Manager report lacks ticker-specific sector metric or evidence-gap reference")
    rationale = _section(text, "## Rating Rationale") or text
    if "ASX source coverage is uneven" in rationale and not (
        all(term in rationale for term in ["10 EMA", "50 SMA", "200 SMA"]) and has_sector_metric
    ):
        errors.append("generic ASX source coverage cannot be the sole reason for Hold")
    return errors


def _asx_complete_report_research_manager_errors(report_dir: Path, evidence_path: Path | None) -> list[str]:
    if not _is_asx_evidence(evidence_path):
        return []
    manager_path = report_dir / "2_research" / "manager.md"
    complete_path = report_dir / "complete_report.md"
    if not manager_path.exists() or not complete_path.exists():
        return []
    manager_text = _read(manager_path)
    complete_text = _read(complete_path)
    if _is_pending(manager_text) or _is_pending(complete_text):
        return []
    if "Rating-vs-Rating Reasoning" not in manager_text:
        return []

    research_section = _section(complete_text, "### Research Manager Decision - Evidence Weighing")
    if not research_section:
        return ["complete_report.md omits Research Manager Decision - Evidence Weighing section"]

    errors: list[str] = []
    recommendation = _recommendation_from_research(manager_text)
    if recommendation and not re.search(rf"\*\*Recommendation\*\*\s*:\s*{re.escape(recommendation)}\b", research_section, re.IGNORECASE):
        errors.append("complete_report.md Research Manager section does not include the actual Research Manager recommendation")
    if not all(term in research_section for term in ["10 EMA", "50 SMA", "200 SMA"]):
        errors.append("complete_report.md Research Manager section does not reflect ticker-specific moving-average setup")
    has_sector_metric_or_gap = bool(
        re.search(
            r"sector-specific metric|sector metric|evidence gap|NIM|CET1|loan growth|arrears|impairment|ROE|production|realised price|unit cost|AISC|reserves|commodity exposure|segment revenue|R&D|plasma collections|premium growth|claims ratio|membership|capital adequacy|sales growth|EBIT margin|inventory|capex|dividends?",
            research_section,
            re.IGNORECASE,
        )
    )
    if not has_sector_metric_or_gap:
        errors.append("complete_report.md Research Manager section lacks sector metric or explicit evidence gap")
    has_rating_vs_rating = bool(
        re.search(r"why not buy|buy\s*/\s*overweight|rating-vs-rating|why not sell|sell\s*/\s*underweight", research_section, re.IGNORECASE)
    )
    if not has_rating_vs_rating:
        errors.append("complete_report.md Research Manager section lacks concise rating-vs-rating reasoning")
    has_decisive_evidence = bool(re.search(r"decisive role evidence|market analyst|financial report analyst", research_section, re.IGNORECASE))
    if not has_decisive_evidence:
        errors.append("complete_report.md Research Manager section lacks decisive role evidence")
    if "ASX source coverage is uneven" in research_section and not (
        all(term in research_section for term in ["10 EMA", "50 SMA", "200 SMA"]) and has_rating_vs_rating and has_sector_metric_or_gap
    ):
        errors.append("complete_report.md uses generic ASX source coverage as the main Research Manager rationale")
    return errors


def _research_manager_quality_errors(research_path: Path) -> list[str]:
    if not research_path.exists():
        return []
    text = _read(research_path)
    if _is_pending(text):
        return []
    matrix = _section(text, "## Structured Evidence Matrix") or _section(text, "### Structured Evidence Matrix")
    if not matrix:
        return []
    errors: list[str] = []
    for required in ["Direction", "Materiality", "Confidence", "Tool output", "Weight", "Reason"]:
        if required.lower() not in matrix.lower():
            errors.append(f"research evidence matrix missing column: {required}")
            break
    rows = _markdown_table_rows(matrix)
    if len(rows) >= 2:
        header = [cell.lower() for cell in rows[0]]
        if any("independence" in cell and "group" in cell for cell in header):
            group_index = next(index for index, cell in enumerate(header) if "independence" in cell and "group" in cell)
            role_index = next((index for index, cell in enumerate(header) if cell == "role" or "source" in cell), None)
            weight_index = next((index for index, cell in enumerate(header) if "weight" in cell), None)
            groups: dict[str, list[dict[str, str]]] = {}
            for row in rows[1:]:
                if len(row) <= group_index:
                    continue
                group = row[group_index].strip()
                if not group:
                    continue
                role = row[role_index].strip().lower() if role_index is not None and len(row) > role_index else ""
                weight = row[weight_index].strip() if weight_index is not None and len(row) > weight_index else ""
                groups.setdefault(group, []).append({"role": role, "weight": weight})
            for group, group_rows in groups.items():
                roles = {row["role"] for row in group_rows}
                has_news = any("news" in role for role in roles)
                has_sentiment = any("sentiment" in role or "social" in role for role in roles)
                if has_news and has_sentiment and group.startswith("event:"):
                    joined_weights = " ".join(row["weight"] for row in group_rows)
                    if re.search(r"-?\s*[12](?:\.0)?\b", joined_weights) or re.search(
                        r"independent signals?|confirm", text, re.IGNORECASE
                    ):
                        errors.append("research manager double-counts one independence group across News and Sentiment")
                        break
        elif re.search(r"news:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}", matrix) and re.search(
            r"social:[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:item:\d{4}",
            matrix,
        ):
            errors.append("research evidence matrix missing independence group column")
    if re.search(r"\b(Buy|Sell|Hold|Underweight|Overweight)\b", text) and not re.search(
        r"why .* wins over|beats Hold|beats Underweight|Sell vs Hold|Hold vs Sell|Underweight", text, re.IGNORECASE
    ):
        errors.append("research manager rating lacks rating-vs-rating justification")
    if re.search(r"evidence score\s+of\s+[+-]?\d+", text, re.IGNORECASE) and not re.search(
        r"score calculation|weight|component", text, re.IGNORECASE
    ):
        errors.append("research manager score is unexplained")
    return errors


def _trader_quality_errors(trader_path: Path) -> list[str]:
    if not trader_path.exists():
        return []
    text = _read(trader_path)
    if _is_pending(text):
        return []
    errors: list[str] = []
    action_match = re.search(r"\bAction\s*[:|-]\s*(BUY|SELL|HOLD|UNDERWEIGHT|OVERWEIGHT)\b", text, re.IGNORECASE)
    final_match = re.search(r"FINAL TRANSACTION PROPOSAL\s*[:|-]\s*(BUY|SELL|HOLD|UNDERWEIGHT|OVERWEIGHT)\b", text, re.IGNORECASE)
    if action_match and final_match and action_match.group(1).upper() != final_match.group(1).upper():
        errors.append("trader final proposal mismatch")
    if final_match and final_match.group(1).upper() in {"BUY", "SELL"} and "Paper-study price framework" not in text:
        errors.append("trader Buy/Sell lacks paper-study price framework")
    if "Sell requires" in text and final_match and final_match.group(1).upper() == "SELL" and not re.search(
        r"below .*200|breakdown|materially negative|material negative", text, re.IGNORECASE
    ):
        errors.append("trader Sell action is not supported by stated Sell condition")
    return errors


def _debate_quality_errors(bull_path: Path, bear_path: Path) -> list[str]:
    errors: list[str] = []
    if bull_path.exists():
        bull_text = _read(bull_path)
        if _is_pending(bull_text):
            pass
        elif not re.search(r"disprove|falsif", bull_text, re.IGNORECASE):
            errors.append("bull case lacks falsification condition")
    if bear_path.exists():
        bear_text = _read(bear_path)
        if _is_pending(bear_text):
            pass
        elif not re.search(r"Response To Bull|Bull['’]?s strongest|answer Bull", bear_text, re.IGNORECASE):
            errors.append("bear case does not answer Bull's strongest argument")
    return errors


def _risk_portfolio_quality_errors(report_dir: Path) -> list[str]:
    errors: list[str] = []
    aggressive = report_dir / "4_risk" / "aggressive_round_1.md"
    conservative = report_dir / "4_risk" / "conservative_round_1.md"
    neutral = report_dir / "4_risk" / "neutral_round_1.md"
    portfolio = report_dir / "5_portfolio" / "decision.md"
    if aggressive.exists() and not _is_pending(_read(aggressive)) and not re.search(r"failure point", _read(aggressive), re.IGNORECASE):
        errors.append("aggressive risk case lacks failure points")
    if conservative.exists() and not _is_pending(_read(conservative)) and not re.search(r"unsupported upside|challenge", _read(conservative), re.IGNORECASE):
        errors.append("conservative risk case does not challenge unsupported upside")
    if neutral.exists() and not _is_pending(_read(neutral)) and not re.search(r"stronger risk side|evidence quality", _read(neutral), re.IGNORECASE):
        errors.append("neutral risk case lacks risk argument quality comparison")
    if portfolio.exists() and not _is_pending(_read(portfolio)) and "Risk debate impact" not in _read(portfolio):
        errors.append("portfolio decision omits risk debate impact")
    return errors


def _debate_record_quality_errors(report_dir: Path) -> list[str]:
    path = report_dir / "debate_record.md"
    if not path.exists():
        return ["debate_record.md is missing"]
    text = _read(path)
    if _is_pending(text):
        return ["debate_record.md contains pending debate output"]
    errors: list[str] = []
    if re.search(r"prepared below and filled as Codex acts|report-folder index", text, re.IGNORECASE):
        errors.append("debate_record.md is still a task index rather than a completed debate transcript")
    required_headings = [
        "Bull Researcher Round 1 - Opening Case",
        "Bear Researcher Round 1 - Rebuttal to Bull",
        "Research Manager Decision - Evidence Weighing",
        "Aggressive Risk Analyst Round 1 - Opportunity Case",
        "Conservative Risk Analyst Round 1 - Response to Aggressive",
        "Neutral Risk Analyst Round 1 - Weighing",
        "Portfolio Manager Synthesis",
    ]
    for heading in required_headings:
        if heading not in text:
            errors.append(f"debate_record.md missing debate turn: {heading}")
            break
    if "Full output:" not in text:
        errors.append("debate_record.md does not link to completed role output files")
    if "Pending debate outputs: `0`" not in text:
        errors.append("debate_record.md does not confirm zero pending debate outputs")
    return errors


def _complete_report_role_consistency_errors(report_dir: Path) -> list[str]:
    try:
        from validate_complete_report_against_roles import (
            validate_report_dir as validate_role_consistency,
        )
    except ImportError as exc:  # pragma: no cover - defensive CLI reporting
        return [f"complete report role-consistency validator unavailable: {exc}"]
    return validate_role_consistency(report_dir)


def validate_report_dir(report_dir: Path, evidence_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    analyst_dir = report_dir / "1_analysts"
    complete_report = report_dir / "complete_report.md"
    quality_gate = report_dir / "6_quality" / "quality_gate.json"
    quality_review = report_dir / "6_quality" / "quality_review.md"
    news = analyst_dir / "news.md"
    market = analyst_dir / "market.md"
    sentiment = analyst_dir / "sentiment.md"
    fundamentals = analyst_dir / "fundamentals.md"
    financial = analyst_dir / "financial_report.md"
    theme = analyst_dir / "industry_theme.md"
    bull = report_dir / "2_research" / "bull_round_1.md"
    bear = report_dir / "2_research" / "bear_round_1.md"
    manager = report_dir / "2_research" / "manager.md"
    trader = report_dir / "3_trading" / "trader.md"

    for relative_parts, required_sections in ROLE_REQUIRED_SECTIONS.items():
        role_path = report_dir.joinpath(*relative_parts)
        if not role_path.exists():
            continue
        role_text = _read(role_path)
        if _is_pending(role_text):
            errors.append(f"{role_path.name} is still pending")
            continue
        for section_name in required_sections:
            if not _has_section(role_text, section_name):
                errors.append(f"{role_path.name} missing required section: {section_name}")

    if not financial.exists():
        errors.append("financial_report.md is missing")
    elif not _is_pending(_read(financial)):
        if "Source coverage table" not in _read(financial):
            errors.append("financial report source coverage is unclear")
        elif "Claim-Source Table" not in _read(financial):
            errors.append("financial_report.md missing required section: Claim-Source Table")

    if not theme.exists():
        errors.append("industry_theme.md is missing")
    else:
        theme_text = _read(theme)
        if not _is_pending(theme_text):
            for required in ["Theme", "Subtheme", "Evidence link", "Classification", "Confidence"]:
                if required not in theme_text:
                    errors.append(f"industry_theme.md missing required column: {required}")
            if re.search(r"preconfigured|taxonomy", theme_text, re.IGNORECASE) and not re.search(
                r"evidence|source|link", theme_text, re.IGNORECASE
            ):
                errors.append("themes appear preconfigured without evidence support")

    fundamentals_text = _read(fundamentals)
    if fundamentals.exists() and not _is_pending(fundamentals_text) and not re.search(
        r"revenue|income|cash flow|balance sheet", fundamentals_text, re.IGNORECASE
    ):
        errors.append("fundamentals report only lists ratios and does not summarize financial statement data")

    complete_text = _read(complete_report)
    if _is_asx_evidence(evidence_path) and not complete_report.exists():
        errors.append("complete_report.md is missing")
    if complete_report.exists() and _is_pending(complete_text):
        errors.append("complete_report.md is still pending")
    elif complete_text:
        errors.extend(_complete_report_trade_date_errors(report_dir, complete_text))
        for heading in ["### Financial Report Analyst", "### Industry / Theme Discovery Analyst"]:
            if heading not in complete_text:
                errors.append(f"complete_report.md omits {heading}")

        research = _section(complete_text, "### Research Manager Decision - Evidence Weighing")
        if not re.search(
            r"financial[- ]report|management commentary|industry/theme|theme",
            research,
            re.IGNORECASE,
        ):
            errors.append("Research Manager ignores material financial-report or theme evidence")

        portfolio = _section(complete_text, "### Portfolio Manager")
        if portfolio and "Risk debate impact" not in portfolio:
            errors.append("Portfolio Manager merely repeats Trader or omits risk debate impact")

    if _asx_source_collection_failed(evidence_path):
        errors.append("ASX source collection failed; report cannot be marked complete")

    errors.extend(_structured_evidence_quality_errors(evidence_path))
    errors.extend(_news_quality_errors(news))
    errors.extend(_market_quality_errors(market))
    errors.extend(_sentiment_quality_errors(sentiment))
    errors.extend(_fundamentals_quality_errors(fundamentals))
    errors.extend(_financial_quality_errors(financial))
    errors.extend(_asx_financial_claim_support_errors(report_dir, evidence_path))
    errors.extend(_debate_quality_errors(bull, bear))
    errors.extend(_research_manager_quality_errors(manager))
    errors.extend(_asx_research_specificity_errors(manager, evidence_path))
    errors.extend(_asx_complete_report_research_manager_errors(report_dir, evidence_path))
    errors.extend(_trader_quality_errors(trader))
    errors.extend(_risk_portfolio_quality_errors(report_dir))
    errors.extend(_debate_record_quality_errors(report_dir))
    errors.extend(_complete_report_role_consistency_errors(report_dir))

    if quality_gate.exists():
        try:
            gate = json.loads(_read(quality_gate))
        except json.JSONDecodeError:
            errors.append("quality_gate.json is not valid JSON")
        else:
            passed = gate.get("passed") is True
            if passed:
                run_root = report_dir.parents[2] if len(report_dir.parents) > 2 else report_dir
                closed_loop_status = run_root / "closed_loop_status.json"
                if not closed_loop_status.exists():
                    errors.append("closed_loop_status.json missing for completed run")
                if not (
                    gate.get("closed_loop_status_path")
                    or gate.get("closed_loop_status")
                    or gate.get("closed_loop_status_artifact")
                ):
                    errors.append("quality_gate.json does not reference closed_loop_status.json")
                review_text = _read(quality_review)
                if re.search(r"validator must still be run|validator still pending|planned check", review_text, re.IGNORECASE):
                    errors.append("quality_review.md says validator is pending while quality_gate.json passed")
            if errors and gate.get("passed") is True:
                errors.append("quality_gate.json passes despite quality errors")
            if not passed:
                errors.append("quality_gate.json does not pass; workflow remains incomplete")

    return errors


def _recommendation_from_research(text: str) -> str:
    match = re.search(r"\*\*Recommendation\*\*\s*:\s*(Buy|Overweight|Hold|Underweight|Sell)", text, re.IGNORECASE)
    return match.group(1).lower() if match else ""


def _research_reasoning_for_similarity(text: str) -> str:
    section = _section(text, "## Rating-vs-Rating Reasoning") or _section(text, "## Rating Rationale") or text
    section = re.sub(r"\b[A-Z]{2,5}(?:\.AX)?\b", "TICKER", section)
    section = re.sub(r"\b\d+(?:\.\d+)?\b", "NUM", section)
    section = re.sub(r"financial:TICKER:\d{4}-\d{2}-\d{2}:\d{3}", "FINANCIAL_ID", section)
    section = re.sub(r"market:TICKER:\d{4}-\d{2}-\d{2}:\d{3}", "MARKET_ID", section)
    section = re.sub(r"news:TICKER:\d{4}-\d{2}-\d{2}:\d{3}", "NEWS_ID", section)
    return re.sub(r"\s+", " ", section.lower()).strip()


def validate_run_dir(output_dir: Path) -> list[str]:
    errors: list[str] = []
    entries: list[dict[str, str]] = []
    for workflow_path in sorted((output_dir / "evidence").glob("*/*/workflow_state.json")):
        try:
            workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        ticker = str(workflow.get("ticker") or workflow_path.parents[1].name)
        if not ticker.upper().endswith(".AX"):
            continue
        evidence_path = Path(str(workflow.get("evidence_path") or workflow_path.parent / "evidence.json"))
        report_dir = Path(str(workflow.get("report_dir") or output_dir / "reports" / ticker / workflow_path.parent.name))
        manager_path = report_dir / "2_research" / "manager.md"
        if not manager_path.exists():
            continue
        text = _read(manager_path)
        if _is_pending(text):
            continue
        setup, _values = _market_setup_from_evidence(evidence_path)
        if not setup:
            continue
        entries.append(
            {
                "ticker": ticker,
                "setup": setup,
                "recommendation": _recommendation_from_research(text),
                "reasoning": _research_reasoning_for_similarity(text),
            }
        )

    for left_index, left in enumerate(entries):
        for right in entries[left_index + 1 :]:
            if left["setup"] == right["setup"]:
                continue
            if left["recommendation"] != right["recommendation"]:
                continue
            if left["recommendation"] not in {"hold", "underweight", "overweight", "sell", "buy"}:
                continue
            similarity = SequenceMatcher(None, left["reasoning"], right["reasoning"]).ratio()
            if similarity >= 0.90:
                errors.append(
                    "near-identical Research Manager rationale despite materially different ASX evidence: "
                    f"{left['ticker']} setup {left['setup']} vs {right['ticker']} setup {right['setup']}"
                )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Codex TradingAgents quality review prerequisites.")
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--run-dir", type=Path)
    args = parser.parse_args(argv)

    errors = validate_report_dir(args.report_dir, args.evidence)
    if args.run_dir:
        errors.extend(validate_run_dir(args.run_dir))
    if errors:
        print("Quality review validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Quality review validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
