from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
WRITER = BUNDLE / "scripts" / "write_codex_session_role_reports.py"
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_debate_scorecard_contains_required_outcome_fields():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    scorecard = writer._debate_outcome_scorecard(
        ticker="BHP.AX",
        trade_date="2026-07-02",
        manager_rec="Overweight",
        trader_action="HOLD",
        primary_driver="sector_metric",
        refs={"exhibit": "financial:BHP.AX:2026-07-02:001", "fund": "fundamental:BHP.AX:2026-07-02:001"},
        asx_reasoning={"confidence_cap": "capex evidence gap caps confidence"},
        is_asx=True,
    )

    text = scorecard["markdown"]
    for field in [
        "Bull evidence quality",
        "Bear evidence quality",
        "Strongest Bull evidence ID",
        "Strongest Bear evidence ID",
        "Which side directly answered the other side better?",
        "Which side relied on weaker or duplicated evidence?",
        "Which evidence gap matters most?",
        "Debate winner",
        "Rating implication",
        "Trader implication",
    ]:
        assert field in text
    assert "| Debate winner | Bull |" in text
    assert "| Trader implication | timing-gated HOLD |" in text
    assert "Changed by debate?" in text


def test_research_manager_hold_requires_debate_winner(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    manager = tmp_path / "manager.md"
    manager.write_text(
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- evidence\n\n"
        "## Primary Rating Driver\n\nPrimary rating driver: mixed\n\n"
        "## Evidence Winner\n\nFinancial and market evidence are mixed.\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Role | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |\n"
        "|---|---|---|---|---|---:|---|---|\n"
        "| Bull Researcher | positive | high | medium | bull | +1 | support | event:T:2026-07-02:earnings |\n\n"
        "## Role Evidence Weighting\n\nEvidence is grouped by independence group.\n\n"
        "## Rating Rationale\n\n**Recommendation**: Hold\n\nHold beats Buy and Sell because evidence is mixed.\n\n"
        "## Rating-vs-Rating Reasoning\n\nWhy not Buy / Overweight? Mixed evidence.\n\n"
        "## Debate Outcome Scorecard\n\n"
        "| Field | Outcome |\n"
        "|---|---|\n"
        "| Bull evidence quality | medium |\n"
        "| Bear evidence quality | medium |\n"
        "| Strongest Bull evidence ID | financial:T:2026-07-02:001 |\n"
        "| Strongest Bear evidence ID | fundamental:T:2026-07-02:001 |\n"
        "| Which side directly answered the other side better? | Bear |\n"
        "| Which side relied on weaker or duplicated evidence? | neither |\n"
        "| Which evidence gap matters most? | source depth |\n"
        "| Rating implication | Hold |\n"
        "| Trader implication | HOLD |\n\n"
        "## Debate Change Assessment\n\n- Changed by debate? No.\n\n"
        "## Market Technicals as Confidence / Timing Modifier\n\nTiming only.\n",
        encoding="utf-8",
    )

    errors = validator._research_manager_quality_errors(manager)

    assert "research manager debate scorecard missing field: Debate winner" in errors
    assert "Research Manager gives Hold without saying whether Bull, Bear, or Balanced won" in errors


def test_same_bull_bear_evidence_requires_independence_group_treatment(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    manager = tmp_path / "manager.md"
    shared = "financial:T:2026-07-02:001"
    manager.write_text(
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- evidence\n\n"
        "## Primary Rating Driver\n\nPrimary rating driver: mixed\n\n"
        "## Evidence Winner\n\nFinancial and market evidence are mixed.\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Role | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |\n"
        "|---|---|---|---|---|---:|---|---|\n"
        "| Bull Researcher | positive | high | medium | bull | +1 | support | event:T:2026-07-02:earnings |\n\n"
        "## Role Evidence Weighting\n\nEvidence is weighed normally.\n\n"
        "## Rating Rationale\n\n**Recommendation**: Hold\n\nHold beats Buy and Sell because evidence is mixed.\n\n"
        "## Rating-vs-Rating Reasoning\n\nWhy not Buy / Overweight? Mixed evidence.\n\n"
        "## Debate Outcome Scorecard\n\n"
        "| Field | Outcome |\n"
        "|---|---|\n"
        "| Bull evidence quality | medium |\n"
        "| Bear evidence quality | medium |\n"
        f"| Strongest Bull evidence ID | {shared} |\n"
        f"| Strongest Bear evidence ID | {shared} |\n"
        "| Which side directly answered the other side better? | Bear |\n"
        "| Which side relied on weaker or duplicated evidence? | neither |\n"
        "| Which evidence gap matters most? | source depth |\n"
        "| Debate winner | Balanced |\n"
        "| Rating implication | Hold |\n"
        "| Trader implication | HOLD |\n\n"
        "## Debate Change Assessment\n\n- Changed by debate? No.\n\n"
        "## Market Technicals as Confidence / Timing Modifier\n\nTiming only.\n",
        encoding="utf-8",
    )

    errors = validator._research_manager_quality_errors(manager)

    assert "Bull and Bear cite the same evidence without independence-group treatment" in errors


def test_portfolio_risk_debate_impact_must_name_stronger_side(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    report_dir = tmp_path / "reports" / "AAPL" / "2026-07-02"
    portfolio_dir = report_dir / "5_portfolio"
    portfolio_dir.mkdir(parents=True)
    (portfolio_dir / "decision.md").write_text(
        "# Portfolio Manager\n\n"
        "## Tool Outputs Used\n\n- risk reports\n\n"
        "## Risk debate impact\n\n"
        "The risk debate tempers action and requires sizing discipline.\n\n"
        "## Final Portfolio Decision\n\n**Rating**: Hold\n",
        encoding="utf-8",
    )

    errors = validator._risk_portfolio_quality_errors(report_dir)

    assert "Portfolio Manager says risk debate tempers action but does not explain which risk side was stronger" in errors


def test_multi_ticker_all_balanced_debate_winner_warns(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    output_dir = tmp_path / "run"
    for ticker, setup in {
        "CBA.AX": (100.0, 105.0, 110.0, 120.0),
        "WOW.AX": (100.0, 95.0, 90.0, 80.0),
    }.items():
        evidence_dir = output_dir / "evidence" / ticker / "2026-07-02"
        market_dir = evidence_dir / "market"
        report_dir = output_dir / "reports" / ticker / "2026-07-02"
        research_dir = report_dir / "2_research"
        market_dir.mkdir(parents=True)
        research_dir.mkdir(parents=True)
        (evidence_dir / "evidence.json").write_text(json.dumps({"ticker": ticker}), encoding="utf-8")
        close, ema_10, sma_50, sma_200 = setup
        (market_dir / "quantitative_observations.json").write_text(
            json.dumps(
                [
                    {"metric_name": "latest_close", "value": close},
                    {"metric_name": "ema_10", "value": ema_10},
                    {"metric_name": "sma_50", "value": sma_50},
                    {"metric_name": "sma_200", "value": sma_200},
                ]
            ),
            encoding="utf-8",
        )
        (evidence_dir / "workflow_state.json").write_text(
            json.dumps({"ticker": ticker, "evidence_path": str(evidence_dir / "evidence.json"), "report_dir": str(report_dir)}),
            encoding="utf-8",
        )
        (research_dir / "manager.md").write_text(
            "# Research Manager\n\n"
            "## Rating-vs-Rating Reasoning\n\n"
            f"Hold for {ticker} based on ticker-specific evidence.\n\n"
            "## Debate Outcome Scorecard\n\n| Field | Outcome |\n|---|---|\n| Debate winner | Balanced |\n\n"
            "**Recommendation**: Hold\n",
            encoding="utf-8",
        )

    errors = validator.validate_run_dir(output_dir)

    assert "warning: debate winner is always Balanced across a multi-ticker run" in errors
