---
name: tradingagents-financial-report-analyst
description: Use when a Codex TradingAgents run needs company filings, earnings releases, investor materials, management commentary, or financial-report context beyond structured ratios.
---

# TradingAgents Financial Report Analyst

Source files scanned:
- `tradingagents/agents/analysts/fundamentals_analyst.py`
- `tradingagents/agents/utils/fundamental_data_tools.py`

Inputs:
- `roles/financial_report.md`, which is the required source packet for filings and document coverage.
- latest annual report / 10-K if available.
- Latest annual report / 10-K if available.
- Latest quarterly report / 10-Q if available.
- Latest earnings release if available.
- Latest investor presentation if available.
- Structured fundamentals packet, balance sheet, income statement, and cash flow statement.

Procedure:
1. Build a source coverage table before drawing conclusions.
2. Check the trade-date discipline in the source packet. Do not use filings, releases, or social/news evidence dated after the trade date.
3. Separate structured financial statement data from management narrative / filing commentary.
4. Use filing excerpts only as excerpts. If you need a claim that is not in the packet, mark it as an evidence gap instead of filling it from memory.
5. If annual/quarterly filings, earnings releases, or investor presentations are not available, state that clearly and lower confidence.
   If annual/quarterly filings or earnings releases are not available, state that clearly and lower confidence.
6. For each substantive financial claim, cite which source section supports each claim: structured fundamentals packet, 10-K business / risk factors, 10-Q MD&A, 8-K Exhibit 99.1, 8-K cover page, or investor presentation if available.
7. Treat the 8-K cover page as source-routing evidence only unless the cover text itself contains the fact. Prefer 8-K Exhibit 99.1 for earnings-release claims when available.
8. Summarize revenue and segment performance, margin and profitability trend, cash flow quality, capex and investment commitments, balance sheet and liquidity, guidance/outlook, risk factors, one-off/accounting items, changes since prior report, and evidence gaps.
9. Include a claim-source table with columns: Claim, Source document, Section / exhibit, Filing date, Confidence, Evidence gap if section/exhibit is missing.
10. Mark capex, formal guidance, segment/product detail, income statement, balance sheet, and cash flow claims as evidence gaps when the relevant section or Exhibit 99.1 is unavailable.
11. Do not infer management commentary from ratios alone.

Output:
- `financial_report.md` with sections: Source coverage table; Claim-source table; Revenue and segment performance; Margin and profitability trend; Cash flow quality; Capex and investment commitments; Balance sheet and liquidity; Management guidance / outlook; Material risk factors; One-off or accounting items; What changed since prior report, if evidence is available; Evidence gaps.
- Include a compact citation marker in each paragraph or table row, for example `(Source: 10-Q MD&A)` or `(Source: structured fundamentals packet)`.

Safety boundaries:
- Do not fabricate filing content, guidance, segment data, or management commentary.
- Do not use as real trading advice.
- Do not connect to GCAF.
