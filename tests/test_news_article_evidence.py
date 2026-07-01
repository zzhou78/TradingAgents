from __future__ import annotations

from codex_tradingagents_skillkit.scripts.news_article_evidence import build_news_evidence


def test_build_news_evidence_distinguishes_full_text_from_snippet_only():
    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Apple supplier update",
                "source": "Example News",
                "url": "https://example.com/apple-supplier",
                "published_date": "2026-06-28",
                "snippet": "Apple supplier commentary.",
                "full_text": "Apple supplier commentary with enough article body detail for extraction.",
            },
            {
                "title": "Apple analyst note",
                "source": "Example News",
                "url": "https://example.com/apple-analyst",
                "published_date": "2026-06-28",
                "snippet": "Analyst note summary only.",
                "full_text": "",
            },
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    cards = result["article_cards"]

    assert cards[0]["full_text_status"] == "full_text"
    assert cards[0]["confidence"] == "medium"
    assert cards[1]["full_text_status"] == "snippet_only"
    assert cards[1]["confidence"] == "low"
    assert "likely_effect" not in cards[0]


def test_build_news_evidence_deduplicates_by_normalized_url_and_title():
    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Apple announces service update",
                "source": "Example News",
                "url": "https://example.com/apple-services?utm_source=x",
                "published_date": "2026-06-28",
                "snippet": "Apple services update.",
                "full_text": "",
            },
            {
                "title": "Apple announces service update",
                "source": "Example News",
                "url": "https://example.com/apple-services",
                "published_date": "2026-06-28",
                "snippet": "Duplicate article.",
                "full_text": "",
            },
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    assert len(result["article_cards"]) == 1
    assert result["article_cards"][0]["duplicate_count"] == 2


def test_build_news_evidence_marks_post_trade_date_invalid():
    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Future Apple article",
                "source": "Example News",
                "url": "https://example.com/future",
                "published_date": "2026-06-30",
                "snippet": "Future item.",
                "full_text": "",
            }
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    card = result["article_cards"][0]
    ledger = result["ledger_entries"][0]

    assert card["as_of_validity"]["valid_for_trade_date"] is False
    assert ledger["as_of_validity"]["valid_for_trade_date"] is False
    assert "post_trade_date" in card["limitations"]


def test_build_news_evidence_fetches_full_text_from_candidate_url():
    fetched_urls: list[str] = []

    def fetch_full_text(url: str) -> str:
        fetched_urls.append(url)
        return "Fetched article body text with enough detail to support review-grade article evidence."

    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Apple services expansion",
                "source": "Example News",
                "url": "https://example.com/apple-services?utm_source=newsletter",
                "published_date": "2026-06-28",
                "snippet": "Apple services expansion summary only.",
                "full_text": "",
            }
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
        full_text_fetcher=fetch_full_text,
    )

    card = result["article_cards"][0]
    assert fetched_urls == ["https://example.com/apple-services"]
    assert card["full_text_status"] == "full_text"
    assert card["full_text_source"] == "url_fetch"
    assert card["confidence"] == "medium"
    assert card["evidence_gap"] == ""


def test_build_news_evidence_keeps_failed_full_text_fetch_low_confidence():
    def fetch_full_text(url: str) -> str:
        raise TimeoutError(f"timed out fetching {url}")

    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Apple analyst note",
                "source": "Example News",
                "url": "https://example.com/apple-analyst",
                "published_date": "2026-06-28",
                "snippet": "Analyst note summary only.",
                "full_text": "",
            }
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
        full_text_fetcher=fetch_full_text,
    )

    card = result["article_cards"][0]
    assert card["full_text_status"] == "snippet_only"
    assert card["full_text_source"] == "unavailable"
    assert card["confidence"] == "low"
    assert "full_text_retrieval_failed" in card["limitations"]
