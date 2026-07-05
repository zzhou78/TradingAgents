from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from validate_quality_review import validate_report_dir


@dataclass(frozen=True)
class RemediationRule:
    marker: str
    failed_gate: str
    root_cause_category: str
    affected_files: tuple[str, ...]
    required_fix: str
    required_tests: tuple[str, ...]


RULES = (
    RemediationRule(
        marker="news evidence has no full-text articles",
        failed_gate="news_full_text_coverage_gate",
        root_cause_category="news_full_text_retrieval",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/news_article_evidence.py",
            "codex_tradingagents_skillkit/scripts/collect_role_evidence.py",
            "codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md",
        ),
        required_fix="Add or improve full-text retrieval for directly relevant candidate news and keep snippet-only items low confidence.",
        required_tests=(
            "tests/test_news_article_evidence.py",
            "codex_tradingagents_skillkit/tests/test_skillkit_bundle.py::test_quality_validator_fails_review_gate_when_all_news_evidence_is_snippet_only",
        ),
    ),
    RemediationRule(
        marker="news evidence has no full-text articles",
        failed_gate="news_article_quality_gate",
        root_cause_category="news_article_quality_insufficient",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/news_article_evidence.py",
            "codex_tradingagents_skillkit/scripts/news_article_quality.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md",
        ),
        required_fix="Ensure snippet-only article evidence remains low-confidence and cannot support review-grade completion without stronger article text or an explicit blocker.",
        required_tests=(
            "codex_tradingagents_skillkit/tests/test_news_article_quality_gate.py",
            "codex_tradingagents_skillkit/tests/test_skillkit_bundle.py::test_quality_validator_fails_review_gate_when_all_news_evidence_is_snippet_only",
        ),
    ),
    RemediationRule(
        marker="news source discovery found no usable news candidates",
        failed_gate="news_source_discovery_gate",
        root_cause_category="news_source_discovery_insufficient",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/news_sources/",
            "codex_tradingagents_skillkit/scripts/collect_role_evidence.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md",
        ),
        required_fix="Improve news candidate discovery or document an approved external source blocker; review-grade reports need at least one usable direct-company, official, or major-media news candidate.",
        required_tests=(
            "codex_tradingagents_skillkit/tests/test_news_sources.py",
            "codex_tradingagents_skillkit/tests/test_news_article_quality_gate.py",
        ),
    ),
    RemediationRule(
        marker="upstream fallback is the only",
        failed_gate="news_source_discovery_gate",
        root_cause_category="news_source_discovery_insufficient",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/news_sources/",
            "codex_tradingagents_skillkit/scripts/collect_role_evidence.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md",
        ),
        required_fix="Improve news source discovery so review-grade reports do not depend only on upstream TradingAgents fallback news.",
        required_tests=(
            "codex_tradingagents_skillkit/tests/test_news_sources.py",
            "codex_tradingagents_skillkit/tests/test_news_article_quality_gate.py",
        ),
    ),
    RemediationRule(
        marker="weak or blocked news article",
        failed_gate="news_article_quality_gate",
        root_cause_category="news_article_quality_insufficient",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/news_article_retrieval.py",
            "codex_tradingagents_skillkit/scripts/news_article_quality.py",
            "codex_tradingagents_skillkit/scripts/news_article_cards.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
        ),
        required_fix="Repair article extraction and quality scoring so error, paywall, video-only, or irrelevant pages are not treated as verified article text.",
        required_tests=(
            "tests/test_news_article_evidence.py",
            "codex_tradingagents_skillkit/tests/test_news_article_quality_gate.py",
        ),
    ),
    RemediationRule(
        marker="sentiment source confidence is unsupported",
        failed_gate="sentiment_quality_gate",
        root_cause_category="sentiment_quality_insufficient",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/sentiment_item_quality.py",
            "codex_tradingagents_skillkit/scripts/sentiment_evidence_cards.py",
            "codex_tradingagents_skillkit/scripts/social_evidence.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-sentiment-analyst/SKILL.md",
        ),
        required_fix="Downgrade or filter low-information social items and prevent platform labels or memes from supporting medium/high-confidence sentiment.",
        required_tests=(
            "tests/test_social_fundamentals_stage_evidence.py",
            "codex_tradingagents_skillkit/tests/test_sentiment_quality_gate.py",
        ),
    ),
    RemediationRule(
        marker="sentiment conclusion is based only on raw social counts",
        failed_gate="sentiment_report_quality_gate",
        root_cause_category="sentiment_quality_insufficient",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-sentiment-analyst/SKILL.md",
        ),
        required_fix="Require Sentiment Analyst reports to cite reasoned, ticker-relevant social evidence instead of raw bullish/bearish counts or platform labels.",
        required_tests=("codex_tradingagents_skillkit/tests/test_sentiment_quality_gate.py",),
    ),
    RemediationRule(
        marker="financial evidence lacks extracted MD&A",
        failed_gate="financial_mda_section_gate",
        root_cause_category="sec_mda_extraction",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/financial_document_sources.py",
            "codex_tradingagents_skillkit/scripts/financial_document_evidence.py",
            "codex_tradingagents_skillkit/skills/tradingagents-financial-report-analyst/SKILL.md",
        ),
        required_fix="Improve 10-K and 10-Q MD&A section extraction and preserve section-level records with evidence gaps when unavailable.",
        required_tests=(
            "tests/test_financial_document_sources.py",
            "tests/test_financial_document_evidence.py",
            "codex_tradingagents_skillkit/tests/test_skillkit_bundle.py::test_quality_validator_fails_review_gate_when_financial_sections_are_not_deep_enough",
        ),
    ),
    RemediationRule(
        marker="earnings 8-K exhibit is unavailable",
        failed_gate="financial_8k_exhibit_gate",
        root_cause_category="sec_8k_exhibit_extraction",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/financial_document_sources.py",
            "codex_tradingagents_skillkit/scripts/financial_document_evidence.py",
        ),
        required_fix="Parse SEC filing indexes for Exhibit 99.1 or equivalent earnings-release exhibits and distinguish them from cover-page evidence.",
        required_tests=(
            "tests/test_financial_document_sources.py::test_extracts_exhibit_99_1_when_present",
            "tests/test_financial_document_sources.py::test_records_unavailable_exhibit_when_missing",
        ),
    ),
    RemediationRule(
        marker="financial evidence lacks extracted cash-flow statement section",
        failed_gate="financial_cash_flow_section_gate",
        root_cause_category="sec_cash_flow_extraction",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/financial_document_sources.py",
            "codex_tradingagents_skillkit/scripts/financial_document_evidence.py",
        ),
        required_fix="Improve filing table/section extraction so cash-flow statement evidence is captured separately from generic filing text.",
        required_tests=(
            "tests/test_financial_document_sources.py",
            "tests/test_financial_document_evidence.py",
        ),
    ),
    RemediationRule(
        marker="evidence_reasoning_audit.json",
        failed_gate="evidence_reasoning_audit_gate",
        root_cause_category="evidence_reasoning_audit_failure",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/evidence_reasoning_auditor.py",
            "codex_tradingagents_skillkit/scripts/run_codex_role_workflow.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-evidence-and-reasoning-auditor/SKILL.md",
        ),
        required_fix="Repair the evidence substrate, metric extraction, report reasoning, or auditor rule that produced critical evidence/reasoning findings.",
        required_tests=(
            "codex_tradingagents_skillkit/tests/test_closed_loop_workflow.py",
            "codex_tradingagents_skillkit/tests/test_evidence_reasoning_auditor.py",
        ),
    ),
    RemediationRule(
        marker="ASX source collection failed",
        failed_gate="asx_official_source_gate",
        root_cause_category="asx_official_source_collection",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/financial_document_sources_asx.py",
            "codex_tradingagents_skillkit/scripts/collect_role_evidence.py",
        ),
        required_fix="Repair official ASX or investor-relations source collection before marking ASX company reports review-ready.",
        required_tests=("codex_tradingagents_skillkit/tests/test_skillkit_bundle.py::test_quality_validator_fails_asx_report_when_asx_source_collection_failed",),
    ),
    RemediationRule(
        marker="mismatch",
        failed_gate="complete_report_role_consistency_gate",
        root_cause_category="complete_report_assembly_mismatch",
        affected_files=(
            "codex_tradingagents_skillkit/scripts/complete_report_assembly.py",
            "codex_tradingagents_skillkit/scripts/validate_complete_report_against_roles.py",
            "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
            "codex_tradingagents_skillkit/skills/tradingagents-run-persistence/SKILL.md",
        ),
        required_fix="Make complete_report.md assembly parse and preserve actual role outputs instead of generating contradictory summary text.",
        required_tests=(
            "codex_tradingagents_skillkit/tests/test_complete_report_role_consistency.py",
            "codex_tradingagents_skillkit/tests/test_skillkit_bundle.py::test_quality_validator_fails_when_complete_report_contradicts_trader",
        ),
    ),
)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _workflow_paths(output_dir: Path) -> list[Path]:
    return sorted((output_dir / "evidence").glob("*/*/workflow_state.json"))


