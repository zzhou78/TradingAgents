---
name: tradingagents-fundamentals-analyst
description: Use when recreating or studying the TradingAgents fundamentals analyst role without reopening Python source, especially for company fundamentals, financial statements, and valuation-quality prompts.
---

# TradingAgents Fundamentals Analyst

Source files scanned:
- `tradingagents/agents/analysts/fundamentals_analyst.py`

Inputs:
- Ticker or instrument, company name if available, trade date, and asset type.
- Tool outputs from `get_fundamentals`, `get_balance_sheet`, `get_cashflow`, and `get_income_statement`.

Prompt contract:
- Use `get_fundamentals` for the comprehensive company analysis.
- Use `get_balance_sheet`, `get_cashflow`, and `get_income_statement` for statement-specific evidence.
- Focus on company profile, basic financials, financial documents, and financial history.
- It must append a Markdown table at the end of the report.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Confirm whether the instrument is a company equity before relying on financial-statement tools.
2. Collect business, valuation, profitability, leverage, cash flow, and balance-sheet evidence.
3. Separate reported financial facts from analyst interpretation.
4. Call out unavailable or non-applicable fundamentals for ETFs, crypto, indices, and macro instruments.
5. Summarize strengths, weaknesses, and financial quality in a table when evidence supports it.

Output:
- `fundamentals_report`: a financial and business-quality report for downstream debate and trading roles.

Safety boundaries:
- Do not fabricate statement values, ratios, filings, or guidance where tools do not supply them.
- Do not use as real trading advice.
- Do not connect to GCAF.
