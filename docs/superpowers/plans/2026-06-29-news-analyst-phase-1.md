# News Analyst Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade only the News Analyst role so it has structured article evidence cards, evidence ledger output, RoleExecutionContract integration, report prompt integration, and hard quality gates.

**Architecture:** Add small Python helpers under `codex_tradingagents_skillkit/scripts` that normalize candidate news records, distinguish full-text from snippet-only evidence, deduplicate repeated items, write a machine-readable evidence ledger, and validate News Analyst report support. Codex remains responsible for final news impact interpretation and writing `news.md`.

**Tech Stack:** Python standard library, existing `pytest`, existing skillkit scripts, JSON/JSONL evidence files, Markdown role reports.

---

## File Structure

- Create: `codex_tradingagents_skillkit/scripts/evidence_contracts.py`
  - Defines `EvidenceLedgerEntry`, `RoleExecutionContract`, validation helpers, and JSON/JSONL serialization.
- Create: `codex_tradingagents_skillkit/scripts/news_article_evidence.py`
  - Converts raw candidate news records into normalized article evidence records and ledger entries.
- Modify: `codex_tradingagents_skillkit/scripts/collect_role_evidence.py`
  - Calls the News article evidence helper after existing `get_news` and `get_global_news` collection.
  - Writes `evidence/<TICKER>/<DATE>/news/article_cards.json` and `evidence_ledger.jsonl`.
  - Adds News RoleExecutionContract fields to `workflow_state.json`.
- Modify: `codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py`
  - Includes the News RoleExecutionContract and article evidence paths in `news_analyst_task.md`.
  - States that Python candidate fields are not final impact judgments.
- Modify: `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
  - Fails completed reports when News Analyst impact labels lack article-card support.
  - Fails high-confidence snippet-only article usage.
  - Fails successful quality gates when News role output is pending.
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md`
  - Adds exact article-card citation and tool-output rules.
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`
  - Adds News evidence ledger and impact-label checks.
- Test: `tests/test_news_evidence_contracts.py`
  - Unit tests for ledger schema, role contract, and invalid records.
- Test: `tests/test_news_article_evidence.py`
  - Unit tests for full-text/snippet distinction, dedupe, as-of discipline, and Python/Codex boundary.
- Modify Test: `tests/test_codex_role_evidence_collector.py`
  - Adds workflow-state and generated-path assertions for News evidence.
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`
  - Adds task prompt and quality gate assertions.

### Task 1: Evidence Contract Models

**Files:**
- Create: `codex_tradingagents_skillkit/scripts/evidence_contracts.py`
- Test: `tests/test_news_evidence_contracts.py`

- [ ] **Step 1: Write failing tests for required ledger fields**

Add this test file:

