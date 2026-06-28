from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
SKILLS_ROOT = BUNDLE / "skills"
PREPARER = BUNDLE / "scripts" / "prepare_codex_report_tasks.py"
WRITER = BUNDLE / "scripts" / "write_codex_reports.py"
VALIDATOR = BUNDLE / "scripts" / "validate_complete_report.py"
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
    "tradingagents-industry-theme-analyst",
    "tradingagents-market-analyst",
    "tradingagents-neutral-risk-analyst",
    "tradingagents-news-analyst",
    "tradingagents-portfolio-manager",
    "tradingagents-quality-reviewer",
    "tradingagents-research-manager",
    "tradingagents-run-persistence",
    "tradingagents-sentiment-analyst",
    "tradingagents-ticker-workflow-runner",
    "tradingagents-trader",
    "tradingagents-workflow-orchestrator",
]


def _minimal_complete_report(*, action: str = "Hold", final: str = "HOLD") -> str:
    return f"""# Trading Analysis Report: AAPL

Generated: 2026-06-27

Context: comparative_run=false

## I. Analyst Team Reports

### Market Analyst

### Sentiment Analyst

### News Analyst

### Fundamentals Analyst

## II. Research Team Debate

### Bull Researcher Round 1 - Opening Case

### Bear Researcher Round 1 - Rebuttal to Bull

### Research Manager Decision - Evidence Weighing

**Recommendation**: Hold

**Primary driver of rating:** mixed

## III. Trading Team Plan

### Trader Proposal

**Action**: {action}

FINAL TRANSACTION PROPOSAL: **{final}**

## IV. Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

### Conservative Risk Analyst Round 1 - Response to Aggressive

### Neutral Risk Analyst Round 1 - Weighing

## V. Portfolio Manager Decision

### Portfolio Manager

**Rating**: Hold

## VI. Paper-Study Disclaimer

Research workflow testing only.
"""


