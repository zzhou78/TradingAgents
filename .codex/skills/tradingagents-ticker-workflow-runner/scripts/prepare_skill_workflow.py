from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_ANALYSTS = ["market", "social", "news", "fundamentals"]
VALID_ANALYSTS = set(DEFAULT_ANALYSTS)
WORKFLOW_SKILLS = [
    "tradingagents-workflow-orchestrator",
    "tradingagents-analyst-sequencing",
    "tradingagents-dataflow-routing",
    "tradingagents-debate-routing",
    "tradingagents-run-persistence",
]
ROLE_SKILLS = [
    "tradingagents-market-analyst",
    "tradingagents-sentiment-analyst",
    "tradingagents-news-analyst",
    "tradingagents-fundamentals-analyst",
    "tradingagents-bull-researcher",
    "tradingagents-bear-researcher",
    "tradingagents-research-manager",
    "tradingagents-trader",
    "tradingagents-aggressive-risk-analyst",
    "tradingagents-conservative-risk-analyst",
    "tradingagents-neutral-risk-analyst",
    "tradingagents-portfolio-manager",
]
REPORT_KEYS = [
    "market_report",
    "sentiment_report",
    "news_report",
    "fundamentals_report",
    "investment_plan",
    "trader_investment_plan",
    "final_trade_decision",
]


@dataclass(frozen=True)
class TickerRun:
    ticker: str
    asset_type: str
    output_slug: str


def _split_tickers(raw: str) -> list[str]:
    return [part.strip().upper() for part in raw.replace("\n", ",").split(",") if part.strip()]


def _read_ticker_file(path: Path) -> list[str]:
    chunks: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        chunks.append(stripped)
    return _split_tickers(",".join(chunks))


def _safe_slug(ticker: str) -> str:
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._=+-")
    cleaned = "".join(ch for ch in ticker.upper() if ch in allowed)
    if not cleaned or cleaned.strip(".") == "":
        raise ValueError(f"invalid ticker for output path: {ticker!r}")
    return cleaned[:32]


def _asset_type(ticker: str, requested: str) -> str:
    if requested != "auto":
        return requested
    upper = ticker.upper()
    if upper.endswith("-USD") or upper.endswith("USDT") or upper in {"BTC", "ETH", "SOL"}:
        return "crypto"
    return "stock"


def _parse_analysts(raw: str) -> list[str]:
    analysts = [item.strip().lower() for item in raw.split(",") if item.strip()]
    unknown = [item for item in analysts if item not in VALID_ANALYSTS]
    if unknown:
        raise ValueError(f"unknown selected analyst key(s): {', '.join(unknown)}")
    if not analysts:
        raise ValueError("at least one analyst must be selected")
    return analysts


def build_packet(args: argparse.Namespace) -> dict:
    datetime.strptime(args.trade_date, "%Y-%m-%d")
    tickers: list[str] = []
    for raw in args.ticker:
        tickers.extend(_split_tickers(raw))
    for ticker_file in args.tickers_file:
        tickers.extend(_read_ticker_file(ticker_file))

    deduped = list(dict.fromkeys(tickers))
    if not deduped:
        raise ValueError("provide at least one ticker through --ticker or --tickers-file")

    selected_analysts = _parse_analysts(args.selected_analysts)
    runs = [
        TickerRun(
            ticker=ticker,
            asset_type=_asset_type(ticker, args.asset_type),
            output_slug=_safe_slug(ticker),
        )
        for ticker in deduped
    ]

    return {
        "trade_date": args.trade_date,
        "selected_analysts": selected_analysts,
        "workflow_skills": WORKFLOW_SKILLS,
        "role_skills": ROLE_SKILLS,
        "report_keys": REPORT_KEYS,
        "runs": [asdict(run) for run in runs],
        "safety_boundaries": [
            "paper-study workflow only",
            "do not run live LLM or market-data calls without explicit approval",
            "do not submit broker orders",
            "do not connect to GCAF",
        ],
    }


def format_markdown(packet: dict) -> str:
    lines = [
        "# TradingAgents Skill Workflow Packet",
        "",
        f"- Trade date: `{packet['trade_date']}`",
        f"- Selected analysts: `{', '.join(packet['selected_analysts'])}`",
        "",
        "## Tickers",
    ]
    for run in packet["runs"]:
        lines.append(f"- `{run['ticker']}` ({run['asset_type']}) -> `{run['output_slug']}`")
    lines.extend(["", "## Workflow Skills"])
    lines.extend(f"- `{skill}`" for skill in packet["workflow_skills"])
    lines.extend(["", "## Role Skills"])
    lines.extend(f"- `{skill}`" for skill in packet["role_skills"])
    lines.extend(["", "## Safety Boundaries"])
    lines.extend(f"- {item}" for item in packet["safety_boundaries"])
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare a TradingAgents skill workflow packet.")
    parser.add_argument("--ticker", action="append", default=[], help="Ticker or comma-separated tickers.")
    parser.add_argument("--tickers-file", action="append", type=Path, default=[], help="File with newline or comma-separated tickers.")
    parser.add_argument("--trade-date", required=True, help="Analysis date in YYYY-MM-DD format.")
    parser.add_argument("--asset-type", choices=["auto", "stock", "crypto"], default="auto")
    parser.add_argument("--selected-analysts", default=",".join(DEFAULT_ANALYSTS), help="Comma-separated analyst keys.")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        packet = build_packet(args)
    except Exception as exc:
        raise SystemExit(str(exc)) from exc

    if args.format == "json":
        print(json.dumps(packet, indent=2))
    else:
        print(format_markdown(packet), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
