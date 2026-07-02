from __future__ import annotations

import hashlib
import re
from typing import Any

REASON_TERMS = {
    "because",
    "due",
    "demand",
    "earnings",
    "revenue",
    "margin",
    "guidance",
    "valuation",
    "cash",
    "growth",
    "azure",
    "services",
    "capex",
    "regulation",
}
MEME_TERMS = {"moon", "rocket", "lol", "joke", "spam", "yolo", "bagholder"}
EVENT_TOPICS = {
    "earnings": ("earnings", "revenue", "margin", "guidance"),
    "valuation": ("valuation", "multiple", "pe", "p/e"),
    "AI capex": ("ai", "azure", "capex", "data center", "datacenter"),
    "layoffs": ("layoff", "layoffs", "job cut", "job cuts", "headcount"),
    "product": ("product", "iphone", "windows", "copilot", "launch"),
    "regulation": ("regulation", "regulator", "antitrust", "sec", "asx"),
    "technical-price-only": ("breakout", "support", "resistance", "chart", "rsi"),
}

SOURCE_CONFIDENCE_CATEGORIES = {
    "sec": "official_company_or_exchange",
    "asx": "official_company_or_exchange",
    "company_ir": "official_company_or_exchange",
    "press_release": "official_company_or_exchange",
    "news_sentiment": "structured_news_sentiment_api",
    "newsapi": "structured_news_sentiment_api",
    "stocktwits": "ticker_specific_retail_platform",
    "fetch_stocktwits_messages": "ticker_specific_retail_platform",
    "reddit": "broad_social_discussion",
    "fetch_reddit_posts": "broad_social_discussion",
}


def normalize_social_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def item_hash(text: str) -> str:
    return hashlib.sha256(normalize_social_text(text).encode()).hexdigest()[:16]


def _cashtags(text: str) -> list[str]:
    return [match.upper() for match in re.findall(r"\$([A-Za-z][A-Za-z0-9.]{0,9})\b", text)]


def _platform_label(text: str) -> str:
    lower = text.lower()
    if "bullish" in lower:
        return "bullish"
    if "bearish" in lower:
        return "bearish"
    return "none"


def _ticker_relevance(ticker: str, text: str, cashtags: list[str]) -> str:
    ticker_root = ticker.upper().replace(".AX", "")
    text_lower = text.lower()
    if "no reddit posts found" in text_lower or "no posts found" in text_lower or "total: 0 messages" in text_lower:
        return "irrelevant"
    if ticker.upper() in cashtags or ticker_root in cashtags or f"${ticker_root.lower()}" in text_lower or ticker.lower() in text_lower:
        return "direct_company"
    if cashtags:
        return "cross_ticker"
    if any(term in text_lower for term in ("market", "nasdaq", "s&p", "dow", "rates", "fed")):
        return "broad_market"
    return "irrelevant"


def _reasoning_quality(text: str, meme_or_joke: bool) -> str:
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9.'-]*", text.lower())
    if meme_or_joke:
        return "low"
    reason_hits = sum(1 for word in words if word in REASON_TERMS)
    if reason_hits >= 2 and len(words) >= 10:
        return "high"
    if reason_hits >= 1 or "because" in words:
        return "medium"
    if len(words) < 5:
        return "low"
    return "low"


def _candidate_sentiment(platform_label: str, text: str) -> str:
    if platform_label in {"bullish", "bearish"}:
        return platform_label
    lower = text.lower()
    if any(word in lower for word in ("strong", "beat", "upside", "buy", "constructive")):
        return "bullish"
    if any(word in lower for word in ("weak", "miss", "risk", "sell", "downside")):
        return "bearish"
    return "neutral"


def _linked_event_type(text: str) -> str:
    lower = text.lower()
    for topic, terms in EVENT_TOPICS.items():
        if any(term in lower for term in terms):
            return topic
    return "none"


def _source_confidence_category(source: str) -> str:
    source_lower = source.lower()
    for key, category in SOURCE_CONFIDENCE_CATEGORIES.items():
        if key in source_lower:
            return category
    return "anonymous_forum_or_comment"


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return cleaned or "none"


def _event_ids(*, ticker: str, trade_date: str, linked_event_type: str) -> tuple[str, str]:
    topic = _slug(linked_event_type)
    return (
        f"event:{ticker.upper()}:{trade_date}:{topic}",
        f"reaction:{ticker.upper()}:{trade_date}:{topic}",
    )


def evaluate_social_item(*, ticker: str, trade_date: str, source: str, text: str, posted_at: str = "") -> dict[str, Any]:
    cashtags = _cashtags(text)
    platform_label = _platform_label(text)
    meme_or_joke = bool(any(term in text.lower() for term in MEME_TERMS) or "\U0001F680" in text)
    ticker_relevance = _ticker_relevance(ticker, text, cashtags)
    reasoning_quality = _reasoning_quality(text, meme_or_joke)
    linked_event_type = _linked_event_type(text)
    candidate_sentiment = _candidate_sentiment(platform_label, text)
    valid_for_trade_date = not posted_at or posted_at[:10] <= trade_date
    spam_or_bot_risk = "high" if "spam" in text.lower() else "medium" if meme_or_joke else "low"
    no_items_placeholder = "no reddit posts found" in text.lower() or "no posts found" in text.lower() or "total: 0 messages" in text.lower()
    event_or_topic_id, independence_group_id = _event_ids(
        ticker=ticker,
        trade_date=trade_date,
        linked_event_type=linked_event_type,
    )
    weight = 0.0
    if ticker_relevance == "direct_company":
        weight += 0.25
    elif ticker_relevance in {"sector_context", "cross_ticker"}:
        weight += 0.10
    if reasoning_quality == "high":
        weight += 0.35
    elif reasoning_quality == "medium":
        weight += 0.20
    else:
        weight += 0.05
    if meme_or_joke or spam_or_bot_risk == "high":
        weight *= 0.35
    if no_items_placeholder:
        weight = 0.0
    if not valid_for_trade_date:
        weight = 0.0
    return {
        "source": source,
        "posted_at": posted_at,
        "text_excerpt": text[:240],
        "ticker_relevance": ticker_relevance,
        "cashtags_detected": cashtags,
        "platform_label": platform_label,
        "candidate_sentiment_label": candidate_sentiment,
        "reasoning_quality": reasoning_quality,
        "event_linked": linked_event_type != "none",
        "linked_event_type": linked_event_type,
        "spam_or_bot_risk": spam_or_bot_risk,
        "meme_or_joke": meme_or_joke,
        "duplicate_or_near_duplicate": False,
        "influence_weight": round(weight, 2),
        "source_confidence_category": _source_confidence_category(source),
        "primary_role_owner": "sentiment_analyst",
        "event_or_topic_id": event_or_topic_id,
        "independence_group_id": independence_group_id,
        "allowed_secondary_roles": ["research_manager", "bear_researcher", "bull_researcher"],
        "secondary_use_purpose": "reaction_evidence",
        "as_of_validity": {"valid_for_trade_date": valid_for_trade_date},
        "limitations": (["no_items_placeholder"] if no_items_placeholder else []) + ([] if valid_for_trade_date else ["post_trade_date"]),
    }
