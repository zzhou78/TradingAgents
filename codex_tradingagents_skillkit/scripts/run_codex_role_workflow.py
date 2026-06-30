from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

PENDING_MARKER = "Pending Codex role output"

STAGE_TASK_FILES = {
    "market_analyst": "market_analyst_task.md",
    "sentiment_analyst": "sentiment_analyst_task.md",
    "news_analyst": "news_analyst_task.md",
    "fundamentals_analyst": "fundamentals_analyst_task.md",
    "financial_report_analyst": "financial_report_task.md",
    "industry_theme_discovery_analyst": "industry_theme_discovery_task.md",
    "research_manager": "research_manager_task.md",
    "trader": "trader_task.md",
    "portfolio_manager": "portfolio_manager_task.md",
    "complete_report": "complete_report_task.md",
    "quality_review": "quality_reviewer_task.md",
}

MEMORY_FOOTER_FIELDS = [
    "* Durable facts to retain:",
    "* Prior mistake to avoid:",
    "* Open questions:",
    "* Evidence references:",
    "* Staleness / expiry:",
]

EVIDENCE_ID_PATTERN = re.compile(
    r"\b(?:market|news|social|fundamentals|financial|stage):[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}\b"
)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _workflow_paths(output_dir: Path, workflow: Path | None = None) -> list[Path]:
    if workflow:
        return [workflow]
    return sorted((output_dir / "evidence").glob("*/*/workflow_state.json"))


def _is_pending_output(path: Path) -> bool:
    text = _read_text(path)
    return not path.exists() or not text.strip() or PENDING_MARKER in text


def _has_heading(text: str, heading: str) -> bool:
    return re.search(rf"^#+\s+{re.escape(heading)}\s*$", text, re.MULTILINE) is not None


def _required_sections(stage: dict[str, Any]) -> list[str]:
    contract = stage.get("role_execution_contract", {})
    sections = contract.get("required_output_sections", [])
    return [str(section) for section in sections]


def _forbidden_input_mentions(stage: dict[str, Any], text: str) -> list[str]:
    mentions = []
    for raw_path in stage.get("forbidden_inputs", []):
        path = Path(raw_path)
        candidates = {str(path), path.name}
        normalized_text = text.replace("\\", "/")
        for candidate in candidates:
            if candidate and (candidate in text or candidate.replace("\\", "/") in normalized_text):
                mentions.append(raw_path)
                break
    return mentions


def validate_stage_output(stage: dict[str, Any]) -> list[str]:
    output_path = Path(stage["output_path"])
    if _is_pending_output(output_path):
        return []

    text = _read_text(output_path)
    errors = []
    for section in _required_sections(stage):
        if not _has_heading(text, section):
            errors.append(f"missing required section: {section}")

    if not _has_heading(text, "Memory Update"):
        errors.append("missing Memory Update section")
    else:
        for field in MEMORY_FOOTER_FIELDS:
            if field not in text:
                errors.append(f"missing memory update field: {field.removesuffix(':')}")

    if stage.get("role_execution_contract", {}).get("required_evidence_citations") and not EVIDENCE_ID_PATTERN.search(text):
        allowed_inputs = "\n".join(stage.get("allowed_inputs", []))
        if not re.search(r"evidence_ledger\.jsonl|input_records\.json|evidence\.json", allowed_inputs):
            errors.append("no structured evidence source available for citation check")
        else:
            errors.append("missing evidence ID citation")

    for forbidden in _forbidden_input_mentions(stage, text):
        errors.append(f"mentions forbidden input: {forbidden}")
    return errors


def _output_stage_index(workflow: dict[str, Any]) -> dict[str, int]:
    return {str(Path(stage["output_path"])): index for index, stage in enumerate(workflow.get("stages", []))}


def _blocking_dependencies(
    *,
    workflow: dict[str, Any],
    stage: dict[str, Any],
    stage_index: int,
) -> list[str]:
    output_indexes = _output_stage_index(workflow)
    blockers = []
    for raw_input in stage.get("allowed_inputs", []):
        normalized = str(Path(raw_input))
        dependency_index = output_indexes.get(normalized)
        if dependency_index is None or dependency_index >= stage_index:
            continue
        if _is_pending_output(Path(raw_input)):
            blockers.append(raw_input)
    return blockers


