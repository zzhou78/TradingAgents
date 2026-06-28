---
name: tradingagents-trader
description: Use when recreating or studying the TradingAgents trader role without reopening Python source, especially for translating the research manager plan into a structured paper trading proposal.
---

# TradingAgents Trader

Source files scanned:
- `tradingagents/agents/trader/trader.py`
- `tradingagents/agents/schemas.py`
- `tradingagents/agents/utils/agent_states.py`

Inputs:
- `ResearchPlan` from the research manager.
- Market report, sentiment report, news report, fundamentals report, and instrument context.

Prompt contract:
- Transaction direction is exactly Buy / Hold / Sell.
- Produce a structured `TraderProposal`.
- Rendered markdown must include `**Action**` and `**Reasoning**`.
- Optional entry price: include only when supported.
- Optional stop loss: include only when supported.
- Optional position sizing note: include only when supported.
- Preserve the trailing `FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**` compatibility line.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Treat the research manager decision as the primary input, then cross-check analyst evidence.
2. Choose a paper proposal action: `Buy`, `Hold`, or `Sell`.
3. Explain trade direction, conviction, major supporting evidence, and key invalidation risks.
4. Include entry zone, stop loss, target, time horizon, or sizing only when evidence supports them.
5. Make clear that the output is a proposal for downstream risk debate, not an execution command.
6. Safety boundaries must not change the Buy / Hold / Sell action.
7. Do not cite paper-study status as a reason to avoid Buy or Sell.
8. The action rationale must come from market evidence, research manager input, and risk evidence.

Output:
- `TraderProposal`: action, reasoning, optional entry/exit levels, sizing notes, and risk notes.
- Include a consistency check before the final proposal. If action is Sell, identify whether price broke below longer-term support or name the separate materially negative setup. If long-term support still holds and no material negative setup is documented, prefer Hold over Sell.

Safety boundaries:
- Do not submit orders or imply broker execution.
- Do not use as real trading advice.
- Do not connect to GCAF.
- Keep safety disclaimers outside `**Reasoning**`; they may appear only as separate implementation or safety notes.