```python
from __future__ import annotations

import json
from pathlib import Path

import pytest

from codex_tradingagents_skillkit.scripts.evidence_contracts import (
    EvidenceLedgerEntry,
    RoleExecutionContract,
    validate_evidence_ledger_entry,
    write_jsonl,
)


def test_evidence_ledger_entry_requires_machine_readable_fields(tmp_path: Path):
    entry = EvidenceLedgerEntry(
        evidence_id="news:AAPL:2026-06-29:001",
        ticker="AAPL",
        trade_date="2026-06-29",
        role="news_analyst",
        tool_name="news_article_evidence",
        tool_version="0.1.0",
        source_url="https://example.com/aapl-ai-update",
        source_date="2026-06-28",
        retrieval_time="2026-06-29T09:30:00+10:00",
        as_of_validity={
            "valid_for_trade_date": True,
            "reason": "source_date is on or before trade_date",
        },
        confidence="medium",
        limitations=["snippet_only"],
        structured_output_path="runs/x/evidence/AAPL/2026-06-29/news/article_cards.json",
        report_sections_using_it=["News Analyst"],
    )

    payload = validate_evidence_ledger_entry(entry.to_dict())

    assert payload["evidence_id"] == "news:AAPL:2026-06-29:001"
    assert payload["as_of_validity"]["valid_for_trade_date"] is True
    assert payload["limitations"] == ["snippet_only"]


def test_evidence_ledger_validation_rejects_missing_required_field():
    payload = {
        "evidence_id": "news:AAPL:2026-06-29:001",
        "ticker": "AAPL",
    }

    with pytest.raises(ValueError, match="missing required evidence ledger field: trade_date"):
        validate_evidence_ledger_entry(payload)


def test_write_jsonl_serializes_one_entry_per_line(tmp_path: Path):
    path = tmp_path / "evidence_ledger.jsonl"
    entry = EvidenceLedgerEntry(
        evidence_id="news:AAPL:2026-06-29:001",
        ticker="AAPL",
        trade_date="2026-06-29",
        role="news_analyst",
        tool_name="news_article_evidence",
        tool_version="0.1.0",
        source_url="https://example.com/aapl",
        source_date="2026-06-28",
        retrieval_time="2026-06-29T09:30:00+10:00",
        as_of_validity={"valid_for_trade_date": True, "reason": "source_date is on or before trade_date"},
        confidence="medium",
        limitations=[],
        structured_output_path="article_cards.json",
        report_sections_using_it=["News Analyst"],
    )

    write_jsonl(path, [entry.to_dict()])

    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["evidence_id"] == "news:AAPL:2026-06-29:001"


def test_role_execution_contract_records_allowed_and_forbidden_boundaries():
    contract = RoleExecutionContract(
        role="news_analyst",
        allowed_inputs=["roles/news.md", "news/article_cards.json", "news/evidence_ledger.jsonl"],
        forbidden_inputs=["future_articles", "uncited_memory", "raw_social_feed_as_news"],
        allowed_memory=["memory/AAPL/news_analyst/memory.md"],
        forbidden_memory=["other_role_memory", "other_ticker_memory"],
        required_tools=["candidate_news_search", "news_article_evidence", "news_evidence_ledger_validator"],
        optional_tools=["browser_full_text_check", "company_ir_search"],
        required_output_sections=[
            "Tool Outputs Used",
            "Article Evidence Cards",
            "News Impact Summary",
            "Evidence Gaps",
            "Memory Update",
        ],
        required_evidence_citations=["evidence_id", "source_url", "source_date", "full_text_status"],
        quality_gate="news_analyst_quality_gate",
        memory_update_schema={
            "durable_facts_to_retain": ["string"],
            "prior_mistakes_to_avoid": ["string"],
            "open_questions": ["string"],
            "evidence_references": ["evidence_id"],
            "staleness_or_expiry": "string",
        },
    )

    payload = contract.to_dict()

    assert payload["role"] == "news_analyst"
    assert "future_articles" in payload["forbidden_inputs"]
    assert "evidence_id" in payload["required_evidence_citations"]
```

- [ ] **Step 2: Run the contract tests and confirm they fail**

Run:

```powershell
python -m pytest tests/test_news_evidence_contracts.py -q
```

Expected: FAIL because `codex_tradingagents_skillkit.scripts.evidence_contracts` does not exist.

- [ ] **Step 3: Implement the minimal contract module**

Create `codex_tradingagents_skillkit/scripts/evidence_contracts.py` with:

