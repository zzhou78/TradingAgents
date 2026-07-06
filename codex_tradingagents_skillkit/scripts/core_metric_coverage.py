from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ACCEPTED_ASSOCIATION_THRESHOLD = 80
ACCEPTED_TABLE_MAPPING_THRESHOLD = 80
ELIGIBLE_ASX_SOURCE_QUALITY_TIERS = {
    "tier_1_asx_lodged_pdf",
    "tier_2_company_results_pdf",
    "tier_3_company_annual_report_pdf",
}
ASX_SECTOR_BY_CODE = {
    "BHP": "miners",
    "CBA": "banks",
    "CSL": "healthcare",
    "MPL": "health_insurers",
    "WOW": "retailers",
}

CORE_METRIC_PROFILES: dict[str, dict[str, tuple[str, ...]]] = {
    "banks": {
        "net_interest_margin": ("net_interest_margin", "nim"),
        "cet1": ("cet1", "cet1_ratio", "cet1_capital"),
        "loan_growth": ("loan_growth", "lending_growth"),
        "arrears": ("arrears",),
        "impairment": ("impairment", "loan_impairment", "credit_impairment"),
        "roe": ("roe", "return_on_equity"),
        "dividend": ("dividend", "dividends"),
    },
    "miners": {
        "production": ("production",),
        "realised_price": ("realised_price", "realized_price"),
        "unit_cost_aisc": ("unit_cost_aisc", "aisc", "unit_cost"),
        "capex": ("capex", "capital_expenditure"),
        "commodity_exposure": ("commodity_exposure", "commodity_mix"),
        "reserves_resources": ("reserves_resources", "reserves", "resources"),
    },
    "healthcare": {
        "segment_revenue": ("segment_revenue", "segment_sales"),
        "margins": ("margins", "margin", "ebit_margin"),
        "r_and_d": ("r_and_d", "research_and_development", "r&d"),
        "plasma_collections": ("plasma_collections", "plasma_collection"),
        "debt": ("debt", "net_debt"),
        "guidance": ("guidance", "outlook"),
    },
    "health_insurers": {
        "premium_growth": ("premium_growth", "premiums_growth"),
        "claims_ratio": ("claims_ratio",),
        "membership": ("membership", "members"),
        "capital_adequacy": ("capital_adequacy", "capital_position"),
        "operating_profit_or_margin": ("operating_profit_or_margin", "operating_profit", "operating_margin"),
    },
    "retailers": {
        "sales_growth": ("sales_growth",),
        "ebit_margin": ("ebit_margin", "margin"),
        "inventory_or_working_capital": (
            "inventory_or_working_capital",
            "inventory",
            "inventories",
            "working_capital",
            "net_investment_in_inventory",
        ),
        "capex": ("capex", "capital_expenditure"),
        "dividends": ("dividends", "dividend"),
        "comparable_sales_if_available": ("comparable_sales_if_available", "comparable_sales", "same_store_sales"),
    },
}

WEAK_STATUSES = {"metric_mentioned_only", "direction_extracted", "table_row_unparsed", "context_only"}
UNAVAILABLE_VALUES = {"", "unavailable", "none", "null", "n/a"}
DENSE_LABELS = [
    "inventories",
    "inventory",
    "trade payables",
    "receivables",
    "revenue",
    "sales",
    "ebit",
    "claims expense",
    "gross profit",
    "assets",
    "liabilities",
    "debt",
]


def _int_field(record: dict[str, Any], field: str) -> int:
    try:
        return int(float(str(record.get(field) or "0")))
    except ValueError:
        return 0


def _clean_value_present(record: dict[str, Any]) -> bool:
    return str(record.get("clean_metric_value") or "").strip().lower() not in UNAVAILABLE_VALUES


def _reason_present(record: dict[str, Any]) -> bool:
    return any(
        str(record.get(field) or "").strip()
        for field in (
            "unavailable_reason",
            "evidence_gap",
            "limitations",
            "source_limitation",
            "confidence_reason",
        )
    )


def _metric_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if str(record.get("section_kind") or record.get("section_type") or "") == "sector_metric"
        or str(record.get("section_name") or "").startswith("sector_metric_")
    ]


