from __future__ import annotations

import re
from typing import Any

try:
    from evidence_contracts import EvidenceLedgerEntry
    from sentiment_evidence_cards import build_sentiment_cards
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry
    from codex_tradingagents_skillkit.scripts.sentiment_evidence_cards import build_sentiment_cards

TOOL_NAME = "social_evidence_processing"
TOOL_VERSION = "0.1.0"
ROLE = "sentiment_analyst"

SOURCE_CONFIDENCE_BY_TOOL = {
    "fetch_stocktwits_messages": "ticker_specific_retail_platform",
    "stocktwits": "ticker_specific_retail_platform",
    "fetch_reddit_posts": "broad_social_discussion",
    "reddit": "broad_social_discussion",
}


def _label_for_line(line: str) -> str:
    lower = line.lower()
    if "bullish" in lower:
        return "bullish"
    if "bearish" in lower:
        return "bearish"
    return "neutral"


def _classify_line(ticker: str, line: str) -> str:
    lower = line.lower()
    ticker_lower = ticker.lower().replace(".ax", "")
    if not line.strip():
        return "irrelevant / spam / joke / low-information"
    if ticker_lower in lower or f"${ticker_lower}" in lower:
        return "directly ticker-relevant"
    if any(token in lower for token in ("market", "nasdaq", "s&p", "dow", "rates", "fed")):
        return "broad-market relevant"
    if re.search(r"\$[A-Za-z]{1,5}\b", line):
        return "cross-ticker / sector relevant"
    return "irrelevant / spam / joke / low-information"


def _source_status(tool_name: str, call: dict[str, Any]) -> tuple[str, list[str]]:
    status = str(call.get("status", "unknown")).lower()
    error = str(call.get("error", "") or "")
    output = str(call.get("output", "") or "")
    combined = f"{error} {output}".lower()
    if status == "ok":
        return "available", []
    limitations: list[str] = []
    if "reddit" in tool_name.lower():
        if "429" in combined or "rate limit" in combined or "too many requests" in combined:
            limitations.append("reddit_rate_limited")
            return "rate_limited", limitations
        if "credential" in combined or "unauthorized" in combined or "401" in combined:
            limitations.append("reddit_credentials_missing")
            return "unavailable", limitations
    limitations.append(error or "source unavailable")
    return "unavailable", limitations


def _source_confidence_category(tool_name: str) -> str:
    lower = tool_name.lower()
    for key, category in SOURCE_CONFIDENCE_BY_TOOL.items():
        if key in lower:
            return category
    return "anonymous_forum_or_comment"


def _ledger_entry(
    *,
    evidence_id: str,
    ticker: str,
    trade_date: str,
    source_url: str,
    retrieval_time: str,
    confidence: str,
    limitations: list[str],
    structured_output_path: str,
) -> dict[str, Any]:
    return EvidenceLedgerEntry(
        evidence_id=evidence_id,
        ticker=ticker,
        trade_date=trade_date,
        role=ROLE,
        tool_name=TOOL_NAME,
        tool_version=TOOL_VERSION,
        source_url=source_url,
        source_date=trade_date,
        retrieval_time=retrieval_time,
        as_of_validity={"valid_for_trade_date": True, "trade_date": trade_date},
        confidence=confidence,
        limitations=limitations,
        structured_output_path=structured_output_path,
        report_sections_using_it=["Social Evidence Processing Rules"],
    ).to_dict()


def build_social_evidence(
    *,
    ticker: str,
    trade_date: str,
    tool_calls: dict[str, dict[str, Any]],
    structured_output_path: str,
    retrieval_time: str,
) -> dict[str, Any]:
    sources: list[dict[str, Any]] = []
    ledger_entries: list[dict[str, Any]] = []
    sequence = 1
    card_sequence = 1
    social_cards: list[dict[str, Any]] = []
    total_usable = 0
    total_items = 0

    for tool_name, call in tool_calls.items():
        evidence_id = f"social:{ticker}:{trade_date}:{sequence:03d}"
        sequence += 1
        source_status, status_limitations = _source_status(tool_name, call)
        status = call.get("status", "unknown")
        output = str(call.get("output", ""))
        lines = [line.strip() for line in output.splitlines() if line.strip()] if status == "ok" else []
        cards, card_sequence = build_sentiment_cards(
            ticker=ticker,
            trade_date=trade_date,
            source=tool_name,
            lines=lines,
            start_index=card_sequence,
        )
        social_cards.extend(cards)
        classified = [
            {
                "text_excerpt": card["text_excerpt"],
                "classification": _classify_line(ticker, card["text_excerpt"]),
                "label": _label_for_line(card["text_excerpt"]),
                "ticker_relevance": card["ticker_relevance"],
                "candidate_sentiment_label": card["candidate_sentiment_label"],
                "reasoning_quality": card["reasoning_quality"],
                "influence_weight": card["influence_weight"],
            }
            for card in cards
        ]
        usable = [
            item
            for item in classified
            if item["ticker_relevance"] == "direct_company"
        ]
        total_items += len(lines)
        total_usable += len(usable)
        bullish = sum(1 for item in usable if item["candidate_sentiment_label"] == "bullish")
        bearish = sum(1 for item in usable if item["candidate_sentiment_label"] == "bearish")
        neutral = len(usable) - bullish - bearish
        limitations = list(status_limitations)
        if not usable:
            limitations.append("no_usable_ticker_relevant_items")
        low_quality = sum(1 for item in classified if item["reasoning_quality"] == "low")
        noisy_share = 1 - (len(usable) / len(classified)) if classified else 1
        reasoned_usable = [item for item in usable if item["reasoning_quality"] in {"medium", "high"}]
        confidence = "low" if source_status != "available" or not usable or not reasoned_usable or noisy_share > 0.5 or low_quality >= len(usable) else "medium"
        source_summary = {
            "evidence_id": evidence_id,
            "source": tool_name,
            "status": source_status,
            "source_confidence_category": _source_confidence_category(tool_name),
            "retail_only": tool_name in {"fetch_stocktwits_messages", "fetch_reddit_posts"},
            "items_reviewed": len(classified),
            "usable_ticker_relevant_items": len(usable),
            "bullish_count": bullish,
            "bearish_count": bearish,
            "neutral_count": neutral,
            "confidence": confidence,
            "limitations": limitations,
            "representative_items": usable[:3],
            "quality_weighted_balance": "pending_codex_interpretation",
            "final_sentiment_judgment": "pending_codex_interpretation",
        }
        sources.append(source_summary)
        ledger_entries.append(
            _ledger_entry(
                evidence_id=evidence_id,
                ticker=ticker,
                trade_date=trade_date,
                source_url=f"local://tool/{tool_name}",
                retrieval_time=retrieval_time,
                confidence=confidence,
                limitations=limitations,
                structured_output_path=structured_output_path,
            )
        )

    overall_limitations = []
    if total_usable == 0:
        overall_limitations.append("social coverage has no usable ticker-relevant items")
    elif total_usable < max(3, total_items // 3):
        overall_limitations.append("social coverage is noisy or sparse")

    return {
        "social_summary": {
            "ticker": ticker,
            "trade_date": trade_date,
            "total_items_reviewed": total_items,
            "usable_items": total_usable,
            "source_limitations": overall_limitations,
            "final_sentiment_judgment": "pending_codex_interpretation",
        },
        "social_cards": social_cards,
        "sources": sources,
        "ledger_entries": ledger_entries,
    }
