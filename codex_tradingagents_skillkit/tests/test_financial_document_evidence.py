from __future__ import annotations

import importlib.util
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
MODULE_PATH = BUNDLE / "scripts" / "financial_document_evidence.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("financial_document_evidence", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_metric_audit_review_markdown_and_csv_include_mapping_fields():
    module = _load_module()
    records = [
        {
            "section_kind": "sector_metric",
            "evidence_id": "financial:WOW.AX:2026-07-02:018",
            "ticker": "WOW.AX",
            "metric_name": "inventory",
            "sector": "retailers",
            "metric_value_status": "table_row_unparsed",
            "association_score": 45,
            "association_reason": "dense table-like row requires mapping",
            "clean_metric_value": "unavailable",
            "value_unit": "unavailable",
            "direction": "neutral",
            "confidence": "low",
            "confidence_reason": "value withheld",
            "table_title": "working_capital",
            "row_label": "unavailable",
            "column_label": "unavailable",
            "cell_value": "unavailable",
            "source_page": "12",
            "table_mapping_confidence": 0,
            "table_mapping_reason": "no mapped cell",
            "supporting_sentence": "Inventories 4,169 4,187 (18) Trade payables...",
        }
    ]

    markdown = module.render_financial_metric_audit_review_markdown(records)
    csv_text = module.render_financial_metric_audit_review_csv(records)

    assert "ASX Metric Audit Review" in markdown
    assert "table_mapping_confidence" in markdown
    assert "financial:WOW.AX:2026-07-02:018" in markdown
    assert "metric_value_status" in csv_text.splitlines()[0]
    assert "table_row_unparsed" in csv_text


def test_collect_table_extraction_diagnostics_preserves_source_summary():
    module = _load_module()
    packet = {
        "ticker": "WOW.AX",
        "trade_date": "2026-07-02",
        "market": "ASX",
        "sources": [
            {
                "source_type": "asx_announcement",
                "document_type": "Annual Report",
                "title": "2025 Annual Report",
                "url": "https://asx.example/wow.pdf",
                "announcement_date": "2025-08-15",
                "table_extraction_diagnostics": {
                    "table_rows_detected": 3,
                    "table_rows_by_strategy": {"pdfplumber_words": 3},
                    "table_rows_by_table": {"page_1_table_1001_pdfplumber_words": 3},
                    "metric_like_table_rows": [],
                    "table_row_unparsed_metrics": [],
                },
            }
        ],
    }

    diagnostics = module.collect_table_extraction_diagnostics(packet)

    assert diagnostics["ticker"] == "WOW.AX"
    assert diagnostics["source_count"] == 1
    assert diagnostics["sources"][0]["table_rows_detected"] == 3