def _record_metric_name(record: dict[str, Any]) -> str:
    return str(record.get("metric_name") or record.get("metric_label") or "").strip().lower()


def _sector_from_ticker(ticker: str) -> str:
    symbol = ticker.upper().strip()
    code = symbol[:-3] if symbol.endswith(".AX") else symbol
    return ASX_SECTOR_BY_CODE.get(code, "")


def _sector_from_records(records: list[dict[str, Any]], *, ticker: str = "") -> str:
    for record in _metric_records(records):
        sector = str(record.get("sector") or "").strip().lower()
        if sector:
            return sector
    inferred = _sector_from_ticker(ticker)
    if inferred:
        return inferred
    return ""


def _dense_numeric_text(text: str) -> bool:
    numbers = re.findall(
        r"\(?-?(?:US\$|A\$|\$)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)?",
        text,
        re.IGNORECASE,
    )
    lower = text.lower()
    label_hits = sum(1 for label in DENSE_LABELS if re.search(rf"\b{re.escape(label)}\b", lower))
    parenthesized = len(re.findall(r"\([\d,]+(?:\.\d+)?\)", text))
    return len(numbers) > 4 and (label_hits >= 2 or parenthesized >= 2)


def _table_mapping_proved(record: dict[str, Any]) -> bool:
    row_label = str(record.get("row_label") or "").strip().lower()
    column_label = str(record.get("column_label") or "").strip().lower()
    cell_value = str(record.get("cell_value") or "").strip().lower()
    current_period_value = str(record.get("current_period_value") or "").strip().lower()
    variance_value = str(record.get("variance_value") or "").strip().lower()
    table_mapping_confidence = _int_field(record, "table_mapping_confidence")
    has_value_cell = any(value not in UNAVAILABLE_VALUES for value in (column_label, cell_value, current_period_value, variance_value))
    return row_label not in UNAVAILABLE_VALUES and has_value_cell and table_mapping_confidence >= ACCEPTED_TABLE_MAPPING_THRESHOLD


def _eligible_source_quality(record: dict[str, Any]) -> bool:
    return str(record.get("source_quality_tier") or "").strip() in ELIGIBLE_ASX_SOURCE_QUALITY_TIERS


def _is_cleanly_extracted(record: dict[str, Any]) -> bool:
    if str(record.get("metric_value_status") or "").strip().lower() != "value_extracted":
        return False
    if not _eligible_source_quality(record):
        return False
    if not _clean_value_present(record):
        return False
    if _int_field(record, "association_score") < ACCEPTED_ASSOCIATION_THRESHOLD:
        return False
    table_mapping_confidence = _int_field(record, "table_mapping_confidence")
    if 0 < table_mapping_confidence < ACCEPTED_TABLE_MAPPING_THRESHOLD:
        return False
    support_text = " ".join(
        str(record.get(field) or "")
        for field in ("supporting_sentence", "raw_row_text", "extracted_value_or_phrase")
    )
    return not (_dense_numeric_text(support_text) and not _table_mapping_proved(record))


def _is_unavailable_with_reason(record: dict[str, Any]) -> bool:
    status = str(record.get("status") or "").strip().lower()
    metric_status = str(record.get("metric_value_status") or "").strip().lower()
    return metric_status == "unavailable" and status != "available" and _reason_present(record)


def _has_documented_absence_or_external_blocker(record: dict[str, Any]) -> bool:
    basis = str(record.get("gap_disclosure_basis") or record.get("unavailable_basis") or "").strip().lower()
    if basis in {"source_lacks_metric", "source_genuinely_lacks_metric", "external_blocker"}:
        return True
    if record.get("source_lacks_metric") is True or record.get("external_blocker") is True:
        return True
    reason_text = " ".join(
        str(record.get(field) or "")
        for field in (
            "unavailable_reason",
            "evidence_gap",
            "limitations",
            "source_limitation",
            "confidence_reason",
        )
    ).lower()
    return "external blocker" in reason_text or "source genuinely lacks" in reason_text


def _is_gap_disclosed_weak_metric(record: dict[str, Any]) -> bool:
    metric_status = str(record.get("metric_value_status") or "").strip().lower()
    confidence = str(record.get("confidence") or "").strip().lower()
    return (
        metric_status in WEAK_STATUSES
        and not _clean_value_present(record)
        and confidence == "low"
        and _reason_present(record)
        and _has_documented_absence_or_external_blocker(record)
    )


