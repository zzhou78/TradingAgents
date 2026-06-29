from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLLECTOR_PATH = (
    ROOT / "codex_tradingagents_skillkit" / "scripts" / "collect_role_evidence.py"
)
MEMORY_VALIDATOR_PATH = ROOT / "codex_tradingagents_skillkit" / "scripts" / "validate_role_memory.py"


def _load_collector():
    spec = importlib.util.spec_from_file_location("collect_role_evidence", COLLECTOR_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_memory_validator():
    spec = importlib.util.spec_from_file_location("validate_role_memory", MEMORY_VALIDATOR_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_collector_requires_no_live_llm_gate_and_collects_selected_role_data(tmp_path, monkeypatch):
    collector = _load_collector()
    calls = []

    def fake_tool(name):
        def _inner(**kwargs):
            calls.append((name, kwargs))
            return f"{name} evidence for {kwargs}"

        return _inner

    monkeypatch.setattr(collector, "get_stock_data", fake_tool("get_stock_data"))
    monkeypatch.setattr(collector, "get_verified_market_snapshot", fake_tool("get_verified_market_snapshot"))
    monkeypatch.setattr(collector, "get_indicators", fake_tool("get_indicators"))
    monkeypatch.setattr(collector, "get_news", fake_tool("get_news"))
    monkeypatch.setattr(collector, "get_global_news", fake_tool("get_global_news"))
    monkeypatch.setattr(collector, "get_insider_transactions", fake_tool("get_insider_transactions"))
    monkeypatch.setattr(collector, "get_fundamentals", fake_tool("get_fundamentals"))
    monkeypatch.setattr(collector, "get_balance_sheet", fake_tool("get_balance_sheet"))
    monkeypatch.setattr(collector, "get_cashflow", fake_tool("get_cashflow"))
    monkeypatch.setattr(collector, "get_income_statement", fake_tool("get_income_statement"))
    monkeypatch.setattr(
        collector,
        "collect_financial_document_sources",
        lambda ticker, trade_date, **kwargs: {
            "status": "ok",
            "sources": [
                {
                    "source_type": "annual_report_10k",
                    "status": "available",
                    "filing_date": "2025-07-30",
                    "url": "https://www.sec.gov/example",
                    "excerpt": "Annual report excerpt",
                }
            ],
        },
    )
    monkeypatch.setattr(collector, "resolve_instrument_identity", lambda ticker: {"company_name": ticker})

    exit_code = collector.main(
        [
            "--ticker",
            "AAPL,MSFT",
            "--trade-date",
            "2026-06-27",
            "--selected-analysts",
            "market,news",
            "--output-dir",
            str(tmp_path),
        ]
    )

    assert exit_code == 0
    called_tools = [name for name, _ in calls]
    assert "get_stock_data" in called_tools
    assert "get_verified_market_snapshot" in called_tools
    assert "get_indicators" in called_tools
    assert "get_news" in called_tools
    assert "get_global_news" in called_tools
    assert "get_insider_transactions" in called_tools
    assert "get_fundamentals" not in called_tools
    assert "get_balance_sheet" not in called_tools

    summary = json.loads((tmp_path / "evidence_summary.json").read_text(encoding="utf-8"))
    assert [run["ticker"] for run in summary["runs"]] == ["AAPL", "MSFT"]
    assert summary["selected_analysts"] == ["market", "news"]
    assert summary["codex_operated"] is True
    assert summary["uses_tradingagents_graph"] is False
    assert "tradingagents-market-analyst" in summary["skill_context"]["role_skills"]

    for ticker in ["AAPL", "MSFT"]:
        packet = tmp_path / "evidence" / ticker / "2026-06-27" / "role_packets.md"
        market_packet = tmp_path / "evidence" / ticker / "2026-06-27" / "roles" / "market.md"
        news_packet = tmp_path / "evidence" / ticker / "2026-06-27" / "roles" / "news.md"
        financial_packet = tmp_path / "evidence" / ticker / "2026-06-27" / "roles" / "financial_report.md"
        fundamentals_packet = tmp_path / "evidence" / ticker / "2026-06-27" / "roles" / "fundamentals.md"
        data = tmp_path / "evidence" / ticker / "2026-06-27" / "evidence.json"
        assert packet.exists()
        assert market_packet.exists()
        assert news_packet.exists()
        assert financial_packet.exists()
        assert not fundamentals_packet.exists()
        assert data.exists()
        assert "## Role: market" in market_packet.read_text(encoding="utf-8")
        assert "## Role: news" in news_packet.read_text(encoding="utf-8")
        assert "annual_report_10k" in financial_packet.read_text(encoding="utf-8")
        assert "## Role: news" not in market_packet.read_text(encoding="utf-8")

    for run in summary["runs"]:
        assert sorted(run["role_packet_paths"]) == ["financial_report", "market", "news"]
        assert run["role_packet_path"].endswith("role_packets.md")
        assert run["workflow_state_path"].endswith("workflow_state.json")
        assert run["debate_record_path"].endswith("debate_record.md")

        workflow = json.loads(Path(run["workflow_state_path"]).read_text(encoding="utf-8"))
        assert workflow["requires_user_input"] is False
        assert workflow["uses_tradingagents_graph"] is False
        assert workflow["report_style"] == "tradingagents"
        memory_root = Path(workflow["memory_root"])
        for role_name in collector.ROLE_MEMORY_NAMES:
            assert (memory_root / role_name / "memory.md").exists()
            assert (memory_root / role_name / "memory.json").exists()
        stage_names = [stage["stage"] for stage in workflow["stages"]]
        assert stage_names[:2] == ["market_analyst", "news_analyst"]
        assert stage_names[2:] == [
            "financial_report_analyst",
            "industry_theme_discovery_analyst",
            "bull_researcher_round_1",
            "bear_researcher_round_1",
            "research_manager",
            "trader",
            "aggressive_risk_round_1",
            "conservative_risk_round_1",
            "neutral_risk_round_1",
            "portfolio_manager",
            "complete_report",
            "quality_review",
        ]
        assert stage_names[-2:] == ["complete_report", "quality_review"]

        market_stage = workflow["stages"][0]
        assert market_stage["skill"] == "tradingagents-market-analyst"
        assert market_stage["allowed_inputs"] == [run["role_packet_paths"]["market"]]
        assert market_stage["role_memory"] == "market_analyst"
        assert len(market_stage["allowed_memory_files"]) == 2
        assert market_stage["memory_update_path"].endswith("memory_updates\\market_analyst.md") or market_stage[
            "memory_update_path"
        ].endswith("memory_updates/market_analyst.md")
        assert market_stage["forbidden_memory_roots"]
        assert market_stage["forbidden_inputs"] == [
            run["role_packet_paths"]["news"],
            run["role_packet_paths"]["financial_report"],
        ]
        financial_stage = workflow["stages"][2]
        assert run["role_packet_paths"]["financial_report"] in financial_stage["allowed_inputs"]

        report_paths = workflow["report_paths"]
        normalized_market_report = report_paths["market_report"].replace("\\", "/")
        normalized_bull_round = report_paths["bull_researcher_round_1"].replace("\\", "/")
        normalized_bear_round = report_paths["bear_researcher_round_1"].replace("\\", "/")
        normalized_aggressive_round = report_paths["aggressive_risk_round_1"].replace("\\", "/")
        normalized_debate_record = report_paths["debate_record"].replace("\\", "/")
        normalized_complete_report = report_paths["complete_report"].replace("\\", "/")
        ticker = run["ticker"]
        assert normalized_market_report.endswith(f"reports/{ticker}/2026-06-27/1_analysts/market.md")
        assert normalized_bull_round.endswith(f"reports/{ticker}/2026-06-27/2_research/bull_round_1.md")
        assert normalized_bear_round.endswith(f"reports/{ticker}/2026-06-27/2_research/bear_round_1.md")
        assert normalized_aggressive_round.endswith(
            f"reports/{ticker}/2026-06-27/4_risk/aggressive_round_1.md"
        )
        assert normalized_debate_record.endswith(f"reports/{ticker}/2026-06-27/debate_record.md")
        assert normalized_complete_report.endswith(f"reports/{ticker}/2026-06-27/complete_report.md")
        assert run["debate_record_path"] == report_paths["debate_record"]
        debate_record = Path(run["debate_record_path"]).read_text(encoding="utf-8")
        assert "# TradingAgents Debate Record" in debate_record
        assert "## Research Team Debate" in debate_record
        assert "bull_researcher_round_1" in debate_record
        assert "bear_researcher_round_1" in debate_record
        assert "## Risk Management Team Debate" in debate_record
        assert "aggressive_risk_round_1" in debate_record
        assert "conservative_risk_round_1" in debate_record
        assert "neutral_risk_round_1" in debate_record
        for report_key in [
            "market_report",
            "news_report",
            "financial_report",
            "industry_theme_report",
            "bull_researcher_round_1",
            "bear_researcher_round_1",
            "research_manager",
            "trader",
            "aggressive_risk_round_1",
            "conservative_risk_round_1",
            "neutral_risk_round_1",
            "portfolio_manager",
            "complete_report",
            "quality_review",
        ]:
            report_path = Path(report_paths[report_key])
            assert report_path.exists(), report_key
            assert "Pending Codex role output" in report_path.read_text(encoding="utf-8")

        stages_by_name = {stage["stage"]: stage for stage in workflow["stages"]}
        assert stages_by_name["bull_researcher_round_1"]["allowed_inputs"] == [
            report_paths["market_report"],
            report_paths["news_report"],
            report_paths["financial_report"],
            report_paths["industry_theme_report"],
        ]
        assert stages_by_name["bear_researcher_round_1"]["allowed_inputs"] == [
            report_paths["market_report"],
            report_paths["news_report"],
            report_paths["financial_report"],
            report_paths["industry_theme_report"],
            report_paths["bull_researcher_round_1"],
        ]
        assert stages_by_name["research_manager"]["allowed_inputs"] == [
            report_paths["market_report"],
            report_paths["news_report"],
            report_paths["financial_report"],
            report_paths["industry_theme_report"],
            report_paths["bull_researcher_round_1"],
            report_paths["bear_researcher_round_1"],
        ]
        assert report_paths["aggressive_risk_round_1"] in stages_by_name[
            "conservative_risk_round_1"
        ]["allowed_inputs"]
        assert report_paths["conservative_risk_round_1"] in stages_by_name[
            "neutral_risk_round_1"
        ]["allowed_inputs"]
        assert report_paths["neutral_risk_round_1"] in stages_by_name[
            "portfolio_manager"
        ]["allowed_inputs"]
        complete_stage = stages_by_name["complete_report"]
        assert report_paths["market_report"] in complete_stage["allowed_inputs"]
        assert report_paths["news_report"] in complete_stage["allowed_inputs"]
        assert report_paths["portfolio_manager"] in complete_stage["allowed_inputs"]
        quality_stage = workflow["stages"][-1]
        assert quality_stage["stage"] == "quality_review"
        assert report_paths["complete_report"] in quality_stage["allowed_inputs"]

    validation = subprocess.run(
        [sys.executable, str(MEMORY_VALIDATOR_PATH), "--output-dir", str(tmp_path)],
        text=True,
        capture_output=True,
    )
    assert validation.returncode == 0, validation.stdout + validation.stderr


def test_social_role_collects_direct_stocktwits_and_reddit_not_news(tmp_path, monkeypatch):
    collector = _load_collector()
    calls = []

    def fake_tool(name):
        def _inner(**kwargs):
            calls.append((name, kwargs))
            return f"{name} evidence"

        return _inner

    monkeypatch.setattr(collector, "fetch_stocktwits_messages", fake_tool("fetch_stocktwits_messages"))
    monkeypatch.setattr(collector, "fetch_reddit_posts", fake_tool("fetch_reddit_posts"))
    monkeypatch.setattr(collector, "get_news", fake_tool("get_news"))
    monkeypatch.setattr(
        collector,
        "collect_financial_document_sources",
        lambda ticker, trade_date, **kwargs: {"status": "unavailable", "sources": []},
    )
    monkeypatch.setattr(collector, "resolve_instrument_identity", lambda ticker: {"company_name": ticker})

    exit_code = collector.main(
        [
            "--ticker",
            "AAPL",
            "--trade-date",
            "2026-06-27",
            "--selected-analysts",
            "social",
            "--output-dir",
            str(tmp_path),
        ]
    )

    assert exit_code == 0
    called_tools = [name for name, _ in calls]
    assert "fetch_stocktwits_messages" in called_tools
    assert "fetch_reddit_posts" in called_tools
    assert "get_news" not in called_tools

    evidence = json.loads(
        (tmp_path / "evidence" / "AAPL" / "2026-06-27" / "evidence.json").read_text(
            encoding="utf-8"
        )
    )
    social_calls = evidence["roles"]["social"]["tool_calls"]
    assert sorted(social_calls) == ["fetch_reddit_posts", "fetch_stocktwits_messages"]
    assert "financial_report" in evidence["roles"]


def test_workflow_state_records_explicit_visible_debate_completion_gates(tmp_path):
    collector = _load_collector()
    role_packet_paths = {
        "market": str(tmp_path / "roles" / "market.md"),
        "news": str(tmp_path / "roles" / "news.md"),
        "financial_report": str(tmp_path / "roles" / "financial_report.md"),
    }

    workflow = collector._workflow_state(
        "AAPL",
        "2026-06-27",
        ["market", "news"],
        role_packet_paths,
        tmp_path / "evidence.json",
        tmp_path / "reports" / "AAPL" / "2026-06-27",
        max_debate_rounds=1,
        max_risk_discuss_rounds=1,
    )

    stages = {stage["stage"]: stage for stage in workflow["stages"]}
    assert (
        stages["bear_researcher_round_1"]["completion_gate"]
        == "Bear must directly rebut the strongest Bull point."
    )
    assert (
        stages["research_manager"]["completion_gate"]
        == "Research Manager must weigh Bull vs Bear evidence."
    )
    assert (
        stages["conservative_risk_round_1"]["completion_gate"]
        == "Conservative Risk must directly respond to Aggressive Risk."
    )
    assert (
        stages["neutral_risk_round_1"]["completion_gate"]
        == "Neutral Risk must weigh Aggressive vs Conservative."
    )
    assert (
        stages["portfolio_manager"]["completion_gate"]
        == "Portfolio Manager must synthesize the risk debate."
    )


def test_collector_records_tool_failures_without_collecting_unselected_roles(tmp_path, monkeypatch):
    collector = _load_collector()

    def failing_stock_data(**kwargs):
        raise RuntimeError("vendor temporarily unavailable")

    monkeypatch.setattr(collector, "get_stock_data", failing_stock_data)
    monkeypatch.setattr(collector, "get_verified_market_snapshot", lambda **kwargs: "snapshot")
    monkeypatch.setattr(collector, "get_indicators", lambda **kwargs: "indicator")
    monkeypatch.setattr(
        collector,
        "collect_financial_document_sources",
        lambda ticker, trade_date, **kwargs: {"status": "unavailable", "sources": []},
    )
    monkeypatch.setattr(collector, "resolve_instrument_identity", lambda ticker: {})

    exit_code = collector.main(
        [
            "--ticker",
            "AAPL",
            "--trade-date",
            "2026-06-27",
            "--selected-analysts",
            "market",
            "--output-dir",
            str(tmp_path),
        ]
    )

    assert exit_code == 0
    evidence = json.loads(
        (tmp_path / "evidence" / "AAPL" / "2026-06-27" / "evidence.json").read_text(
            encoding="utf-8"
        )
    )
    stock_call = evidence["roles"]["market"]["tool_calls"]["get_stock_data"]
    assert stock_call["status"] == "error"
    assert "vendor temporarily unavailable" in stock_call["error"]
    assert "fundamentals" not in evidence["roles"]
    assert "financial_report" in evidence["roles"]


def test_workflow_state_can_expand_research_and_risk_debate_rounds(tmp_path):
    collector = _load_collector()
    role_packet_paths = {
        "market": str(tmp_path / "roles" / "market.md"),
        "news": str(tmp_path / "roles" / "news.md"),
        "financial_report": str(tmp_path / "roles" / "financial_report.md"),
    }

    workflow = collector._workflow_state(
        "AAPL",
        "2026-06-27",
        ["market", "news"],
        role_packet_paths,
        tmp_path / "evidence.json",
        tmp_path / "reports" / "AAPL" / "2026-06-27",
        max_debate_rounds=2,
        max_risk_discuss_rounds=2,
    )

    stages = {stage["stage"]: stage for stage in workflow["stages"]}
    assert "bull_researcher_round_2" in stages
    assert "bear_researcher_round_2" in stages
    assert "aggressive_risk_round_2" in stages
    assert "neutral_risk_round_2" in stages

    paths = workflow["report_paths"]
    assert paths["bear_researcher_round_1"] in stages[
        "bull_researcher_round_2"
    ]["allowed_inputs"]
    assert paths["bull_researcher_round_2"] in stages[
        "bear_researcher_round_2"
    ]["allowed_inputs"]
    assert paths["neutral_risk_round_1"] in stages[
        "aggressive_risk_round_2"
    ]["allowed_inputs"]
    assert paths["neutral_risk_round_2"] in stages[
        "portfolio_manager"
    ]["allowed_inputs"]


def test_collector_does_not_call_upstream_graph_or_llm_backend():
    source = COLLECTOR_PATH.read_text(encoding="utf-8")

    assert "TradingAgentsGraph" not in source
    assert "tradingagents.graph" not in source
    assert "create_llm_client" not in source
    assert "run_tradingagents_reports" not in source


def test_memory_validator_rejects_placeholder_memory_updates(tmp_path):
    validator = _load_memory_validator()
    memory_root = tmp_path / "memory" / "AAPL"
    for role_name in validator.ROLE_MEMORY_NAMES:
        role_root = memory_root / role_name
        role_root.mkdir(parents=True)
        (role_root / "memory.md").write_text(f"# {role_name}\n", encoding="utf-8")
        (role_root / "memory.json").write_text(json.dumps({"role": role_name}), encoding="utf-8")

    output_path = tmp_path / "reports" / "AAPL" / "2026-06-27" / "1_analysts" / "news.md"
    output_path.parent.mkdir(parents=True)
    output_path.write_text(
        "# News Analyst\n\n## Memory Update\n\nNo durable role-memory update was recorded for this historical generated output.\n",
        encoding="utf-8",
    )
    workflow_path = tmp_path / "evidence" / "AAPL" / "2026-06-27" / "workflow_state.json"
    workflow_path.parent.mkdir(parents=True)
    workflow_path.write_text(
        json.dumps(
            {
                "ticker": "AAPL",
                "memory_root": str(memory_root),
                "report_dir": str(output_path.parents[2]),
                "stages": [
                    {
                        "stage": "news_analyst",
                        "role_memory": "news_analyst",
                        "allowed_memory_files": [
                            str(memory_root / "news_analyst" / "memory.md"),
                            str(memory_root / "news_analyst" / "memory.json"),
                        ],
                        "forbidden_memory_roots": [
                            str(memory_root / role_name)
                            for role_name in validator.ROLE_MEMORY_NAMES
                            if role_name != "news_analyst"
                        ],
                        "output_path": str(output_path),
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    issues = validator.validate(tmp_path)

    assert "AAPL/news_analyst: memory update is placeholder or not evidence-linked" in issues
