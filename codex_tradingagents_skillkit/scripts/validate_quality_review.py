from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROLE_REQUIRED_SECTIONS = {
    ("1_analysts", "market.md"): ["Tool Outputs Used", "Quantitative Regime / Tool Outputs"],
    ("1_analysts", "news.md"): ["Tool Outputs Used", "Article Evidence Cards"],
    ("1_analysts", "fundamentals.md"): ["Tool Outputs Used"],
    ("1_analysts", "financial_report.md"): ["Tool Outputs Used", "Claim-Source Table"],
    ("2_research", "manager.md"): ["Tool Outputs Used", "Structured Evidence Matrix"],
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


def validate_report_dir(report_dir: Path, evidence_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    analyst_dir = report_dir / "1_analysts"
    complete_report = report_dir / "complete_report.md"
    quality_gate = report_dir / "6_quality" / "quality_gate.json"
    fundamentals = analyst_dir / "fundamentals.md"
    financial = analyst_dir / "financial_report.md"
    theme = analyst_dir / "industry_theme.md"

    for relative_parts, required_sections in ROLE_REQUIRED_SECTIONS.items():
        role_path = report_dir.joinpath(*relative_parts)
        if not role_path.exists():
            continue
        role_text = _read(role_path)
        if _is_pending(role_text):
            continue
        for section_name in required_sections:
            if not _has_section(role_text, section_name):
                errors.append(f"{role_path.name} missing required section: {section_name}")

    if not financial.exists():
        errors.append("financial_report.md is missing")
    elif "Source coverage table" not in _read(financial):
        errors.append("financial report source coverage is unclear")
    elif "Claim-Source Table" not in _read(financial) and not _is_pending(_read(financial)):
        errors.append("financial_report.md missing required section: Claim-Source Table")

    if not theme.exists():
        errors.append("industry_theme.md is missing")
    else:
        theme_text = _read(theme)
        for required in ["Theme", "Subtheme", "Evidence link", "Classification", "Confidence"]:
            if required not in theme_text:
                errors.append(f"industry_theme.md missing required column: {required}")
        if re.search(r"preconfigured|taxonomy", theme_text, re.IGNORECASE) and not re.search(
            r"evidence|source|link", theme_text, re.IGNORECASE
        ):
            errors.append("themes appear preconfigured without evidence support")

    fundamentals_text = _read(fundamentals)
    if fundamentals.exists() and not re.search(
        r"revenue|income|cash flow|balance sheet", fundamentals_text, re.IGNORECASE
    ):
        errors.append("fundamentals report only lists ratios and does not summarize financial statement data")

    complete_text = _read(complete_report)
    for heading in ["### Financial Report Analyst", "### Industry / Theme Discovery Analyst"]:
        if heading not in complete_text:
            errors.append(f"complete_report.md omits {heading}")

    research = _section(complete_text, "### Research Manager Decision - Evidence Weighing")
    if complete_text and not re.search(
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
