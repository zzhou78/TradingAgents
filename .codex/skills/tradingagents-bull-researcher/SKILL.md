---
name: tradingagents-bull-researcher
description: Use when recreating or studying the TradingAgents bull researcher role without reopening Python source, especially for constructing the positive thesis in the research debate.
---

# TradingAgents Bull Researcher

Source files scanned:
- `tradingagents/agents/researchers/bull_researcher.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- Analyst reports: market, sentiment, news, and fundamentals.
- Current investment debate state, including prior bull and bear arguments.

Prompt contract:
- Advocate for investing in the stock or asset with growth potential, competitive advantages, positive indicators, and direct bear counterpoints.
- Use instrument context plus market, sentiment, news, fundamentals, debate history, and the last bear argument.
- Engage conversationally and debate effectively rather than listing data.
- Prefix the saved argument as `Bull Analyst:` and update `history`, `bull_history`, `current_response`, and `count`.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Build the strongest evidence-backed positive thesis from the analyst reports.
2. Prioritize catalysts, improving fundamentals, constructive technicals, favorable sentiment, and upside asymmetry.
3. Directly answer the bear case using evidence, not generic optimism.
4. Preserve debate history so the research manager can see how the argument evolved.
5. Keep the argument concise enough for comparison against the bear researcher.

Output:
- Updated bull-side debate argument in the investment debate state.

Safety boundaries:
- Do not ignore material risks that are explicit in the analyst reports.
- Do not use as real trading advice.
- Do not connect to GCAF.
