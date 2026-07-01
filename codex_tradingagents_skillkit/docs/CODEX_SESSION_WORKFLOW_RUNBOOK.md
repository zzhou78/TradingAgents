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

Generate remediation tasks when the quality gate fails:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\run_quality_remediation.py --output-dir codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_validation_final
```

The remediation command writes `quality_remediation_plan.json` under each
failed report's `6_quality` folder. The plan is an implementation queue for
Codex: it names the failed gate, root-cause category, affected code areas,
required tests, rerun command, and whether the issue blocks review-grade
completion. It does not make investment judgments.

## Gates

- Pending role outputs block downstream stages that depend on them.
- A completed role output must remove `Pending Codex role output`.
- A completed role output must include its RoleExecutionContract sections.
- A completed role output must include evidence citations when the contract requires them.
- A completed role output must include the required `## Memory Update` footer fields.
- `complete_report.md` is not accepted while required role outputs are pending.
- `quality_gate.json` must not pass while validator errors exist.
- Review-grade completion must fail when all news article cards are snippet-only.
- Review-grade completion must fail when structured financial evidence lacks extracted MD&A, lacks a cash-flow statement section, or an earnings-related 8-K only provides cover-page evidence without Exhibit 99.1 or equivalent.
- ASX source collection failure blocks normal ASX company review completion unless Quality Reviewer documents the unresolved limitation.

## Remediation Loop

Quality failure is not the end of the workflow. It starts an engineering
feedback loop:

1. `validate_quality_review.py` emits hard evidence or report-quality errors.
2. `run_quality_remediation.py` converts those errors into
   `quality_remediation_plan.json`.
3. Codex reads the plan and fixes the relevant collector, extractor, role
   prompt, validator, or report-writing step.
4. Tests are added or updated for the exact failure class.
5. Evidence is recollected, tasks are regenerated, reports are rerun, and the
   workflow controller is rerun.
6. The before/after result is recorded in the run folder.

The remediation loop must not weaken a valid quality gate just to pass a run.
If evidence remains insufficient, the plan should keep the report
`validation_only_not_review_ready` and point to the next extractor or source
coverage improvement.

## Standing Auto-Remediation Approval

Option 1 is approved for all future TradingAgents workflows. After a failed
quality gate, Codex must continue automatically; do not ask the user to proceed before executing `next_remediation_task.md`. The next action is to fix
the affected collector, extractor, validator, skill, prompt, or report
integration with tests; rerun the affected ticker workflow; and repeat until the
quality gate passes or a true external blocker is documented.

This standing approval is scoped to the local Codex-session workflow. It does
not approve new plugins, credentials, broker/order tools, real trading actions,
or browser/computer-use actions that could affect real trading.
