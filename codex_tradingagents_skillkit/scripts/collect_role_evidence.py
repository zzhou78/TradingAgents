# ruff: noqa: E402

from __future__ import annotations

import argparse
import ast
import contextlib
import json
import re
import sys
from collections.abc import Callable
from datetime import datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

import yfinance as yf
from yfinance import cache as yf_cache

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = BUNDLE_ROOT.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from evidence_contracts import RoleExecutionContract, write_jsonl
from financial_document_evidence import (
    build_financial_document_evidence,
    collect_table_extraction_diagnostics,
    render_financial_metric_audit_review_csv,
    render_financial_metric_audit_review_markdown,
)
from financial_document_sources import (
    collect_financial_document_sources,
    render_financial_document_packet,
)
from fundamentals_evidence import build_fundamentals_evidence
from market_data_evidence import build_market_data_evidence
from news_article_evidence import build_news_evidence
from news_sources.orchestrator import collect_news_candidates
from social_evidence import build_social_evidence
from stage_input_evidence import build_stage_input_evidence

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

ARTICLE_FETCH_USER_AGENT = "CodexTradingAgentsSkillkit/0.1 (+paper-study evidence collection)"
ARTICLE_FETCH_MAX_BYTES = 1_000_000
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
DEFAULT_COMPANY_NEWS_URLS = {
    "AAPL": [
        "https://www.apple.com/newsroom/",
        "https://investor.apple.com/investor-relations/default.aspx",
    ],
    "MSFT": [
        "https://www.microsoft.com/en-us/Investor/press-releases",
        "https://news.microsoft.com/",
    ],
}
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

NEWS_MEMORY_UPDATE_SCHEMA = {
    "durable_facts_to_retain": ["string"],
    "prior_mistakes_to_avoid": ["string"],
    "open_questions": ["string"],
    "evidence_references": ["evidence_id"],
    "staleness_or_expiry": "string",
}

FINANCIAL_MEMORY_UPDATE_SCHEMA = {
    "durable_facts_to_retain": ["string"],
    "prior_mistakes_to_avoid": ["string"],
    "open_questions": ["string"],
    "evidence_references": ["evidence_id"],
    "staleness_or_expiry": "string",
}

MARKET_MEMORY_UPDATE_SCHEMA = {
    "durable_facts_to_retain": ["string"],
    "prior_mistakes_to_avoid": ["string"],
    "open_questions": ["string"],
    "evidence_references": ["evidence_id"],
    "staleness_or_expiry": "string",
}

GENERIC_MEMORY_UPDATE_SCHEMA = {
    "durable_facts_to_retain": ["string"],
    "prior_mistakes_to_avoid": ["string"],
    "open_questions": ["string"],
    "evidence_references": ["evidence_id"],
    "staleness_or_expiry": "string",
}

