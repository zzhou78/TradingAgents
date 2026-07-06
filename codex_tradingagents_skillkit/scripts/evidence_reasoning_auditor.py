from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ACCEPTED_ASSOCIATION_THRESHOLD = 80
ACCEPTED_TABLE_MAPPING_THRESHOLD = 80
WEAK_METRIC_STATUSES = {"table_row_unparsed", "context_only", "metric_mentioned_only", "unavailable"}
ROLE_REPORTS = [
    ("research_manager", Path("2_research") / "manager.md"),
    ("trader", Path("3_trading") / "trader.md"),
    ("aggressive_risk", Path("4_risk") / "aggressive_round_1.md"),
    ("conservative_risk", Path("4_risk") / "conservative_round_1.md"),
    ("neutral_risk", Path("4_risk") / "neutral_round_1.md"),
    ("portfolio_manager", Path("5_portfolio") / "decision.md"),
    ("complete_report", Path("complete_report.md")),
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _evidence_dir(evidence_path: Path | None) -> Path | None:
    return evidence_path.parent if evidence_path else None


def _financial_records(evidence_path: Path | None) -> list[dict[str, Any]]:
    evidence_dir = _evidence_dir(evidence_path)
    if not evidence_dir:
        return []
    path = evidence_dir / "financial_report" / "section_records.json"
    if not path.exists():
        return []
    try:
        payload = _read_json(path)
    except json.JSONDecodeError:
        return []
    return [record for record in payload if isinstance(record, dict)]


def _clean_value_present(record: dict[str, Any]) -> bool:
    return str(record.get("clean_metric_value") or "").strip().lower() not in {"", "unavailable", "none", "null"}


def _int_field(record: dict[str, Any], field: str) -> int:
    try:
        return int(float(str(record.get(field) or "0")))
    except ValueError:
        return 0


def _dense_numeric_text(text: str) -> bool:
    numbers = re.findall(
        r"\(?-?(?:US\$|A\$|\$)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)?",
        text,
        re.IGNORECASE,
    )
    labels = re.findall(
        r"\b(?:inventor(?:y|ies)|trade payables|receivables|revenue|sales|ebit|claims expense|gross profit|assets|liabilities|debt)\b",
        text,
        re.IGNORECASE,
    )
    distinct_labels = {label.lower() for label in labels}
    parenthesized = len(re.findall(r"\([\d,]+(?:\.\d+)?\)", text))
    return len(numbers) > 4 and (len(distinct_labels) >= 2 or parenthesized >= 2)


def _finding(
    *,
    attack: str,
    finding: str,
    reference: str,
    required_remediation: str,
    regression_test: str,
) -> dict[str, str]:
    return {
        "attack": attack,
        "finding": finding,
        "evidence_reference": reference,
        "required_remediation": required_remediation,
        "regression_test": regression_test,
    }


def _warning(*, attack: str, warning: str, reference: str, regression_test: str = "") -> dict[str, str]:
    return {
        "attack": attack,
        "warning": warning,
        "evidence_reference": reference,
        "regression_test": regression_test,
    }


def _metric_attachment_findings(records: list[dict[str, Any]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    critical: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    for record in records:
        if record.get("section_kind") != "sector_metric":
            continue
        evidence_id = str(record.get("evidence_id") or "uncited")
        metric_name = str(record.get("metric_name") or "unknown_metric")
        status = str(record.get("metric_value_status") or "").strip().lower()
        direction = str(record.get("direction") or "").strip().lower()
        confidence = str(record.get("confidence") or "").strip().lower()
        association_score = _int_field(record, "association_score")
        table_mapping_confidence = _int_field(record, "table_mapping_confidence")
        row_label = str(record.get("row_label") or "").strip().lower()
        column_label = str(record.get("column_label") or "").strip().lower()
        support_text = str(record.get("supporting_sentence") or record.get("extracted_value_or_phrase") or "")
        reference = f"{evidence_id} metric={metric_name}"

        if _clean_value_present(record):
            if status != "value_extracted":
                critical.append(
                    _finding(
                        attack="Metric-Value Attachment Attack",
                        finding="clean_metric_value is populated without metric_value_status=value_extracted.",
                        reference=reference,
                        required_remediation="Suppress the clean value or set value_extracted only after valid association proof.",
                        regression_test="Add a metric audit test where clean_metric_value with weak status fails.",
                    )
                )
            if association_score < ACCEPTED_ASSOCIATION_THRESHOLD:
                critical.append(
                    _finding(
                        attack="Metric-Value Attachment Attack",
                        finding="clean_metric_value is populated below the accepted association threshold.",
                        reference=reference,
                        required_remediation="Raise association proof or set clean_metric_value unavailable.",
                        regression_test="Add a low association score clean-value suppression test.",
                    )
                )
            if 0 < table_mapping_confidence < ACCEPTED_TABLE_MAPPING_THRESHOLD:
                critical.append(
                    _finding(
                        attack="Metric-Value Attachment Attack",
                        finding="clean_metric_value is populated below the accepted table mapping threshold.",
                        reference=reference,
                        required_remediation="Require row/column mapping confidence >= 80 or suppress the clean value.",
                        regression_test="Add a table_mapping_confidence threshold regression test.",
                    )
                )

        if (
            status == "value_extracted"
            and _dense_numeric_text(support_text)
            and row_label in {"", "unavailable"}
            and column_label in {"", "unavailable"}
        ):
            critical.append(
                _finding(
                    attack="Dense Table Attack",
                    finding="Dense numeric text produced a clean value without row_label and column_label.",
                    reference=reference,
                    required_remediation="Downgrade the metric to table_row_unparsed unless row/column mapping proves the value.",
                    regression_test="Add a dense table value extraction rejection test.",
                )
            )

        if status in WEAK_METRIC_STATUSES and direction in {"supportive", "adverse"} and confidence in {"medium", "high"}:
            critical.append(
                _finding(
                    attack="Evidence Reliability Attack",
                    finding="Weak metric status is counted as medium/high-confidence directional evidence.",
                    reference=reference,
                    required_remediation="Downgrade confidence or prevent weak statuses from driving supportive/adverse conclusions.",
                    regression_test="Add a weak metric status directional-confidence regression test.",
                )
            )

        if status in {"table_row_unparsed", "metric_mentioned_only"}:
            warnings.append(
                _warning(
                    attack="Validator Blind-Spot Attack",
                    warning="Metric is present but clean value or row/column mapping remains unresolved.",
                    reference=reference,
                    regression_test="Consider adding a fixture for this metric/source layout.",
                )
            )
    return critical, warnings


def _role_reasoning_findings(report_dir: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    critical: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    role_text = {name: _read(report_dir / relative) for name, relative in ROLE_REPORTS}
    material_text = "\n".join(text for text in role_text.values() if text.strip())
    if material_text and not re.search(r"\b(?:market|news|social|fundamentals|financial|stage):[A-Z0-9.\-]+:\d{4}-\d{2}-\d{2}:\d{3}\b", material_text):
        critical.append(
            _finding(
                attack="Evidence Reliability Attack",
                finding="Material role reports do not cite evidence IDs.",
                reference=str(report_dir),
                required_remediation="Add evidence IDs to material claims in Research Manager, Trader, Risk, and Portfolio reports.",
                regression_test="Add a report audit test for missing material evidence IDs.",
            )
        )
    manager = role_text.get("research_manager", "")
    if manager and "Debate Outcome Scorecard" not in manager:
        warnings.append(
            _warning(
                attack="Reasoning Logic Attack",
                warning="Research Manager report lacks a Debate Outcome Scorecard.",
                reference=str(report_dir / "2_research" / "manager.md"),
                regression_test="Keep the quality validator coverage for Debate Outcome Scorecard.",
            )
        )
    trader = role_text.get("trader", "")
    if trader and "FINAL TRANSACTION PROPOSAL" in trader and "paper-study" not in trader.lower():
        critical.append(
            _finding(
                attack="Role Separation Attack",
                finding="Trader proposal does not preserve the paper-study boundary.",
                reference=str(report_dir / "3_trading" / "trader.md"),
                required_remediation="Add explicit paper-study framing and prevent real execution wording.",
                regression_test="Add a Trader paper-study boundary regression test.",
            )
        )
    portfolio = role_text.get("portfolio_manager", "")
    if portfolio and "Risk debate impact" not in portfolio:
        warnings.append(
            _warning(
                attack="Reasoning Logic Attack",
                warning="Portfolio Manager may not explain which risk side was stronger.",
                reference=str(report_dir / "5_portfolio" / "decision.md"),
                regression_test="Keep the Portfolio risk-debate impact validator coverage.",
            )
        )
    return critical, warnings


def audit_report_dir(report_dir: Path, evidence_path: Path | None = None) -> dict[str, Any]:
    records = _financial_records(evidence_path)
    metric_critical, metric_warnings = _metric_attachment_findings(records)
    role_critical, role_warnings = _role_reasoning_findings(report_dir)
    critical = [*metric_critical, *role_critical]
    warnings = [*metric_warnings, *role_warnings]
    verdict = "fail" if critical else ("pass_with_warnings" if warnings else "pass")
    return {
        "summary_verdict": verdict,
        "critical_findings": critical,
        "warnings": warnings,
        "evidence_references": [item["evidence_reference"] for item in [*critical, *warnings]],
        "required_remediation": [item["required_remediation"] for item in critical],
        "regression_tests_needed": sorted(
            {item["regression_test"] for item in [*critical, *warnings] if item.get("regression_test")}
        ),
        "do_not_change": [
            "Do not replace Bull/Bear debate, Research Manager, Trader, Risk Analysts, Portfolio Manager, or Quality Reviewer.",
            "Keep Research Manager rating separate from Trader action and Portfolio stance.",
            "Keep paper-study-only boundary, ASX metric safeguards, dense-table table_row_unparsed behavior, validators, and remediation loop.",
        ],
    }


def render_audit_markdown(audit: dict[str, Any]) -> str:
    def bullet(items: list[Any], empty: str) -> str:
        if not items:
            return f"- {empty}"
        rows = []
        for item in items:
            if isinstance(item, dict):
                label = item.get("finding") or item.get("warning") or json.dumps(item, sort_keys=True)
                ref = item.get("evidence_reference", "")
                rows.append(f"- {label} Reference: `{ref}`")
            else:
                rows.append(f"- {item}")
        return "\n".join(rows)

    return "\n".join(
        [
            "# Evidence And Reasoning Audit",
            "",
            "## Summary Verdict",
            str(audit["summary_verdict"]),
            "",
            "## Critical Findings",
            bullet(list(audit.get("critical_findings", [])), "None."),
            "",
            "## Warnings",
            bullet(list(audit.get("warnings", [])), "None."),
            "",
            "## Evidence References",
            bullet(list(audit.get("evidence_references", [])), "None."),
            "",
            "## Required Remediation",
            bullet(list(audit.get("required_remediation", [])), "None."),
            "",
            "## Regression Tests Needed",
            bullet(list(audit.get("regression_tests_needed", [])), "None."),
            "",
            "## Do Not Change",
            bullet(list(audit.get("do_not_change", [])), "None."),
            "",
        ]
    )


def write_audit(report_dir: Path, evidence_path: Path | None = None) -> dict[str, Any]:
    audit = audit_report_dir(report_dir, evidence_path)
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True, exist_ok=True)
    json_path = quality_dir / "evidence_reasoning_audit.json"
    md_path = quality_dir / "evidence_reasoning_audit.md"
    json_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")
    md_path.write_text(render_audit_markdown(audit), encoding="utf-8")
    audit["json_path"] = str(json_path)
    audit["markdown_path"] = str(md_path)
    return audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit TradingAgents evidence substrate and reasoning logic.")
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    audit = write_audit(args.report_dir, args.evidence)
    if args.format == "json":
        print(json.dumps(audit, indent=2))
    else:
        print(f"Evidence/reasoning audit: {audit['summary_verdict']}")
        print(f"Critical findings: {len(audit['critical_findings'])}")
        print(f"Warnings: {len(audit['warnings'])}")
    return 1 if audit["summary_verdict"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
