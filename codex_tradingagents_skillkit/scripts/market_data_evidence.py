from __future__ import annotations

import re
from typing import Any

try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "market_data_evidence"
TOOL_VERSION = "0.1.0"
ROLE = "market_analyst"

METRIC_PATTERNS = [
    ("latest_close", r"\bLatest\s+close\s*[:=]\s*\$?(-?\d+(?:\.\d+)?)", ["latest close", "price level"]),
    ("latest_close", r"\|\s*Close\s*\|\s*\$?(-?\d+(?:\.\d+)?)\s*\|", ["latest close", "price level"]),
    ("ema_10", r"\b10\s*EMA\s*[:=]\s*\$?(-?\d+(?:\.\d+)?)", ["10 EMA", "near-term momentum"]),
    ("ema_10", r"\|\s*close_10_ema\s*\|\s*\$?(-?\d+(?:\.\d+)?)\s*\|", ["10 EMA", "near-term momentum"]),
    ("sma_50", r"\b50\s*SMA\s*[:=]\s*\$?(-?\d+(?:\.\d+)?)", ["50 SMA", "intermediate trend"]),
    ("sma_50", r"\|\s*close_50_sma\s*\|\s*\$?(-?\d+(?:\.\d+)?)\s*\|", ["50 SMA", "intermediate trend"]),
    ("sma_200", r"\b200\s*SMA\s*[:=]\s*\$?(-?\d+(?:\.\d+)?)", ["200 SMA", "long-term trend"]),
    ("sma_200", r"\|\s*close_200_sma\s*\|\s*\$?(-?\d+(?:\.\d+)?)\s*\|", ["200 SMA", "long-term trend"]),
    ("rsi", r"\bRSI\s*[:=]\s*(-?\d+(?:\.\d+)?)", ["RSI", "momentum regime"]),
    ("rsi", r"\|\s*rsi\s*\|\s*(-?\d+(?:\.\d+)?)\s*\|", ["RSI", "momentum regime"]),
    ("macd", r"\bMACD\s*[:=]\s*(-?\d+(?:\.\d+)?)", ["MACD", "momentum regime"]),
    ("macd", r"\|\s*macd\s*\|\s*(-?\d+(?:\.\d+)?)\s*\|", ["MACD", "momentum regime"]),
    ("atr", r"\bATR\s*[:=]\s*(-?\d+(?:\.\d+)?)", ["ATR", "volatility regime"]),
    ("atr", r"\|\s*atr\s*\|\s*(-?\d+(?:\.\d+)?)\s*\|", ["ATR", "volatility regime"]),
    ("volume", r"\bVolume\s*[:=]\s*([0-9,]+(?:\.\d+)?)", ["volume", "participation"]),
    ("volume", r"\|\s*Volume\s*\|\s*([0-9,]+(?:\.\d+)?)\s*\|", ["volume", "participation"]),
]

COMPARISONS = {
    "ema_10": ("latest_close_vs_ema_10", ["price relative to 10 EMA", "near-term momentum"]),
    "sma_50": ("latest_close_vs_sma_50", ["price relative to 50 SMA", "intermediate trend"]),
    "sma_200": ("latest_close_vs_sma_200", ["price relative to 200 SMA", "long-term trend support/resistance"]),
}


def _parse_number(raw: str) -> float:
    return float(raw.replace(",", ""))


def _relation(left: float, right: float) -> str:
    if left > right:
        return "above"
    if left < right:
        return "below"
    return "equal"


def _ledger_entry(
    *,
    evidence_id: str,
    ticker: str,
    trade_date: str,
    source_date: str,
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
        source_date=source_date,
        retrieval_time=retrieval_time,
        as_of_validity={
            "valid_for_trade_date": True,
            "trade_date": trade_date,
        },
        confidence=confidence,
        limitations=limitations,
        structured_output_path=structured_output_path,
        report_sections_using_it=["Quantitative Regime / Tool Outputs"],
    ).to_dict()


def _source_url(tool_name: str) -> str:
    return f"local://tool/{tool_name}"


def _latest_trading_date(output: str, trade_date: str) -> str:
    match = re.search(r"Latest trading row used:\s*(\d{4}-\d{2}-\d{2})", output)
    return match.group(1) if match else trade_date


