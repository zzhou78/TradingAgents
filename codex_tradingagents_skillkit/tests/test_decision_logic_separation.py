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
