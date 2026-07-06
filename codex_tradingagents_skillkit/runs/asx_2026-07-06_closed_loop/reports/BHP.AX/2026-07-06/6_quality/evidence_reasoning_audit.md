# Evidence And Reasoning Audit

## Summary Verdict
fail

## Critical Findings
- Dense numeric text produced a clean value without row_label and column_label. Reference: `financial:BHP.AX:2026-07-06:032 metric=realised_price`

## Warnings
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:BHP.AX:2026-07-06:035 metric=reserves_resources`
- Metric is present but clean value or row/column mapping remains unresolved. Reference: `financial:BHP.AX:2026-07-06:036 metric=commodity_exposure`

## Evidence References
- financial:BHP.AX:2026-07-06:032 metric=realised_price
- financial:BHP.AX:2026-07-06:035 metric=reserves_resources
- financial:BHP.AX:2026-07-06:036 metric=commodity_exposure

## Required Remediation
- Downgrade the metric to table_row_unparsed unless row/column mapping proves the value.

## Regression Tests Needed
- Add a dense table value extraction rejection test.
- Consider adding a fixture for this metric/source layout.

## Do Not Change
- Do not replace Bull/Bear debate, Research Manager, Trader, Risk Analysts, Portfolio Manager, or Quality Reviewer.
- Keep Research Manager rating separate from Trader action and Portfolio stance.
- Keep paper-study-only boundary, ASX metric safeguards, dense-table table_row_unparsed behavior, validators, and remediation loop.
