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
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from financial_document_sources import (
    collect_financial_document_sources,
    render_financial_document_packet,
)

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
from tradingagents.dataflows.reddit import fetch_reddit_posts
from tradingagents.dataflows.stocktwits import fetch_stocktwits_messages
from tradingagents.default_config import DEFAULT_CONFIG

DEFAULT_ANALYSTS = ["market", "social", "news", "fundamentals"]
VALID_ANALYSTS = set(DEFAULT_ANALYSTS)
MARKET_INDICATORS = ["close_50_sma", "close_200_sma", "rsi", "macd", "atr"]
FINANCIAL_REPORT_ROLE = "financial_report"

ROLE_SKILLS = {
    "market": "tradingagents-market-analyst",
    "social": "tradingagents-sentiment-analyst",
    "news": "tradingagents-news-analyst",
    "fundamentals": "tradingagents-fundamentals-analyst",
    FINANCIAL_REPORT_ROLE: "tradingagents-financial-report-analyst",
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
    "tradingagents-quality-reviewer",
]
DEFAULT_MAX_DEBATE_ROUNDS = 1
DEFAULT_MAX_RISK_DISCUSS_ROUNDS = 1
ROLE_MEMORY_NAMES = [
    "market_analyst",
    "sentiment_analyst",
    "news_analyst",
    "fundamentals_analyst",
    "financial_report_analyst",
    "industry_theme_discovery_analyst",
    "bull_researcher",
    "bear_researcher",
    "research_manager",
    "trader",
    "aggressive_risk_analyst",
    "conservative_risk_analyst",
    "neutral_risk_analyst",
    "portfolio_manager",
    "quality_reviewer",
]
MEMORY_UPDATE_FOOTER = """## Memory Update

* Durable facts to retain:
* Prior mistake to avoid:
* Open questions:
* Evidence references:
* Staleness / expiry:
"""


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


