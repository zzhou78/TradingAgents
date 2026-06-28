---
name: tradingagents-analyst-sequencing
description: Use when reproducing TradingAgents graph analyst selection, analyst order, tool-loop routing, report keys, message clearing, or analyst wall-time behavior from graph source.
---

# TradingAgents Analyst Sequencing

Source files scanned:
- `tradingagents/graph/analyst_execution.py`
- `tradingagents/graph/setup.py`
- `tradingagents/graph/conditional_logic.py`
- `tradingagents/graph/trading_graph.py`

Inputs:
- Selected analyst keys, normally some ordered subset of `market`, `social`, `news`, and `fundamentals`.
- Current graph state messages and any report fields already produced.

Procedure:
1. Preserve selected analyst order exactly; reject unknown keys instead of inventing a new analyst.
2. Use this mapping:
   - `market` -> `Market Analyst`, `tools_market`, `Msg Clear Market`, `market_report`.
   - `social` -> `Sentiment Analyst`, `tools_social`, `Msg Clear Sentiment`, `sentiment_report`.
   - `news` -> `News Analyst`, `tools_news`, `Msg Clear News`, `news_report`.
   - `fundamentals` -> `Fundamentals Analyst`, `tools_fundamentals`, `Msg Clear Fundamentals`, `fundamentals_report`.
3. For each analyst, if the latest message has tool calls, route to its tool node and then back to the same analyst.
4. When no tool calls remain, accept the report, clear transient messages, and move to the next selected analyst.
5. After the final selected analyst clears messages, route through the Codex extension analysts: Financial Report Analyst, then Industry / Theme Discovery Analyst, before `Bull Researcher`.
6. If tracking elapsed time, start the first incomplete selected analyst and mark an analyst complete when its report field appears.

Output:
- Ordered analyst report set ready for the bull/bear research debate.

Safety boundaries:
- Do not rename the persisted `social` key; it remains the wire key even though the node label is Sentiment Analyst.
- Do not fabricate missing reports for skipped analysts.
- Do not use as real trading advice.
- Do not connect to GCAF.
