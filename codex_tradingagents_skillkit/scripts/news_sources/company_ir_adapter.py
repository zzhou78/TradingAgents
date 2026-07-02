from __future__ import annotations

import html
import re
import urllib.request
from collections.abc import Callable
from urllib.parse import urljoin

from news_sources.base import NewsCandidate, SourceAttempt

HtmlFetcher = Callable[[str], str]


def _default_fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "CodexTradingAgentsNewsSources/0.1"})
    with urllib.request.urlopen(request, timeout=15) as response:  # noqa: S310 - user/official IR URLs.
        return response.read().decode("utf-8", errors="replace")


def _clean(raw: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))).strip()


def _published_date(page_html: str) -> str:
    match = re.search(r"datetime=['\"](\d{4}-\d{2}-\d{2})", page_html, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", page_html)
    if match:
        return match.group(1)
    return ""


def _company_needles(company_name: str, ticker: str) -> list[str]:
    needles = [ticker.lower(), company_name.lower()]
    first_word = re.split(r"\s+", company_name.strip())[0].lower() if company_name.strip() else ""
    if first_word and len(first_word) > 2:
        needles.append(first_word)
    return list(dict.fromkeys(needle for needle in needles if needle))


class CompanyIrAdapter:
    name = "company_ir_adapter"

    def __init__(
        self,
        *,
        ticker: str,
        company_name: str,
        trade_date: str,
        urls: list[str],
        html_fetcher: HtmlFetcher | None = None,
    ):
        self.ticker = ticker
        self.company_name = company_name
        self.trade_date = trade_date
        self.urls = urls
        self.html_fetcher = html_fetcher or _default_fetch

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        candidates: list[NewsCandidate] = []
        limitations: list[str] = []
        for page_url in self.urls:
            try:
                page_html = self.html_fetcher(page_url)
            except Exception as exc:  # noqa: BLE001 - source attempt should degrade cleanly.
                limitations.append(f"{page_url}: {exc}")
                continue
            source_date = _published_date(page_html)
            needles = _company_needles(self.company_name, self.ticker)
            for href, label in re.findall(r"(?is)<a[^>]+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", page_html):
                title = _clean(label)
                if not title:
                    continue
                haystack = title.lower()
                if not any(needle in haystack for needle in needles):
                    continue
                candidates.append(
                    NewsCandidate(
                        title=title,
                        source=self.company_name,
                        source_url=urljoin(page_url, href),
                        published_at=source_date,
                        discovered_by=self.name,
                        source_type="company_ir",
                        raw_snippet=title,
                        tickers_detected=[self.ticker] if self.ticker.lower() in haystack else [],
                        company_names_detected=[self.company_name],
                        retrieval_limitations=[] if source_date else ["source_date_unavailable"],
                    )
                )
        status = "available" if candidates else "unavailable"
        return candidates, SourceAttempt(
            adapter=self.name,
            status=status,
            items_found=len(candidates),
            limitations=limitations,
            fallback_used=False,
        )
