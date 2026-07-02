from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
ORCHESTRATOR = BUNDLE / "scripts" / "news_sources" / "orchestrator.py"
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"
RSS_ADAPTER = BUNDLE / "scripts" / "news_sources" / "rss_adapter.py"


def _load_orchestrator():
    spec = importlib.util.spec_from_file_location("news_sources.orchestrator", ORCHESTRATOR)
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


def _load_rss_adapter():
    spec = importlib.util.spec_from_file_location("news_sources.rss_adapter", RSS_ADAPTER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_company_ir_adapter_returns_normalized_candidates(tmp_path: Path):
    orchestrator = _load_orchestrator()

    def fake_fetch(url: str) -> str:
        assert "investors.example" in url
        return """
        <html><body>
        <a href="https://investors.example/msft-ai-update">
        Microsoft announces AI infrastructure update
        </a>
        <time datetime="2026-06-29">29 Jun 2026</time>
        </body></html>
        """

    result = orchestrator.collect_news_candidates(
        ticker="MSFT",
        company_name="Microsoft",
        trade_date="2026-06-30",
        lookback_days=7,
        approved_sources=["company_ir"],
        company_ir_urls=["https://investors.example/news"],
        html_fetcher=fake_fetch,
        output_dir=tmp_path,
    )

    assert result["source_attempts"][0]["adapter"] == "company_ir_adapter"
    assert result["source_attempts"][0]["status"] == "available"
    assert result["candidates"][0]["candidate_id"] == "candidate:MSFT:2026-06-30:001"
    assert result["candidates"][0]["discovered_by"] == "company_ir_adapter"
    assert result["candidates"][0]["source_type"] == "company_ir"
    assert result["candidates"][0]["source_url"] == "https://investors.example/msft-ai-update"
    assert (tmp_path / "candidates.json").exists()
    assert (tmp_path / "source_attempts.json").exists()
    assert (tmp_path / "evidence_ledger.jsonl").exists()


def test_upstream_adapter_is_fallback_marked():
    orchestrator = _load_orchestrator()

    result = orchestrator.collect_news_candidates(
        ticker="MSFT",
        company_name="Microsoft",
        trade_date="2026-06-30",
        lookback_days=7,
        approved_sources=["upstream"],
        upstream_calls={
            "get_news": {
                "status": "ok",
                "output": json.dumps(
                    [
                        {
                            "title": "Microsoft supplier update",
                            "source": "upstream",
                            "url": "https://example.com/msft",
                            "published_date": "2026-06-29",
                            "snippet": "Microsoft supplier update.",
                        }
                    ]
                ),
            }
        },
    )

    assert result["source_attempts"][0]["adapter"] == "upstream_tradingagents_adapter"
    assert result["source_attempts"][0]["fallback_used"] is True
    assert result["candidates"][0]["source_type"] == "upstream_fallback"


def test_newsapi_missing_key_is_unavailable_not_crash(monkeypatch):
    orchestrator = _load_orchestrator()
    monkeypatch.delenv("NEWSAPI_KEY", raising=False)

    result = orchestrator.collect_news_candidates(
        ticker="MSFT",
        company_name="Microsoft",
        trade_date="2026-06-30",
        lookback_days=7,
        approved_sources=["newsapi"],
    )

    assert result["candidates"] == []
    assert result["source_attempts"][0]["adapter"] == "newsapi_adapter"
    assert result["source_attempts"][0]["status"] == "unavailable"
    assert "NEWSAPI_KEY" in result["source_attempts"][0]["limitations"][0]


def test_rss_adapter_filters_by_trade_date_and_normalizes_candidate():
    rss_module = _load_rss_adapter()
    feed = """
    <rss><channel>
      <item>
        <title>Apple announces services update</title>
        <link>https://www.apple.com/newsroom/apple-services-update/</link>
        <pubDate>Mon, 29 Jun 2026 10:00:00 GMT</pubDate>
        <description>Apple services update for customers.</description>
      </item>
      <item>
        <title>Apple future update</title>
        <link>https://www.apple.com/newsroom/future/</link>
        <pubDate>Wed, 01 Jul 2026 10:00:00 GMT</pubDate>
        <description>Apple future item.</description>
      </item>
    </channel></rss>
    """
    adapter = rss_module.RssAdapter(
        ticker="AAPL",
        company_name="Apple Inc.",
        trade_date="2026-06-30",
        lookback_days=7,
        feeds=["https://example.com/feed.xml"],
        rss_fetcher=lambda url: feed,
    )

    candidates, attempt = adapter.collect()

    assert attempt.status == "available"
    assert len(candidates) == 1
    assert candidates[0].title == "Apple announces services update"
    assert candidates[0].published_at == "2026-06-29"
    assert candidates[0].source_type == "company_ir"


def test_regulatory_sources_create_earnings_release_candidate():
    orchestrator = _load_orchestrator()

    result = orchestrator.collect_news_candidates(
        ticker="AAPL",
        company_name="Apple Inc.",
        trade_date="2026-06-30",
        lookback_days=30,
        approved_sources=["regulatory"],
        financial_sources=[
            {
                "source_type": "earnings_release_8k",
                "status": "available",
                "filing_date": "2026-04-30",
                "url": "https://www.sec.gov/aapl-8k",
                "description": "8-K",
                "excerpt": "Exhibit 99.1 Apple reports second quarter results. Apple revenue increased.",
            }
        ],
    )

    assert result["source_attempts"][0]["adapter"] == "regulatory_filings_adapter"
    assert result["source_attempts"][0]["status"] == "available"
    assert result["candidates"][0]["source_type"] == "regulator"
    assert result["candidates"][0]["full_text"]


def test_regulatory_sources_create_asx_official_candidate():
    orchestrator = _load_orchestrator()

    result = orchestrator.collect_news_candidates(
        ticker="BHP.AX",
        company_name="BHP Group",
        trade_date="2026-07-02",
        lookback_days=180,
        approved_sources=["regulatory"],
        financial_sources=[
            {
                "source_type": "asx_fallback_document",
                "status": "available",
                "announcement_date": "2025-12-31",
                "url": "https://www.bhp.com/investor-hub/reports-and-presentations/annual-report",
                "title": "BHP 2025 Annual Report",
                "excerpt": "Annual Report 2025. BHP management discussion and financial performance.",
            }
        ],
    )

    assert result["source_attempts"][0]["adapter"] == "regulatory_filings_adapter"
    assert result["source_attempts"][0]["status"] == "available"
    assert result["candidates"][0]["source"] == "ASX announcement"
    assert result["candidates"][0]["source_type"] == "official_exchange"
    assert result["candidates"][0]["full_text"]


def test_quality_gate_fails_when_upstream_fallback_is_only_news_source(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    evidence_dir = tmp_path / "evidence" / "MSFT" / "2026-06-30"
    (report_dir / "1_analysts").mkdir(parents=True)
    (evidence_dir / "news").mkdir(parents=True)
    (report_dir / "1_analysts" / "news.md").write_text(
        "## Tool Outputs Used\n\n"
        "## Article Evidence Cards\n\n"
        "## News Impact Summary\n\n"
        "Neutral impact from news:MSFT:2026-06-30:001.\n",
        encoding="utf-8",
    )
    (evidence_dir / "news" / "source_attempts.json").write_text(
        json.dumps(
            [
                {
                    "adapter": "upstream_tradingagents_adapter",
                    "status": "available",
                    "items_found": 1,
                    "limitations": ["fallback_only"],
                    "fallback_used": True,
                }
            ]
        ),
        encoding="utf-8",
    )
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "MSFT", "trade_date": "2026-06-30"}), encoding="utf-8")

    errors = validator.validate_report_dir(report_dir, evidence_path)

    assert any("upstream fallback is the only attempted news source" in error for error in errors)
