# Financial Report Analyst Report - WOW.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:WOW.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | Revenue 1.7 to 69,077 Profit after tax attributable to equity holders of the parent entity before significant |
| financial:WOW.AX:2026-07-06:012 | asx_fallback_document | material_risks | 2025-12-31 | available | impairment of $346 million, MyDeal impairment and closure costs of $52 million, Healthylife impairment of $17 |
| financial:WOW.AX:2026-07-06:003 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | Financial Review are featured on pages 2–79 of this report and the information in these sections has been veri |
| financial:WOW.AX:2026-07-06:008 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | segment. Group NPAT declined by a normalised 17.1% 1 reflecting lower earnings and higher net finance costs. T |
| financial:WOW.AX:2026-07-06:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all |
| financial:WOW.AX:2026-07-06:004 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all |
| financial:WOW.AX:2026-07-06:001 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | Revenue 1.7 to 69,077 Profit after tax attributable to equity holders of the parent entity before significant |
| financial:WOW.AX:2026-07-06:016 | asx_fallback_document | sector_metric_sales_growth | 2025-12-31 | available | __TABLE_ROW__ page=35 table=1001 row=13 title=pdfplumber_words / Total sales / 51,452 / 50,823 / 1.2% / |
| financial:WOW.AX:2026-07-06:017 | asx_fallback_document | sector_metric_comparable_sales_if_available | 2025-12-31 | available | Excluding the impact of these divestments, H2 sales increased by 6.9% with comparable sales growth of approxim |
| financial:WOW.AX:2026-07-06:018 | asx_fallback_document | sector_metric_ebit_margin | 2025-12-31 | available | Australian Food F25 EBIT of $2,753 million declined by a normalised 10.5% with the EBIT margin decreasing by a |
| financial:WOW.AX:2026-07-06:019 | asx_fallback_document | sector_metric_inventory | 2025-12-31 | available | Decrease in inventories of $44 million reflects lower inventory holdings in Australian Food, New Zealand Food |
| financial:WOW.AX:2026-07-06:020 | asx_fallback_document | sector_metric_capex | 2025-12-31 | available | 2025 (52 WEEKS) AUSTRALIAN FOOD $M AUSTRALIAN B2B $M NEW ZEALAND FOOD $M W LIVING $M OTHER $M ELIMINATIONS/ RE |
| financial:WOW.AX:2026-07-06:021 | asx_fallback_document | sector_metric_dividends | 2025-12-31 | available | __TABLE_ROW__ page=34 table=2 row=21 title=pdfplumber_crop_balance_sheet_text_table_2 / and dividends /  /  / |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:WOW.AX:2026-07-06:001 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:WOW.AX:2026-07-06:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:WOW.AX:2026-07-06:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:WOW.AX:2026-07-06:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:WOW.AX:2026-07-06:004 ASX document | cash_flow_statement | 2025-12-31 | medium | none |
| ASX sector metric: sales growth | financial:WOW.AX:2026-07-06:016 ASX section record | sector_metric_sales_growth | 2025-12-31 | medium | none |
| ASX sector metric: comparable sales | financial:WOW.AX:2026-07-06:017 ASX section record | sector_metric_comparable_sales_if_available | 2025-12-31 | medium | none |
| ASX sector metric: EBIT margin | financial:WOW.AX:2026-07-06:018 ASX section record | sector_metric_ebit_margin | 2025-12-31 | medium | none |
| ASX sector metric: inventory | financial:WOW.AX:2026-07-06:019 ASX section record | sector_metric_inventory | 2025-12-31 | medium | none |
| ASX sector metric: capex | financial:WOW.AX:2026-07-06:020 ASX section record | sector_metric_capex | 2025-12-31 | low | none |
| ASX sector metric: dividend | financial:WOW.AX:2026-07-06:021 ASX section record | sector_metric_dividends | 2025-12-31 | medium | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| financial:WOW.AX:2026-07-06:016 | retailers | sales growth | available | medium | none |
| financial:WOW.AX:2026-07-06:017 | retailers | comparable sales | available | medium | none |
| financial:WOW.AX:2026-07-06:018 | retailers | EBIT margin | available | medium | none |
| financial:WOW.AX:2026-07-06:019 | retailers | inventory | available | medium | none |
| financial:WOW.AX:2026-07-06:020 | retailers | capex | available | low | none |
| financial:WOW.AX:2026-07-06:021 | retailers | dividend | available | medium | none |

## Evidence gaps
- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.
- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.
- Guidance is not inferred unless explicitly found in the extracted ASX document section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:WOW.AX:2026-07-06:001, financial:WOW.AX:2026-07-06:003, financial:WOW.AX:2026-07-06:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
