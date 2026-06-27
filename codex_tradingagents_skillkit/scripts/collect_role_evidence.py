# ruff: noqa: E402

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yfinance as yf
from yfinance import cache as yf_cache

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = BUNDLE_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tradingagents.agents.utils.agent_utils import resolve_instrument_identity
from tradingagents.agents.utils.core_stock_tools import get_stock_data
from tradingagents.agents.utils.fundamental_data_tools import (
    get_balance_sheet,
    get_cashflow,
    get_fundamentals,
    get_income_statement,
)
from tradingagents.agents.utils.market_data_validation_tools import (
    get_verified_market_snapshot,
)
from tradingagents.agents.utils.news_data_tools import (
    get_global_news,
    get_insider_transactions,
    get_news,
)
from tradingagents.agents.utils.technical_indicators_tools import get_indicators
from tradingagents.dataflows.config import set_config
from tradingagents.default_config import DEFAULT_CONFIG

DEFAULT_ANALYSTS = ["market", "social", "news", "fundamentals"]
VALID_ANALYSTS = set(DEFAULT_ANALYSTS)
MARKET_INDICATORS = ["close_50_sma", "close_200_sma", "rsi", "macd", "atr"]

ROLE_SKILLS = {
    "market": "tradingagents-market-analyst",
    "social": "tradingagents-sentiment-analyst",
    "news": "tradingagents-news-analyst",
    "fundamentals": "tradingagents-fundamentals-analyst",
}
ANALYST_STAGE_NAMES = {
    "market": "market_analyst",
    "social": "sentiment_analyst",
    "news": "news_analyst",
    "fundamentals": "fundamentals_analyst",
}
ANALYST_REPORT_FILES = {
    "market": "market.md",
    "social": "sentiment.md",
    "news": "news.md",
    "fundamentals": "fundamentals.md",
}
WORKFLOW_SKILLS = [
    "tradingagents-workflow-orchestrator",
    "tradingagents-analyst-sequencing",
    "tradingagents-dataflow-routing",
    "tradingagents-debate-routing",
    "tradingagents-run-persistence",
]
DEFAULT_MAX_DEBATE_ROUNDS = 1
DEFAULT_MAX_RISK_DISCUSS_ROUNDS = 1


def _split_tickers(raw: str) -> list[str]:
    return [part.strip().upper() for part in raw.replace("\n", ",").split(",") if part.strip()]


def _parse_analysts(raw: str) -> list[str]:
    analysts = [item.strip().lower() for item in raw.split(",") if item.strip()]
    unknown = [item for item in analysts if item not in VALID_ANALYSTS]
    if unknown:
        raise ValueError(f"unknown selected analyst key(s): {', '.join(unknown)}")
    if not analysts:
        raise ValueError("at least one analyst must be selected")
    return analysts


def _start_date(trade_date: str, lookback_days: int) -> str:
    parsed = datetime.strptime(trade_date, "%Y-%m-%d")
    return (parsed - timedelta(days=lookback_days)).strftime("%Y-%m-%d")


def _call_tool(func: Callable[..., Any], **kwargs: Any) -> dict[str, Any]:
    try:
        value = func.invoke(kwargs) if hasattr(func, "invoke") else func(**kwargs)
        return {"status": "ok", "args": kwargs, "output": str(value)}
    except Exception as exc:  # noqa: BLE001 - evidence collection records failures.
        return {"status": "error", "args": kwargs, "error": str(exc)}


def _build_config(output_dir: Path) -> dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    config["results_dir"] = str(output_dir / "tradingagents_results")
    config["data_cache_dir"] = str(output_dir / "tradingagents_cache")
    config["memory_log_path"] = str(output_dir / "tradingagents_memory" / "trading_memory.md")
    config["checkpoint_enabled"] = False
    yfinance_cache_dir = output_dir / "yfinance_cache"
    yfinance_cache_dir.mkdir(parents=True, exist_ok=True)
    yf.set_tz_cache_location(str(yfinance_cache_dir))
    yf_cache.set_cache_location(str(yfinance_cache_dir))
    return config


