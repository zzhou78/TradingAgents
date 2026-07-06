import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
AUDITOR = BUNDLE / "scripts" / "evidence_reasoning_auditor.py"


def _load_auditor():
    spec = importlib.util.spec_from_file_location("evidence_reasoning_auditor", AUDITOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_evidence(records: list[dict[str, object]], tmp_path: Path) -> Path:
    evidence_dir = tmp_path / "evidence" / "WOW.AX" / "2026-07-02"
    financial_dir = evidence_dir / "financial_report"
    financial_dir.mkdir(parents=True)
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "WOW.AX", "trade_date": "2026-07-02"}), encoding="utf-8")
    (financial_dir / "section_records.json").write_text(json.dumps(records), encoding="utf-8")
    return evidence_path


def test_auditor_fails_clean_value_with_weak_metric_status(tmp_path: Path):
    module = _load_auditor()
    evidence_path = _write_evidence(
        [
            {
                "section_kind": "sector_metric",
                "evidence_id": "financial:WOW.AX:2026-07-02:101",
                "metric_name": "inventory",
                "status": "available",
                "clean_metric_value": "44",
                "metric_value_status": "table_row_unparsed",
                "association_score": 100,
                "direction": "supportive",
                "confidence": "medium",
                "supporting_sentence": "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201)",
            }
        ],
        tmp_path,
    )

    audit = module.audit_report_dir(tmp_path / "reports" / "WOW.AX" / "2026-07-02", evidence_path)

    assert audit["summary_verdict"] == "fail"
    assert any("clean_metric_value is populated without metric_value_status=value_extracted" in item["finding"] for item in audit["critical_findings"])


def test_auditor_fails_dense_clean_value_without_row_column_mapping(tmp_path: Path):
    module = _load_auditor()
    evidence_path = _write_evidence(
        [
            {
                "section_kind": "sector_metric",
                "evidence_id": "financial:WOW.AX:2026-07-02:102",
                "metric_name": "inventory",
                "status": "available",
                "clean_metric_value": "44",
                "metric_value_status": "value_extracted",
                "association_score": 95,
                "table_mapping_confidence": 0,
                "direction": "neutral",
                "confidence": "low",
                "row_label": "",
                "column_label": "",
                "supporting_sentence": (
                    "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201) "
                    "Net investment in inventory 44 31 13"
                ),
            }
        ],
        tmp_path,
    )

    audit = module.audit_report_dir(tmp_path / "reports" / "WOW.AX" / "2026-07-02", evidence_path)

    assert audit["summary_verdict"] == "fail"
    assert any("Dense numeric text produced a clean value without row_label and column_label" in item["finding"] for item in audit["critical_findings"])


def test_auditor_allows_narrative_ebit_margin_sentence_with_repeated_label(tmp_path: Path):
    module = _load_auditor()
    evidence_path = _write_evidence(
        [
            {
                "section_kind": "sector_metric",
                "evidence_id": "financial:WOW.AX:2026-07-02:018",
                "metric_name": "ebit_margin",
                "status": "available",
                "clean_metric_value": "82",
                "value_unit": "bps",
                "metric_value_status": "value_extracted",
                "association_score": 100,
                "table_mapping_confidence": 0,
                "direction": "adverse",
                "confidence": "medium",
                "row_label": "unavailable",
                "column_label": "unavailable",
                "supporting_sentence": (
                    "Australian Food F25 EBIT of $2,753 million declined by a normalised 10.5% "
                    "with the EBIT margin decreasing by a normalised 82 bps to 5.4%."
                ),
            }
        ],
        tmp_path,
    )

    audit = module.audit_report_dir(tmp_path / "reports" / "WOW.AX" / "2026-07-02", evidence_path)

    assert audit["critical_findings"] == []


def test_auditor_allows_valid_metric_and_warns_on_unparsed_rows(tmp_path: Path):
    module = _load_auditor()
    evidence_path = _write_evidence(
        [
            {
                "section_kind": "sector_metric",
                "evidence_id": "financial:MPL.AX:2026-07-02:201",
                "metric_name": "claims_ratio",
                "status": "available",
                "clean_metric_value": "3.3",
                "value_unit": "%",
                "metric_value_status": "value_extracted",
                "association_score": 92,
                "table_mapping_confidence": 90,
                "direction": "adverse",
                "confidence": "medium",
                "row_label": "claims ratio",
                "column_label": "change",
                "supporting_sentence": "Claims ratio increased by 3.3%.",
            },
            {
                "section_kind": "sector_metric",
                "evidence_id": "financial:WOW.AX:2026-07-02:103",
                "metric_name": "inventory",
                "status": "available",
                "clean_metric_value": "unavailable",
                "metric_value_status": "table_row_unparsed",
                "association_score": 55,
                "direction": "neutral",
                "confidence": "low",
                "supporting_sentence": "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201)",
            },
        ],
        tmp_path,
    )

    audit = module.audit_report_dir(tmp_path / "reports" / "WOW.AX" / "2026-07-02", evidence_path)

    assert audit["summary_verdict"] == "pass_with_warnings"
    assert audit["critical_findings"] == []
    assert any("row/column mapping remains unresolved" in item["warning"] for item in audit["warnings"])
