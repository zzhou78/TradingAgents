from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class SocialCandidate:
    source: str
    source_url: str
    posted_at: str
    text: str
    author_id_hash: str = ""
    author_metadata_available: bool = False
    platform_label: str = "none"
    cashtags_detected: list[str] = field(default_factory=list)
    reply_count: int | None = None
    like_count: int | None = None
    repost_count: int | None = None
    retrieval_limitations: list[str] = field(default_factory=list)


@dataclass
class SentimentSourceResult:
    source: str
    status: str
    candidates: list[SocialCandidate] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    cache_used: bool = False
    cache_age_seconds: int | None = None
    retry_after_seconds: int | None = None
    request_budget_remaining: int | None = None


class SentimentSourceAdapter(Protocol):
    name: str

    def collect(self) -> list[SocialCandidate]:
        ...

    def collect_with_status(self) -> SentimentSourceResult:
        ...
