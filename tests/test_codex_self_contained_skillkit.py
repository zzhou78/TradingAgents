from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "codex_tradingagents_skillkit"
CANONICAL_SKILLS = ROOT / ".codex" / "skills"
BUNDLE_SKILLS = BUNDLE / "skills"
RUNNER = (
    BUNDLE_SKILLS
    / "tradingagents-ticker-workflow-runner"
    / "scripts"
    / "prepare_skill_workflow.py"
)


def _skill_files(root: Path) -> dict[str, str]:
    files = {}
    for path in root.glob("tradingagents-*/**/*"):
        if path.is_file():
            files[str(path.relative_to(root)).replace("\\", "/")] = path.read_text(
                encoding="utf-8"
            )
    return files


def test_skillkit_contains_docs_tests_and_skills():
    assert (BUNDLE / "README.md").exists()
    assert (BUNDLE / "MANIFEST.md").exists()
    assert (BUNDLE / "docs" / "STUDY_LOCAL_SETUP_AND_SAFETY_REVIEW.md").exists()
    assert (BUNDLE / "docs" / "ARCHITECTURE_LEARNING_NOTES.md").exists()
    assert (BUNDLE / "tests" / "test_skillkit_bundle.py").exists()
    assert RUNNER.exists()

    readme = (BUNDLE / "README.md").read_text(encoding="utf-8")
    manifest = (BUNDLE / "MANIFEST.md").read_text(encoding="utf-8")
    assert "Real data retrieval and processing still uses upstream Python" in readme
    assert "not a vendored runtime distribution" in manifest
    assert "--ticker AAPL,MSFT" in readme


def test_skillkit_skills_mirror_discoverable_codex_skills():
    canonical = _skill_files(CANONICAL_SKILLS)
    bundled = _skill_files(BUNDLE_SKILLS)

    assert bundled == canonical


def test_skillkit_runner_accepts_ticker_list_from_bundle_path():
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
        cwd=ROOT,
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
