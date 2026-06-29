from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROLE_MEMORY_NAMES = {
    "market_analyst",
    "sentiment_analyst",
    "news_analyst",
    "fundamentals_analyst",
    "financial_report_analyst",
    "industry_theme_discovery_analyst",
    "bull_researcher",
    "bear_researcher",
    "research_manager",
    "trader",
    "aggressive_risk_analyst",
    "conservative_risk_analyst",
    "neutral_risk_analyst",
    "portfolio_manager",
    "quality_reviewer",
}


def _workflow_paths(output_dir: Path) -> list[Path]:
    return sorted((output_dir / "evidence").glob("*/*/workflow_state.json"))


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _is_pending_output(path: Path) -> bool:
    if not path.exists():
        return True
    return "Pending Codex role output" in path.read_text(encoding="utf-8", errors="replace")


def _memory_update_section(text: str) -> str:
    marker = "## Memory Update"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1]


def _memory_update_is_meaningful(text: str) -> bool:
    section = _memory_update_section(text)
    if not section:
        return False
    lowered = section.lower()
    if "no durable role-memory update" in lowered or "none recorded yet" in lowered:
        return False
    for line in section.splitlines():
        if "evidence references" not in line.lower():
            continue
        value = line.split(":", 1)[1].strip() if ":" in line else ""
        value = value.strip("-* `")
        return bool(value and value.lower() not in {"none", "n/a", "not applicable"})
    return False


def _validate_workflow(workflow_path: Path) -> list[str]:
    issues: list[str] = []
    workflow = _read_json(workflow_path)
    ticker = workflow["ticker"]
    memory_root = Path(workflow.get("memory_root", workflow_path.parents[3] / "memory" / ticker))
    for role in ROLE_MEMORY_NAMES:
        role_root = memory_root / role
        if not (role_root / "memory.md").exists():
            issues.append(f"{ticker}: missing memory.md for {role}")
        if not (role_root / "memory.json").exists():
            issues.append(f"{ticker}: missing memory.json for {role}")

    for stage in workflow.get("stages", []):
        stage_name = stage.get("stage", "unknown")
        role_memory = stage.get("role_memory")
        allowed_memory = [Path(path) for path in stage.get("allowed_memory_files", [])]
        forbidden_roots = [Path(path) for path in stage.get("forbidden_memory_roots", [])]
        if not role_memory:
            issues.append(f"{ticker}/{stage_name}: missing role_memory")
            continue
        if role_memory not in ROLE_MEMORY_NAMES:
            issues.append(f"{ticker}/{stage_name}: unknown role_memory {role_memory}")
        if len(allowed_memory) < 2:
            issues.append(f"{ticker}/{stage_name}: missing allowed_memory_files")
        for path in allowed_memory:
            if memory_root / role_memory not in path.parents:
                issues.append(f"{ticker}/{stage_name}: allowed memory crosses role boundary: {path}")
        for other_role in ROLE_MEMORY_NAMES - {role_memory}:
            expected_root = memory_root / other_role
            if expected_root not in forbidden_roots:
                issues.append(f"{ticker}/{stage_name}: missing forbidden memory root {expected_root}")
        output_path = Path(stage.get("output_path", ""))
        if output_path.exists() and not _is_pending_output(output_path):
            text = output_path.read_text(encoding="utf-8", errors="replace")
            if "## Memory Update" not in text:
                issues.append(f"{ticker}/{stage_name}: output missing Memory Update section")
            elif not _memory_update_is_meaningful(text):
                issues.append(f"{ticker}/{stage_name}: memory update is placeholder or not evidence-linked")
            for forbidden_root in forbidden_roots:
                if str(forbidden_root) in text:
                    issues.append(f"{ticker}/{stage_name}: output references forbidden memory root {forbidden_root}")

    report_dir = Path(workflow.get("report_dir", ""))
    quality_gate = report_dir / "6_quality" / "quality_gate.json"
    if issues and quality_gate.exists():
        try:
            gate = _read_json(quality_gate)
            if gate.get("passed") is True:
                issues.append(f"{ticker}: quality_gate.json passes despite memory isolation issue")
        except json.JSONDecodeError:
            issues.append(f"{ticker}: quality_gate.json is not valid JSON")
    return issues


def validate(output_dir: Path) -> list[str]:
    paths = _workflow_paths(output_dir)
    if not paths:
        return [f"No workflow_state.json files found under {output_dir}"]
    issues: list[str] = []
    for workflow_path in paths:
        issues.extend(_validate_workflow(workflow_path))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Codex TradingAgents role-memory isolation contracts.")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    issues = validate(args.output_dir)
    if issues:
        print("Role memory validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Role memory validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
