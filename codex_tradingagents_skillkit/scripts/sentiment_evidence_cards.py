from __future__ import annotations

from typing import Any

try:
    from sentiment_item_quality import evaluate_social_item, item_hash
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.sentiment_item_quality import (
        evaluate_social_item,
        item_hash,
    )


def build_sentiment_cards(
    *,
    ticker: str,
    trade_date: str,
    source: str,
    lines: list[str],
    start_index: int = 1,
) -> tuple[list[dict[str, Any]], int]:
    cards: list[dict[str, Any]] = []
    seen: dict[str, dict[str, Any]] = {}
    sequence = start_index
    for line in lines:
        key = item_hash(line)
        if key in seen:
            seen[key]["duplicate_or_near_duplicate"] = True
            continue
        card = evaluate_social_item(
            ticker=ticker,
            trade_date=trade_date,
            source=source,
            text=line,
        )
        card["evidence_id"] = f"social:{ticker}:{trade_date}:item:{sequence:04d}"
        sequence += 1
        seen[key] = card
        cards.append(card)
    return cards, sequence


def build_sentiment_cards_from_candidates(
    *,
    ticker: str,
    trade_date: str,
    candidates: list[Any],
    start_index: int = 1,
) -> tuple[list[dict[str, Any]], int]:
    cards: list[dict[str, Any]] = []
    seen: dict[str, dict[str, Any]] = {}
    sequence = start_index
    for candidate in candidates:
        text = str(getattr(candidate, "text", "") or "")
        if not text.strip():
            continue
        key = item_hash(text)
        if key in seen:
            seen[key]["duplicate_or_near_duplicate"] = True
            continue
        source = str(getattr(candidate, "source", "unknown") or "unknown")
        card = evaluate_social_item(
            ticker=ticker,
            trade_date=trade_date,
            source=source,
            text=text,
            posted_at=str(getattr(candidate, "posted_at", "") or ""),
        )
        platform_label = str(getattr(candidate, "platform_label", "") or "")
        if platform_label and platform_label != "none":
            card["platform_label"] = platform_label
        cashtags = getattr(candidate, "cashtags_detected", None)
        if cashtags:
            card["cashtags_detected"] = list(cashtags)
        card["source_url"] = str(getattr(candidate, "source_url", "") or "")
        card["author_id_hash"] = str(getattr(candidate, "author_id_hash", "") or "")
        card["author_metadata_available"] = bool(getattr(candidate, "author_metadata_available", False))
        card["reply_count"] = getattr(candidate, "reply_count", None)
        card["like_count"] = getattr(candidate, "like_count", None)
        card["repost_count"] = getattr(candidate, "repost_count", None)
        retrieval_limitations = list(getattr(candidate, "retrieval_limitations", []) or [])
        if retrieval_limitations:
            card["limitations"] = [*card.get("limitations", []), *retrieval_limitations]
        card["evidence_id"] = f"social:{ticker}:{trade_date}:item:{sequence:04d}"
        sequence += 1
        seen[key] = card
        cards.append(card)
    return cards, sequence
