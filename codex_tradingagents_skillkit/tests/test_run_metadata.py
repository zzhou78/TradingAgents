from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
MODULE_PATH = BUNDLE / "scripts" / "collect_role_evidence.py"
WORKFLOW_MODULE_PATH = BUNDLE / "scripts" / "run_codex_role_workflow.py"
QUALITY_VALIDATOR_PATH = BUNDLE / "scripts" / "validate_quality_review.py"


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


def _load_quality_validator():
    spec = importlib.util.spec_from_file_location("validate_quality_review", QUALITY_VALIDATOR_PATH)
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


def test_run_folder_trade_date_mismatch_requires_explicit_metadata(tmp_path: Path):
    module = _load_workflow_module()
    output_dir = tmp_path / "aapl_msft_2026-06-30_review_gate_fixed"
    workflow_path = output_dir / "evidence" / "AAPL" / "2026-07-02" / "workflow_state.json"
    workflow_path.parent.mkdir(parents=True)
    workflow = {
        "ticker": "AAPL",
        "trade_date": "2026-07-02",
        "output_dir": str(output_dir),
        "run_metadata": {
            "trade_date": "2026-07-02",
            "run_folder_name": output_dir.name,
            "authoritative_result_folder": True,
        },
    }

    errors = module._run_metadata_errors(workflow_path, workflow)

    assert "run_metadata.json missing for run folder" in errors
    assert "run folder trade_date mismatch has no explicit run_metadata.json" in errors


def test_run_folder_metadata_file_can_explain_date_mismatch(tmp_path: Path):
    module = _load_workflow_module()
    output_dir = tmp_path / "aapl_msft_review"
    workflow_path = output_dir / "evidence" / "AAPL" / "2026-07-02" / "workflow_state.json"
    workflow_path.parent.mkdir(parents=True)
    (output_dir / "run_metadata.json").write_text(
        json.dumps(
            {
                "run_id": "aapl_msft_review:AAPL:2026-07-02:test",
                "run_folder_name": output_dir.name,
                "ticker_list": ["AAPL"],
                "market": "US",
                "trade_date": "2026-07-02",
                "evidence_as_of_date": "2026-07-02",
                "run_executed_at": "2026-07-02T12:00:00+10:00",
                "authoritative_result_folder": str(output_dir),
                "workflow_status": "pending",
            }
        ),
        encoding="utf-8",
    )
    workflow = {
        "ticker": "AAPL",
        "trade_date": "2026-07-02",
        "output_dir": str(output_dir),
        "run_metadata": {
            "trade_date": "2026-07-02",
            "run_folder_name": output_dir.name,
            "authoritative_result_folder": False,
        },
    }

    assert module._run_metadata_errors(workflow_path, workflow) == []


def test_run_metadata_requires_market_field(tmp_path: Path):
    module = _load_workflow_module()
    output_dir = tmp_path / "asx_2026-07-02_closed_loop"
    workflow_path = output_dir / "evidence" / "BHP.AX" / "2026-07-02" / "workflow_state.json"
    workflow_path.parent.mkdir(parents=True)
    (output_dir / "run_metadata.json").write_text(
        json.dumps(
            {
                "run_id": "asx_2026-07-02_closed_loop:BHP.AX:2026-07-02:test",
                "run_folder_name": output_dir.name,
                "ticker_list": ["BHP.AX"],
                "trade_date": "2026-07-02",
                "evidence_as_of_date": "2026-07-02",
                "run_executed_at": "2026-07-02T12:00:00+10:00",
                "authoritative_result_folder": str(output_dir),
                "workflow_status": "pending",
            }
        ),
        encoding="utf-8",
    )
    workflow = {
        "ticker": "BHP.AX",
        "trade_date": "2026-07-02",
        "output_dir": str(output_dir),
        "run_metadata": {
            "trade_date": "2026-07-02",
            "run_folder_name": output_dir.name,
            "authoritative_result_folder": True,
        },
    }

    assert "run_metadata.json missing required field: market" in module._run_metadata_errors(workflow_path, workflow)


def test_closed_loop_review_ready_status_requires_nested_metadata_match(tmp_path: Path):
    validator = _load_quality_validator()
    output_dir = tmp_path / "us_2026-07-02_closed_loop"
    output_dir.mkdir()
    (output_dir / "run_metadata.json").write_text(
        json.dumps({"status": "pending", "workflow_status": "pending"}),
        encoding="utf-8",
    )
    (output_dir / "closed_loop_status.json").write_text(
        json.dumps(
            {
                "status": "review_ready_paper_study",
                "workflow": {
                    "runs": [
                        {
                            "ticker": "AAPL",
                            "status": "review_ready_paper_study",
                            "run_metadata": {"status": "pending", "workflow_status": "pending"},
                        }
                    ]
                },
            }
        ),
        encoding="utf-8",
    )

    errors = validator.validate_run_dir(output_dir)

    assert "run_metadata.json status does not match closed_loop_status.json status" in errors
    assert (
        "closed_loop_status.json nested run_metadata.workflow_status for AAPL does not match outer run status"
        in errors
    )
