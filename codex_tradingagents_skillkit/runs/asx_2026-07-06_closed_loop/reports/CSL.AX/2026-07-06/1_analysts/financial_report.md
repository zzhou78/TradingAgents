# Financial Report Analyst Report - CSL.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:CSL.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 C |
| financial:CSL.AX:2026-07-06:012 | asx_fallback_document | material_risks | 2025-12-31 | available | risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief |
| financial:CSL.AX:2026-07-06:003 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Ris |
| financial:CSL.AX:2026-07-06:008 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | segment. This growth is driven by demographic trends such as an aging population, the increasing prevalence of |
| financial:CSL.AX:2026-07-06:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | Cash, equity and debt for future growth 14 Performance WHAT CSL DOES THE VALUE CSL CREATES Provide a safe, rew |
| financial:CSL.AX:2026-07-06:019 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciatio |
| financial:CSL.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 C |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:CSL.AX:2026-07-06:001 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:CSL.AX:2026-07-06:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:CSL.AX:2026-07-06:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:CSL.AX:2026-07-06:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:CSL.AX:2026-07-06:019 ASX document | cash_flow_statement | 2025-12-31 | medium | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| none | ASX | sector metrics | unavailable | low | no ASX sector metric records extracted |

## Evidence gaps
- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.
- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.
- Guidance is not inferred unless explicitly found in the extracted ASX document section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:CSL.AX:2026-07-06:001, financial:CSL.AX:2026-07-06:003, financial:CSL.AX:2026-07-06:019
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
