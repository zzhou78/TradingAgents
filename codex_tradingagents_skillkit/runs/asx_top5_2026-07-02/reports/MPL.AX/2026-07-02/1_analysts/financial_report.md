# Financial Report Analyst Report - MPL.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:MPL.AX:2026-07-02:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | income 73 Consolidated statement of financial position 74 Consolidated statement of changes in equity 75 Conso |
| financial:MPL.AX:2026-07-02:012 | asx_fallback_document | material_risks | 2025-12-31 | available | Risk management 41 Directors’ report 47 Remuneration report 50 Financial report 72 Consolidated statement of c |
| financial:MPL.AX:2026-07-02:003 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | Operating and financial review 25 Directors 34 Executive leadership team 37 Corporate governance 39 Risk manag |
| financial:MPL.AX:2026-07-02:008 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14. |
| financial:MPL.AX:2026-07-02:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 D |
| financial:MPL.AX:2026-07-02:004 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | Consolidated statement of cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity |
| financial:MPL.AX:2026-07-02:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | income 73 Consolidated statement of financial position 74 Consolidated statement of changes in equity 75 Conso |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Quarterly revenue and earnings context | financial:MPL.AX:2026-07-02:001 8-K | Exhibit 99.1 | 2025-12-31 | medium | none |
| Management discussion supports operating trend review | financial:MPL.AX:2026-07-02:003 10-Q | 10-Q MD&A | 2025-12-31 | medium | none |
| Liquidity appears supported by company cash resources and access to markets | financial:MPL.AX:2026-07-02:007 10-Q | Liquidity and capital resources | 2025-12-31 | medium | none |
| Segment/product mix is available for specialist interpretation | financial:MPL.AX:2026-07-02:008 10-Q | Segment/product revenue tables | 2025-12-31 | medium | none |
| Cash-flow statement is available for operating cash flow and capital return review | financial:MPL.AX:2026-07-02:004 10-Q | Cash flow statement | 2025-12-31 | medium | none |
| Risk factors require caution around company-specific uncertainties | financial:MPL.AX:2026-07-02:012 10-K | Risk factors | 2025-12-31 | medium | none |
| Formal guidance detail | structured fundamentals packet | unavailable section / exhibit if not in Exhibit 99.1 | 2026-07-02 | low | explicit evidence gap if guidance not in extracted exhibit |
| Capex commitments / contractual obligations | 10-K/10-Q | unavailable commitments/capex section | 2026-07-02 | low | evidence gap: commitments/capex section marked unavailable where not extracted |

## Evidence gaps
- Do not treat an 8-K cover page as the earnings release; the earnings-release claim uses Exhibit 99.1 when available.
- Commitments / capex / contractual-obligations sections are gap-labelled when extraction marked them unavailable.
- Guidance is not inferred unless explicitly found in the extracted exhibit or filing section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:MPL.AX:2026-07-02:001, financial:MPL.AX:2026-07-02:003, financial:MPL.AX:2026-07-02:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
