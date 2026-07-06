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
| financial:CSL.AX:2026-07-06:025 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciatio |
| financial:CSL.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 C |
| financial:CSL.AX:2026-07-06:016 | asx_fallback_document | sector_metric_segment_revenue | 2025-12-31 | unavailable |  |
| financial:CSL.AX:2026-07-06:017 | asx_fallback_document | sector_metric_r_and_d | 2025-12-31 | available | + READ MORE ABOUT CSL’S R&D PIPELINE AT WWW.CSL.COM/RESEARCH-ANDDEVELOPMENT/PRODUCT-PIPELINE NPATA attributabl |
| financial:CSL.AX:2026-07-06:018 | asx_fallback_document | sector_metric_plasma_collections | 2025-12-31 | available | In plasma collection the focus is on three areas; enhancing collection efficiency, reducing the unit acquisiti |
| financial:CSL.AX:2026-07-06:019 | asx_fallback_document | sector_metric_margins | 2025-12-31 | available | CODE OF RESPONSIBLE BUSINESS PRACTICE SALES, MARKETING, POLICY EARLY STAGE RESEARCH MANUFACTURING PRODUCT DEVE |
| financial:CSL.AX:2026-07-06:020 | asx_fallback_document | sector_metric_debt | 2025-12-31 | available | CODE OF RESPONSIBLE BUSINESS PRACTICE SALES, MARKETING, POLICY EARLY STAGE RESEARCH MANUFACTURING PRODUCT DEVE |
| financial:CSL.AX:2026-07-06:021 | asx_fallback_document | sector_metric_guidance | 2025-12-31 | available | + READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$11,158m CSL Behring revenue 16 Performance Th |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:CSL.AX:2026-07-06:001 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:CSL.AX:2026-07-06:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:CSL.AX:2026-07-06:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:CSL.AX:2026-07-06:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:CSL.AX:2026-07-06:025 ASX document | cash_flow_statement | 2025-12-31 | medium | none |
| ASX sector metric: segment revenue | financial:CSL.AX:2026-07-06:016 ASX section record | sector_metric_segment_revenue | 2025-12-31 | low | segment revenue was not identified in selected eligible ASX financial documents. |
| ASX sector metric: R&D | financial:CSL.AX:2026-07-06:017 ASX section record | sector_metric_r_and_d | 2025-12-31 | low | none |
| ASX sector metric: plasma collections | financial:CSL.AX:2026-07-06:018 ASX section record | sector_metric_plasma_collections | 2025-12-31 | low | none |
| ASX sector metric: margin | financial:CSL.AX:2026-07-06:019 ASX section record | sector_metric_margins | 2025-12-31 | low | none |
| ASX sector metric: net debt | financial:CSL.AX:2026-07-06:020 ASX section record | sector_metric_debt | 2025-12-31 | low | none |
| ASX sector metric: guidance | financial:CSL.AX:2026-07-06:021 ASX section record | sector_metric_guidance | 2025-12-31 | low | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| financial:CSL.AX:2026-07-06:016 | healthcare | segment revenue | unavailable | low | segment revenue was not identified in selected eligible ASX financial documents. |
| financial:CSL.AX:2026-07-06:017 | healthcare | R&D | available | low | none |
| financial:CSL.AX:2026-07-06:018 | healthcare | plasma collections | available | low | none |
| financial:CSL.AX:2026-07-06:019 | healthcare | margin | available | low | none |
| financial:CSL.AX:2026-07-06:020 | healthcare | net debt | available | low | none |
| financial:CSL.AX:2026-07-06:021 | healthcare | guidance | available | low | none |

## Evidence gaps
- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.
- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.
- Guidance is not inferred unless explicitly found in the extracted ASX document section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:CSL.AX:2026-07-06:001, financial:CSL.AX:2026-07-06:003, financial:CSL.AX:2026-07-06:025
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
