# Codex TradingAgents Skillkit

This folder is the self-contained set of artifacts created in this study branch.
It separates our Codex workflow layer from the upstream TradingAgents source.

Contents:
- `skills/`: Codex skills generated from `tradingagents/agents`, `tradingagents/graph`, and `tradingagents/dataflows`.
- `skills/tradingagents-ticker-workflow-runner/scripts/prepare_skill_workflow.py`: offline runner that turns ticker input into a workflow packet.
- `scripts/collect_role_evidence.py`: upstream-data evidence collector for Codex-operated role reports.
- `scripts/prepare_codex_report_tasks.py`: prepares task prompts for Codex role execution after evidence collection.
- `scripts/write_codex_reports.py`: compatibility wrapper for `prepare_codex_report_tasks.py`; it no longer writes investment reasoning. `write_codex_reports.py is a compatibility wrapper`.
- `scripts/validate_complete_report.py`: hard contract validator for required headings, date discipline, social-dump limits, action matching, disclaimer, and primary driver.
- `tests/`: regression tests for the skills and runner.
- `docs/`: study notes produced during this branch.
- `MANIFEST.md`: inventory of what is ours and how it maps to upstream source.

Runtime boundary:
- This folder is our Codex workflow layer, not a vendored copy of the TradingAgents runtime.
- Real data retrieval and processing still uses upstream Python under `tradingagents/dataflows/`.
- The `tradingagents-dataflow-routing` skill documents how Codex should route data calls safely; it does not replace those Python modules.
- Keep upstream runtime code in `tradingagents/` so it stays clear which parts are ours.

API and model boundary:
- In the Codex-operated workflow, Codex acts each TradingAgents role using the converted skills. Do not call upstream `TradingAgentsGraph` for role reasoning.
- No extra cloud LLM key or local model endpoint is required for the role reasoning in this chat.
- Market and news data still come from upstream data vendors. The default yfinance path is keyless but still uses network data; FRED and Alpha Vantage are optional keyed vendors if enabled.

Apple and Microsoft workflow-packet example:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\skills\tradingagents-ticker-workflow-runner\scripts\prepare_skill_workflow.py --ticker AAPL,MSFT --trade-date 2026-06-27 --format markdown
```

Apple and Microsoft role-evidence example for Codex-operated reports:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\collect_role_evidence.py --ticker AAPL,MSFT --trade-date 2026-06-27
```

After collection, prepare Codex role task prompts:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\prepare_codex_report_tasks.py --output-dir codex_tradingagents_skillkit\runs\run_2026-06-27
```

`write_codex_reports.py` is a compatibility wrapper for this task-preparation step. Python prepares `reports/<TICKER>/<DATE>/tasks/*.md`; Codex fills the actual role reports and `complete_report.md`.

Validate a Codex-written complete report:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\validate_complete_report.py --report codex_tradingagents_skillkit\runs\run_2026-06-27\reports\AAPL\2026-06-27\complete_report.md
```

The task preparer reads each ticker's `workflow_state.json` and writes task prompts without asking for more user input. The default stage list includes visible one-round debate turns:
- `bull_researcher_round_1`
- `bear_researcher_round_1`
- `research_manager`
- `trader`
- `aggressive_risk_round_1`
- `conservative_risk_round_1`
- `neutral_risk_round_1`
- `portfolio_manager`
- `complete_report`
- `quality_review`

The collector also writes `reports/<TICKER>/<DATE>/debate_record.md` and creates pending Markdown files for every stage output path. The task preparer does not replace those pending files; Codex role execution writes the role reports. Use `debate_record.md` and `tasks/task_manifest.json` to find the visible debate turn order and per-stage task files.

Quick checks:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_codex_self_contained_skillkit.py -q
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit\tests\test_skillkit_bundle.py -q
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\skills\tradingagents-ticker-workflow-runner\scripts\prepare_skill_workflow.py --ticker AAPL,MSFT --trade-date 2026-06-27 --format json
```

Safety:
- This is a paper-study workflow.
- It does not submit broker orders.
- It does not connect to GCAF.
- The runner prepares workflow packets only; it does not call live LLMs or market-data vendors.
- The evidence collector can call market-data services through upstream dataflow tools, but it does not call LLMs.
- The Sentiment Analyst evidence collector uses direct StockTwits and Reddit collection rather than reusing the news feed.
- The task preparer does not call upstream graph orchestration, external LLMs, broker APIs, or market-data vendors; it writes task prompts from the already collected evidence packet.
- Codex must keep role passes independent: each analyst role reads only its own `evidence/<TICKER>/<DATE>/roles/<role>.md` packet; downstream debate/trading/risk roles read prior reports only at their workflow stage.
- `workflow_state.json` is the automatic run contract: it lists stage order, allowed inputs, forbidden inputs, and report paths.
- `debate_record.md` is the report-folder index for the research and risk debate turns.
- Missing stage outputs are created as pending Markdown files so every path listed in the debate record is findable from `reports/`.
- The complete report must preserve exact visible debate headings and pass `validate_complete_report.py`.
- Analytical quality is reviewed by the `tradingagents-quality-reviewer` skill, which writes `quality_review.md` and `quality_gate.json`.
