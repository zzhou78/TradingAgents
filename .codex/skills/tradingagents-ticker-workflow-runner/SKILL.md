---
name: tradingagents-ticker-workflow-runner
description: Use when a user provides one ticker, many tickers, or a ticker file and wants Codex to prepare or run a TradingAgents-style skill workflow without calling live LLMs or data vendors by default.
---

# TradingAgents Ticker Workflow Runner

Source files scanned:
- `tradingagents/graph/trading_graph.py`
- `tradingagents/graph/setup.py`
- `tradingagents/graph/propagation.py`
- `tradingagents/dataflows/interface.py`
- `tradingagents/dataflows/symbol_utils.py`
- `tradingagents/dataflows/utils.py`
- `.codex/skills/tradingagents-workflow-orchestrator/SKILL.md`
- `.codex/skills/tradingagents-dataflow-routing/SKILL.md`

Inputs:
- User-supplied tickers through `--ticker` or `--tickers-file`.
- Required `--trade-date` in `YYYY-MM-DD`.
- Optional `--asset-type`, `--selected-analysts`, and output `--format`.

Procedure:
1. Run `prepare_skill_workflow.py` to normalize the user request into a deterministic workflow packet.
2. Use `--ticker` for one ticker or comma-separated tickers.
3. Use `--tickers-file` for newline or comma-separated ticker lists; blank lines and `#` comments are ignored.
4. Use `--trade-date` to anchor all date ranges.
5. Use `--selected-analysts` to choose ordered selected analysts; defaults follow the graph: market, social, news, fundamentals.
6. For each packet item, run `tradingagents-workflow-orchestrator`, then the relevant analyst role skills, Financial Report Analyst, Industry / Theme Discovery Analyst, `tradingagents-dataflow-routing`, debate skills, trader, risk skills, portfolio manager, run-persistence skill, and quality reviewer.
7. Do not run live LLM or market-data calls unless the current user explicitly approves them.
8. After quality review, run the Codex workflow controller. If it reports `quality_remediation`, do not stop at `quality_remediation_plan.json`; read `next_remediation_task.md`, implement the fix with tests, rerun evidence/report generation, and continue until the quality gate passes or a true external blocker is documented.
9. For ASX multi-ticker review runs, use a clear ASX-specific output folder such as `codex_tradingagents_skillkit/runs/asx_YYYY-MM-DD_closed_loop/`; do not store ASX reports under an AAPL/MSFT folder.
10. ASX run metadata must include `market: ASX`, `ticker_list`, `trade_date`, `evidence_as_of_date`, `run_executed_at`, `authoritative_result_folder`, and `workflow_status`.

Output:
- JSON or markdown workflow packet listing ticker runs, inferred asset types, selected analysts, workflow skills, role skills, expected report keys, and safety boundaries.
- For failed review-grade runs, include the remediation status, `quality_remediation_plan.json`, and `next_remediation_task.md` instead of claiming completion.

## Closed Self-Improvement Loop

The ticker workflow runner owns the outer loop across nominated tickers. A
quality failure means the next runnable item is the first pending task in
`next_remediation_task.md`. Codex must implement that task, rerun the affected
ticker workflow, and repeat until the quality gate passes or a true external
blocker is documented.

## Standing Auto-Remediation Approval

Option 1 is approved for all future TradingAgents workflows. After any nominated
ticker reaches `quality_remediation`, Codex must continue automatically; do not ask the user to proceed before implementing `next_remediation_task.md`,
rerunning the affected ticker workflow, and checking the controller again.

Safety boundaries:
- This prepares a paper-study workflow; it is not broker automation.
- Do not run live LLM or market-data calls by default.
- Do not use as real trading advice.
- Do not connect to GCAF.
