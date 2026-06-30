from __future__ import annotations

import re
from typing import Any

try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "fundamentals_statement_evidence"
TOOL_VERSION = "0.1.0"
ROLE = "fundamentals_analyst"

TOOL_SECTIONS = {
    "get_fundamentals": "company fundamentals packet",
    "get_income_statement": "income statement",
    "get_balance_sheet": "balance sheet",
    "get_cashflow": "cash flow statement",
}


def _supports_claims(tool_name: str, output: str) -> list[str]:
    lower = output.lower()
    claims = [TOOL_SECTIONS.get(tool_name, tool_name)]
    for label, pattern in {
        "revenue": r"revenue|sales",
        "net income": r"net income|earnings",
        "cash flow": r"cash flow|free cash flow|operating cash",
        "debt/liquidity": r"debt|cash|liquid",
        "valuation": r"pe|p/e|price/book|valuation",
        "profitability": r"margin|roe|roa|profit",
    }.items():
        if re.search(pattern, lower):
            claims.append(label)
    return list(dict.fromkeys(claims))


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
        report_sections_using_it=["Sector-Specific Metrics", "Financial Statement Evidence"],
    ).to_dict()


def build_fundamentals_evidence(
    *,
    ticker: str,
    trade_date: str,
    identity: dict[str, Any],
    tool_calls: dict[str, dict[str, Any]],
    structured_output_path: str,
    retrieval_time: str,
) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    ledger_entries: list[dict[str, Any]] = []
    sector = str(identity.get("sector", "unknown"))
    industry = str(identity.get("industry", "unknown"))
    sequence = 1

    for tool_name, call in tool_calls.items():
        evidence_id = f"fundamentals:{ticker}:{trade_date}:{sequence:03d}"
        sequence += 1
        status = call.get("status", "unknown")
        output = str(call.get("output", ""))
        limitations = [] if status == "ok" and output.strip() else ["tool_unavailable_or_empty"]
        confidence = "medium" if not limitations else "low"
        record = {
            "evidence_id": evidence_id,
            "ticker": ticker,
            "trade_date": trade_date,
            "source": tool_name,
            "section_name": TOOL_SECTIONS.get(tool_name, tool_name),
            "status": "available" if status == "ok" and output.strip() else "unavailable",
            "excerpt": output[:1000],
            "supports_claims": _supports_claims(tool_name, output) if output else [],
            "sector": sector,
            "industry": industry,
            "sector_specific_metric_expectations": _sector_metric_expectations(sector, industry),
            "confidence": confidence,
            "limitations": limitations,
            "final_fundamentals_judgment": "pending_codex_interpretation",
        }
        records.append(record)
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

    return {"statement_records": records, "ledger_entries": ledger_entries}


def _sector_metric_expectations(sector: str, industry: str) -> list[str]:
    sector_lower = sector.lower()
    blob = f"{sector} {industry}".lower()
    if "technology" in sector_lower or "software" in blob:
        return ["revenue growth", "gross margin", "R&D", "subscription mix", "cloud/AI exposure"]
    if "bank" in blob or "financial" in blob:
        return ["NIM", "CET1", "loan growth", "arrears", "impairment", "dividend", "ROE"]
    if any(token in blob for token in ("mine", "resource", "metal", "energy", "oil", "gas")):
        return ["production", "realised price", "unit costs", "reserves/resources", "capex", "commodity exposure"]
    if "health" in blob or "biotech" in blob or "pharma" in blob:
        return ["pipeline", "R&D", "regulatory milestones", "gross margin", "cash runway"]
    if "consumer" in blob or "retail" in blob:
        return ["same-store sales", "gross margin", "inventory", "store count", "consumer demand"]
    return ["sector-specific metrics unavailable; state evidence gap"]
