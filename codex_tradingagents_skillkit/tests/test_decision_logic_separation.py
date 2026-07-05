from __future__ import annotations

import importlib.util
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
WRITER = BUNDLE / "scripts" / "write_codex_session_role_reports.py"
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_overweight_research_with_weak_timing_stays_hold():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Overweight",
        close=90.0,
        ema_10=95.0,
        sma_50=100.0,
        sma_200=110.0,
        rsi=40.0,
        macd=-0.5,
        atr=2.0,
        is_asx=True,
    )

    assert setup["action"] == "HOLD"
    assert "Rating and action differ" in setup["tension"]


def test_underweight_research_with_unconfirmed_sell_timing_stays_hold():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Underweight",
        close=102.0,
        ema_10=104.0,
        sma_50=105.0,
        sma_200=95.0,
        rsi=48.0,
        macd=0.1,
        atr=2.0,
        is_asx=False,
    )

    assert setup["action"] == "HOLD"
    assert "Rating and action differ" in setup["tension"]


def test_buy_requires_research_alignment_and_confirmed_setup():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Overweight",
        close=110.0,
        ema_10=105.0,
        sma_50=100.0,
        sma_200=95.0,
        rsi=60.0,
        macd=0.5,
        atr=2.0,
        is_asx=False,
    )

    assert setup["action"] == "BUY"
    assert setup["setup_score"] >= 4
    assert setup["buy_confirmation"] is True
    assert "BUY requires Research Manager Buy/Overweight" in setup["threshold_rule"]


def test_fixture_a_overweight_confirmed_setup_trader_buy():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Overweight",
        close=112.0,
        ema_10=108.0,
        sma_50=104.0,
        sma_200=99.0,
        rsi=62.0,
        macd=0.8,
        atr=2.0,
        is_asx=False,
    )

    assert setup["setup_score"] >= 4
    assert setup["buy_confirmation"] is True
    assert setup["trend"] > 0
    assert setup["momentum"] > 0
    assert setup["support_resistance"] > 0
    assert setup["action"] == "BUY"


def test_fixture_b_underweight_confirmed_downside_trader_sell():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Underweight",
        close=88.0,
        ema_10=93.0,
        sma_50=97.0,
        sma_200=103.0,
        rsi=33.0,
        macd=-0.9,
        atr=2.0,
        is_asx=False,
    )

    assert setup["setup_score"] <= -4
    assert setup["sell_confirmation"] is True
    assert setup["trend"] < 0
    assert setup["momentum"] < 0
    assert setup["support_resistance"] < 0
    assert setup["action"] == "SELL"


def test_positive_score_can_remain_hold_without_confirmation():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Overweight",
        close=110.0,
        ema_10=105.0,
        sma_50=100.0,
        sma_200=95.0,
        rsi=48.0,
        macd=0.1,
        atr=2.0,
        is_asx=False,
    )

    assert setup["setup_score"] >= 4
    assert setup["action"] == "HOLD"
    assert setup["buy_confirmation"] is False
    assert "lacks execution confirmation" in setup["hold_explanation"]


def test_fixture_c_overweight_high_score_missing_confirmation_trader_hold():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Overweight",
        close=110.0,
        ema_10=105.0,
        sma_50=100.0,
        sma_200=95.0,
        rsi=49.0,
        macd=0.0,
        atr=2.0,
        is_asx=False,
    )

    assert setup["setup_score"] >= 4
    assert setup["buy_confirmation"] is False
    assert setup["momentum"] == 0
    assert setup["action"] == "HOLD"


def test_fixture_d_underweight_weak_score_no_breakdown_trader_hold():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Underweight",
        close=102.0,
        ema_10=103.0,
        sma_50=104.0,
        sma_200=95.0,
        rsi=48.0,
        macd=0.1,
        atr=2.0,
        is_asx=False,
    )

    assert setup["setup_score"] > -4
    assert setup["sell_confirmation"] is False
    assert not (setup["trend"] < 0 and setup["momentum"] < 0 and setup["support_resistance"] < 0)
    assert setup["action"] == "HOLD"


