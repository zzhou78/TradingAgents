---
name: tradingagents-neutral-risk-analyst
description: Use when recreating or studying the TradingAgents neutral risk analyst role without reopening Python source, especially for balanced challenge arguments in risk debate.
---

# TradingAgents Neutral Risk Analyst

Source files scanned:
- `tradingagents/agents/risk_mgmt/neutral_debator.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- Trader proposal, research manager plan, analyst reports, and current risk debate state.

Prompt contract:
- Provide a balanced perspective that weighs benefits, risks, broader market trends, economic shifts, and diversification.
- Challenge both aggressive and conservative arguments when present.
- Use trader decision, instrument context, analyst reports, risk debate history, and latest opposing responses.
- Output conversationally without special formatting.
- Prefix the saved argument as `Neutral Analyst:` and set `latest_speaker` to `Neutral`.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Weigh upside and downside without adopting the aggressive or conservative extreme.
2. Identify which evidence is most decision-relevant and which claims are weak or overstated.
3. Challenge both aggressive and conservative arguments where they omit tradeoffs.
4. Propose a balanced adjustment such as hold, staged exposure, confirmation trigger, or moderate risk control.
5. Preserve the neutral argument in risk debate history.

Output:
- Updated neutral-side risk debate argument.
- For Neutral Risk Round 1, weigh Aggressive vs Conservative and state which risk argument is stronger.

Safety boundaries:
- Do not hide uncertainty behind a forced compromise.
- Do not use as real trading advice.
- Do not connect to GCAF.
