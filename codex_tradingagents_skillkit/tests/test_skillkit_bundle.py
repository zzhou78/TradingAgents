from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
SKILLS_ROOT = BUNDLE / "skills"
PREPARER = BUNDLE / "scripts" / "prepare_codex_report_tasks.py"
CODEX_WORKFLOW_RUNNER = BUNDLE / "scripts" / "run_codex_role_workflow.py"
WRITER = BUNDLE / "scripts" / "write_codex_reports.py"
VALIDATOR = BUNDLE / "scripts" / "validate_complete_report.py"
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"
MEMORY_VALIDATOR = BUNDLE / "scripts" / "validate_role_memory.py"
RUNNER = (
    SKILLS_ROOT
    / "tradingagents-ticker-workflow-runner"
    / "scripts"
    / "prepare_skill_workflow.py"
)

EXPECTED_SKILLS = [
    "tradingagents-aggressive-risk-analyst",
    "tradingagents-analyst-sequencing",
    "tradingagents-bear-researcher",
    "tradingagents-bull-researcher",
    "tradingagents-conservative-risk-analyst",
    "tradingagents-dataflow-routing",
    "tradingagents-debate-routing",
    "tradingagents-financial-report-analyst",
    "tradingagents-fundamentals-analyst",
    "tradingagents-industry-theme-discovery-analyst",
    "tradingagents-market-analyst",
    "tradingagents-neutral-risk-analyst",
    "tradingagents-news-analyst",
    "tradingagents-portfolio-manager",
    "tradingagents-quality-reviewer",
    "tradingagents-research-manager",
    "tradingagents-run-persistence",
    "tradingagents-sentiment-analyst",
    "tradingagents-ticker-workflow-runner",
    "tradingagents-trader",
    "tradingagents-workflow-orchestrator",
]


def _minimal_complete_report(*, action: str = "Hold", final: str = "HOLD") -> str:
    price_framework = (
        "\n**Paper-study price framework**: Reference price 100.00; invalidation 95.00; first target 110.00.\n"
        if final in {"BUY", "SELL"}
        else ""
    )
    return f"""# Trading Analysis Report: AAPL

Generated: 2026-06-27

Context: comparative_run=false

## I. Analyst Team Reports

### Market Analyst

### Sentiment Analyst

### News Analyst

### Fundamentals Analyst

### Financial Report Analyst

### Industry / Theme Discovery Analyst

## II. Research Team Debate

### Bull Researcher Round 1 - Opening Case

### Bear Researcher Round 1 - Rebuttal to Bull

### Research Manager Decision - Evidence Weighing

**Recommendation**: Hold

**Primary driver of rating:** mixed

## III. Trading Team Plan

### Trader Proposal

**Action**: {action}
{price_framework}

FINAL TRANSACTION PROPOSAL: **{final}**

## IV. Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

### Conservative Risk Analyst Round 1 - Response to Aggressive

### Neutral Risk Analyst Round 1 - Weighing

## V. Portfolio Manager Decision

### Portfolio Manager

**Rating**: Hold

## VI. Paper-Study Disclaimer

Research workflow testing only.
"""


