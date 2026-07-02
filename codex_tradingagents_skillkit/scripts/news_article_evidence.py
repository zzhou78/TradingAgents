from __future__ import annotations

import hashlib
import re
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

try:
    from evidence_contracts import EvidenceLedgerEntry
    from news_article_cards import build_article_card
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry
    from codex_tradingagents_skillkit.scripts.news_article_cards import build_article_card

TOOL_NAME = "news_article_evidence"
TOOL_VERSION = "0.1.0"
TRACKING_QUERY_PREFIXES = ("utm_",)
TRACKING_QUERY_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
COMMON_COMPANY_NAMES = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
}


def _normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key not in TRACKING_QUERY_KEYS and not key.startswith(TRACKING_QUERY_PREFIXES)
    ]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), ""))


def _fingerprint(candidate: dict[str, str]) -> str:
    normalized_url = _normalize_url(str(candidate.get("url", "")))
    title = re.sub(r"\s+", " ", str(candidate.get("title", "")).strip().lower())
    return hashlib.sha256(f"{normalized_url}|{title}".encode()).hexdigest()[:16]


def build_news_evidence(
    *,
    ticker: str,
    trade_date: str,
    candidates: list[dict[str, str]],
    structured_output_path: str,
    retrieval_time: str,
    full_text_fetcher: Callable[[str], str] | None = None,
) -> dict[str, list[dict[str, Any]]]:
    seen: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    for candidate in candidates:
        key = _fingerprint(candidate)
        if key in seen:
            seen[key]["duplicate_count"] = int(seen[key]["duplicate_count"]) + 1
            continue
        candidate = dict(candidate)
        source_url = _normalize_url(str(candidate.get("url") or ""))
        if not source_url:
            source_url = _normalize_url(str(candidate.get("source_url") or ""))
        evidence_id = f"news:{ticker}:{trade_date}:{len(order) + 1:03d}"
        company_name = str(candidate.get("company_name") or COMMON_COMPANY_NAMES.get(ticker.upper()) or ticker)
        card = build_article_card(
            ticker=ticker,
            company_name=company_name,
            trade_date=trade_date,
            candidate=candidate,
            evidence_id=evidence_id,
            retrieval_time=retrieval_time,
            source_url=source_url,
            full_text_fetcher=full_text_fetcher,
        )
        seen[key] = card
        order.append(key)

    article_cards = [seen[key] for key in order]
    ledger_entries = [
        EvidenceLedgerEntry(
            evidence_id=str(card["evidence_id"]),
            ticker=ticker,
            trade_date=trade_date,
            role="news_analyst",
            tool_name=TOOL_NAME,
            tool_version=TOOL_VERSION,
            source_url=str(card["source_url"]),
            source_date=str(card["source_date"]),
            retrieval_time=retrieval_time,
            as_of_validity=dict(card["as_of_validity"]),
            confidence=str(card["confidence"]),
            limitations=list(card["limitations"]),
            structured_output_path=structured_output_path,
            report_sections_using_it=["News Analyst"],
        ).to_dict()
        for card in article_cards
    ]
    return {"article_cards": article_cards, "ledger_entries": ledger_entries}
