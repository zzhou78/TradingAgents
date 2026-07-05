from __future__ import annotations

from typing import Any

try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "financial_document_evidence"
TOOL_VERSION = "0.1.0"
ASX_METRIC_AUDIT_FIELDS = [
    "metric_value_status",
    "association_score",
    "association_reason",
    "clean_metric_value",
    "value_unit",
    "value_context",
    "period_reference",
    "comparison_reference",
    "supporting_sentence",
    "comparison_basis",
    "direction",
    "confidence_reason",
    "table_title",
    "row_label",
    "column_label",
    "source_page",
    "current_period_value",
    "prior_period_value",
    "variance_value",
    "variance_percent",
]


def _filing_date(source: dict[str, Any], section: dict[str, Any] | None = None) -> str:
    section = section or {}
    return str(
        section.get("filing_date")
        or source.get("filing_date")
        or source.get("announcement_date")
        or source.get("lodgement_date")
        or ""
    )


def _source_url(source: dict[str, Any], section: dict[str, Any] | None = None) -> str:
    section = section or {}
    return str(section.get("url") or source.get("url") or "")


def _confidence(status: str, excerpt: str) -> str:
    return "medium" if status == "available" and excerpt else "low"


def _limitations(status: str, section_kind: str, source: dict[str, Any]) -> list[str]:
    limitations: list[str] = []
    if status != "available":
        limitations.append("section_unavailable")
    if source.get("status") in {"unavailable", "error"}:
        limitations.append("source_unavailable")
    if section_kind == "8k_cover_page":
        limitations.append("cover_page_only")
    if section_kind == "exhibit_99_1" and status != "available":
        limitations.append("exhibit_unavailable")
    return limitations


def _as_of_validity(source_date: str, trade_date: str) -> dict[str, Any]:
    valid = bool(source_date and source_date <= trade_date)
    return {
        "valid_for_trade_date": valid,
        "reason": "source_date is on or before trade_date" if valid else "source_date is after trade_date or missing",
    }


def _record(
    *,
    evidence_id: str,
    ticker: str,
    trade_date: str,
    source: dict[str, Any],
    section: dict[str, Any],
    section_kind: str,
    section_name: str,
    retrieval_time: str,
) -> dict[str, Any]:
    status = str(section.get("status") or source.get("status") or "unavailable")
    excerpt = str(section.get("excerpt") or "")
    source_date = _filing_date(source, section)
    evidence_gap = (
        str(section.get("unavailable_reason") or section.get("reason") or source.get("reason") or "")
        if status != "available"
        else ""
    )
    limitations = _limitations(status, section_kind, source)
    record = {
        "evidence_id": evidence_id,
        "ticker": ticker,
        "trade_date": trade_date,
        "source_type": str(section.get("source_type") or source.get("source_type") or "unknown"),
        "section_name": section_name,
        "section_kind": section_kind,
        "metric_name": str(section.get("metric_name") or ""),
        "metric_label": str(section.get("metric_label") or ""),
        "sector": str(section.get("sector") or source.get("asx_sector") or ""),
        "status": status,
        "filing_date": source_date,
        "source_date": source_date,
        "url": _source_url(source, section),
        "excerpt": excerpt,
        "supports_claims": list(section.get("supports_claims") or []),
        "evidence_gap": evidence_gap,
        "confidence": str(section.get("metric_confidence") or _confidence(status, excerpt)),
        "limitations": limitations,
        "as_of_validity": _as_of_validity(source_date, trade_date),
        "retrieval_time": retrieval_time,
        "final_financial_judgment": "pending_codex_interpretation",
    }
    for field in ASX_METRIC_AUDIT_FIELDS:
        if field in section:
            record[field] = section[field]
    return record


