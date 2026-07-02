from __future__ import annotations

import json
import time
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from sentiment_sources.base import SentimentSourceResult, SocialCandidate
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.sentiment_sources.base import (
        SentimentSourceResult,
        SocialCandidate,
    )

BUNDLE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CACHE_ROOT = BUNDLE_ROOT / "cache"
DEFAULT_CACHE_TTL_SECONDS = 48 * 60 * 60


class RedditRateLimitError(Exception):
    def __init__(self, message: str = "reddit rate limited", *, retry_after_seconds: int | None = None) -> None:
        super().__init__(message)
        self.retry_after_seconds = retry_after_seconds


class RedditAdapter:
    name = "reddit_adapter"

    def __init__(
        self,
        *,
        lines: list[str] | None = None,
        ticker: str = "",
        trade_date: str = "",
        cache_root: Path | str = DEFAULT_CACHE_ROOT,
        credentials_configured: bool = False,
        fetcher: Callable[[], list[str] | list[dict[str, Any]]] | None = None,
        cache_ttl_seconds: int = DEFAULT_CACHE_TTL_SECONDS,
        max_retries: int = 2,
        request_budget: int = 1,
    ) -> None:
        self.lines = lines
        self.ticker = ticker.upper()
        self.trade_date = trade_date
        self.cache_root = Path(cache_root)
        self.credentials_configured = credentials_configured
        self.fetcher = fetcher
        self.cache_ttl_seconds = cache_ttl_seconds
        self.max_retries = max(0, max_retries)
        self.request_budget = max(0, request_budget)

    @property
    def cache_path(self) -> Path:
        ticker = self.ticker or "UNKNOWN"
        trade_date = self.trade_date or "unknown-date"
        return self.cache_root / "reddit" / ticker / f"{trade_date}.json"

    def collect(self) -> list[SocialCandidate]:
        return self.collect_with_status().candidates

    def collect_with_status(self) -> SentimentSourceResult:
        if self.lines is not None:
            return SentimentSourceResult(
                source="reddit",
                status="available",
                candidates=self._candidates_from_items(self.lines),
            )

        cached = self._read_cache()
        if cached and cached["fresh"]:
            return SentimentSourceResult(
                source="reddit",
                status="available",
                candidates=self._candidates_from_items(cached["items"]),
                limitations=[],
                cache_used=True,
                cache_age_seconds=cached["age_seconds"],
                request_budget_remaining=self.request_budget,
            )

        stale_limitations: list[str] = []
        stale_candidates: list[SocialCandidate] = []
        stale_age_seconds: int | None = None
        if cached:
            stale_limitations.append("reddit_cache_stale")
            stale_candidates = self._candidates_from_items(cached["items"])
            stale_age_seconds = cached["age_seconds"]

        if not self.credentials_configured:
            return SentimentSourceResult(
                source="reddit",
                status="unavailable",
                candidates=stale_candidates,
                limitations=[*stale_limitations, "reddit_credentials_missing"],
                cache_used=bool(cached),
                cache_age_seconds=stale_age_seconds,
                request_budget_remaining=self.request_budget,
            )

        if self.request_budget <= 0:
            return SentimentSourceResult(
                source="reddit",
                status="unavailable",
                candidates=stale_candidates,
                limitations=[*stale_limitations, "reddit_request_budget_exhausted"],
                cache_used=bool(cached),
                cache_age_seconds=stale_age_seconds,
                request_budget_remaining=0,
            )

        if self.fetcher is None:
            return SentimentSourceResult(
                source="reddit",
                status="unavailable",
                candidates=stale_candidates,
                limitations=[*stale_limitations, "reddit_fetcher_unavailable"],
                cache_used=bool(cached),
                cache_age_seconds=stale_age_seconds,
                request_budget_remaining=max(0, self.request_budget - 1),
            )

        last_retry_after: int | None = None
        for attempt in range(self.max_retries + 1):
            try:
                items = self.fetcher()
            except RedditRateLimitError as exc:
                last_retry_after = exc.retry_after_seconds
                if attempt >= self.max_retries:
                    return SentimentSourceResult(
                        source="reddit",
                        status="rate_limited",
                        candidates=stale_candidates,
                        limitations=[*stale_limitations, "reddit_rate_limited"],
                        cache_used=bool(cached),
                        cache_age_seconds=stale_age_seconds,
                        retry_after_seconds=last_retry_after,
                        request_budget_remaining=max(0, self.request_budget - 1),
                    )
                self._bounded_backoff(attempt, exc.retry_after_seconds)
            except Exception as exc:  # pragma: no cover - defensive status plumbing
                return SentimentSourceResult(
                    source="reddit",
                    status="error",
                    candidates=stale_candidates,
                    limitations=[*stale_limitations, f"reddit_error:{type(exc).__name__}"],
                    cache_used=bool(cached),
                    cache_age_seconds=stale_age_seconds,
                    request_budget_remaining=max(0, self.request_budget - 1),
                )
            else:
                self._write_cache(items)
                candidates = self._candidates_from_items(items)
                limitations = [] if candidates else ["reddit_no_usable_items"]
                return SentimentSourceResult(
                    source="reddit",
                    status="available",
                    candidates=candidates,
                    limitations=limitations,
                    cache_used=False,
                    request_budget_remaining=max(0, self.request_budget - 1),
                )

        return SentimentSourceResult(
            source="reddit",
            status="rate_limited",
            candidates=stale_candidates,
            limitations=[*stale_limitations, "reddit_rate_limited"],
            cache_used=bool(cached),
            cache_age_seconds=stale_age_seconds,
            retry_after_seconds=last_retry_after,
            request_budget_remaining=max(0, self.request_budget - 1),
        )

    def _read_cache(self) -> dict[str, Any] | None:
        if not self.cache_path.exists():
            return None
        try:
            payload = json.loads(self.cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        cached_at = _parse_datetime(str(payload.get("cached_at", "")))
        if cached_at is None:
            return None
        age_seconds = max(0, int((datetime.now(timezone.utc) - cached_at).total_seconds()))
        return {
            "items": payload.get("items", []),
            "age_seconds": age_seconds,
            "fresh": age_seconds <= self.cache_ttl_seconds,
        }

    def _write_cache(self, items: list[str] | list[dict[str, Any]]) -> None:
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "cached_at": datetime.now(timezone.utc).isoformat(),
            "items": items,
        }
        self.cache_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _candidates_from_items(self, items: list[str] | list[dict[str, Any]]) -> list[SocialCandidate]:
        candidates: list[SocialCandidate] = []
        for item in items:
            if isinstance(item, str):
                text = item
                posted_at = ""
            elif isinstance(item, dict):
                text = str(item.get("text") or item.get("body") or item.get("title") or "")
                posted_at = str(item.get("posted_at") or item.get("created_at") or "")
            else:
                continue
            if not text.strip():
                continue
            candidates.append(
                SocialCandidate(
                    source="reddit",
                    source_url="local://tool/fetch_reddit_posts",
                    posted_at=posted_at,
                    text=text.strip(),
                    author_metadata_available=False,
                    retrieval_limitations=[],
                )
            )
        return candidates

    def _bounded_backoff(self, attempt: int, retry_after_seconds: int | None) -> None:
        delay = min(float(retry_after_seconds or (2**attempt)), 2.0)
        if delay > 0:
            time.sleep(delay)


def _parse_datetime(value: str) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)
