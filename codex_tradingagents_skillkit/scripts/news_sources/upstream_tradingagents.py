from __future__ import annotations

import ast
import json
from typing import Any

from news_sources.base import NewsCandidate, SourceAttempt


def _candidate_from_mapping(payload: dict[str, Any], *, ticker: str, company_name: str) -> NewsCandidate:
    source = payload.get("source") or payload.get("publisher") or "upstream_tradingagents"
    if isinstance(source, dict):
        source = source.get("name") or "upstream_tradingagents"
    published = str(
        payload.get("published_date")
        or payload.get("date")
        or payload.get("published")
        or payload.get("datetime")
        or ""
    )[:10]
    title = str(payload.get("title") or payload.get("headline") or payload.get("name") or "").strip()
    snippet = str(payload.get("snippet") or payload.get("summary") or payload.get("description") or "").strip()
    full_text = str(payload.get("full_text") or payload.get("content") or payload.get("body") or "").strip()
    haystack = f"{title} {snippet}"
    return NewsCandidate(
        title=title,
        source=str(source),
        source_url=str(payload.get("url") or payload.get("link") or payload.get("article_url") or "").strip(),
        published_at=published,
        discovered_by="upstream_tradingagents_adapter",
        source_type="upstream_fallback",
        raw_snippet=snippet,
        full_text=full_text,
        tickers_detected=[ticker] if ticker.upper() in haystack.upper() else [],
        company_names_detected=[company_name] if company_name and company_name.lower() in haystack.lower() else [],
        retrieval_limitations=["upstream_fallback"],
    )


def _records_from_output(output: str) -> list[dict[str, Any]]:
    try:
        parsed = json.loads(output)
    except json.JSONDecodeError:
        try:
            parsed = ast.literal_eval(output)
        except (ValueError, SyntaxError):
            parsed = None
    if isinstance(parsed, list):
        return [record for record in parsed if isinstance(record, dict)]
    if isinstance(parsed, dict):
        for key in ("articles", "news", "items", "results"):
            rows = parsed.get(key)
            if isinstance(rows, list):
                return [record for record in rows if isinstance(record, dict)]
        return [parsed]
    return []


class UpstreamTradingAgentsAdapter:
    name = "upstream_tradingagents_adapter"

    def __init__(self, *, ticker: str, company_name: str, upstream_calls: dict[str, dict[str, Any]] | None):
        self.ticker = ticker
        self.company_name = company_name
        self.upstream_calls = upstream_calls or {}

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        candidates: list[NewsCandidate] = []
        for tool_name in ("get_news", "get_global_news"):
            call = self.upstream_calls.get(tool_name, {})
            if call.get("status") != "ok" or not call.get("output"):
                continue
            for record in _records_from_output(str(call["output"])):
                candidate = _candidate_from_mapping(record, ticker=self.ticker, company_name=self.company_name)
                if candidate.title or candidate.source_url:
                    candidates.append(candidate)
        return candidates, SourceAttempt(
            adapter=self.name,
            status="available" if candidates else "unavailable",
            items_found=len(candidates),
            limitations=["fallback_only"],
            fallback_used=True,
        )
