from __future__ import annotations

import re
from typing import Any

try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "social_evidence_processing"
TOOL_VERSION = "0.1.0"
ROLE = "sentiment_analyst"


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
    total_usable = 0
    total_items = 0

    for tool_name, call in tool_calls.items():
        evidence_id = f"social:{ticker}:{trade_date}:{sequence:03d}"
        sequence += 1
        status = call.get("status", "unknown")
        output = str(call.get("output", ""))
        lines = [line.strip() for line in output.splitlines() if line.strip()] if status == "ok" else []
        classified = [
            {
                "text_excerpt": line[:240],
                "classification": _classify_line(ticker, line),
                "label": _label_for_line(line),
            }
            for line in lines
        ]
        usable = [
            item
            for item in classified
            if item["classification"] == "directly ticker-relevant"
        ]
        total_items += len(classified)
        total_usable += len(usable)
        bullish = sum(1 for item in usable if item["label"] == "bullish")
        bearish = sum(1 for item in usable if item["label"] == "bearish")
        neutral = len(usable) - bullish - bearish
        limitations = []
        if status != "ok":
            limitations.append(str(call.get("error", "source unavailable")))
        if not usable:
            limitations.append("no_usable_ticker_relevant_items")
        noisy_share = 1 - (len(usable) / len(classified)) if classified else 1
        confidence = "low" if status != "ok" or not usable or noisy_share > 0.5 else "medium"
        source_summary = {
            "evidence_id": evidence_id,
            "source": tool_name,
            "status": "available" if status == "ok" else "unavailable",
            "items_reviewed": len(classified),
            "usable_ticker_relevant_items": len(usable),
            "bullish_count": bullish,
            "bearish_count": bearish,
            "neutral_count": neutral,
            "confidence": confidence,
            "limitations": limitations,
            "representative_items": usable[:3],
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
        "sources": sources,
        "ledger_entries": ledger_entries,
    }