def _write_workflow(tmp_path: Path) -> tuple[Path, dict[str, Path]]:
    output_dir = tmp_path / "run"
    evidence_dir = output_dir / "evidence" / "AAPL" / "2026-06-27"
    market_evidence_dir = evidence_dir / "market"
    news_evidence_dir = evidence_dir / "news"
    report_dir = output_dir / "reports" / "AAPL" / "2026-06-27"
    evidence_dir.mkdir(parents=True)
    market_evidence_dir.mkdir(parents=True)
    news_evidence_dir.mkdir(parents=True)
    report_dir.mkdir(parents=True)
    evidence_path = evidence_dir / "evidence.json"
    market_observations_path = market_evidence_dir / "quantitative_observations.json"
    market_ledger_path = market_evidence_dir / "evidence_ledger.jsonl"
    article_cards_path = news_evidence_dir / "article_cards.json"
    evidence_ledger_path = news_evidence_dir / "evidence_ledger.jsonl"
    financial_evidence_dir = evidence_dir / "financial_report"
    financial_evidence_dir.mkdir(parents=True)
    financial_sections_path = financial_evidence_dir / "section_records.json"
    financial_ledger_path = financial_evidence_dir / "evidence_ledger.jsonl"
    report_paths = {
        "market_report": report_dir / "1_analysts" / "market.md",
        "sentiment_report": report_dir / "1_analysts" / "sentiment.md",
        "news_report": report_dir / "1_analysts" / "news.md",
        "fundamentals_report": report_dir / "1_analysts" / "fundamentals.md",
        "financial_report": report_dir / "1_analysts" / "financial_report.md",
        "industry_theme_report": report_dir / "1_analysts" / "industry_theme.md",
        "bull_researcher_round_1": report_dir / "2_research" / "bull_round_1.md",
        "bear_researcher_round_1": report_dir / "2_research" / "bear_round_1.md",
        "research_manager": report_dir / "2_research" / "manager.md",
        "trader": report_dir / "3_trading" / "trader.md",
        "aggressive_risk_round_1": report_dir / "4_risk" / "aggressive_round_1.md",
        "conservative_risk_round_1": report_dir / "4_risk" / "conservative_round_1.md",
        "neutral_risk_round_1": report_dir / "4_risk" / "neutral_round_1.md",
        "portfolio_manager": report_dir / "5_portfolio" / "decision.md",
        "debate_record": report_dir / "debate_record.md",
        "complete_report": report_dir / "complete_report.md",
        "quality_review": report_dir / "6_quality" / "quality_review.md",
    }
    evidence_path.write_text(
        json.dumps(
            {
                "ticker": "AAPL",
                "trade_date": "2026-06-27",
                "identity": {
                    "company_name": "Apple Inc.",
                    "sector": "Technology",
                    "industry": "Consumer Electronics",
                },
                "roles": {
                    "market": {
                        "tool_calls": {
                            "get_verified_market_snapshot": {
                                "output": "Latest close: 195.64\n10 EMA: 198.12\n50 SMA: 201.33\n200 SMA: 180.50"
                            }
                        }
                    },
                    "news": {
                        "tool_calls": {
                            "get_news": {
                                "output": "### AAPL seeks approval to buy CXMT chips (source: Example)\nCould reduce memory pressure but adds supplier risk."
                            }
                        }
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    market_observations_path.write_text(
        json.dumps(
            [
                {
                    "evidence_id": "market:AAPL:2026-06-27:001",
                    "ticker": "AAPL",
                    "trade_date": "2026-06-27",
                    "metric_name": "latest_close",
                    "status": "available",
                    "value": 195.64,
                    "supports_claims": ["latest close", "price level"],
                    "confidence": "medium",
                    "final_market_judgment": "pending_codex_interpretation",
                },
                {
                    "evidence_id": "market:AAPL:2026-06-27:002",
                    "ticker": "AAPL",
                    "trade_date": "2026-06-27",
                    "metric_name": "latest_close_vs_sma_200",
                    "status": "available",
                    "relation": "above",
                    "comparison": {
                        "left_metric": "latest_close",
                        "left_value": 195.64,
                        "right_metric": "sma_200",
                        "right_value": 180.50,
                    },
                    "supports_claims": ["price relative to 200 SMA", "long-term trend support/resistance"],
                    "confidence": "medium",
                    "final_market_judgment": "pending_codex_interpretation",
                },
            ]
        ),
        encoding="utf-8",
    )
    market_ledger_path.write_text(
        json.dumps(
            {
                "evidence_id": "market:AAPL:2026-06-27:001",
                "ticker": "AAPL",
                "trade_date": "2026-06-27",
                "role": "market_analyst",
                "tool_name": "market_data_evidence",
                "tool_version": "0.1.0",
                "source_url": "local://tool/get_verified_market_snapshot",
                "source_date": "2026-06-27",
                "retrieval_time": "2026-06-27T09:30:00+10:00",
                "as_of_validity": {
                    "valid_for_trade_date": True,
                    "reason": "source_date is on or before trade_date",
                },
                "confidence": "medium",
                "limitations": [],
                "structured_output_path": str(market_observations_path),
                "report_sections_using_it": ["Quantitative Regime / Tool Outputs"],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    article_cards_path.write_text(
        json.dumps(
            [
                {
                    "evidence_id": "news:AAPL:2026-06-27:001",
                    "title": "AAPL seeks approval to buy CXMT chips",
                    "source_url": "https://example.com/aapl-cxmt",
                    "source_date": "2026-06-26",
                    "full_text_status": "snippet_only",
                    "confidence": "low",
                }
            ]
        ),
        encoding="utf-8",
    )
    evidence_ledger_path.write_text(
        json.dumps(
            {
                "evidence_id": "news:AAPL:2026-06-27:001",
                "ticker": "AAPL",
                "trade_date": "2026-06-27",
                "role": "news_analyst",
                "tool_name": "news_article_evidence",
                "tool_version": "0.1.0",
                "source_url": "https://example.com/aapl-cxmt",
                "source_date": "2026-06-26",
                "retrieval_time": "2026-06-27T09:30:00+10:00",
                "as_of_validity": {
                    "valid_for_trade_date": True,
                    "reason": "source_date is on or before trade_date",
                },
                "confidence": "low",
                "limitations": ["snippet_only"],
                "structured_output_path": str(article_cards_path),
                "report_sections_using_it": ["News Analyst"],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    financial_sections_path.write_text(
        json.dumps(
            [
                {
                    "evidence_id": "financial:AAPL:2026-06-27:001",
                    "source_type": "annual_report_10k",
                    "section_name": "10-K business overview",
                    "section_kind": "business_overview",
                    "status": "available",
                    "filing_date": "2025-07-30",
                    "url": "https://example.com/aapl-10k",
                    "excerpt": "Business overview.",
                    "supports_claims": ["business model"],
                    "evidence_gap": "",
                    "confidence": "medium",
                }
            ]
        ),
        encoding="utf-8",
    )
    financial_ledger_path.write_text(
        json.dumps(
            {
                "evidence_id": "financial:AAPL:2026-06-27:001",
                "ticker": "AAPL",
                "trade_date": "2026-06-27",
                "role": "financial_report_analyst",
                "tool_name": "financial_document_evidence",
                "tool_version": "0.1.0",
                "source_url": "https://example.com/aapl-10k",
                "source_date": "2025-07-30",
                "retrieval_time": "2026-06-27T09:30:00+10:00",
                "as_of_validity": {
                    "valid_for_trade_date": True,
                    "reason": "source_date is on or before trade_date",
                },
                "confidence": "medium",
                "limitations": [],
                "structured_output_path": str(financial_sections_path),
                "report_sections_using_it": ["Financial Report Analyst"],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    for path in report_paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Pending Codex role output.\n", encoding="utf-8")
    memory_root = output_dir / "memory" / "AAPL"
    news_memory = memory_root / "news_analyst"
    market_memory = memory_root / "market_analyst"
    news_memory.mkdir(parents=True)
    market_memory.mkdir(parents=True)
    (market_memory / "memory.md").write_text("# market memory\n", encoding="utf-8")
    (market_memory / "memory.json").write_text('{"role": "market_analyst", "ticker": "AAPL"}\n', encoding="utf-8")
    (news_memory / "memory.md").write_text("# news memory\n", encoding="utf-8")
    (news_memory / "memory.json").write_text('{"role": "news_analyst", "ticker": "AAPL"}\n', encoding="utf-8")
    workflow = {
        "ticker": "AAPL",
        "trade_date": "2026-06-27",
        "evidence_path": str(evidence_path),
        "report_dir": str(report_dir),
        "report_paths": {key: str(path) for key, path in report_paths.items()},
        "memory_root": str(memory_root),
        "stages": [
            {
                "stage": "market_analyst",
                "skill": "tradingagents-market-analyst",
                "allowed_inputs": [
                    str(evidence_path),
                    str(market_observations_path),
                    str(market_ledger_path),
                ],
                "forbidden_inputs": [],
                "allowed_memory_files": [
                    str(market_memory / "memory.md"),
                    str(market_memory / "memory.json"),
                ],
                "forbidden_memory_roots": [str(news_memory)],
                "output_path": str(report_paths["market_report"]),
                "memory_update_path": str(report_dir / "memory_updates" / "market_analyst.md"),
                "role_execution_contract": {
                    "role": "market_analyst",
                    "allowed_inputs": [
                        str(evidence_path),
                        str(market_observations_path),
                        str(market_ledger_path),
                    ],
                    "forbidden_inputs": ["future_prices", "uncited_memory"],
                    "allowed_memory": [str(market_memory / "memory.md")],
                    "forbidden_memory": ["other_role_memory"],
                    "required_tools": ["get_verified_market_snapshot", "market_data_evidence"],
                    "optional_tools": ["market_calendar_check"],
                    "required_output_sections": [
                        "Tool Outputs Used",
                        "Quantitative Regime / Tool Outputs",
                        "Evidence Gaps",
                    ],
                    "required_evidence_citations": [
                        "evidence_id",
                        "metric_name",
                        "value",
                        "relation",
                    ],
                    "quality_gate": "market_metric_consistency_gate",
                    "memory_update_schema": {"evidence_references": ["evidence_id"]},
                },
            },
            {
                "stage": "news_analyst",
                "skill": "tradingagents-news-analyst",
                "allowed_inputs": [
                    str(evidence_path),
                    str(article_cards_path),
                    str(evidence_ledger_path),
                ],
                "forbidden_inputs": [],
                "allowed_memory_files": [
                    str(news_memory / "memory.md"),
                    str(news_memory / "memory.json"),
                ],
                "forbidden_memory_roots": [str(market_memory)],
                "output_path": str(report_paths["news_report"]),
                "memory_update_path": str(report_dir / "memory_updates" / "news_analyst.md"),
                "role_execution_contract": {
                    "role": "news_analyst",
                    "allowed_inputs": [
                        str(evidence_path),
                        str(article_cards_path),
                        str(evidence_ledger_path),
                    ],
                    "forbidden_inputs": ["future_articles", "uncited_memory"],
                    "allowed_memory": [str(news_memory / "memory.md")],
                    "forbidden_memory": ["other_role_memory"],
                    "required_tools": ["candidate_news_search", "news_article_evidence"],
                    "optional_tools": ["browser_full_text_check"],
                    "required_output_sections": [
                        "Tool Outputs Used",
                        "Article Evidence Cards",
                        "News Impact Summary",
                        "Evidence Gaps",
                    ],
                    "required_evidence_citations": [
                        "evidence_id",
                        "source_url",
                        "source_date",
                        "full_text_status",
                    ],
                    "quality_gate": "news_analyst_quality_gate",
                    "memory_update_schema": {"evidence_references": ["evidence_id"]},
                },
            }
            ,
            {
                "stage": "financial_report_analyst",
                "skill": "tradingagents-financial-report-analyst",
                "allowed_inputs": [
                    str(report_paths["market_report"]),
                    str(report_paths["news_report"]),
                    str(evidence_path),
                    str(financial_sections_path),
                    str(financial_ledger_path),
                ],
                "forbidden_inputs": [],
                "allowed_memory_files": [
                    str(news_memory / "memory.md"),
                    str(news_memory / "memory.json"),
                ],
                "forbidden_memory_roots": [str(market_memory)],
                "output_path": str(report_paths["financial_report"]),
                "memory_update_path": str(report_dir / "memory_updates" / "financial_report_analyst.md"),
                "role_execution_contract": {
                    "role": "financial_report_analyst",
                    "allowed_inputs": [
                        str(evidence_path),
                        str(financial_sections_path),
                        str(financial_ledger_path),
                    ],
                    "forbidden_inputs": ["future_filings", "uncited_memory"],
                    "allowed_memory": [str(news_memory / "memory.md")],
                    "forbidden_memory": ["other_role_memory"],
                    "required_tools": ["collect_financial_document_sources", "financial_document_evidence"],
                    "optional_tools": ["sec_filing_lookup", "asx_announcement_lookup"],
                    "required_output_sections": [
                        "Tool Outputs Used",
                        "Source coverage table",
                        "Claim-Source Table",
                        "Evidence gaps",
                    ],
                    "required_evidence_citations": [
                        "evidence_id",
                        "source_type",
                        "section_name",
                        "filing_date",
                        "evidence_gap",
                    ],
                    "quality_gate": "financial_report_claim_source_gate",
                    "memory_update_schema": {"evidence_references": ["evidence_id"]},
                },
            },
        ],
    }
    for stage_name, skill, output_key, role_name, required_sections in [
        (
            "industry_theme_discovery_analyst",
            "tradingagents-industry-theme-discovery-analyst",
            "industry_theme_report",
            "industry_theme_discovery_analyst",
            ["Tool Outputs Used", "Theme Evidence Table"],
        ),
        (
            "bull_researcher_round_1",
            "tradingagents-bull-researcher",
            "bull_researcher_round_1",
            "bull_researcher",
            ["Tool Outputs Used", "Strongest Bull Evidence", "Falsification Conditions"],
        ),
        (
            "bear_researcher_round_1",
            "tradingagents-bear-researcher",
            "bear_researcher_round_1",
            "bear_researcher",
            ["Tool Outputs Used", "Strongest Bear Evidence", "Falsification Conditions", "Response To Bull"],
        ),
        (
            "research_manager",
            "tradingagents-research-manager",
            "research_manager",
            "research_manager",
            ["Tool Outputs Used", "Structured Evidence Matrix"],
        ),
        (
            "trader",
            "tradingagents-trader",
            "trader",
            "trader",
            ["Tool Outputs Used", "Action Consistency Check", "Paper-study price framework"],
        ),
        (
            "aggressive_risk_round_1",
            "tradingagents-aggressive-risk-analyst",
            "aggressive_risk_round_1",
            "aggressive_risk_analyst",
            ["Tool Outputs Used", "Opportunity Case", "Failure Points"],
        ),
        (
            "conservative_risk_round_1",
            "tradingagents-conservative-risk-analyst",
            "conservative_risk_round_1",
            "conservative_risk_analyst",
            ["Tool Outputs Used", "Downside Case", "Unsupported Upside Challenges"],
        ),
        (
            "neutral_risk_round_1",
            "tradingagents-neutral-risk-analyst",
            "neutral_risk_round_1",
            "neutral_risk_analyst",
            ["Tool Outputs Used", "Risk Argument Quality", "Stronger Risk Side"],
        ),
        (
            "portfolio_manager",
            "tradingagents-portfolio-manager",
            "portfolio_manager",
            "portfolio_manager",
            ["Tool Outputs Used", "Risk debate impact", "Final Portfolio Decision"],
        ),
        (
            "complete_report",
            "tradingagents-run-persistence",
            "complete_report",
            "complete_report",
            ["Tool Outputs Used", "Complete Report"],
        ),
        (
            "quality_review",
            "tradingagents-quality-reviewer",
            "quality_review",
            "quality_reviewer",
            ["Tool Outputs Used", "Quality Gate Findings"],
        ),
    ]:
        workflow["stages"].append(
            {
                "stage": stage_name,
                "skill": skill,
                "allowed_inputs": [str(evidence_path), str(report_paths["market_report"]), str(report_paths["news_report"])],
                "forbidden_inputs": [],
                "allowed_memory_files": [
                    str(market_memory / "memory.md"),
                    str(market_memory / "memory.json"),
                ],
                "forbidden_memory_roots": [str(news_memory)],
                "output_path": str(report_paths[output_key]),
                "memory_update_path": str(report_dir / "memory_updates" / f"{stage_name}.md"),
                "role_execution_contract": {
                    "role": role_name,
                    "allowed_inputs": [str(evidence_path), str(report_paths["market_report"]), str(report_paths["news_report"])],
                    "forbidden_inputs": ["uncited_memory"],
                    "allowed_memory": [str(market_memory / "memory.md")],
                    "forbidden_memory": ["other_role_memory"],
                    "required_tools": ["stage_input_evidence"],
                    "optional_tools": [],
                    "required_output_sections": required_sections,
                    "required_evidence_citations": ["evidence_id"],
                    "quality_gate": f"{role_name}_gate",
                    "memory_update_schema": {"evidence_references": ["evidence_id"]},
                },
            }
        )
    (evidence_dir / "workflow_state.json").write_text(
        json.dumps(workflow),
        encoding="utf-8",
    )
    return output_dir, report_paths


def test_bundle_has_expected_skills_and_docs():
    assert (BUNDLE / "README.md").exists()
    assert (BUNDLE / "MANIFEST.md").exists()
    assert (BUNDLE / "scripts" / "collect_role_evidence.py").exists()
    assert PREPARER.exists()
    assert CODEX_WORKFLOW_RUNNER.exists()
    assert WRITER.exists()
    assert VALIDATOR.exists()
    assert QUALITY_VALIDATOR.exists()
    assert MEMORY_VALIDATOR.exists()

    readme = (BUNDLE / "README.md").read_text(encoding="utf-8")
    manifest = (BUNDLE / "MANIFEST.md").read_text(encoding="utf-8")
    assert "prepare_codex_report_tasks.py" in readme
    assert "financial_document_sources.py" in readme
    assert "write_codex_reports.py is a compatibility wrapper" in readme
    assert "prepare_codex_report_tasks.py" in manifest
    assert "financial_document_sources.py" in manifest
    assert "tradingagents-financial-report-analyst" in manifest
    assert "tradingagents-industry-theme-discovery-analyst" in manifest
    assert "tradingagents-quality-reviewer" in manifest

    actual = sorted(path.name for path in SKILLS_ROOT.glob("tradingagents-*") if path.is_dir())
    assert actual == sorted(EXPECTED_SKILLS)

    for skill in EXPECTED_SKILLS:
        text = (SKILLS_ROOT / skill / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert "description: Use when" in text
        assert "Do not use as real trading advice." in text
        assert "Do not connect to GCAF." in text


def test_bundle_runner_accepts_cli_tickers():
    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--ticker",
            "AAPL,MSFT",
            "--trade-date",
            "2026-06-27",
            "--format",
            "json",
        ],
        cwd=BUNDLE,
        text=True,
        capture_output=True,
        check=True,
    )

    payload = json.loads(result.stdout)
    assert [run["ticker"] for run in payload["runs"]] == ["AAPL", "MSFT"]
    assert "tradingagents-financial-report-analyst" in payload["role_skills"]
    assert "tradingagents-industry-theme-discovery-analyst" in payload["role_skills"]
    assert "tradingagents-quality-reviewer" in payload["workflow_skills"]


def test_prepare_codex_report_tasks_writes_task_prompts_not_reports(tmp_path: Path):
    output_dir, report_paths = _write_workflow(tmp_path)

    result = subprocess.run(
        [
            sys.executable,
            str(PREPARER),
            "--output-dir",
            str(output_dir),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    task_dir = output_dir / "reports" / "AAPL" / "2026-06-27" / "tasks"
    manifest = json.loads((task_dir / "task_manifest.json").read_text(encoding="utf-8"))
    news_task = (task_dir / "news_analyst_task.md").read_text(encoding="utf-8")
    market_task = (task_dir / "market_analyst_task.md").read_text(encoding="utf-8")
    fundamentals_task = (task_dir / "fundamentals_analyst_task.md").read_text(encoding="utf-8")
    financial_task = (task_dir / "financial_report_task.md").read_text(encoding="utf-8")
    theme_task = (task_dir / "industry_theme_discovery_task.md").read_text(encoding="utf-8")
    bull_task = (task_dir / "bull_researcher_round_1_task.md").read_text(encoding="utf-8")
    bear_task = (task_dir / "bear_researcher_round_1_task.md").read_text(encoding="utf-8")
    research_task = (task_dir / "research_manager_task.md").read_text(encoding="utf-8")
    trader_task = (task_dir / "trader_task.md").read_text(encoding="utf-8")
    aggressive_task = (task_dir / "aggressive_risk_round_1_task.md").read_text(encoding="utf-8")
    conservative_task = (task_dir / "conservative_risk_round_1_task.md").read_text(encoding="utf-8")
    neutral_task = (task_dir / "neutral_risk_round_1_task.md").read_text(encoding="utf-8")
    portfolio_task = (task_dir / "portfolio_manager_task.md").read_text(encoding="utf-8")
    quality_task = (task_dir / "quality_reviewer_task.md").read_text(encoding="utf-8")

    assert "AAPL: prepared Codex report tasks" in result.stdout
    assert manifest["ticker"] == "AAPL"
    assert "news_analyst_task.md" in manifest["tasks"]
    assert manifest["tasks"]["news_analyst_task.md"]["stage"] == "news_analyst"
    assert manifest["tasks"]["news_analyst_task.md"]["output_path"].replace("\\", "/").endswith("1_analysts/news.md")
    assert manifest["tasks"]["financial_report_task.md"]["dependency_inputs"]
    assert "required_output_sections" in manifest["tasks"]["market_analyst_task.md"]
    assert "financial_report_task.md" in manifest["tasks"]
    assert "industry_theme_discovery_task.md" in manifest["tasks"]
    assert "bull_researcher_round_1_task.md" in manifest["tasks"]
    assert "bear_researcher_round_1_task.md" in manifest["tasks"]
    assert "aggressive_risk_round_1_task.md" in manifest["tasks"]
    assert "Codex must write" in news_task
    assert "## Required Tool-Using Expert Workflow" in news_task
    assert "## Tool Outputs Used" in news_task
    assert "## Article Evidence Cards" in news_task
    assert "Do not let Python classify likely effect" in news_task
    assert "## RoleExecutionContract" in news_task
    assert "article_cards.json" in news_task
    assert "evidence_ledger.jsonl" in news_task
    assert "Python candidate fields are not final investment judgments" in news_task
    assert "Do not assign final impact labels without citing article evidence IDs" in news_task
    assert "## Allowed Memory Files" in news_task
    assert "## Forbidden Memory Roots" in news_task
    assert "## Memory Update" in news_task
    assert "## Quantitative Regime / Tool Outputs" in market_task
    assert "## RoleExecutionContract" in market_task
    assert "quantitative_observations.json" in market_task
    assert "evidence_ledger.jsonl" in market_task
    assert "Python metric observations are not final technical judgments" in market_task
    assert "Do not make price-versus-moving-average claims without metric evidence IDs" in market_task
    assert "## Tool Outputs Used" in fundamentals_task
    assert "sector-specific metrics" in fundamentals_task
    assert "## Structured Evidence Matrix" in research_task
    assert manifest["tasks"]["news_analyst_task.md"]["allowed_memory_files"]
    assert "tradingagents-financial-report-analyst" in financial_task
    assert "## Claim-Source Table" in financial_task
    assert "## RoleExecutionContract" in financial_task
    assert "section_records.json" in financial_task
    assert "evidence_ledger.jsonl" in financial_task
    assert "Python section records are not final financial judgments" in financial_task
    assert "Do not make major financial claims without section evidence IDs or explicit evidence gaps" in financial_task
    assert "If online sources or filings are unavailable, state the evidence gap." in financial_task
    assert "tradingagents-industry-theme-discovery-analyst" in theme_task
    assert "## RoleExecutionContract" in theme_task
    assert "Python must not classify themes or financial-report conclusions." in theme_task
    assert "## Strongest Bull Evidence" in bull_task
    assert "## RoleExecutionContract" in bull_task
    assert "## Strongest Bear Evidence" in bear_task
    assert "## Response To Bull" in bear_task
    assert "quality_gate.json" in quality_task
    assert "## RoleExecutionContract" in research_task
    assert "## Action Consistency Check" in trader_task
    assert "FINAL TRANSACTION PROPOSAL" in trader_task
    assert "## Opportunity Case" in aggressive_task
    assert "## Unsupported Upside Challenges" in conservative_task
    assert "## Risk Argument Quality" in neutral_task
    assert "## Risk debate impact" in portfolio_task
    assert "ASX reports are not complete when ASX source collection fails" in quality_task
    assert report_paths["news_report"].read_text(encoding="utf-8") == "Pending Codex role output.\n"
    assert report_paths["complete_report"].read_text(encoding="utf-8") == "Pending Codex role output.\n"


def test_write_codex_reports_is_task_preparation_compatibility_wrapper(tmp_path: Path):
    output_dir, report_paths = _write_workflow(tmp_path)

    subprocess.run(
        [
            sys.executable,
            str(WRITER),
            "--output-dir",
            str(output_dir),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    task_dir = output_dir / "reports" / "AAPL" / "2026-06-27" / "tasks"
    assert (task_dir / "research_manager_task.md").exists()
    assert report_paths["research_manager"].read_text(encoding="utf-8") == "Pending Codex role output.\n"


def test_codex_role_workflow_runner_reports_next_stage_and_blockers(tmp_path: Path):
    output_dir, _report_paths = _write_workflow(tmp_path)
    subprocess.run([sys.executable, str(PREPARER), "--output-dir", str(output_dir)], check=True)

    result = subprocess.run(
        [
            sys.executable,
            str(CODEX_WORKFLOW_RUNNER),
            "--output-dir",
            str(output_dir),
            "--format",
            "json",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    payload = json.loads(result.stdout)
    run = payload["runs"][0]
    assert run["next_stage"]["stage"] == "market_analyst"
    assert run["next_stage"]["task_path"].endswith("market_analyst_task.md")
    statuses = {stage["stage"]: stage for stage in run["stages"]}
    assert statuses["market_analyst"]["status"] == "pending"
    assert statuses["financial_report_analyst"]["status"] == "blocked"
    assert "market.md" in " ".join(statuses["financial_report_analyst"]["blocking_dependencies"])
    assert "news.md" in " ".join(statuses["financial_report_analyst"]["blocking_dependencies"])


def test_codex_role_workflow_runner_resumes_after_completed_stage(tmp_path: Path):
    output_dir, report_paths = _write_workflow(tmp_path)
    subprocess.run([sys.executable, str(PREPARER), "--output-dir", str(output_dir)], check=True)
    report_paths["market_report"].write_text(
        """# Market Analyst

## Tool Outputs Used

- market:AAPL:2026-06-27:001 from quantitative_observations.json.

## Quantitative Regime / Tool Outputs

Latest close: 195.64. 200 SMA: 180.50. Price is above the 200 SMA.

## Evidence Gaps

No intraday confirmation evidence.

## Memory Update

* Durable facts to retain: AAPL market evidence market:AAPL:2026-06-27:001 was used.
* Prior mistake to avoid: Do not invert price versus moving-average relations.
* Open questions: None.
* Evidence references: market:AAPL:2026-06-27:001
* Staleness / expiry: Expires after 2026-06-27.
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(CODEX_WORKFLOW_RUNNER),
            "--output-dir",
            str(output_dir),
            "--format",
            "json",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    payload = json.loads(result.stdout)
    run = payload["runs"][0]
    assert run["next_stage"]["stage"] == "news_analyst"
    statuses = {stage["stage"]: stage for stage in run["stages"]}
    assert statuses["market_analyst"]["status"] == "complete"


def test_codex_role_workflow_runner_flags_invalid_completed_output(tmp_path: Path):
    output_dir, report_paths = _write_workflow(tmp_path)
    subprocess.run([sys.executable, str(PREPARER), "--output-dir", str(output_dir)], check=True)
    report_paths["market_report"].write_text(
        """# Market Analyst

## Tool Outputs Used

- market:AAPL:2026-06-27:001.

## Memory Update

* Durable facts to retain: market:AAPL:2026-06-27:001
* Prior mistake to avoid: None.
* Open questions: None.
* Evidence references: market:AAPL:2026-06-27:001
* Staleness / expiry: Expires after 2026-06-27.
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(CODEX_WORKFLOW_RUNNER),
            "--output-dir",
            str(output_dir),
            "--format",
            "json",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    payload = json.loads(result.stdout)
    run = payload["runs"][0]
    assert run["next_stage"]["stage"] == "market_analyst"
    assert run["next_stage"]["status"] == "invalid"
    assert "missing required section: Quantitative Regime / Tool Outputs" in run["next_stage"]["validation_errors"]


def test_complete_report_validator_accepts_hard_contract_report(tmp_path: Path):
    report = tmp_path / "complete_report.md"
    report.write_text(_minimal_complete_report(), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_complete_report_validator_rejects_raw_social_dump(tmp_path: Path):
    report = tmp_path / "raw_social.md"
    raw_lines = "\n".join(
        f"[2026-06-27T10:0{i}:00Z - @user{i} - no-label] $AAPL repeated social line"
        for i in range(6)
    )
    report.write_text(_minimal_complete_report() + raw_lines, encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "too many raw social examples" in result.stdout


def test_complete_report_validator_rejects_post_date_social_evidence(tmp_path: Path):
    report = tmp_path / "post_date.md"
    report.write_text(
        _minimal_complete_report()
        + "[2026-06-28T00:01:00Z - @late - Bullish] $AAPL look-ahead social line\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "post-date evidence found" in result.stdout


def test_complete_report_validator_rejects_final_proposal_mismatch(tmp_path: Path):
    report = tmp_path / "mismatch.md"
    report.write_text(_minimal_complete_report(action="Hold", final="SELL"), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "final proposal mismatch" in result.stdout


def test_complete_report_validator_rejects_missing_primary_driver(tmp_path: Path):
    report = tmp_path / "missing_primary_driver.md"
    report.write_text(
        _minimal_complete_report().replace("**Primary driver of rating:** mixed\n", ""),
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "missing primary driver" in result.stdout


def test_complete_report_validator_rejects_missing_financial_report_heading(tmp_path: Path):
    report = tmp_path / "missing_financial_report.md"
    report.write_text(
        _minimal_complete_report().replace("### Financial Report Analyst\n\n", ""),
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "### Financial Report Analyst" in result.stdout


def test_complete_report_validator_rejects_missing_industry_theme_discovery_heading(tmp_path: Path):
    report = tmp_path / "missing_industry_theme_discovery.md"
    report.write_text(
        _minimal_complete_report().replace("### Industry / Theme Discovery Analyst\n\n", ""),
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "### Industry / Theme Discovery Analyst" in result.stdout


def _write_quality_fixture(tmp_path: Path, *, include_financial: bool, include_theme: bool) -> Path:
    report_dir = tmp_path / "reports" / "AAPL" / "2026-06-27"
    analyst_dir = report_dir / "1_analysts"
    quality_dir = report_dir / "6_quality"
    analyst_dir.mkdir(parents=True)
    quality_dir.mkdir(parents=True)
    (report_dir / "complete_report.md").write_text(_minimal_complete_report(), encoding="utf-8")
    (quality_dir / "quality_gate.json").write_text('{"passed": true, "issues": []}\n', encoding="utf-8")
    if include_financial:
        (analyst_dir / "financial_report.md").write_text(
            "# Financial Report Analyst\n\n## Source coverage table\n\n| Source | Status |\n|---|---|\n| Fundamentals packet | available |\n",
            encoding="utf-8",
        )
    if include_theme:
        (analyst_dir / "industry_theme.md").write_text(
            "| Theme | Subtheme | Evidence link | Classification | Reason | Confidence |\n"
            "|---|---|---|---|---|---|\n"
            "| memory supply chain | component cost | news.md | mixed | supported by report source | medium |\n",
            encoding="utf-8",
        )
    return report_dir


def test_quality_validator_fails_when_financial_report_is_missing(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=False, include_theme=True)

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "financial_report.md is missing" in result.stdout


def test_quality_validator_fails_when_industry_theme_report_is_missing(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=False)

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "industry_theme.md is missing" in result.stdout


def test_quality_validator_fails_when_role_outputs_lack_expert_tool_sections(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    research_dir = report_dir / "2_research"
    research_dir.mkdir(parents=True)
    (analyst_dir / "market.md").write_text("# Market Analyst\n\nGeneric market view.\n", encoding="utf-8")
    (analyst_dir / "news.md").write_text("# News Analyst\n\nGeneric news view.\n", encoding="utf-8")
    (analyst_dir / "fundamentals.md").write_text("# Fundamentals Analyst\n\nGeneric fundamentals.\n", encoding="utf-8")
    (research_dir / "manager.md").write_text("# Research Manager\n\nGeneric decision.\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "market.md missing required section: Tool Outputs Used" in result.stdout
    assert "market.md missing required section: Quantitative Regime / Tool Outputs" in result.stdout
    assert "news.md missing required section: Article Evidence Cards" in result.stdout
    assert "fundamentals.md missing required section: Tool Outputs Used" in result.stdout
    assert "manager.md missing required section: Structured Evidence Matrix" in result.stdout


def test_quality_validator_fails_when_market_claim_conflicts_with_200_sma(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "market.md").write_text(
        "# Market Analyst\n\n"
        "## Tool Outputs Used\n\n"
        "- market_data_evidence\n\n"
        "## Quantitative Regime / Tool Outputs\n\n"
        "| Metric | Value |\n"
        "|---|---:|\n"
        "| Latest close | 372.97 |\n"
        "| 200 SMA | 446.27 |\n\n"
        "A close above the 200 SMA points to long-term support.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "market moving-average claim conflicts with metric evidence" in result.stdout


def test_quality_validator_fails_when_market_claim_conflicts_with_above_200_sma(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "market.md").write_text(
        "# Market Analyst\n\n"
        "## Tool Outputs Used\n\n"
        "- market_data_evidence\n\n"
        "## Quantitative Regime / Tool Outputs\n\n"
        "| Metric | Value |\n"
        "|---|---:|\n"
        "| Latest close | 500.00 |\n"
        "| 200 SMA | 446.27 |\n\n"
        "The latest close is below the 200 SMA, showing a long-term breakdown.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "market moving-average claim conflicts with metric evidence" in result.stdout


def test_quality_validator_fails_when_market_report_is_pending(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "market.md").write_text("# market_analyst\n\nPending Codex role output.\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "market.md is still pending" in result.stdout


def test_quality_validator_fails_when_news_impact_lacks_article_evidence_citation(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "news.md").write_text(
        "# News Analyst\n\n"
        "## Tool Outputs Used\n\n"
        "- news_article_evidence\n\n"
        "## Article Evidence Cards\n\n"
        "| Evidence ID | Title | Full-text status | Confidence |\n"
        "|---|---|---|---|\n"
        "| news:AAPL:2026-06-27:001 | Apple analyst note | full_text | medium |\n\n"
        "## News Impact Summary\n\n"
        "Overall impact: Positive.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "news impact label lacks article evidence citation" in result.stdout


def test_quality_validator_fails_when_snippet_only_news_is_high_confidence(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "news.md").write_text(
        "# News Analyst\n\n"
        "## Tool Outputs Used\n\n"
        "- news_article_evidence\n\n"
        "## Article Evidence Cards\n\n"
        "| Evidence ID | Title | Full-text status | Confidence |\n"
        "|---|---|---|---|\n"
        "| news:AAPL:2026-06-27:001 | Apple analyst note | snippet_only | high |\n\n"
        "## News Impact Summary\n\n"
        "Overall impact: Mixed based on news:AAPL:2026-06-27:001.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "snippet-only news evidence cannot be high confidence" in result.stdout


def test_quality_validator_fails_when_news_output_is_pending(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "news.md").write_text(
        "# news_analyst\n\nPending Codex role output.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "news.md is still pending" in result.stdout


def test_quality_validator_fails_when_financial_claim_lacks_section_evidence(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    financial = report_dir / "1_analysts" / "financial_report.md"
    financial.write_text(
        "# Financial Report Analyst\n\n"
        "## Tool Outputs Used\n\n"
        "- financial_document_evidence\n\n"
        "## Source coverage table\n\n"
        "| Source | Status |\n|---|---|\n| 10-Q | available |\n\n"
        "## Claim-Source Table\n\n"
        "| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap |\n"
        "|---|---|---|---|---|---|\n"
        "| Revenue increased |  |  | 2026-04-29 | medium |  |\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "financial claim lacks section evidence citation" in result.stdout


def test_quality_validator_fails_when_financial_gap_is_missing_for_unavailable_section(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    financial = report_dir / "1_analysts" / "financial_report.md"
    financial.write_text(
        "# Financial Report Analyst\n\n"
        "## Tool Outputs Used\n\n"
        "- financial_document_evidence\n\n"
        "## Source coverage table\n\n"
        "| Source | Status |\n|---|---|\n| 10-Q | available |\n\n"
        "## Claim-Source Table\n\n"
        "| Claim | Source document | Section / exhibit | Filing date | Confidence | Evidence gap |\n"
        "|---|---|---|---|---|---|\n"
        "| Capex commitments unavailable | 10-Q | unavailable | 2026-04-29 | low |  |\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "financial evidence gap missing for unavailable section" in result.stdout


def test_quality_validator_fails_when_financial_report_is_pending(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    financial = report_dir / "1_analysts" / "financial_report.md"
    financial.write_text("# financial_report_analyst\n\nPending Codex role output.\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "financial_report.md is still pending" in result.stdout


def test_quality_validator_fails_when_sentiment_contains_raw_social_dump(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    raw_lines = "\n".join(f"[2026-06-27T10:0{i}:00Z - @u{i}] $AAPL raw line" for i in range(5))
    (analyst_dir / "sentiment.md").write_text(
        "# Sentiment\n\n## Tool Outputs Used\n\n- social_evidence_processing\n\n"
        "## Social Evidence Processing Rules\n\n"
        "| Source | Items reviewed | Usable ticker-relevant items |\n|---|---:|---:|\n| StockTwits | 5 | 5 |\n\n"
        f"{raw_lines}\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "sentiment report includes raw social feed instead of summary" in result.stdout


def test_quality_validator_fails_when_fundamentals_lacks_statement_citation(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    analyst_dir = report_dir / "1_analysts"
    (analyst_dir / "fundamentals.md").write_text(
        "# Fundamentals\n\n"
        "## Tool Outputs Used\n\n- fundamentals_statement_evidence\n\n"
        "## Financial Statement Evidence\n\nRevenue improved without citation.\n\n"
        "## Sector-Specific Metrics\n\nEvidence gap: no bank-specific metrics extracted.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "fundamentals claim lacks statement evidence citation" in result.stdout


def test_quality_validator_fails_when_research_matrix_missing_required_columns(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    research_dir = report_dir / "2_research"
    research_dir.mkdir(parents=True)
    (research_dir / "manager.md").write_text(
        "# Research Manager\n\n"
        "## Tool Outputs Used\n\n- stage_input_evidence\n\n"
        "## Structured Evidence Matrix\n\n"
        "| Evidence | Confidence |\n|---|---|\n| Market weak | medium |\n\n"
        "**Recommendation**: Sell\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "research evidence matrix missing column: Direction" in result.stdout


def test_quality_validator_fails_when_trader_action_mismatches_final_proposal(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    trading_dir = report_dir / "3_trading"
    trading_dir.mkdir(parents=True)
    (trading_dir / "trader.md").write_text(
        "# Trader\n\n"
        "## Tool Outputs Used\n\n- stage_input_evidence\n\n"
        "## Action Consistency Check\n\nAction: Hold\n\n"
        "## Paper-study price framework\n\nReference price: 100.\n\n"
        "FINAL TRANSACTION PROPOSAL: SELL\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(QUALITY_VALIDATOR), "--report-dir", str(report_dir)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "trader final proposal mismatch" in result.stdout


def test_quality_validator_fails_asx_report_when_asx_source_collection_failed(tmp_path: Path):
    report_dir = _write_quality_fixture(tmp_path, include_financial=True, include_theme=True)
    evidence_dir = tmp_path / "evidence" / "BHP.AX" / "2026-06-27"
    evidence_dir.mkdir(parents=True)
    (evidence_dir / "evidence.json").write_text(
        json.dumps(
            {
                "ticker": "BHP.AX",
                "trade_date": "2026-06-27",
                "roles": {
                    "financial_report": {
                        "tool_calls": {
                            "collect_financial_document_sources": {
                                "status": "error",
                                "output": "| asx_announcements | error |",
                            }
                        }
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    (report_dir / "complete_report.md").write_text(
        _minimal_complete_report().replace("AAPL", "BHP.AX"),
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(QUALITY_VALIDATOR),
            "--report-dir",
            str(report_dir),
            "--evidence",
            str(evidence_dir / "evidence.json"),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "ASX source collection failed; report cannot be marked complete" in result.stdout


def test_news_theme_and_quality_skills_define_llm_reasoning_contracts():
    market = (SKILLS_ROOT / "tradingagents-market-analyst" / "SKILL.md").read_text(encoding="utf-8")
    news = (SKILLS_ROOT / "tradingagents-news-analyst" / "SKILL.md").read_text(encoding="utf-8")
    fundamentals = (SKILLS_ROOT / "tradingagents-fundamentals-analyst" / "SKILL.md").read_text(encoding="utf-8")
    financial = (SKILLS_ROOT / "tradingagents-financial-report-analyst" / "SKILL.md").read_text(encoding="utf-8")
    theme = (SKILLS_ROOT / "tradingagents-industry-theme-discovery-analyst" / "SKILL.md").read_text(encoding="utf-8")
    research = (SKILLS_ROOT / "tradingagents-research-manager" / "SKILL.md").read_text(encoding="utf-8")
    trader = (SKILLS_ROOT / "tradingagents-trader" / "SKILL.md").read_text(encoding="utf-8")
    bull = (SKILLS_ROOT / "tradingagents-bull-researcher" / "SKILL.md").read_text(encoding="utf-8")
    bear = (SKILLS_ROOT / "tradingagents-bear-researcher" / "SKILL.md").read_text(encoding="utf-8")
    aggressive = (SKILLS_ROOT / "tradingagents-aggressive-risk-analyst" / "SKILL.md").read_text(encoding="utf-8")
    conservative = (SKILLS_ROOT / "tradingagents-conservative-risk-analyst" / "SKILL.md").read_text(encoding="utf-8")
    neutral = (SKILLS_ROOT / "tradingagents-neutral-risk-analyst" / "SKILL.md").read_text(encoding="utf-8")
    portfolio = (SKILLS_ROOT / "tradingagents-portfolio-manager" / "SKILL.md").read_text(encoding="utf-8")
    quality = (SKILLS_ROOT / "tradingagents-quality-reviewer" / "SKILL.md").read_text(encoding="utf-8")

    for required in [
        "## Tool Outputs Used",
        "## Quantitative Regime / Tool Outputs",
        "latest close, 10 EMA, 50 SMA, 200 SMA",
        "template claims that conflict with actual data",
        "RoleExecutionContract",
        "evidence_id",
        "Python metric observations are not final technical judgments",
        "Do not make price-versus-moving-average claims without metric evidence IDs",
    ]:
        assert required in market

    for required in [
        "## Tool Outputs Used",
        "## Article Evidence Cards",
        "full-text status",
        "snippet-only",
        "classify each news item using reasoning, not keywords",
        "direct company news, indirect industry/theme context, or irrelevant",
        "What could make the effect ambiguous?",
        "| Event | Relevance | Event type | Likely effect | Reason | Confidence |",
        "political-trading or celebrity-trading",
        "company fundamentals, regulation, price action, or sentiment",
        "RoleExecutionContract",
        "evidence_id",
        "Snippet-only",
        "Python candidate fields are not final investment judgments",
    ]:
        assert required in news

    for required in [
        "Social Evidence Processing Rules",
        "social_summary.json",
        "Do not infer institutional sentiment from StockTwits or Reddit",
    ]:
        assert required in (SKILLS_ROOT / "tradingagents-sentiment-analyst" / "SKILL.md").read_text(encoding="utf-8")

    for required in [
        "## Tool Outputs Used",
        "## Sector-Specific Metrics",
        "sector-specific metrics",
        "banks use NIM, CET1",
        "miners/resources use production, realised price",
    ]:
        assert required in fundamentals

    for required in [
        "## Tool Outputs Used",
        "## Claim-Source Table",
        "latest annual report / 10-K if available",
        "Source coverage table",
        "cite which source section supports each claim",
        "Claim-source table",
        "Claim, Source document, Section / exhibit, Filing date, Confidence, Evidence gap",
        "Mark capex, formal guidance, segment/product detail, income statement, balance sheet, and cash flow claims as evidence gaps",
        "For ASX companies",
        "NIM, CET1, loan growth, arrears, impairment, dividend, ROE",
        "10-K business / risk factors",
        "10-Q MD&A",
        "8-K Exhibit 99.1",
        "management narrative / filing commentary",
        "If annual/quarterly filings or earnings releases are not available",
        "RoleExecutionContract",
        "evidence_id",
        "Python section records are not final financial judgments",
        "Do not make major financial claims without section evidence IDs or explicit evidence gaps",
    ]:
        assert required in financial

    for required in [
        "Discover relevant themes/subthemes from evidence",
        "Do not force-fit preconfigured themes",
        "tailwind, headwind, mixed, irrelevant, or insufficient evidence",
        "state confidence",
        "memory supply chain / app-store regulation / edge AI only when supported",
        "enterprise AI / Azure / data-center power only when supported",
        "## Theme Evidence Table",
        "Do not use preconfigured themes unless the evidence link supports them",
    ]:
        assert required in theme

    for required in [
        "## Tool Outputs Used",
        "## Structured Evidence Matrix",
        "weight, confidence, and evidence gap",
        "why Sell wins over Hold or Underweight",
        "direction, materiality, confidence, tool output, weight, and reason",
    ]:
        assert required in research

    for text, required in [
        (bull, "## Strongest Bull Evidence"),
        (bull, "## Falsification Conditions"),
        (bear, "## Strongest Bear Evidence"),
        (bear, "## Response To Bull"),
        (trader, "## Action Consistency Check"),
        (trader, "Never use broker/order tools"),
        (aggressive, "## Failure Points"),
        (conservative, "## Unsupported Upside Challenges"),
        (neutral, "## Risk Argument Quality"),
        (portfolio, "Risk debate impact"),
    ]:
        assert required in text

    for required in [
        "## Tool Outputs Used",
        "## Quality Gate Findings",
        "Tool Outputs Used",
        "Article Evidence Cards",
        "Structured Evidence Matrix",
        "ASX reports are not complete when ASX source collection fails",
        "complete_report.md",
        "role reports",
        "evidence summary",
        "quality_review.md",
        "quality_gate.json",
        "financial_report.md is missing",
        "industry_theme.md is missing",
        "political-trading or celebrity-trading headlines",
        "company fundamentals, regulation, price action, or sentiment",
        "news impact label lacks article evidence citation",
        "snippet-only news evidence cannot be high confidence",
        "financial claim lacks section evidence citation",
        "financial evidence gap missing for unavailable section",
        "market moving-average claim conflicts with metric evidence",
        "market.md is still pending",
        "research evidence matrix missing direction",
        "trader final proposal mismatch",
        "portfolio decision omits risk debate impact",
        '"passed": false',
    ]:
        assert required in quality
