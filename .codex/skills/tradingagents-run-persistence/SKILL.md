---
name: tradingagents-run-persistence
description: Use when reproducing TradingAgents graph run state, checkpoint resume semantics, final JSON/report persistence, deferred reflection, benchmark outcome lookup, or final signal parsing.
---

# TradingAgents Run Persistence

Source files scanned:
- `tradingagents/graph/propagation.py`
- `tradingagents/graph/trading_graph.py`
- `tradingagents/graph/checkpointer.py`
- `tradingagents/graph/reflection.py`
- `tradingagents/graph/signal_processing.py`

Inputs:
- Ticker, trade date, asset type, instrument context, prior memory context, graph final state, and optional config paths.
- Portfolio manager final decision markdown.

Procedure:
1. Initial state contains the human ticker/company message, `company_of_interest`, `asset_type`, `instrument_context`, `trade_date`, `past_context`, empty investment and risk debate states, and empty analyst reports.
2. Use recursion-limit config for graph execution; include callbacks only when provided.
3. If checkpointing is enabled, compile with a per-ticker SQLite saver under `data_cache_dir/checkpoints` and use a deterministic ticker/date thread ID.
4. Resume only the same ticker/date thread; a different date starts fresh.
5. On successful completion, clear the ticker/date checkpoint so stale state is not reused.
6. Log final state as JSON under `results_dir/<safe ticker>/TradingAgentsStrategy_logs/full_states_log_<date>.json`.
7. Store the final decision for deferred reflection; later same-ticker runs may resolve raw and benchmark-relative return, then store a 2-4 sentence reflection.
8. Parse the final signal from the portfolio manager markdown with the five-tier rating heuristic; do not make an extra LLM call for signal extraction.

Output:
- Initial-state contract, checkpoint behavior, final state log, optional report tree, deferred reflection update, and parsed rating.

Complete report assembly:
- `complete_report.md` should mimic original TradingAgents while making debate turns visible.
- Python scripts may prepare Codex task prompts, but Codex role execution writes the analytical reports.
- `write_codex_reports.py` is a compatibility wrapper for task preparation, not a reasoning writer.
- Use the exact heading `# Trading Analysis Report: <TICKER>`.
- I. Analyst Team Reports: `### Market Analyst`, `### Sentiment Analyst`, `### News Analyst`, `### Fundamentals Analyst`, `### Financial Report Analyst`, and `### Industry / Theme Discovery Analyst`.
- II. Research Team Debate: `### Bull Researcher Round 1 - Opening Case`, `### Bear Researcher Round 1 - Rebuttal to Bull`, and `### Research Manager Decision - Evidence Weighing`.
- III. Trading Team Plan: `### Trader Proposal` and the `FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**` line.
- For any Buy or Sell final proposal, the Trader Proposal must include `**Paper-study price framework**` with a reference price or entry zone, invalidation level, and first confirmation or target level. Hold may instead list watch levels.
- IV. Risk Management Team Debate: `### Aggressive Risk Analyst Round 1 - Opportunity Case`, `### Conservative Risk Analyst Round 1 - Response to Aggressive`, and `### Neutral Risk Analyst Round 1 - Weighing`.
- V. Portfolio Manager Decision: `### Portfolio Manager` with Rating, Executive Summary, Investment Thesis, Risk Assessment or equivalent risk discussion, and Paper-study implementation notes.
- VI. Paper-Study Disclaimer: include a visible paper-study disclaimer section.

## Sentiment Report Output Rule

The final report must summarize social evidence. It must not include the full raw StockTwits or Reddit feed.
The hard contract validator must pass before the report is accepted.
The quality-reviewer skill must review analytical quality separately from the hard validator.
The report must identify the primary driver of rating.
The report must distinguish research rating from trader action when they differ.

Required sentiment table:
- Source
- Items reviewed
- Usable ticker-relevant items
- Bullish / bearish / neutral split
- Dominant themes
- Confidence
- Limitations

Safety boundaries:
- Do not write outside configured cache/results directories; use safe ticker path components.
- Do not treat logged decisions or reflections as real investment advice.
- Do not use as real trading advice.
- Do not connect to GCAF.