ROLE_CONTRACT_CONFIGS = {
    "sentiment_analyst": {
        "forbidden_inputs": [
            "future_social_posts",
            "raw_feed_dump_in_final_report",
            "institutional_sentiment_inference",
            "news_article_cards_as_independent_sentiment",
        ],
        "required_tools": ["fetch_stocktwits_messages", "social_evidence_processing"],
        "optional_tools": ["fetch_reddit_posts", "sentiment_source_status_review", "news_article_context_review"],
        "required_output_sections": [
            "Tool Outputs Used",
            "Sentiment Evidence Quality Summary",
            "Source Quality Table",
            "Top Reasoned Items",
            "Excluded / Downgraded Evidence",
            "Event Context vs Reaction Evidence",
            "Final Sentiment Interpretation",
            "Evidence Gaps",
            "Memory Update",
        ],
        "required_evidence_citations": [
            "evidence_id",
            "source",
            "source_confidence_category",
            "items_reviewed",
            "usable_ticker_relevant_items",
            "confidence",
            "independence_group_id",
        ],
        "quality_gate": "sentiment_social_evidence_gate",
    },
    "fundamentals_analyst": {
        "forbidden_inputs": ["future_filings", "uncited_memory", "unsupported_statement_values"],
        "required_tools": [
            "get_fundamentals",
            "get_balance_sheet",
            "get_cashflow",
            "get_income_statement",
            "fundamentals_statement_evidence",
        ],
        "optional_tools": ["sector_metric_adapter"],
        "required_output_sections": [
            "Tool Outputs Used",
            "Financial Statement Evidence",
            "Sector-Specific Metrics",
            "Evidence Gaps",
            "Memory Update",
        ],
        "required_evidence_citations": ["evidence_id", "source", "section_name", "supports_claims", "confidence"],
        "quality_gate": "fundamentals_statement_evidence_gate",
    },
    "industry_theme_discovery_analyst": {
        "forbidden_inputs": ["preconfigured_theme_without_evidence", "uncited_memory"],
        "required_tools": ["stage_input_evidence", "theme_evidence_link_validator"],
        "optional_tools": ["company_ir_search", "sector_source_search"],
        "required_output_sections": ["Tool Outputs Used", "Theme Evidence Table", "Evidence Gaps", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "theme", "subtheme", "evidence_link", "confidence"],
        "quality_gate": "industry_theme_evidence_gate",
    },
    "bull_researcher": {
        "forbidden_inputs": ["uncited_memory", "generic_bull_template"],
        "required_tools": ["stage_input_evidence", "strongest_evidence_selector"],
        "optional_tools": ["falsification_checklist"],
        "required_output_sections": ["Tool Outputs Used", "Strongest Bull Evidence", "Falsification Conditions", "Response To Bear", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "source_role", "materiality", "confidence"],
        "quality_gate": "bull_debate_evidence_gate",
    },
    "bear_researcher": {
        "forbidden_inputs": ["uncited_memory", "generic_bear_template"],
        "required_tools": ["stage_input_evidence", "strongest_evidence_selector"],
        "optional_tools": ["falsification_checklist"],
        "required_output_sections": ["Tool Outputs Used", "Strongest Bear Evidence", "Falsification Conditions", "Response To Bull", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "source_role", "materiality", "confidence"],
        "quality_gate": "bear_debate_evidence_gate",
    },
    "research_manager": {
        "forbidden_inputs": ["unexplained_rating_score", "uncited_memory", "double_counted_role_mentions"],
        "required_tools": ["stage_input_evidence", "evidence_matrix_validator"],
        "optional_tools": ["scoring_arithmetic_check"],
        "required_output_sections": [
            "Tool Outputs Used",
            "Structured Evidence Matrix",
            "Rating Rationale",
            "Debate Outcome Scorecard",
            "Debate Change Assessment",
            "Evidence Gaps",
            "Memory Update",
        ],
        "required_evidence_citations": [
            "evidence_id",
            "direction",
            "materiality",
            "confidence",
            "weight",
            "reason",
            "independence_group_id",
        ],
        "quality_gate": "research_manager_evidence_matrix_gate",
    },
    "trader": {
        "forbidden_inputs": ["live_order_tool", "broker_tool", "action_reasoning_mismatch"],
        "required_tools": ["stage_input_evidence", "trader_action_consistency_validator"],
        "optional_tools": ["paper_price_framework_check"],
        "required_output_sections": [
            "Tool Outputs Used",
            "Action Consistency Check",
            "Setup Quality Assessment",
            "Setup Thresholds",
            "Paper-study price framework",
            "FINAL TRANSACTION PROPOSAL",
            "Memory Update",
        ],
        "required_evidence_citations": ["evidence_id", "reference_price", "confirmation_level", "invalidation_level"],
        "quality_gate": "trader_action_consistency_gate",
    },
    "aggressive_risk_analyst": {
        "forbidden_inputs": ["unsupported_upside_template", "uncited_memory"],
        "required_tools": ["stage_input_evidence", "opportunity_risk_checklist"],
        "optional_tools": ["catalyst_sensitivity_check"],
        "required_output_sections": ["Tool Outputs Used", "Opportunity Case", "Failure Points", "Response To Prior Risk Arguments", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "upside_driver", "failure_point", "confidence"],
        "quality_gate": "aggressive_risk_evidence_gate",
    },
    "conservative_risk_analyst": {
        "forbidden_inputs": ["unsupported_downside_template", "uncited_memory"],
        "required_tools": ["stage_input_evidence", "downside_risk_checklist"],
        "optional_tools": ["drawdown_scenario_check"],
        "required_output_sections": ["Tool Outputs Used", "Downside Case", "Unsupported Upside Challenges", "Response To Aggressive", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "downside_driver", "evidence_gap", "confidence"],
        "quality_gate": "conservative_risk_evidence_gate",
    },
    "neutral_risk_analyst": {
        "forbidden_inputs": ["forced_compromise", "uncited_memory"],
        "required_tools": ["stage_input_evidence", "risk_argument_quality_comparison"],
        "optional_tools": ["risk_balance_matrix"],
        "required_output_sections": ["Tool Outputs Used", "Risk Argument Quality", "Stronger Risk Side", "Evidence Gaps", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "argument_quality", "confidence", "reason"],
        "quality_gate": "neutral_risk_evidence_gate",
    },
    "portfolio_manager": {
        "forbidden_inputs": ["trader_repeat_only", "broker_tool", "uncited_memory"],
        "required_tools": ["stage_input_evidence", "portfolio_decision_consistency_validator"],
        "optional_tools": ["risk_adjusted_decision_check"],
        "required_output_sections": ["Tool Outputs Used", "Risk debate impact", "Final Portfolio Decision", "Evidence Gaps", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "research_decision", "trader_action", "risk_debate_impact"],
        "quality_gate": "portfolio_decision_evidence_gate",
    },
    "quality_reviewer": {
        "forbidden_inputs": ["ignore_hard_validator_errors", "uncited_memory"],
        "required_tools": ["validate_quality_review", "stage_input_evidence", "evidence_ledger_consistency_check"],
        "optional_tools": ["complete_report_validator"],
        "required_output_sections": ["Tool Outputs Used", "Quality Gate Findings", "Evidence Gaps", "Memory Update"],
        "required_evidence_citations": ["evidence_id", "role_report", "validator_error", "required_fix"],
        "quality_gate": "quality_reviewer_gate",
    },
    "complete_report": {
        "forbidden_inputs": ["pending_role_output_as_complete", "uncited_memory"],
        "required_tools": ["stage_input_evidence", "complete_report_assembly_gate"],
        "optional_tools": ["validate_complete_report"],
        "required_output_sections": ["Tool Outputs Used", "Complete Report", "Evidence Gaps"],
        "required_evidence_citations": ["evidence_id", "role_report", "report_section"],
        "quality_gate": "complete_report_persistence_gate",
    },
}


