from __future__ import annotations

import re
from typing import Any

from news_sources.base import NewsCandidate, SourceAttempt


def _title_from_source(source: dict[str, Any]) -> str:
    excerpt = re.sub(r"\s+", " ", str(source.get("excerpt") or "")).strip()
    match = re.search(r"Exhibit\s+99\.1\s+(.{20,180}?)(?:\s{2,}|CUPERTINO|REDMOND|[A-Z][a-z]+,\s[A-Z][a-z]+)", excerpt)
    if match:
        return match.group(1).strip(" -|")
    description = str(source.get("description") or "").strip()
    filing_date = str(source.get("filing_date") or "").strip()
    return f"{description or 'Earnings release'} filed {filing_date}".strip()


def _date_from_source(source: dict[str, Any]) -> str:
    for key in ("filing_date", "announcement_date", "lodgement_date", "source_date", "published_at"):
        value = str(source.get(key) or "").strip()
        if value:
            return value[:10]
    return ""


def _is_asx_official_source(source_type: str) -> bool:
    return source_type.startswith("asx_")


class RegulatoryFilingsAdapter:
    name = "regulatory_filings_adapter"

    def __init__(self, *, ticker: str, company_name: str, trade_date: str, financial_sources: list[dict[str, Any]] | None):
        self.ticker = ticker
        self.company_name = company_name
        self.trade_date = trade_date
        self.financial_sources = financial_sources or []

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        candidates: list[NewsCandidate] = []
        for source in self.financial_sources:
            if not isinstance(source, dict):
                continue
            source_type = str(source.get("source_type") or "")
            filing_date = _date_from_source(source)
            excerpt = str(source.get("excerpt") or "")
            url = str(source.get("url") or "")
            if source.get("status") != "available":
                continue
            if source_type != "earnings_release_8k" and not _is_asx_official_source(source_type):
                continue
            if not filing_date or filing_date > self.trade_date or not excerpt:
                continue
            is_asx = _is_asx_official_source(source_type)
            candidates.append(
                NewsCandidate(
                    title=str(source.get("title") or "").strip() or _title_from_source(source),
                    source="ASX announcement" if is_asx else "SEC filing",
                    source_url=url,
                    published_at=filing_date,
                    discovered_by=self.name,
                    source_type="official_exchange" if is_asx else "regulator",
                    raw_snippet=excerpt[:500],
                    full_text=excerpt,
                    tickers_detected=[self.ticker],
                    company_names_detected=[self.company_name],
                )
            )
        return candidates, SourceAttempt(
            adapter=self.name,
            status="available" if candidates else "unavailable",
            items_found=len(candidates),
            limitations=[] if candidates else ["no pre-trade-date regulatory or ASX official-source candidate found"],
            fallback_used=False,
        )
