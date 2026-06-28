from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _section(text: str, heading: str) -> str:
    match = re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^#{2,3}\s+", rest, re.MULTILINE)
    return rest[: next_heading.start()] if next_heading else rest


def validate_report_dir(report_dir: Path) -> list[str]:
    errors: list[str] = []
    analyst_dir = report_dir / "1_analysts"
    complete_report = report_dir / "complete_report.md"
    quality_gate = report_dir / "6_quality" / "quality_gate.json"
    fundamentals = analyst_dir / "fundamentals.md"
    financial = analyst_dir / "financial_report.md"
    theme = analyst_dir / "industry_theme.md"

    if not financial.exists():
        errors.append("financial_report.md is missing")
    elif "Source coverage table" not in _read(financial):
        errors.append("financial report source coverage is unclear")

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
    args = parser.parse_args(argv)

    errors = validate_report_dir(args.report_dir)
    if errors:
        print("Quality review validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Quality review validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
