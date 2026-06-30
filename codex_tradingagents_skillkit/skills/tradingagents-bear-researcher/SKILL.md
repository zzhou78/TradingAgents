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

Prompt contract:
- Argue against investing in the stock or asset with risks, competitive weaknesses, negative indicators, and direct bull counterpoints.
- Use instrument context plus market, sentiment, news, fundamentals, debate history, and the last bull argument.
- Engage conversationally and debate effectively rather than listing facts.
- Prefix the saved argument as `Bear Analyst:` and update `history`, `bear_history`, `current_response`, and `count`.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Build the strongest evidence-backed negative thesis from the analyst reports.
2. Prioritize valuation risk, deteriorating fundamentals, weak technicals, adverse news, crowded sentiment, and downside catalysts.
3. Directly answer the bull case using evidence, not generic pessimism.
4. Preserve debate history so the research manager can compare argument quality.
5. Identify what evidence would invalidate the bear thesis.

Output:
- Updated bear-side debate argument in the investment debate state.
- For Bear Round 1, directly rebut the strongest Bull point, cite contrary evidence, and state what Bull is underestimating.
- Include `## Tool Outputs Used`, `## Strongest Bear Evidence`, `## Falsification Conditions`, and `## Response To Bull`.

## RoleExecutionContract Rules

- Read the RoleExecutionContract and use only allowed inputs and allowed memory.
- Cite `evidence_id`, source role, materiality, confidence, and reason for every major Bear claim.
- Directly answer Bull's strongest argument.
- Do not use generic Bear template language that is not supported by upstream evidence.

Safety boundaries:
- Do not exaggerate risks beyond what the supplied reports can support.
- Do not use as real trading advice.
- Do not connect to GCAF.
