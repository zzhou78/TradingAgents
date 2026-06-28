---
name: tradingagents-financial-report-analyst
description: Use when a Codex TradingAgents run needs company filings, earnings releases, investor materials, management commentary, or financial-report context beyond structured ratios.
---

# TradingAgents Financial Report Analyst

Source files scanned:
- `tradingagents/agents/analysts/fundamentals_analyst.py`
- `tradingagents/agents/utils/fundamental_data_tools.py`

Inputs:
- latest annual report / 10-K if available.
- Latest annual report / 10-K if available.
- Latest quarterly report / 10-Q if available.
- Latest earnings release if available.
- Latest investor presentation if available.
- Structured fundamentals packet, balance sheet, income statement, and cash flow statement.

Procedure:
1. Build a source coverage table before drawing conclusions.
2. Separate structured financial statement data from management narrative / filing commentary.
3. If annual/quarterly filings or earnings releases are not available, state that clearly and lower confidence.
4. Summarize revenue and segment performance, margin and profitability trend, cash flow quality, capex and investment commitments, balance sheet and liquidity, guidance/outlook, risk factors, one-off/accounting items, changes since prior report, and evidence gaps.
5. Do not infer management commentary from ratios alone.

Output:
- `financial_report.md` with sections: Source coverage table; Revenue and segment performance; Margin and profitability trend; Cash flow quality; Capex and investment commitments; Balance sheet and liquidity; Management guidance / outlook; Material risk factors; One-off or accounting items; What changed since prior report, if evidence is available; Evidence gaps.

Safety boundaries:
- Do not fabricate filing content, guidance, segment data, or management commentary.
- Do not use as real trading advice.
- Do not connect to GCAF.
