# Financial Report Analyst Phase 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade only the Financial Report Analyst role so filing/document evidence is section-level, ledger-backed, visible in task prompts, and enforced by quality gates.

**Architecture:** Reuse the Phase 1 `EvidenceLedgerEntry` and `RoleExecutionContract` models. Keep the existing SEC/ASX document collectors as source fetchers, then add a financial evidence adapter that flattens 10-K/10-Q sections, ASX extracted sections, 8-K cover pages, and Exhibit 99.1 records into `section_records.json` plus `evidence_ledger.jsonl` for Codex to interpret.

**Tech Stack:** Python standard library, existing `pytest`, existing SEC/ASX collectors, JSON/JSONL evidence files, Markdown role reports.

---

## File Structure

- Create: `codex_tradingagents_skillkit/scripts/financial_document_evidence.py`
  - Converts collected financial document packets into section/exhibit evidence records and ledger entries.
- Modify: `codex_tradingagents_skillkit/scripts/collect_role_evidence.py`
  - Writes `evidence/<TICKER>/<DATE>/financial_report/section_records.json`.
  - Writes `evidence/<TICKER>/<DATE>/financial_report/evidence_ledger.jsonl`.
  - Adds Financial Report Analyst RoleExecutionContract to `workflow_state.json`.
- Modify: `codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py`
  - Already supports generic contract rendering; tests must prove financial contracts and evidence paths appear in `financial_report_task.md`.
- Modify: `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
  - Adds Financial Report claim-source table checks for missing section/evidence citations and missing evidence gaps.
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-financial-report-analyst/SKILL.md`
  - Adds RoleExecutionContract and evidence ID citation rules.
- Modify: `.codex/skills/tradingagents-financial-report-analyst/SKILL.md`
  - Mirrors the bundled skill update.
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`
  - Adds Financial Report evidence gate wording.
- Modify: `.codex/skills/tradingagents-quality-reviewer/SKILL.md`
  - Mirrors the bundled skill update.
- Test: `tests/test_financial_document_evidence.py`
  - Unit tests for flattening SEC sections, 8-K Exhibit 99.1, ASX sections, unavailable evidence gaps, and ledger fields.
- Modify Test: `tests/test_codex_role_evidence_collector.py`
  - Adds workflow-state and generated-path assertions for Financial Report evidence.
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`
  - Adds task prompt, quality gate, and skill text assertions.

### Task 1: Financial Section Evidence Adapter

**Files:**
- Create: `codex_tradingagents_skillkit/scripts/financial_document_evidence.py`
- Test: `tests/test_financial_document_evidence.py`

- [ ] **Step 1: Write failing tests**

Create tests that call `build_financial_document_evidence()` with a packet containing:

- a 10-K section record;
- a 10-Q unavailable capex section;
- an 8-K cover page;
- an available Exhibit 99.1;
- an ASX extracted section.

Assert that:

- output contains `section_records`;
- each record has `evidence_id`, `source_type`, `section_name`, `section_kind`, `status`, `filing_date`, `url`, `excerpt`, `supports_claims`, and `evidence_gap`;
- unavailable sections are retained as evidence gaps;
- ledger entries use role `financial_report_analyst`;
- Python does not create final financial conclusions.

- [ ] **Step 2: Run failing tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_financial_document_evidence.py -q
```

Expected: FAIL because `financial_document_evidence.py` does not exist.

- [ ] **Step 3: Implement adapter**

Implement:

- `build_financial_document_evidence(ticker, trade_date, packet, structured_output_path, retrieval_time)`;
- stable IDs: `financial:<TICKER>:<TRADE_DATE>:001`;
- confidence: `medium` for available excerpt, `low` for unavailable/error;
- limitations: `section_unavailable`, `source_unavailable`, `cover_page_only`, or `exhibit_unavailable` where applicable.

- [ ] **Step 4: Run adapter tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_financial_document_evidence.py -q
```

Expected: PASS.

### Task 2: Collector Integration And RoleExecutionContract

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/collect_role_evidence.py`
- Modify Test: `tests/test_codex_role_evidence_collector.py`

- [ ] **Step 1: Add failing collector test**

Add a test that runs the collector with a mocked financial packet and asserts:

- `financial_report/section_records.json` exists;
- `financial_report/evidence_ledger.jsonl` exists;
- `workflow_state.json` financial stage contains `role_execution_contract`;
- financial stage allowed inputs include the section records and ledger paths.

- [ ] **Step 2: Run collector tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_codex_role_evidence_collector.py -q
```

