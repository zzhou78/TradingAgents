from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

REQUIRED_EVIDENCE_LEDGER_FIELDS = [
    "evidence_id",
    "ticker",
    "trade_date",
    "role",
    "tool_name",
    "tool_version",
    "source_url",
    "source_date",
    "retrieval_time",
    "as_of_validity",
    "confidence",
    "limitations",
    "structured_output_path",
    "report_sections_using_it",
]


@dataclass(frozen=True)
class EvidenceLedgerEntry:
    evidence_id: str
    ticker: str
    trade_date: str
    role: str
    tool_name: str
    tool_version: str
    source_url: str
    source_date: str
    retrieval_time: str
    as_of_validity: dict[str, Any]
    confidence: str
    limitations: list[str]
    structured_output_path: str
    report_sections_using_it: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RoleExecutionContract:
    role: str
    allowed_inputs: list[str]
    forbidden_inputs: list[str]
    allowed_memory: list[str]
    forbidden_memory: list[str]
    required_tools: list[str]
    optional_tools: list[str]
    required_output_sections: list[str]
    required_evidence_citations: list[str]
    quality_gate: str
    memory_update_schema: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def validate_evidence_ledger_entry(payload: dict[str, Any]) -> dict[str, Any]:
    for field in REQUIRED_EVIDENCE_LEDGER_FIELDS:
        if field not in payload:
            raise ValueError(f"missing required evidence ledger field: {field}")
    if not isinstance(payload["as_of_validity"], dict):
        raise ValueError("as_of_validity must be an object")
    if "valid_for_trade_date" not in payload["as_of_validity"]:
        raise ValueError("as_of_validity.valid_for_trade_date is required")
    if payload["confidence"] not in {"high", "medium", "low"}:
        raise ValueError("confidence must be high, medium, or low")
    if not isinstance(payload["limitations"], list):
        raise ValueError("limitations must be a list")
    if not isinstance(payload["report_sections_using_it"], list):
        raise ValueError("report_sections_using_it must be a list")
    return payload


def write_jsonl(path: Path, entries: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(validate_evidence_ledger_entry(entry), sort_keys=True) for entry in entries]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