def _write_workflow(tmp_path: Path) -> tuple[Path, dict[str, Path]]:
    output_dir = tmp_path / "run"
    evidence_dir = output_dir / "evidence" / "AAPL" / "2026-06-27"
    report_dir = output_dir / "reports" / "AAPL" / "2026-06-27"
    evidence_dir.mkdir(parents=True)
    report_dir.mkdir(parents=True)
    evidence_path = evidence_dir / "evidence.json"
    report_paths = {
        "market_report": report_dir / "1_analysts" / "market.md",
        "sentiment_report": report_dir / "1_analysts" / "sentiment.md",
        "news_report": report_dir / "1_analysts" / "news.md",
        "fundamentals_report": report_dir / "1_analysts" / "fundamentals.md",
        "bull_researcher_round_1": report_dir / "2_research" / "bull_round_1.md",
        "bear_researcher_round_1": report_dir / "2_research" / "bear_round_1.md",
        "research_manager": report_dir / "2_research" / "manager.md",
        "trader": report_dir / "3_trading" / "trader.md",
        "aggressive_risk_round_1": report_dir / "4_risk" / "aggressive_round_1.md",
        "conservative_risk_round_1": report_dir / "4_risk" / "conservative_round_1.md",
        "neutral_risk_round_1": report_dir / "4_risk" / "neutral_round_1.md",
        "portfolio_manager": report_dir / "5_portfolio" / "decision.md",
        "debate_record": report_dir / "debate_record.md",
        "complete_report": report_dir / "complete_report.md",
    }
    evidence_path.write_text(
        json.dumps(
            {
                "ticker": "AAPL",
                "trade_date": "2026-06-27",
                "identity": {
                    "company_name": "Apple Inc.",
                    "sector": "Technology",
                    "industry": "Consumer Electronics",
                },
                "roles": {
                    "news": {
                        "tool_calls": {
                            "get_news": {
                                "output": "### AAPL seeks approval to buy CXMT chips (source: Example)\nCould reduce memory pressure but adds supplier risk."
                            }
                        }
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    for path in report_paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Pending Codex role output.\n", encoding="utf-8")
    workflow = {
        "ticker": "AAPL",
        "trade_date": "2026-06-27",
        "evidence_path": str(evidence_path),
        "report_dir": str(report_dir),
        "report_paths": {key: str(path) for key, path in report_paths.items()},
    }
    (evidence_dir / "workflow_state.json").write_text(
        json.dumps(workflow),
        encoding="utf-8",
    )
    return output_dir, report_paths


def test_bundle_has_expected_skills_and_docs():
    assert (BUNDLE / "README.md").exists()
    assert (BUNDLE / "MANIFEST.md").exists()
    assert (BUNDLE / "scripts" / "collect_role_evidence.py").exists()
    assert PREPARER.exists()
    assert WRITER.exists()
    assert VALIDATOR.exists()

    readme = (BUNDLE / "README.md").read_text(encoding="utf-8")
    manifest = (BUNDLE / "MANIFEST.md").read_text(encoding="utf-8")
    assert "prepare_codex_report_tasks.py" in readme
    assert "write_codex_reports.py is a compatibility wrapper" in readme
    assert "prepare_codex_report_tasks.py" in manifest
    assert "tradingagents-industry-theme-analyst" in manifest
    assert "tradingagents-quality-reviewer" in manifest

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
    assert "tradingagents-industry-theme-analyst" in payload["workflow_skills"]
    assert "tradingagents-quality-reviewer" in payload["workflow_skills"]


def test_prepare_codex_report_tasks_writes_task_prompts_not_reports(tmp_path: Path):
    output_dir, report_paths = _write_workflow(tmp_path)

    result = subprocess.run(
        [
            sys.executable,
            str(PREPARER),
            "--output-dir",
            str(output_dir),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    task_dir = output_dir / "reports" / "AAPL" / "2026-06-27" / "tasks"
    manifest = json.loads((task_dir / "task_manifest.json").read_text(encoding="utf-8"))
    news_task = (task_dir / "news_analyst_task.md").read_text(encoding="utf-8")
    theme_task = (task_dir / "industry_theme_task.md").read_text(encoding="utf-8")
    quality_task = (task_dir / "quality_reviewer_task.md").read_text(encoding="utf-8")

    assert "AAPL: prepared Codex report tasks" in result.stdout
    assert manifest["ticker"] == "AAPL"
    assert "news_analyst_task.md" in manifest["tasks"]
    assert "Codex must write" in news_task
    assert "Do not let Python classify likely effect" in news_task
    assert "tradingagents-industry-theme-analyst" in theme_task
    assert "quality_gate.json" in quality_task
    assert report_paths["news_report"].read_text(encoding="utf-8") == "Pending Codex role output.\n"
    assert report_paths["complete_report"].read_text(encoding="utf-8") == "Pending Codex role output.\n"


def test_write_codex_reports_is_task_preparation_compatibility_wrapper(tmp_path: Path):
    output_dir, report_paths = _write_workflow(tmp_path)

    subprocess.run(
        [
            sys.executable,
            str(WRITER),
            "--output-dir",
            str(output_dir),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    task_dir = output_dir / "reports" / "AAPL" / "2026-06-27" / "tasks"
    assert (task_dir / "research_manager_task.md").exists()
    assert report_paths["research_manager"].read_text(encoding="utf-8") == "Pending Codex role output.\n"


def test_complete_report_validator_accepts_hard_contract_report(tmp_path: Path):
    report = tmp_path / "complete_report.md"
    report.write_text(_minimal_complete_report(), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_complete_report_validator_rejects_raw_social_dump(tmp_path: Path):
    report = tmp_path / "raw_social.md"
    raw_lines = "\n".join(
        f"[2026-06-27T10:0{i}:00Z - @user{i} - no-label] $AAPL repeated social line"
        for i in range(6)
    )
    report.write_text(_minimal_complete_report() + raw_lines, encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "too many raw social examples" in result.stdout


def test_complete_report_validator_rejects_post_date_social_evidence(tmp_path: Path):
    report = tmp_path / "post_date.md"
    report.write_text(
        _minimal_complete_report()
        + "[2026-06-28T00:01:00Z - @late - Bullish] $AAPL look-ahead social line\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "post-date evidence found" in result.stdout


def test_complete_report_validator_rejects_final_proposal_mismatch(tmp_path: Path):
    report = tmp_path / "mismatch.md"
    report.write_text(_minimal_complete_report(action="Hold", final="SELL"), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "final proposal mismatch" in result.stdout


def test_complete_report_validator_rejects_missing_primary_driver(tmp_path: Path):
    report = tmp_path / "missing_primary_driver.md"
    report.write_text(
        _minimal_complete_report().replace("**Primary driver of rating:** mixed\n", ""),
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "missing primary driver" in result.stdout


def test_news_theme_and_quality_skills_define_llm_reasoning_contracts():
    news = (SKILLS_ROOT / "tradingagents-news-analyst" / "SKILL.md").read_text(encoding="utf-8")
    theme = (SKILLS_ROOT / "tradingagents-industry-theme-analyst" / "SKILL.md").read_text(encoding="utf-8")
    quality = (SKILLS_ROOT / "tradingagents-quality-reviewer" / "SKILL.md").read_text(encoding="utf-8")

    for required in [
        "classify each news item using reasoning, not keywords",
        "direct company news, indirect industry/theme context, or irrelevant",
        "What could make the effect ambiguous?",
        "| Event | Relevance | Event type | Likely effect | Reason | Confidence |",
    ]:
        assert required in news

    for required in [
        "infer relevant industry context from sector, industry, company, and evidence",
        "identify relevant themes and subthemes",
        "tailwind, headwind, mixed, or irrelevant",
        "state confidence",
    ]:
        assert required in theme

    for required in [
        "complete_report.md",
        "role reports",
        "evidence summary",
        "quality_review.md",
        "quality_gate.json",
        '"passed": false',
    ]:
        assert required in quality
