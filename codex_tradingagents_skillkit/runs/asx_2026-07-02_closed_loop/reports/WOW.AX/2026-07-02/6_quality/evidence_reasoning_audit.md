# Evidence And Reasoning Audit

## Summary Verdict
pass_with_warnings

## Critical Findings
- None.

## Warnings
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:WOW.AX:2026-07-02:016 metric=sales_growth`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:WOW.AX:2026-07-02:017 metric=comparable_sales_if_available`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:WOW.AX:2026-07-02:019 metric=inventory`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:WOW.AX:2026-07-02:040 metric=inventory`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:WOW.AX:2026-07-02:041 metric=capex`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:WOW.AX:2026-07-02:042 metric=dividends`

## Evidence References
- financial:WOW.AX:2026-07-02:016 metric=sales_growth
- financial:WOW.AX:2026-07-02:017 metric=comparable_sales_if_available
- financial:WOW.AX:2026-07-02:019 metric=inventory
- financial:WOW.AX:2026-07-02:040 metric=inventory
- financial:WOW.AX:2026-07-02:041 metric=capex
- financial:WOW.AX:2026-07-02:042 metric=dividends

## Required Remediation
- None.

## Regression Tests Needed
- Consider adding a fixture for this metric/source layout.

## Do Not Change
- Do not replace Bull/Bear debate, Research Manager, Trader, Risk Analysts, Portfolio Manager, or Quality Reviewer.
- Keep Research Manager rating separate from Trader action and Portfolio stance.
- Keep paper-study-only boundary, ASX metric safeguards, dense-table table_row_unparsed behavior, validators, and remediation loop.
