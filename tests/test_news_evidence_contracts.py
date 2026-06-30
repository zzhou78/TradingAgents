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
        as_of_validity={
            "valid_for_trade_date": True,
            "reason": "source_date is on or before trade_date",
        },
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
