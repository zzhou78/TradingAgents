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
    "tier_3_structured_online_annual_report",
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

MATERIALITY_RULES: dict[str, dict[str, tuple[str, ...]]] = {
    "banks": {
        "critical": ("net_interest_margin", "cet1", "credit_quality_group"),
        "important": ("loan_growth", "dividend", "roe", "arrears", "impairment"),
        "supporting": (),
        "optional_if_available": (),
    },
    "miners": {
        "critical": ("production", "realised_price", "unit_cost_aisc", "capex", "commodity_exposure"),
        "important": ("reserves_resources",),
        "supporting": (),
        "optional_if_available": (),
    },
    "healthcare": {
        "critical": (
            "segment_revenue_or_growth",
            "margins",
            "guidance",
            "debt_or_balance_sheet",
            "plasma_collections_or_collection_network",
        ),
        "important": ("r_and_d", "product_segment_commentary", "pipeline_commentary"),
        "supporting": (),
        "optional_if_available": (),
    },
    "health_insurers": {
        "critical": ("claims_ratio", "capital_adequacy"),
        "important": ("premium_growth", "membership", "operating_profit_or_margin"),
        "supporting": (),
        "optional_if_available": (),
    },
    "retailers": {
        "critical": ("sales_growth", "ebit_margin"),
        "important": ("inventory_or_working_capital", "capex", "comparable_sales_if_available"),
        "supporting": ("dividends",),
        "optional_if_available": (),
    },
}

REQUIREMENT_ALIASES: dict[str, tuple[str, ...]] = {
    "credit_quality_group": ("impairment", "arrears", "loan_loss_rate"),
    "segment_revenue_or_growth": ("segment_revenue", "segment_growth"),
    "debt_or_balance_sheet": ("debt", "net_debt", "borrowings", "debt_or_balance_sheet"),
    "plasma_collections_or_collection_network": (
        "plasma_collections",
        "plasma_collection",
        "plasma_collection_network",
    ),
    "product_segment_commentary": ("product_segment_commentary", "segment_commentary", "product_commentary"),
    "pipeline_commentary": ("pipeline_commentary", "pipeline"),
}

VALID_METRIC_SUBTYPES: dict[str, set[str]] = {
    "inventory_or_working_capital": {"inventory_balance", "inventory_or_working_capital_movement"},
    "inventory": {"inventory_balance", "inventory_or_working_capital_movement"},
    "dividends": {"dividend_amount_or_dps"},
    "dividend": {"dividend_amount_or_dps"},
}

