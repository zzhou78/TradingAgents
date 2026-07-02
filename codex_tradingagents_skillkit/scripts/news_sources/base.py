from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class NewsCandidate:
    title: str
    source: str
    source_url: str
    published_at: str
    discovered_by: str
    source_type: str
    raw_snippet: str = ""
    full_text: str = ""
    tickers_detected: list[str] = field(default_factory=list)
    company_names_detected: list[str] = field(default_factory=list)
    retrieval_limitations: list[str] = field(default_factory=list)

    def to_dict(self, *, candidate_id: str, ticker: str, company_name: str) -> dict[str, Any]:
        return {
            "candidate_id": candidate_id,
            "ticker": ticker,
            "company_name": company_name,
            "title": self.title,
            "source": self.source,
            "source_url": self.source_url,
            "url": self.source_url,
            "published_at": self.published_at,
            "published_date": self.published_at[:10],
            "discovered_by": self.discovered_by,
            "source_type": self.source_type,
            "raw_snippet": self.raw_snippet,
            "snippet": self.raw_snippet,
            "full_text": self.full_text,
            "tickers_detected": self.tickers_detected,
            "company_names_detected": self.company_names_detected,
            "retrieval_limitations": self.retrieval_limitations,
        }


@dataclass
class SourceAttempt:
    adapter: str
    status: str
    items_found: int = 0
    limitations: list[str] = field(default_factory=list)
    fallback_used: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "adapter": self.adapter,
            "status": self.status,
            "items_found": self.items_found,
            "limitations": self.limitations,
            "fallback_used": self.fallback_used,
        }


class NewsSourceAdapter(Protocol):
    name: str

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        ...
