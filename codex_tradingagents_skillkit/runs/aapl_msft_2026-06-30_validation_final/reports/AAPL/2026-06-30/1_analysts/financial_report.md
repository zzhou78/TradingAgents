# Financial Report Analyst

## Tool Outputs Used

- financial_document_evidence section records: financial:AAPL:2026-06-30:001 and related 10-K, 10-Q, and 8-K records.

## Source coverage table

| Source document | Section / exhibit | Status | Filing date | Evidence ID | Evidence gap |
|---|---|---|---|---|---|
| annual_report_10k | 10-K business overview | available | 2025-10-31 | financial:AAPL:2026-06-30:001 | none |
| annual_report_10k | 10-K risk factors | available | 2025-10-31 | financial:AAPL:2026-06-30:002 | none |
| annual_report_10k | 10-K segment information | available | 2025-10-31 | financial:AAPL:2026-06-30:004 | none |
| quarterly_report_10q | 10-Q liquidity and capital resources | available | 2026-05-01 | financial:AAPL:2026-06-30:016 | none |
| quarterly_report_10q | 10-Q income statement | available | 2026-05-01 | financial:AAPL:2026-06-30:018 | none |
| earnings_release_exhibit | Exhibit 99.1 | available | 2026-04-30 | financial:AAPL:2026-06-30:022 | none |
| investor_presentation | Latest investor presentation | unavailable |  | financial:AAPL:2026-06-30:023 | No investor presentation source was discovered from the SEC submissions feed. |

## Claim-Source Table

| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap |
|---|---|---|---|---|---|
| Business model and revenue drivers are filing-supported. | 10-K | 10-K business overview financial:AAPL:2026-06-30:001 | 2025-10-31 | medium | none |
| Risk discussion is available from annual and quarterly filings. | 10-K / 10-Q | risk factors | 2025-10-31 | medium | none |
| Liquidity review is supported by the 10-Q liquidity section. | 10-Q | liquidity and capital resources | available | medium | none |
| Formal guidance evidence is limited. | 8-K | Exhibit 99.1 | available if extracted | low | Exhibit 99.1 available for earnings-release claims. |
| Capex and contractual obligations require caution. | 10-K / 10-Q | commitments / capex | mixed | low-to-medium | commitments/capex section unavailable in extracted AAPL filings. |

## Evidence gaps

MD&A extraction is unavailable in the current section records, and investor presentation coverage is unavailable. The report therefore cites specific sections and avoids unsupported management-commentary claims.

## Memory Update

* Durable facts to retain: AAPL financial_report_analyst used financial:AAPL:2026-06-30:001 for this 2026-06-30 validation run.
* Prior mistake to avoid: Do not override current evidence with template language.
* Open questions: Refresh evidence for any later trade date.
* Evidence references: financial:AAPL:2026-06-30:001
* Staleness / expiry: Expires after 2026-06-30.