def _task_file_for_stage(stage_name: str) -> str:
    if stage_name.startswith("bull_researcher_round_"):
        return f"bull_researcher_round_{stage_name.rsplit('_', 1)[-1]}_task.md"
    if stage_name.startswith("bear_researcher_round_"):
        return f"bear_researcher_round_{stage_name.rsplit('_', 1)[-1]}_task.md"
    if stage_name.startswith("aggressive_risk_round_"):
        return f"aggressive_risk_round_{stage_name.rsplit('_', 1)[-1]}_task.md"
    if stage_name.startswith("conservative_risk_round_"):
        return f"conservative_risk_round_{stage_name.rsplit('_', 1)[-1]}_task.md"
    if stage_name.startswith("neutral_risk_round_"):
        return f"neutral_risk_round_{stage_name.rsplit('_', 1)[-1]}_task.md"
    return STAGE_TASK_FILES.get(stage_name, f"{stage_name}_task.md")


def _task_path(workflow: dict[str, Any], stage: dict[str, Any]) -> str:
    report_dir = Path(workflow.get("report_dir") or Path(stage["output_path"]).parents[1])
    return str(report_dir / "tasks" / _task_file_for_stage(stage["stage"]))


def summarize_workflow(workflow_path: Path) -> dict[str, Any]:
    workflow = _read_json(workflow_path)
    stage_summaries = []
    next_stage = None
    complete_count = 0

    for index, stage in enumerate(workflow.get("stages", [])):
        output_path = Path(stage["output_path"])
        blocking_dependencies = _blocking_dependencies(workflow=workflow, stage=stage, stage_index=index)
        validation_errors = validate_stage_output(stage)

        if _is_pending_output(output_path):
            status = "blocked" if blocking_dependencies else "pending"
        elif validation_errors:
            status = "invalid"
        else:
            status = "complete"
            complete_count += 1

        summary = {
            "stage": stage["stage"],
            "skill": stage.get("skill", ""),
            "status": status,
            "task_path": _task_path(workflow, stage),
            "output_path": str(output_path),
            "blocking_dependencies": blocking_dependencies,
            "validation_errors": validation_errors,
            "completion_gate": stage.get("completion_gate", ""),
        }
        stage_summaries.append(summary)
        if next_stage is None and status in {"pending", "invalid"}:
            next_stage = summary

    quality_errors = []
    if complete_count == len(stage_summaries) and stage_summaries:
        try:
            from validate_quality_review import validate_report_dir

            quality_errors = validate_report_dir(
                Path(workflow["report_dir"]),
                Path(workflow["evidence_path"]) if workflow.get("evidence_path") else None,
            )
        except Exception as exc:  # pragma: no cover - defensive CLI reporting
            quality_errors = [f"quality validation failed to run: {exc}"]

    return {
        "ticker": workflow.get("ticker", ""),
        "trade_date": workflow.get("trade_date", ""),
        "workflow_path": str(workflow_path),
        "report_dir": workflow.get("report_dir", ""),
        "total_stages": len(stage_summaries),
        "complete_stages": complete_count,
        "next_stage": next_stage,
        "stages": stage_summaries,
        "quality_errors": quality_errors,
        "complete": complete_count == len(stage_summaries) and not quality_errors,
    }


def summarize(output_dir: Path, workflow: Path | None = None) -> dict[str, Any]:
    paths = _workflow_paths(output_dir, workflow)
    if not paths:
        raise FileNotFoundError(f"No workflow_state.json files found under {output_dir}")
    runs = [summarize_workflow(path) for path in paths]
    return {"output_dir": str(output_dir), "runs": runs}


def _print_text(payload: dict[str, Any]) -> None:
    for run in payload["runs"]:
        print(f"{run['ticker']} {run['trade_date']}: {run['complete_stages']}/{run['total_stages']} stages complete")
        next_stage = run.get("next_stage")
        if next_stage:
            print(f"Next stage: {next_stage['stage']} ({next_stage['status']})")
            print(f"Task: {next_stage['task_path']}")
            print(f"Output: {next_stage['output_path']}")
            if next_stage["blocking_dependencies"]:
                print("Blocking dependencies:")
                for dependency in next_stage["blocking_dependencies"]:
                    print(f"- {dependency}")
            if next_stage["validation_errors"]:
                print("Validation errors:")
                for error in next_stage["validation_errors"]:
                    print(f"- {error}")
        elif run["complete"]:
            print("Workflow complete.")
        else:
            print("No runnable stage; blocked stages remain.")
        if run["quality_errors"]:
            print("Quality errors:")
            for error in run["quality_errors"]:
                print(f"- {error}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report Codex-session TradingAgents role workflow status.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--workflow", type=Path)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--fail-on-incomplete", action="store_true")
    args = parser.parse_args(argv)

    try:
        payload = summarize(args.output_dir, args.workflow)
    except Exception as exc:
        print(str(exc))
        return 1

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        _print_text(payload)

    if args.fail_on_incomplete and not all(run["complete"] for run in payload["runs"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