def _clean_tool_text(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.replace("\r\n", "\n").split("\n"))


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
    calls = {
        "fetch_stocktwits_messages": _call_tool(
            fetch_stocktwits_messages,
            ticker=ticker,
            limit=30,
        ),
        "fetch_reddit_posts": _call_tool(
            fetch_reddit_posts,
            ticker=ticker,
            limit_per_sub=5,
            inter_request_delay=0.0,
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


def _collect_financial_report(ticker: str, trade_date: str, identity: dict[str, Any] | None = None) -> dict[str, Any]:
    packet = collect_financial_document_sources(ticker, trade_date, identity=identity)
    return {
        "skill": ROLE_SKILLS[FINANCIAL_REPORT_ROLE],
        "tool_calls": {
            "collect_financial_document_sources": {
                "status": packet.get("status", "unknown"),
                "args": {
                    "ticker": ticker,
                    "trade_date": trade_date,
                    "source_policy": "Market-aware routing: US uses SEC; ASX uses ASX announcements; unsupported markets return explicit unavailable coverage.",
                },
                "output": render_financial_document_packet(packet),
            }
        },
    }


def _collect_role(role: str, ticker: str, trade_date: str, lookback_days: int) -> dict[str, Any]:
    if role == "market":
        return _collect_market(ticker, trade_date, lookback_days)
    if role == "social":
        return _collect_social(ticker, trade_date, lookback_days)
    if role == "news":
        return _collect_news(ticker, trade_date, lookback_days)
    if role == "fundamentals":
        return _collect_fundamentals(ticker, trade_date)
    if role == FINANCIAL_REPORT_ROLE:
        return _collect_financial_report(ticker, trade_date)
    raise ValueError(f"unknown role: {role}")


def _stage_memory_role(stage_name: str) -> str:
    if stage_name.startswith("bull_researcher_round"):
        return "bull_researcher"
    if stage_name.startswith("bear_researcher_round"):
        return "bear_researcher"
    if stage_name.startswith("aggressive_risk_round"):
        return "aggressive_risk_analyst"
    if stage_name.startswith("conservative_risk_round"):
        return "conservative_risk_analyst"
    if stage_name.startswith("neutral_risk_round"):
        return "neutral_risk_analyst"
    if stage_name == "quality_review":
        return "quality_reviewer"
    if stage_name in {"complete_report"}:
        return "portfolio_manager"
    return stage_name


def _memory_seed(role: str, ticker: str, trade_date: str) -> str:
    return f"""# Role Memory: {ticker} / {role}

- role: `{role}`
- ticker: `{ticker}`
- last_updated: `{trade_date}`
- review_date: `{trade_date}`

## Durable facts learned

- None recorded yet.

## Recurring issues

- None recorded yet.

## Prior role conclusions

- None recorded yet.

## Prior mistakes to avoid

- Prefer current evidence over stale memory.

## Open questions

- None recorded yet.

## Stale assumptions

- None recorded yet.

## Evidence references

- None recorded yet.
"""


def _ensure_role_memories(ticker: str, trade_date: str) -> dict[str, dict[str, str]]:
    memory_map: dict[str, dict[str, str]] = {}
    for role in ROLE_MEMORY_NAMES:
        role_dir = BUNDLE_ROOT / "memory" / ticker / role
        role_dir.mkdir(parents=True, exist_ok=True)
        md_path = role_dir / "memory.md"
        json_path = role_dir / "memory.json"
        if not md_path.exists():
            md_path.write_text(_memory_seed(role, ticker, trade_date), encoding="utf-8")
        if not json_path.exists():
            json_path.write_text(
                json.dumps(
                    {
                        "role": role,
                        "ticker": ticker,
                        "last_updated": trade_date,
                        "durable_facts_learned": [],
                        "recurring_issues": [],
                        "prior_role_conclusions": [],
                        "prior_mistakes_to_avoid": ["Prefer current evidence over stale memory."],
                        "open_questions": [],
                        "stale_assumptions": [],
                        "evidence_references": [],
                        "review_date": trade_date,
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
        memory_map[role] = {
            "memory_md": str(md_path),
            "memory_json": str(json_path),
            "root": str(role_dir),
        }
    return memory_map


def _attach_memory_contract(
    stage: dict[str, Any],
    *,
    ticker: str,
    memory_map: dict[str, dict[str, str]],
    report_dir: Path,
) -> dict[str, Any]:
    memory_role = _stage_memory_role(stage["stage"])
    own_memory = memory_map[memory_role]
    stage["role_memory"] = memory_role
    stage["allowed_memory_files"] = [own_memory["memory_md"], own_memory["memory_json"]]
    stage["forbidden_memory_roots"] = [
        details["root"] for role, details in memory_map.items() if role != memory_role
    ]
    update_dir = report_dir / "memory_updates"
    stage["memory_update_path"] = str(update_dir / f"{stage['stage']}.md")
    stage["memory_rules"] = [
        "Read only the allowed input files.",
        "Read only the allowed memory files.",
        "Do not inspect other role memory.",
        "Current evidence overrides stale memory.",
        "If memory conflicts with current evidence, state the conflict explicitly.",
        "At the end, write a memory update for this role only.",
    ]
    stage["ticker"] = ticker
    return stage


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
                    _clean_tool_text(call.get("output") or call.get("error", "")),
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
                _clean_tool_text(call.get("output") or call.get("error", "")),
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
        "financial_report": str(report_dir / "1_analysts" / "financial_report.md"),
        "industry_theme_report": str(report_dir / "1_analysts" / "industry_theme.md"),
        "quality_review": str(report_dir / "6_quality" / "quality_review.md"),
        "quality_gate": str(report_dir / "6_quality" / "quality_gate.json"),
        "debate_record": str(report_dir / "debate_record.md"),
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
    memory_map: dict[str, dict[str, str]] | None = None,
) -> dict[str, Any]:
    memory_map = memory_map or _ensure_role_memories(ticker, trade_date)
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
            _attach_memory_contract(
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
                },
                ticker=ticker,
                memory_map=memory_map,
                report_dir=report_dir,
            )
        )

    analyst_outputs = [
        paths["sentiment_report" if role == "social" else f"{role}_report"]
        for role in selected_analysts
    ]
    stages.append(
        _attach_memory_contract(
            {
            "stage": "financial_report_analyst",
            "skill": "tradingagents-financial-report-analyst",
            "allowed_inputs": analyst_outputs
            + [role_packet_paths[FINANCIAL_REPORT_ROLE], str(evidence_path)],
            "forbidden_inputs": [],
            "output_path": paths["financial_report"],
            "completion_gate": "write financial_report.md before industry/theme discovery",
            },
            ticker=ticker,
            memory_map=memory_map,
            report_dir=report_dir,
        )
    )
    analyst_outputs.append(paths["financial_report"])
    stages.append(
        _attach_memory_contract(
            {
            "stage": "industry_theme_discovery_analyst",
            "skill": "tradingagents-industry-theme-discovery-analyst",
            "allowed_inputs": analyst_outputs + [str(evidence_path)],
            "forbidden_inputs": [],
            "output_path": paths["industry_theme_report"],
            "completion_gate": "discover evidence-grounded industry/theme context before research debate",
            },
            ticker=ticker,
            memory_map=memory_map,
            report_dir=report_dir,
        )
    )
    analyst_outputs.append(paths["industry_theme_report"])
    downstream = []
    completion_gates = {
        "bear_researcher_round_1": "Bear must directly rebut the strongest Bull point.",
        "research_manager": "Research Manager must weigh Bull vs Bear evidence.",
        "conservative_risk_round_1": "Conservative Risk must directly respond to Aggressive Risk.",
        "neutral_risk_round_1": "Neutral Risk must weigh Aggressive vs Conservative.",
        "portfolio_manager": "Portfolio Manager must synthesize the risk debate.",
    }
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
            _attach_memory_contract(
                {
                "stage": stage_name,
                "skill": skill,
                "allowed_inputs": allowed_inputs,
                "forbidden_inputs": [],
                "output_path": paths[stage_name],
                "completion_gate": completion_gates.get(
                    stage_name, "write the visible debate-stage output before advancing"
                ),
                },
                ticker=ticker,
                memory_map=memory_map,
                report_dir=report_dir,
            )
        )
    complete_report_inputs = analyst_outputs + [
        paths[stage_name]
        for stage_name, _, _ in downstream
    ]
    stages.append(
        _attach_memory_contract(
            {
            "stage": "complete_report",
            "skill": "tradingagents-run-persistence",
            "allowed_inputs": complete_report_inputs,
            "forbidden_inputs": [],
            "output_path": paths["complete_report"],
            "completion_gate": "assemble TradingAgents-style complete_report.md",
            },
            ticker=ticker,
            memory_map=memory_map,
            report_dir=report_dir,
        )
    )
    stages.append(
        _attach_memory_contract(
            {
            "stage": "quality_review",
            "skill": "tradingagents-quality-reviewer",
            "allowed_inputs": complete_report_inputs + [paths["complete_report"], str(evidence_path)],
            "forbidden_inputs": [],
            "output_path": paths["quality_review"],
            "completion_gate": "write quality_review.md and quality_gate.json",
            },
            ticker=ticker,
            memory_map=memory_map,
            report_dir=report_dir,
        )
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
            "Each stage may read only its own role memory for the same ticker.",
            "Memory must not override current evidence.",
        ],
        "memory_root": str(BUNDLE_ROOT / "memory" / ticker),
        "stages": stages,
    }


