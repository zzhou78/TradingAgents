from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "stage_input_evidence"
TOOL_VERSION = "0.1.0"


def build_stage_input_evidence(
    *,
    ticker: str,
    trade_date: str,
    role: str,
    allowed_inputs: list[str],
    structured_output_path: str,
    retrieval_time: str,
) -> dict[str, list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    ledger_entries: list[dict[str, Any]] = []
    for index, input_path in enumerate(allowed_inputs, start=1):
        evidence_id = f"stage:{role}:{ticker}:{trade_date}:{index:03d}"
        exists = Path(input_path).exists()
        limitations = [] if exists else ["input_pending_or_missing_at_task_generation"]
        confidence = "medium" if exists else "low"
        record = {
            "evidence_id": evidence_id,
            "ticker": ticker,
            "trade_date": trade_date,
            "role": role,
            "input_path": input_path,
            "status": "available" if exists else "pending_or_missing",
            "supports_claims": ["upstream role evidence", "cross-role synthesis input"],
            "confidence": confidence,
            "limitations": limitations,
            "final_role_judgment": "pending_codex_interpretation",
        }
        records.append(record)
        ledger_entries.append(
            EvidenceLedgerEntry(
                evidence_id=evidence_id,
                ticker=ticker,
                trade_date=trade_date,
                role=role,
                tool_name=TOOL_NAME,
                tool_version=TOOL_VERSION,
                source_url=f"local://file/{input_path}",
                source_date=trade_date,
                retrieval_time=retrieval_time,
                as_of_validity={"valid_for_trade_date": True, "trade_date": trade_date},
                confidence=confidence,
                limitations=limitations,
                structured_output_path=structured_output_path,
                report_sections_using_it=["Tool Outputs Used"],
            ).to_dict()
        )
    return {"input_records": records, "ledger_entries": ledger_entries}
