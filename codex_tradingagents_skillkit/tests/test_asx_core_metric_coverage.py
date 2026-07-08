import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
COVERAGE = BUNDLE / "scripts" / "core_metric_coverage.py"
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_coverage():
    spec = importlib.util.spec_from_file_location("core_metric_coverage", COVERAGE)
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


def _clean_metric(sector: str, metric_name: str, value: str = "1.0") -> dict[str, object]:
    return {
        "section_kind": "sector_metric",
        "sector": sector,
        "metric_name": metric_name,
        "source_quality_tier": "tier_1_asx_lodged_pdf",
        "document_role": "annual_report",
        "status": "available",
        "clean_metric_value": value,
        "metric_value_status": "value_extracted",
        "association_score": 92,
        "association_reason": "label and value are directly attached",
        "table_mapping_confidence": 0,
        "direction": "neutral",
        "confidence": "medium",
        "evidence_id": f"financial:TEST:2026-07-02:{metric_name}",
        "supporting_sentence": f"{metric_name} {value}",
    }


def _narrative_metric(sector: str, metric_name: str, status: str) -> dict[str, object]:
    return {
        "section_kind": "sector_metric",
        "sector": sector,
        "metric_name": metric_name,
        "source_quality_tier": "tier_1_asx_lodged_pdf",
        "document_role": "annual_report",
        "status": "available",
        "clean_metric_value": "unavailable",
        "metric_value_status": status,
        "association_score": 90,
        "association_reason": "eligible financial report section contains a supported narrative metric",
        "table_mapping_confidence": 0,
        "direction": "neutral",
        "confidence": "medium",
        "evidence_id": f"financial:TEST:2026-07-02:{metric_name}",
        "supporting_sentence": f"{metric_name} narrative is supported by source section proof.",
        "section_title": "operating_and_financial_review",
        "source_page": "12",
    }


def _unavailable_metric(sector: str, metric_name: str) -> dict[str, object]:
    return {
        "section_kind": "sector_metric",
        "sector": sector,
        "metric_name": metric_name,
        "source_quality_tier": "tier_1_asx_lodged_pdf",
        "document_role": "annual_report",
        "status": "unavailable",
        "clean_metric_value": "unavailable",
        "metric_value_status": "unavailable",
        "association_score": 0,
        "direction": "unavailable",
        "confidence": "low",
        "evidence_id": f"financial:TEST:2026-07-02:{metric_name}",
        "unavailable_reason": "Reviewed source documents do not disclose this metric before the trade date.",
        "evidence_gap": "Metric absent from extracted source documents.",
    }


def _weak_gap_metric(sector: str, metric_name: str, status: str = "metric_mentioned_only") -> dict[str, object]:
    return {
        "section_kind": "sector_metric",
        "sector": sector,
        "metric_name": metric_name,
        "source_quality_tier": "tier_1_asx_lodged_pdf",
        "document_role": "annual_report",
        "status": "available",
        "clean_metric_value": "unavailable",
        "metric_value_status": status,
        "association_score": 35,
        "direction": "neutral",
        "confidence": "low",
        "evidence_id": f"financial:TEST:2026-07-02:{metric_name}",
        "supporting_sentence": f"{metric_name} was mentioned without a safely attached value.",
        "evidence_gap": "Source mentions the metric, but no high-confidence clean value was attached.",
        "confidence_reason": "clean value withheld because association score is below accepted threshold",
    }


def test_bhp_core_metrics_fail_when_mostly_unresolved():
    module = _load_coverage()
    records = [
        {**_clean_metric("miners", "production"), "metric_value_status": "table_row_unparsed", "clean_metric_value": "unavailable"},
        {**_clean_metric("miners", "realised_price"), "metric_value_status": "metric_mentioned_only", "clean_metric_value": "unavailable"},
        {**_clean_metric("miners", "unit_cost_aisc"), "metric_value_status": "direction_extracted", "clean_metric_value": "unavailable"},
        _unavailable_metric("miners", "capex"),
        {**_clean_metric("miners", "commodity_exposure"), "metric_value_status": "context_only", "clean_metric_value": "unavailable"},
        {**_unavailable_metric("miners", "reserves_resources"), "unavailable_reason": "", "evidence_gap": ""},
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="BHP.AX")

    assert status["core_metric_coverage_passed"] is False
    assert set(status["core_metrics_unresolved"]) >= {
        "production",
        "realised_price",
        "unit_cost_aisc",
        "commodity_exposure",
        "reserves_resources",
    }
    assert status["core_metrics_unavailable_with_reason"] == ["capex"]


