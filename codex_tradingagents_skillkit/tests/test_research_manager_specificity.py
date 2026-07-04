from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_quality_validator():
    spec = importlib.util.spec_from_file_location("validate_quality_review", QUALITY_VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_asx_evidence(output_dir: Path, ticker: str, setup: tuple[float, float, float, float]) -> tuple[Path, Path]:
    trade_date = "2026-07-02"
    evidence_dir = output_dir / "evidence" / ticker / trade_date
    report_dir = output_dir / "reports" / ticker / trade_date
    market_dir = evidence_dir / "market"
    research_dir = report_dir / "2_research"
    market_dir.mkdir(parents=True)
    research_dir.mkdir(parents=True)
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": ticker, "trade_date": trade_date}), encoding="utf-8")
    close, ema_10, sma_50, sma_200 = setup
    records = [
        {"metric_name": "latest_close", "value": close},
        {"metric_name": "ema_10", "value": ema_10},
        {"metric_name": "sma_50", "value": sma_50},
        {"metric_name": "sma_200", "value": sma_200},
    ]
    (market_dir / "quantitative_observations.json").write_text(json.dumps(records), encoding="utf-8")
    (evidence_dir / "workflow_state.json").write_text(
        json.dumps(
            {
                "ticker": ticker,
                "trade_date": trade_date,
                "evidence_path": str(evidence_path),
                "report_dir": str(report_dir),
            }
        ),
        encoding="utf-8",
    )
    return evidence_path, report_dir


def _manager_text(rationale: str) -> str:
    return (
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- market and financial evidence\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Role | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |\n"
        "|---|---|---|---|---|---:|---|---|\n"
        "| Market Analyst | mixed | high | medium | market snapshot | 0 | market setup | market:TICKER:2026-07-02:trend |\n\n"
        "## Rating Rationale\n\n"
        "**Recommendation**: Hold\n\n"
        f"{rationale}\n\n"
        "## Rating-vs-Rating Reasoning\n\n"
        f"{rationale}\n"
    )


def test_asx_run_flags_near_identical_hold_rationale_for_different_market_setups(tmp_path: Path):
    validator = _load_quality_validator()
    output_dir = tmp_path / "run"
    _evidence_path, cba_report = _write_asx_evidence(output_dir, "CBA.AX", (100.0, 105.0, 110.0, 120.0))
    _evidence_path, mpl_report = _write_asx_evidence(output_dir, "MPL.AX", (100.0, 95.0, 90.0, 80.0))
    generic = (
        "Hold beats Buy because ASX source coverage is uneven. Hold beats Sell because official records support a "
        "reviewable base case. Sector metrics are considered with evidence gaps."
    )
    (cba_report / "2_research" / "manager.md").write_text(_manager_text(generic), encoding="utf-8")
    (mpl_report / "2_research" / "manager.md").write_text(_manager_text(generic), encoding="utf-8")

    errors = validator.validate_run_dir(output_dir)

    assert any("near-identical Research Manager rationale" in error for error in errors)


def test_asx_research_manager_requires_market_fact_and_sector_metric_or_gap(tmp_path: Path):
    validator = _load_quality_validator()
    evidence_path, report_dir = _write_asx_evidence(tmp_path / "run", "CBA.AX", (100.0, 105.0, 110.0, 120.0))
    manager_path = report_dir / "2_research" / "manager.md"
    manager_path.write_text(
        _manager_text("Hold is selected because evidence is mixed, with no specific market or sector metric discussion."),
        encoding="utf-8",
    )

    errors = validator._asx_research_specificity_errors(manager_path, evidence_path)

    assert "ASX Research Manager report lacks ticker-specific market moving-average facts" in errors
    assert "ASX Research Manager report lacks ticker-specific sector metric or evidence-gap reference" in errors


def test_generic_asx_source_coverage_cannot_be_sole_hold_reason(tmp_path: Path):
    validator = _load_quality_validator()
    evidence_path, report_dir = _write_asx_evidence(tmp_path / "run", "CBA.AX", (100.0, 105.0, 110.0, 120.0))
    manager_path = report_dir / "2_research" / "manager.md"
    manager_path.write_text(
        _manager_text(
            "Hold beats Buy because ASX source coverage is uneven; it beats Sell because official records exist. "
            "No other ticker-specific reason is provided."
        ),
        encoding="utf-8",
    )

    errors = validator._asx_research_specificity_errors(manager_path, evidence_path)

    assert "generic ASX source coverage cannot be the sole reason for Hold" in errors


def test_asx_complete_report_must_reflect_manager_rating_vs_rating_reasoning(tmp_path: Path):
    validator = _load_quality_validator()
    evidence_path, report_dir = _write_asx_evidence(tmp_path / "run", "CBA.AX", (100.0, 105.0, 110.0, 120.0))
    manager_path = report_dir / "2_research" / "manager.md"
    manager_path.write_text(
        _manager_text(
            "Hold is ticker-specific here: latest close 100.00 is below the 10 EMA (105.00), below the 50 SMA "
            "(110.00), and below the 200 SMA (120.00). Why not Buy / Overweight? The all-below-average setup "
            "blocks Buy. Why not Sell / Underweight? CET1 sector metric evidence is available via "
            "financial:CBA.AX:2026-07-02:001 and prevents a completed Sell case. Decisive role evidence is Market "
            "Analyst plus Financial Report Analyst."
        ),
        encoding="utf-8",
    )
    (report_dir / "complete_report.md").write_text(
        "# Complete Codex TradingAgents Report - CBA.AX\n\n"
        "### Research Manager Decision - Evidence Weighing\n"
        "**Recommendation**: Hold\n"
        "Research Manager weighs market, financial-report, news, theme, and sentiment evidence by independence group. "
        "Hold beats Buy because ASX source coverage is uneven and beats Sell where official-source records still "
        "support a reviewable base case.\n\n"
        "### Trader\n"
        "FINAL TRANSACTION PROPOSAL: **HOLD**\n",
        encoding="utf-8",
    )

    errors = validator._asx_complete_report_research_manager_errors(report_dir, evidence_path)

    assert "complete_report.md Research Manager section does not reflect ticker-specific moving-average setup" in errors
    assert "complete_report.md Research Manager section lacks sector metric or explicit evidence gap" in errors
    assert "complete_report.md uses generic ASX source coverage as the main Research Manager rationale" in errors
