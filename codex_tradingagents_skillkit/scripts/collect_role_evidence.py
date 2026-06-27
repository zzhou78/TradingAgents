from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable

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
WORKFLOW_SKILLS = [
    "tradingagents-workflow-orchestrator",
    "tradingagents-analyst-sequencing",
    "tradingagents-dataflow-routing",
]


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
        if hasattr(func, "invoke"):
            value = func.invoke(kwargs)
        else:
            value = func(**kwargs)
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


def collect(args: argparse.Namespace) -> dict[str, Any]:
    selected_analysts = _parse_analysts(args.selected_analysts)
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
        summary["runs"].append(
            {
                "ticker": ticker,
                "evidence_path": str(evidence_path),
                "role_packet_path": str(packet_path),
                "role_packet_paths": role_packet_paths,
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