def test_cba_materiality_passes_with_major_warnings_when_credit_quality_uses_impairment():
    module = _load_coverage()
    records = [
        _clean_metric("banks", "net_interest_margin"),
        _clean_metric("banks", "cet1"),
        _clean_metric("banks", "loan_growth"),
        _weak_gap_metric("banks", "arrears"),
        _clean_metric("banks", "impairment"),
        _weak_gap_metric("banks", "roe"),
        _clean_metric("banks", "dividend"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="CBA.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert status["critical_metrics_required"] == ["net_interest_margin", "cet1", "credit_quality_group"]
    assert status["critical_metrics_clean"] == ["net_interest_margin", "cet1", "credit_quality_group"]
    assert status["critical_metrics_unresolved"] == []
    assert {"arrears", "roe"}.issubset(set(status["important_metrics_unresolved"]))
    assert any("arrears not cleanly extracted" in warning for warning in status["major_warnings"])
    assert any("ROE not cleanly extracted" in warning for warning in status["major_warnings"])
    assert any("credit quality assessment relies on impairment" in warning for warning in status["major_warnings"])


def test_cba_materiality_requires_one_clean_credit_quality_metric():
    module = _load_coverage()
    records = [
        _clean_metric("banks", "net_interest_margin"),
        _clean_metric("banks", "cet1"),
        _clean_metric("banks", "loan_growth"),
        _weak_gap_metric("banks", "arrears"),
        _weak_gap_metric("banks", "impairment"),
        _clean_metric("banks", "roe"),
        _clean_metric("banks", "dividend"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="CBA.AX")

    assert status["core_metric_coverage_passed"] is False
    assert status["materiality_status"] == "remediation_required"
    assert status["critical_metrics_unresolved"] == ["credit_quality_group"]
    assert any("credit_quality_group" in reason for reason in status["remediation_required_reasons"])
    assert set(status["core_metrics_unresolved"]) >= {"arrears", "impairment"}


def test_core_metric_clean_value_from_landing_page_tier_fails_coverage():
    module = _load_coverage()
    records = [
        {
            **_clean_metric("banks", "net_interest_margin", "2.05"),
            "source_quality_tier": "tier_4_company_ir_landing_page",
            "document_role": "landing_page",
        },
        _clean_metric("banks", "cet1", "12.3"),
        _clean_metric("banks", "loan_growth"),
        _unavailable_metric("banks", "arrears"),
        _unavailable_metric("banks", "impairment"),
        _clean_metric("banks", "roe"),
        _clean_metric("banks", "dividend"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="CBA.AX")

    assert status["core_metric_coverage_passed"] is False
    assert "net_interest_margin" in status["core_metrics_unresolved"]
    assert status["core_metric_coverage_details"]["net_interest_margin"]["reason"] == (
        "clean value is not from an eligible ASX financial document source tier"
    )


def test_asx_core_metric_coverage_fails_when_no_sector_metric_records_exist():
    module = _load_coverage()

    status = module.evaluate_core_metric_coverage(
        [
            {
                "section_kind": "source_coverage",
                "ticker": "CBA.AX",
                "source_quality_tier": "tier_4_company_ir_landing_page",
                "document_role": "landing_page",
                "metric_eligibility": "discovery_only",
            }
        ],
        ticker="CBA.AX",
    )

    assert status["sector"] == "banks"
    assert status["core_metric_coverage_passed"] is False
    assert {"net_interest_margin", "cet1", "loan_growth"}.issubset(
        set(status["core_metrics_unresolved"])
    )


def test_cba_nim_and_cet1_mentioned_only_fail_core_coverage():
    module = _load_coverage()
    records = [
        {**_clean_metric("banks", "net_interest_margin"), "metric_value_status": "metric_mentioned_only", "clean_metric_value": "unavailable"},
        {**_clean_metric("banks", "cet1"), "metric_value_status": "metric_mentioned_only", "clean_metric_value": "unavailable"},
        _clean_metric("banks", "loan_growth"),
        _unavailable_metric("banks", "arrears"),
        _unavailable_metric("banks", "impairment"),
        _clean_metric("banks", "roe"),
        _clean_metric("banks", "dividend"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="CBA.AX")

    assert status["core_metric_coverage_passed"] is False
    assert {"net_interest_margin", "cet1"}.issubset(set(status["core_metrics_unresolved"]))


def test_mpl_passes_when_claims_ratio_clean_and_other_core_metrics_clean_or_unavailable():
    module = _load_coverage()
    records = [
        _unavailable_metric("health_insurers", "premium_growth"),
        _clean_metric("health_insurers", "claims_ratio", "3.3%"),
        _unavailable_metric("health_insurers", "membership"),
        _clean_metric("health_insurers", "capital_adequacy", "$250m"),
        _unavailable_metric("health_insurers", "operating_profit_or_margin"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="MPL.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["core_metrics_cleanly_extracted"] == ["claims_ratio", "capital_adequacy"]
    assert status["core_metrics_unresolved"] == []


def test_wow_materiality_passes_with_major_warnings_when_important_metrics_are_unresolved():
    module = _load_coverage()
    records = [
        _clean_metric("retailers", "sales_growth"),
        _clean_metric("retailers", "ebit_margin", "82 bps"),
        {**_clean_metric("retailers", "inventory"), "metric_value_status": "table_row_unparsed", "clean_metric_value": "unavailable"},
        _unavailable_metric("retailers", "capex"),
        _clean_metric("retailers", "dividends"),
        _unavailable_metric("retailers", "comparable_sales"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="WOW.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert status["critical_metrics_clean"] == ["sales_growth", "ebit_margin"]
    assert "inventory_or_working_capital" in status["core_metrics_unresolved"]
    assert "inventory_or_working_capital" in status["important_metrics_unresolved"]
    assert "ebit_margin" in status["core_metrics_cleanly_extracted"]


def test_dense_table_clean_value_without_row_column_does_not_pass_core_coverage():
    module = _load_coverage()
    records = [
        {
            **_clean_metric("retailers", "inventory"),
            "clean_metric_value": "44",
            "metric_value_status": "value_extracted",
            "association_score": 100,
            "table_mapping_confidence": 0,
            "row_label": "",
            "column_label": "",
            "supporting_sentence": "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201) Net investment in inventory 44 31 13",
        },
        _clean_metric("retailers", "sales_growth"),
        _clean_metric("retailers", "ebit_margin"),
        _unavailable_metric("retailers", "capex"),
        _clean_metric("retailers", "dividends"),
        _unavailable_metric("retailers", "comparable_sales"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="WOW.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert "inventory_or_working_capital" in status["core_metrics_unresolved"]


def test_wow_inventory_movement_subtype_can_satisfy_working_capital_metric():
    module = _load_coverage()
    records = [
        _clean_metric("retailers", "sales_growth"),
        _clean_metric("retailers", "ebit_margin"),
        {
            **_clean_metric("retailers", "inventory", "44"),
            "metric_subtype": "inventory_or_working_capital_movement",
            "row_label": "Net investment in inventory",
            "column_label": "Variance $m",
            "cell_value": "44",
            "table_mapping_confidence": 90,
        },
        _clean_metric("retailers", "capex"),
        _unavailable_metric("retailers", "dividends"),
        _unavailable_metric("retailers", "comparable_sales"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="WOW.AX")

    assert status["core_metric_coverage_passed"] is True
    assert "inventory_or_working_capital" in status["important_metrics_clean"]
    assert "inventory_or_working_capital" not in status["important_metrics_unresolved"]


def test_wow_dividend_change_subtype_does_not_satisfy_dividend_amount_metric():
    module = _load_coverage()
    records = [
        _clean_metric("retailers", "sales_growth"),
        _clean_metric("retailers", "ebit_margin"),
        _clean_metric("retailers", "inventory", "4169"),
        _clean_metric("retailers", "capex"),
        {
            **_clean_metric("retailers", "dividends", "5"),
            "metric_subtype": "dividend_change_percent",
            "value_unit": "%",
        },
        _unavailable_metric("retailers", "comparable_sales"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="WOW.AX")

    assert status["core_metric_coverage_passed"] is True
    assert "dividends" in status["supporting_metrics_unresolved"]
    assert status["core_metric_coverage_details"]["dividends"]["reason"] == (
        "clean value subtype is not valid for this metric profile"
    )


def test_bhp_commodity_exposure_portfolio_mix_narrative_satisfies_critical_without_numeric_value():
    module = _load_coverage()
    records = [
        _clean_metric("miners", "production"),
        _clean_metric("miners", "realised_price"),
        _clean_metric("miners", "unit_cost_aisc"),
        _clean_metric("miners", "capex"),
        {
            **_narrative_metric("miners", "commodity_exposure", "portfolio_mix_narrative"),
            "commodity_names": ["iron ore", "copper", "steelmaking coal", "potash"],
        },
        _unavailable_metric("miners", "reserves_resources"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="BHP.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert "commodity_exposure" in status["critical_metrics_clean"]
    assert "reserves_resources" in status["important_metrics_unresolved"]


def test_bhp_commodity_exposure_minimal_portfolio_mix_fixture_satisfies_critical():
    module = _load_coverage()
    records = [
        _clean_metric("miners", "production"),
        _clean_metric("miners", "realised_price"),
        _clean_metric("miners", "unit_cost_aisc"),
        _clean_metric("miners", "capex"),
        {
            "metric_name": "commodity_exposure",
            "metric_value_status": "portfolio_mix_narrative",
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "metric_eligibility": "eligible_financial_document",
            "supporting_sentence": "BHP portfolio includes copper, iron ore, steelmaking coal and potash.",
            "source_page": "3",
        },
        _unavailable_metric("miners", "reserves_resources"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="BHP.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert "commodity_exposure" in status["critical_metrics_clean"]
    assert "commodity_exposure" not in status["critical_metrics_unresolved"]


def test_bhp_missing_realised_price_still_blocks_miner_materiality():
    module = _load_coverage()
    records = [
        _clean_metric("miners", "production"),
        _weak_gap_metric("miners", "realised_price"),
        _clean_metric("miners", "unit_cost_aisc"),
        _clean_metric("miners", "capex"),
        _narrative_metric("miners", "commodity_exposure", "portfolio_mix_narrative"),
        _unavailable_metric("miners", "reserves_resources"),
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="BHP.AX")

    assert status["core_metric_coverage_passed"] is False
    assert status["materiality_status"] == "remediation_required"
    assert "realised_price" in status["critical_metrics_unresolved"]


def test_csl_structured_online_annual_report_tier_is_eligible_for_critical_healthcare_metrics():
    module = _load_coverage()
    records = [
        {**_clean_metric("healthcare", "segment_revenue"), "source_quality_tier": "tier_3_structured_online_annual_report"},
        {**_clean_metric("healthcare", "margins"), "source_quality_tier": "tier_3_structured_online_annual_report"},
        {
            **_narrative_metric("healthcare", "guidance", "guidance_narrative"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
        },
        {**_clean_metric("healthcare", "debt"), "source_quality_tier": "tier_3_structured_online_annual_report"},
        {
            **_clean_metric("healthcare", "plasma_collections"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
        },
        {**_weak_gap_metric("healthcare", "r_and_d"), "source_quality_tier": "tier_3_structured_online_annual_report"},
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="CSL.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert status["critical_metrics_unresolved"] == []
    assert "debt_or_balance_sheet" in status["critical_metrics_clean"]
    assert "plasma_collections_or_collection_network" in status["critical_metrics_clean"]
    assert "r_and_d" in status["important_metrics_unresolved"]


def test_csl_segment_growth_profitability_guidance_and_plasma_narratives_satisfy_critical_groups():
    module = _load_coverage()
    records = [
        {
            **_clean_metric("healthcare", "segment_revenue", "8"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
            "metric_value_status": "segment_growth",
            "value_unit": "%",
            "segment_name": "CSL Seqirus",
            "section_title": "CSL Seqirus",
        },
        {
            **_clean_metric("healthcare", "margins", "14"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
            "metric_value_status": "profitability_metric",
            "row_label": "NPATA",
            "value_unit": "%",
        },
        {
            **_narrative_metric("healthcare", "guidance", "guidance_narrative"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
            "section_title": "Outlook",
        },
        {
            **_clean_metric("healthcare", "borrowings", "5200"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
            "row_label": "Net debt",
            "value_unit": "US$m",
        },
        {
            **_narrative_metric("healthcare", "plasma_collections", "plasma_network_narrative"),
            "source_quality_tier": "tier_3_structured_online_annual_report",
            "section_title": "CSL Plasma",
            "supporting_sentence": "CSL Plasma expanded its plasma collection network and donor centres.",
        },
        {**_weak_gap_metric("healthcare", "r_and_d"), "source_quality_tier": "tier_3_structured_online_annual_report"},
    ]

    status = module.evaluate_core_metric_coverage(records, ticker="CSL.AX")

    assert status["core_metric_coverage_passed"] is True
    assert status["materiality_status"] == "review_ready_with_major_warnings"
    assert status["critical_metrics_unresolved"] == []
    assert "segment_revenue_or_growth" in status["critical_metrics_clean"]
    assert "margins" in status["critical_metrics_clean"]
    assert "guidance" in status["critical_metrics_clean"]
    assert "debt_or_balance_sheet" in status["critical_metrics_clean"]
    assert "plasma_collections_or_collection_network" in status["critical_metrics_clean"]
    assert any("guidance" in warning for warning in status["major_warnings"])
    assert any("plasma" in warning for warning in status["major_warnings"])


def test_quality_gate_passed_fails_when_core_metric_coverage_fails(tmp_path: Path):
    validator = _load_quality_validator()
    run_dir = tmp_path / "run"
    evidence_dir = run_dir / "evidence" / "CBA.AX" / "2026-07-02"
    financial_dir = evidence_dir / "financial_report"
    report_dir = run_dir / "reports" / "CBA.AX" / "2026-07-02"
    quality_dir = report_dir / "6_quality"
    financial_dir.mkdir(parents=True)
    quality_dir.mkdir(parents=True)
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "CBA.AX", "trade_date": "2026-07-02"}), encoding="utf-8")
    records = [
        {**_clean_metric("banks", "net_interest_margin"), "metric_value_status": "metric_mentioned_only", "clean_metric_value": "unavailable"},
        {**_clean_metric("banks", "cet1"), "metric_value_status": "metric_mentioned_only", "clean_metric_value": "unavailable"},
        _clean_metric("banks", "loan_growth"),
        _unavailable_metric("banks", "arrears"),
        _unavailable_metric("banks", "impairment"),
        _clean_metric("banks", "roe"),
        _clean_metric("banks", "dividend"),
    ]
    (financial_dir / "section_records.json").write_text(json.dumps(records), encoding="utf-8")
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
    (quality_dir / "evidence_reasoning_audit.json").write_text(
        json.dumps({"summary_verdict": "pass", "critical_findings": [], "warnings": []}),
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir, evidence_path)

    assert "ASX core metric coverage failed; review-ready quality gate cannot pass" in errors
    assert "quality_gate.json passes despite quality errors" in errors
