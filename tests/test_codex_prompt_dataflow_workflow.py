from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".codex" / "skills"
RUNNER = (
    SKILLS_ROOT
    / "tradingagents-ticker-workflow-runner"
    / "scripts"
    / "prepare_skill_workflow.py"
)


ROLE_PROMPT_CONTRACTS = {
    "tradingagents-market-analyst": [
        "Prompt contract:",
        "select up to 8 indicators",
        "call get_stock_data first",
        "call get_verified_market_snapshot before writing the final report",
        "append a Markdown table",
        "Use the configured output language",
    ],
    "tradingagents-sentiment-analyst": [
        "Prompt contract:",
        "pre-fetches Yahoo Finance news, StockTwits, and Reddit",
        "overall_band",
        "overall_score",
        "confidence",
        "narrative",
        "Use the configured output language",
    ],
    "tradingagents-news-analyst": [
        "Prompt contract:",
        "get_news(query, start_date, end_date)",
        "get_global_news(curr_date, look_back_days, limit)",
        "get_macro_indicators(indicator, curr_date, look_back_days)",
        "get_prediction_markets(topic, limit)",
        "append a Markdown table",
    ],
    "tradingagents-fundamentals-analyst": [
        "Prompt contract:",
        "get_fundamentals",
        "get_balance_sheet",
        "get_cashflow",
        "get_income_statement",
        "append a Markdown table",
    ],
    "tradingagents-research-manager": [
        "Prompt contract:",
        "Buy / Overweight / Hold / Underweight / Sell",
        "Reserve Hold",
        "ResearchPlan",
        "**Recommendation**",
        "**Strategic Actions**",
    ],
    "tradingagents-trader": [
        "Prompt contract:",
        "Buy / Hold / Sell",
        "TraderProposal",
        "**Action**",
        "FINAL TRANSACTION PROPOSAL",
    ],
    "tradingagents-portfolio-manager": [
        "Prompt contract:",
        "PortfolioDecision",
        "**Rating**",
        "**Executive Summary**",
        "**Investment Thesis**",
        "Buy / Overweight / Hold / Underweight / Sell",
    ],
}


def test_role_skills_capture_prompt_contracts():
    for skill_name, phrases in ROLE_PROMPT_CONTRACTS.items():
        text = (SKILLS_ROOT / skill_name / "SKILL.md").read_text(encoding="utf-8")
        for phrase in phrases:
            assert phrase in text, f"{phrase!r} missing from {skill_name}"


def test_dataflow_routing_skill_documents_tool_calls_and_vendor_rules():
    text = (
        SKILLS_ROOT
        / "tradingagents-dataflow-routing"
        / "SKILL.md"
    ).read_text(encoding="utf-8")

    for phrase in [
        "Source files scanned:",
        "route_to_vendor",
        "tool_vendors override category data_vendors",
        "explicit vendor list is the fallback chain",
        "NO_DATA_AVAILABLE",
        "DATA_UNAVAILABLE",
        "get_stock_data(symbol, start_date, end_date)",
        "get_indicators(symbol, indicator, curr_date, look_back_days)",
        "get_macro_indicators(indicator, curr_date, look_back_days)",
        "get_prediction_markets(topic, limit)",
        "safe_ticker_component",
        "Do not use as real trading advice.",
        "Do not connect to GCAF.",
    ]:
        assert phrase in text


def test_ticker_workflow_runner_exists_and_documents_user_input():
    skill_text = (
        SKILLS_ROOT
        / "tradingagents-ticker-workflow-runner"
        / "SKILL.md"
    ).read_text(encoding="utf-8")

    for phrase in [
        "Source files scanned:",
        "prepare_skill_workflow.py",
        "--ticker",
        "--tickers-file",
        "--trade-date",
        "selected analysts",
        "Do not run live LLM or market-data calls",
        "Do not use as real trading advice.",
        "Do not connect to GCAF.",
    ]:
        assert phrase in skill_text
    assert RUNNER.exists()


def test_ticker_workflow_runner_accepts_cli_and_file_tickers(tmp_path):
    tickers_file = tmp_path / "tickers.txt"
    tickers_file.write_text("MSFT\n# comment\nBTC-USD, ETH-USD\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--ticker",
            "AAPL,TSLA",
            "--tickers-file",
            str(tickers_file),
            "--trade-date",
            "2026-06-27",
            "--asset-type",
            "auto",
            "--selected-analysts",
            "market,news",
            "--format",
            "json",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )

    payload = json.loads(result.stdout)
    assert [item["ticker"] for item in payload["runs"]] == [
        "AAPL",
        "TSLA",
        "MSFT",
        "BTC-USD",
        "ETH-USD",
    ]
    assert payload["trade_date"] == "2026-06-27"
    assert payload["selected_analysts"] == ["market", "news"]
    assert payload["runs"][3]["asset_type"] == "crypto"
    assert payload["workflow_skills"][0] == "tradingagents-workflow-orchestrator"
    assert "tradingagents-dataflow-routing" in payload["workflow_skills"]
