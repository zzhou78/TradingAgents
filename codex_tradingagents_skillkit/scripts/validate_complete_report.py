from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_STRINGS = [
    "# Trading Analysis Report:",
    "Generated:",
    "## I. Analyst Team Reports",
    "### Market Analyst",
    "### Sentiment Analyst",
    "### News Analyst",
    "### Fundamentals Analyst",
    "### Financial Report Analyst",
    "### Industry / Theme Discovery Analyst",
    "## II. Research Team Debate",
    "### Bull Researcher Round 1 - Opening Case",
    "### Bear Researcher Round 1 - Rebuttal to Bull",
    "### Research Manager Decision - Evidence Weighing",
    "## III. Trading Team Plan",
    "### Trader Proposal",
    "## IV. Risk Management Team Debate",
    "### Aggressive Risk Analyst Round 1 - Opportunity Case",
    "### Conservative Risk Analyst Round 1 - Response to Aggressive",
    "### Neutral Risk Analyst Round 1 - Weighing",
    "## V. Portfolio Manager Decision",
    "FINAL TRANSACTION PROPOSAL:",
    "## VI. Paper-Study Disclaimer",
    "Primary driver of rating:",
]


def _report_ticker(text: str) -> str | None:
    match = re.search(r"^# Trading Analysis Report:\s*(?P<ticker>\S+)\s*$", text, re.MULTILINE)
    return match.group("ticker").upper() if match else None


def _is_comparative(text: str) -> bool:
    return "comparative_run=true" in text.lower()


def _section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^#{2,3}\s+", rest, re.MULTILINE)
    return rest[: next_heading.start()] if next_heading else rest


def _generated_date(text: str) -> str | None:
    match = re.search(r"^Generated:\s*(\d{4}-\d{2}-\d{2})\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def _timestamp_dates(text: str) -> list[str]:
    return re.findall(r"\[(\d{4}-\d{2}-\d{2})T", text)


def _field_value(text: str, label: str) -> str | None:
    pattern = re.compile(rf"\*\*{re.escape(label)}\*\*:\s*([A-Za-z]+)", re.IGNORECASE)
    match = pattern.search(text)
    return match.group(1).capitalize() if match else None


def _final_proposal(text: str) -> str | None:
    match = re.search(r"FINAL TRANSACTION PROPOSAL:\s*\*\*(BUY|HOLD|SELL)\*\*", text, re.IGNORECASE)
    return match.group(1).capitalize() if match else None


def validate_report(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = []
    for item in REQUIRED_STRINGS:
        if item in text:
            continue
        if item == "Primary driver of rating:":
            errors.append("missing primary driver: report must include 'Primary driver of rating:'")
        else:
            errors.append(f"missing heading: {item}")

    ticker = _report_ticker(text)
    if (
        ticker == "MSFT"
        and not _is_comparative(text)
        and re.search(r"(Apple|AAPL)", text, re.IGNORECASE)
    ):
        errors.append("cross-ticker leakage: MSFT report mentions Apple/AAPL without comparative_run=true")

    timestamp_dates = _timestamp_dates(text)
    if len(timestamp_dates) > 5:
        errors.append(f"too many raw social examples: found {len(timestamp_dates)} timestamped lines; maximum is 5")

    generated = _generated_date(text)
    if generated:
        for date in timestamp_dates:
            if date > generated:
                errors.append(f"post-date evidence found: social timestamp {date} is after Generated date {generated}")
                break

    research = _section(text, "### Research Manager Decision - Evidence Weighing")
    portfolio = _section(text, "### Portfolio Manager")
    trader = _section(text, "### Trader Proposal")
    research_rating = _field_value(research, "Recommendation")
    trader_action = _field_value(trader, "Action")
    portfolio_rating = _field_value(portfolio, "Rating")
    final = _final_proposal(text)
    if trader_action and final and trader_action != final:
        errors.append(f"final proposal mismatch: Trader Action is {trader_action}, FINAL TRANSACTION PROPOSAL is {final}")
    if final in {"Buy", "Sell"} and "**Paper-study price framework**" not in trader:
        errors.append("missing price framework: Buy/Sell Trader Proposal must include **Paper-study price framework**")
    if final == "Sell" and not re.search(r"(200 SMA|materially negative|longer-term support)", trader, re.IGNORECASE):
        errors.append(
            "unsupported Sell action: Trader section must cite 200 SMA, longer-term support break, or explicit material negative setup"
        )
    if not trader_action:
        errors.append("missing hard contract field: Trader section must include **Action**")
    if not final:
        errors.append("missing hard contract field: FINAL TRANSACTION PROPOSAL must be BUY/HOLD/SELL")
    if research and not research_rating:
        errors.append("missing hard contract field: Research Manager section must include **Recommendation**")
    if portfolio and not portfolio_rating:
        errors.append("missing hard contract field: Portfolio Manager section must include **Rating**")

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
