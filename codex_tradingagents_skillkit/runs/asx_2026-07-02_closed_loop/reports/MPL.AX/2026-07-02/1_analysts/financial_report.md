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
| financial:MPL.AX:2026-07-02:016 | asx_fallback_document | sector_metric_premium_growth | 2025-12-31 | available | premiums, or products or services from our health and wellbeing partners. To help ease the burden of last year |
| financial:MPL.AX:2026-07-02:017 | asx_fallback_document | sector_metric_claims_ratio | 2025-12-31 | available | claims expense (including risk equalisation) (6,814.6) (6,595.8) 3.3% Gross profit 1,396.4 1,307. 2 6.8% Manag |
| financial:MPL.AX:2026-07-02:018 | asx_fallback_document | sector_metric_membership | 2025-12-31 | available | policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholder |
| financial:MPL.AX:2026-07-02:019 | asx_fallback_document | sector_metric_capital_adequacy | 2025-12-31 | available | capital adequacy requirement of $250 million for Medibank, with effect from 1 July 2023, following a review of |

## Claim-Source Table
| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Official ASX financial-report context | financial:MPL.AX:2026-07-02:001 ASX document | revenue_income_npat | 2025-12-31 | medium | none |
| Management discussion / outlook support | financial:MPL.AX:2026-07-02:003 ASX document | management_discussion_analysis | 2025-12-31 | medium | none |
| Liquidity / cash-debt evidence | financial:MPL.AX:2026-07-02:007 ASX document | cash_debt_gearing | 2025-12-31 | medium | none |
| Segment/product evidence | financial:MPL.AX:2026-07-02:008 ASX document | segment_product_performance | 2025-12-31 | medium | none |
| Cash-flow evidence | financial:MPL.AX:2026-07-02:004 ASX document | cash_flow_statement | 2025-12-31 | medium | none |
| ASX sector metric: Premium growth | financial:MPL.AX:2026-07-02:016 ASX section record | sector_metric_premium_growth | 2025-12-31 | medium | none |
| ASX sector metric: Claims ratio | financial:MPL.AX:2026-07-02:017 ASX section record | sector_metric_claims_ratio | 2025-12-31 | medium | none |
| ASX sector metric: Membership | financial:MPL.AX:2026-07-02:018 ASX section record | sector_metric_membership | 2025-12-31 | medium | none |
| ASX sector metric: Capital adequacy | financial:MPL.AX:2026-07-02:019 ASX section record | sector_metric_capital_adequacy | 2025-12-31 | medium | none |

## ASX Sector Metric Evidence
| Evidence ID | Sector | Metric | Status | Confidence | Evidence gap |
|---|---|---|---|---|---|
| financial:MPL.AX:2026-07-02:016 | health_insurers | Premium growth | available | medium | none |
| financial:MPL.AX:2026-07-02:017 | health_insurers | Claims ratio | available | medium | none |
| financial:MPL.AX:2026-07-02:018 | health_insurers | Membership | available | medium | none |
| financial:MPL.AX:2026-07-02:019 | health_insurers | Capital adequacy | available | medium | none |

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
