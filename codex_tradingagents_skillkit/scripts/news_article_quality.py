from __future__ import annotations

import re
from difflib import SequenceMatcher
from typing import Any

ERROR_PATTERNS = [
    r"oops[, ]+something went wrong",
    r"\b404\b",
    r"\bpage not found\b",
    r"\baccess denied\b",
    r"\btemporarily unavailable\b",
]
PAYWALL_PATTERNS = [
    r"\bsubscribe\b",
    r"\blog in\b",
    r"\bsign in\b",
    r"\bpaywall\b",
    r"\bcookies?\b",
    r"\bconsent\b",
]
VIDEO_PATTERNS = [
    r"\bwatch the video\b",
    r"\bvideo\b",
    r"\btranscript\b",
]
BOILERPLATE_PATTERNS = [
    r"\bprivacy policy\b",
    r"\bterms of use\b",
    r"\ball rights reserved\b",
    r"\badvertisement\b",
]


def _words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9.'-]*", text)


def _sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"[.!?]+", text) if part.strip()]


def _has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def _title_similarity(title: str, text: str) -> float:
    title = re.sub(r"\s+", " ", title.lower()).strip()
    if not title or not text:
        return 0.0
    body_start = re.sub(r"\s+", " ", text.lower()).strip()[: max(80, len(title) * 2)]
    return round(SequenceMatcher(None, title, body_start).ratio(), 2)


def _entity_hits(text: str, *, company_name: str, ticker: str) -> list[str]:
    hits: list[str] = []
    if company_name and re.search(rf"\b{re.escape(company_name)}\b", text, re.IGNORECASE):
        hits.append(company_name)
    if ticker and (re.search(rf"\b{re.escape(ticker)}\b", text, re.IGNORECASE) or hits):
        hits.append(ticker)
    return hits


def _event_fact_count(text: str) -> int:
    count = 0
    count += len(re.findall(r"\b\d+(?:\.\d+)?\s*(?:%|percent|billion|million|bn|mn)\b", text, re.IGNORECASE))
    count += len(re.findall(r"\b(?:said|announced|reported|filed|expects|plans|warned|confirmed)\b", text, re.IGNORECASE))
    count += len(re.findall(r"\b20\d{2}\b", text))
    return min(count, 10)


def _status_from_score(score: int, *, text: str, flags: list[str], word_count: int) -> str:
    if "error_page" in flags:
        return "error_page"
    if "blocked_or_paywalled" in flags:
        return "blocked_or_paywalled"
    if "video_without_transcript" in flags:
        return "video_without_transcript"
    if not text:
        return "metadata_only"
    if word_count < 20:
        return "snippet_only"
    if score >= 80:
        return "full_text_verified"
    if score >= 50:
        return "partial_text"
    if score >= 20:
        return "snippet_only"
    return "invalid_or_irrelevant"


def evaluate_article_quality(
    *,
    title: str,
    text: str,
    source_date: str,
    trade_date: str,
    company_name: str,
    ticker: str,
    fetch_status: str = "ok",
    http_status: int | None = None,
    content_type: str = "text/html",
    extraction_method: str = "",
) -> dict[str, Any]:
    normalized_text = re.sub(r"\s+", " ", text or "").strip()
    lower_text = normalized_text.lower()
    words = _words(normalized_text)
    sentences = _sentences(normalized_text)
    flags: list[str] = []

    if fetch_status != "ok":
        flags.append("fetch_failed")
    if http_status and http_status >= 400:
        flags.append("error_page")
    if _has_any(lower_text, ERROR_PATTERNS):
        flags.append("error_page")
    if _has_any(lower_text, PAYWALL_PATTERNS) and len(words) < 80:
        flags.append("blocked_or_paywalled")
    if "video" in lower_text and "transcript" in lower_text and re.search(r"\bno transcript\b", lower_text):
        flags.append("video_without_transcript")
    if _has_any(lower_text, BOILERPLATE_PATTERNS):
        flags.append("boilerplate")

    valid_for_trade_date = bool(source_date and source_date <= trade_date)
    if not valid_for_trade_date:
        flags.append("post_trade_date")

    company_entity_hits = _entity_hits(normalized_text, company_name=company_name, ticker=ticker)
    if not company_entity_hits:
        flags.append("no_company_entity_match")

    word_count = len(words)
    sentence_count = len(sentences)
    title_similarity = _title_similarity(title, normalized_text)
    event_fact_count = _event_fact_count(normalized_text)

    score = 0
    if fetch_status == "ok":
        score += 10
    if not http_status or http_status < 400:
        score += 10
    if "html" in content_type.lower() or not content_type:
        score += 5
    if word_count >= 80:
        score += 25
    elif word_count >= 20:
        score += 20
    elif word_count >= 12:
        score += 12
    elif word_count >= 8:
        score += 5
    if sentence_count >= 3:
        score += 15
    elif sentence_count >= 2:
        score += 8
    if source_date:
        score += 5
    if valid_for_trade_date:
        score += 5
    if company_entity_hits:
        score += 15
    if event_fact_count >= 2:
        score += 10
    elif event_fact_count == 1:
        score += 5
    if title_similarity >= 0.45:
        score += 5

    if "error_page" in flags:
        score = min(score, 10)
    if "blocked_or_paywalled" in flags:
        score = min(score, 18)
    if "video_without_transcript" in flags:
        score = min(score, 18)
    if "no_company_entity_match" in flags:
        score = min(score, 55)
    if "boilerplate" in flags:
        score = max(0, score - 15)
    score = max(0, min(100, score))
    text_status = _status_from_score(score, text=normalized_text, flags=flags, word_count=word_count)
    return {
        "text_status": text_status,
        "content_quality_score": score,
        "quality_flags": flags,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "title_similarity": title_similarity,
        "company_entity_hits": company_entity_hits,
        "event_fact_count": event_fact_count,
        "as_of_validity": {
            "valid_for_trade_date": valid_for_trade_date,
            "reason": "source_date is on or before trade_date" if valid_for_trade_date else "source_date is after trade_date",
        },
        "materiality_readiness": "ready_for_codex_interpretation"
        if text_status in {"full_text_verified", "partial_text"} and valid_for_trade_date
        else "limited_or_not_ready_for_codex_interpretation",
        "extraction_method": extraction_method,
    }
