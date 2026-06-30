from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROLE_REQUIRED_SECTIONS = {
    ("1_analysts", "market.md"): ["Tool Outputs Used", "Quantitative Regime / Tool Outputs"],
    ("1_analysts", "sentiment.md"): ["Tool Outputs Used", "Social Evidence Processing Rules"],
    ("1_analysts", "news.md"): ["Tool Outputs Used", "Article Evidence Cards"],
    ("1_analysts", "fundamentals.md"): ["Tool Outputs Used", "Financial Statement Evidence", "Sector-Specific Metrics"],
    ("1_analysts", "financial_report.md"): ["Tool Outputs Used", "Claim-Source Table"],
    ("1_analysts", "industry_theme.md"): ["Tool Outputs Used", "Theme Evidence Table"],
    ("2_research", "bull_round_1.md"): ["Tool Outputs Used", "Strongest Bull Evidence", "Falsification Conditions"],
    ("2_research", "bear_round_1.md"): ["Tool Outputs Used", "Strongest Bear Evidence", "Falsification Conditions", "Response To Bull"],
    ("2_research", "manager.md"): ["Tool Outputs Used", "Structured Evidence Matrix"],
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
    return status in {"error", "unavailable"} or "asx_announcements | error" in output


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
    if "Sector-Specific Metrics" in text and not re.search(r"gap|NIM|CET1|production|capex|pipeline|same-store|R&D", text, re.IGNORECASE):
        errors.append("fundamentals sector metrics are not sector-specific or gap-labelled")
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


def validate_report_dir(report_dir: Path, evidence_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    analyst_dir = report_dir / "1_analysts"
    complete_report = report_dir / "complete_report.md"
    quality_gate = report_dir / "6_quality" / "quality_gate.json"
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
    if complete_report.exists() and _is_pending(complete_text):
        errors.append("complete_report.md is still pending")
    elif complete_text:
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

    errors.extend(_news_quality_errors(news))
    errors.extend(_market_quality_errors(market))
    errors.extend(_sentiment_quality_errors(sentiment))
    errors.extend(_fundamentals_quality_errors(fundamentals))
    errors.extend(_financial_quality_errors(financial))
    errors.extend(_debate_quality_errors(bull, bear))
    errors.extend(_research_manager_quality_errors(manager))
    errors.extend(_trader_quality_errors(trader))
    errors.extend(_risk_portfolio_quality_errors(report_dir))

    if quality_gate.exists():
        try:
            gate = json.loads(_read(quality_gate))
        except json.JSONDecodeError:
            errors.append("quality_gate.json is not valid JSON")
        else:
            if errors and gate.get("passed") is True:
                errors.append("quality_gate.json passes despite missing role outputs")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Codex TradingAgents quality review prerequisites.")
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args(argv)

    errors = validate_report_dir(args.report_dir, args.evidence)
    if errors:
        print("Quality review validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Quality review validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
