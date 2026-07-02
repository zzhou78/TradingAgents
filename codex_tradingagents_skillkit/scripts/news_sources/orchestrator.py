# ruff: noqa: E402

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from news_sources.base import NewsCandidate, SourceAttempt
from news_sources.company_ir_adapter import CompanyIrAdapter, HtmlFetcher
from news_sources.newsapi_adapter import NewsApiAdapter
from news_sources.regulatory_filings_adapter import RegulatoryFilingsAdapter
from news_sources.rss_adapter import RssAdapter
from news_sources.upstream_tradingagents import UpstreamTradingAgentsAdapter
from news_sources.websearch_adapter import WebSearchAdapter

SOURCE_ORDER = ("company_ir", "regulatory", "websearch", "newsapi", "rss", "upstream")


def _adapter_for_source(
    source: str,
    *,
    ticker: str,
    company_name: str,
    trade_date: str,
    lookback_days: int,
    company_ir_urls: list[str],
    upstream_calls: dict[str, dict[str, Any]] | None,
    financial_sources: list[dict[str, Any]] | None,
    html_fetcher: HtmlFetcher | None,
):
    if source == "company_ir":
        return CompanyIrAdapter(
            ticker=ticker,
            company_name=company_name,
            trade_date=trade_date,
            urls=company_ir_urls,
            html_fetcher=html_fetcher,
        )
    if source == "regulatory":
        return RegulatoryFilingsAdapter(
            ticker=ticker,
            company_name=company_name,
            trade_date=trade_date,
            financial_sources=financial_sources,
        )
    if source == "websearch":
        return WebSearchAdapter()
    if source == "newsapi":
        return NewsApiAdapter()
    if source == "rss":
        return RssAdapter(
            ticker=ticker,
            company_name=company_name,
            trade_date=trade_date,
            lookback_days=lookback_days,
        )
    if source == "upstream":
        return UpstreamTradingAgentsAdapter(
            ticker=ticker,
            company_name=company_name,
            upstream_calls=upstream_calls,
        )
    return None


def _candidate_dicts(
    *,
    ticker: str,
    company_name: str,
    trade_date: str,
    candidates: list[NewsCandidate],
) -> list[dict[str, Any]]:
    rows = []
    for index, candidate in enumerate(candidates, start=1):
        rows.append(
            candidate.to_dict(
                candidate_id=f"candidate:{ticker}:{trade_date}:{index:03d}",
                ticker=ticker,
                company_name=company_name,
            )
        )
    return rows


def _ledger_entries(*, ticker: str, trade_date: str, candidates: list[dict[str, Any]], output_dir: Path | None) -> list[dict[str, Any]]:
    structured_output_path = str(output_dir / "candidates.json") if output_dir else ""
    entries = []
    for candidate in candidates:
        entries.append(
            {
                "evidence_id": candidate["candidate_id"],
                "ticker": ticker,
                "trade_date": trade_date,
                "role": "news_analyst",
                "tool_name": "news_source_adapter",
                "tool_version": "0.1.0",
                "source_url": candidate.get("source_url", ""),
                "source_date": candidate.get("published_at", ""),
                "retrieval_time": "",
                "as_of_validity": {
                    "valid_for_trade_date": bool(candidate.get("published_at") and candidate["published_at"] <= trade_date),
                    "reason": "source_date is on or before trade_date"
                    if candidate.get("published_at") and candidate["published_at"] <= trade_date
                    else "source_date is after trade_date or missing",
                },
                "confidence": "low" if candidate.get("source_type") == "upstream_fallback" else "medium",
                "limitations": list(candidate.get("retrieval_limitations") or []),
                "structured_output_path": structured_output_path,
                "report_sections_using_it": ["News Analyst"],
            }
        )
    return entries


def _write_outputs(output_dir: Path, candidates: list[dict[str, Any]], attempts: list[dict[str, Any]], ledger_entries: list[dict[str, Any]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "candidates.json").write_text(json.dumps(candidates, indent=2), encoding="utf-8")
    (output_dir / "source_attempts.json").write_text(json.dumps(attempts, indent=2), encoding="utf-8")
    (output_dir / "evidence_ledger.jsonl").write_text(
        "".join(json.dumps(entry, sort_keys=True) + "\n" for entry in ledger_entries),
        encoding="utf-8",
    )


def collect_news_candidates(
    *,
    ticker: str,
    company_name: str,
    trade_date: str,
    lookback_days: int,
    approved_sources: list[str],
    company_ir_urls: list[str] | None = None,
    upstream_calls: dict[str, dict[str, Any]] | None = None,
    financial_sources: list[dict[str, Any]] | None = None,
    html_fetcher: HtmlFetcher | None = None,
    output_dir: str | Path | None = None,
) -> dict[str, Any]:
    all_candidates: list[NewsCandidate] = []
    attempts: list[SourceAttempt] = []
    requested = [source for source in SOURCE_ORDER if source in set(approved_sources)]
    for source in requested:
        adapter = _adapter_for_source(
            source,
            ticker=ticker,
            company_name=company_name,
            trade_date=trade_date,
            lookback_days=lookback_days,
            company_ir_urls=company_ir_urls or [],
            upstream_calls=upstream_calls,
            financial_sources=financial_sources,
            html_fetcher=html_fetcher,
        )
        if not adapter:
            continue
        candidates, attempt = adapter.collect()
        all_candidates.extend(candidates)
        attempts.append(attempt)

    candidate_rows = _candidate_dicts(
        ticker=ticker,
        company_name=company_name,
        trade_date=trade_date,
        candidates=all_candidates,
    )
    attempt_rows = [attempt.to_dict() for attempt in attempts]
    output_path = Path(output_dir) if output_dir else None
    ledger_entries = _ledger_entries(
        ticker=ticker,
        trade_date=trade_date,
        candidates=candidate_rows,
        output_dir=output_path,
    )
    if output_path:
        _write_outputs(output_path, candidate_rows, attempt_rows, ledger_entries)
    return {
        "candidates": candidate_rows,
        "source_attempts": attempt_rows,
        "ledger_entries": ledger_entries,
    }