```python
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

REQUIRED_EVIDENCE_LEDGER_FIELDS = [
    "evidence_id",
    "ticker",
    "trade_date",
    "role",
    "tool_name",
    "tool_version",
    "source_url",
    "source_date",
    "retrieval_time",
    "as_of_validity",
    "confidence",
    "limitations",
    "structured_output_path",
    "report_sections_using_it",
]


@dataclass(frozen=True)
class EvidenceLedgerEntry:
    evidence_id: str
    ticker: str
    trade_date: str
    role: str
    tool_name: str
    tool_version: str
    source_url: str
    source_date: str
    retrieval_time: str
    as_of_validity: dict[str, Any]
    confidence: str
    limitations: list[str]
    structured_output_path: str
    report_sections_using_it: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RoleExecutionContract:
    role: str
    allowed_inputs: list[str]
    forbidden_inputs: list[str]
    allowed_memory: list[str]
    forbidden_memory: list[str]
    required_tools: list[str]
    optional_tools: list[str]
    required_output_sections: list[str]
    required_evidence_citations: list[str]
    quality_gate: str
    memory_update_schema: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def validate_evidence_ledger_entry(payload: dict[str, Any]) -> dict[str, Any]:
    for field in REQUIRED_EVIDENCE_LEDGER_FIELDS:
        if field not in payload:
            raise ValueError(f"missing required evidence ledger field: {field}")
    if not isinstance(payload["as_of_validity"], dict):
        raise ValueError("as_of_validity must be an object")
    if "valid_for_trade_date" not in payload["as_of_validity"]:
        raise ValueError("as_of_validity.valid_for_trade_date is required")
    if payload["confidence"] not in {"high", "medium", "low"}:
        raise ValueError("confidence must be high, medium, or low")
    if not isinstance(payload["limitations"], list):
        raise ValueError("limitations must be a list")
    if not isinstance(payload["report_sections_using_it"], list):
        raise ValueError("report_sections_using_it must be a list")
    return payload


def write_jsonl(path: Path, entries: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(validate_evidence_ledger_entry(entry), sort_keys=True) for entry in entries]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
```

- [ ] **Step 4: Run contract tests and confirm they pass**

Run:

```powershell
python -m pytest tests/test_news_evidence_contracts.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit the contract module**

Run:

```powershell
git add codex_tradingagents_skillkit/scripts/evidence_contracts.py tests/test_news_evidence_contracts.py
git commit -m "Add evidence ledger and role contract models"
```

### Task 2: News Article Evidence Tool

**Files:**
- Create: `codex_tradingagents_skillkit/scripts/news_article_evidence.py`
- Test: `tests/test_news_article_evidence.py`

- [ ] **Step 1: Write failing tests for article cards**

Add `tests/test_news_article_evidence.py`:

```python
from __future__ import annotations

from codex_tradingagents_skillkit.scripts.news_article_evidence import build_news_evidence


def test_build_news_evidence_distinguishes_full_text_from_snippet_only():
    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Apple supplier update",
                "source": "Example News",
                "url": "https://example.com/apple-supplier",
                "published_date": "2026-06-28",
                "snippet": "Apple supplier commentary.",
                "full_text": "Apple supplier commentary with enough article body detail for extraction.",
            },
            {
                "title": "Apple analyst note",
                "source": "Example News",
                "url": "https://example.com/apple-analyst",
                "published_date": "2026-06-28",
                "snippet": "Analyst note summary only.",
                "full_text": "",
            },
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    cards = result["article_cards"]

    assert cards[0]["full_text_status"] == "full_text"
    assert cards[0]["confidence"] == "medium"
    assert cards[1]["full_text_status"] == "snippet_only"
    assert cards[1]["confidence"] == "low"
    assert "likely_effect" not in cards[0]


def test_build_news_evidence_deduplicates_by_normalized_url_and_title():
    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Apple announces service update",
                "source": "Example News",
                "url": "https://example.com/apple-services?utm_source=x",
                "published_date": "2026-06-28",
                "snippet": "Apple services update.",
                "full_text": "",
            },
            {
                "title": "Apple announces service update",
                "source": "Example News",
                "url": "https://example.com/apple-services",
                "published_date": "2026-06-28",
                "snippet": "Duplicate article.",
                "full_text": "",
            },
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    assert len(result["article_cards"]) == 1
    assert result["article_cards"][0]["duplicate_count"] == 2


