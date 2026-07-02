# Financial Report Analyst Report - AAPL

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:AAPL:2026-07-02:001 | annual_report_10k | 10-K business overview | 2025-10-31 | available | Item 1. Business 1 |
| financial:AAPL:2026-07-02:002 | annual_report_10k | 10-K risk factors | 2025-10-31 | available | Item 1A. Risk Factors 5 |
| financial:AAPL:2026-07-02:013 | quarterly_report_10q | 10-Q MD&A | 2026-05-01 | available | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations 13 |
| financial:AAPL:2026-07-02:015 | quarterly_report_10q | 10-Q segment/product revenue tables | 2026-05-01 | available | net sales by reportable segment for the three- and six-month periods ended March 28, 2026 and March 29, 2025 ( |
| financial:AAPL:2026-07-02:016 | quarterly_report_10q | 10-Q liquidity and capital resources | 2026-05-01 | available | Liquidity and Capital Resources The Company believes its balances of cash, cash equivalents and marketable sec |
| financial:AAPL:2026-07-02:020 | quarterly_report_10q | 10-Q cash flow statement | 2026-05-01 | available | CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS (Unaudited) (In millions) Six Months Ended March 28, 2026 Marc |
| financial:AAPL:2026-07-02:022 | earnings_release_exhibit | Exhibit 99.1 | 2026-04-30 | available | EX-99.1 2 a8-kex991q2202603282026.htm EX-99.1 Document Exhibit 99.1 Apple reports second quarter results March |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Quarterly revenue and earnings context | financial:AAPL:2026-07-02:022 8-K | Exhibit 99.1 | 2026-04-30 | medium | none |
| Management discussion supports operating trend review | financial:AAPL:2026-07-02:013 10-Q | 10-Q MD&A | 2026-05-01 | medium | none |
| Liquidity appears supported by company cash resources and access to markets | financial:AAPL:2026-07-02:016 10-Q | Liquidity and capital resources | 2026-05-01 | medium | none |
| Segment/product mix is available for specialist interpretation | financial:AAPL:2026-07-02:015 10-Q | Segment/product revenue tables | 2026-05-01 | medium | none |
| Cash-flow statement is available for operating cash flow and capital return review | financial:AAPL:2026-07-02:020 10-Q | Cash flow statement | 2026-05-01 | medium | none |
| Risk factors require caution around company-specific uncertainties | financial:AAPL:2026-07-02:002 10-K | Risk factors | 2025-10-31 | medium | none |
| Formal guidance detail | structured fundamentals packet | unavailable section / exhibit if not in Exhibit 99.1 | 2026-07-02 | low | explicit evidence gap if guidance not in extracted exhibit |
| Capex commitments / contractual obligations | 10-K/10-Q | unavailable commitments/capex section | 2026-07-02 | low | evidence gap: commitments/capex section marked unavailable where not extracted |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| not applicable | US technology | not applicable | unavailable | low | ASX sector metric extraction not applicable |

## Evidence gaps
- Do not treat an 8-K cover page as the earnings release; the earnings-release claim uses Exhibit 99.1 when available.
- Commitments / capex / contractual-obligations sections are gap-labelled when extraction marked them unavailable.
- Guidance is not inferred unless explicitly found in the extracted exhibit or filing section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:AAPL:2026-07-02:022, financial:AAPL:2026-07-02:013, financial:AAPL:2026-07-02:020
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