def _write_debate_record(workflow: dict[str, Any], path: Path) -> None:
    stage_groups = [
        (
            "Research Team Debate",
            {"bull_researcher_round", "bear_researcher_round", "research_manager"},
        ),
        (
            "Risk Management Team Debate",
            {
                "aggressive_risk_round",
                "conservative_risk_round",
                "neutral_risk_round",
                "portfolio_manager",
            },
        ),
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# TradingAgents Debate Record",
        "",
        f"- Ticker: `{workflow['ticker']}`",
        f"- Trade date: `{workflow['trade_date']}`",
        f"- Max research debate rounds: `{workflow['max_debate_rounds']}`",
        f"- Max risk debate rounds: `{workflow['max_risk_discuss_rounds']}`",
        "",
        "This file is the report-folder index for Codex-visible debate turns. The turn files are prepared below and filled as Codex acts each role stage.",
        "",
    ]
    for heading, stage_prefixes in stage_groups:
        lines.extend([f"## {heading}", ""])
        for stage in workflow["stages"]:
            stage_name = stage["stage"]
            if not any(stage_name.startswith(prefix) for prefix in stage_prefixes):
                continue
            lines.extend(
                [
                    f"### {stage_name}",
                    "",
                    f"- Skill: `{stage['skill']}`",
                    f"- Output: `{stage['output_path']}`",
                    "- Allowed inputs:",
                ]
            )
            lines.extend(f"  - `{input_path}`" for input_path in stage["allowed_inputs"])
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_stage_scaffolds(workflow: dict[str, Any]) -> None:
    for stage in workflow["stages"]:
        path = Path(stage["output_path"])
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {stage['stage']}",
            "",
            "Pending Codex role output.",
            "",
            f"- Ticker: `{workflow['ticker']}`",
            f"- Trade date: `{workflow['trade_date']}`",
            f"- Skill: `{stage['skill']}`",
            f"- Completion gate: {stage['completion_gate']}",
            "",
            "## Allowed Inputs",
            "",
        ]
        lines.extend(f"- `{input_path}`" for input_path in stage["allowed_inputs"])
        if stage["forbidden_inputs"]:
            lines.extend(["", "## Forbidden Inputs", ""])
            lines.extend(f"- `{input_path}`" for input_path in stage["forbidden_inputs"])
        lines.extend(
            [
                "",
                "## Role Output",
                "",
                "Codex fills this section when the workflow reaches this stage.",
                "",
                MEMORY_UPDATE_FOOTER.rstrip(),
            ]
        )
        path.write_text("\n".join(lines), encoding="utf-8")


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
            "role_skills": [
                *[ROLE_SKILLS[key] for key in selected_analysts],
                "tradingagents-financial-report-analyst",
                "tradingagents-industry-theme-discovery-analyst",
            ],
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
        evidence["roles"][FINANCIAL_REPORT_ROLE] = _collect_financial_report(
            ticker,
            args.trade_date,
            identity,
        )
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
        workflow = _workflow_state(
            ticker,
            args.trade_date,
            selected_analysts,
            role_packet_paths,
            evidence_path,
            report_dir,
            max_debate_rounds,
            max_risk_discuss_rounds,
        )
        workflow_path.write_text(
            json.dumps(workflow, indent=2),
            encoding="utf-8",
        )
        debate_record_path = Path(workflow["report_paths"]["debate_record"])
        _write_stage_scaffolds(workflow)
        _write_debate_record(workflow, debate_record_path)
        summary["runs"].append(
            {
                "ticker": ticker,
                "evidence_path": str(evidence_path),
                "role_packet_path": str(packet_path),
                "role_packet_paths": role_packet_paths,
                "workflow_state_path": str(workflow_path),
                "debate_record_path": str(debate_record_path),
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
