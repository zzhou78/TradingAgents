from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COLLECTOR_PATH = (
    ROOT / "codex_tradingagents_skillkit" / "scripts" / "collect_role_evidence.py"
)


def _load_collector():
    spec = importlib.util.spec_from_file_location("collect_role_evidence", COLLECTOR_PATH)
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
        fundamentals_packet = tmp_path / "evidence" / ticker / "2026-06-27" / "roles" / "fundamentals.md"
        data = tmp_path / "evidence" / ticker / "2026-06-27" / "evidence.json"
        assert packet.exists()
        assert market_packet.exists()
        assert news_packet.exists()
        assert not fundamentals_packet.exists()
        assert data.exists()
        assert "## Role: market" in market_packet.read_text(encoding="utf-8")
        assert "## Role: news" in news_packet.read_text(encoding="utf-8")
        assert "## Role: news" not in market_packet.read_text(encoding="utf-8")

    for run in summary["runs"]:
        assert sorted(run["role_packet_paths"]) == ["market", "news"]
        assert run["role_packet_path"].endswith("role_packets.md")
        assert run["workflow_state_path"].endswith("workflow_state.json")

        workflow = json.loads(Path(run["workflow_state_path"]).read_text(encoding="utf-8"))
        assert workflow["requires_user_input"] is False
        assert workflow["uses_tradingagents_graph"] is False
        assert workflow["report_style"] == "tradingagents"
        stage_names = [stage["stage"] for stage in workflow["stages"]]
        assert stage_names[:2] == ["market_analyst", "news_analyst"]
        assert stage_names[-1] == "complete_report"

        market_stage = workflow["stages"][0]
        assert market_stage["skill"] == "tradingagents-market-analyst"
        assert market_stage["allowed_inputs"] == [run["role_packet_paths"]["market"]]
        assert market_stage["forbidden_inputs"] == [run["role_packet_paths"]["news"]]

        report_paths = workflow["report_paths"]
        normalized_market_report = report_paths["market_report"].replace("\\", "/")
        normalized_complete_report = report_paths["complete_report"].replace("\\", "/")
        ticker = run["ticker"]
        assert normalized_market_report.endswith(f"reports/{ticker}/2026-06-27/1_analysts/market.md")
        assert normalized_complete_report.endswith(f"reports/{ticker}/2026-06-27/complete_report.md")
        final_stage = workflow["stages"][-1]
        assert report_paths["market_report"] in final_stage["allowed_inputs"]
        assert report_paths["news_report"] in final_stage["allowed_inputs"]
        assert report_paths["portfolio_manager"] in final_stage["allowed_inputs"]


def test_collector_records_tool_failures_without_collecting_unselected_roles(tmp_path, monkeypatch):
    collector = _load_collector()

    def failing_stock_data(**kwargs):
        raise RuntimeError("vendor temporarily unavailable")

    monkeypatch.setattr(collector, "get_stock_data", failing_stock_data)
    monkeypatch.setattr(collector, "get_verified_market_snapshot", lambda **kwargs: "snapshot")
    monkeypatch.setattr(collector, "get_indicators", lambda **kwargs: "indicator")
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


def test_collector_does_not_call_upstream_graph_or_llm_backend():
    source = COLLECTOR_PATH.read_text(encoding="utf-8")

    assert "TradingAgentsGraph" not in source
    assert "tradingagents.graph" not in source
    assert "create_llm_client" not in source
    assert "run_tradingagents_reports" not in source
