---
name: tradingagents-bear-researcher
description: Use when recreating or studying the TradingAgents bear researcher role without reopening Python source, especially for constructing the risk and downside thesis in the research debate.
---

# TradingAgents Bear Researcher

Source files scanned:
- `tradingagents/agents/researchers/bear_researcher.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- Analyst reports: market, sentiment, news, and fundamentals.
- Current investment debate state, including prior bear and bull arguments.

Procedure:
1. Build the strongest evidence-backed negative thesis from the analyst reports.
2. Prioritize valuation risk, deteriorating fundamentals, weak technicals, adverse news, crowded sentiment, and downside catalysts.
3. Directly answer the bull case using evidence, not generic pessimism.
4. Preserve debate history so the research manager can compare argument quality.
5. Identify what evidence would invalidate the bear thesis.

Output:
- Updated bear-side debate argument in the investment debate state.

Safety boundaries:
- Do not exaggerate risks beyond what the supplied reports can support.
- Do not use as real trading advice.
- Do not connect to GCAF.
