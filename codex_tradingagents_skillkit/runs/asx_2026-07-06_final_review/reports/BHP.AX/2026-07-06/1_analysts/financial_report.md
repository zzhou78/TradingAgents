# Financial Report Analyst Report - BHP.AX

## Tool Outputs Used
- financial_report/section_records.json section-level filing extraction.
- fundamentals/statement_records.json as structured fundamentals packet context.

## Source coverage table
| Evidence ID | Source type | Section / exhibit | Filing date | Status | Short excerpt |
|---|---|---|---|---|---|
| financial:BHP.AX:2026-07-06:016 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | income and retirement. Over the past five years, BHP has delivered more than US$50 billion in cash dividends t |
| financial:BHP.AX:2026-07-06:012 | asx_fallback_document | material_risks | 2025-12-31 | available | risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulator |
| financial:BHP.AX:2026-07-06:003 | asx_fallback_document | management_discussion_analysis | 2025-12-31 | available | outlook Ethics and Business Conduct Competition law compliance Industry associations Interacting with governme |
| financial:BHP.AX:2026-07-06:008 | asx_fallback_document | segment_product_performance | 2025-12-31 | available | production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 pro |
| financial:BHP.AX:2026-07-06:007 | asx_fallback_document | cash_debt_gearing | 2025-12-31 | available | Debt investors Consensus estimates Sustainability approach Value chain sustainability Nature and environmental |
| financial:BHP.AX:2026-07-06:004 | asx_fallback_document | cash_flow_statement | 2025-12-31 | available | operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per c |
| financial:BHP.AX:2026-07-06:016 | asx_fallback_document | revenue_income_npat | 2025-12-31 | available | income and retirement. Over the past five years, BHP has delivered more than US$50 billion in cash dividends t |
| financial:BHP.AX:2026-07-06:031 | asx_fallback_document | sector_metric_production | 2025-12-31 | available | production record 263 Mt ^1% on FY2024 Western Australia Iron Ore (WAIO) is the lowest-cost major iron ore pro |
| financial:BHP.AX:2026-07-06:032 | asx_fallback_document | sector_metric_realised_price | 2025-12-31 | available | re 4,392 3,711 Underlying ROCE 17% 13% Total copper production (kt) 2,017 1,865 Average realised prices Copper |
| financial:BHP.AX:2026-07-06:033 | asx_fallback_document | sector_metric_unit_cost_aisc | 2025-12-31 | available | Production for FY2026 is expected to increase to between 18 and 20 Mt (36 and 40 Mt on a 100 per cent basis), |
| financial:BHP.AX:2026-07-06:034 | asx_fallback_document | sector_metric_capex | 2025-12-31 | available | investing cash flows (13,350) (8,762) (13,065) Net financing cash flows (5,971) (11,669) (10,315) Net (decreas |
| financial:BHP.AX:2026-07-06:035 | asx_fallback_document | sector_metric_reserves_resources | 2025-12-31 | available | Total reserves (2) (15) 13 Summarised financial information relating to each of the Group’s subsidiaries with |
| financial:BHP.AX:2026-07-06:036 | asx_fallback_document | sector_metric_commodity_exposure | 2025-12-31 | available | Examples of forward-looking statements contained in this Report include, without limitation, statements descri |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:BHP.AX:2026-07-06:016 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:BHP.AX:2026-07-06:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:BHP.AX:2026-07-06:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:BHP.AX:2026-07-06:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:BHP.AX:2026-07-06:004 ASX document | cash_flow_statement | 2025-12-31 | medium | none |
| ASX sector metric: production | financial:BHP.AX:2026-07-06:031 ASX section record | sector_metric_production | 2025-12-31 | medium | none |
| ASX sector metric: realised price | financial:BHP.AX:2026-07-06:032 ASX section record | sector_metric_realised_price | 2025-12-31 | medium | none |
| ASX sector metric: unit cost | financial:BHP.AX:2026-07-06:033 ASX section record | sector_metric_unit_cost_aisc | 2025-12-31 | medium | none |
| ASX sector metric: capex | financial:BHP.AX:2026-07-06:034 ASX section record | sector_metric_capex | 2025-12-31 | medium | none |
| ASX sector metric: reserves | financial:BHP.AX:2026-07-06:035 ASX section record | sector_metric_reserves_resources | 2025-12-31 | low | none |
| ASX sector metric: commodity exposure | financial:BHP.AX:2026-07-06:036 ASX section record | sector_metric_commodity_exposure | 2025-12-31 | medium | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| financial:BHP.AX:2026-07-06:031 | miners | production | available | medium | none |
| financial:BHP.AX:2026-07-06:032 | miners | realised price | available | medium | none |
| financial:BHP.AX:2026-07-06:033 | miners | unit cost | available | medium | none |
| financial:BHP.AX:2026-07-06:034 | miners | capex | available | medium | none |
| financial:BHP.AX:2026-07-06:035 | miners | reserves | available | low | none |
| financial:BHP.AX:2026-07-06:036 | miners | commodity exposure | available | medium | none |

## Evidence gaps
- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.
- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.
- Guidance is not inferred unless explicitly found in the extracted ASX document section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:BHP.AX:2026-07-06:016, financial:BHP.AX:2026-07-06:003, financial:BHP.AX:2026-07-06:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