def test_build_news_evidence_marks_post_trade_date_invalid():
    result = build_news_evidence(
        ticker="AAPL",
        trade_date="2026-06-29",
        candidates=[
            {
                "title": "Future Apple article",
                "source": "Example News",
                "url": "https://example.com/future",
                "published_date": "2026-06-30",
                "snippet": "Future item.",
                "full_text": "",
            }
        ],
        structured_output_path="runs/x/news/article_cards.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    card = result["article_cards"][0]
    ledger = result["ledger_entries"][0]

    assert card["as_of_validity"]["valid_for_trade_date"] is False
    assert ledger["as_of_validity"]["valid_for_trade_date"] is False
    assert "post_trade_date" in card["limitations"]
```

- [ ] **Step 2: Run article tests and confirm they fail**

Run:

```powershell
python -m pytest tests/test_news_article_evidence.py -q
```

Expected: FAIL because `news_article_evidence.py` does not exist.

- [ ] **Step 3: Implement normalized article cards**

Create `codex_tradingagents_skillkit/scripts/news_article_evidence.py` with these functions:

```python
from __future__ import annotations

import hashlib
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from evidence_contracts import EvidenceLedgerEntry

TOOL_NAME = "news_article_evidence"
TOOL_VERSION = "0.1.0"
TRACKING_QUERY_PREFIXES = ("utm_",)
TRACKING_QUERY_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}


def _normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key not in TRACKING_QUERY_KEYS and not key.startswith(TRACKING_QUERY_PREFIXES)
    ]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), ""))


def _fingerprint(candidate: dict[str, str]) -> str:
    normalized_url = _normalize_url(str(candidate.get("url", "")))
    title = re.sub(r"\s+", " ", str(candidate.get("title", "")).strip().lower())
    return hashlib.sha256(f"{normalized_url}|{title}".encode("utf-8")).hexdigest()[:16]


def _full_text_status(candidate: dict[str, str]) -> str:
    full_text = str(candidate.get("full_text") or "").strip()
    return "full_text" if len(full_text) >= 40 else "snippet_only"


def _confidence(full_text_status: str, limitations: list[str]) -> str:
    if "post_trade_date" in limitations:
        return "low"
    if full_text_status == "snippet_only":
        return "low"
    return "medium"


def build_news_evidence(
    *,
    ticker: str,
    trade_date: str,
    candidates: list[dict[str, str]],
    structured_output_path: str,
    retrieval_time: str,
) -> dict[str, list[dict[str, object]]]:
    seen: dict[str, dict[str, object]] = {}
    order: list[str] = []
    for candidate in candidates:
        key = _fingerprint(candidate)
        if key in seen:
            seen[key]["duplicate_count"] = int(seen[key]["duplicate_count"]) + 1
            continue
        published_date = str(candidate.get("published_date") or "")
        valid_for_trade_date = bool(published_date and published_date <= trade_date)
        limitations: list[str] = []
        full_text_status = _full_text_status(candidate)
        if full_text_status == "snippet_only":
            limitations.append("snippet_only")
        if not valid_for_trade_date:
            limitations.append("post_trade_date")
        confidence = _confidence(full_text_status, limitations)
        evidence_id = f"news:{ticker}:{trade_date}:{len(order) + 1:03d}"
        as_of_validity = {
            "valid_for_trade_date": valid_for_trade_date,
            "reason": "source_date is on or before trade_date"
            if valid_for_trade_date
            else "source_date is after trade_date",
        }
        card = {
            "evidence_id": evidence_id,
            "ticker": ticker,
            "trade_date": trade_date,
            "title": str(candidate.get("title") or "").strip(),
            "source": str(candidate.get("source") or "").strip(),
            "source_url": _normalize_url(str(candidate.get("url") or "")),
            "source_date": published_date,
            "retrieval_time": retrieval_time,
            "full_text_status": full_text_status,
            "direct_company_relevance": "pending_codex_interpretation",
            "event_type": "pending_codex_interpretation",
            "key_facts": [],
            "novelty": "pending_codex_interpretation",
            "materiality": "pending_codex_interpretation",
            "reason": "pending_codex_interpretation",
            "confidence": confidence,
            "evidence_gap": "full text unavailable" if full_text_status == "snippet_only" else "",
            "limitations": limitations,
            "as_of_validity": as_of_validity,
            "duplicate_count": 1,
        }
        seen[key] = card
        order.append(key)

    article_cards = [seen[key] for key in order]
    ledger_entries = [
        EvidenceLedgerEntry(
            evidence_id=str(card["evidence_id"]),
            ticker=ticker,
            trade_date=trade_date,
            role="news_analyst",
            tool_name=TOOL_NAME,
            tool_version=TOOL_VERSION,
            source_url=str(card["source_url"]),
            source_date=str(card["source_date"]),
            retrieval_time=retrieval_time,
            as_of_validity=dict(card["as_of_validity"]),
            confidence=str(card["confidence"]),
            limitations=list(card["limitations"]),
            structured_output_path=structured_output_path,
            report_sections_using_it=["News Analyst"],
        ).to_dict()
        for card in article_cards
    ]
    return {"article_cards": article_cards, "ledger_entries": ledger_entries}
