# Evidence And Reasoning Audit

## Summary Verdict
pass_with_warnings

## Critical Findings
- None.

## Warnings
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:CSL.AX:2026-07-06:018 metric=plasma_collections`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:CSL.AX:2026-07-06:019 metric=margins`

## Evidence References
- financial:CSL.AX:2026-07-06:018 metric=plasma_collections
- financial:CSL.AX:2026-07-06:019 metric=margins

## Required Remediation
- None.

## Regression Tests Needed
- Consider adding a fixture for this metric/source layout.

## Do Not Change
- Do not replace Bull/Bear debate, Research Manager, Trader, Risk Analysts, Portfolio Manager, or Quality Reviewer.
- Keep Research Manager rating separate from Trader action and Portfolio stance.
- Keep paper-study-only boundary, ASX metric safeguards, dense-table table_row_unparsed behavior, validators, and remediation loop.
