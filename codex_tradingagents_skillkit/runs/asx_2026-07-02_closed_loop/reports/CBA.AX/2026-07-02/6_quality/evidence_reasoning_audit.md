# Evidence And Reasoning Audit

## Summary Verdict
pass_with_warnings

## Critical Findings
- None.

## Warnings
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:CBA.AX:2026-07-02:041 metric=arrears`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:CBA.AX:2026-07-02:044 metric=roe`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:CBA.AX:2026-07-02:063 metric=arrears`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:CBA.AX:2026-07-02:066 metric=roe`

## Evidence References
- financial:CBA.AX:2026-07-02:041 metric=arrears
- financial:CBA.AX:2026-07-02:044 metric=roe
- financial:CBA.AX:2026-07-02:063 metric=arrears
- financial:CBA.AX:2026-07-02:066 metric=roe

## Required Remediation
- None.

## Regression Tests Needed
- Consider adding a fixture for this metric/source layout.

## Do Not Change
- Do not replace Bull/Bear debate, Research Manager, Trader, Risk Analysts, Portfolio Manager, or Quality Reviewer.
- Keep Research Manager rating separate from Trader action and Portfolio stance.
- Keep paper-study-only boundary, ASX metric safeguards, dense-table table_row_unparsed behavior, validators, and remediation loop.
