from __future__ import annotations

import re
from collections.abc import Callable
from typing import Any

try:
    from news_article_quality import evaluate_article_quality
    from news_article_retrieval import extract_article_text_from_html
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.news_article_quality import evaluate_article_quality
    from codex_tradingagents_skillkit.scripts.news_article_retrieval import (
        extract_article_text_from_html,
    )


def _excerpt(text: str, *, limit: int = 600) -> str:
    normalized = re.sub(r"\s+", " ", text or "").strip()
    if len(normalized) <= limit:
        return normalized
    return normalized[:limit].rsplit(" ", 1)[0].strip()


def _legacy_full_text_status(text_status: str) -> str:
    return "full_text" if text_status in {"full_text_verified", "partial_text"} else "snippet_only"


def _confidence(text_status: str, limitations: list[str]) -> str:
    if "post_trade_date" in limitations:
        return "low"
    if text_status == "full_text_verified":
        return "medium"
    if text_status == "partial_text":
        return "medium"
    return "low"


def _fetch_candidate_text(
    *,
    candidate: dict[str, Any],
    source_url: str,
    valid_for_trade_date: bool,
    full_text_fetcher: Callable[[str], str] | None,
    limitations: list[str],
) -> tuple[str, str, str, str, int | None, str, str]:
    candidate_text = str(candidate.get("full_text") or "").strip()
    if len(candidate_text) >= 40:
        return candidate_text, "candidate_full_text", "candidate_full_text", "ok", None, source_url, ""

    if full_text_fetcher and source_url and valid_for_trade_date:
        try:
            fetched = str(full_text_fetcher(source_url) or "").strip()
        except Exception:
            limitations.append("full_text_retrieval_failed")
            fetched = ""
        if fetched:
            if "<html" in fetched.lower() or "<article" in fetched.lower() or "<main" in fetched.lower():
                retrieval = extract_article_text_from_html(fetched, title=str(candidate.get("title") or ""), final_url=source_url)
                return (
                    retrieval.text,
                    "url_fetch",
                    retrieval.extraction_method,
                    retrieval.fetch_status,
                    retrieval.http_status,
                    retrieval.final_url or source_url,
                    retrieval.content_type,
                )
            return fetched, "url_fetch", "url_fetch", "ok", None, source_url, ""

    snippet = str(candidate.get("snippet") or candidate.get("raw_snippet") or "").strip()
    return snippet, "unavailable", "candidate_snippet", "ok", None, source_url, ""


def build_article_card(
    *,
    ticker: str,
    company_name: str,
    trade_date: str,
    candidate: dict[str, Any],
    evidence_id: str,
    retrieval_time: str,
    source_url: str,
    full_text_fetcher: Callable[[str], str] | None = None,
) -> dict[str, Any]:
    title = str(candidate.get("title") or "").strip()
    source_date = str(candidate.get("published_date") or candidate.get("published_at") or "")[:10]
    valid_for_trade_date = bool(source_date and source_date <= trade_date)
    limitations = list(candidate.get("retrieval_limitations") or [])
    text, full_text_source, extraction_method, fetch_status, http_status, final_url, content_type = _fetch_candidate_text(
        candidate=candidate,
        source_url=source_url,
        valid_for_trade_date=valid_for_trade_date,
        full_text_fetcher=full_text_fetcher,
        limitations=limitations,
    )
    quality = evaluate_article_quality(
        title=title,
        text=text,
        source_date=source_date,
        trade_date=trade_date,
        company_name=company_name,
        ticker=ticker,
        fetch_status=fetch_status,
        http_status=http_status,
        content_type=content_type or "text/plain",
        extraction_method=extraction_method,
    )
    text_status = str(quality["text_status"])
    if (
        text_status == "snippet_only"
        and full_text_source in {"candidate_full_text", "url_fetch"}
        and len(text) >= 40
        and not any(flag in quality["quality_flags"] for flag in {"error_page", "blocked_or_paywalled", "video_without_transcript"})
    ):
        text_status = "partial_text"
        quality["content_quality_score"] = max(int(quality["content_quality_score"]), 50)
    legacy_status = _legacy_full_text_status(text_status)
    for flag in quality["quality_flags"]:
        if flag not in limitations:
            limitations.append(flag)
    if legacy_status == "snippet_only" and "snippet_only" not in limitations:
        limitations.append("snippet_only")

    confidence = _confidence(text_status, limitations)
    evidence_gap = "" if legacy_status == "full_text" else "full text unavailable or not review-grade"
    return {
        "evidence_id": evidence_id,
        "ticker": ticker,
        "trade_date": trade_date,
        "company_name": company_name,
        "title": title,
        "source": str(candidate.get("source") or "").strip(),
        "source_url": source_url,
        "source_date": source_date,
        "discovered_by": str(candidate.get("discovered_by") or ""),
        "retrieval_time": retrieval_time,
        "fetch_status": fetch_status,
        "http_status": http_status,
        "final_url": final_url,
        "content_type": content_type or "text/plain",
        "extraction_method": extraction_method,
        "text_status": text_status,
        "content_quality_score": quality["content_quality_score"],
        "quality_flags": quality["quality_flags"],
        "word_count": quality["word_count"],
        "sentence_count": quality["sentence_count"],
        "title_similarity": quality["title_similarity"],
        "company_entity_hits": quality["company_entity_hits"],
        "event_fact_count": quality["event_fact_count"],
        "key_facts_for_codex": [],
        "full_text_status": legacy_status,
        "full_text_source": full_text_source,
        "full_text_excerpt": _excerpt(text) if legacy_status == "full_text" else "",
        "direct_company_relevance": "pending_codex_interpretation",
        "event_type": "pending_codex_interpretation",
        "key_facts": [],
        "novelty": "pending_codex_interpretation",
        "materiality": "pending_codex_interpretation",
        "reason": "pending_codex_interpretation",
        "confidence": confidence,
        "evidence_gap": evidence_gap,
        "limitations": limitations,
        "as_of_validity": quality["as_of_validity"],
        "materiality_readiness": quality["materiality_readiness"],
        "duplicate_count": 1,
    }