def _news_role_execution_contract(
    *,
    allowed_inputs: list[str],
    allowed_memory: list[str] | None = None,
) -> dict[str, Any]:
    return RoleExecutionContract(
        role="news_analyst",
        allowed_inputs=allowed_inputs,
        forbidden_inputs=["future_articles", "uncited_memory", "raw_social_feed_as_news"],
        allowed_memory=allowed_memory or [],
        forbidden_memory=["other_role_memory", "other_ticker_memory"],
        required_tools=[
            "candidate_news_search",
            "news_article_evidence",
            "news_evidence_ledger_validator",
        ],
        optional_tools=["browser_full_text_check", "company_ir_search"],
        required_output_sections=[
            "Tool Outputs Used",
            "Article Evidence Cards",
            "News Impact Summary",
            "Evidence Gaps",
            "Memory Update",
        ],
        required_evidence_citations=[
            "evidence_id",
            "source_url",
            "source_date",
            "full_text_status",
        ],
        quality_gate="news_analyst_quality_gate",
        memory_update_schema=NEWS_MEMORY_UPDATE_SCHEMA,
    ).to_dict()


def _financial_role_execution_contract(
    *,
    allowed_inputs: list[str],
    allowed_memory: list[str] | None = None,
) -> dict[str, Any]:
    return RoleExecutionContract(
        role="financial_report_analyst",
        allowed_inputs=allowed_inputs,
        forbidden_inputs=["future_filings", "uncited_memory", "unsupported_management_commentary"],
        allowed_memory=allowed_memory or [],
        forbidden_memory=["other_role_memory", "other_ticker_memory"],
        required_tools=[
            "collect_financial_document_sources",
            "financial_document_evidence",
            "financial_claim_source_validator",
        ],
        optional_tools=["sec_filing_lookup", "asx_announcement_lookup", "company_ir_search", "pdf_text_extraction"],
        required_output_sections=[
            "Tool Outputs Used",
            "Source coverage table",
            "Claim-Source Table",
            "Evidence gaps",
            "Memory Update",
        ],
        required_evidence_citations=[
            "evidence_id",
            "source_type",
            "section_name",
            "filing_date",
            "evidence_gap",
        ],
        quality_gate="financial_report_claim_source_gate",
        memory_update_schema=FINANCIAL_MEMORY_UPDATE_SCHEMA,
    ).to_dict()


def _market_role_execution_contract(
    *,
    allowed_inputs: list[str],
    allowed_memory: list[str] | None = None,
) -> dict[str, Any]:
    return RoleExecutionContract(
        role="market_analyst",
        allowed_inputs=allowed_inputs,
        forbidden_inputs=["future_prices", "uncited_memory", "template_trend_claims"],
        allowed_memory=allowed_memory or [],
        forbidden_memory=["other_role_memory", "other_ticker_memory"],
        required_tools=[
            "get_verified_market_snapshot",
            "get_stock_data",
            "get_indicators",
            "market_data_evidence",
            "market_metric_consistency_validator",
        ],
        optional_tools=["market_calendar_check", "yfinance_cache_review"],
        required_output_sections=[
            "Tool Outputs Used",
            "Quantitative Regime / Tool Outputs",
            "Evidence Gaps",
            "Memory Update",
        ],
        required_evidence_citations=[
            "evidence_id",
            "metric_name",
            "value",
            "relation",
            "source_date",
        ],
        quality_gate="market_metric_consistency_gate",
        memory_update_schema=MARKET_MEMORY_UPDATE_SCHEMA,
    ).to_dict()


def _generic_role_execution_contract(
    *,
    role: str,
    allowed_inputs: list[str],
    allowed_memory: list[str] | None = None,
) -> dict[str, Any]:
    config = ROLE_CONTRACT_CONFIGS[role]
    return RoleExecutionContract(
        role=role,
        allowed_inputs=allowed_inputs,
        forbidden_inputs=config["forbidden_inputs"],
        allowed_memory=allowed_memory or [],
        forbidden_memory=["other_role_memory", "other_ticker_memory"],
        required_tools=config["required_tools"],
        optional_tools=config["optional_tools"],
        required_output_sections=config["required_output_sections"],
        required_evidence_citations=config["required_evidence_citations"],
        quality_gate=config["quality_gate"],
        memory_update_schema=GENERIC_MEMORY_UPDATE_SCHEMA,
    ).to_dict()


def _contract_role_for_stage(stage_name: str) -> str | None:
    if stage_name == "sentiment_analyst":
        return "sentiment_analyst"
    if stage_name == "fundamentals_analyst":
        return "fundamentals_analyst"
    if stage_name == "industry_theme_discovery_analyst":
        return "industry_theme_discovery_analyst"
    if stage_name.startswith("bull_researcher_round"):
        return "bull_researcher"
    if stage_name.startswith("bear_researcher_round"):
        return "bear_researcher"
    if stage_name == "research_manager":
        return "research_manager"
    if stage_name == "trader":
        return "trader"
    if stage_name.startswith("aggressive_risk_round"):
        return "aggressive_risk_analyst"
    if stage_name.startswith("conservative_risk_round"):
        return "conservative_risk_analyst"
    if stage_name.startswith("neutral_risk_round"):
        return "neutral_risk_analyst"
    if stage_name == "portfolio_manager":
        return "portfolio_manager"
    if stage_name == "complete_report":
        return "complete_report"
    if stage_name == "quality_review":
        return "quality_reviewer"
    return None


