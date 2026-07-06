# Evidence And Reasoning Audit

## Summary Verdict
pass_with_warnings

## Critical Findings
- None.

## Warnings
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:MPL.AX:2026-07-02:016 metric=premium_growth`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:MPL.AX:2026-07-02:019 metric=capital_adequacy`

## Evidence References
- financial:MPL.AX:2026-07-02:016 metric=premium_growth
- financial:MPL.AX:2026-07-02:019 metric=capital_adequacy

## Required Remediation
- None.

## Regression Tests Needed
- Consider adding a fixture for this metric/source layout.

## Do Not Change
- Do not replace Bull/Bear debate, Research Manager, Trader, Risk Analysts, Portfolio Manager, or Quality Reviewer.
- Keep Research Manager rating separate from Trader action and Portfolio stance.
- Keep paper-study-only boundary, ASX metric safeguards, dense-table table_row_unparsed behavior, validators, and remediation loop.