```

- [ ] **Step 4: Fix imports for script execution**

If direct pytest imports fail because `evidence_contracts` is resolved differently from package imports, replace the import block with:

```python
try:
    from evidence_contracts import EvidenceLedgerEntry
except ModuleNotFoundError:
    from codex_tradingagents_skillkit.scripts.evidence_contracts import EvidenceLedgerEntry
```

- [ ] **Step 5: Run article tests and confirm they pass**

Run:

```powershell
python -m pytest tests/test_news_article_evidence.py -q
```

Expected: PASS.

- [ ] **Step 6: Commit the News article evidence tool**

Run:

```powershell
git add codex_tradingagents_skillkit/scripts/news_article_evidence.py tests/test_news_article_evidence.py
git commit -m "Add News Analyst article evidence tool"
```

### Task 3: Integrate News Evidence Into Collection

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/collect_role_evidence.py`
- Modify Test: `tests/test_codex_role_evidence_collector.py`

- [ ] **Step 1: Add a collector test for News evidence outputs**

Add a test that runs `collect()` with mocked news tool outputs and asserts:

```python
news_dir = output_dir / "evidence" / "AAPL" / "2026-06-29" / "news"
assert (news_dir / "article_cards.json").exists()
assert (news_dir / "evidence_ledger.jsonl").exists()
workflow = json.loads((output_dir / "evidence" / "AAPL" / "2026-06-29" / "workflow_state.json").read_text())
news_stage = next(stage for stage in workflow["stages"] if stage["stage"] == "news_analyst")
assert news_stage["role_execution_contract"]["role"] == "news_analyst"
assert any(path.endswith("news/article_cards.json") for path in news_stage["allowed_inputs"])
assert any(path.endswith("news/evidence_ledger.jsonl") for path in news_stage["allowed_inputs"])
```

- [ ] **Step 2: Run the collector test and confirm it fails**

Run:

```powershell
python -m pytest tests/test_codex_role_evidence_collector.py -q
```

Expected: FAIL on missing `article_cards.json`, `evidence_ledger.jsonl`, or `role_execution_contract`.

- [ ] **Step 3: Add candidate parsing and file writing**

Modify `collect_role_evidence.py` to:

- import `build_news_evidence` and `write_jsonl`;
- create `evidence_dir / "news"`;
- build candidate records from existing `get_news` and `get_global_news` outputs;
- write `article_cards.json`;
- write `evidence_ledger.jsonl`;
- add those paths to the News Analyst stage `allowed_inputs`;
- add `role_execution_contract` to the News Analyst stage.

