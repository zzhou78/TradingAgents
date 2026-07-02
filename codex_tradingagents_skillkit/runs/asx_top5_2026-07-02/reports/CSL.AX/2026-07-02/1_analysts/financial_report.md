# Financial Report Analyst Report - CSL.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:CSL.AX:2026-07-02:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 C |
| financial:CSL.AX:2026-07-02:012 | asx_fallback_document | material_risks | 2025-12-31 | available | risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief |
| financial:CSL.AX:2026-07-02:003 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Ris |
| financial:CSL.AX:2026-07-02:008 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | segment. This growth is driven by demographic trends such as an aging population, the increasing prevalence of |
| financial:CSL.AX:2026-07-02:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | Cash, equity and debt for future growth 14 Performance WHAT CSL DOES THE VALUE CSL CREATES Provide a safe, rew |
| financial:CSL.AX:2026-07-02:069 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciatio |
| financial:CSL.AX:2026-07-02:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 C |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Quarterly revenue and earnings context | financial:CSL.AX:2026-07-02:001 8-K | Exhibit 99.1 | 2025-12-31 | medium | none |
| Management discussion supports operating trend review | financial:CSL.AX:2026-07-02:003 10-Q | 10-Q MD&A | 2025-12-31 | medium | none |
| Liquidity appears supported by company cash resources and access to markets | financial:CSL.AX:2026-07-02:007 10-Q | Liquidity and capital resources | 2025-12-31 | medium | none |
| Segment/product mix is available for specialist interpretation | financial:CSL.AX:2026-07-02:008 10-Q | Segment/product revenue tables | 2025-12-31 | medium | none |
| Cash-flow statement is available for operating cash flow and capital return review | financial:CSL.AX:2026-07-02:069 10-Q | Cash flow statement | 2025-12-31 | medium | none |
| Risk factors require caution around company-specific uncertainties | financial:CSL.AX:2026-07-02:012 10-K | Risk factors | 2025-12-31 | medium | none |
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
* Evidence references: financial:CSL.AX:2026-07-02:001, financial:CSL.AX:2026-07-02:003, financial:CSL.AX:2026-07-02:069
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
