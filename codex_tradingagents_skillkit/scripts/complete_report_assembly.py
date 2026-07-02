from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from validate_complete_report_against_roles import _field_values, validate_report_dir

REQUIRED_FIELDS = (
    "manager_recommendation",
    "trader_action",
    "trader_final",
    "trader_reference_price",
    "portfolio_rating",
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _identity(report_dir: Path) -> tuple[str, str]:
    if len(report_dir.parts) >= 2:
        return report_dir.parts[-2], report_dir.parts[-1]
    return "UNKNOWN", "UNKNOWN"


def _section_text(text: str, heading: str) -> str:
    match = re.search(rf"^#+\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^#+\s+", rest, re.MULTILINE)
    section = rest[: next_heading.start()] if next_heading else rest
    return " ".join(section.split())


def _one_line_summary(path: Path, preferred_heading: str, fallback: str) -> str:
    text = _read(path)
    section = _section_text(text, preferred_heading)
    candidate = section or " ".join(text.split())
    if not candidate:
        return fallback
    return candidate[:360].rstrip()


def _missing_required_fields(values: dict[str, str]) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not values.get(field)]


def _evidence_path_for_report_dir(report_dir: Path, ticker: str, trade_date: str) -> Path:
    if len(report_dir.parents) >= 3:
        output_dir = report_dir.parents[2]
        return output_dir / "evidence" / ticker / trade_date / "evidence.json"
    return report_dir / "evidence.json"


def _run_metadata(report_dir: Path, *, generated_at: str) -> dict[str, str | bool]:
    ticker, trade_date = _identity(report_dir)
    default = {
        "trade_date": trade_date,
        "evidence_as_of_date": trade_date,
        "run_executed_at": generated_at,
        "output_dir": str(report_dir.parents[2]) if len(report_dir.parents) >= 3 else "",
        "run_id": "",
        "authoritative_result_folder": False,
        "status": "pending",
    }
    evidence_path = _evidence_path_for_report_dir(report_dir, ticker, trade_date)
    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default
    metadata = evidence.get("run_metadata", {})
    if not isinstance(metadata, dict):
        return default
    return {**default, **metadata}


def assemble_complete_report(report_dir: Path) -> tuple[str, list[str]]:
    values = _field_values(report_dir)
    missing = _missing_required_fields(values)
    if missing:
        return "", [f"missing required role value: {field}" for field in missing]

    ticker, trade_date = _identity(report_dir)
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    run_metadata = _run_metadata(report_dir, generated_at=generated_at)
    market_summary = _one_line_summary(
        report_dir / "1_analysts" / "market.md",
        "Quantitative Regime / Tool Outputs",
        "Market Analyst output unavailable.",
    )
    sentiment_summary = _one_line_summary(
        report_dir / "1_analysts" / "sentiment.md",
        "Final sentiment interpretation",
        "Sentiment Analyst output unavailable.",
    )
    news_summary = _one_line_summary(
        report_dir / "1_analysts" / "news.md",
        "News Impact Summary",
        "News Analyst output unavailable.",
    )
    fundamentals_summary = _one_line_summary(
        report_dir / "1_analysts" / "fundamentals.md",
        "Financial Statement Evidence",
        "Fundamentals Analyst output unavailable.",
    )
    financial_summary = _one_line_summary(
        report_dir / "1_analysts" / "financial_report.md",
        "Claim-Source Table",
        "Financial Report Analyst output unavailable.",
    )
    theme_summary = _one_line_summary(
        report_dir / "1_analysts" / "industry_theme.md",
        "Theme Evidence Table",
        "Industry / Theme Discovery Analyst output unavailable.",
    )
    bull_summary = _one_line_summary(
        report_dir / "2_research" / "bull_round_1.md",
        "Strongest Bull Evidence",
        "Bull Researcher output unavailable.",
    )
    bear_summary = _one_line_summary(
        report_dir / "2_research" / "bear_round_1.md",
        "Strongest Bear Evidence",
        "Bear Researcher output unavailable.",
    )
    portfolio_summary = _one_line_summary(
        report_dir / "5_portfolio" / "decision.md",
        "Final Portfolio Decision",
        "Portfolio Manager output unavailable.",
    )

    report = f"""# Trading Analysis Report: {ticker}

Generated: {trade_date}

Trade date: {run_metadata['trade_date']}
Evidence as of: {run_metadata['evidence_as_of_date']}
Run executed at: {run_metadata['run_executed_at']}
Run ID: {run_metadata['run_id']}
Authoritative result folder: {str(run_metadata['authoritative_result_folder']).lower()}
Run status: {run_metadata['status']}

Context: comparative_run=false

## Tool Outputs Used

- Complete report assembled from completed role reports. It preserves Research Manager, Trader, and Portfolio Manager outputs without overriding them.

## Complete Report

## I. Analyst Team Reports

### Market Analyst

{market_summary}

### Sentiment Analyst

{sentiment_summary}

### News Analyst

{news_summary}

### Fundamentals Analyst

{fundamentals_summary}

### Financial Report Analyst

{financial_summary}

### Industry / Theme Discovery Analyst

{theme_summary}

## II. Research Team Debate

### Bull Researcher Round 1 - Opening Case

{bull_summary}

### Bear Researcher Round 1 - Rebuttal to Bull

{bear_summary}

### Research Manager Decision - Evidence Weighing

**Recommendation**: {values['manager_recommendation']}

**Primary driver of rating:** Preserved from Research Manager role output. See `2_research/manager.md`.

financial-report evidence and industry/theme evidence are preserved from the specialist role files and remain part of the Research Manager evidence context; this assembler does not override those role-level interpretations.

## III. Trading Team Plan

### Trader Proposal

**Action**: {values['trader_action']}

## Paper-study price framework

Reference price: {values['trader_reference_price']}

FINAL TRANSACTION PROPOSAL: **{values['trader_final']}**

## IV. Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

See `4_risk/aggressive_round_1.md`.

### Conservative Risk Analyst Round 1 - Response to Aggressive

See `4_risk/conservative_round_1.md`.

### Neutral Risk Analyst Round 1 - Weighing

See `4_risk/neutral_round_1.md`.

## V. Portfolio Manager Decision

### Portfolio Manager

**Rating**: {values['portfolio_rating']}

Risk debate impact: {portfolio_summary}

## Evidence Gaps

Evidence gaps remain as stated in the role reports. This assembly step does not invent missing evidence or override role conclusions.

## VI. Paper-Study Disclaimer

This is a paper-study Codex TradingAgents workflow validation artifact, not investment advice and not a broker order.

## Memory Update

* Durable facts to retain: {ticker} complete_report was assembled from role outputs for trade date {trade_date}.
* Prior mistake to avoid: Do not override Research Manager, Trader, or Portfolio Manager outputs during complete-report assembly.
* Open questions: Refresh evidence for later trade dates.
* Evidence references: See role reports and structured evidence ledgers.
* Staleness / expiry: Expires after {trade_date}.
"""
    return report, []


def write_complete_report(report_dir: Path) -> list[str]:
    report, errors = assemble_complete_report(report_dir)
    if errors:
        return errors
    output_path = report_dir / "complete_report.md"
    output_path.write_text(report, encoding="utf-8")
    return validate_report_dir(report_dir)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Assemble complete_report.md from completed role reports.")
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args(argv)

    errors = write_complete_report(args.report_dir)
    if errors:
        print("Complete report assembly failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Complete report assembled: {args.report_dir / 'complete_report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
