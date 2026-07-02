from __future__ import annotations

import importlib.util
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_quality_validator():
    spec = importlib.util.spec_from_file_location("validate_quality_review", QUALITY_VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_quality_validator_rejects_stale_debate_record_index(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "AAPL" / "2026-07-02"
    report_dir.mkdir(parents=True)
    (report_dir / "debate_record.md").write_text(
        "# TradingAgents Debate Record\n\n"
        "This file is the report-folder index for Codex-visible debate turns. "
        "The turn files are prepared below and filled as Codex acts each role stage.\n",
        encoding="utf-8",
    )

    errors = validator._debate_record_quality_errors(report_dir)

    assert "debate_record.md is still a task index rather than a completed debate transcript" in errors


def test_quality_validator_accepts_completed_debate_record(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "AAPL" / "2026-07-02"
    report_dir.mkdir(parents=True)
    (report_dir / "debate_record.md").write_text(
        "# TradingAgents Debate Record\n\n"
        "- Status: completed Codex-visible debate transcript assembled from role outputs\n\n"
        "## Research Team Debate\n\n"
        "### Bull Researcher Round 1 - Opening Case\n\n- Full output: `bull_round_1.md`\n\nBody.\n\n"
        "### Bear Researcher Round 1 - Rebuttal to Bull\n\n- Full output: `bear_round_1.md`\n\nBody.\n\n"
        "### Research Manager Decision - Evidence Weighing\n\n- Full output: `manager.md`\n\nBody.\n\n"
        "## Risk Management Team Debate\n\n"
        "### Aggressive Risk Analyst Round 1 - Opportunity Case\n\n- Full output: `aggressive_round_1.md`\n\nBody.\n\n"
        "### Conservative Risk Analyst Round 1 - Response to Aggressive\n\n- Full output: `conservative_round_1.md`\n\nBody.\n\n"
        "### Neutral Risk Analyst Round 1 - Weighing\n\n- Full output: `neutral_round_1.md`\n\nBody.\n\n"
        "### Portfolio Manager Synthesis\n\n- Full output: `decision.md`\n\nBody.\n\n"
        "## Transcript Integrity\n\n- Pending debate outputs: `0`\n",
        encoding="utf-8",
    )

    assert validator._debate_record_quality_errors(report_dir) == []