The parser may initially support structured fixture-like records and fallback text blocks. It must leave final fields such as `direct_company_relevance`, `materiality`, and `reason` as `pending_codex_interpretation`.

- [ ] **Step 4: Run collector tests**

Run:

```powershell
python -m pytest tests/test_codex_role_evidence_collector.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit collection integration**

Run:

```powershell
git add codex_tradingagents_skillkit/scripts/collect_role_evidence.py tests/test_codex_role_evidence_collector.py
git commit -m "Write News Analyst evidence ledger during collection"
```

### Task 4: Integrate Contract Into News Task Prompt

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add prompt integration assertions**

Extend the task-preparation test to assert the generated `news_analyst_task.md` contains:

```python
assert "## RoleExecutionContract" in news_task
assert "article_cards.json" in news_task
assert "evidence_ledger.jsonl" in news_task
assert "Python candidate fields are not final investment judgments" in news_task
assert "Do not assign final impact labels without citing article evidence IDs" in news_task
```

- [ ] **Step 2: Run the skillkit bundle tests and confirm they fail**

Run:

```powershell
python -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL because the prompt does not include the new contract block.

- [ ] **Step 3: Render RoleExecutionContract in task prompts**

Modify `_task_text()` so that when the stage contains `role_execution_contract`, it writes:

```markdown
## RoleExecutionContract

```json
{...contract...}
```
```

For News Analyst, add this rule to the task text:

```markdown
Python candidate fields are not final investment judgments. Do not assign final impact labels without citing article evidence IDs. Snippet-only evidence cannot support high-confidence impact labels.
```

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
python -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit prompt integration**

Run:

```powershell
git add codex_tradingagents_skillkit/scripts/prepare_codex_report_tasks.py codex_tradingagents_skillkit/tests/test_skillkit_bundle.py
git commit -m "Add News Analyst execution contract to task prompts"
```

### Task 5: Add News Quality Gates

**Files:**
- Modify: `codex_tradingagents_skillkit/scripts/validate_quality_review.py`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add failing quality tests**

Add tests that build a temporary report directory and evidence file, then assert validation fails when:

```python
assert "news impact label lacks article evidence citation" in result.stdout
assert "snippet-only news evidence cannot be high confidence" in result.stdout
assert "news.md is still pending" in result.stdout
```

Use report content like:

```markdown
# News Analyst

## Tool Outputs Used

- news_article_evidence

## Article Evidence Cards

| Evidence ID | Title | Full-text status | Confidence |
|---|---|---|---|
| news:AAPL:2026-06-29:001 | Apple analyst note | snippet_only | high |

## News Impact Summary

Overall impact: Positive.
```

- [ ] **Step 2: Run bundle tests and confirm they fail**

Run:

```powershell
python -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL because the validator does not yet inspect News article-card support.

- [ ] **Step 3: Implement News validation helpers**

Modify `validate_quality_review.py` to:

- detect pending `1_analysts/news.md`;
- parse `## Article Evidence Cards`;
- reject high confidence on rows containing `snippet_only`;
- detect impact labels such as `Positive`, `Negative`, `Mixed`, `Material positive`, and `Material negative`;
- require at least one `news:<ticker>:<date>:` evidence ID in the same section when an impact label appears.

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
python -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit quality gates**

Run:

```powershell
git add codex_tradingagents_skillkit/scripts/validate_quality_review.py codex_tradingagents_skillkit/tests/test_skillkit_bundle.py
git commit -m "Gate News Analyst impact labels on article evidence"
```

### Task 6: Update News And Quality Skills

**Files:**
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md`
- Modify: `codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md`
- Modify Test: `codex_tradingagents_skillkit/tests/test_skillkit_bundle.py`

- [ ] **Step 1: Add skill text assertions**

Add assertions that the News skill contains:

```python
assert "RoleExecutionContract" in news_skill
assert "evidence_id" in news_skill
assert "Snippet-only" in news_skill
assert "Python candidate fields are not final investment judgments" in news_skill
```

Add assertions that the Quality Reviewer skill contains:

```python
assert "news impact label lacks article evidence citation" in quality_skill
assert "snippet-only news evidence cannot be high confidence" in quality_skill
```

- [ ] **Step 2: Run bundle tests and confirm they fail**

Run:

```powershell
python -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: FAIL because the skills do not yet contain the new required language.

