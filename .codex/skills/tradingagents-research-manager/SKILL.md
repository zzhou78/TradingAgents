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
- Analyst reports and instrument context when available, including Fundamentals Analyst, Financial Report Analyst, and Industry / Theme Discovery Analyst.

Prompt contract:
- The rating scale is exactly Buy / Overweight / Hold / Underweight / Sell.
- Reserve Hold for genuinely balanced evidence; otherwise commit to the stronger side.
- Produce a structured `ResearchPlan`.
- Rendered markdown must include `**Recommendation**`, `**Rationale**`, and `**Strategic Actions**`.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Compare the bull and bear arguments for evidence quality, recency, specificity, and materiality.
2. Decide which side is better supported, or whether the evidence is mixed.
3. Assign one of the role's ratings: `Buy`, `Overweight`, `Hold`, `Underweight`, or `Sell`.
4. Write strategic actions that explain what a downstream trader should do with the conclusion.
5. State whether the rating is primarily driven by technical, valuation, fundamental, financial report / management commentary, news, industry/theme, or mixed evidence.
6. Preserve unresolved uncertainties rather than forcing false precision.

Output:
- `ResearchPlan`: rating, rationale, key evidence, risks, and strategic actions for the trader.
- Include `## Tool Outputs Used` listing the role reports, evidence packets, validators, or source files used.
- Include `## Structured Evidence Matrix` comparing Bull, Bear, market, sentiment, news, fundamentals, financial-report, and industry/theme evidence with weight, confidence, and evidence gap.
- Include strongest Bull evidence, strongest Bear evidence, which side has better evidence, and why the final rating was selected.
- Show the scoring rule and score components when a numeric evidence score is used. Explicitly justify why Sell wins over Hold or Underweight, or why Hold/Underweight is selected instead of Sell when long-term support still holds.
- Identify the primary driver of rating.
- Explain the impact of Fundamentals Analyst, Financial Report Analyst, and Industry / Theme Discovery Analyst evidence, or state that the evidence is unavailable or immaterial.
- Explain rating/action tension when relevant.
- Explain why Sell beats Underweight/Hold, or why Underweight/Hold beats Sell.

Safety boundaries:
- Do not turn the research rating into a real portfolio instruction.
- Do not use as real trading advice.
- Do not connect to GCAF.