def build_market_data_evidence(
    *,
    ticker: str,
    trade_date: str,
    tool_calls: dict[str, dict[str, Any]],
    structured_output_path: str,
    retrieval_time: str,
) -> dict[str, list[dict[str, Any]]]:
    metric_observations: list[dict[str, Any]] = []
    ledger_entries: list[dict[str, Any]] = []
    values: dict[str, float] = {}
    value_source_dates: dict[str, str] = {}
    sequence = 1

    for tool_name, call in tool_calls.items():
        if call.get("status") == "error":
            evidence_id = f"market:{ticker}:{trade_date}:{sequence:03d}"
            sequence += 1
            error_text = str(call.get("error", "tool unavailable"))
            observation = {
                "evidence_id": evidence_id,
                "ticker": ticker,
                "trade_date": trade_date,
                "metric_name": tool_name,
                "status": "unavailable",
                "value": None,
                "tool_call": tool_name,
                "supports_claims": [],
                "confidence": "low",
                "limitations": ["tool_unavailable", error_text],
                "source_date": trade_date,
                "retrieval_time": retrieval_time,
                "as_of_validity": {
                    "valid_for_trade_date": True,
                    "trade_date": trade_date,
                    "source_date": trade_date,
                },
                "final_market_judgment": "pending_codex_interpretation",
            }
            metric_observations.append(observation)
            ledger_entries.append(
                _ledger_entry(
                    evidence_id=evidence_id,
                    ticker=ticker,
                    trade_date=trade_date,
                    source_url=_source_url(tool_name),
                    source_date=trade_date,
                    retrieval_time=retrieval_time,
                    confidence="low",
                    limitations=observation["limitations"],
                    structured_output_path=structured_output_path,
                )
            )
            continue

        if call.get("status") != "ok":
            continue

        output = str(call.get("output", ""))
        source_date = _latest_trading_date(output, trade_date)
        for metric_name, pattern, supports_claims in METRIC_PATTERNS:
            if metric_name in values:
                continue
            match = re.search(pattern, output, re.IGNORECASE)
            if not match:
                continue
            value = _parse_number(match.group(1))
            values[metric_name] = value
            value_source_dates[metric_name] = source_date
            evidence_id = f"market:{ticker}:{trade_date}:{sequence:03d}"
            sequence += 1
            observation = {
                "evidence_id": evidence_id,
                "ticker": ticker,
                "trade_date": trade_date,
                "metric_name": metric_name,
                "status": "available",
                "value": value,
                "tool_call": tool_name,
                "supports_claims": supports_claims,
                "confidence": "medium",
                "limitations": [],
                "source_date": source_date,
                "retrieval_time": retrieval_time,
                "as_of_validity": {
                    "valid_for_trade_date": source_date <= trade_date,
                    "trade_date": trade_date,
                    "source_date": source_date,
                },
                "final_market_judgment": "pending_codex_interpretation",
            }
            metric_observations.append(observation)
            ledger_entries.append(
                _ledger_entry(
                    evidence_id=evidence_id,
                    ticker=ticker,
                    trade_date=trade_date,
                    source_url=_source_url(tool_name),
                    source_date=source_date,
                    retrieval_time=retrieval_time,
                    confidence="medium",
                    limitations=[],
                    structured_output_path=structured_output_path,
                )
            )

    latest_close = values.get("latest_close")
    latest_close_source_date = value_source_dates.get("latest_close", trade_date)
    if latest_close is not None:
        for right_metric, (comparison_metric_name, supports_claims) in COMPARISONS.items():
            right_value = values.get(right_metric)
            if right_value is None:
                continue
            evidence_id = f"market:{ticker}:{trade_date}:{sequence:03d}"
            sequence += 1
            observation = {
                "evidence_id": evidence_id,
                "ticker": ticker,
                "trade_date": trade_date,
                "metric_name": comparison_metric_name,
                "status": "available",
                "value": None,
                "relation": _relation(latest_close, right_value),
                "comparison": {
                    "left_metric": "latest_close",
                    "left_value": latest_close,
                    "right_metric": right_metric,
                    "right_value": right_value,
                },
                "tool_call": TOOL_NAME,
                "supports_claims": supports_claims,
                "confidence": "medium",
                "limitations": [],
                "source_date": latest_close_source_date,
                "retrieval_time": retrieval_time,
                "as_of_validity": {
                    "valid_for_trade_date": latest_close_source_date <= trade_date,
                    "trade_date": trade_date,
                    "source_date": latest_close_source_date,
                },
                "final_market_judgment": "pending_codex_interpretation",
            }
            metric_observations.append(observation)
            ledger_entries.append(
                _ledger_entry(
                    evidence_id=evidence_id,
                    ticker=ticker,
                    trade_date=trade_date,
                    source_url=_source_url(TOOL_NAME),
                    source_date=latest_close_source_date,
                    retrieval_time=retrieval_time,
                    confidence="medium",
                    limitations=[],
                    structured_output_path=structured_output_path,
                )
            )

    return {
        "metric_observations": metric_observations,
        "ledger_entries": ledger_entries,
    }
