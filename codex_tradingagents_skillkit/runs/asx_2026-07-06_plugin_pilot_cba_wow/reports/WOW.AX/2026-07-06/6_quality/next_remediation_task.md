# Next Quality Remediation Task

Ticker: `WOW.AX`
Trade date: `2026-07-06`
Root cause category: `asx_core_metric_coverage_insufficient`
Failed gate: `asx_core_metric_coverage_gate`
Status: `pending`

## Validator Error

ASX core metric coverage failed; review-ready quality gate cannot pass

## Required Fix

Improve ASX core financial metric extraction or mark genuinely absent metrics unavailable with documented source absence; do not accept unresolved core metrics as review-ready.

## Affected Files

- `codex_tradingagents_skillkit/scripts/core_metric_coverage.py`
- `codex_tradingagents_skillkit/scripts/financial_document_sources_asx.py`
- `codex_tradingagents_skillkit/scripts/financial_document_evidence.py`
- `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
- `codex_tradingagents_skillkit/scripts/run_codex_role_workflow.py`

## Required Tests

- `codex_tradingagents_skillkit/tests/test_asx_core_metric_coverage.py`
- `codex_tradingagents_skillkit/tests/test_financial_document_sources.py`

## Verification And Rerun

1. Implement the required fix with tests.
2. Run the required tests and the relevant full verification suite.
3. Rerun evidence collection and report workflow using:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\collect_role_evidence.py --ticker WOW.AX --trade-date 2026-07-06 --output-dir codex_tradingagents_skillkit\runs\asx_2026-07-06_plugin_pilot_cba_wow
```

4. Rerun the Codex workflow controller.
5. Update `quality_remediation_plan.json` task status only after the quality gate no longer reports this failure.

## Closed-Loop Rule

Do not stop at this task file. Codex must implement the fix, rerun the workflow,
and continue with the next pending remediation task until the quality gate passes
or a true external blocker is documented.
