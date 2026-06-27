# Manifest

## Origin

Everything in this folder was created for the Codex TradingAgents study branch.
The upstream TradingAgents source remains in the normal project folders, mainly:

- `tradingagents/agents`
- `tradingagents/graph`
- `tradingagents/dataflows`

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
