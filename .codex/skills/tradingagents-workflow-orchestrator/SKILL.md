---
name: tradingagents-workflow-orchestrator
description: Use when mimicking the TradingAgents graph workflow from graph source, coordinating selected analyst skills, research debate, trader proposal, risk debate, portfolio decision, reports, and rating extraction.
---

# TradingAgents Workflow Orchestrator

Source files scanned:
- `tradingagents/graph/trading_graph.py`
- `tradingagents/graph/setup.py`
- `tradingagents/graph/analyst_execution.py`
- `tradingagents/graph/conditional_logic.py`
- `tradingagents/graph/propagation.py`
- `tradingagents/graph/checkpointer.py`
- `tradingagents/graph/reflection.py`
- `tradingagents/graph/signal_processing.py`

Inputs:
- Ticker or company, trade date, asset type, selected analysts, and any pre-collected evidence.
- Existing role-skill outputs: analyst reports, debate notes, trader proposal, risk debate, and portfolio manager decision.
- Optional config concepts: `max_debate_rounds`, `max_risk_discuss_rounds`, checkpoint setting, results directory, and data cache directory.
- Optional ticker workflow packet from `tradingagents-ticker-workflow-runner`.

Required role skills:
- `tradingagents-market-analyst`
- `tradingagents-sentiment-analyst`
- `tradingagents-news-analyst`
- `tradingagents-fundamentals-analyst`
- `tradingagents-financial-report-analyst`
- `tradingagents-industry-theme-discovery-analyst`
- `tradingagents-bull-researcher`
- `tradingagents-bear-researcher`
- `tradingagents-research-manager`
- `tradingagents-trader`
- `tradingagents-aggressive-risk-analyst`
- `tradingagents-conservative-risk-analyst`
- `tradingagents-neutral-risk-analyst`
- `tradingagents-portfolio-manager`

Procedure:
1. Initialize the run state with ticker/company, trade date, asset type, instrument context, past context, empty analyst reports, empty investment debate, and empty risk debate.
2. Run selected analysts in configured order; the default keys are `market, social, news, fundamentals`, and the social key maps to Sentiment Analyst.
3. Extend the analyst layer with Financial Report Analyst and Industry / Theme Discovery Analyst before the bull/bear research debate.
3. For data access and tool-call planning, use `tradingagents-dataflow-routing`; do not bypass its vendor routing, no-data, or path-safety rules.
4. For analyst details, use `tradingagents-analyst-sequencing`; each analyst may call tools until no tool calls remain, then its report is accepted and messages are cleared before the next analyst.
5. Run the core graph order: analysts -> financial report analyst -> industry/theme discovery analyst -> bull/bear research debate -> research manager -> trader. This preserves the original TradingAgents debate chain: analysts -> bull/bear research debate -> research manager -> trader.
6. Run risk review in graph order: trader -> aggressive/conservative/neutral risk debate -> portfolio manager.
7. For debate turn routing and stop conditions, use `tradingagents-debate-routing`.
8. For checkpoints, final-state logging, deferred reflection, report writing, and deterministic rating extraction, use `tradingagents-run-persistence`.
9. Extract the final signal as one of `Buy / Overweight / Hold / Underweight / Sell` from the portfolio manager markdown, not from a second LLM call.
10. Do not compare the ticker to another ticker unless the run context explicitly says this is a comparative multi-ticker report. In a single-ticker report, do not mention another ticker as a comparison point unless it appears in the evidence packet and is material to the thesis.
11. If the controller reports `quality_remediation` as the next stage, the workflow is not complete. Read `quality_remediation_plan.json` and `next_remediation_task.md`, implement the remediation task with tests, rerun evidence collection/report generation, and repeat until the quality gate passes or a true external blocker is documented.

Output:
- Final study artifact containing analyst reports, investment debate, research plan, trader proposal, risk debate, portfolio manager decision, and parsed five-tier rating.
- If quality remediation is pending, output the remediation status and next task instead of claiming a completed review-grade workflow.

## Closed Self-Improvement Loop

Quality failure must feed back into implementation work. The orchestrator must
treat `next_remediation_task.md` as the next runnable stage after a failed
quality gate. Codex should keep improving collectors, extractors, validators,
prompts, or report integration and rerunning the workflow until the quality gate
passes or a true external blocker is documented.

## Standing Auto-Remediation Approval

Option 1 is approved for all future TradingAgents workflows. If the controller
reports `quality_remediation`, Codex must execute the next remediation task; do not ask the user to proceed. Continue through fix, tests, rerun, and
controller validation until the quality gate passes or a true external blocker
is documented.

Safety boundaries:
- Treat the result as a paper-study workflow only, even when the role names sound operational.
- Do not run live LLM or market-data calls unless explicitly approved for the current task.
- Do not submit orders, configure brokers, or create real buy/sell instructions.
- Do not use as real trading advice.
- Do not connect to GCAF.
