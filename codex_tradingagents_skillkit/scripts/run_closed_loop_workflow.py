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
    metadata["workflow_status"] = status
    path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return str(path)


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
            "status": "workflow_complete",
            "closed_loop_status_path": str(status_path),
            "closed_loop_status_artifact": "closed_loop_status.json",
            "notes": "Codex-session workflow and quality validators passed; see closed_loop_status.json for run-level workflow status.",
        }
        gate_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        written.append(str(gate_path))
    return written


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
    if any(run.get("quality_errors") or (run.get("next_stage") or {}).get("stage") == "quality_remediation" for run in workflow_payload["runs"]):
        for _iteration in range(max(1, max_remediation_iterations)):
            remediation_plans = run_quality_remediation(output_dir=output_dir)
            break

    payload = {
        "output_dir": str(output_dir),
        "status": _status_from_runs(workflow_payload["runs"], remediation_plans),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "commands": commands,
        "workflow": workflow_payload,
        "remediation_plans": remediation_plans,
        "patched_quality_gates": patched_quality_gates,
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