def _matching_records(records: list[dict[str, Any]], aliases: tuple[str, ...]) -> list[dict[str, Any]]:
    alias_set = {alias.lower() for alias in aliases}
    return [record for record in _metric_records(records) if _record_metric_name(record) in alias_set]


def evaluate_core_metric_coverage(records: list[dict[str, Any]], *, ticker: str = "") -> dict[str, Any]:
    sector = _sector_from_records(records, ticker=ticker)
    profiles = CORE_METRIC_PROFILES.get(sector, {})
    required = list(profiles)
    cleanly_extracted: list[str] = []
    unavailable_with_reason: list[str] = []
    gap_disclosed: list[str] = []
    unresolved: list[str] = []
    details: dict[str, dict[str, Any]] = {}

    for metric, aliases in profiles.items():
        candidates = _matching_records(records, aliases)
        if any(_is_cleanly_extracted(record) for record in candidates):
            cleanly_extracted.append(metric)
            details[metric] = {"status": "cleanly_extracted"}
            continue
        ineligible_clean_candidates = [
            record
            for record in candidates
            if str(record.get("metric_value_status") or "").strip().lower() == "value_extracted"
            and _clean_value_present(record)
            and not _eligible_source_quality(record)
        ]
        if ineligible_clean_candidates:
            unresolved.append(metric)
            details[metric] = {
                "status": "unresolved",
                "reason": "clean value is not from an eligible ASX financial document source tier",
                "source_quality_tiers": [
                    str(record.get("source_quality_tier") or "") for record in ineligible_clean_candidates
                ],
                "evidence_ids": [str(record.get("evidence_id") or "") for record in ineligible_clean_candidates],
            }
            continue
        weak_candidates = [
            record
            for record in candidates
            if str(record.get("metric_value_status") or "").strip().lower() in WEAK_STATUSES
        ]
        if weak_candidates:
            if all(_is_gap_disclosed_weak_metric(record) for record in weak_candidates):
                gap_disclosed.append(metric)
                details[metric] = {
                    "status": "gap_disclosed",
                    "reason": "source mentions the metric, but extraction disclosed that no clean value was safely attached",
                    "evidence_ids": [str(record.get("evidence_id") or "") for record in weak_candidates],
                }
                continue
            unresolved.append(metric)
            details[metric] = {
                "status": "unresolved",
                "reason": "source appears to contain the metric but extraction did not produce a clean value",
                "evidence_ids": [str(record.get("evidence_id") or "") for record in weak_candidates],
            }
            continue
        if candidates and all(_is_unavailable_with_reason(record) for record in candidates):
            unavailable_with_reason.append(metric)
            details[metric] = {"status": "unavailable_with_reason"}
            continue
        unresolved.append(metric)
        details[metric] = {
            "status": "unresolved",
            "reason": "core metric missing, unavailable without reason, or not cleanly extracted",
            "evidence_ids": [str(record.get("evidence_id") or "") for record in candidates],
        }

    passed = bool(required) and not unresolved
    if not required:
        passed = True
    return {
        "ticker": ticker,
        "sector": sector,
        "core_metric_coverage_status": "passed" if passed else "failed",
        "core_metrics_required": required,
        "core_metrics_cleanly_extracted": cleanly_extracted,
        "core_metrics_unavailable_with_reason": unavailable_with_reason,
        "core_metrics_gap_disclosed": gap_disclosed,
        "core_metrics_unresolved": unresolved,
        "core_metric_coverage_passed": passed,
        "core_metric_coverage_details": details,
    }


def read_section_records(evidence_path: Path | None) -> list[dict[str, Any]]:
    if not evidence_path:
        return []
    path = evidence_path.parent / "financial_report" / "section_records.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [record for record in payload if isinstance(record, dict)]


def evaluate_core_metric_coverage_from_evidence(evidence_path: Path | None, *, ticker: str = "") -> dict[str, Any]:
    return evaluate_core_metric_coverage(read_section_records(evidence_path), ticker=ticker)
