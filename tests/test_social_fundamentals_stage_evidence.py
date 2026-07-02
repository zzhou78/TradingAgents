from __future__ import annotations

from codex_tradingagents_skillkit.scripts.fundamentals_evidence import build_fundamentals_evidence
from codex_tradingagents_skillkit.scripts.social_evidence import build_social_evidence
from codex_tradingagents_skillkit.scripts.stage_input_evidence import build_stage_input_evidence


def test_build_social_evidence_filters_noisy_retail_feed_and_lowers_confidence():
    result = build_social_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        tool_calls={
            "fetch_stocktwits_messages": {
                "status": "ok",
                "output": "$AAPL Bullish services strength\n$TSLA joke post\nmarket breadth weak\nspam",
            },
            "fetch_reddit_posts": {"status": "error", "error": "429 rate limited"},
        },
        structured_output_path="runs/x/social/social_summary.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    assert result["social_summary"]["total_items_reviewed"] == 4
    assert result["social_summary"]["usable_items"] == 1
    assert result["sources"][0]["usable_ticker_relevant_items"] == 1
    assert result["sources"][0]["confidence"] == "low"
    assert "reddit_rate_limited" in result["sources"][1]["limitations"]
    assert "no_usable_ticker_relevant_items" in result["sources"][1]["limitations"]
    assert result["ledger_entries"][0]["role"] == "sentiment_analyst"
    assert result["social_cards"][0]["ticker_relevance"] == "direct_company"
    assert result["social_cards"][0]["reasoning_quality"] == "medium"
    assert result["social_cards"][1]["ticker_relevance"] == "cross_ticker"
    assert result["social_cards"][1]["meme_or_joke"] is True
    assert result["social_cards"][1]["influence_weight"] < result["social_cards"][0]["influence_weight"]


def test_build_social_evidence_deduplicates_and_limits_platform_label_confidence():
    result = build_social_evidence(
        ticker="MSFT",
        trade_date="2026-06-30",
        tool_calls={
            "fetch_stocktwits_messages": {
                "status": "ok",
                "output": "$MSFT Bullish 🚀\n$MSFT Bullish 🚀\n$MSFT Bullish because Azure demand remains strong",
            }
        },
        structured_output_path="runs/x/social/social_summary.json",
        retrieval_time="2026-06-30T09:30:00+10:00",
    )

    cards = result["social_cards"]

    assert len(cards) == 2
    assert cards[0]["duplicate_or_near_duplicate"] is True
    assert cards[0]["reasoning_quality"] == "low"
    assert cards[0]["candidate_sentiment_label"] == "bullish"
    assert cards[0]["influence_weight"] < cards[1]["influence_weight"]
    assert result["sources"][0]["confidence"] != "high"


def test_build_fundamentals_evidence_records_statement_sections_and_sector_expectations():
    result = build_fundamentals_evidence(
        ticker="CBA.AX",
        trade_date="2026-06-29",
        identity={"sector": "Financial Services", "industry": "Banks"},
        tool_calls={
            "get_income_statement": {"status": "ok", "output": "Revenue and net income increased."},
            "get_balance_sheet": {"status": "ok", "output": "Cash, debt, and liquidity details."},
        },
        structured_output_path="runs/x/fundamentals/statement_records.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    first = result["statement_records"][0]
    assert first["evidence_id"] == "fundamentals:CBA.AX:2026-06-29:001"
    assert first["section_name"] == "income statement"
    assert "revenue" in first["supports_claims"]
    assert "NIM" in first["sector_specific_metric_expectations"]
    assert first["final_fundamentals_judgment"] == "pending_codex_interpretation"
    assert result["ledger_entries"][0]["tool_name"] == "fundamentals_statement_evidence"


def test_build_fundamentals_evidence_prioritizes_technology_sector_over_consumer_industry():
    result = build_fundamentals_evidence(
        ticker="AAPL",
        trade_date="2026-06-30",
        identity={"sector": "Technology", "industry": "Consumer Electronics"},
        tool_calls={"get_fundamentals": {"status": "ok", "output": "Revenue, gross margin, and R&D data"}},
        structured_output_path="runs/x/fundamentals/statement_records.json",
        retrieval_time="2026-06-30T09:30:00+10:00",
    )

    expectations = result["statement_records"][0]["sector_specific_metric_expectations"]
    assert "R&D" in expectations
    assert "store count" not in expectations


def test_build_stage_input_evidence_records_pending_and_available_inputs(tmp_path):
    available = tmp_path / "market.md"
    missing = tmp_path / "manager.md"
    available.write_text("# Market\n", encoding="utf-8")

    result = build_stage_input_evidence(
        ticker="MSFT",
        trade_date="2026-06-29",
        role="research_manager",
        allowed_inputs=[str(available), str(missing)],
        structured_output_path=str(tmp_path / "input_records.json"),
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    assert result["input_records"][0]["status"] == "available"
    assert result["input_records"][1]["status"] == "pending_or_missing"
    assert result["ledger_entries"][1]["confidence"] == "low"
    assert result["ledger_entries"][1]["limitations"] == ["input_pending_or_missing_at_task_generation"]