Expected: FAIL on missing financial evidence files or contract.

- [ ] **Step 3: Implement collector integration**

Modify collection so the financial document packet is preserved as structured data, passed to the adapter, written to the financial report evidence folder, and added to the Financial Report Analyst stage.

- [ ] **Step 4: Run collector tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_codex_role_evidence_collector.py -q
```

Expected: PASS.

### Task 3: Financial Task Prompt Integration

**Files:**
- Modify: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`
- Modify: `codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py` only if tests show a gap.

- [ ] **Step 1: Add task prompt assertions**

Assert `financial_report_task.md` contains:

- `## RoleExecutionContract`;
- `section_records.json`;
- `evidence_ledger.jsonl`;
- `Python section records are not final financial judgments`;
- `Do not make major financial claims without section evidence IDs or explicit evidence gaps`.

- [ ] **Step 2: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL until the financial contract is rendered and boundary wording is present.

- [ ] **Step 3: Add financial boundary block if needed**

If generic contract rendering is insufficient, add a Financial Report Analyst boundary block in `prepare_codex_report_tasks.py`.

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

### Task 4: Financial Claim-Source Quality Gates

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add failing quality tests**

Add tests that fail when:

- a Financial Report Analyst `## Claim-Source Table` contains a substantive claim but no evidence ID or source section;
- a missing capex/guidance/segment row has no evidence gap;
- a pending `financial_report.md` is present in a completed review.

- [ ] **Step 2: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL until validator checks are implemented.

- [ ] **Step 3: Implement financial quality checks**

Add helper logic that parses `## Claim-Source Table`, detects rows, and enforces:

- evidence IDs matching `financial:<ticker>:<date>:NNN`, or recognizable source sections such as `10-K`, `10-Q`, `8-K Exhibit 99.1`, `ASX`, or `structured fundamentals packet`;
- empty source/section cells require a non-empty evidence gap;
- pending financial output blocks success.

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

### Task 5: Skill Text And Mirror Updates

**Files:**
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-financial-report-analyst/SKILL.md`
- Modify: `.codex/skills/tradingagents-financial-report-analyst/SKILL.md`
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`
- Modify: `.codex/skills/tradingagents-quality-reviewer/SKILL.md`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add failing skill assertions**

Assert financial skill contains:

- `RoleExecutionContract`;
- `evidence_id`;
- `Python section records are not final financial judgments`;
- `Do not make major financial claims without section evidence IDs or explicit evidence gaps`.

Assert quality skill contains:

- `financial claim lacks section evidence citation`;
- `financial evidence gap missing for unavailable section`.

- [ ] **Step 2: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL until skills are updated.

- [ ] **Step 3: Update bundled and canonical skill copies**

Add the same Financial Report evidence gate wording to both skill roots.

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

### Task 6: Verification

**Files:**
- No new source files.

- [ ] **Step 1: Run focused tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_financial_document_evidence.py tests/test_codex_role_evidence_collector.py codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

- [ ] **Step 2: Run financial document source tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_financial_document_sources.py -q
```

Expected: PASS.

- [ ] **Step 3: Run lint on changed Python files**

Run:

```powershell
.\.venv\Scripts\python.exe -m ruff check codex_tradingagents_skillkit/scripts tests codex_tradingagents_skillkit/tests
```

Expected: PASS.

- [ ] **Step 4: Run full test suite**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Expected: PASS, with existing optional-provider skips acceptable.

## Acceptance Criteria

- Financial Report Analyst has section/exhibit evidence records.
- Financial Report Analyst has ledger output.
- `workflow_state.json` contains a Financial Report Analyst RoleExecutionContract.
- `financial_report_task.md` exposes the contract and evidence paths.
- Claim-source quality gates reject unsupported financial claims.
- Missing capex/guidance/segment detail is represented as an evidence gap.
- Bundled and `.codex/skills` Financial/Quality skill files remain mirrored.
- No role beyond Financial Report Analyst is claimed as upgraded by this phase.
