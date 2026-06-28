from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_STRINGS = [
    "## II. Research Team Debate",
    "### Bull Researcher Round 1 - Opening Case",
    "### Bear Researcher Round 1 - Rebuttal to Bull",
    "### Research Manager Decision - Evidence Weighing",
    "## IV. Risk Management Team Debate",
    "### Aggressive Risk Analyst Round 1 - Opportunity Case",
    "### Conservative Risk Analyst Round 1 - Response to Aggressive",
    "### Neutral Risk Analyst Round 1 - Weighing",
    "FINAL TRANSACTION PROPOSAL:",
    "## VI. Paper-Study Disclaimer",
]


def _report_ticker(text: str) -> str | None:
    match = re.search(r"^# Trading Analysis Report:\s*(?P<ticker>\S+)\s*$", text, re.MULTILINE)
    return match.group("ticker").upper() if match else None


def _is_comparative(text: str) -> bool:
    return "comparative_run=true" in text.lower()


def validate_report(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = [f"missing required report contract string: {item}" for item in REQUIRED_STRINGS if item not in text]

    ticker = _report_ticker(text)
    if (
        ticker == "MSFT"
        and not _is_comparative(text)
        and re.search(r"(Apple|AAPL)", text, re.IGNORECASE)
    ):
        errors.append("cross-ticker leakage: MSFT report mentions Apple/AAPL without comparative_run=true")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Codex TradingAgents complete_report.md contract.")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args(argv)

    errors = validate_report(args.report)
    if errors:
        print("Report contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Report contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
