# Codex-Session TradingAgents Workflow Runbook

This workflow is for Codex-operated paper-study reports. It does not call the
upstream TradingAgents graph for role reasoning, does not submit broker orders,
and does not install new tools or grant credentials.

## Boundary

- Python collects, extracts, normalizes, deduplicates, queues, and validates evidence.
- Python may calculate market metrics, extract filing sections, summarize social-feed counts, and build article evidence cards.
- Python must not make final investment judgments.
- Codex acts each role with the named TradingAgents skill and writes the role report.
- Codex may use already-approved local tools and Python helpers for repeatable extraction or validation.
- Codex must not install new plugins, grant credentials, use broker/order tools, or use browser/computer-use actions that could affect real trading without approval.
- A standalone unattended run would require a future approved model backend; the default runner is a Codex-session controller only.

## Commands

Collect evidence:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\collect_role_evidence.py --ticker AAPL,MSFT --trade-date 2026-06-30 --output-dir codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_validation_final
```

Prepare task prompts:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\prepare_codex_report_tasks.py --output-dir codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_validation_final
```

Ask the controller for the next Codex stage:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\run_codex_role_workflow.py --output-dir codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_validation_final
```

Codex then reads the reported task file, reads only its allowed inputs and
allowed memory files, writes the reported output file, and reruns the controller.
The workflow is complete only when every stage is complete and the final quality
gate has no errors.

## Gates

- Pending role outputs block downstream stages that depend on them.
- A completed role output must remove `Pending Codex role output`.
- A completed role output must include its RoleExecutionContract sections.
- A completed role output must include evidence citations when the contract requires them.
- A completed role output must include the required `## Memory Update` footer fields.
- `complete_report.md` is not accepted while required role outputs are pending.
- `quality_gate.json` must not pass while validator errors exist.
- ASX source collection failure blocks normal ASX company review completion unless Quality Reviewer documents the unresolved limitation.