def test_overweight_confirmed_buy_fixture_preserves_portfolio_rating():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    manager_rec = "Overweight"
    setup = writer._trader_setup_assessment(
        manager_rec=manager_rec,
        close=120.0,
        ema_10=110.0,
        sma_50=105.0,
        sma_200=100.0,
        rsi=64.0,
        macd=1.1,
        atr=2.0,
        is_asx=False,
    )
    portfolio_rating = manager_rec

    assert setup["action"] == "BUY"
    assert portfolio_rating == "Overweight"


def test_sell_requires_research_alignment_and_confirmed_breakdown():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    setup = writer._trader_setup_assessment(
        manager_rec="Underweight",
        close=90.0,
        ema_10=95.0,
        sma_50=100.0,
        sma_200=105.0,
        rsi=35.0,
        macd=-0.7,
        atr=2.0,
        is_asx=False,
    )

    assert setup["action"] == "SELL"
    assert setup["setup_score"] <= -4
    assert setup["sell_confirmation"] is True


def test_underweight_downside_fixture_supports_sell_or_timing_gated_hold():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    confirmed = writer._trader_setup_assessment(
        manager_rec="Underweight",
        close=88.0,
        ema_10=94.0,
        sma_50=98.0,
        sma_200=104.0,
        rsi=34.0,
        macd=-0.8,
        atr=2.0,
        is_asx=False,
    )
    unconfirmed = writer._trader_setup_assessment(
        manager_rec="Underweight",
        close=98.0,
        ema_10=100.0,
        sma_50=101.0,
        sma_200=92.0,
        rsi=49.0,
        macd=0.1,
        atr=2.0,
        is_asx=False,
    )

    assert confirmed["action"] == "SELL"
    assert unconfirmed["action"] == "HOLD"
    assert "Rating and action differ" in unconfirmed["tension"]


