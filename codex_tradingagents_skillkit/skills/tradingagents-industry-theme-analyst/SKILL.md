---
name: tradingagents-industry-theme-analyst
description: Use when a TradingAgents-style report needs industry, sector, or theme context inferred from company evidence and current news.
---

# TradingAgents Industry Theme Analyst

Inputs:
- Ticker, company name, sector, industry, trade date, analyst evidence, and news packet.

Procedure:
1. infer relevant industry context from sector, industry, company, and evidence.
2. identify relevant themes and subthemes, such as AI infrastructure, supply chain, regulation, consumer demand, rates, commodities, or sector rotation.
3. Link current news to those themes; do not force unrelated news into a theme.
4. Classify each theme as tailwind, headwind, mixed, or irrelevant.
5. state confidence and explain what evidence would change the theme classification.

Output:
- `industry_theme_report`: concise theme table plus 1-2 paragraphs explaining the most material theme links.
- Required columns: Theme, Subtheme, Evidence link, Classification, Reason, Confidence.

Safety boundaries:
- Do not use broad sector commentary as ticker-specific proof without a clear link.
- Do not use as real trading advice.
- Do not connect to GCAF.
