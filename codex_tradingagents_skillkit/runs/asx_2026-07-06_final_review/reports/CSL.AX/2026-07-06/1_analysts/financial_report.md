# Financial Report Analyst Report - CSL.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:CSL.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../9 |
| financial:CSL.AX:2026-07-06:012 | asx_fallback_document | material_risks | 2025-12-31 | available | risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief |
| financial:CSL.AX:2026-07-06:003 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | Outlook ../18/ Anchor Global Manufacturing Presence ../20/ Anchor Platforms, Therapeutic Areas and Product Por |
| financial:CSL.AX:2026-07-06:008 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | Segment Information 96 Note 2: Business Disposals 99 Note Page metadata Shareholder Information CSL’s 20 large |
| financial:CSL.AX:2026-07-06:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statem |
| financial:CSL.AX:2026-07-06:004 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidate |
| financial:CSL.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../9 |
| financial:CSL.AX:2026-07-06:016 | asx_fallback_document | sector_metric_segment_revenue | 2025-12-31 | available | US$11,158m CSL Behring revenue US$2,166m CSL Seqirus revenue US$2,234m CSL Vifor revenue Cashflow from operati |
| financial:CSL.AX:2026-07-06:017 | asx_fallback_document | sector_metric_r_and_d | 2025-12-31 | available | R&D investment US$ million 1,266†^ 1,428¶^ 1,359¶^ 106 Clinical trials in operation Number 60 60 59 30 Safety |
| financial:CSL.AX:2026-07-06:018 | asx_fallback_document | sector_metric_plasma_collections | 2025-12-31 | available | + READ MORE PAGE 18 INNOVATION EXCELLENCE AND INNOVATION CSL is one of the world’s largest collectors of human |
| financial:CSL.AX:2026-07-06:019 | asx_fallback_document | sector_metric_margins | 2025-12-31 | available | + READ MORE ABOUT CSL’S R&D PIPELINE AT WWW.CSL.COM/RESEARCH-ANDDEVELOPMENT/PRODUCT-PIPELINE NPATA attributabl |
| financial:CSL.AX:2026-07-06:020 | asx_fallback_document | sector_metric_debt | 2025-12-31 | available | assets 11 203 163 Other non-current assets 14 189 158 Total Non-Current Assets 27,554 27,254 TOTAL ASSETS 39,4 |
| financial:CSL.AX:2026-07-06:021 | asx_fallback_document | sector_metric_guidance | 2025-12-31 | available | While these changes are among the most significant for our company in the last 20 years, the Board and managem |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:CSL.AX:2026-07-06:001 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:CSL.AX:2026-07-06:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:CSL.AX:2026-07-06:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:CSL.AX:2026-07-06:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:CSL.AX:2026-07-06:004 ASX document | cash_flow_statement | 2025-12-31 | medium | none |
| ASX sector metric: segment revenue | financial:CSL.AX:2026-07-06:016 ASX section record | sector_metric_segment_revenue | 2025-12-31 | medium | none |
| ASX sector metric: R&D | financial:CSL.AX:2026-07-06:017 ASX section record | sector_metric_r_and_d | 2025-12-31 | medium | none |
| ASX sector metric: plasma collections | financial:CSL.AX:2026-07-06:018 ASX section record | sector_metric_plasma_collections | 2025-12-31 | medium | none |
| ASX sector metric: margin | financial:CSL.AX:2026-07-06:019 ASX section record | sector_metric_margins | 2025-12-31 | medium | none |
| ASX sector metric: net debt | financial:CSL.AX:2026-07-06:020 ASX section record | sector_metric_debt | 2025-12-31 | medium | none |
| ASX sector metric: guidance | financial:CSL.AX:2026-07-06:021 ASX section record | sector_metric_guidance | 2025-12-31 | medium | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| financial:CSL.AX:2026-07-06:016 | healthcare | segment revenue | available | medium | none |
| financial:CSL.AX:2026-07-06:017 | healthcare | R&D | available | medium | none |
| financial:CSL.AX:2026-07-06:018 | healthcare | plasma collections | available | medium | none |
| financial:CSL.AX:2026-07-06:019 | healthcare | margin | available | medium | none |
| financial:CSL.AX:2026-07-06:020 | healthcare | net debt | available | medium | none |
| financial:CSL.AX:2026-07-06:021 | healthcare | guidance | available | medium | none |

## Evidence gaps
- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.
- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.
- Guidance is not inferred unless explicitly found in the extracted ASX document section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:CSL.AX:2026-07-06:001, financial:CSL.AX:2026-07-06:003, financial:CSL.AX:2026-07-06:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
