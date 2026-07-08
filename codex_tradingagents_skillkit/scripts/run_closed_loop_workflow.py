# ruff: noqa: E402

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from run_codex_role_workflow import summarize
from run_quality_remediation import run as run_quality_remediation

MATERIALITY_GATE_FIELDS = [
    "materiality_status",
    "critical_metrics_required",
    "critical_metrics_clean",
    "critical_metrics_unresolved",
    "important_metrics_clean",
    "important_metrics_unresolved",
    "supporting_metrics_clean",
    "supporting_metrics_unresolved",
    "warnings",
    "major_warnings",
    "remediation_required_reasons",
]


def _run_command(args: list[str]) -> dict[str, Any]:
    result = subprocess.run(args, text=True, capture_output=True)
    return {
        "command": args,
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def _status_from_runs(runs: list[dict[str, Any]], remediation_plans: list[dict[str, Any]]) -> str:
    if any(plan.get("remediation_tasks") for plan in remediation_plans):
        return "remediation_required"
    if any(run.get("core_metric_coverage_passed") is False for run in runs):
        return "remediation_required"
    if any(run.get("review_ready") for run in runs) and all(run.get("review_ready") for run in runs):
        return "review_ready_paper_study"
    if any(run.get("next_stage") for run in runs):
        return "pending_codex_role_execution"
    if any(run.get("quality_errors") for run in runs):
        return "remediation_required"
    return "pending"


def _write_status(output_dir: Path, payload: dict[str, Any]) -> Path:
    path = output_dir / "closed_loop_status.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def _update_run_metadata_status(output_dir: Path, status: str) -> str:
    path = output_dir / "run_metadata.json"
    if not path.exists():
        return ""
    try:
        metadata = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ""
    if not isinstance(metadata, dict):
        return ""
    metadata["status"] = status
    metadata["workflow_status"] = status
    path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return str(path)


def _sync_nested_run_metadata_status(workflow_payload: dict[str, Any], status: str) -> None:
    if status != "review_ready_paper_study":
        return
    for run in workflow_payload.get("runs", []):
        if not isinstance(run, dict) or run.get("status") != status:
            continue
        run_metadata = run.get("run_metadata")
        if not isinstance(run_metadata, dict):
            continue
        run_metadata["status"] = status
        run_metadata["workflow_status"] = status


def _materiality_gate_fields(run: dict[str, Any]) -> dict[str, Any]:
    return {field: run.get(field, [] if field != "materiality_status" else "not_applicable") for field in MATERIALITY_GATE_FIELDS}


def _patch_quality_gates_with_status(output_dir: Path, status_path: Path) -> list[str]:
    patched: list[str] = []
    for gate_path in sorted((output_dir / "reports").glob("*/*/6_quality/quality_gate.json")):
        try:
            gate = json.loads(gate_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if gate.get("passed") is True:
            gate["closed_loop_status_path"] = str(status_path)
            gate["closed_loop_status_artifact"] = "closed_loop_status.json"
            gate_path.write_text(json.dumps(gate, indent=2), encoding="utf-8")
            patched.append(str(gate_path))
    return patched


def _write_passed_quality_gates(workflow_payload: dict[str, Any], status_path: Path) -> list[str]:
    written: list[str] = []
    for run in workflow_payload.get("runs", []):
        if not isinstance(run, dict):
            continue
        if run.get("quality_errors") or not run.get("complete"):
            continue
        report_dir = Path(str(run.get("report_dir") or ""))
        if not report_dir:
            continue
        quality_dir = report_dir / "6_quality"
        quality_dir.mkdir(parents=True, exist_ok=True)
        gate_path = quality_dir / "quality_gate.json"
        payload = {
            "passed": True,
            "ticker": run.get("ticker", ""),
            "trade_date": run.get("trade_date", ""),
            "issues": [],
            "validator": "validate_quality_review.py",
            "status": run.get("materiality_status") or "workflow_complete",
            "workflow_status": "workflow_complete",
            "quality_gate_passed": bool(run.get("quality_gate_passed")),
            "evidence_reasoning_audit_status": run.get("evidence_reasoning_audit_status", "missing"),
            "evidence_reasoning_critical_findings": list(run.get("evidence_reasoning_critical_findings") or []),
            "core_metric_coverage_status": run.get("core_metric_coverage_status", "not_applicable"),
            "core_metrics_required": list(run.get("core_metrics_required") or []),
            "core_metrics_cleanly_extracted": list(run.get("core_metrics_cleanly_extracted") or []),
            "core_metrics_materially_satisfied": list(run.get("core_metrics_materially_satisfied") or []),
            "core_metrics_unavailable_with_reason": list(run.get("core_metrics_unavailable_with_reason") or []),
            "core_metrics_unresolved": list(run.get("core_metrics_unresolved") or []),
            "core_metric_coverage_passed": bool(run.get("core_metric_coverage_passed")),
            **_materiality_gate_fields(run),
            "review_ready": bool(run.get("review_ready")),
            "closed_loop_status_path": str(status_path),
            "closed_loop_status_artifact": "closed_loop_status.json",
            "notes": "Codex-session workflow and quality validators passed; see closed_loop_status.json for run-level workflow status.",
        }
        gate_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        written.append(str(gate_path))
    return written


def _write_failed_quality_gates(workflow_payload: dict[str, Any], status_path: Path) -> list[str]:
    written: list[str] = []
    for run in workflow_payload.get("runs", []):
        if not isinstance(run, dict):
            continue
        errors = list(run.get("quality_errors") or [])
        if run.get("core_metric_coverage_passed") is False and not any(
            "ASX core metric coverage failed" in str(error) for error in errors
        ):
            errors.append("ASX core metric coverage failed; review-ready quality gate cannot pass")
        if not errors:
            continue
        report_dir = Path(str(run.get("report_dir") or ""))
        if not report_dir:
            continue
        quality_dir = report_dir / "6_quality"
        quality_dir.mkdir(parents=True, exist_ok=True)
        gate_path = quality_dir / "quality_gate.json"
        payload = {
            "passed": False,
            "ticker": run.get("ticker", ""),
            "trade_date": run.get("trade_date", ""),
            "issues": [
                {
                    "severity": "major",
                    "section": "Quality Gate",
                    "issue": str(error),
                    "required_fix": "Resolve the validation failure and rerun the closed-loop workflow before review-ready status.",
                }
                for error in errors
            ],
            "validator": "validate_quality_review.py",
            "status": "remediation_required",
            "quality_gate_passed": False,
            "evidence_reasoning_audit_status": run.get("evidence_reasoning_audit_status", "missing"),
            "evidence_reasoning_critical_findings": list(run.get("evidence_reasoning_critical_findings") or []),
            "core_metric_coverage_status": run.get("core_metric_coverage_status", "not_applicable"),
            "core_metrics_required": list(run.get("core_metrics_required") or []),
            "core_metrics_cleanly_extracted": list(run.get("core_metrics_cleanly_extracted") or []),
            "core_metrics_materially_satisfied": list(run.get("core_metrics_materially_satisfied") or []),
            "core_metrics_unavailable_with_reason": list(run.get("core_metrics_unavailable_with_reason") or []),
            "core_metrics_unresolved": list(run.get("core_metrics_unresolved") or []),
            "core_metric_coverage_passed": bool(run.get("core_metric_coverage_passed")),
            **_materiality_gate_fields(run),
            "review_ready": False,
            "closed_loop_status_path": str(status_path),
            "closed_loop_status_artifact": "closed_loop_status.json",
            "notes": "Closed-loop validation failed; see quality_remediation_plan.json and next_remediation_task.md.",
        }
        gate_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        written.append(str(gate_path))
    return written


def _write_pending_quality_gates(
    workflow_payload: dict[str, Any],
    status_path: Path,
    workflow_status: str,
) -> list[str]:
    written: list[str] = []
    for run in workflow_payload.get("runs", []):
        if not isinstance(run, dict):
            continue
        if run.get("complete") or run.get("quality_errors"):
            continue
        next_stage = run.get("next_stage") if isinstance(run.get("next_stage"), dict) else {}
        report_dir = Path(str(run.get("report_dir") or ""))
        if not report_dir:
            continue
        quality_dir = report_dir / "6_quality"
        quality_dir.mkdir(parents=True, exist_ok=True)
        gate_path = quality_dir / "quality_gate.json"
        issues: list[dict[str, str]] = []
        if next_stage:
            stage = str(next_stage.get("stage") or "unknown")
            issues.append(
                {
                    "severity": "pending",
                    "section": "Workflow",
                    "issue": f"Codex role execution is not complete; next stage: {stage}",
                    "required_fix": "Run the remaining Codex role stages before marking the report review-ready.",
                }
            )
        audit_findings = list(run.get("evidence_reasoning_critical_findings") or [])
        if audit_findings:
            issues.append(
                {
                    "severity": "pending",
                    "section": "Evidence and Reasoning Audit",
                    "issue": "; ".join(str(finding) for finding in audit_findings),
                    "required_fix": "Run the Evidence and Reasoning Auditor after role outputs are complete.",
                }
            )
        payload = {
            "passed": False,
            "ticker": run.get("ticker", ""),
            "trade_date": run.get("trade_date", ""),
            "issues": issues,
            "validator": "validate_quality_review.py",
            "status": workflow_status,
            "workflow_status": workflow_status,
            "quality_gate_passed": bool(run.get("quality_gate_passed")),
            "evidence_reasoning_audit_status": run.get("evidence_reasoning_audit_status", "missing"),
            "evidence_reasoning_critical_findings": audit_findings,
            "core_metric_coverage_status": run.get("core_metric_coverage_status", "not_applicable"),
            "core_metrics_required": list(run.get("core_metrics_required") or []),
            "core_metrics_cleanly_extracted": list(run.get("core_metrics_cleanly_extracted") or []),
            "core_metrics_materially_satisfied": list(run.get("core_metrics_materially_satisfied") or []),
            "core_metrics_unavailable_with_reason": list(run.get("core_metrics_unavailable_with_reason") or []),
            "core_metrics_unresolved": list(run.get("core_metrics_unresolved") or []),
            "core_metric_coverage_passed": bool(run.get("core_metric_coverage_passed")),
            **_materiality_gate_fields(run),
            "review_ready": False,
            "closed_loop_status_path": str(status_path),
            "closed_loop_status_artifact": "closed_loop_status.json",
            "notes": (
                "Codex role workflow is pending; ASX core metric coverage fields reflect current evidence "
                "so metric blockers are distinct from role/audit completion blockers."
            ),
        }
        gate_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        written.append(str(gate_path))
    return written


def _workflow_pending_issue(run: dict[str, Any]) -> str:
    next_stage = run.get("next_stage") if isinstance(run.get("next_stage"), dict) else {}
    if next_stage:
        return f"Codex role execution is not complete; next stage: {next_stage.get('stage') or 'unknown'}"
    return "Codex role execution is not complete"


def _write_pending_remediation_artifacts(workflow_payload: dict[str, Any], workflow_status: str) -> list[str]:
    written: list[str] = []
    output_dir = Path(str(workflow_payload.get("output_dir") or ""))
    for run in workflow_payload.get("runs", []):
        if not isinstance(run, dict):
            continue
        if run.get("complete") or run.get("quality_errors") or run.get("core_metric_coverage_passed") is False:
            continue
        report_dir = Path(str(run.get("report_dir") or ""))
        if not report_dir:
            continue
        quality_dir = report_dir / "6_quality"
        quality_dir.mkdir(parents=True, exist_ok=True)
        plan_path = quality_dir / "quality_remediation_plan.json"
        task_path = quality_dir / "next_remediation_task.md"
        issue = _workflow_pending_issue(run)
        audit_findings = [str(item) for item in run.get("evidence_reasoning_critical_findings") or []]
        validator_errors = [issue, *audit_findings]
        next_stage = run.get("next_stage") if isinstance(run.get("next_stage"), dict) else {}
        task = {
            "failed_gate": "codex_role_workflow",
            "root_cause_category": "role_report_execution_pending",
            "validator_error": issue,
            "affected_files": [item for item in [next_stage.get("task_path"), next_stage.get("output_path")] if item],
            "required_fix": "Run the remaining Codex role stages and then run the Evidence and Reasoning Auditor.",
            "required_tests": [],
            "rerun_command": "",
            "blocking_for_review_grade": True,
            "status": "pending",
            "rerun_commands": [],
            "task_id": f"complete-role-workflow:{run.get('ticker', '')}:{run.get('trade_date', '')}",
        }
        workflow_path = Path(str(run.get("workflow_path") or ""))
        evidence_path = str(workflow_path.with_name("evidence.json")) if workflow_path else ""
        payload = {
            "ticker": run.get("ticker", ""),
            "trade_date": run.get("trade_date", ""),
            "report_dir": str(report_dir),
            "evidence_path": evidence_path,
            "status": workflow_status,
            "blocking_for_review_grade": True,
            "validator_errors": validator_errors,
            "evidence_metric_blockers": [],
            "core_metric_coverage_status": run.get("core_metric_coverage_status", "not_applicable"),
            "core_metric_coverage_passed": bool(run.get("core_metric_coverage_passed")),
            "materiality_status": run.get("materiality_status", "not_applicable"),
            "critical_metrics_clean": list(run.get("critical_metrics_clean") or []),
            "critical_metrics_unresolved": list(run.get("critical_metrics_unresolved") or []),
            "core_metrics_cleanly_extracted": list(run.get("core_metrics_cleanly_extracted") or []),
            "core_metrics_materially_satisfied": list(run.get("core_metrics_materially_satisfied") or []),
            "core_metrics_unresolved": list(run.get("core_metrics_unresolved") or []),
            "remediation_required_reasons": list(run.get("remediation_required_reasons") or []),
            "remediation_tasks": [task],
            "next_remediation_task_path": str(task_path),
            "next_remediation_task": task,
            "closed_loop_status_path": str(output_dir / "closed_loop_status.json") if output_dir else "closed_loop_status.json",
            "notes": (
                "No upstream ASX metric evidence blocker remains for this ticker in the current evidence run; "
                "review-grade completion is blocked by pending role reports and audit."
            ),
        }
        plan_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        task_path.write_text(
            "# Next Remediation Task\n\n"
            f"- Failed gate: {task['failed_gate']}\n"
            f"- Root cause: {task['root_cause_category']}\n"
            f"- Current blocker: {issue}\n"
            "- Evidence metric blockers: none in the current ASX core metric coverage result.\n"
            "- Required fix: run the remaining Codex role stages, then run the Evidence and Reasoning Auditor.\n",
            encoding="utf-8",
        )
        written.extend([str(plan_path), str(task_path)])
    return written


def _patch_quality_reviews_with_warnings(workflow_payload: dict[str, Any]) -> list[str]:
    warnings = [str(item) for item in workflow_payload.get("run_quality_warnings", []) if item]
    if not warnings:
        return []
    patched: list[str] = []
    warning_block = "\n".join(f"- {warning}" for warning in warnings)
    for run in workflow_payload.get("runs", []):
        if not isinstance(run, dict):
            continue
        report_dir = Path(str(run.get("report_dir") or ""))
        review_path = report_dir / "6_quality" / "quality_review.md"
        if not review_path.exists():
            continue
        text = review_path.read_text(encoding="utf-8")
        section = "## Run-Level Warnings"
        replacement = f"{section}\n{warning_block}\n\n"
        if section in text:
            text = text.split(section, 1)[0].rstrip() + "\n\n" + replacement
        else:
            text = text.rstrip() + "\n\n" + replacement
        review_path.write_text(text, encoding="utf-8")
        patched.append(str(review_path))
    return patched


def _aggregate_completion_gates(workflow_payload: dict[str, Any]) -> dict[str, Any]:
    runs = [run for run in workflow_payload.get("runs", []) if isinstance(run, dict)]
    critical: list[Any] = []
    warnings: list[Any] = []
    statuses = []
    core_required: dict[str, list[Any]] = {}
    core_clean: dict[str, list[Any]] = {}
    core_materially_satisfied: dict[str, list[Any]] = {}
    core_unavailable: dict[str, list[Any]] = {}
    core_unresolved: dict[str, list[Any]] = {}
    materiality_status_by_ticker: dict[str, str] = {}
    critical_required: dict[str, list[Any]] = {}
    critical_clean: dict[str, list[Any]] = {}
    critical_unresolved: dict[str, list[Any]] = {}
    important_clean: dict[str, list[Any]] = {}
    important_unresolved: dict[str, list[Any]] = {}
    supporting_clean: dict[str, list[Any]] = {}
    supporting_unresolved: dict[str, list[Any]] = {}
    materiality_warnings: dict[str, list[Any]] = {}
    materiality_major_warnings: dict[str, list[Any]] = {}
    remediation_required_reasons: dict[str, list[Any]] = {}
    core_statuses = []
    for run in runs:
        ticker = str(run.get("ticker") or "")
        critical.extend(run.get("evidence_reasoning_critical_findings") or [])
        warnings.extend(run.get("evidence_reasoning_warnings") or [])
        statuses.append(str(run.get("evidence_reasoning_audit_status") or "missing"))
        core_statuses.append(str(run.get("core_metric_coverage_status") or "not_applicable"))
        if run.get("core_metrics_required"):
            core_required[ticker] = list(run.get("core_metrics_required") or [])
            core_clean[ticker] = list(run.get("core_metrics_cleanly_extracted") or [])
            core_materially_satisfied[ticker] = list(run.get("core_metrics_materially_satisfied") or [])
            core_unavailable[ticker] = list(run.get("core_metrics_unavailable_with_reason") or [])
            core_unresolved[ticker] = list(run.get("core_metrics_unresolved") or [])
        if run.get("materiality_status"):
            materiality_status_by_ticker[ticker] = str(run.get("materiality_status"))
            critical_required[ticker] = list(run.get("critical_metrics_required") or [])
            critical_clean[ticker] = list(run.get("critical_metrics_clean") or [])
            critical_unresolved[ticker] = list(run.get("critical_metrics_unresolved") or [])
            important_clean[ticker] = list(run.get("important_metrics_clean") or [])
            important_unresolved[ticker] = list(run.get("important_metrics_unresolved") or [])
            supporting_clean[ticker] = list(run.get("supporting_metrics_clean") or [])
            supporting_unresolved[ticker] = list(run.get("supporting_metrics_unresolved") or [])
            materiality_warnings[ticker] = list(run.get("warnings") or [])
            materiality_major_warnings[ticker] = list(run.get("major_warnings") or [])
            remediation_required_reasons[ticker] = list(run.get("remediation_required_reasons") or [])
    if critical or any(status == "fail" for status in statuses):
        audit_status = "fail"
    elif warnings or any(status == "pass_with_warnings" for status in statuses):
        audit_status = "pass_with_warnings"
    elif statuses and all(status == "pass" for status in statuses):
        audit_status = "pass"
    else:
        audit_status = "missing"
    quality_gate_passed = bool(runs) and all(bool(run.get("quality_gate_passed")) for run in runs)
    core_metric_coverage_passed = bool(runs) and all(bool(run.get("core_metric_coverage_passed", True)) for run in runs)
    if not core_statuses or all(status == "not_applicable" for status in core_statuses):
        core_metric_status = "not_applicable"
    elif core_metric_coverage_passed:
        core_metric_status = "passed"
    else:
        core_metric_status = "failed"
    review_ready = (
        quality_gate_passed
        and not critical
        and audit_status in {"pass", "pass_with_warnings"}
        and core_metric_coverage_passed
    )
    return {
        "quality_gate_passed": quality_gate_passed,
        "evidence_reasoning_audit_status": audit_status,
        "evidence_reasoning_critical_findings": critical,
        "evidence_reasoning_warnings": warnings,
        "core_metric_coverage_status": core_metric_status,
        "core_metrics_required": core_required,
        "core_metrics_cleanly_extracted": core_clean,
        "core_metrics_materially_satisfied": core_materially_satisfied,
        "core_metrics_unavailable_with_reason": core_unavailable,
        "core_metrics_unresolved": core_unresolved,
        "core_metric_coverage_passed": core_metric_coverage_passed,
        "materiality_status": materiality_status_by_ticker,
        "critical_metrics_required": critical_required,
        "critical_metrics_clean": critical_clean,
        "critical_metrics_unresolved": critical_unresolved,
        "important_metrics_clean": important_clean,
        "important_metrics_unresolved": important_unresolved,
        "supporting_metrics_clean": supporting_clean,
        "supporting_metrics_unresolved": supporting_unresolved,
        "warnings": materiality_warnings,
        "major_warnings": materiality_major_warnings,
        "remediation_required_reasons": remediation_required_reasons,
        "review_ready": review_ready,
    }


def run_closed_loop(
    *,
    output_dir: Path,
    ticker: str = "",
    trade_date: str = "",
    collect: bool = False,
    prepare: bool = False,
    max_remediation_iterations: int = 1,
) -> dict[str, Any]:
    commands: list[dict[str, Any]] = []
    provisional_payload = {
        "output_dir": str(output_dir),
        "status": "running",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "commands": [],
        "workflow": {"runs": []},
        "remediation_plans": [],
        "closed_loop_rule": "continue from next_remediation_task.md until quality passes or a true external blocker is documented",
    }
    provisional_status_path = _write_status(output_dir, provisional_payload)
    if collect:
        if not ticker or not trade_date:
            raise ValueError("--collect requires --ticker and --trade-date")
        commands.append(
            _run_command(
                [
                    sys.executable,
                    "codex_tradingagents_skillkit/scripts/collect_role_evidence.py",
                    "--ticker",
                    ticker,
                    "--trade-date",
                    trade_date,
                    "--output-dir",
                    str(output_dir),
                ]
            )
        )
    if prepare:
        commands.append(
            _run_command(
                [
                    sys.executable,
                    "codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py",
                    "--output-dir",
                    str(output_dir),
                ]
            )
        )

    patched_quality_gates = _patch_quality_gates_with_status(output_dir, provisional_status_path)
    workflow_payload = summarize(output_dir)
    remediation_plans: list[dict[str, Any]] = []
    if any(
        run.get("quality_errors")
        or run.get("core_metric_coverage_passed") is False
        or (run.get("next_stage") or {}).get("stage") == "quality_remediation"
        for run in workflow_payload["runs"]
    ):
        for _iteration in range(max(1, max_remediation_iterations)):
            remediation_plans = run_quality_remediation(output_dir=output_dir)
            break

    status = _status_from_runs(workflow_payload["runs"], remediation_plans)
    gate_summary = _aggregate_completion_gates(workflow_payload)
    _sync_nested_run_metadata_status(workflow_payload, status)
    patched_quality_reviews = _patch_quality_reviews_with_warnings(workflow_payload)
    payload = {
        "output_dir": str(output_dir),
        "status": status,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "commands": commands,
        "workflow": workflow_payload,
        "remediation_plans": remediation_plans,
        **gate_summary,
        "patched_quality_gates": patched_quality_gates,
        "patched_quality_reviews": patched_quality_reviews,
        "written_failed_quality_gates": _write_failed_quality_gates(workflow_payload, provisional_status_path),
        "written_pending_quality_gates": _write_pending_quality_gates(
            workflow_payload,
            provisional_status_path,
            str(status),
        ),
        "written_pending_remediation_artifacts": _write_pending_remediation_artifacts(
            workflow_payload,
            str(status),
        ),
        "written_quality_gates": _write_passed_quality_gates(workflow_payload, provisional_status_path),
        "closed_loop_rule": "continue from next_remediation_task.md until quality passes or a true external blocker is documented",
    }
    payload["run_metadata_path"] = _update_run_metadata_status(output_dir, str(payload["status"]))
    payload["status_path"] = str(_write_status(output_dir, payload))
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Coordinate a Codex-session TradingAgents closed-loop workflow.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--ticker", default="")
    parser.add_argument("--trade-date", default="")
    parser.add_argument("--collect", action="store_true")
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--max-remediation-iterations", type=int, default=1)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    try:
        payload = run_closed_loop(
            output_dir=args.output_dir,
            ticker=args.ticker,
            trade_date=args.trade_date,
            collect=args.collect,
            prepare=args.prepare,
            max_remediation_iterations=args.max_remediation_iterations,
        )
    except Exception as exc:
        print(str(exc))
        return 1

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print(f"Closed-loop status: {payload['status']}")
        print(f"Status file: {payload['status_path']}")
        for plan in payload["remediation_plans"]:
            if plan.get("next_remediation_task_path"):
                print(f"Next remediation task: {plan['next_remediation_task_path']}")
    return 0 if payload["status"] == "review_ready_paper_study" else 1


if __name__ == "__main__":
    raise SystemExit(main())
