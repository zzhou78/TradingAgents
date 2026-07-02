from __future__ import annotations

import re
import urllib.request
import xml.etree.ElementTree as ET
from collections.abc import Callable
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime

from news_sources.base import NewsCandidate, SourceAttempt

RssFetcher = Callable[[str], str]

DEFAULT_RSS_FEEDS = {
    "AAPL": ["https://www.apple.com/newsroom/rss-feed.rss"],
    "MSFT": ["https://blogs.microsoft.com/feed/"],
}


def _default_fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "CodexTradingAgentsNewsSources/0.1"})
    with urllib.request.urlopen(request, timeout=15) as response:  # noqa: S310 - whitelisted public RSS feeds.
        return response.read().decode("utf-8", errors="replace")


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", text or "")).strip()


def _published_date(value: str) -> str:
    if not value:
        return ""
    try:
        return parsedate_to_datetime(value).date().isoformat()
    except (TypeError, ValueError, IndexError):
        match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", value)
        return match.group(1) if match else ""


def _company_needles(company_name: str, ticker: str) -> list[str]:
    first = re.split(r"\s+", company_name.strip())[0].lower() if company_name.strip() else ""
    return [needle for needle in dict.fromkeys([ticker.lower(), company_name.lower(), first]) if needle]


class RssAdapter:
    name = "rss_adapter"

    def __init__(
        self,
        *,
        ticker: str,
        company_name: str,
        trade_date: str,
        lookback_days: int,
        feeds: list[str] | None = None,
        rss_fetcher: RssFetcher | None = None,
    ) -> None:
        self.ticker = ticker
        self.company_name = company_name
        self.trade_date = trade_date
        self.lookback_days = lookback_days
        self.feeds = feeds if feeds is not None else DEFAULT_RSS_FEEDS.get(ticker.upper(), [])
        self.rss_fetcher = rss_fetcher or _default_fetch

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        if not self.feeds:
            return [], SourceAttempt(
                adapter=self.name,
                status="unavailable",
                limitations=["No whitelisted RSS feeds configured for this ticker."],
            )
        candidates: list[NewsCandidate] = []
        limitations: list[str] = []
        trade_date_dt = datetime.fromisoformat(self.trade_date).date()
        start_date = trade_date_dt - timedelta(days=self.lookback_days)
        needles = _company_needles(self.company_name, self.ticker)
        for feed_url in self.feeds:
            try:
                root = ET.fromstring(self.rss_fetcher(feed_url))
            except Exception as exc:  # noqa: BLE001 - adapter records source limitation.
                limitations.append(f"{feed_url}: {exc}")
                continue
            for item in root.findall(".//item"):
                title = _clean(item.findtext("title", ""))
                link = _clean(item.findtext("link", ""))
                description = _clean(item.findtext("description", ""))
                published = _published_date(item.findtext("pubDate", ""))
                if not title or not link or not published:
                    continue
                published_dt = datetime.fromisoformat(published).date()
                if published_dt > trade_date_dt or published_dt < start_date:
                    continue
                haystack = f"{title} {description}".lower()
                if not any(needle in haystack for needle in needles):
                    continue
                candidates.append(
                    NewsCandidate(
                        title=title,
                        source=self.company_name,
                        source_url=link,
                        published_at=published,
                        discovered_by=self.name,
                        source_type="company_ir",
                        raw_snippet=description,
                        tickers_detected=[self.ticker] if self.ticker.lower() in haystack else [],
                        company_names_detected=[self.company_name],
                    )
                )
        return candidates, SourceAttempt(
            adapter=self.name,
            status="available" if candidates else "unavailable",
            items_found=len(candidates),
            limitations=limitations,
            fallback_used=False,
        )
