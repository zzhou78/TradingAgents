from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
VALIDATOR = BUNDLE / "scripts" / "validate_complete_report_against_roles.py"
ASSEMBLER = BUNDLE / "scripts" / "complete_report_assembly.py"


def _write_report_set(
    tmp_path: Path,
    *,
    manager_recommendation: str = "Sell",
    trader_action: str = "Sell",
    trader_final: str = "SELL",
    trader_reference_price: str = "368.57",
    portfolio_rating: str = "Underweight",
    complete_recommendation: str = "Sell",
    complete_action: str = "Sell",
    complete_final: str = "SELL",
    complete_reference_price: str = "368.57",
    market_close: str = "372.97",
    market_200_sma: str = "446.27",
    complete_market_sentence: str = "Price remains below the 200 SMA, so long-term trend support is not intact.",
) -> Path:
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    (report_dir / "1_analysts").mkdir(parents=True)
    (report_dir / "2_research").mkdir(parents=True)
    (report_dir / "3_trading").mkdir(parents=True)
    (report_dir / "5_portfolio").mkdir(parents=True)

    (report_dir / "1_analysts" / "market.md").write_text(
        "# Market Analyst\n\n"
        "## Quantitative Regime / Tool Outputs\n\n"
        f"| Latest close | {market_close} |\n"
        f"| 200 SMA | {market_200_sma} |\n\n"
        f"The latest close is below the 200 SMA because {market_close} is under {market_200_sma}.\n",
        encoding="utf-8",
    )
    (report_dir / "2_research" / "manager.md").write_text(
        "# Research Manager\n\n"
        "## Structured Evidence Matrix\n\n"
        f"**Recommendation**: {manager_recommendation}\n\n"
        "**Primary driver of rating:** weak technicals with mixed evidence.\n",
        encoding="utf-8",
    )
    (report_dir / "3_trading" / "trader.md").write_text(
        "# Trader\n\n"
        "## Action Consistency Check\n\n"
        f"**Action**: {trader_action}\n\n"
        "## Paper-study price framework\n\n"
        f"Reference price: {trader_reference_price}\n\n"
        f"FINAL TRANSACTION PROPOSAL: **{trader_final}**\n",
        encoding="utf-8",
    )
    (report_dir / "5_portfolio" / "decision.md").write_text(
        "# Portfolio Manager\n\n"
        "## Final Portfolio Decision\n\n"
        f"**Rating**: {portfolio_rating}\n",
        encoding="utf-8",
    )
    (report_dir / "complete_report.md").write_text(
        "# Trading Analysis Report: MSFT\n\n"
        "## II. Research Team Debate\n\n"
        "### Research Manager Decision - Evidence Weighing\n\n"
        f"**Recommendation**: {complete_recommendation}\n\n"
        "## III. Trading Team Plan\n\n"
        "### Trader Proposal\n\n"
        f"**Action**: {complete_action}\n\n"
        f"Reference price: {complete_reference_price}\n\n"
        f"FINAL TRANSACTION PROPOSAL: **{complete_final}**\n\n"
        "### Market Summary\n\n"
        f"{complete_market_sentence}\n\n"
        "## V. Portfolio Manager Decision\n\n"
        "### Portfolio Manager\n\n"
        f"**Rating**: {portfolio_rating}\n",
        encoding="utf-8",
    )
    return report_dir


def _run_validator(report_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )


def test_validator_fails_when_complete_report_recommendation_contradicts_manager(tmp_path: Path):
    report_dir = _write_report_set(tmp_path, manager_recommendation="Sell", complete_recommendation="Hold")

    result = _run_validator(report_dir)

    assert result.returncode != 0
    assert "Research Manager recommendation mismatch" in result.stdout


def test_validator_fails_when_complete_report_reference_price_contradicts_trader(tmp_path: Path):
    report_dir = _write_report_set(
        tmp_path,
        trader_reference_price="368.57",
        complete_reference_price="497.41",
    )

    result = _run_validator(report_dir)

    assert result.returncode != 0
    assert "Trader reference price mismatch" in result.stdout


def test_validator_fails_when_complete_report_market_language_contradicts_market_report(tmp_path: Path):
    report_dir = _write_report_set(
        tmp_path,
        market_close="372.97",
        market_200_sma="446.27",
        complete_market_sentence="A close above the 200 SMA points to long-term support intact.",
    )

    result = _run_validator(report_dir)

    assert result.returncode != 0
    assert "market-regime language contradicts Market Analyst report" in result.stdout


def test_validator_passes_when_complete_report_agrees_with_roles(tmp_path: Path):
    report_dir = _write_report_set(tmp_path)

    result = _run_validator(report_dir)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Complete report role consistency validation passed." in result.stdout


def test_assembler_rewrites_complete_report_from_role_outputs(tmp_path: Path):
    report_dir = _write_report_set(
        tmp_path,
        manager_recommendation="Sell",
        trader_action="Sell",
        trader_final="SELL",
        trader_reference_price="368.57",
        portfolio_rating="Underweight",
        complete_recommendation="Hold",
        complete_action="Hold",
        complete_final="HOLD",
        complete_reference_price="497.41",
    )

    assemble_result = subprocess.run(
        [sys.executable, str(ASSEMBLER), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert assemble_result.returncode == 0, assemble_result.stdout + assemble_result.stderr
    complete = (report_dir / "complete_report.md").read_text(encoding="utf-8")
    assert "**Recommendation**: Sell" in complete
    assert "**Action**: Sell" in complete
    assert "Reference price: 368.57" in complete
    assert "FINAL TRANSACTION PROPOSAL: **SELL**" in complete
    assert "**Rating**: Underweight" in complete
    assert "financial-report evidence and industry/theme evidence" in complete
    validate_result = _run_validator(report_dir)
    assert validate_result.returncode == 0, validate_result.stdout + validate_result.stderr


def test_assembler_displays_run_metadata_from_evidence(tmp_path: Path):
    report_dir = _write_report_set(tmp_path)
    evidence_dir = tmp_path / "evidence" / "MSFT" / "2026-06-30"
    evidence_dir.mkdir(parents=True)
    (evidence_dir / "evidence.json").write_text(
        json.dumps(
            {
                "ticker": "MSFT",
                "trade_date": "2026-06-30",
                "run_metadata": {
                    "trade_date": "2026-06-30",
                    "evidence_as_of_date": "2026-06-30",
                    "run_executed_at": "2026-07-01T20:14:15+10:00",
                    "output_dir": str(tmp_path),
                    "run_id": "run:MSFT:2026-06-30:test",
                    "authoritative_result_folder": True,
                    "status": "pending",
                },
            }
        ),
        encoding="utf-8",
    )

    assemble_result = subprocess.run(
        [sys.executable, str(ASSEMBLER), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert assemble_result.returncode == 0, assemble_result.stdout + assemble_result.stderr
    complete = (report_dir / "complete_report.md").read_text(encoding="utf-8")
    assert "Trade date: 2026-06-30" in complete
    assert "Evidence as of: 2026-06-30" in complete
    assert "Run executed at: 2026-07-01T20:14:15+10:00" in complete
    assert "Run ID: run:MSFT:2026-06-30:test" in complete
