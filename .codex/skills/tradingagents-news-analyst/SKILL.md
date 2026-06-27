---
name: tradingagents-news-analyst
description: Use when recreating or studying the TradingAgents news analyst role without reopening Python source, especially for company news, macro indicators, global news, and prediction-market context.
---

# TradingAgents News Analyst

Source files scanned:
- `tradingagents/agents/analysts/news_analyst.py`

Inputs:
- Ticker or instrument, company name if available, trade date, and asset type.
- Tool outputs from `get_news`, `get_global_news`, `get_macro_indicators`, and `get_prediction_markets`.

Procedure:
1. Pull company or asset-specific news before broad macro context.
2. Add global news, macro indicators, and prediction-market signals only where relevant to the instrument.
3. Distinguish dated facts from interpretation and preserve event timing.
4. Flag stale, sparse, or unavailable feeds because news conclusions drift quickly.
5. End with a compact markdown table of major events, likely impact, and evidence source.

Output:
- `news_report`: a current-event and macro context report for researchers, trader, and risk reviewers.

Safety boundaries:
- Do not present old headlines as current catalysts.
- Do not use as real trading advice.
- Do not connect to GCAF.
