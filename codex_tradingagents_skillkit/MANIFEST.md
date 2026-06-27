# Manifest

## Origin

Everything in this folder was created for the Codex TradingAgents study branch.
The upstream TradingAgents source remains in the normal project folders, mainly:

- `tradingagents/agents`
- `tradingagents/graph`
- `tradingagents/dataflows`

This is intentional. The skillkit is self-contained for our Codex-created
workflow layer, but it is not a vendored runtime distribution. If a run needs
real market, news, social, macro, or prediction-market data, it still depends on
the upstream Python modules in `tradingagents/dataflows/` and their configured
vendors. The `tradingagents-dataflow-routing` skill records how to call that
layer safely; it does not duplicate or replace the implementation.

## Skill Inventory

Role skills derived from `tradingagents/agents`:
- `tradingagents-market-analyst`
- `tradingagents-sentiment-analyst`
- `tradingagents-news-analyst`
- `tradingagents-fundamentals-analyst`
- `tradingagents-bull-researcher`
- `tradingagents-bear-researcher`
- `tradingagents-research-manager`
- `tradingagents-trader`
- `tradingagents-aggressive-risk-analyst`
- `tradingagents-conservative-risk-analyst`
- `tradingagents-neutral-risk-analyst`
- `tradingagents-portfolio-manager`

Workflow skills derived from `tradingagents/graph`:
- `tradingagents-workflow-orchestrator`
- `tradingagents-analyst-sequencing`
- `tradingagents-debate-routing`
- `tradingagents-run-persistence`

Data and runner skills:
- `tradingagents-dataflow-routing`
- `tradingagents-ticker-workflow-runner`

## Runtime Entry Points

Use the workflow packet generator when you only want to prepare the Codex skill sequence:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\skills\tradingagents-ticker-workflow-runner\scripts\prepare_skill_workflow.py --ticker AAPL,MSFT --trade-date 2026-06-27 --format json
```

Ticker input options:
- `--ticker AAPL`
- `--ticker AAPL,MSFT`
- `--tickers-file path\to\tickers.txt`

The output names the skills to run, inferred asset type, report keys, and safety boundaries.

Use the evidence collector when you want upstream TradingAgents dataflow tools to gather role-specific evidence for Codex-operated reports:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\collect_role_evidence.py --ticker AAPL,MSFT --trade-date 2026-06-27
```

The evidence collector writes outputs under `codex_tradingagents_skillkit/runs/`
by default:
- `evidence/<TICKER>/<DATE>/evidence.json`
- `evidence/<TICKER>/<DATE>/role_packets.md`
- `evidence/<TICKER>/<DATE>/roles/<role>.md`
- `evidence/<TICKER>/<DATE>/workflow_state.json`
- `evidence_summary.json`
- `tradingagents_results/`
- `tradingagents_cache/`
- `tradingagents_memory/trading_memory.md`
- `yfinance_cache/`

Example output scope for Apple and Microsoft:
- `AAPL` and `MSFT` are normalized as stock tickers.
- The packet lists `tradingagents-dataflow-routing` as the data-routing skill.
- The packet command does not run live LLM, market-data vendor, cache, checkpoint, or broker actions.
- The evidence command can call market-data vendors through upstream dataflow tools, but it does not call upstream `TradingAgentsGraph` or any LLM backend.

## API and Model Requirements

The Codex skills themselves do not require API keys. In the Codex-operated
workflow, Codex is the role reasoning engine, so no separate cloud LLM key or
local Ollama/OpenAI-compatible endpoint is required for analyst, researcher,
trader, risk, or portfolio-manager reasoning.

Data APIs are separate from LLM APIs. The default yfinance route is keyless but
uses network data; FRED and Alpha Vantage are optional keyed vendors if enabled.

## Codex-Operated Report Contract

1. Run `collect_role_evidence.py` for the nominated tickers and date.
2. Codex follows the workflow skills converted from `tradingagents/graph`.
3. Codex acts each role independently:
   - analyst roles read only their own `roles/<role>.md` evidence packet;
   - `bull_researcher_round_1` reads only completed analyst reports;
   - `bear_researcher_round_1` reads analyst reports and directly responds to bull round 1;
   - future rounds can extend the same alternating bull/bear pattern;
   - trader reads the research-manager decision;
   - `aggressive_risk_round_1` reads the trader proposal and completed upstream reports;
   - `conservative_risk_round_1` responds to aggressive risk round 1;
   - `neutral_risk_round_1` weighs aggressive and conservative risk round 1;
   - portfolio manager reads the risk debate and produces the final paper-study decision.
4. Codex writes TradingAgents-style markdown sections under the run output folder.
5. No broker integration, GCAF connection, or real trading instruction is allowed.

`workflow_state.json` is the automatic execution contract. It records
`requires_user_input: false`, the ordered stage list, each role's allowed inputs,
forbidden analyst packets, and TradingAgents-style output paths. Codex should
advance through that file without asking for additional user input unless data
collection fails in a way that prevents evidence-grounded reporting.

The default `complete_report.md` structure is:
- I. Analyst Team Reports.
- II. Research Team Debate.
- III. Trading Team Plan.
- IV. Risk Management Team Debate.
- V. Portfolio Manager Decision.