def _apply_stage_contract(stage: dict[str, Any]) -> None:
    if stage["stage"] == "news_analyst":
        stage["role_execution_contract"] = _news_role_execution_contract(
            allowed_inputs=stage["allowed_inputs"],
            allowed_memory=stage["allowed_memory_files"],
        )
        return
    if stage["stage"] == "market_analyst":
        stage["role_execution_contract"] = _market_role_execution_contract(
            allowed_inputs=stage["allowed_inputs"],
            allowed_memory=stage["allowed_memory_files"],
        )
        return
    if stage["stage"] == "financial_report_analyst":
        stage["role_execution_contract"] = _financial_role_execution_contract(
            allowed_inputs=stage["allowed_inputs"],
            allowed_memory=stage["allowed_memory_files"],
        )
        return
    contract_role = _contract_role_for_stage(stage["stage"])
    if contract_role:
        stage["role_execution_contract"] = _generic_role_execution_contract(
            role=contract_role,
            allowed_inputs=stage["allowed_inputs"],
            allowed_memory=stage["allowed_memory_files"],
        )


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


def _line_date(line: str) -> str | None:
    match = re.search(r"\[(\d{4}-\d{2}-\d{2})(?:T|\]|\s)", line)
    return match.group(1) if match else None


def _social_label_counts(lines: list[str]) -> tuple[int, int, int]:
    bullish = bearish = unlabeled = 0
    for line in lines:
        if "· Bullish]" in line:
            bullish += 1
        elif "· Bearish]" in line:
            bearish += 1
        elif "· no-label]" in line:
            unlabeled += 1
    return bullish, bearish, unlabeled


def _filter_social_output_as_of(call: dict[str, Any], trade_date: str) -> dict[str, Any]:
    if call.get("status") != "ok" or not call.get("output"):
        return call
    output = str(call["output"])
    kept_lines: list[str] = []
    removed = 0
    for line in output.splitlines():
        date = _line_date(line)
        if date and date > trade_date:
            removed += 1
            continue
        kept_lines.append(line)
    if not removed:
        return call

    if kept_lines and kept_lines[0].startswith("Bullish:"):
        message_lines = [line for line in kept_lines if _line_date(line)]
        bullish, bearish, unlabeled = _social_label_counts(message_lines)
        total = bullish + bearish + unlabeled
        bull_pct = round(100 * bullish / total) if total else 0
        bear_pct = round(100 * bearish / total) if total else 0
        kept_lines[0] = (
            f"Bullish: {bullish} ({bull_pct}%) · "
            f"Bearish: {bearish} ({bear_pct}%) · "
            f"Unlabeled: {unlabeled} · "
            f"Total: {total} messages on or before {trade_date}"
        )
    suffix = "item" if removed == 1 else "items"
    kept_lines.append(f"As-of filter: removed {removed} post-trade-date social {suffix} after {trade_date}.")
    call["output"] = "\n".join(kept_lines).strip()
    call.setdefault("as_of_filter", {})
    call["as_of_filter"] = {
        "trade_date": trade_date,
        "removed_post_trade_date_items": removed,
    }
    return call


class _ArticleBodyTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._skip_depth = 0
        self._capture_depth = 0
        self._chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg", "header", "footer", "nav", "aside"}:
            self._skip_depth += 1
            return
        if tag in {"article", "main", "p", "h1", "h2", "h3", "li"} and self._skip_depth == 0:
            self._capture_depth += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg", "header", "footer", "nav", "aside"}:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if tag in {"article", "main", "p", "h1", "h2", "h3", "li"} and self._capture_depth:
            self._capture_depth -= 1
            if self._chunks and self._chunks[-1] != "\n":
                self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth or not self._capture_depth:
            return
        text = re.sub(r"\s+", " ", data).strip()
        if text:
            self._chunks.append(text)

    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self._chunks)).strip()


def _extract_article_full_text_from_html(html: str) -> str:
    parser = _ArticleBodyTextParser()
    parser.feed(html)
    return parser.text()


def _fetch_article_full_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": ARTICLE_FETCH_USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with contextlib.closing(urlopen(request, timeout=8)) as response:
        content_type = str(response.headers.get("Content-Type", ""))
        if "html" not in content_type.lower():
            return ""
        raw = response.read(ARTICLE_FETCH_MAX_BYTES)
        charset = response.headers.get_content_charset() or "utf-8"
    return _extract_article_full_text_from_html(raw.decode(charset, errors="replace"))


def _candidate_from_mapping(payload: dict[str, Any]) -> dict[str, str]:
    title = payload.get("title") or payload.get("headline") or payload.get("name") or ""
    source = payload.get("source") or payload.get("publisher") or payload.get("site") or ""
    if isinstance(source, dict):
        source = source.get("name") or source.get("publisher") or ""
    url = payload.get("url") or payload.get("link") or payload.get("article_url") or ""
    published_date = (
        payload.get("published_date")
        or payload.get("date")
        or payload.get("published")
        or payload.get("datetime")
        or payload.get("time_published")
        or ""
    )
    if published_date:
        published_date = str(published_date)[:10]
    snippet = payload.get("snippet") or payload.get("summary") or payload.get("description") or ""
    full_text = payload.get("full_text") or payload.get("content") or payload.get("body") or ""
    return {
        "title": str(title).strip(),
        "source": str(source).strip(),
        "url": str(url).strip(),
        "published_date": str(published_date).strip(),
        "snippet": str(snippet).strip(),
        "full_text": str(full_text).strip(),
    }


