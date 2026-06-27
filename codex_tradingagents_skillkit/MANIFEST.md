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

## Runtime Entry Point

Use the offline workflow packet generator:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\skills\tradingagents-ticker-workflow-runner\scripts\prepare_skill_workflow.py --ticker AAPL,MSFT --trade-date 2026-06-27 --format json
```

Ticker input options:
- `--ticker AAPL`
- `--ticker AAPL,MSFT`
- `--tickers-file path\to\tickers.txt`

The output names the skills to run, inferred asset type, report keys, and safety boundaries.

Example output scope for Apple and Microsoft:
- `AAPL` and `MSFT` are normalized as stock tickers.
- The packet lists `tradingagents-dataflow-routing` as the data-routing skill.
- No live LLM, market-data vendor, cache, checkpoint, or broker action is run by this command.