def _collect_market(ticker: str, trade_date: str, lookback_days: int) -> dict[str, Any]:
    start = _start_date(trade_date, lookback_days)
    calls = {
        "get_stock_data": _call_tool(
            get_stock_data,
            symbol=ticker,
            start_date=start,
            end_date=trade_date,
        ),
        "get_verified_market_snapshot": _call_tool(
            get_verified_market_snapshot,
            symbol=ticker,
            curr_date=trade_date,
            look_back_days=lookback_days,
        ),
    }
    for indicator in MARKET_INDICATORS:
        calls[f"get_indicators:{indicator}"] = _call_tool(
            get_indicators,
            symbol=ticker,
            indicator=indicator,
            curr_date=trade_date,
            look_back_days=lookback_days,
        )
    return {"skill": ROLE_SKILLS["market"], "tool_calls": calls}


def _collect_social(ticker: str, trade_date: str, lookback_days: int) -> dict[str, Any]:
    start = _start_date(trade_date, min(lookback_days, 7))
    calls = {
        "get_news": _call_tool(
            get_news,
            ticker=ticker,
            start_date=start,
            end_date=trade_date,
        )
    }
    return {"skill": ROLE_SKILLS["social"], "tool_calls": calls}


def _collect_news(ticker: str, trade_date: str, lookback_days: int) -> dict[str, Any]:
    start = _start_date(trade_date, min(lookback_days, 7))
    calls = {
        "get_news": _call_tool(
            get_news,
            ticker=ticker,
            start_date=start,
            end_date=trade_date,
        ),
        "get_global_news": _call_tool(
            get_global_news,
            curr_date=trade_date,
            look_back_days=min(lookback_days, 7),
            limit=5,
        ),
        "get_insider_transactions": _call_tool(
            get_insider_transactions,
            ticker=ticker,
        ),
    }
    return {"skill": ROLE_SKILLS["news"], "tool_calls": calls}


def _collect_fundamentals(ticker: str, trade_date: str) -> dict[str, Any]:
    calls = {
        "get_fundamentals": _call_tool(
            get_fundamentals,
            ticker=ticker,
            curr_date=trade_date,
        ),
        "get_balance_sheet": _call_tool(
            get_balance_sheet,
            ticker=ticker,
            freq="quarterly",
            curr_date=trade_date,
        ),
        "get_cashflow": _call_tool(
            get_cashflow,
            ticker=ticker,
            freq="quarterly",
            curr_date=trade_date,
        ),
        "get_income_statement": _call_tool(
            get_income_statement,
            ticker=ticker,
            freq="quarterly",
            curr_date=trade_date,
        ),
    }
    return {"skill": ROLE_SKILLS["fundamentals"], "tool_calls": calls}


def _collect_role(role: str, ticker: str, trade_date: str, lookback_days: int) -> dict[str, Any]:
    if role == "market":
        return _collect_market(ticker, trade_date, lookback_days)
    if role == "social":
        return _collect_social(ticker, trade_date, lookback_days)
    if role == "news":
        return _collect_news(ticker, trade_date, lookback_days)
    if role == "fundamentals":
        return _collect_fundamentals(ticker, trade_date)
    raise ValueError(f"unknown role: {role}")


