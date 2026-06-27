# Codex TradingAgents Skillkit

This folder is the self-contained set of artifacts created in this study branch.
It separates our Codex workflow layer from the upstream TradingAgents source.

Contents:
- `skills/`: Codex skills generated from `tradingagents/agents`, `tradingagents/graph`, and `tradingagents/dataflows`.
- `skills/tradingagents-ticker-workflow-runner/scripts/prepare_skill_workflow.py`: offline runner that turns ticker input into a workflow packet.
- `tests/`: regression tests for the skills and runner.
- `docs/`: study notes produced during this branch.
- `MANIFEST.md`: inventory of what is ours and how it maps to upstream source.

Quick checks:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_codex_self_contained_skillkit.py -q
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\skills\tradingagents-ticker-workflow-runner\scripts\prepare_skill_workflow.py --ticker AAPL,BTC-USD --trade-date 2026-06-27 --format markdown
```

Safety:
- This is a paper-study workflow.
- It does not submit broker orders.
- It does not connect to GCAF.
- The runner prepares workflow packets only; it does not call live LLMs or market-data vendors.
