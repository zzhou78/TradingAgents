from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


BUNDLE = Path(__file__).resolve().parents[1]
SKILLS_ROOT = BUNDLE / "skills"
RUNNER = (
    SKILLS_ROOT
    / "tradingagents-ticker-workflow-runner"
    / "scripts"
    / "prepare_skill_workflow.py"
)

EXPECTED_SKILLS = [
    "tradingagents-aggressive-risk-analyst",
    "tradingagents-analyst-sequencing",
    "tradingagents-bear-researcher",
    "tradingagents-bull-researcher",
    "tradingagents-conservative-risk-analyst",
    "tradingagents-dataflow-routing",
    "tradingagents-debate-routing",
    "tradingagents-fundamentals-analyst",
    "tradingagents-market-analyst",
    "tradingagents-neutral-risk-analyst",
    "tradingagents-news-analyst",
    "tradingagents-portfolio-manager",
    "tradingagents-research-manager",
    "tradingagents-run-persistence",
    "tradingagents-sentiment-analyst",
    "tradingagents-ticker-workflow-runner",
    "tradingagents-trader",
    "tradingagents-workflow-orchestrator",
]


def test_bundle_has_expected_skills_and_docs():
    assert (BUNDLE / "README.md").exists()
    assert (BUNDLE / "MANIFEST.md").exists()
    assert (BUNDLE / "scripts" / "collect_role_evidence.py").exists()
    assert (BUNDLE / "docs" / "STUDY_LOCAL_SETUP_AND_SAFETY_REVIEW.md").exists()
    assert (BUNDLE / "docs" / "ARCHITECTURE_LEARNING_NOTES.md").exists()

    readme = (BUNDLE / "README.md").read_text(encoding="utf-8")
    manifest = (BUNDLE / "MANIFEST.md").read_text(encoding="utf-8")
    assert "Real data retrieval and processing still uses upstream Python" in readme
    assert "Codex acts each TradingAgents role using the converted skills" in readme
    assert "not a vendored runtime distribution" in manifest
    assert "collect_role_evidence.py" in manifest
    assert "--ticker AAPL,MSFT" in readme

    actual = sorted(path.name for path in SKILLS_ROOT.glob("tradingagents-*") if path.is_dir())
    assert actual == sorted(EXPECTED_SKILLS)

    for skill in EXPECTED_SKILLS:
        text = (SKILLS_ROOT / skill / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert "description: Use when" in text
        assert "Do not use as real trading advice." in text
        assert "Do not connect to GCAF." in text


def test_bundle_runner_accepts_cli_tickers():
    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--ticker",
            "AAPL,MSFT",
            "--trade-date",
            "2026-06-27",
            "--format",
            "json",
        ],
        cwd=BUNDLE,
        text=True,
        capture_output=True,
        check=True,
    )

    payload = json.loads(result.stdout)
    assert [run["ticker"] for run in payload["runs"]] == ["AAPL", "MSFT"]
    assert payload["runs"][0]["asset_type"] == "stock"
    assert payload["runs"][1]["asset_type"] == "stock"
    assert "tradingagents-workflow-orchestrator" in payload["workflow_skills"]
    assert "tradingagents-dataflow-routing" in payload["workflow_skills"]
