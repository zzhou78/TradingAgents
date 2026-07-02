from __future__ import annotations

import importlib.util
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]


def _load_script(name: str):
    path = BUNDLE / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_reddit_adapter():
    path = BUNDLE / "scripts" / "sentiment_sources" / "reddit_adapter.py"
    spec = importlib.util.spec_from_file_location("reddit_adapter", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_quality_validator():
    return _load_script("validate_quality_review")


def test_direct_ticker_reasoned_post_gets_higher_weight_and_independence_metadata():
    quality = _load_script("sentiment_item_quality")

    card = quality.evaluate_social_item(
        ticker="MSFT",
        trade_date="2026-06-30",
        source="stocktwits",
        text="$MSFT bullish because Azure demand and margin growth still support earnings.",
        posted_at="2026-06-30T13:20:00Z",
    )

    assert card["ticker_relevance"] == "direct_company"
    assert card["reasoning_quality"] in {"medium", "high"}
    assert card["influence_weight"] >= 0.45
    assert card["source_confidence_category"] == "ticker_specific_retail_platform"
    assert card["primary_role_owner"] == "sentiment_analyst"
    assert card["secondary_use_purpose"] == "reaction_evidence"
    assert card["independence_group_id"].startswith("reaction:MSFT:2026-06-30:")


def test_rocket_meme_post_receives_low_reasoning_quality_and_weight():
    quality = _load_script("sentiment_item_quality")

    card = quality.evaluate_social_item(
        ticker="MSFT",
        trade_date="2026-06-30",
        source="stocktwits",
        text="$MSFT moon rocket bullish lol",
        posted_at="2026-06-30T13:20:00Z",
    )

    assert card["reasoning_quality"] == "low"
    assert card["meme_or_joke"] is True
    assert card["influence_weight"] <= 0.12


def test_duplicate_social_posts_are_deduplicated_and_marked():
    cards_module = _load_script("sentiment_evidence_cards")

    cards, _ = cards_module.build_sentiment_cards(
        ticker="MSFT",
        trade_date="2026-06-30",
        source="stocktwits",
        lines=[
            "$MSFT bearish because guidance risk remains.",
            "$MSFT bearish because guidance risk remains.",
        ],
    )

    assert len(cards) == 1
    assert cards[0]["duplicate_or_near_duplicate"] is True


def test_post_after_trade_date_is_invalid_for_as_of_use():
    quality = _load_script("sentiment_item_quality")

    card = quality.evaluate_social_item(
        ticker="MSFT",
        trade_date="2026-06-30",
        source="stocktwits",
        text="$MSFT bullish because earnings beat expectations.",
        posted_at="2026-07-01T00:01:00Z",
    )

    assert card["as_of_validity"]["valid_for_trade_date"] is False
    assert card["influence_weight"] == 0.0
    assert "post_trade_date" in card["limitations"]


def test_cross_ticker_post_is_not_direct_company_evidence():
    quality = _load_script("sentiment_item_quality")

    card = quality.evaluate_social_item(
        ticker="MSFT",
        trade_date="2026-06-30",
        source="stocktwits",
        text="$AAPL and $NVDA are driving the AI trade today.",
        posted_at="2026-06-30T10:00:00Z",
    )

    assert card["ticker_relevance"] == "cross_ticker"
    assert card["influence_weight"] < 0.25


def test_bullish_platform_label_without_reasoning_does_not_create_medium_confidence():
    social = _load_script("social_evidence")

    packet = social.build_social_evidence(
        ticker="MSFT",
        trade_date="2026-06-30",
        tool_calls={"fetch_stocktwits_messages": {"status": "ok", "output": "$MSFT bullish"}},
        structured_output_path="social/social_summary.json",
        retrieval_time="2026-06-30T23:59:00+10:00",
    )

    assert packet["sources"][0]["confidence"] == "low"
    assert packet["social_cards"][0]["platform_label"] == "bullish"
    assert packet["social_cards"][0]["reasoning_quality"] == "low"


def test_reddit_rate_limit_response_produces_rate_limited_status(tmp_path: Path):
    module = _load_reddit_adapter()

    def fetcher() -> list[str]:
        raise module.RedditRateLimitError("rate limited", retry_after_seconds=60)

    adapter = module.RedditAdapter(
        ticker="MSFT",
        trade_date="2026-06-30",
        cache_root=tmp_path,
        credentials_configured=True,
        fetcher=fetcher,
    )

    result = adapter.collect_with_status()

    assert result.status == "rate_limited"
    assert "reddit_rate_limited" in result.limitations
    assert result.candidates == []


def test_cached_reddit_data_is_used_before_network_call(tmp_path: Path):
    module = _load_reddit_adapter()
    cache_file = tmp_path / "reddit" / "MSFT" / "2026-06-30.json"
    cache_file.parent.mkdir(parents=True)
    cache_file.write_text(
        json.dumps(
            {
                "cached_at": datetime.now(timezone.utc).isoformat(),
                "items": [
                    {
                        "text": "$MSFT bullish because Azure demand is resilient.",
                        "posted_at": "2026-06-30T12:00:00Z",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    def fetcher() -> list[str]:
        raise AssertionError("network fetch should not run when fresh cache exists")

    adapter = module.RedditAdapter(
        ticker="MSFT",
        trade_date="2026-06-30",
        cache_root=tmp_path,
        credentials_configured=True,
        fetcher=fetcher,
    )

    result = adapter.collect_with_status()

    assert result.status == "available"
    assert result.cache_used is True
    assert result.candidates[0].text.startswith("$MSFT bullish")


def test_stale_reddit_cache_is_disclosed(tmp_path: Path):
    module = _load_reddit_adapter()
    cache_file = tmp_path / "reddit" / "MSFT" / "2026-06-30.json"
    cache_file.parent.mkdir(parents=True)
    cache_file.write_text(
        json.dumps(
            {
                "cached_at": (datetime.now(timezone.utc) - timedelta(days=9)).isoformat(),
                "items": [{"text": "$MSFT bearish because valuation risk is high.", "posted_at": "2026-06-29T12:00:00Z"}],
            }
        ),
        encoding="utf-8",
    )

    adapter = module.RedditAdapter(
        ticker="MSFT",
        trade_date="2026-06-30",
        cache_root=tmp_path,
        credentials_configured=False,
    )

    result = adapter.collect_with_status()

    assert result.status == "unavailable"
    assert result.cache_used is True
    assert "reddit_cache_stale" in result.limitations
    assert "reddit_credentials_missing" in result.limitations


def test_missing_reddit_credentials_returns_unavailable_not_crash(tmp_path: Path):
    module = _load_reddit_adapter()
    adapter = module.RedditAdapter(ticker="MSFT", trade_date="2026-06-30", cache_root=tmp_path)

    result = adapter.collect_with_status()

    assert result.status == "unavailable"
    assert "reddit_credentials_missing" in result.limitations


def test_sentiment_report_with_hidden_reddit_rate_limit_fails_validation(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    evidence_dir = tmp_path / "evidence" / "MSFT" / "2026-06-30"
    (report_dir / "1_analysts").mkdir(parents=True)
    (evidence_dir / "social").mkdir(parents=True)
    (report_dir / "1_analysts" / "sentiment.md").write_text(
        "# Sentiment\n\n"
        "## Tool Outputs Used\n\n- social_evidence_processing\n\n"
        "## Social Evidence Processing Rules\n\n"
        "Reddit is unavailable but final sentiment is neutral.\n\n"
        "## Final Sentiment Interpretation\n\nNeutral.\n",
        encoding="utf-8",
    )
    (evidence_dir / "social" / "social_summary.json").write_text(
        json.dumps({"sources": [{"source": "reddit", "status": "rate_limited", "limitations": ["reddit_rate_limited"]}]}),
        encoding="utf-8",
    )
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "MSFT", "trade_date": "2026-06-30"}), encoding="utf-8")

    errors = validator.validate_report_dir(report_dir, evidence_path)

    assert any("reddit rate limit is hidden" in error for error in errors)


def test_sentiment_using_news_article_cards_as_independent_signal_fails_validation(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    analyst_dir = report_dir / "1_analysts"
    analyst_dir.mkdir(parents=True)
    (analyst_dir / "sentiment.md").write_text(
        "# Sentiment\n\n"
        "## Tool Outputs Used\n\n- news/article_cards.json\n\n"
        "## Social Evidence Processing Rules\n\n"
        "Usable ticker items: 0.\n\n"
        "## Final Sentiment Interpretation\n\n"
        "Sentiment is independently bearish because News Analyst article cards show negative layoffs coverage.\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert any("News Analyst article cards as independent sentiment evidence" in error for error in errors)


def test_research_manager_double_counting_one_event_across_news_and_sentiment_fails_validation(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    research_dir = report_dir / "2_research"
    research_dir.mkdir(parents=True)
    (research_dir / "manager.md").write_text(
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- stage_input_evidence\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Role | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group |\n"
        "|---|---|---|---|---|---:|---|---|\n"
        "| News | Bearish | High | Medium | news:MSFT:2026-06-30:001 | -2 | Reuters layoffs article | event:MSFT:2026-06-30:layoffs |\n"
        "| Sentiment | Bearish | Medium | Low | social:MSFT:2026-06-30:item:0001 | -2 | StockTwits repeats layoffs headline | event:MSFT:2026-06-30:layoffs |\n\n"
        "## Rating Rationale\n\nSell beats Hold because two independent signals confirm layoffs.\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert any("research manager double-counts one independence group" in error for error in errors)


def test_research_manager_using_independence_groups_correctly_passes_double_count_gate(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    research_dir = report_dir / "2_research"
    research_dir.mkdir(parents=True)
    (research_dir / "manager.md").write_text(
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- stage_input_evidence\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Role | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group |\n"
        "|---|---|---|---|---|---:|---|---|\n"
        "| News | Bearish | High | Medium | news:MSFT:2026-06-30:001 | -2 | Layoffs event fact | event:MSFT:2026-06-30:layoffs |\n"
        "| Sentiment | Bearish | Low | Low | social:MSFT:2026-06-30:item:0001 | -0.5 | Related retail reaction; not a separate fundamental fact | reaction:MSFT:2026-06-30:layoffs |\n\n"
        "## Rating Rationale\n\nSell vs Hold is not decided from social alone; the related reaction is lower-confidence context.\n",
        encoding="utf-8",
    )

    errors = validator._research_manager_quality_errors(report_dir / "2_research" / "manager.md")

    assert not any("double-counts" in error for error in errors)
