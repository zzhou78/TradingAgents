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

Prompt contract:
- Use `get_news(query, start_date, end_date)` for company, asset-specific, or targeted news.
- Use `get_global_news(curr_date, look_back_days, limit)` for broader macroeconomic news.
- Use `get_macro_indicators(indicator, curr_date, look_back_days)` for FRED-grounded macro commentary.
- Use `get_prediction_markets(topic, limit)` for market-implied probabilities of forward-looking events.
- It must append a Markdown table at the end of the report.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Pull company or asset-specific news before broad macro context.
2. Add global news, macro indicators, and prediction-market signals only where relevant to the instrument.
3. Distinguish dated facts from interpretation and preserve event timing.
4. Flag stale, sparse, or unavailable feeds because news conclusions drift quickly.
5. End with a compact markdown table of major events, likely impact, and evidence source.

## LLM News Classification

Codex must classify each news item using reasoning, not keywords. For each item, decide:
- Is it direct company news, indirect industry/theme context, or irrelevant?
- What event type is it?
- What is the likely effect?
- Why?
- What could make the effect ambiguous?
- Is confidence high, medium, or low?

Required table:

| Event | Relevance | Event type | Likely effect | Reason | Confidence |
|---|---|---|---|---|---|
| AAPL seeks approval to buy CXMT chips | Direct | supply-chain / regulation | mixed | Could reduce memory cost pressure, but introduces geopolitical/supplier risk | Medium |

Output:
- `news_report`: a current-event and macro context report for researchers, trader, and risk reviewers.
- Filter relevance explicitly. Separate direct ticker/company news, indirect sector or market context, and excluded low-relevance items. Do not include unrelated headlines in the decision table unless the report explains why they materially affect the ticker.
- Classify each retained direct or indirect news item with likely effect: positive, negative, or mixed/unclear. Exclude irrelevant headlines from the decision table.

Safety boundaries:
- Do not present old headlines as current catalysts.
- Do not use as real trading advice.
- Do not connect to GCAF.
