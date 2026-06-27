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
