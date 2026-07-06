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
| financial:MPL.AX:2026-07-02:016 | asx_fallback_document | sector_metric_premium_growth | 2025-12-31 | available | r for the 4th year running. Our Live Better rewards members redeemed around $33 million in rewards points this |
| financial:MPL.AX:2026-07-02:017 | asx_fallback_document | sector_metric_claims_ratio | 2025-12-31 | available | .5% to 22.5 cents per share. The key reasons for the movements in the Health Insurance and Medibank Health res |
| financial:MPL.AX:2026-07-02:018 | asx_fallback_document | sector_metric_membership | 2025-12-31 | available | tomers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3 |
| financial:MPL.AX:2026-07-02:019 | asx_fallback_document | sector_metric_capital_adequacy | 2025-12-31 | available | dividend Medibank’s capital management objective is to maintain a strong financial risk profile and capacity t |
| financial:MPL.AX:2026-07-02:020 | asx_fallback_document | sector_metric_operating_profit_or_margin | 2025-12-31 | available | advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:MPL.AX:2026-07-02:001 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:MPL.AX:2026-07-02:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:MPL.AX:2026-07-02:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:MPL.AX:2026-07-02:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:MPL.AX:2026-07-02:004 ASX document | cash_flow_statement | 2025-12-31 | medium | none |
| ASX sector metric: premium growth | financial:MPL.AX:2026-07-02:016 ASX section record | sector_metric_premium_growth | 2025-12-31 | low | none |
| ASX sector metric: claims ratio | financial:MPL.AX:2026-07-02:017 ASX section record | sector_metric_claims_ratio | 2025-12-31 | medium | none |
| ASX sector metric: membership | financial:MPL.AX:2026-07-02:018 ASX section record | sector_metric_membership | 2025-12-31 | medium | none |
| ASX sector metric: capital adequacy | financial:MPL.AX:2026-07-02:019 ASX section record | sector_metric_capital_adequacy | 2025-12-31 | medium | none |
| ASX sector metric: operating profit | financial:MPL.AX:2026-07-02:020 ASX section record | sector_metric_operating_profit_or_margin | 2025-12-31 | medium | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| financial:MPL.AX:2026-07-02:016 | health_insurers | premium growth | available | low | none |
| financial:MPL.AX:2026-07-02:017 | health_insurers | claims ratio | available | medium | none |
| financial:MPL.AX:2026-07-02:018 | health_insurers | membership | available | medium | none |
| financial:MPL.AX:2026-07-02:019 | health_insurers | capital adequacy | available | medium | none |
| financial:MPL.AX:2026-07-02:020 | health_insurers | operating profit | available | medium | none |

## Evidence gaps
- ASX financial-report claims use official ASX/company IR section records and sector metrics, not SEC exhibit assumptions.
- Sector-specific metrics are either cited as available or explicitly gap-labelled with low confidence.
- Guidance is not inferred unless explicitly found in the extracted ASX document section.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: financial:MPL.AX:2026-07-02:001, financial:MPL.AX:2026-07-02:003, financial:MPL.AX:2026-07-02:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
