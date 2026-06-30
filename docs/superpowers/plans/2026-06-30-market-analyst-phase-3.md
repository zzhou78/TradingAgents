# Market Analyst Phase 3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade only the Market Analyst role so quantitative market evidence is ledger-backed, visible in task prompts, and protected by contradiction gates.

**Architecture:** Reuse the shared `EvidenceLedgerEntry` and `RoleExecutionContract` models. Add a market evidence adapter that turns market tool outputs into normalized metric observations, relation checks such as latest close versus moving averages, and evidence ledger entries; Codex still writes final technical interpretation.

**Tech Stack:** Python standard library, existing `pytest`, existing market tool outputs, JSON/JSONL evidence files, Markdown role reports.

---

## File Structure

- Create: `codex_tradingagents_skillkit/scripts/market_data_evidence.py`
  - Normalizes market tool outputs into metric observations and ledger entries.
- Modify: `codex_tradingagents_skillkit/scripts/collect_role_evidence.py`
  - Writes `evidence/<TICKER>/<DATE>/market/quantitative_observations.json`.
  - Writes `evidence/<TICKER>/<DATE>/market/evidence_ledger.jsonl`.
  - Adds Market Analyst RoleExecutionContract to `workflow_state.json`.
- Modify: `codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py`
  - Adds Market Analyst evidence boundary wording to generated task prompts.
- Modify: `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
  - Adds market contradiction checks for latest close versus 10 EMA, 50 SMA, and 200 SMA when values are present.
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-market-analyst/SKILL.md`
  - Adds RoleExecutionContract and evidence ID citation rules.
- Modify: `.codex/skills/tradingagents-market-analyst/SKILL.md`
  - Mirrors the bundled Market skill update.
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`
  - Adds Market Analyst contradiction gate wording.
- Modify: `.codex/skills/tradingagents-quality-reviewer/SKILL.md`
  - Mirrors the bundled Quality skill update.
- Test: `tests/test_market_data_evidence.py`
  - Unit tests for metric extraction, moving-average relation records, unavailable tool handling, and ledger output.
- Modify Test: `tests/test_codex_role_evidence_collector.py`
  - Adds workflow-state and generated-path assertions for Market evidence.
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`
  - Adds task prompt, quality gate, and skill text assertions.

### Task 1: Market Evidence Adapter

**Files:**
- Create: `codex_tradingagents_skillkit/scripts/market_data_evidence.py`
- Test: `tests/test_market_data_evidence.py`

- [ ] **Step 1: Write failing tests**

Create tests that call `build_market_data_evidence()` with market tool calls containing:

- latest close;
- 10 EMA;
- 50 SMA;
- 200 SMA;
- RSI;
- MACD;
- ATR;
- volume;
- one failed indicator call.

Assert that:

- output contains `metric_observations`;
- each observation has `evidence_id`, `metric_name`, `value`, `tool_name`, `status`, `supports_claims`, `confidence`, and `final_market_judgment`;
- relation observations include `latest_close_vs_200_sma=below` when close is below 200 SMA;
- failed tool calls produce low-confidence unavailable observations;
- ledger entries use role `market_analyst`.

- [ ] **Step 2: Run failing tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_market_data_evidence.py -q
```

Expected: FAIL because `market_data_evidence.py` does not exist.

- [ ] **Step 3: Implement adapter**

Implement:

- `build_market_data_evidence(ticker, trade_date, tool_calls, structured_output_path, retrieval_time)`;
- stable IDs: `market:<TICKER>:<TRADE_DATE>:001`;
- metric extraction for common labels: latest close, close, 10 EMA, 50 SMA, 200 SMA, RSI, MACD, ATR, volume;
- relation records for latest close versus each moving average when both values are available;
- `final_market_judgment="pending_codex_interpretation"`.

- [ ] **Step 4: Run adapter tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_market_data_evidence.py -q
```

Expected: PASS.