def _source_unavailable_record(
    *,
    evidence_id: str,
    ticker: str,
    trade_date: str,
    source: dict[str, Any],
    retrieval_time: str,
) -> dict[str, Any]:
    source_type = str(source.get("source_type") or "unknown")
    section = {
        "status": source.get("status", "unavailable"),
        "source_type": source_type,
        "filing_date": _filing_date(source),
        "url": source.get("url", ""),
        "excerpt": source.get("excerpt", ""),
        "supports_claims": [],
        "reason": source.get("reason", "Source was unavailable."),
    }
    return _record(
        evidence_id=evidence_id,
        ticker=ticker,
        trade_date=trade_date,
        source=source,
        section=section,
        section_kind=source_type,
        section_name=str(source.get("source_name") or source_type),
        retrieval_time=retrieval_time,
    )


def _section_records_from_source(
    *,
    ticker: str,
    trade_date: str,
    source: dict[str, Any],
    retrieval_time: str,
    next_index: int,
) -> tuple[list[dict[str, Any]], int]:
    records: list[dict[str, Any]] = []

    for section in [*source.get("sections", []), *source.get("extracted_sections", [])]:
        evidence_id = f"financial:{ticker}:{trade_date}:{next_index:03d}"
        records.append(
            _record(
                evidence_id=evidence_id,
                ticker=ticker,
                trade_date=trade_date,
                source=source,
                section=section,
                section_kind=str(section.get("section_type") or section.get("section_name") or "section"),
                section_name=str(section.get("section_name") or section.get("source_section") or "section"),
                retrieval_time=retrieval_time,
            )
        )
        next_index += 1

    cover = source.get("cover_page", {})
    if cover:
        evidence_id = f"financial:{ticker}:{trade_date}:{next_index:03d}"
        records.append(
            _record(
                evidence_id=evidence_id,
                ticker=ticker,
                trade_date=trade_date,
                source=source,
                section=cover,
                section_kind="8k_cover_page",
                section_name="8-K cover page",
                retrieval_time=retrieval_time,
            )
        )
        next_index += 1

    exhibit = source.get("exhibit_99_1", {})
    if exhibit:
        evidence_id = f"financial:{ticker}:{trade_date}:{next_index:03d}"
        records.append(
            _record(
                evidence_id=evidence_id,
                ticker=ticker,
                trade_date=trade_date,
                source=source,
                section=exhibit,
                section_kind="exhibit_99_1",
                section_name=str(exhibit.get("exhibit_name") or "Exhibit 99.1"),
                retrieval_time=retrieval_time,
            )
        )
        next_index += 1

    if not records and source.get("status") in {"unavailable", "error"}:
        evidence_id = f"financial:{ticker}:{trade_date}:{next_index:03d}"
        records.append(
            _source_unavailable_record(
                evidence_id=evidence_id,
                ticker=ticker,
                trade_date=trade_date,
                source=source,
                retrieval_time=retrieval_time,
            )
        )
        next_index += 1

    return records, next_index


def build_financial_document_evidence(
    *,
    ticker: str,
    trade_date: str,
    packet: dict[str, Any],
    structured_output_path: str,
    retrieval_time: str,
) -> dict[str, list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    next_index = 1
    for source in packet.get("sources", []):
        source_records, next_index = _section_records_from_source(
            ticker=ticker,
            trade_date=trade_date,
            source=source,
            retrieval_time=retrieval_time,
            next_index=next_index,
        )
        records.extend(source_records)

    ledger_entries = [
        EvidenceLedgerEntry(
            evidence_id=str(record["evidence_id"]),
            ticker=ticker,
            trade_date=trade_date,
            role="financial_report_analyst",
            tool_name=TOOL_NAME,
            tool_version=TOOL_VERSION,
            source_url=str(record["url"]),
            source_date=str(record["source_date"]),
            retrieval_time=retrieval_time,
            as_of_validity=dict(record["as_of_validity"]),
            confidence=str(record["confidence"]),
            limitations=list(record["limitations"]),
            structured_output_path=structured_output_path,
            report_sections_using_it=["Financial Report Analyst"],
        ).to_dict()
        for record in records
    ]
    return {"section_records": records, "ledger_entries": ledger_entries}
