# Financial Report Analyst

## Tool Outputs Used

- financial_document_evidence section records: 23 records from 10-K, 10-Q, 8-K, and investor-presentation coverage.
- Evidence ledger: `codex_tradingagents_skillkit/runs/aapl_msft_2026-06-30_review_gate_fixed/evidence/AAPL/2026-06-30/financial_report/evidence_ledger.jsonl`.

## Source coverage table

| Source document | Section / exhibit | Status | Filing date | Evidence ID | Evidence gap |
|---|---|---|---|---|---|
| annual_report_10k | 10-K business overview | available | 2025-10-31 | financial:AAPL:2026-06-30:001 | none |
| quarterly_report_10q | 10-Q business overview | unavailable | 2026-05-01 | financial:AAPL:2026-06-30:011 | 10-Q business overview was not identified in the extracted filing text. |
| annual_report_10k | 10-K risk factors | available | 2025-10-31 | financial:AAPL:2026-06-30:002 | none |
| quarterly_report_10q | 10-Q risk factors | available | 2026-05-01 | financial:AAPL:2026-06-30:012 | none |
| annual_report_10k | 10-K MD&A | available | 2025-10-31 | financial:AAPL:2026-06-30:003 | none |
| quarterly_report_10q | 10-Q MD&A | available | 2026-05-01 | financial:AAPL:2026-06-30:013 | none |
| annual_report_10k | 10-K liquidity and capital resources | available | 2025-10-31 | financial:AAPL:2026-06-30:006 | none |
| quarterly_report_10q | 10-Q liquidity and capital resources | available | 2026-05-01 | financial:AAPL:2026-06-30:016 | none |
| annual_report_10k | 10-K segment/product revenue tables | available | 2025-10-31 | financial:AAPL:2026-06-30:005 | none |
| quarterly_report_10q | 10-Q segment/product revenue tables | available | 2026-05-01 | financial:AAPL:2026-06-30:015 | none |
| annual_report_10k | 10-K income statement | available | 2025-10-31 | financial:AAPL:2026-06-30:008 | none |
| quarterly_report_10q | 10-Q income statement | available | 2026-05-01 | financial:AAPL:2026-06-30:018 | none |
| annual_report_10k | 10-K balance sheet | available | 2025-10-31 | financial:AAPL:2026-06-30:009 | none |
| quarterly_report_10q | 10-Q balance sheet | available | 2026-05-01 | financial:AAPL:2026-06-30:019 | none |
| annual_report_10k | 10-K cash flow statement | available | 2025-10-31 | financial:AAPL:2026-06-30:010 | none |
| quarterly_report_10q | 10-Q cash flow statement | available | 2026-05-01 | financial:AAPL:2026-06-30:020 | none |
| earnings_release_exhibit | Exhibit 99.1 | available | 2026-04-30 | financial:AAPL:2026-06-30:022 | none |
| investor_presentation | Latest investor presentation | unavailable |  | financial:AAPL:2026-06-30:023 | No investor presentation source was discovered from the SEC submissions feed. |

## Claim-Source Table

| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap |
|---|---|---|---|---|---|
| Business model and revenue drivers are filing-supported. | 10-K | 10-K business overview financial:AAPL:2026-06-30:001 | 2025-10-31 | medium | none |
| Risk discussion is available from annual and quarterly filings. | 10-K / 10-Q | 10-K risk factors financial:AAPL:2026-06-30:002 | 2025-10-31 | medium | none |
| Management commentary and operating trend discussion are available. | 10-K / 10-Q | 10-K MD&A financial:AAPL:2026-06-30:003 | 2025-10-31 | medium | none |
| Segment or product-level performance is supported. | 10-K / 10-Q | 10-K segment/product revenue tables financial:AAPL:2026-06-30:005 | 2025-10-31 | medium | none |
| Liquidity review is supported by filing evidence. | 10-K / 10-Q | 10-K liquidity and capital resources financial:AAPL:2026-06-30:006 | 2025-10-31 | medium | none |
| Income statement, balance sheet, and cash-flow statement evidence are available. | 10-K / 10-Q | 10-K income statement financial:AAPL:2026-06-30:008; 10-K balance sheet financial:AAPL:2026-06-30:009; 10-K cash flow statement financial:AAPL:2026-06-30:010 | 2025-10-31 | medium | none |
| Earnings-release detail is supported by the 8-K exhibit. | 8-K | Exhibit 99.1 financial:AAPL:2026-06-30:022 | 2026-04-30 | medium | none |

## Evidence gaps

Investor-presentation coverage remains unavailable from the SEC submissions feed. Any capex, guidance, or product detail not present in the cited sections should be treated as an evidence gap rather than inferred.

## Memory Update

* Durable facts to retain: AAPL financial_report_analyst used financial:AAPL:2026-06-30:001 and financial:AAPL:2026-06-30:003 for this 2026-06-30 validation run.
* Prior mistake to avoid: Do not report MD&A, Exhibit 99.1, or cash-flow statement extraction as unavailable when current section records show them available.
* Open questions: Refresh evidence for any later trade date.
* Evidence references: financial:AAPL:2026-06-30:001, financial:AAPL:2026-06-30:003
* Staleness / expiry: Expires after 2026-06-30.
