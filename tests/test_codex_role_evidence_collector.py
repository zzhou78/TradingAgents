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
        data = tmp_path / "evidence" / ticker / "2026-06-27" / "evidence.json"
        assert packet.exists()
        assert data.exists()
        text = packet.read_text(encoding="utf-8")
        assert "## Role: market" in text
        assert "## Role: news" in text
        assert "## Role: fundamentals" not in text


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
    assert "create_llm_client" not in source
    assert "run_tradingagents_reports" not in source