def test_research_manager_moving_average_primary_rating_fails(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    manager = tmp_path / "manager.md"
    manager.write_text(
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- market evidence\n\n"
        "## Primary Rating Driver\n\nPrimary rating driver: market_technical\n\n"
        "## Evidence Winner\n\nPrice is above 10 EMA, 50 SMA, and 200 SMA, therefore Overweight.\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Role | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |\n"
        "|---|---|---|---|---|---:|---|---|\n"
        "| Market Analyst | positive | high | medium | market snapshot | +2 | moving averages | market:T:2026-07-02:trend |\n\n"
        "## Rating-vs-Rating Reasoning\n\nOverweight beats Hold because of moving averages.\n",
        encoding="utf-8",
    )

    errors = validator._research_manager_quality_errors(manager)

    assert "research manager rating is basically a moving-average rule" in errors


def test_trader_moving_average_only_buy_fails(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    trader = tmp_path / "trader.md"
    trader.write_text(
        "# Trader\n\n"
        "## Tool Outputs Used\n\n- market evidence\n\n"
        "## Action Consistency Check\n\n**Action**: BUY\n\n"
        "Price is above 10 EMA, 50 SMA, and 200 SMA.\n\n"
        "## Setup Quality Assessment\n\nAbove 10 EMA, 50 SMA, and 200 SMA.\n\n"
        "## Paper-study price framework\n\nReference price 10, confirmation 11, invalidation 9.\n\n"
        "## FINAL TRANSACTION PROPOSAL\n\nFINAL TRANSACTION PROPOSAL: **BUY**\n",
        encoding="utf-8",
    )

    errors = validator._trader_quality_errors(trader)

    assert "trader setup quality omits required score components" in errors


def test_complete_report_hiding_rating_action_tension_fails(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    report_dir = tmp_path / "reports" / "CBA.AX" / "2026-07-02"
    report_dir.mkdir(parents=True)
    (report_dir / "complete_report.md").write_text(
        "# Complete Report\n\n"
        "Research Manager Rating: Overweight\n"
        "Trader Action: HOLD\n"
        "Portfolio Rating: Overweight\n\n"
        "### Research Manager Decision - Evidence Weighing\n"
        "**Recommendation**: Overweight\n\n"
        "### Trader\n"
        "**Action**: HOLD\n",
        encoding="utf-8",
    )

    errors = validator._rating_action_tension_errors(report_dir)

    assert "complete_report.md hides rating/action tension" in errors


def test_portfolio_risk_impact_requires_concrete_risk_and_opportunity(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    report_dir = tmp_path / "reports" / "AAPL" / "2026-07-02"
    portfolio_dir = report_dir / "5_portfolio"
    portfolio_dir.mkdir(parents=True)
    (portfolio_dir / "decision.md").write_text(
        "# Portfolio Manager Decision\n\n"
        "## Tool Outputs Used\n\n- risk debate\n\n"
        "## Risk debate impact\n"
        "The risk debate tempers implementation. Stronger risk side: balanced with a conservative sizing bias.\n\n"
        "## Final Portfolio Decision\n\n**Rating**: Hold\n",
        encoding="utf-8",
    )

    errors = validator._risk_portfolio_quality_errors(report_dir)

    assert "Portfolio Manager does not name the strongest concrete opportunity" in errors
    assert "Portfolio Manager does not name the strongest concrete risk" in errors


def test_sector_metric_availability_is_not_automatically_supportive():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    neutral = {
        "metric_name": "realised_price",
        "metric_label": "Realised price",
        "status": "available",
        "excerpt": "average realised prices for major assets including copper and iron ore",
    }
    adverse = {
        "metric_name": "ebit_margin",
        "metric_label": "EBIT margin",
        "status": "available",
        "excerpt": "EBIT margin decreasing by a normalised 82 bps to 5.4%.",
    }

    assert writer._asx_metric_direction(neutral) == "neutral"
    assert writer._asx_metric_direction(adverse) == "adverse"


def test_sector_metric_direction_audit_records_extracted_basis():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    records = [
        {
            "section_kind": "sector_metric",
            "metric_name": "ebit_margin",
            "metric_label": "EBIT margin",
            "status": "available",
            "confidence": "medium",
            "evidence_id": "financial:WOW.AX:2026-07-02:017",
            "excerpt": "EBIT margin decreasing by a normalised 82 bps to 5.4%.",
        }
    ]

    audit = writer._asx_metric_audit_records(records)

    assert audit[0]["metric_name"] == "ebit_margin"
    assert audit[0]["clean_metric_value"] == "82"
    assert audit[0]["value_unit"] == "bps"
    assert audit[0]["metric_value_status"] == "value_extracted"
    assert int(audit[0]["association_score"]) >= 80
    assert "unit bps compatible" in audit[0]["association_reason"]
    assert audit[0]["supporting_sentence"] == "EBIT margin decreasing by a normalised 82 bps to 5.4%."
    assert audit[0]["direction"] == "adverse"
    assert audit[0]["confidence"] == "medium"
    assert audit[0]["evidence_id"] == "financial:WOW.AX:2026-07-02:017"
    assert audit[0]["table_title"] == "unavailable"


def test_navigation_sector_metric_is_context_only_low_confidence():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    records = [
        {
            "section_kind": "sector_metric",
            "metric_name": "reserves_resources",
            "metric_label": "Reserves/resources",
            "status": "available",
            "confidence": "medium",
            "evidence_id": "financial:BHP.AX:2026-07-02:030",
            "excerpt": (
                "Home Search Contact us All investor resources Reports and presentations "
                "Frequently Asked Questions Key contacts Downloads resources"
            ),
        }
    ]

    audit = writer._asx_metric_audit_records(records)

    assert audit[0]["direction"] == "context_only"
    assert audit[0]["confidence"] == "low"
    assert "navigation/page-list" in audit[0]["confidence_reason"]
    assert audit[0]["metric_value_status"] == "context_only"
    assert audit[0]["clean_metric_value"] == "unavailable"


def test_metric_audit_rejects_low_association_clean_values():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    record = {
        "section_kind": "sector_metric",
        "metric_name": "net_interest_margin",
        "metric_label": "NIM",
        "status": "available",
        "confidence": "medium",
        "evidence_id": "financial:CBA.AX:2026-07-02:010",
        "excerpt": "NIM commentary was stable. Operating income increased 5% on FY24.",
        "clean_metric_value": "5",
        "value_unit": "%",
        "association_score": 42,
        "metric_value_status": "direction_extracted",
    }

    audit = writer._asx_metric_audit_records([record])

    assert audit[0]["clean_metric_value"] == "unavailable"
    assert audit[0]["metric_value_status"] == "direction_extracted"
    assert audit[0]["association_score"] == "42"


def test_metric_mentioned_only_is_not_counted_as_supportive_direction():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    record = {
        "section_kind": "sector_metric",
        "metric_name": "cet1",
        "metric_label": "CET1",
        "status": "available",
        "direction": "supportive",
        "metric_value_status": "metric_mentioned_only",
        "excerpt": "CET1 commentary without a clean value.",
    }

    assert writer._asx_metric_direction(record) == "neutral"


def test_metric_audit_summary_excludes_low_confidence_weak_associations():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    records = [
        {
            "section_kind": "sector_metric",
            "metric_name": "dividends",
            "metric_label": "Dividends",
            "status": "available",
            "confidence": "low",
            "evidence_id": "financial:WOW.AX:2026-07-02:010",
            "excerpt": "Dividend 1 cents footnote marker.",
            "clean_metric_value": "1",
            "value_unit": "cents",
            "association_score": 35,
            "metric_value_status": "context_only",
        },
        {
            "section_kind": "sector_metric",
            "metric_name": "ebit_margin",
            "metric_label": "EBIT margin",
            "status": "available",
            "confidence": "medium",
            "evidence_id": "financial:WOW.AX:2026-07-02:011",
            "excerpt": "EBIT margin decreasing by a normalised 82 bps to 5.4%.",
            "clean_metric_value": "82",
            "value_unit": "bps",
            "association_score": 92,
            "metric_value_status": "value_extracted",
        },
    ]

    summary = writer._asx_metric_audit_summary(records, "Hold")

    assert "ebit_margin adverse (82 bps; value_extracted; association_score 92" in summary
    assert "Dividend 1 cents" not in summary
    assert "dividends" not in summary


def test_quality_validator_requires_metric_association_audit_fields(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text('{"ticker": "WOW.AX"}', encoding="utf-8")
    report_dir = tmp_path / "reports" / "WOW.AX" / "2026-07-02"
    manager_path = report_dir / "2_research" / "manager.md"
    manager_path.parent.mkdir(parents=True)
    manager_path.write_text(
        """## Tool Outputs Used
## Primary Rating Driver
## Evidence Winner
## Structured Evidence Matrix
## Role Evidence Weighting
## Rating-vs-Rating Reasoning
10 EMA 95, 50 SMA 90, 200 SMA 80. Sector metric EBIT margin adverse financial:WOW.AX:2026-07-02:011.
## Debate Outcome Scorecard
## Market Technicals as Confidence / Timing Modifier
## Sector Metric Direction Audit
| metric_name | clean_metric_value | evidence_id |
|---|---|---|
| ebit_margin | 82 | financial:WOW.AX:2026-07-02:011 |
""",
        encoding="utf-8",
    )

    errors = validator._asx_research_specificity_errors(manager_path, evidence_path)

    assert "ASX Research Manager report lacks auditable sector metric direction records" in errors


def test_quality_validator_rejects_clean_value_below_association_threshold(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text('{"ticker": "CBA.AX"}', encoding="utf-8")
    report_dir = tmp_path / "reports" / "CBA.AX" / "2026-07-02"
    manager_path = report_dir / "2_research" / "manager.md"
    manager_path.parent.mkdir(parents=True)
    manager_path.write_text(
        """## Tool Outputs Used
## Primary Rating Driver
## Evidence Winner
## Structured Evidence Matrix
## Role Evidence Weighting
## Rating-vs-Rating Reasoning
10 EMA 105, 50 SMA 110, 200 SMA 120. Sector metric NIM adverse financial:CBA.AX:2026-07-02:011.
## Debate Outcome Scorecard
## Market Technicals as Confidence / Timing Modifier
## Sector Metric Direction Audit
| metric_name | extracted_value_or_phrase | clean_metric_value | value_unit | value_context | metric_value_status | association_score | association_reason | period_reference | comparison_reference | supporting_sentence | comparison_basis | direction | confidence | confidence_reason | evidence_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| net_interest_margin | NIM commentary. Operating income increased 5%. | 5 | % | operating income | direction_extracted | 42 | competing operating income label closer | not specified | not specified | NIM commentary. Operating income increased 5%. | metric mentioned without explicit comparative baseline | neutral | medium | source confidence medium | financial:CBA.AX:2026-07-02:011 |
""",
        encoding="utf-8",
    )

    errors = validator._asx_research_specificity_errors(manager_path, evidence_path)

    assert "ASX metric audit populates clean_metric_value below accepted association threshold" in errors


def test_quality_validator_rejects_dense_high_score_without_row_mapping(tmp_path: Path):
    validator = _load_module(QUALITY_VALIDATOR, "validate_quality_review")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text('{"ticker": "WOW.AX"}', encoding="utf-8")
    report_dir = tmp_path / "reports" / "WOW.AX" / "2026-07-02"
    manager_path = report_dir / "2_research" / "manager.md"
    manager_path.parent.mkdir(parents=True)
    dense_sentence = (
        "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201) "
        "Net investment in inventory increased by 44 $m compared with FY24."
    )
    manager_path.write_text(
        f"""## Tool Outputs Used
## Primary Rating Driver
## Evidence Winner
## Structured Evidence Matrix
## Role Evidence Weighting
## Rating-vs-Rating Reasoning
10 EMA 95, 50 SMA 90, 200 SMA 80. Sector metric inventory adverse financial:WOW.AX:2026-07-02:011.
## Debate Outcome Scorecard
## Market Technicals as Confidence / Timing Modifier
## Sector Metric Direction Audit
| metric_name | extracted_value_or_phrase | clean_metric_value | value_unit | value_context | metric_value_status | association_score | association_reason | period_reference | comparison_reference | supporting_sentence | comparison_basis | direction | confidence | confidence_reason | evidence_id | table_title | row_label | column_label | source_page |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| inventory | {dense_sentence} | 44 | $m | inventory near 44 $m | value_extracted | 95 | label-value distance 3 tokens; unit $m compatible | FY2025 | FY2024 | {dense_sentence} | period-over-period wording in extracted filing/report phrase | adverse | medium | clean value accepted | financial:WOW.AX:2026-07-02:011 | unavailable | unavailable | unavailable | unavailable |
""",
        encoding="utf-8",
    )

    errors = validator._asx_research_specificity_errors(manager_path, evidence_path)

    assert "ASX metric audit has high association score on dense numeric text without row/column mapping" in errors


def test_metric_clean_value_unavailable_when_numbers_are_unlabelled():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    record = {
        "section_kind": "sector_metric",
        "metric_name": "production",
        "metric_label": "Production",
        "status": "available",
        "excerpt": "production, including highest copper production in 17 years and record Q4 production.",
    }

    value_parts = writer._metric_value_parts(record)

    assert value_parts["clean_metric_value"] == "unavailable"
    assert value_parts["value_unit"] == "unavailable"
    assert value_parts["value_context"] == "no high-confidence metric-value association"


def test_metric_clean_value_keeps_labelled_value_context():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    record = {
        "section_kind": "sector_metric",
        "metric_name": "unit_cost_aisc",
        "metric_label": "Unit cost",
        "status": "available",
        "excerpt": "Across the group, unit costs at our major assets were down 4.7 per cent year-on-year.",
    }

    value_parts = writer._metric_value_parts(record)

    assert value_parts["clean_metric_value"] == "4.7"
    assert value_parts["value_unit"] == "per cent"
    assert "unit cost" in value_parts["value_context"].lower()
    assert value_parts["metric_value_status"] == "value_extracted"


def test_unsupported_commodity_exposure_is_not_supportive():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    record = {
        "section_kind": "sector_metric",
        "metric_name": "commodity_exposure",
        "metric_label": "Commodity exposure",
        "status": "available",
        "excerpt": "Copper Iron ore Potash Reports Presentations Shareholder services",
    }

    assert writer._asx_metric_direction(record) == "context_only"


def test_metric_audit_summary_uses_top_directional_rows():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    records = [
        {
            "section_kind": "sector_metric",
            "metric_name": "unit_cost_aisc",
            "metric_label": "Unit cost",
            "status": "available",
            "confidence": "medium",
            "evidence_id": "financial:BHP.AX:2026-07-02:018",
            "excerpt": "unit cost reduction and WAIO remains the lowest-cost major iron ore producer in the world.",
        },
        {
            "section_kind": "sector_metric",
            "metric_name": "capex",
            "metric_label": "Capex",
            "status": "unavailable",
            "confidence": "low",
            "evidence_id": "financial:BHP.AX:2026-07-02:019",
            "unavailable_reason": "not found",
        },
    ]

    summary = writer._asx_metric_audit_summary(records, "Overweight")

    assert "unit_cost_aisc supportive" in summary
    assert "financial:BHP.AX:2026-07-02:018" in summary


def test_execution_caution_wording_is_market_specific():
    writer = _load_module(WRITER, "write_codex_session_role_reports")

    assert "ASX-specific" in writer._market_execution_caution(is_asx=True)
    assert "Generic execution/liquidity caution" in writer._market_execution_caution(is_asx=False)
    assert "ASX-specific" not in writer._market_execution_caution(is_asx=False)


def test_research_rating_uses_metric_direction_not_availability():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    refs = {
        "close": "market:T:2026-07-02:001",
        "ema10": "market:T:2026-07-02:002",
        "sma50": "market:T:2026-07-02:003",
        "sma200": "market:T:2026-07-02:004",
        "exhibit": "financial:T:2026-07-02:001",
    }
    records = [
        {
            "section_kind": "sector_metric",
            "metric_name": "sales_growth",
            "metric_label": "Sales growth",
            "sector": "retailers",
            "status": "available",
            "evidence_id": "financial:T:2026-07-02:010",
            "excerpt": "comparable sales definitions and adjustments",
        },
        {
            "section_kind": "sector_metric",
            "metric_name": "ebit_margin",
            "metric_label": "EBIT margin",
            "sector": "retailers",
            "status": "available",
            "evidence_id": "financial:T:2026-07-02:011",
            "excerpt": "EBIT margin decreasing by a normalised 82 bps to 5.4%.",
        },
        {
            "section_kind": "management_discussion_analysis",
            "section_name": "management_discussion_analysis",
            "status": "available",
        },
        {"section_kind": "cash_flow_statement", "section_name": "cash_flow_statement", "status": "available"},
    ]

    reasoning = writer._asx_research_reasoning(
        ticker="WOW.AX",
        close=100.0,
        ema_10=95.0,
        sma_50=90.0,
        sma_200=80.0,
        rel_10="above",
        rel_50="above",
        rel_200="above",
        financial_records=records,
        refs=refs,
        best_news_id="news:T:2026-07-02:001",
        first_social_id="social:T:2026-07-02:001",
    )

    assert reasoning["manager_rec"] == "Hold"
    assert "not strong enough for a directional rating" in reasoning["evidence_winner"]


def test_adverse_sector_metrics_can_drive_underweight_research():
    writer = _load_module(WRITER, "write_codex_session_role_reports")
    refs = {
        "close": "market:T:2026-07-02:001",
        "ema10": "market:T:2026-07-02:002",
        "sma50": "market:T:2026-07-02:003",
        "sma200": "market:T:2026-07-02:004",
        "exhibit": "financial:T:2026-07-02:001",
    }
    records = [
        {
            "section_kind": "sector_metric",
            "metric_name": "arrears",
            "metric_label": "Arrears",
            "sector": "banks",
            "status": "available",
            "evidence_id": "financial:T:2026-07-02:020",
            "excerpt": "home loan and personal loan arrears increased",
        },
        {
            "section_kind": "sector_metric",
            "metric_name": "impairment",
            "metric_label": "Impairment",
            "sector": "banks",
            "status": "available",
            "evidence_id": "financial:T:2026-07-02:021",
            "excerpt": "impairment provisions increased against credit risk weighted assets",
        },
        {
            "section_kind": "management_discussion_analysis",
            "section_name": "management_discussion_analysis",
            "status": "available",
        },
        {"section_kind": "cash_flow_statement", "section_name": "cash_flow_statement", "status": "available"},
    ]

    reasoning = writer._asx_research_reasoning(
        ticker="CBA.AX",
        close=100.0,
        ema_10=105.0,
        sma_50=110.0,
        sma_200=120.0,
        rel_10="below",
        rel_50="below",
        rel_200="below",
        financial_records=records,
        refs=refs,
        best_news_id="news:T:2026-07-02:001",
        first_social_id="social:T:2026-07-02:001",
    )

    assert reasoning["manager_rec"] == "Underweight"
    assert reasoning["primary_driver"] == "sector_metric"