NARRATIVE_MATERIALITY_STATUSES = {
    "commodity_exposure": {"portfolio_mix_narrative"},
    "guidance": {"guidance_narrative"},
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


def _metric_subtype_rejection_reason(metric_name: str, record: dict[str, Any]) -> str:
    subtype = str(record.get("metric_subtype") or "").strip().lower()
    if not subtype:
        return ""
    allowed = VALID_METRIC_SUBTYPES.get(metric_name, set())
    if subtype in allowed:
        return ""
    if "movement" in subtype or "change" in subtype:
        return "clean value subtype is not valid for this metric profile"
    return ""


def _is_cleanly_extracted(record: dict[str, Any], metric_name: str = "") -> bool:
    if str(record.get("metric_value_status") or "").strip().lower() != "value_extracted":
        return False
    if not _eligible_source_quality(record):
        return False
    if not _clean_value_present(record):
        return False
    if metric_name and _metric_subtype_rejection_reason(metric_name, record):
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


def _proof_present(record: dict[str, Any]) -> bool:
    return any(
        str(record.get(field) or "").strip().lower() not in UNAVAILABLE_VALUES
        for field in ("section_title", "source_page", "table_title", "row_label", "supporting_sentence")
    )


def _commodity_names(record: dict[str, Any]) -> list[str]:
    value = record.get("commodity_names")
    if isinstance(value, list):
        names = [str(item).strip().lower() for item in value if str(item).strip()]
    else:
        text = " ".join(
            str(record.get(field) or "")
            for field in ("supporting_sentence", "extracted_value_or_phrase", "raw_row_text")
        ).lower()
        names = [
            commodity
            for commodity in ("iron ore", "copper", "steelmaking coal", "coal", "potash", "nickel", "petroleum")
            if commodity in text
        ]
    return _dedupe(names)


def _is_materially_satisfied_narrative(metric_name: str, record: dict[str, Any]) -> bool:
    status = str(record.get("metric_value_status") or "").strip().lower()
    if status not in NARRATIVE_MATERIALITY_STATUSES.get(metric_name, set()):
        return False
    if not _eligible_source_quality(record) or not _proof_present(record):
        return False
    if metric_name == "commodity_exposure":
        return len(_commodity_names(record)) >= 2
    return True


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def _matching_records(records: list[dict[str, Any]], aliases: tuple[str, ...]) -> list[dict[str, Any]]:
    alias_set = {alias.lower() for alias in aliases}
    return [record for record in _metric_records(records) if _record_metric_name(record) in alias_set]


def _aliases_for_metric(sector: str, metric: str) -> tuple[str, ...]:
    profiles = CORE_METRIC_PROFILES.get(sector, {})
    if metric in profiles:
        return profiles[metric]
    aliases = REQUIREMENT_ALIASES.get(metric)
    if aliases:
        return aliases
    return (metric,)


def _metric_state(records: list[dict[str, Any]], sector: str, metric: str) -> dict[str, Any]:
    candidates = _matching_records(records, _aliases_for_metric(sector, metric))
    evidence_ids = [str(record.get("evidence_id") or "") for record in candidates]
    if any(_is_cleanly_extracted(record, metric) for record in candidates):
        return {"status": "cleanly_extracted", "materially_satisfied": True, "evidence_ids": evidence_ids}
    narrative_candidates = [record for record in candidates if _is_materially_satisfied_narrative(metric, record)]
    if narrative_candidates:
        return {
            "status": "materially_satisfied",
            "materially_satisfied": True,
            "reason": f"{metric} is supported by eligible narrative evidence rather than a clean numeric value",
            "evidence_ids": [str(record.get("evidence_id") or "") for record in narrative_candidates],
        }
    subtype_rejected_candidates = [
        record
        for record in candidates
        if str(record.get("metric_value_status") or "").strip().lower() == "value_extracted"
        and _clean_value_present(record)
        and _metric_subtype_rejection_reason(metric, record)
    ]
    if subtype_rejected_candidates:
        return {
            "status": "unresolved",
            "materially_satisfied": False,
            "reason": "clean value subtype is not valid for this metric profile",
            "evidence_ids": [str(record.get("evidence_id") or "") for record in subtype_rejected_candidates],
        }
    ineligible_clean_candidates = [
        record
        for record in candidates
        if str(record.get("metric_value_status") or "").strip().lower() == "value_extracted"
        and _clean_value_present(record)
        and not _eligible_source_quality(record)
    ]
    if ineligible_clean_candidates:
        return {
            "status": "unresolved",
            "materially_satisfied": False,
            "reason": "clean value is not from an eligible ASX financial document source tier",
            "source_quality_tiers": [
                str(record.get("source_quality_tier") or "") for record in ineligible_clean_candidates
            ],
            "evidence_ids": [str(record.get("evidence_id") or "") for record in ineligible_clean_candidates],
        }
    weak_candidates = [
        record
        for record in candidates
        if str(record.get("metric_value_status") or "").strip().lower() in WEAK_STATUSES
    ]
    if weak_candidates:
        if all(_is_gap_disclosed_weak_metric(record) for record in weak_candidates):
            return {
                "status": "gap_disclosed",
                "materially_satisfied": False,
                "source_limited": True,
                "reason": "source mentions the metric, but extraction disclosed that no clean value was safely attached",
                "evidence_ids": [str(record.get("evidence_id") or "") for record in weak_candidates],
            }
        return {
            "status": "unresolved",
            "materially_satisfied": False,
            "reason": "source appears to contain the metric but extraction did not produce a clean value",
            "evidence_ids": [str(record.get("evidence_id") or "") for record in weak_candidates],
        }
    if candidates and all(_is_unavailable_with_reason(record) for record in candidates):
        source_limited = any(_has_documented_absence_or_external_blocker(record) for record in candidates)
        return {
            "status": "unavailable_with_reason",
            "materially_satisfied": source_limited,
            "source_limited": source_limited,
            "evidence_ids": evidence_ids,
        }
    return {
        "status": "unresolved",
        "materially_satisfied": False,
        "reason": "core metric missing, unavailable without reason, or not cleanly extracted",
        "evidence_ids": evidence_ids,
    }


def _requirement_state(states: dict[str, dict[str, Any]], sector: str, requirement: str) -> dict[str, Any]:
    if requirement == "credit_quality_group":
        member_states = {metric: states.get(metric, {}) for metric in ("impairment", "arrears", "loan_loss_rate")}
        clean_members = [
            metric
            for metric, state in member_states.items()
            if state.get("status") == "cleanly_extracted" or state.get("materially_satisfied") is True
        ]
        if clean_members:
            return {
                "status": "cleanly_extracted",
                "materially_satisfied": True,
                "clean_members": clean_members,
            }
        return {
            "status": "unresolved",
            "materially_satisfied": False,
            "reason": "credit_quality_group requires at least one clean impairment, arrears, or loan-loss metric",
        }
    state = states.get(requirement)
    if state is None:
        state = _metric_state([], sector, requirement)
    return state


def _warning_label(metric: str) -> str:
    return {
        "roe": "ROE",
        "arrears": "arrears",
        "credit_quality_group": "credit quality group",
    }.get(metric, metric)


def _materiality_summary(
    *,
    sector: str,
    states: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    rules = MATERIALITY_RULES.get(sector, {})
    critical_required = list(rules.get("critical", ()))
    critical_clean: list[str] = []
    critical_unresolved: list[str] = []
    remediation_required_reasons: list[str] = []
    warnings: list[str] = []
    major_warnings: list[str] = []

    for metric in critical_required:
        state = _requirement_state(states, sector, metric)
        if state.get("materially_satisfied") is True:
            critical_clean.append(metric)
            continue
        critical_unresolved.append(metric)
        remediation_required_reasons.append(
            f"critical metric {metric} is not cleanly extracted or source-limited: {state.get('reason', 'unresolved')}"
        )

    tier_outputs: dict[str, list[str]] = {}
    for tier in ("important", "supporting"):
        clean: list[str] = []
        unresolved: list[str] = []
        for metric in rules.get(tier, ()):
            state = _requirement_state(states, sector, metric)
            if state.get("materially_satisfied") is True or (
                state.get("status") == "unavailable_with_reason" and state.get("source_limited") is True
            ):
                clean.append(metric)
            elif state.get("status") != "unavailable_with_reason":
                unresolved.append(metric)
            else:
                unresolved.append(metric)
        tier_outputs[f"{tier}_clean"] = clean
        tier_outputs[f"{tier}_unresolved"] = unresolved

    for metric in tier_outputs["important_unresolved"]:
        major_warnings.append(f"{_warning_label(metric)} not cleanly extracted")
    for metric in tier_outputs["supporting_unresolved"]:
        warnings.append(f"{_warning_label(metric)} not cleanly extracted")

    if sector == "banks":
        arrears_clean = states.get("arrears", {}).get("materially_satisfied") is True
        impairment_clean = states.get("impairment", {}).get("materially_satisfied") is True
        if impairment_clean and not arrears_clean:
            if "arrears not cleanly extracted" not in major_warnings:
                major_warnings.append("arrears not cleanly extracted")
            major_warnings.append("credit quality assessment relies on impairment / loan impairment expense instead of arrears")
        if "roe" in tier_outputs["important_unresolved"] and "ROE not cleanly extracted" not in major_warnings:
            major_warnings.append("ROE not cleanly extracted")

    if critical_unresolved:
        materiality_status = "remediation_required"
    elif major_warnings:
        materiality_status = "review_ready_with_major_warnings"
    elif warnings:
        materiality_status = "review_ready_with_warnings"
    else:
        materiality_status = "review_ready_clean"

    return {
        "materiality_status": materiality_status,
        "critical_metrics_required": critical_required,
        "critical_metrics_clean": critical_clean,
        "critical_metrics_unresolved": critical_unresolved,
        "important_metrics_clean": tier_outputs["important_clean"],
        "important_metrics_unresolved": tier_outputs["important_unresolved"],
        "supporting_metrics_clean": tier_outputs["supporting_clean"],
        "supporting_metrics_unresolved": tier_outputs["supporting_unresolved"],
        "warnings": _dedupe(warnings),
        "major_warnings": _dedupe(major_warnings),
        "remediation_required_reasons": remediation_required_reasons,
    }


def evaluate_core_metric_coverage(records: list[dict[str, Any]], *, ticker: str = "") -> dict[str, Any]:
    sector = _sector_from_records(records, ticker=ticker)
    profiles = CORE_METRIC_PROFILES.get(sector, {})
    required = list(profiles)
    states: dict[str, dict[str, Any]] = {}
    details: dict[str, dict[str, Any]] = {}
    for metric in required:
        states[metric] = _metric_state(records, sector, metric)
    for tier_metrics in MATERIALITY_RULES.get(sector, {}).values():
        for metric in tier_metrics:
            if metric not in states and metric != "credit_quality_group":
                states[metric] = _metric_state(records, sector, metric)

    cleanly_extracted = [metric for metric in required if states[metric].get("status") == "cleanly_extracted"]
    materially_satisfied = [
        metric
        for metric in required
        if states[metric].get("status") == "materially_satisfied"
        and states[metric].get("materially_satisfied") is True
    ]
    unavailable_with_reason = [
        metric for metric in required if states[metric].get("status") == "unavailable_with_reason"
    ]
    gap_disclosed = [metric for metric in required if states[metric].get("status") == "gap_disclosed"]
    unresolved = [metric for metric in required if states[metric].get("status") == "unresolved"]
    for metric, state in states.items():
        details[metric] = {key: value for key, value in state.items() if key != "materially_satisfied"}

    materiality = _materiality_summary(sector=sector, states=states)
    passed = materiality["materiality_status"] != "remediation_required"
    if not required and not materiality["critical_metrics_required"]:
        passed = True
        materiality["materiality_status"] = "review_ready_clean"
    return {
        "ticker": ticker,
        "sector": sector,
        "core_metric_coverage_status": "passed" if passed else "failed",
        "core_metrics_required": required,
        "core_metrics_cleanly_extracted": cleanly_extracted,
        "core_metrics_materially_satisfied": materially_satisfied,
        "core_metrics_unavailable_with_reason": unavailable_with_reason,
        "core_metrics_gap_disclosed": gap_disclosed,
        "core_metrics_unresolved": unresolved,
        "core_metric_coverage_passed": passed,
        "core_metric_coverage_details": details,
        **materiality,
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
