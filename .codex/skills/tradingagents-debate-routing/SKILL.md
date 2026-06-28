---
name: tradingagents-debate-routing
description: Use when reproducing TradingAgents graph debate flow, including bull/bear research turns, research-manager handoff, aggressive/conservative/neutral risk turns, and portfolio-manager handoff.
---

# TradingAgents Debate Routing

Source files scanned:
- `tradingagents/graph/setup.py`
- `tradingagents/graph/conditional_logic.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- Analyst reports and current `investment_debate_state`.
- Trader proposal and current `risk_debate_state`.
- Configured `max_debate_rounds` and `max_risk_discuss_rounds`.

Procedure:
1. Start investment debate after the last analyst with `Bull Researcher`.
2. Continue investment debate until `investment_debate_state["count"] >= 2 * max_debate_rounds`.
3. While investment debate continues, route `Bull...` current responses to `Bear Researcher`; otherwise route to `Bull Researcher`.
4. When investment debate stops, route to `Research Manager`, then directly to `Trader`.
5. Start risk debate after `Trader` with `Aggressive Analyst`.
6. Continue risk debate until `risk_debate_state["count"] >= 3 * max_risk_discuss_rounds`.
7. While risk debate continues, route after `Aggressive...` to `Conservative Analyst`, after `Conservative...` to `Neutral Analyst`, and otherwise to `Aggressive Analyst`.
8. When risk debate stops, route to `Portfolio Manager`, then end the graph.

## Codex-visible debate rendering

- The report must show the actual debate turns.
- Bear must directly respond to Bull.
- Research Manager must explicitly weigh Bull vs Bear.
- Conservative Risk must directly respond to Aggressive Risk.
- Neutral Risk must explicitly weigh Aggressive vs Conservative.
- Portfolio Manager must synthesize the risk debate.
- Keep the visible sequence aligned with analyst reports, bull/bear debate, research manager, trader, aggressive/conservative/neutral risk debate, and portfolio manager.
- Documentation alone is not sufficient. The generated report must preserve visible debate-stage headings. If the final report does not contain the required headings, the run is incomplete.

Output:
- Completed investment debate, research-manager plan, trader proposal, risk debate, and portfolio-manager-ready context.

Safety boundaries:
- Do not skip the trader stage between research manager and risk debate.
- Do not let debate loops run indefinitely; respect the configured counters.
- Do not use as real trading advice.
- Do not connect to GCAF.
