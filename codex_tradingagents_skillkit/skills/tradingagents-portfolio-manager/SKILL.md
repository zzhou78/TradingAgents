---
name: tradingagents-portfolio-manager
description: Use when recreating or studying the TradingAgents portfolio manager role without reopening Python source, especially for synthesizing trader proposals and risk debate into a final paper decision.
---

# TradingAgents Portfolio Manager

Source files scanned:
- `tradingagents/agents/managers/portfolio_manager.py`
- `tradingagents/agents/schemas.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- Trader proposal, research manager plan, risk debate history, analyst reports, and optional memory context.

Prompt contract:
- Produce a structured `PortfolioDecision`.
- Rating is exactly Buy / Overweight / Hold / Underweight / Sell.
- Rendered markdown must include `**Rating**`, `**Executive Summary**`, and `**Investment Thesis**`.
- Optional fields are price target and time horizon. This does not override the Trader rule: if final action is Buy or Sell, preserve or restate the Trader's labelled paper-study price framework.
- Be decisive and ground conclusions in specific evidence from the analysts and risk debate.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Review the trader proposal against the aggressive, conservative, and neutral risk arguments.
2. Decide whether risk-adjusted evidence supports accepting, modifying, or rejecting the proposal.
3. Produce a structured `PortfolioDecision` with rating, executive summary, thesis, risk assessment, and optional price target or horizon. For Buy/Sell decisions, include the Trader's paper-study reference price or entry zone and the key confirmation/invalidation levels.
4. Include implementation notes only as paper-study guidance, never as broker instructions.
5. Write the final decision in clear markdown for learning and auditability.

Output:
- `PortfolioDecision` and final decision text for the TradingAgents study flow.
- Synthesize the risk debate and do not merely repeat the Trader.
- State Risk debate impact.
- State financial-report impact if material, or say it was unavailable/immaterial.
- State industry/theme impact if material, or say it was unavailable/immaterial.
- Distinguish technical/momentum Sell from fundamental Sell.
- Explain what would invalidate or improve the final decision.

Safety boundaries:
- Do not create real buy, sell, rebalance, or broker instructions.
- Do not use as real trading advice.
- Do not connect to GCAF.
