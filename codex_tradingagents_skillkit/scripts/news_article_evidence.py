from __future__ import annotations

import hashlib
import re
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "news_article_evidence"
TOOL_VERSION = "0.1.0"
TRACKING_QUERY_PREFIXES = ("utm_",)
TRACKING_QUERY_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}


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


def _full_text_status(candidate: dict[str, str]) -> str:
    full_text = str(candidate.get("full_text") or "").strip()
    return "full_text" if len(full_text) >= 40 else "snippet_only"


def _full_text_excerpt(candidate: dict[str, str], *, limit: int = 600) -> str:
    full_text = re.sub(r"\s+", " ", str(candidate.get("full_text") or "").strip())
    if len(full_text) <= limit:
        return full_text
    return full_text[:limit].rsplit(" ", 1)[0].strip()


def _confidence(full_text_status: str, limitations: list[str]) -> str:
    if "post_trade_date" in limitations:
        return "low"
    if full_text_status == "snippet_only":
        return "low"
    return "medium"


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
        published_date = str(candidate.get("published_date") or "")
        valid_for_trade_date = bool(published_date and published_date <= trade_date)
        limitations: list[str] = []
        source_url = _normalize_url(str(candidate.get("url") or ""))
        full_text_source = "candidate_full_text" if _full_text_status(candidate) == "full_text" else "unavailable"
        if full_text_source == "unavailable" and full_text_fetcher and source_url and valid_for_trade_date:
            try:
                fetched_full_text = str(full_text_fetcher(source_url) or "").strip()
            except Exception:
                fetched_full_text = ""
                limitations.append("full_text_retrieval_failed")
            if len(fetched_full_text) >= 40:
                candidate["full_text"] = fetched_full_text
                full_text_source = "url_fetch"
        full_text_status = _full_text_status(candidate)
        if full_text_status == "snippet_only":
            limitations.append("snippet_only")
        if not valid_for_trade_date:
            limitations.append("post_trade_date")
        confidence = _confidence(full_text_status, limitations)
        evidence_id = f"news:{ticker}:{trade_date}:{len(order) + 1:03d}"
        as_of_validity = {
            "valid_for_trade_date": valid_for_trade_date,
            "reason": (
                "source_date is on or before trade_date"
                if valid_for_trade_date
                else "source_date is after trade_date"
            ),
        }
        card: dict[str, Any] = {
            "evidence_id": evidence_id,
            "ticker": ticker,
            "trade_date": trade_date,
            "title": str(candidate.get("title") or "").strip(),
            "source": str(candidate.get("source") or "").strip(),
            "source_url": source_url,
            "source_date": published_date,
            "retrieval_time": retrieval_time,
            "full_text_status": full_text_status,
            "full_text_source": full_text_source,
            "full_text_excerpt": _full_text_excerpt(candidate) if full_text_status == "full_text" else "",
            "direct_company_relevance": "pending_codex_interpretation",
            "event_type": "pending_codex_interpretation",
            "key_facts": [],
            "novelty": "pending_codex_interpretation",
            "materiality": "pending_codex_interpretation",
            "reason": "pending_codex_interpretation",
            "confidence": confidence,
            "evidence_gap": "full text unavailable" if full_text_status == "snippet_only" else "",
            "limitations": limitations,
            "as_of_validity": as_of_validity,
            "duplicate_count": 1,
        }
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
