# Financial Report Analyst: AAPL

## Source coverage table

| Source | Status | Use in this report | Confidence impact |
|---|---|---|---|
| Structured fundamentals packet | Available | TTM revenue, income, free cash flow, margins, leverage, liquidity, valuation | Medium |
| Latest annual report / 10-K | Available: filed 2025-10-31 | Business overview, risk factors, segment/product revenue tables, liquidity, financial statements | Raises confidence |
| Latest quarterly report / 10-Q | Available: filed 2026-05-01 | March 2026 risk factors, segment/product revenue tables, liquidity, financial statements | Raises confidence |
| Latest earnings 8-K cover page | Available: Item 2.02 filed 2026-04-30 | Confirms the earnings release source and Exhibit 99.1 routing | Medium |
| 8-K Exhibit 99.1 | Available | Earnings-release revenue, EPS, product/services sales, operating cash flow, dividend, and buyback details | Raises confidence |
| Investor presentation | Not discovered from SEC submissions feed | Not used | Lowers confidence for presentation-specific claims |

## Claim-source table

| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap if section/exhibit is missing |
|---|---|---|---|---|---|
| Quarterly revenue grew 17% year over year to 111.2B | 8-K earnings release; 10-Q | Exhibit 99.1; 10-Q income statement | 2026-04-30; 2026-05-01 | High | None for revenue amount; 10-Q MD&A was not extracted |
| Product/services split was 80.208B / 30.976B in the March quarter | 8-K earnings release; 10-Q | Exhibit 99.1; 10-Q segment/product revenue tables | 2026-04-30; 2026-05-01 | High | None for extracted product/services table |
| Liquidity remains adequate for cash needs and capital return | 10-Q | Liquidity and capital resources; balance sheet | 2026-05-01 | High | None for liquidity; investor presentation unavailable |
| Supplier/manufacturing obligations are material | 10-Q liquidity section | Liquidity and capital resources | 2026-05-01 | Medium | Dedicated commitments/capex section was not extracted |
| Formal numerical guidance | 8-K earnings release | Exhibit 99.1 | 2026-04-30 | Low | Exhibit excerpt includes commentary and forward-looking risk language, not a formal guidance table |
| Material risk factors | 10-K and 10-Q | Risk factors | 2025-10-31; 2026-05-01 | High | None for formal risk-factor section |
| Cash-flow quality is strong | 8-K earnings release; 10-Q | Exhibit 99.1; cash flow statement | 2026-04-30; 2026-05-01 | High | None for operating cash-flow evidence |

## Revenue and segment performance

Structured evidence shows TTM revenue of 451.4B. Exhibit 99.1 reports March-quarter revenue of 111.2B, up 17% year over year, and the extracted 10-Q income statement supports the same quarterly revenue base. Exhibit 99.1 and the 10-Q segment/product revenue tables show product net sales of 80.208B and services net sales of 30.976B for the quarter. (Source: structured fundamentals packet; 8-K Exhibit 99.1; 10-Q income statement; 10-Q segment/product revenue tables)

## Margin and profitability trend

Apple shows high profitability in the structured packet: net income 122.6B, profit margin 27.15%, operating margin 32.28%, and ROE 1.41. Exhibit 99.1 reports diluted EPS of 2.01, up 22% year over year, and includes condensed statement-of-operations detail that supports margin review. (Source: structured fundamentals packet; 8-K Exhibit 99.1; 10-Q income statement)

## Cash flow quality

Free cash flow is 101.1B in the structured packet. Exhibit 99.1 states the March quarter generated over 28B in operating cash flow, and the 10-Q cash-flow statement section is available for statement-level support. This supports strong cash-generation quality. (Source: structured fundamentals packet; 8-K Exhibit 99.1; 10-Q cash flow statement)

## Capex and investment commitments

The 10-Q liquidity section reports manufacturing purchase obligations of 44.6B and other purchase obligations of 30.4B as of March 28, 2026. That supports supplier/manufacturing obligation discussion, but the dedicated commitments/capex section was not extracted for either the 10-K or 10-Q, so capex schedule detail remains an evidence gap. (Source: 10-Q liquidity and capital resources; evidence gap: 10-K/10-Q commitments / capex / contractual obligations unavailable)

## Balance sheet and liquidity

Current ratio is 1.07 and debt/equity is 79.55. The 10-Q liquidity section says Apple believes cash, marketable securities, operating cash generation, and access to debt markets will be sufficient for cash requirements and the capital return program over the next 12 months and beyond. The 10-Q balance sheet section is available for statement-level support. (Source: structured fundamentals packet; 10-Q liquidity and capital resources; 10-Q balance sheet)

## Management guidance / outlook

The 8-K cover page confirms the press release was furnished as Exhibit 99.1, and Exhibit 99.1 includes management commentary from the CEO and CFO. The CEO attributed the record March quarter to total revenue, iPhone demand, services, and new products; the CFO cited operating cash flow, EPS, and installed-base strength. The extracted Exhibit 99.1 excerpt does not provide a formal numerical guidance table, so formal guidance remains an evidence gap. (Source: 8-K cover page; 8-K Exhibit 99.1; evidence gap: formal guidance table unavailable)

## Material risk factors

The extracted 10-K and 10-Q risk-factor sections are available and should be used for formal risk language. Evidence-supported risks remain premium valuation, memory/input-cost pressure, app-store regulatory pressure in Brazil, AI roadmap credibility, and supplier approval risk around blacklisted Chinese memory. (Source: 10-K risk factors; 10-Q risk factors)

## One-off or accounting items

No one-off or accounting item is identified in the extracted sections. Exhibit 99.1 reports dividend and buyback actions, including a 0.27 quarterly dividend and an additional 100B repurchase authorization, but these are capital-return decisions rather than one-off accounting adjustments. (Source: 8-K Exhibit 99.1)

## What changed since prior report, if evidence is available

The key change in this run is section-level extraction. The Financial Report Analyst now has named 10-K/10-Q records with available/unavailable status for business, risk, segment/product revenue, liquidity, income statement, balance sheet, cash flow, and capex/commitments sections, plus the actual Exhibit 99.1 earnings release. (Source: roles/financial_report.md; 8-K Exhibit 99.1)

## Evidence gaps

Investor presentation evidence is unavailable. 10-K/10-Q MD&A and dedicated commitments/capex sections were not extracted, so capex schedule detail and management discussion should not be overstated. Exhibit 99.1 was extracted, but a formal numerical guidance table was not identified in the excerpt. (Source: section-level financial document packet)

## Memory Update

No durable role-memory update was recorded for this historical generated output.
