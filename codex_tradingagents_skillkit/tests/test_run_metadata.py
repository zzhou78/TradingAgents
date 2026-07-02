from __future__ import annotations

import importlib.util
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
MODULE_PATH = BUNDLE / "scripts" / "collect_role_evidence.py"
WORKFLOW_MODULE_PATH = BUNDLE / "scripts" / "run_codex_role_workflow.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("collect_role_evidence", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_workflow_module():
    spec = importlib.util.spec_from_file_location("run_codex_role_workflow", WORKFLOW_MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _memory_map(tmp_path: Path, roles: list[str]) -> dict[str, dict[str, str]]:
    memory = {}
    for role in roles:
        root = tmp_path / "memory" / role
        root.mkdir(parents=True)
        md_path = root / "memory.md"
        json_path = root / "memory.json"
        md_path.write_text("", encoding="utf-8")
        json_path.write_text("{}", encoding="utf-8")
        memory[role] = {"root": str(root), "memory_md": str(md_path), "memory_json": str(json_path)}
    return memory


def test_workflow_state_records_run_metadata(tmp_path: Path):
    module = _load_module()
    evidence_path = tmp_path / "evidence" / "MSFT" / "2026-06-30" / "evidence.json"
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    evidence_path.parent.mkdir(parents=True)
    report_dir.mkdir(parents=True)
    role_packet_paths = {
        "market": str(evidence_path.parent / "roles" / "market.md"),
        "social": str(evidence_path.parent / "roles" / "social.md"),
        "news": str(evidence_path.parent / "roles" / "news.md"),
        "fundamentals": str(evidence_path.parent / "roles" / "fundamentals.md"),
        "financial_report": str(evidence_path.parent / "roles" / "financial_report.md"),
    }
    run_metadata = {
        "trade_date": "2026-06-30",
        "evidence_as_of_date": "2026-06-30",
        "run_executed_at": "2026-07-01T20:14:15+10:00",
        "output_dir": str(tmp_path),
        "run_id": "run:MSFT:2026-06-30:test",
        "authoritative_result_folder": True,
        "status": "pending",
    }

    workflow = module._workflow_state(
        "MSFT",
        "2026-06-30",
        ["market", "social", "news", "fundamentals"],
        role_packet_paths,
        evidence_path,
        report_dir,
        1,
        1,
        memory_map=_memory_map(tmp_path, module.ROLE_MEMORY_NAMES),
        role_evidence_paths={},
        run_metadata=run_metadata,
    )

    assert workflow["run_metadata"] == run_metadata
    assert workflow["evidence_as_of_date"] == "2026-06-30"
    assert workflow["run_executed_at"] == "2026-07-01T20:14:15+10:00"
    assert workflow["authoritative_result_folder"] is True
    assert workflow["status"] == "pending"


def test_review_status_requires_authoritative_result_folder():
    module = _load_workflow_module()

    assert (
        module._review_status(
            complete_count=1,
            total_stages=1,
            quality_errors=[],
            run_metadata={"authoritative_result_folder": False},
        )
        == "validation_only"
    )
    assert (
        module._review_status(
            complete_count=1,
            total_stages=1,
            quality_errors=[],
            run_metadata={"authoritative_result_folder": True},
        )
        == "review_ready_paper_study"
    )