def _identity(report_dir: Path, evidence_path: Path | None) -> tuple[str, str]:
    if evidence_path and evidence_path.exists():
        try:
            evidence = _read_json(evidence_path)
        except json.JSONDecodeError:
            evidence = {}
        ticker = str(evidence.get("ticker") or "")
        trade_date = str(evidence.get("trade_date") or "")
        if ticker and trade_date:
            return ticker, trade_date
    parts = report_dir.parts
    if len(parts) >= 2:
        return parts[-2], parts[-1]
    return "", ""


def _rerun_command(*, ticker: str, trade_date: str, output_dir: Path | None) -> str:
    output = str(output_dir) if output_dir else "<output-dir>"
    return (
        ".\\.venv\\Scripts\\python.exe codex_tradingagents_skillkit\\scripts\\collect_role_evidence.py "
        f"--ticker {ticker or '<ticker>'} --trade-date {trade_date or '<trade-date>'} --output-dir {output}"
    )


def _tasks_for_error(error: str, *, rerun_command: str) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    for rule in RULES:
        if rule.marker.lower() in error.lower():
            tasks.append(
                {
                    "failed_gate": rule.failed_gate,
                    "root_cause_category": rule.root_cause_category,
                    "validator_error": error,
                    "affected_files": list(rule.affected_files),
                    "required_fix": rule.required_fix,
                    "required_tests": list(rule.required_tests),
                    "rerun_command": rerun_command,
                    "blocking_for_review_grade": True,
                    "status": "pending",
                }
            )
    if tasks:
        return tasks
    return [
        {
            "failed_gate": "quality_review_gate",
            "root_cause_category": "report_quality_validation",
            "validator_error": error,
            "affected_files": [
                "codex_tradingagents_skillkit/scripts/validate_quality_review.py",
                "codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md",
            ],
            "required_fix": "Inspect the validator error and repair the relevant report, prompt, validator, or evidence adapter.",
            "required_tests": ["codex_tradingagents_skillkit/tests/test_skillkit_bundle.py"],
            "rerun_command": rerun_command,
            "blocking_for_review_grade": True,
            "status": "pending",
        }
    ]


