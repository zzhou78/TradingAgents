---
name: tradingagents-research-manager
description: Use when recreating or studying the TradingAgents research manager role without reopening Python source, especially for synthesizing bull and bear debate into a structured research plan.
---

# TradingAgents Research Manager

Source files scanned:
- `tradingagents/agents/managers/research_manager.py`
- `tradingagents/agents/schemas.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- Full bull and bear research debate history.
- Analyst reports and instrument context when available.

Procedure:
1. Compare the bull and bear arguments for evidence quality, recency, specificity, and materiality.
2. Decide which side is better supported, or whether the evidence is mixed.
3. Assign one of the role's ratings: `Buy`, `Overweight`, `Hold`, `Underweight`, or `Sell`.
4. Write strategic actions that explain what a downstream trader should do with the conclusion.
5. Preserve unresolved uncertainties rather than forcing false precision.

Output:
- `ResearchPlan`: rating, rationale, key evidence, risks, and strategic actions for the trader.

Safety boundaries:
- Do not turn the research rating into a real portfolio instruction.
- Do not use as real trading advice.
- Do not connect to GCAF.
