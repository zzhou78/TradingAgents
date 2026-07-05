from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
CLOSED_LOOP = BUNDLE / "scripts" / "run_closed_loop_workflow.py"
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_closed_loop():
    spec = importlib.util.spec_from_file_location("run_closed_loop_workflow", CLOSED_LOOP)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_quality_validator():
    spec = importlib.util.spec_from_file_location("validate_quality_review", QUALITY_VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _memory_footer() -> str:
    return """
## Memory Update

* Durable facts to retain:
* Prior mistake to avoid:
* Open questions:
* Evidence references:
* Staleness / expiry:
"""


def test_closed_loop_creates_remediation_task_for_quality_failure(tmp_path: Path):
    module = _load_closed_loop()
    output_dir = tmp_path / "run"
    evidence_dir = output_dir / "evidence" / "MSFT" / "2026-06-30"
    report_dir = output_dir / "reports" / "MSFT" / "2026-06-30"
    analyst_dir = report_dir / "1_analysts"
    evidence_dir.mkdir(parents=True)
    analyst_dir.mkdir(parents=True)
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "MSFT", "trade_date": "2026-06-30"}), encoding="utf-8")
    sentiment_report = analyst_dir / "sentiment.md"
    sentiment_report.write_text(
        "# Sentiment\n\n"
        "## Tool Outputs Used\n\n- social_evidence_processing\n\n"
        "## Social Evidence Processing Rules\n\n"
        "| Source | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral split | Confidence |\n"
        "|---|---:|---:|---|---|\n"
        "| StockTwits | 10 | 10 | 9 / 0 / 1 | high |\n\n"
        "Final sentiment is bullish because 90% of platform labels are bullish.\n"
        + _memory_footer(),
        encoding="utf-8",
    )
    workflow_path = evidence_dir / "workflow_state.json"
    workflow_path.write_text(
        json.dumps(
            {
                "ticker": "MSFT",
                "trade_date": "2026-06-30",
                "evidence_path": str(evidence_path),
                "report_dir": str(report_dir),
                "run_metadata": {"authoritative_result_folder": True},
                "stages": [
                    {
                        "stage": "sentiment_analyst",
                        "skill": "tradingagents-sentiment-analyst",
                        "allowed_inputs": [str(evidence_path)],
                        "forbidden_inputs": [],
                        "output_path": str(sentiment_report),
                        "completion_gate": "role report complete",
                        "role_execution_contract": {
                            "required_output_sections": [
                                "Tool Outputs Used",
                                "Social Evidence Processing Rules",
                            ],
                            "required_evidence_citations": [],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    payload = module.run_closed_loop(output_dir=output_dir)

    assert payload["status"] == "remediation_required"
    assert (output_dir / "closed_loop_status.json").exists()
    task_path = report_dir / "6_quality" / "next_remediation_task.md"
    plan_path = report_dir / "6_quality" / "quality_remediation_plan.json"
    assert task_path.exists()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    assert any(task["root_cause_category"] == "sentiment_quality_insufficient" for task in plan["remediation_tasks"])
    assert all(task["task_id"].startswith("remediate:MSFT:2026-06-30:") for task in plan["remediation_tasks"])
    assert all(task["rerun_commands"] for task in plan["remediation_tasks"])


def test_passed_quality_gate_requires_closed_loop_status_artifact(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "run" / "reports" / "MSFT" / "2026-07-02"
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True)
    (quality_dir / "quality_gate.json").write_text(
        json.dumps({"passed": True, "status": "workflow_complete", "issues": []}),
        encoding="utf-8",
    )
    (quality_dir / "quality_review.md").write_text(
        "# Quality Review\n\n## Tool Outputs Used\n\n- validate_quality_review.py was run and passed.\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert "closed_loop_status.json missing for completed run" in errors
    assert "quality_gate.json does not reference closed_loop_status.json" in errors


def test_passed_quality_gate_requires_evidence_reasoning_audit(tmp_path: Path):
    validator = _load_quality_validator()
    run_dir = tmp_path / "run"
    report_dir = run_dir / "reports" / "MSFT" / "2026-07-02"
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True)
    (run_dir / "closed_loop_status.json").write_text(json.dumps({"status": "running"}), encoding="utf-8")
    (quality_dir / "quality_gate.json").write_text(
        json.dumps(
            {
                "passed": True,
                "status": "workflow_complete",
                "issues": [],
                "closed_loop_status_artifact": "closed_loop_status.json",
            }
        ),
        encoding="utf-8",
    )
    (quality_dir / "quality_review.md").write_text(
        "# Quality Review\n\n## Tool Outputs Used\n\n- validate_quality_review.py was run and passed.\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert "evidence_reasoning_audit.json missing for completed run" in errors


def test_closed_loop_blocks_review_ready_when_auditor_has_critical_findings(tmp_path: Path):
    module = _load_closed_loop()
    output_dir = tmp_path / "run"
    report_dir = output_dir / "reports" / "MSFT" / "2026-07-02"
    evidence_dir = output_dir / "evidence" / "MSFT" / "2026-07-02"
    financial_dir = evidence_dir / "financial_report"
    quality_dir = report_dir / "6_quality"
    report_dir.mkdir(parents=True)
    quality_dir.mkdir(parents=True)
    financial_dir.mkdir(parents=True)
    (output_dir / "run_metadata.json").write_text(
        json.dumps(
            {
                "run_id": "test-run",
                "run_folder_name": output_dir.name,
                "ticker_list": ["MSFT"],
                "market": "US",
                "trade_date": "2026-07-02",
                "evidence_as_of_date": "2026-07-02",
                "run_executed_at": "2026-07-02T12:00:00+10:00",
                "authoritative_result_folder": True,
                "workflow_status": "running",
            }
        ),
        encoding="utf-8",
    )
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "MSFT", "trade_date": "2026-07-02"}), encoding="utf-8")
    (financial_dir / "section_records.json").write_text(
        json.dumps(
            [
                {
                    "section_kind": "sector_metric",
                    "evidence_id": "financial:MSFT:2026-07-02:901",
                    "metric_name": "inventory",
                    "status": "available",
                    "clean_metric_value": "44",
                    "metric_value_status": "table_row_unparsed",
                    "association_score": 100,
                    "direction": "supportive",
                    "confidence": "medium",
                    "supporting_sentence": "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201)",
                }
            ]
        ),
        encoding="utf-8",
    )
    output_path = report_dir / "complete_report.md"
    output_path.write_text("# Complete Report\n\n" + _memory_footer(), encoding="utf-8")
    workflow_path = evidence_dir / "workflow_state.json"
    workflow_path.write_text(
        json.dumps(
            {
                "ticker": "MSFT",
                "trade_date": "2026-07-02",
                "evidence_path": str(evidence_path),
                "report_dir": str(report_dir),
                "run_metadata": {
                    "run_folder_name": output_dir.name,
                    "authoritative_result_folder": True,
                    "status": "running",
                    "workflow_status": "running",
                },
                "stages": [
                    {
                        "stage": "complete_report",
                        "skill": "tradingagents-run-persistence",
                        "allowed_inputs": [str(evidence_path)],
                        "forbidden_inputs": [],
                        "output_path": str(output_path),
                        "completion_gate": "complete report written",
                        "role_execution_contract": {
                            "required_output_sections": [],
                            "required_evidence_citations": [],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (quality_dir / "quality_gate.json").write_text(
        json.dumps({"passed": True, "status": "workflow_complete", "issues": []}),
        encoding="utf-8",
    )
    (quality_dir / "quality_review.md").write_text(
        "# Quality Review\n\n## Tool Outputs Used\n\n- validate_quality_review.py was run and passed.\n",
        encoding="utf-8",
    )

    payload = module.run_closed_loop(output_dir=output_dir)

    assert payload["status"] == "remediation_required"
    run = payload["workflow"]["runs"][0]
    assert run["quality_gate_passed"] is True
    assert run["evidence_reasoning_audit_status"] == "fail"
    assert run["evidence_reasoning_critical_findings"]
    assert (quality_dir / "evidence_reasoning_audit.json").exists()
    assert run["review_ready"] is False


def test_run_warnings_are_written_to_quality_review_without_failure(tmp_path: Path):
    module = _load_closed_loop()
    report_dir = tmp_path / "run" / "reports" / "AAPL" / "2026-07-02"
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True)
    review_path = quality_dir / "quality_review.md"
    review_path.write_text(
        "# Quality Reviewer Report\n\n## Quality Gate Findings\n- Validators passed.\n",
        encoding="utf-8",
    )
    workflow_payload = {
        "run_quality_warnings": ["debate winner is always Balanced across a multi-ticker run"],
        "runs": [{"ticker": "AAPL", "report_dir": str(report_dir)}],
    }

    patched = module._patch_quality_reviews_with_warnings(workflow_payload)

    assert patched == [str(review_path)]
    text = review_path.read_text(encoding="utf-8")
    assert "## Run-Level Warnings" in text
    assert "debate winner is always Balanced" in text
