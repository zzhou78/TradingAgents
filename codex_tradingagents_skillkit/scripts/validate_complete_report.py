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
    errors = [f"missing heading: {item}" for item in REQUIRED_STRINGS if item not in text]

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

    bear = _section(text, "### Bear Researcher Round 1 - Rebuttal to Bull")
    if bear and not re.search(r"\b(rebut|underestimating|respond)\b", bear, re.IGNORECASE):
        errors.append("debate substance missing: Bear section must directly rebut or state what Bull is underestimating")

    research = _section(text, "### Research Manager Decision - Evidence Weighing")
    if research:
        if "Scoring Rule" not in research:
            errors.append("missing scoring components: Research Manager section lacks Scoring Rule")
        if "Score Components" not in research:
            errors.append("missing scoring components: Research Manager section lacks Score Components")

    neutral = _section(text, "### Neutral Risk Analyst Round 1 - Weighing")
    if neutral and not ("Aggressive" in neutral and "Conservative" in neutral):
        errors.append("debate substance missing: Neutral Risk section must mention both Aggressive and Conservative")

    portfolio = _section(text, "### Portfolio Manager")
    if portfolio and not re.search(r"Risk debate impact", portfolio, re.IGNORECASE):
        errors.append("debate substance missing: Portfolio Manager section lacks Risk debate impact")

    if "Primary driver of rating:" not in text:
        errors.append("missing primary driver: report must include 'Primary driver of rating:'")

    trader = _section(text, "### Trader Proposal")
    research_rating = _field_value(research, "Recommendation")
    trader_action = _field_value(trader, "Action")
    portfolio_rating = _field_value(portfolio, "Rating")
    final = _final_proposal(text)
    if trader_action and final and trader_action != final:
        errors.append(f"final proposal mismatch: Trader Action is {trader_action}, FINAL TRANSACTION PROPOSAL is {final}")
    if (
        research_rating
        and portfolio_rating
        and research_rating != portfolio_rating
        and not re.search(r"(portfolio rating differs|differs from research manager|rating differs)", text, re.IGNORECASE)
    ):
        errors.append(
            f"rating mismatch: Portfolio Manager Rating is {portfolio_rating}, Research Manager Recommendation is {research_rating}, and no difference explanation is present"
        )
    if research_rating == "Underweight" and trader_action == "Hold" and not re.search(
        r"(Underweight research rating with Hold trader action|action differs from rating|Trader Action is Hold)",
        text,
        re.IGNORECASE,
    ):
        errors.append("rating/action consistency: Underweight research rating with Hold trader action requires explicit explanation")
    if trader_action == "Sell" and not re.search(r"(below the 200 SMA|materially negative setup)", trader, re.IGNORECASE):
        errors.append("rating/action consistency: Sell action requires below the 200 SMA or materially negative setup in Trader section")

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
