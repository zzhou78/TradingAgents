# Financial Report Analyst: MSFT

## Source coverage table

| Source | Status | Use in this report | Confidence impact |
|---|---|---|---|
| Structured fundamentals packet | Available | Revenue, income, free cash flow, margins, leverage, liquidity, valuation | Medium |
| Latest annual report / 10-K | Available: filed 2025-07-30 | Business overview, risk factors, segment references, liquidity, commitments/capex context | Raises confidence |
| Latest quarterly report / 10-Q | Available: filed 2026-04-29 | March 2026 financial statements, risk factors, segment references, liquidity, commitments/capex context | Raises confidence |
| Latest earnings 8-K cover page | Available: Item 2.02 filed 2026-04-29 | Confirms an earnings release was furnished as Exhibit 99.1 | Medium |
| 8-K Exhibit 99.1 | Not extracted from SEC index in this run | Not used for earnings-release claims | Lowers confidence for release-specific management quotes |
| Investor presentation | Not discovered from SEC submissions feed | Not used | Lowers confidence for presentation-specific claims |

## Revenue and segment performance

Structured evidence shows TTM revenue of 318.3B. The March 2026 10-Q reports three-month revenue of 82.886B versus 70.066B in the prior-year period, and nine-month revenue of 241.832B versus 205.283B. The report packet also extracts a 10-Q segment-information section, but the excerpt is not sufficient for a complete segment bridge by Azure, Office, Windows, LinkedIn, or gaming. (Source: structured fundamentals packet; 10-Q MD&A; 10-Q segment information)

## Margin and profitability trend

MSFT shows strong profitability: net income 125.2B, profit margin 39.34%, operating margin 46.33%, and ROE 0.34. The March 2026 10-Q excerpt reports quarterly gross margin of 56.058B and operating income of 38.398B, supporting the quality case. (Source: structured fundamentals packet; 10-Q MD&A)

## Cash flow quality

Free cash flow is 37.0B in the structured packet. The 10-K liquidity section says existing cash, short-term investments, operating cash flows, and capital-market access are expected to fund operating activities and cash commitments. The 10-Q liquidity section reports cash from operations increased 34.0B to 127.5B for the nine months ended March 31, 2026. (Source: structured fundamentals packet; 10-K liquidity and capital resources; 10-Q liquidity and capital resources)

## Capex and investment commitments

The 10-Q commitments/capex section reports cash used in investing increased 42.6B to 84.7B for the nine months ended March 31, 2026, primarily including a 32.7B increase in additions to property and equipment and a 9.1B increase in other investing primarily to facilitate component purchases. This directly supports the AI/data-center capex intensity concern discussed elsewhere in the report. (Source: 10-Q commitments / capex / contractual obligations)

## Balance sheet and liquidity

Current ratio is 1.28 and debt/equity is 30.27. The 10-Q liquidity section reports cash, cash equivalents, and short-term investments of 78.3B as of March 31, 2026, compared with 94.6B as of June 30, 2025. Liquidity remains substantial, but the decline in cash and short-term investments matters when paired with elevated property and equipment additions. (Source: structured fundamentals packet; 10-Q liquidity and capital resources)

## Management guidance / outlook

The 8-K cover page confirms Microsoft furnished an earnings press release as Exhibit 99.1 for the March 2026 quarter. However, Exhibit 99.1 itself was not extracted from the SEC filing index in this run, so this report does not quote management outlook or release-specific guidance. (Source: 8-K cover page)

## Material risk factors

The extracted 10-K and 10-Q risk-factor sections are available and should be the preferred source for formal risk language. Evidence-supported risk themes remain AI/cloud infrastructure capex intensity, data-center power availability, cloud regulation, OpenAI dependency, and weak current technical trend. Direct risk-factor quotations should be limited to the extracted filing sections. (Source: 10-K risk factors; 10-Q risk factors)

## One-off or accounting items

No one-off or accounting item is identified in the extracted filing sections. The Item 2.02 8-K cover page is source-routing evidence for an earnings release, not by itself a one-off accounting item. (Source: 8-K cover page; 10-Q MD&A)

## What changed since prior report, if evidence is available

The key change in this run is extraction depth. The Financial Report Analyst now has named 10-K/10-Q sections for business, risk factors, segment information, liquidity, and commitments/capex, rather than only full-filing excerpts. That raises confidence in financial-statement and capex/liquidity discussion, but it does not overturn the technical-led Sell conclusion. (Source: roles/financial_report.md; 10-K business; 10-Q liquidity and capital resources)

## Evidence gaps

Investor presentation evidence is still unavailable. Exhibit 99.1 was referenced by the 8-K cover page but not extracted from the SEC index in this run, so earnings-release quotes and management outlook remain an evidence gap. A full segment bridge still requires deeper table extraction. (Source: 8-K cover page; investor-presentation coverage row)
