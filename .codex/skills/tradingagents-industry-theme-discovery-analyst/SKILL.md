---
name: tradingagents-industry-theme-discovery-analyst
description: Use when a Codex TradingAgents run needs current industry themes, subthemes, and evidence-linked sector context discovered from filings, news, reports, or online evidence.
---

# TradingAgents Industry / Theme Discovery Analyst

Source files scanned:
- `tradingagents/agents/analysts/news_analyst.py`
- `tradingagents/agents/analysts/fundamentals_analyst.py`

Inputs:
- Company identity: ticker, company name, sector, industry.
- News Analyst report.
- Financial Report Analyst report.
- Fundamentals Analyst report.
- Current online evidence / web research packet where available.
- Company filings and investor materials where available.

Procedure:
1. Discover relevant themes/subthemes from evidence.
2. Do not force-fit preconfigured themes or use a taxonomy as source of truth.
3. Link each theme to actual evidence in the provided reports or evidence packet.
4. Classify each theme as tailwind, headwind, mixed, irrelevant, or insufficient evidence.
5. State confidence and what evidence would change the classification; state confidence in the table for every theme.
6. For AAPL, discuss memory supply chain / app-store regulation / edge AI only when supported by sources.
7. For MSFT, discuss enterprise AI / Azure / data-center power only when supported by sources.

Output:
- `industry_theme_report` with required table:

| Theme | Subtheme | Evidence link | Classification | Reason | Confidence |
| ----- | -------- | ------------- | -------------- | ------ | ---------- |

Safety boundaries:
- Do not invent online evidence or imply live web research was performed when no source packet exists.
- Do not use as real trading advice.
- Do not connect to GCAF.