def _fallback_candidates_from_text(
    text: str,
    *,
    default_source: str = "",
    default_date: str = "",
) -> list[dict[str, str]]:
    if re.search(r"\bNo .*news found\b", text, re.IGNORECASE):
        return []
    candidates: list[dict[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip(" -\t")
        if not line:
            continue
        url_match = re.search(r"https?://\S+", line)
        date_match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", line)
        title = line
        if url_match:
            title = title.replace(url_match.group(0), "").strip(" -|")
        if date_match:
            title = title.replace(date_match.group(1), "").strip(" -|")
        if not title:
            title = line[:120]
        candidates.append(
            {
                "title": title[:240],
                "source": default_source,
                "url": url_match.group(0) if url_match else "",
                "published_date": date_match.group(1) if date_match else default_date,
                "snippet": line,
                "full_text": "",
            }
        )
    return candidates


def _markdown_news_candidates(text: str, *, default_source: str, default_date: str) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    blocks = re.split(r"(?=^###\s+)", text, flags=re.MULTILINE)
    for block in blocks:
        block = block.strip()
        if not block.startswith("### "):
            continue
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        header = lines[0].removeprefix("###").strip()
        source = default_source
        source_match = re.search(r"\(source:\s*([^)]+)\)\s*$", header)
        if source_match:
            source = source_match.group(1).strip()
            header = header[: source_match.start()].strip()
        url = ""
        snippet_lines: list[str] = []
        for line in lines[1:]:
            if line.lower().startswith("link:"):
                url = line.split(":", 1)[1].strip()
            elif not line.startswith("###"):
                snippet_lines.append(line)
        if not header or header.lower().startswith("link:"):
            continue
        candidates.append(
            {
                "title": header,
                "source": source,
                "url": url,
                "published_date": default_date,
                "snippet": " ".join(snippet_lines).strip(),
                "full_text": "",
            }
        )
    return candidates


def _extract_news_candidates_from_call(
    call: dict[str, Any],
    *,
    default_source: str,
    default_date: str,
) -> list[dict[str, str]]:
    if call.get("status") != "ok" or not call.get("output"):
        return []
    output = str(call["output"])
    markdown_candidates = _markdown_news_candidates(
        output,
        default_source=default_source,
        default_date=default_date,
    )
    if markdown_candidates:
        return markdown_candidates
    parsed: Any | None = None
    try:
        parsed = json.loads(output)
    except json.JSONDecodeError:
        try:
            parsed = ast.literal_eval(output)
        except (ValueError, SyntaxError):
            parsed = None

    records: list[Any]
    if isinstance(parsed, list):
        records = parsed
    elif isinstance(parsed, dict):
        for key in ("articles", "news", "items", "results"):
            if isinstance(parsed.get(key), list):
                records = parsed[key]
                break
        else:
            records = [parsed]
    else:
        return _fallback_candidates_from_text(output, default_source=default_source, default_date=default_date)

    candidates = [
        _candidate_from_mapping(record)
        for record in records
        if isinstance(record, dict)
    ]
    return [candidate for candidate in candidates if candidate["title"] or candidate["url"]]


def _news_candidates_from_calls(calls: dict[str, dict[str, Any]], *, trade_date: str) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    for tool_name in ("get_news", "get_global_news"):
        candidates.extend(
            _extract_news_candidates_from_call(
                calls.get(tool_name, {}),
                default_source=tool_name,
                default_date=trade_date,
            )
        )
    return candidates


def _company_ir_urls(ticker: str, identity: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    urls.extend(DEFAULT_COMPANY_NEWS_URLS.get(ticker.upper(), []))
    for key in (
        "investor_relations_url",
        "investorRelationsUrl",
        "ir_url",
        "investors_url",
        "press_releases_url",
        "news_url",
    ):
        value = identity.get(key)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            urls.append(value)
    return list(dict.fromkeys(urls))


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
    for key in ("fetch_stocktwits_messages", "fetch_reddit_posts"):
        calls[key] = _filter_social_output_as_of(calls[key], trade_date)
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
        "structured_packet": packet,
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
    role_evidence_paths: dict[str, list[str]] | None = None,
    run_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    memory_map = memory_map or _ensure_role_memories(ticker, trade_date)
    role_evidence_paths = role_evidence_paths or {}
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
        allowed_inputs = [role_packet_paths[role], *role_evidence_paths.get(role, [])]
        stage = _attach_memory_contract(
            {
                "stage": stage_name,
                "skill": ROLE_SKILLS[role],
                "allowed_inputs": allowed_inputs,
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
        _apply_stage_contract(stage)
        stages.append(stage)

    analyst_outputs = [
        paths["sentiment_report" if role == "social" else f"{role}_report"]
        for role in selected_analysts
    ]
    financial_allowed_inputs = (
        analyst_outputs
        + [role_packet_paths[FINANCIAL_REPORT_ROLE], str(evidence_path)]
        + role_evidence_paths.get(FINANCIAL_REPORT_ROLE, [])
    )
    financial_stage = _attach_memory_contract(
        {
            "stage": "financial_report_analyst",
            "skill": "tradingagents-financial-report-analyst",
            "allowed_inputs": financial_allowed_inputs,
            "forbidden_inputs": [],
            "output_path": paths["financial_report"],
            "completion_gate": "write financial_report.md before industry/theme discovery",
        },
        ticker=ticker,
        memory_map=memory_map,
        report_dir=report_dir,
    )
    _apply_stage_contract(financial_stage)
    stages.append(financial_stage)
    analyst_outputs.append(paths["financial_report"])
    theme_stage = _attach_memory_contract(
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
    _apply_stage_contract(theme_stage)
    stages.append(theme_stage)
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
        downstream_stage = _attach_memory_contract(
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
        _apply_stage_contract(downstream_stage)
        stages.append(downstream_stage)
    complete_report_inputs = analyst_outputs + [
        paths[stage_name]
        for stage_name, _, _ in downstream
    ]
    complete_stage = _attach_memory_contract(
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
    _apply_stage_contract(complete_stage)
    stages.append(complete_stage)
    quality_stage = _attach_memory_contract(
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
    _apply_stage_contract(quality_stage)
    stages.append(quality_stage)

    run_metadata = run_metadata or {
        "trade_date": trade_date,
        "evidence_as_of_date": trade_date,
        "run_executed_at": "",
        "output_dir": str(report_dir.parents[2]) if len(report_dir.parents) > 2 else "",
        "run_folder_name": report_dir.parents[2].name if len(report_dir.parents) > 2 else "",
        "ticker_list": [ticker],
        "run_id": "",
        "authoritative_result_folder": False,
        "authoritative_result_folder_path": str(report_dir.parents[2]) if len(report_dir.parents) > 2 else "",
        "status": "pending",
        "workflow_status": "pending",
    }
    return {
        "ticker": ticker,
        "trade_date": trade_date,
        "evidence_as_of_date": run_metadata.get("evidence_as_of_date", trade_date),
        "run_executed_at": run_metadata.get("run_executed_at", ""),
        "output_dir": run_metadata.get("output_dir", ""),
        "run_folder_name": run_metadata.get("run_folder_name", ""),
        "run_id": run_metadata.get("run_id", ""),
        "authoritative_result_folder": bool(run_metadata.get("authoritative_result_folder")),
        "status": run_metadata.get("status", "pending"),
        "workflow_status": run_metadata.get("workflow_status", run_metadata.get("status", "pending")),
        "run_metadata": run_metadata,
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


def _write_stage_input_evidence(workflow: dict[str, Any], evidence_dir: Path) -> None:
    retrieval_time = datetime.now().astimezone().isoformat(timespec="seconds")
    for stage in workflow["stages"]:
        contract = stage.get("role_execution_contract", {})
        if "stage_input_evidence" not in contract.get("required_tools", []):
            continue
        stage_dir = evidence_dir / "stage_inputs" / stage["stage"]
        stage_dir.mkdir(parents=True, exist_ok=True)
        input_records_path = stage_dir / "input_records.json"
        ledger_path = stage_dir / "evidence_ledger.jsonl"
        base_inputs = list(stage["allowed_inputs"])
        stage_evidence = build_stage_input_evidence(
            ticker=workflow["ticker"],
            trade_date=workflow["trade_date"],
            role=contract["role"],
            allowed_inputs=base_inputs,
            structured_output_path=str(input_records_path),
            retrieval_time=retrieval_time,
        )
        input_records_path.write_text(
            json.dumps(stage_evidence["input_records"], indent=2),
            encoding="utf-8",
        )
        write_jsonl(ledger_path, stage_evidence["ledger_entries"])
        stage["allowed_inputs"] = [*base_inputs, str(input_records_path), str(ledger_path)]
        _apply_stage_contract(stage)


def _is_authoritative_result_folder(output_dir: Path, trade_date: str) -> bool:
    return trade_date in output_dir.name


def _run_folder_metadata(
    *,
    output_dir: Path,
    tickers: list[str],
    trade_date: str,
    run_executed_at: str,
    workflow_status: str = "pending",
) -> dict[str, Any]:
    market = _run_market(tickers)
    return {
        "run_id": f"{output_dir.name}:{','.join(tickers)}:{trade_date}:{run_executed_at}",
        "run_folder_name": output_dir.name,
        "ticker_list": tickers,
        "market": market,
        "trade_date": trade_date,
        "evidence_as_of_date": trade_date,
        "run_executed_at": run_executed_at,
        "authoritative_result_folder": str(output_dir),
        "workflow_status": workflow_status,
    }


def _run_market(tickers: list[str]) -> str:
    symbols = [ticker.upper().strip() for ticker in tickers]
    if symbols and all(symbol.endswith(".AX") for symbol in symbols):
        return "ASX"
    if symbols and all("." not in symbol for symbol in symbols):
        return "US"
    return "mixed"


def _run_metadata(
    *,
    ticker: str,
    tickers: list[str],
    trade_date: str,
    output_dir: Path,
    run_executed_at: str,
    status: str = "pending",
) -> dict[str, Any]:
    market = _run_market(tickers)
    return {
        "trade_date": trade_date,
        "evidence_as_of_date": trade_date,
        "run_executed_at": run_executed_at,
        "output_dir": str(output_dir),
        "market": market,
        "run_folder_name": output_dir.name,
        "ticker_list": tickers,
        "run_id": f"{output_dir.name}:{ticker}:{trade_date}:{run_executed_at}",
        "authoritative_result_folder": _is_authoritative_result_folder(output_dir, trade_date),
        "authoritative_result_folder_path": str(output_dir),
        "status": status,
        "workflow_status": status,
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
    run_executed_at = datetime.now().astimezone().isoformat(timespec="seconds")
    run_folder_metadata = _run_folder_metadata(
        output_dir=output_dir,
        tickers=tickers,
        trade_date=args.trade_date,
        run_executed_at=run_executed_at,
    )
    run_metadata_path = output_dir / "run_metadata.json"
    run_metadata_path.write_text(json.dumps(run_folder_metadata, indent=2), encoding="utf-8")

    summary = {
        "trade_date": args.trade_date,
        "evidence_as_of_date": args.trade_date,
        "run_executed_at": run_executed_at,
        "market": run_folder_metadata["market"],
        "selected_analysts": selected_analysts,
        "max_debate_rounds": max_debate_rounds,
        "max_risk_discuss_rounds": max_risk_discuss_rounds,
        "output_dir": str(output_dir),
        "run_folder_name": output_dir.name,
        "run_metadata_path": str(run_metadata_path),
        "authoritative_result_folder": _is_authoritative_result_folder(output_dir, args.trade_date),
        "status": "pending",
        "workflow_status": "pending",
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
        run_metadata = _run_metadata(
            ticker=ticker,
            tickers=tickers,
            trade_date=args.trade_date,
            output_dir=output_dir,
            run_executed_at=run_executed_at,
        )
        evidence_dir = output_dir / "evidence" / ticker / args.trade_date
        evidence_dir.mkdir(parents=True, exist_ok=True)
        identity = resolve_instrument_identity(ticker)
        evidence = {
            "ticker": ticker,
            "trade_date": args.trade_date,
            "evidence_as_of_date": args.trade_date,
            "run_executed_at": run_executed_at,
            "output_dir": str(output_dir),
            "run_id": run_metadata["run_id"],
            "authoritative_result_folder": run_metadata["authoritative_result_folder"],
            "status": run_metadata["status"],
            "run_metadata": run_metadata,
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
        role_evidence_paths: dict[str, list[str]] = {}
        if "market" in evidence["roles"]:
            market_dir = evidence_dir / "market"
            market_dir.mkdir(exist_ok=True)
            observations_path = market_dir / "quantitative_observations.json"
            market_ledger_path = market_dir / "evidence_ledger.jsonl"
            market_evidence = build_market_data_evidence(
                ticker=ticker,
                trade_date=args.trade_date,
                tool_calls=evidence["roles"]["market"]["tool_calls"],
                structured_output_path=str(observations_path),
                retrieval_time=datetime.now().astimezone().isoformat(timespec="seconds"),
            )
            observations_path.write_text(
                json.dumps(market_evidence["metric_observations"], indent=2),
                encoding="utf-8",
            )
            write_jsonl(market_ledger_path, market_evidence["ledger_entries"])
            role_evidence_paths["market"] = [str(observations_path), str(market_ledger_path)]
            evidence["roles"]["market"]["structured_evidence"] = {
                "metric_observations": str(observations_path),
                "evidence_ledger": str(market_ledger_path),
                "tool_name": "market_data_evidence",
            }
        if "news" in evidence["roles"]:
            news_dir = evidence_dir / "news"
            news_dir.mkdir(exist_ok=True)
            news_candidates = collect_news_candidates(
                ticker=ticker,
                company_name=str(identity.get("company_name") or ticker),
                trade_date=args.trade_date,
                lookback_days=args.lookback_days,
                approved_sources=["company_ir", "regulatory", "websearch", "newsapi", "rss", "upstream"],
                company_ir_urls=_company_ir_urls(ticker, identity),
                upstream_calls=evidence["roles"]["news"]["tool_calls"],
                financial_sources=evidence["roles"][FINANCIAL_REPORT_ROLE]["structured_packet"].get("sources", []),
                output_dir=news_dir,
            )
            article_cards_path = news_dir / "article_cards.json"
            source_ledger_path = news_dir / "source_evidence_ledger.jsonl"
            article_ledger_path = news_dir / "evidence_ledger.jsonl"
            generated_source_ledger_path = news_dir / "evidence_ledger.jsonl"
            if generated_source_ledger_path.exists():
                source_ledger_path.write_text(generated_source_ledger_path.read_text(encoding="utf-8"), encoding="utf-8")
            news_evidence = build_news_evidence(
                ticker=ticker,
                trade_date=args.trade_date,
                candidates=news_candidates["candidates"],
                structured_output_path=str(article_cards_path),
                retrieval_time=datetime.now().astimezone().isoformat(timespec="seconds"),
                full_text_fetcher=_fetch_article_full_text,
            )
            article_cards_path.write_text(
                json.dumps(news_evidence["article_cards"], indent=2),
                encoding="utf-8",
            )
            write_jsonl(article_ledger_path, news_evidence["ledger_entries"])
            role_evidence_paths["news"] = [
                str(news_dir / "candidates.json"),
                str(news_dir / "source_attempts.json"),
                str(source_ledger_path),
                str(article_cards_path),
                str(article_ledger_path),
            ]
            evidence["roles"]["news"]["structured_evidence"] = {
                "candidates": str(news_dir / "candidates.json"),
                "source_attempts": str(news_dir / "source_attempts.json"),
                "source_evidence_ledger": str(source_ledger_path),
                "article_cards": str(article_cards_path),
                "evidence_ledger": str(article_ledger_path),
                "tool_name": "news_article_evidence",
            }
        if "social" in evidence["roles"]:
            social_dir = evidence_dir / "social"
            social_dir.mkdir(exist_ok=True)
            social_summary_path = social_dir / "social_summary.json"
            social_cards_path = social_dir / "social_cards.json"
            social_ledger_path = social_dir / "evidence_ledger.jsonl"
            social_evidence = build_social_evidence(
                ticker=ticker,
                trade_date=args.trade_date,
                tool_calls=evidence["roles"]["social"]["tool_calls"],
                structured_output_path=str(social_summary_path),
                retrieval_time=datetime.now().astimezone().isoformat(timespec="seconds"),
            )
            social_summary_path.write_text(
                json.dumps(
                    {
                        "social_summary": social_evidence["social_summary"],
                        "sources": social_evidence["sources"],
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
            social_cards_path.write_text(json.dumps(social_evidence["social_cards"], indent=2), encoding="utf-8")
            write_jsonl(social_ledger_path, social_evidence["ledger_entries"])
            role_evidence_paths["social"] = [str(social_summary_path), str(social_cards_path), str(social_ledger_path)]
            evidence["roles"]["social"]["structured_evidence"] = {
                "social_summary": str(social_summary_path),
                "social_cards": str(social_cards_path),
                "evidence_ledger": str(social_ledger_path),
                "tool_name": "social_evidence_processing",
            }
        if "fundamentals" in evidence["roles"]:
            fundamentals_dir = evidence_dir / "fundamentals"
            fundamentals_dir.mkdir(exist_ok=True)
            statement_records_path = fundamentals_dir / "statement_records.json"
            fundamentals_ledger_path = fundamentals_dir / "evidence_ledger.jsonl"
            fundamentals_evidence = build_fundamentals_evidence(
                ticker=ticker,
                trade_date=args.trade_date,
                identity=identity,
                tool_calls=evidence["roles"]["fundamentals"]["tool_calls"],
                structured_output_path=str(statement_records_path),
                retrieval_time=datetime.now().astimezone().isoformat(timespec="seconds"),
            )
            statement_records_path.write_text(
                json.dumps(fundamentals_evidence["statement_records"], indent=2),
                encoding="utf-8",
            )
            write_jsonl(fundamentals_ledger_path, fundamentals_evidence["ledger_entries"])
            role_evidence_paths["fundamentals"] = [str(statement_records_path), str(fundamentals_ledger_path)]
            evidence["roles"]["fundamentals"]["structured_evidence"] = {
                "statement_records": str(statement_records_path),
                "evidence_ledger": str(fundamentals_ledger_path),
                "tool_name": "fundamentals_statement_evidence",
            }
        financial_dir = evidence_dir / "financial_report"
        financial_dir.mkdir(exist_ok=True)
        financial_section_records_path = financial_dir / "section_records.json"
        financial_ledger_path = financial_dir / "evidence_ledger.jsonl"
        financial_metric_review_md_path = financial_dir / "asx_metric_audit_review.md"
        financial_metric_review_csv_path = financial_dir / "asx_metric_audit_review.csv"
        financial_table_diagnostics_path = financial_dir / "asx_table_extraction_diagnostics.json"
        financial_packet = evidence["roles"][FINANCIAL_REPORT_ROLE].get("structured_packet", {})
        financial_evidence = build_financial_document_evidence(
            ticker=ticker,
            trade_date=args.trade_date,
            packet=financial_packet,
            structured_output_path=str(financial_section_records_path),
            retrieval_time=datetime.now().astimezone().isoformat(timespec="seconds"),
        )
        financial_section_records_path.write_text(
            json.dumps(financial_evidence["section_records"], indent=2),
            encoding="utf-8",
        )
        write_jsonl(financial_ledger_path, financial_evidence["ledger_entries"])
        financial_metric_review_md_path.write_text(
            render_financial_metric_audit_review_markdown(financial_evidence["section_records"]),
            encoding="utf-8",
        )
        financial_metric_review_csv_path.write_text(
            render_financial_metric_audit_review_csv(financial_evidence["section_records"]),
            encoding="utf-8",
        )
        financial_table_diagnostics_path.write_text(
            json.dumps(collect_table_extraction_diagnostics(financial_packet), indent=2),
            encoding="utf-8",
        )
        role_evidence_paths[FINANCIAL_REPORT_ROLE] = [
            str(financial_section_records_path),
            str(financial_ledger_path),
            str(financial_metric_review_md_path),
            str(financial_metric_review_csv_path),
            str(financial_table_diagnostics_path),
        ]
        evidence["roles"][FINANCIAL_REPORT_ROLE]["structured_evidence"] = {
            "section_records": str(financial_section_records_path),
            "evidence_ledger": str(financial_ledger_path),
            "asx_metric_audit_review": str(financial_metric_review_md_path),
            "asx_metric_audit_review_csv": str(financial_metric_review_csv_path),
            "asx_table_extraction_diagnostics": str(financial_table_diagnostics_path),
            "tool_name": "financial_document_evidence",
        }
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
            role_evidence_paths=role_evidence_paths,
            run_metadata=run_metadata,
        )
        _write_stage_input_evidence(workflow, evidence_dir)
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
                "run_metadata": run_metadata,
                "status": run_metadata["status"],
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