def _write_role_packets(evidence: dict[str, Any], path: Path) -> None:
    lines = [
        f"# Codex Role Evidence Packet: {evidence['ticker']}",
        "",
        f"- Trade date: `{evidence['trade_date']}`",
        f"- Instrument identity: `{evidence['identity'].get('company_name', evidence['ticker'])}`",
        "",
        "These packets are evidence only. Codex must act each role independently using the named skill.",
        "",
    ]
    for role, role_data in evidence["roles"].items():
        lines.extend(
            [
                f"## Role: {role}",
                "",
                f"- Skill: `{role_data['skill']}`",
                "",
            ]
        )
        for tool_name, call in role_data["tool_calls"].items():
            lines.extend(
                [
                    f"### Tool: {tool_name}",
                    "",
                    f"- Status: `{call['status']}`",
                    "",
                    "```text",
                    call.get("output") or call.get("error", ""),
                    "```",
                    "",
                ]
            )
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_single_role_packet(
    evidence: dict[str, Any],
    role: str,
    role_data: dict[str, Any],
    path: Path,
) -> None:
    lines = [
        f"# Codex Role Evidence Packet: {evidence['ticker']} / {role}",
        "",
        f"- Trade date: `{evidence['trade_date']}`",
        f"- Instrument identity: `{evidence['identity'].get('company_name', evidence['ticker'])}`",
        f"- Skill: `{role_data['skill']}`",
        "",
        "Read only this packet when acting this analyst role. Do not inspect other analyst role packets until the workflow advances to a downstream debate stage.",
        "",
        f"## Role: {role}",
        "",
    ]
    for tool_name, call in role_data["tool_calls"].items():
        lines.extend(
            [
                f"### Tool: {tool_name}",
                "",
                f"- Status: `{call['status']}`",
                "",
                "```text",
                call.get("output") or call.get("error", ""),
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def _report_paths(
    report_dir: Path,
    selected_analysts: list[str],
    max_debate_rounds: int,
    max_risk_discuss_rounds: int,
) -> dict[str, str]:
    paths = {
        "research_manager": str(report_dir / "2_research" / "manager.md"),
        "trader": str(report_dir / "3_trading" / "trader.md"),
        "portfolio_manager": str(report_dir / "5_portfolio" / "decision.md"),
        "complete_report": str(report_dir / "complete_report.md"),
    }
    for round_number in range(1, max_debate_rounds + 1):
        paths[f"bull_researcher_round_{round_number}"] = str(
            report_dir / "2_research" / f"bull_round_{round_number}.md"
        )
        paths[f"bear_researcher_round_{round_number}"] = str(
            report_dir / "2_research" / f"bear_round_{round_number}.md"
        )
    for round_number in range(1, max_risk_discuss_rounds + 1):
        paths[f"aggressive_risk_round_{round_number}"] = str(
            report_dir / "4_risk" / f"aggressive_round_{round_number}.md"
        )
        paths[f"conservative_risk_round_{round_number}"] = str(
            report_dir / "4_risk" / f"conservative_round_{round_number}.md"
        )
        paths[f"neutral_risk_round_{round_number}"] = str(
            report_dir / "4_risk" / f"neutral_round_{round_number}.md"
        )
    for role in selected_analysts:
        key = "sentiment_report" if role == "social" else f"{role}_report"
        paths[key] = str(report_dir / "1_analysts" / ANALYST_REPORT_FILES[role])
    return paths


def _workflow_state(
    ticker: str,
    trade_date: str,
    selected_analysts: list[str],
    role_packet_paths: dict[str, str],
    evidence_path: Path,
    report_dir: Path,
    max_debate_rounds: int,
    max_risk_discuss_rounds: int,
) -> dict[str, Any]:
    paths = _report_paths(
        report_dir,
        selected_analysts,
        max_debate_rounds,
        max_risk_discuss_rounds,
    )
    stages = []
    for role in selected_analysts:
        stage_name = ANALYST_STAGE_NAMES[role]
        output_key = "sentiment_report" if role == "social" else f"{role}_report"
        stages.append(
            {
                "stage": stage_name,
                "skill": ROLE_SKILLS[role],
                "allowed_inputs": [role_packet_paths[role]],
                "forbidden_inputs": [
                    path
                    for other_role, path in role_packet_paths.items()
                    if other_role != role
                ],
                "output_path": paths[output_key],
                "completion_gate": f"write {output_key} in TradingAgents analyst style",
            }
        )

    analyst_outputs = [
        paths["sentiment_report" if role == "social" else f"{role}_report"]
        for role in selected_analysts
    ]
    downstream = []
    research_debate_outputs = []
    for round_number in range(1, max_debate_rounds + 1):
        bull_stage = f"bull_researcher_round_{round_number}"
        bear_stage = f"bear_researcher_round_{round_number}"
        downstream.append(
            (
                bull_stage,
                "tradingagents-bull-researcher",
                analyst_outputs + research_debate_outputs,
            )
        )
        downstream.append(
            (
                bear_stage,
                "tradingagents-bear-researcher",
                analyst_outputs + research_debate_outputs + [paths[bull_stage]],
            )
        )
        research_debate_outputs.extend([paths[bull_stage], paths[bear_stage]])

    downstream.extend(
        [
            (
                "research_manager",
                "tradingagents-research-manager",
                analyst_outputs + research_debate_outputs,
            ),
            (
                "trader",
                "tradingagents-trader",
                analyst_outputs + [paths["research_manager"]],
            ),
        ]
    )
    risk_debate_outputs = []
    for round_number in range(1, max_risk_discuss_rounds + 1):
        aggressive_stage = f"aggressive_risk_round_{round_number}"
        conservative_stage = f"conservative_risk_round_{round_number}"
        neutral_stage = f"neutral_risk_round_{round_number}"
        base_risk_inputs = analyst_outputs + [paths["research_manager"], paths["trader"]]
        downstream.append(
            (
                aggressive_stage,
                "tradingagents-aggressive-risk-analyst",
                base_risk_inputs + risk_debate_outputs,
            )
        )
        downstream.append(
            (
                conservative_stage,
                "tradingagents-conservative-risk-analyst",
                base_risk_inputs + risk_debate_outputs + [paths[aggressive_stage]],
            )
        )
        downstream.append(
            (
                neutral_stage,
                "tradingagents-neutral-risk-analyst",
                base_risk_inputs
                + risk_debate_outputs
                + [paths[aggressive_stage], paths[conservative_stage]],
            )
        )
        risk_debate_outputs.extend(
            [paths[aggressive_stage], paths[conservative_stage], paths[neutral_stage]]
        )
    downstream.append(
        (
            "portfolio_manager",
            "tradingagents-portfolio-manager",
            analyst_outputs + [paths["research_manager"], paths["trader"]] + risk_debate_outputs,
        )
    )
    for stage_name, skill, allowed_inputs in downstream:
        stages.append(
            {
                "stage": stage_name,
                "skill": skill,
                "allowed_inputs": allowed_inputs,
                "forbidden_inputs": [],
                "output_path": paths[stage_name],
                "completion_gate": "write the stage output before advancing",
            }
        )
    complete_report_inputs = analyst_outputs + [
        paths[stage_name]
        for stage_name, _, _ in downstream
    ]
    stages.append(
        {
            "stage": "complete_report",
            "skill": "tradingagents-run-persistence",
            "allowed_inputs": complete_report_inputs,
            "forbidden_inputs": [],
            "output_path": paths["complete_report"],
            "completion_gate": "assemble TradingAgents-style complete_report.md",
        }
    )

    return {
        "ticker": ticker,
        "trade_date": trade_date,
        "codex_operated": True,
        "requires_user_input": False,
        "uses_tradingagents_graph": False,
        "report_style": "tradingagents",
        "max_debate_rounds": max_debate_rounds,
        "max_risk_discuss_rounds": max_risk_discuss_rounds,
        "evidence_path": str(evidence_path),
        "report_dir": str(report_dir),
        "report_paths": paths,
        "rules": [
            "Codex acts each role using the listed skill.",
            "Analyst stages read only their own role packet.",
            "Downstream stages read only completed prior report files listed in allowed_inputs.",
            "Do not call upstream graph orchestration or external LLM backends for role reasoning.",
            "Do not submit broker orders, connect to GCAF, or treat output as real trading advice.",
        ],
        "stages": stages,
    }


def collect(args: argparse.Namespace) -> dict[str, Any]:
    selected_analysts = _parse_analysts(args.selected_analysts)
    max_debate_rounds = max(1, args.max_debate_rounds)
    max_risk_discuss_rounds = max(1, args.max_risk_discuss_rounds)
    tickers: list[str] = []
    for raw in args.ticker:
        tickers.extend(_split_tickers(raw))
    tickers = list(dict.fromkeys(tickers))
    if not tickers:
        raise ValueError("provide at least one ticker through --ticker")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    set_config(_build_config(output_dir))

    summary = {
        "trade_date": args.trade_date,
        "selected_analysts": selected_analysts,
        "max_debate_rounds": max_debate_rounds,
        "max_risk_discuss_rounds": max_risk_discuss_rounds,
        "output_dir": str(output_dir),
        "codex_operated": True,
        "uses_tradingagents_graph": False,
        "skill_context": {
            "workflow_skills": WORKFLOW_SKILLS,
            "role_skills": [ROLE_SKILLS[key] for key in selected_analysts],
            "skill_root": str(BUNDLE_ROOT / "skills"),
            "runtime_uses_upstream_python": ["tradingagents/dataflows", "tradingagents/agents/utils"],
        },
        "runs": [],
    }

    for ticker in tickers:
        evidence_dir = output_dir / "evidence" / ticker / args.trade_date
        evidence_dir.mkdir(parents=True, exist_ok=True)
        identity = resolve_instrument_identity(ticker)
        evidence = {
            "ticker": ticker,
            "trade_date": args.trade_date,
            "identity": identity,
            "roles": {
                role: _collect_role(role, ticker, args.trade_date, args.lookback_days)
                for role in selected_analysts
            },
        }
        evidence_path = evidence_dir / "evidence.json"
        packet_path = evidence_dir / "role_packets.md"
        role_dir = evidence_dir / "roles"
        role_dir.mkdir(exist_ok=True)
        evidence_path.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
        _write_role_packets(evidence, packet_path)
        role_packet_paths = {}
        for role, role_data in evidence["roles"].items():
            role_packet = role_dir / f"{role}.md"
            _write_single_role_packet(evidence, role, role_data, role_packet)
            role_packet_paths[role] = str(role_packet)
        report_dir = output_dir / "reports" / ticker / args.trade_date
        workflow_path = evidence_dir / "workflow_state.json"
        workflow_path.write_text(
            json.dumps(
                _workflow_state(
                    ticker,
                    args.trade_date,
                    selected_analysts,
                    role_packet_paths,
                    evidence_path,
                    report_dir,
                    max_debate_rounds,
                    max_risk_discuss_rounds,
                ),
                indent=2,
            ),
            encoding="utf-8",
        )
        summary["runs"].append(
            {
                "ticker": ticker,
                "evidence_path": str(evidence_path),
                "role_packet_path": str(packet_path),
                "role_packet_paths": role_packet_paths,
                "workflow_state_path": str(workflow_path),
            }
        )

    (output_dir / "evidence_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    return summary


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect upstream TradingAgents data evidence for Codex-operated role reports."
    )
    parser.add_argument("--ticker", action="append", default=[], help="Ticker or comma-separated tickers.")
    parser.add_argument("--trade-date", required=True, help="Analysis date in YYYY-MM-DD format.")
    parser.add_argument("--output-dir", type=Path, default=BUNDLE_ROOT / "runs")
    parser.add_argument("--selected-analysts", default=",".join(DEFAULT_ANALYSTS))
    parser.add_argument("--lookback-days", type=int, default=30)
    parser.add_argument("--max-debate-rounds", type=int, default=DEFAULT_MAX_DEBATE_ROUNDS)
    parser.add_argument("--max-risk-discuss-rounds", type=int, default=DEFAULT_MAX_RISK_DISCUSS_ROUNDS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    try:
        summary = collect(_parse_args(argv))
    except Exception as exc:
        print(f"Evidence collection failed: {exc}", file=sys.stderr)
        return 1

    for run in summary["runs"]:
        print(f"{run['ticker']}: {run['role_packet_path']}")
    print(f"Summary: {Path(summary['output_dir']) / 'evidence_summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