### Task 2: Collector Integration And RoleExecutionContract

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/collect_role_evidence.py`
- Modify Test: `tests/test_codex_role_evidence_collector.py`

- [ ] **Step 1: Add failing collector test**

Add a test that runs the collector with mocked market tool outputs and asserts:

- `market/quantitative_observations.json` exists;
- `market/evidence_ledger.jsonl` exists;
- `workflow_state.json` market stage contains `role_execution_contract`;
- market stage allowed inputs include observation and ledger paths.

- [ ] **Step 2: Run collector tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_codex_role_evidence_collector.py -q
```

Expected: FAIL until collector writes market evidence files and contract.

- [ ] **Step 3: Implement collector integration**

Modify collection so the market tool calls are passed to the adapter, written to the market evidence folder, and added to the Market Analyst stage.

- [ ] **Step 4: Run collector tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_codex_role_evidence_collector.py -q
```

Expected: PASS.

### Task 3: Market Task Prompt Integration

**Files:**
- Modify: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`
- Modify: `codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py`

- [ ] **Step 1: Add task prompt assertions**

Assert `market_analyst_task.md` contains:

- `## RoleExecutionContract`;
- `quantitative_observations.json`;
- `evidence_ledger.jsonl`;
- `Python metric observations are not final technical judgments`;
- `Do not make price-versus-moving-average claims without metric evidence IDs`.

- [ ] **Step 2: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL until market contract and boundary wording appear.

- [ ] **Step 3: Add market boundary block**

Add Market Analyst prompt boundary wording in `prepare_codex_report_tasks.py`.

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

### Task 4: Market Contradiction Quality Gates

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add failing quality tests**

Add tests that fail when:

- report text says price is above 200 SMA while extracted values show latest close below 200 SMA;
- report text says price is below 200 SMA while extracted values show latest close above 200 SMA;
- pending `market.md` is present in a completed review.

- [ ] **Step 2: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL until validator checks are implemented.

- [ ] **Step 3: Implement market quality checks**

Add helper logic that extracts latest close and SMA values from Market report text and rejects contradictory above/below claims when numeric values are present.

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

### Task 5: Skill Text And Mirror Updates

**Files:**
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-market-analyst/SKILL.md`
- Modify: `.codex/skills/tradingagents-market-analyst/SKILL.md`
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`
- Modify: `.codex/skills/tradingagents-quality-reviewer/SKILL.md`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add failing skill assertions**

Assert Market skill contains:

- `RoleExecutionContract`;
- `evidence_id`;
- `Python metric observations are not final technical judgments`;
- `Do not make price-versus-moving-average claims without metric evidence IDs`.

Assert Quality skill contains:

- `market moving-average claim conflicts with metric evidence`;
- `market.md is still pending`.

- [ ] **Step 2: Run bundle tests**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL until skills are updated.

- [ ] **Step 3: Update bundled and canonical skill copies**

Add the same Market Analyst evidence gate wording to both skill roots.

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
.\.venv\Scripts\python.exe -m pytest tests/test_market_data_evidence.py tests/test_codex_role_evidence_collector.py codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

- [ ] **Step 2: Run lint on changed Python files**

Run:

```powershell
.\.venv\Scripts\python.exe -m ruff check codex_tradingagents_skillkit/scripts tests codex_tradingagents_skillkit/tests
```

Expected: PASS.

- [ ] **Step 3: Run full test suite**

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Expected: PASS, with existing optional-provider skips acceptable.

## Acceptance Criteria

- Market Analyst has normalized metric observations.
- Market Analyst has ledger output.
- `workflow_state.json` contains a Market Analyst RoleExecutionContract.
- `market_analyst_task.md` exposes the contract and evidence paths.
- Market quality gates reject price-versus-moving-average contradictions.
- Bundled and `.codex/skills` Market/Quality skill files remain mirrored.
- No role beyond Market Analyst is claimed as upgraded by this phase.