- [ ] **Step 3: Update skill files**

In `tradingagents-news-analyst/SKILL.md`, add:

```markdown
## RoleExecutionContract Rules

- Read the RoleExecutionContract before writing the report.
- Use only allowed inputs and allowed memory.
- Cite `evidence_id`, source URL, source date, and full-text status for every material article claim.
- Python candidate fields are not final investment judgments.
- Do not assign final impact labels without citing article evidence IDs.
- Snippet-only evidence cannot support high-confidence impact labels.
```

In `tradingagents-quality-reviewer/SKILL.md`, add:

```markdown
## News Analyst Evidence Gate

Fail the report when:
- news impact label lacks article evidence citation;
- snippet-only news evidence cannot be high confidence;
- News Analyst uses post-trade-date evidence as valid;
- News Analyst omits article evidence cards for material news claims.
```

- [ ] **Step 4: Run bundle tests**

Run:

```powershell
python -m pytest codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit skill updates**

Run:

```powershell
git add codex_tradingagents_skillkit/skills/tradingagents-news-analyst/SKILL.md codex_tradingagents_skillkit/skills/tradingagents-quality-reviewer/SKILL.md codex_tradingagents_skillkit/tests/test_skillkit_bundle.py
git commit -m "Document News Analyst evidence gates"
```

### Task 7: End-to-End News Phase Verification

**Files:**
- No new source files.

- [ ] **Step 1: Run focused unit tests**

Run:

```powershell
python -m pytest tests/test_news_evidence_contracts.py tests/test_news_article_evidence.py -q
```

Expected: PASS.

- [ ] **Step 2: Run collector and skillkit tests**

Run:

```powershell
python -m pytest tests/test_codex_role_evidence_collector.py codex_tradingagents_skillkit/tests/test_skillkit_bundle.py -q
```

Expected: PASS.

- [ ] **Step 3: Run existing complete report validator tests**

Run:

```powershell
python -m pytest tests/test_reporting.py -q
```

Expected: PASS.

- [ ] **Step 4: Inspect git diff for scope control**

Run:

```powershell
git status -sb
git diff --stat
```

Expected: only News Phase 1 files are changed. Existing unrelated modified files from the earlier interrupted implementation are not included unless deliberately touched by this plan.

- [ ] **Step 5: Commit final verification note if needed**

If the previous tasks already committed all source changes, do not create an empty commit. If a small documentation update is needed for verification commands, commit only that documentation:

```powershell
git add codex_tradingagents_skillkit/docs/EXPERT_ROLE_WORKFLOW_DESIGN.md docs/superpowers/plans/2026-06-29-news-analyst-phase-1.md
git commit -m "Document News Analyst phase one upgrade plan"
```

## Acceptance Criteria

- `article_cards.json` exists for News Analyst evidence collection.
- `evidence_ledger.jsonl` exists and contains required fields.
- `workflow_state.json` contains a News `role_execution_contract`.
- `news_analyst_task.md` includes the contract and evidence paths.
- News Analyst skill tells Codex that Python candidate fields are not final judgments.
- Quality validation fails unsupported News impact labels.
- Quality validation fails high-confidence snippet-only evidence.
- Quality validation fails pending News role output in a completed review.
- Existing complete-report validation remains passing.
- No other role is claimed as upgraded.

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-29-news-analyst-phase-1.md`. Two execution options:

1. Subagent-Driven (recommended) - dispatch a fresh subagent per task, review between tasks, fast iteration.

2. Inline Execution - execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