def build_remediation_plan(
    *,
    report_dir: Path,
    evidence_path: Path | None,
    output_dir: Path | None = None,
) -> dict[str, Any]:
    errors = validate_report_dir(report_dir, evidence_path)
    ticker, trade_date = _identity(report_dir, evidence_path)
    rerun_command = _rerun_command(ticker=ticker, trade_date=trade_date, output_dir=output_dir)
    created_at = datetime.now().astimezone().isoformat(timespec="seconds")
    seen: set[tuple[str, str]] = set()
    tasks = []
    for error in errors:
        for task in _tasks_for_error(error, rerun_command=rerun_command):
            key = (task["failed_gate"], task["root_cause_category"])
            if key in seen:
                continue
            seen.add(key)
            task["task_id"] = f"remediate:{ticker or 'UNKNOWN'}:{trade_date or 'UNKNOWN'}:{len(tasks) + 1:03d}"
            task["rerun_commands"] = [rerun_command]
            task["created_at"] = created_at
            task["updated_at"] = created_at
            tasks.append(task)
    status = "remediation_required" if tasks else "no_remediation_required"
    return {
        "ticker": ticker,
        "trade_date": trade_date,
        "report_dir": str(report_dir),
        "evidence_path": str(evidence_path) if evidence_path else "",
        "status": status,
        "blocking_for_review_grade": bool(tasks),
        "validator_errors": errors,
        "remediation_tasks": tasks,
    }


