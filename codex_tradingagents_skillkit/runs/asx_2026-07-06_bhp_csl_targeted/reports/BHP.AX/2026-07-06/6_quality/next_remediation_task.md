# Next Quality Remediation Task

Ticker: `BHP.AX`
Trade date: `2026-07-06`
Root cause category: `report_quality_validation`
Failed gate: `quality_review_gate`
Status: `pending`

## Validator Error

market.md is still pending

## Required Fix

Inspect the validator error and repair the relevant report, prompt, validator, or evidence adapter.

## Affected Files

- `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
- `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`

## Required Tests

- `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

## Verification And Rerun

1. Implement the required fix with tests.
2. Run the required tests and the relevant full verification suite.
3. Rerun evidence collection and report workflow using:

```powershell
.\.venv\Scripts\python.exe codex_tradingagents_skillkit\scripts\collect_role_evidence.py --ticker BHP.AX --trade-date 2026-07-06 --output-dir codex_tradingagents_skillkit\runs\asx_2026-07-06_bhp_csl_targeted
```

4. Rerun the Codex workflow controller.
5. Update `quality_remediation_plan.json` task status only after the quality gate no longer reports this failure.

## Closed-Loop Rule

Do not stop at this task file. Codex must implement the fix, rerun the workflow,
and continue with the next pending remediation task until the quality gate passes
or a true external blocker is documented.
