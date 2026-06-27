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
6. For each packet item, run `tradingagents-workflow-orchestrator`, then the relevant analyst role skills, `tradingagents-dataflow-routing`, debate skills, trader, risk skills, portfolio manager, and run-persistence skill.
7. Do not run live LLM or market-data calls unless the current user explicitly approves them.

Output:
- JSON or markdown workflow packet listing ticker runs, inferred asset types, selected analysts, workflow skills, role skills, expected report keys, and safety boundaries.

Safety boundaries:
- This prepares a paper-study workflow; it is not broker automation.
- Do not run live LLM or market-data calls by default.
- Do not use as real trading advice.
- Do not connect to GCAF.