def write_plan(plan: dict[str, Any], report_dir: Path) -> Path:
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True, exist_ok=True)
    plan_path = quality_dir / "quality_remediation_plan.json"
    plan_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    return plan_path


def _next_pending_task(plan: dict[str, Any]) -> dict[str, Any] | None:
    for task in plan.get("remediation_tasks", []):
        if task.get("status") == "pending":
            return task
    return None


def write_next_task(plan: dict[str, Any], report_dir: Path) -> Path | None:
    task = _next_pending_task(plan)
    if not task:
        return None
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True, exist_ok=True)
    task_path = quality_dir / "next_remediation_task.md"
    affected_files = "\n".join(f"- `{path}`" for path in task["affected_files"])
    required_tests = "\n".join(f"- `{test}`" for test in task["required_tests"])
    task_path.write_text(
        f"""# Next Quality Remediation Task

Ticker: `{plan.get('ticker', '')}`
Trade date: `{plan.get('trade_date', '')}`
Root cause category: `{task['root_cause_category']}`
Failed gate: `{task['failed_gate']}`
Status: `{task['status']}`

## Validator Error

{task['validator_error']}

## Required Fix

{task['required_fix']}

## Affected Files

{affected_files}

## Required Tests

{required_tests}

## Verification And Rerun

1. Implement the required fix with tests.
2. Run the required tests and the relevant full verification suite.
3. Rerun evidence collection and report workflow using:

```powershell
{task['rerun_command']}
```

4. Rerun the Codex workflow controller.
5. Update `quality_remediation_plan.json` task status only after the quality gate no longer reports this failure.

## Closed-Loop Rule

Do not stop at this task file. Codex must implement the fix, rerun the workflow,
and continue with the next pending remediation task until the quality gate passes
or a true external blocker is documented.
""",
        encoding="utf-8",
    )
    plan["next_remediation_task_path"] = str(task_path)
    plan["next_remediation_task"] = task
    return task_path


def _runs_from_output_dir(output_dir: Path) -> list[tuple[Path, Path | None]]:
    runs = []
    for workflow_path in _workflow_paths(output_dir):
        workflow = _read_json(workflow_path)
        report_dir = Path(workflow["report_dir"])
        evidence_path = Path(workflow["evidence_path"]) if workflow.get("evidence_path") else None
        runs.append((report_dir, evidence_path))
    return runs


def run(
    *,
    output_dir: Path | None = None,
    report_dir: Path | None = None,
    evidence_path: Path | None = None,
) -> list[dict[str, Any]]:
    if output_dir:
        runs = _runs_from_output_dir(output_dir)
    elif report_dir:
        runs = [(report_dir, evidence_path)]
    else:
        raise ValueError("Provide --output-dir or --report-dir")
    plans = []
    for current_report_dir, current_evidence_path in runs:
        plan = build_remediation_plan(
            report_dir=current_report_dir,
            evidence_path=current_evidence_path,
            output_dir=output_dir,
        )
        task_path = write_next_task(plan, current_report_dir)
        plan_path = write_plan(plan, current_report_dir)
        plan["plan_path"] = str(plan_path)
        if task_path:
            plan["next_remediation_task_path"] = str(task_path)
        plans.append(plan)
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Codex TradingAgents quality remediation plans.")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--report-dir", type=Path)
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args(argv)

    try:
        plans = run(output_dir=args.output_dir, report_dir=args.report_dir, evidence_path=args.evidence)
    except Exception as exc:
        print(str(exc))
        return 2
    for plan in plans:
        print(f"{plan['ticker']} {plan['trade_date']}: {plan['status']}")
        print(f"Plan: {plan['plan_path']}")
        if plan.get("next_remediation_task_path"):
            print(f"Next task: {plan['next_remediation_task_path']}")
        for task in plan["remediation_tasks"]:
            print(f"- {task['root_cause_category']}: {task['required_fix']}")
    return 1 if any(plan["remediation_tasks"] for plan in plans) else 0


if __name__ == "__main__":
    raise SystemExit(main())
