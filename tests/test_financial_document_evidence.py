from __future__ import annotations

from codex_tradingagents_skillkit.scripts.financial_document_evidence import (
    build_financial_document_evidence,
)


def test_build_financial_document_evidence_flattens_sections_exhibits_and_gaps():
    packet = {
        "ticker": "MSFT",
        "trade_date": "2026-06-29",
        "sources": [
            {
                "source_type": "annual_report_10k",
                "status": "available",
                "filing_date": "2025-07-30",
                "url": "https://sec.example/10k.htm",
                "sections": [
                    {
                        "section_type": "business_overview",
                        "section_name": "10-K business overview",
                        "status": "available",
                        "source_type": "annual_report_10k",
                        "filing_date": "2025-07-30",
                        "url": "https://sec.example/10k.htm",
                        "excerpt": "Business overview discusses cloud and AI demand.",
                        "supports_claims": ["business model", "revenue drivers"],
                    }
                ],
            },
            {
                "source_type": "quarterly_report_10q",
                "status": "available",
                "filing_date": "2026-04-29",
                "url": "https://sec.example/10q.htm",
                "sections": [
                    {
                        "section_type": "commitments_capex_contractual_obligations",
                        "section_name": "10-Q commitments / capex / contractual obligations",
                        "status": "unavailable",
                        "source_type": "quarterly_report_10q",
                        "filing_date": "2026-04-29",
                        "url": "https://sec.example/10q.htm",
                        "excerpt": "",
                        "supports_claims": ["capex", "commitments"],
                        "unavailable_reason": "Capex section was not identified.",
                    }
                ],
            },
            {
                "source_type": "earnings_release_8k",
                "status": "available",
                "filing_date": "2026-04-30",
                "url": "https://sec.example/8k.htm",
                "cover_page": {
                    "status": "available",
                    "source_type": "earnings_release_8k_cover_page",
                    "filing_date": "2026-04-30",
                    "url": "https://sec.example/8k.htm",
                    "excerpt": "8-K cover page says Exhibit 99.1 was furnished.",
                    "supports_claims": ["8-K item routing"],
                },
                "exhibit_99_1": {
                    "status": "available",
                    "source_type": "earnings_release_exhibit",
                    "exhibit_name": "Exhibit 99.1",
                    "filing_date": "2026-04-30",
                    "url": "https://sec.example/ex991.htm",
                    "excerpt": "Exhibit 99.1 discusses revenue growth and guidance.",
                    "supports_claims": ["guidance", "earnings release"],
                },
            },
            {
                "source_type": "asx_announcement",
                "status": "available",
                "announcement_date": "2025-08-12",
                "url": "https://asx.example/annual.pdf",
                "extracted_sections": [
                    {
                        "section_name": "sector_metric_ebit_margin",
                        "section_type": "sector_metric",
                        "status": "available",
                        "source_type": "asx_announcement",
                        "filing_date": "2025-08-12",
                        "url": "https://asx.example/annual.pdf",
                        "excerpt": "EBIT margin decreasing by 82 bps.",
                        "supports_claims": ["EBIT margin"],
                        "metric_name": "ebit_margin",
                        "metric_label": "EBIT margin",
                        "sector": "retailers",
                        "metric_value_status": "value_extracted",
                        "association_score": 92,
                        "association_reason": "table row label matches accepted metric label",
                        "clean_metric_value": "82",
                        "value_unit": "bps",
                        "value_context": "table row/column label association",
                        "period_reference": "FY2025",
                        "comparison_reference": "FY2024",
                        "supporting_sentence": "EBIT margin decreasing by 82 bps.",
                        "comparison_basis": "period-over-period wording",
                        "direction": "adverse",
                        "confidence_reason": "clean value accepted",
                        "table_title": "Segment performance",
                        "row_label": "EBIT margin",
                        "column_label": "FY2025",
                        "source_page": "12",
                    }
                ],
            },
            {
                "source_type": "investor_presentation",
                "source_name": "Latest investor presentation",
                "status": "unavailable",
                "reason": "No investor presentation source was discovered.",
            },
        ],
    }

    result = build_financial_document_evidence(
        ticker="MSFT",
        trade_date="2026-06-29",
        packet=packet,
        structured_output_path="runs/x/financial_report/section_records.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    records = result["section_records"]
    ledger = result["ledger_entries"]
    by_kind = {record["section_kind"]: record for record in records}

    assert by_kind["business_overview"]["evidence_id"] == "financial:MSFT:2026-06-29:001"
    assert by_kind["business_overview"]["status"] == "available"
    assert by_kind["business_overview"]["confidence"] == "medium"
    assert by_kind["business_overview"]["final_financial_judgment"] == "pending_codex_interpretation"
    assert by_kind["commitments_capex_contractual_obligations"]["status"] == "unavailable"
    assert by_kind["commitments_capex_contractual_obligations"]["evidence_gap"] == "Capex section was not identified."
    assert "section_unavailable" in by_kind["commitments_capex_contractual_obligations"]["limitations"]
    assert by_kind["8k_cover_page"]["section_name"] == "8-K cover page"
    assert by_kind["exhibit_99_1"]["section_name"] == "Exhibit 99.1"
    assert by_kind["sector_metric"]["source_type"] == "asx_announcement"
    assert by_kind["sector_metric"]["metric_value_status"] == "value_extracted"
    assert by_kind["sector_metric"]["association_score"] == 92
    assert by_kind["sector_metric"]["clean_metric_value"] == "82"
    assert by_kind["sector_metric"]["row_label"] == "EBIT margin"
    assert by_kind["investor_presentation"]["status"] == "unavailable"

    assert len(ledger) == len(records)
    assert ledger[0]["role"] == "financial_report_analyst"
    assert ledger[0]["tool_name"] == "financial_document_evidence"
    assert ledger[0]["structured_output_path"].endswith("section_records.json")
    assert ledger[1]["confidence"] == "low"
