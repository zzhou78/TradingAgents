# Financial Report Analyst Report - CBA.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:CBA.AX:2026-07-02:014 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | profit after tax (NPAT) 7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Lev |
| financial:CBA.AX:2026-07-02:012 | asx_fallback_document | material_risks | 2025-12-31 | available | risk framework, together with a strong culture, empowers our people to take the right risks to deliver better |
| financial:CBA.AX:2026-07-02:016 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | Outlook We know many of our customers are still cautious with global volatility creating uncertainty. The Aust |
| financial:CBA.AX:2026-07-02:021 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | NIM) is an important measure of our financial performance. It represents the return on our interest earning as |
| financial:CBA.AX:2026-07-02:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | cash Interest rates & fees Help & support Locate us Contact us About us / Investors / Reporting / 2025 Annual |
| financial:CBA.AX:2026-07-02:017 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | cash flows in any given year. Series of severe cyclones over South-East Queensland Assumes two severe cyclones |
| financial:CBA.AX:2026-07-02:014 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | profit after tax (NPAT) 7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Lev |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Quarterly revenue and earnings context | financial:CBA.AX:2026-07-02:014 8-K | Exhibit 99.1 | 2025-12-31 | medium | none |
| Management discussion supports operating trend review | financial:CBA.AX:2026-07-02:016 10-Q | 10-Q MD&A | 2025-12-31 | medium | none |
| Liquidity appears supported by company cash resources and access to markets | financial:CBA.AX:2026-07-02:007 10-Q | Liquidity and capital resources | 2025-12-31 | medium | none |
| Segment/product mix is available for specialist interpretation | financial:CBA.AX:2026-07-02:021 10-Q | Segment/product revenue tables | 2025-12-31 | medium | none |
| Cash-flow statement is available for operating cash flow and capital return review | financial:CBA.AX:2026-07-02:017 10-Q | Cash flow statement | 2025-12-31 | medium | none |
| Risk factors require caution around company-specific uncertainties | financial:CBA.AX:2026-07-02:012 10-K | Risk factors | 2025-12-31 | medium | none |
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
* Evidence references: financial:CBA.AX:2026-07-02:014, financial:CBA.AX:2026-07-02:016, financial:CBA.AX:2026-07-02:017
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
