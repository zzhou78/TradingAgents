from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
SKILLS_ROOT = BUNDLE / "skills"
VALIDATOR = BUNDLE / "scripts" / "validate_complete_report.py"
WRITER = BUNDLE / "scripts" / "write_codex_reports.py"
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
    "tradingagents-fundamentals-analyst",
    "tradingagents-market-analyst",
    "tradingagents-neutral-risk-analyst",
    "tradingagents-news-analyst",
    "tradingagents-portfolio-manager",
    "tradingagents-research-manager",
    "tradingagents-run-persistence",
    "tradingagents-sentiment-analyst",
    "tradingagents-ticker-workflow-runner",
    "tradingagents-trader",
    "tradingagents-workflow-orchestrator",
]


def _load_writer():
    spec = importlib.util.spec_from_file_location("write_codex_reports", WRITER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _snapshot(close: float, ema10: float, sma50: float, sma200: float, rsi: float, macd: float, macds: float) -> str:
    return f"""## Verified market data snapshot

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Close | {close:.2f} |
| Volume | 1000 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | {ema10:.2f} |
| close_50_sma | {sma50:.2f} |
| close_200_sma | {sma200:.2f} |
| rsi | {rsi:.2f} |
| macd | {macd:.2f} |
| macds | {macds:.2f} |
| atr | 1.00 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-06-26 | {close:.2f} |
"""


def _evidence(
    ticker: str,
    *,
    close: float,
    ema10: float,
    sma50: float,
    sma200: float,
    rsi: float,
    macd: float,
    macds: float,
    pe: float,
    pb: float = 2.0,
    news: str = "",
    stocktwits: str = "",
) -> dict[str, object]:
    return {
        "ticker": ticker,
        "trade_date": "2026-06-27",
        "identity": {"company_name": f"{ticker} Company"},
        "roles": {
            "market": {
                "tool_calls": {
                    "get_verified_market_snapshot": {
                        "output": _snapshot(close, ema10, sma50, sma200, rsi, macd, macds)
                    },
                    "get_stock_data": {"output": "Date,Open,High,Low,Close,Volume,Dividends,Stock Splits\n"},
                }
            },
            "social": {
                "tool_calls": {
                    "fetch_stocktwits_messages": {"output": stocktwits},
                    "fetch_reddit_posts": {"output": ""},
                }
            },
            "news": {"tool_calls": {"get_news": {"output": news}}},
            "fundamentals": {
                "tool_calls": {
                    "get_fundamentals": {
                        "output": "\n".join(
                            [
                                "Market Cap: 1000000000",
                                "Revenue (TTM): 200000000",
                                "Net Income: 30000000",
                                "Free Cash Flow: 25000000",
                                f"PE Ratio (TTM): {pe}",
                                "Forward PE: 20",
                                f"Price to Book: {pb}",
                                "Return on Equity: 0.30",
                            ]
                        )
                    },
                    "get_cashflow": {"output": "NO_DATA_AVAILABLE"},
                    "get_income_statement": {"output": "NO_DATA_AVAILABLE"},
                }
            },
        },
    }


def test_bundle_has_expected_skills_and_docs():
    assert (BUNDLE / "README.md").exists()
    assert (BUNDLE / "MANIFEST.md").exists()
    assert (BUNDLE / "scripts" / "collect_role_evidence.py").exists()
    assert (BUNDLE / "scripts" / "write_codex_reports.py").exists()
    assert VALIDATOR.exists()
    assert (BUNDLE / "docs" / "STUDY_LOCAL_SETUP_AND_SAFETY_REVIEW.md").exists()
    assert (BUNDLE / "docs" / "ARCHITECTURE_LEARNING_NOTES.md").exists()

    readme = (BUNDLE / "README.md").read_text(encoding="utf-8")
    manifest = (BUNDLE / "MANIFEST.md").read_text(encoding="utf-8")
    assert "Real data retrieval and processing still uses upstream Python" in readme
    assert "Codex acts each TradingAgents role using the converted skills" in readme
    assert "not a vendored runtime distribution" in manifest
    assert "collect_role_evidence.py" in manifest
    assert "write_codex_reports.py" in manifest
    assert "validate_complete_report.py" in manifest
    assert "--ticker AAPL,MSFT" in readme

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
    assert payload["runs"][0]["asset_type"] == "stock"
    assert payload["runs"][1]["asset_type"] == "stock"
    assert "tradingagents-workflow-orchestrator" in payload["workflow_skills"]
    assert "tradingagents-dataflow-routing" in payload["workflow_skills"]


def test_trader_skill_preserves_original_transaction_contract():
    text = (SKILLS_ROOT / "tradingagents-trader" / "SKILL.md").read_text(encoding="utf-8")

    assert "Buy / Hold / Sell" in text
    assert "Optional entry price" in text
    assert "Optional stop loss" in text
    assert "Optional position sizing note" in text
    assert "FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**" in text
    assert "Safety boundaries must not change the Buy / Hold / Sell action." in text
    assert "Do not cite paper-study status as a reason to avoid Buy or Sell." in text
    assert "The action rationale must come from market evidence, research manager input, and risk evidence." in text


def test_debate_and_complete_report_docs_make_debate_turns_visible():
    debate = (SKILLS_ROOT / "tradingagents-debate-routing" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    persistence = (SKILLS_ROOT / "tradingagents-run-persistence" / "SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "Codex-visible debate rendering" in debate
    for required in [
        "Bear must directly respond to Bull.",
        "Research Manager must explicitly weigh Bull vs Bear.",
        "Conservative Risk must directly respond to Aggressive Risk.",
        "Neutral Risk must explicitly weigh Aggressive vs Conservative.",
        "Portfolio Manager must synthesize the risk debate.",
        "Documentation alone is not sufficient.",
    ]:
        assert required in debate

    for section in [
        "I. Analyst Team Reports",
        "II. Research Team Debate",
        "Bull Researcher Round 1 - Opening Case",
        "Bear Researcher Round 1 - Rebuttal to Bull",
        "Research Manager Decision - Evidence Weighing",
        "III. Trading Team Plan",
        "FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**",
        "IV. Risk Management Team Debate",
        "Aggressive Risk Analyst Round 1 - Opportunity Case",
        "Conservative Risk Analyst Round 1 - Response to Aggressive",
        "Neutral Risk Analyst Round 1 - Weighing",
        "V. Portfolio Manager Decision",
        "VI. Paper-Study Disclaimer",
    ]:
        assert section in persistence


def test_debate_role_skills_define_interaction_outputs():
    expected = {
        "tradingagents-bull-researcher": "state the strongest positive thesis, cite analyst evidence, and state what Bear must disprove",
        "tradingagents-bear-researcher": "directly rebut the strongest Bull point, cite contrary evidence, and state what Bull is underestimating",
        "tradingagents-research-manager": "Include strongest Bull evidence, strongest Bear evidence, which side has better evidence, and why the final rating was selected.",
        "tradingagents-aggressive-risk-analyst": "explain why taking risk could be justified",
        "tradingagents-conservative-risk-analyst": "directly respond to Aggressive Risk and explain why the proposal may still be unsafe",
        "tradingagents-neutral-risk-analyst": "weigh Aggressive vs Conservative and state which risk argument is stronger",
        "tradingagents-portfolio-manager": "Synthesize the risk debate and do not merely repeat the Trader.",
        "tradingagents-workflow-orchestrator": "Do not compare the ticker to another ticker unless the run context explicitly says this is a comparative multi-ticker report.",
        "tradingagents-market-analyst": "Do not use generic technical template claims that conflict with actual data.",
        "tradingagents-sentiment-analyst": "Enforce as-of-date discipline: exclude social posts after the report trade date from the role report.",
        "tradingagents-news-analyst": "Filter relevance explicitly. Separate direct ticker/company news, indirect sector or market context, and excluded low-relevance items.",
        "tradingagents-trader": "Include a consistency check before the final proposal.",
    }

    for skill, required in expected.items():
        text = (SKILLS_ROOT / skill / "SKILL.md").read_text(encoding="utf-8")
        assert required in text


def test_codex_report_writer_fills_role_reports(tmp_path: Path):
    output_dir = tmp_path / "run"
    evidence_dir = output_dir / "evidence" / "TEST.AX" / "2026-06-27"
    report_dir = output_dir / "reports" / "TEST.AX" / "2026-06-27"
    evidence_dir.mkdir(parents=True)

    evidence_path = evidence_dir / "evidence.json"
    report_paths = {
        "research_manager": report_dir / "2_research" / "manager.md",
        "trader": report_dir / "3_trading" / "trader.md",
        "portfolio_manager": report_dir / "5_portfolio" / "decision.md",
        "debate_record": report_dir / "debate_record.md",
        "complete_report": report_dir / "complete_report.md",
        "bull_researcher_round_1": report_dir / "2_research" / "bull_round_1.md",
        "bear_researcher_round_1": report_dir / "2_research" / "bear_round_1.md",
        "aggressive_risk_round_1": report_dir / "4_risk" / "aggressive_round_1.md",
        "conservative_risk_round_1": report_dir / "4_risk" / "conservative_round_1.md",
        "neutral_risk_round_1": report_dir / "4_risk" / "neutral_round_1.md",
        "market_report": report_dir / "1_analysts" / "market.md",
        "sentiment_report": report_dir / "1_analysts" / "sentiment.md",
        "news_report": report_dir / "1_analysts" / "news.md",
        "fundamentals_report": report_dir / "1_analysts" / "fundamentals.md",
    }
    workflow = {
        "ticker": "TEST.AX",
        "trade_date": "2026-06-27",
        "evidence_path": str(evidence_path),
        "report_paths": {key: str(path) for key, path in report_paths.items()},
    }
    (evidence_dir / "workflow_state.json").write_text(
        json.dumps(workflow), encoding="utf-8"
    )

    snapshot = """## Verified market data snapshot for TEST.AX

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 10.00 |
| High | 11.00 |
| Low | 9.50 |
| Close | 12.00 |
| Volume | 1000 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 11.00 |
| close_50_sma | 10.50 |
| close_200_sma | 9.00 |
| rsi | 62.00 |
| macd | 0.50 |
| macds | 0.20 |
| atr | 0.70 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-06-26 | 12.00 |
"""
    stock_csv = """Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-06-26,10.00,11.00,9.50,12.00,1000,0.0,0.0
"""
    evidence = {
        "ticker": "TEST.AX",
        "trade_date": "2026-06-27",
        "identity": {
            "company_name": "Test Limited",
            "sector": "Industrials",
            "industry": "Testing",
        },
        "roles": {
            "market": {
                "tool_calls": {
                    "get_verified_market_snapshot": {"output": snapshot},
                    "get_stock_data": {"output": stock_csv},
                }
            },
            "news": {
                "tool_calls": {
                    "get_news": {
                        "output": "### Test growth plan (source: Example News)\nGrowth plan summary."
                    }
                }
            },
            "fundamentals": {
                "tool_calls": {
                    "get_fundamentals": {
                        "output": "\n".join(
                            [
                                "Market Cap: 1000000000",
                                "Revenue (TTM): 200000000",
                                "Net Income: 30000000",
                                "Free Cash Flow: 25000000",
                                "PE Ratio (TTM): 18",
                                "Forward PE: 16",
                                "Price to Book: 2",
                                "Dividend Yield: 3",
                                "Return on Equity: 0.12",
                                "Debt to Equity: 20",
                                "Current Ratio: 1.4",
                            ]
                        )
                    },
                    "get_cashflow": {"output": "NO_DATA_AVAILABLE"},
                    "get_income_statement": {"output": "NO_DATA_AVAILABLE"},
                }
            },
        },
    }
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(BUNDLE / "scripts" / "write_codex_reports.py"),
            "--output-dir",
            str(output_dir),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    complete = report_paths["complete_report"].read_text(encoding="utf-8")
    trader = report_paths["trader"].read_text(encoding="utf-8")

    assert "TEST.AX:" in result.stdout
    assert "Pending Codex role output" not in complete
    assert "Bull Researcher Round 1 - Opening Case" in complete
    assert "Conservative Risk Analyst Round 1 - Response to Aggressive" in complete
    assert "Portfolio Manager Decision" in complete
    assert "FINAL TRANSACTION PROPOSAL: **BUY**" in complete
    assert "paper-study workflow" not in trader


def test_complete_report_validator_rejects_old_linear_report(tmp_path: Path):
    report = tmp_path / "old_report.md"
    report.write_text(
        """# Trading Analysis Report: MSFT

## I. Analyst Team Reports

## II. Research Team Debate

### Bull Researcher Round 1

### Bear Researcher Round 1

## III. Trading Team Plan

FINAL TRANSACTION PROPOSAL: **BUY**
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "Bull Researcher Round 1 - Opening Case" in result.stdout


def test_complete_report_validator_accepts_required_headings(tmp_path: Path):
    report = tmp_path / "complete_report.md"
    report.write_text(
        """# Trading Analysis Report: MSFT

Context: comparative_run=false

## I. Analyst Team Reports

### Market Analyst

### Sentiment Analyst

### News Analyst

### Fundamentals Analyst

## II. Research Team Debate

### Bull Researcher Round 1 - Opening Case

### Bear Researcher Round 1 - Rebuttal to Bull

### Research Manager Decision - Evidence Weighing

## III. Trading Team Plan

### Trader Proposal

FINAL TRANSACTION PROPOSAL: **BUY**

## IV. Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

### Conservative Risk Analyst Round 1 - Response to Aggressive

### Neutral Risk Analyst Round 1 - Weighing

## V. Portfolio Manager Decision

### Portfolio Manager

**Rating**: Buy

**Executive Summary**: Summary.

**Investment Thesis**: Thesis.

**Risk Assessment**: Risk.

**Paper-study implementation notes**: Notes.

## VI. Paper-Study Disclaimer
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_complete_report_validator_rejects_unexplained_msft_apple_leakage(tmp_path: Path):
    report = tmp_path / "msft_report.md"
    report.write_text(
        """# Trading Analysis Report: MSFT

Context: comparative_run=false

## II. Research Team Debate

### Bull Researcher Round 1 - Opening Case

Apple is the comparison.

### Bear Researcher Round 1 - Rebuttal to Bull

### Research Manager Decision - Evidence Weighing

## III. Trading Team Plan

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

### Conservative Risk Analyst Round 1 - Response to Aggressive

### Neutral Risk Analyst Round 1 - Weighing

## VI. Paper-Study Disclaimer
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--report", str(report)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "cross-ticker leakage" in result.stdout


def test_codex_report_writer_filters_msft_apple_social_leakage(tmp_path: Path):
    output_dir = tmp_path / "run"
    evidence_dir = output_dir / "evidence" / "MSFT" / "2026-06-27"
    report_dir = output_dir / "reports" / "MSFT" / "2026-06-27"
    evidence_dir.mkdir(parents=True)

    evidence_path = evidence_dir / "evidence.json"
    report_paths = {
        "research_manager": report_dir / "2_research" / "manager.md",
        "trader": report_dir / "3_trading" / "trader.md",
        "portfolio_manager": report_dir / "5_portfolio" / "decision.md",
        "complete_report": report_dir / "complete_report.md",
        "bull_researcher_round_1": report_dir / "2_research" / "bull_round_1.md",
        "bear_researcher_round_1": report_dir / "2_research" / "bear_round_1.md",
        "aggressive_risk_round_1": report_dir / "4_risk" / "aggressive_round_1.md",
        "conservative_risk_round_1": report_dir / "4_risk" / "conservative_round_1.md",
        "neutral_risk_round_1": report_dir / "4_risk" / "neutral_round_1.md",
        "market_report": report_dir / "1_analysts" / "market.md",
        "sentiment_report": report_dir / "1_analysts" / "sentiment.md",
        "news_report": report_dir / "1_analysts" / "news.md",
        "fundamentals_report": report_dir / "1_analysts" / "fundamentals.md",
    }
    (evidence_dir / "workflow_state.json").write_text(
        json.dumps(
            {
                "ticker": "MSFT",
                "trade_date": "2026-06-27",
                "evidence_path": str(evidence_path),
                "report_paths": {key: str(path) for key, path in report_paths.items()},
            }
        ),
        encoding="utf-8",
    )
    snapshot = """## Verified market data snapshot for MSFT

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Close | 12.00 |
| Volume | 1000 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 11.00 |
| close_50_sma | 10.50 |
| close_200_sma | 9.00 |
| rsi | 62.00 |
| macd | 0.50 |
| macds | 0.20 |
| atr | 0.70 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-06-26 | 12.00 |
"""
    evidence = {
        "ticker": "MSFT",
        "trade_date": "2026-06-27",
        "identity": {"company_name": "Microsoft Corporation"},
        "roles": {
            "market": {
                "tool_calls": {
                    "get_verified_market_snapshot": {"output": snapshot},
                    "get_stock_data": {"output": "Date,Open,High,Low,Close,Volume,Dividends,Stock Splits\n"},
                }
            },
            "social": {
                "tool_calls": {
                    "fetch_stocktwits_messages": {
                        "output": "Bullish: 1\n$AAPL and Apple comparison line\n$MSFT clean line"
                    },
                    "fetch_reddit_posts": {"output": "MSFT-only social line"},
                }
            },
            "news": {"tool_calls": {"get_news": {"output": ""}}},
            "fundamentals": {
                "tool_calls": {
                    "get_fundamentals": {"output": "PE Ratio (TTM): 18"},
                    "get_cashflow": {"output": "NO_DATA_AVAILABLE"},
                    "get_income_statement": {"output": "NO_DATA_AVAILABLE"},
                }
            },
        },
    }
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")

    subprocess.run(
        [
            sys.executable,
            str(BUNDLE / "scripts" / "write_codex_reports.py"),
            "--output-dir",
            str(output_dir),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    complete = report_paths["complete_report"].read_text(encoding="utf-8")
    assert "MSFT clean line" in complete
    assert "Apple" not in complete
    assert "AAPL" not in complete


def test_report_writer_avoids_technical_claims_that_conflict_with_200_sma():
    writer = _load_writer()
    ctx = writer._context(
        _evidence(
            "MSFT",
            close=372.97,
            ema10=377.15,
            sma50=410.52,
            sma200=446.27,
            rsi=40.48,
            macd=-13.75,
            macds=-9.66,
            pe=22.23,
        )
    )

    market = writer.market_report(ctx)
    bull = writer.bull_report(ctx)

    assert "A close above the 200 SMA" not in market
    assert "If price is still above the long-term average" not in bull
    assert "below the 200 SMA" in market
    assert "below the 200 SMA" in bull


def test_scoring_rule_keeps_aapl_style_setup_underweight_not_sell():
    writer = _load_writer()
    ctx = writer._context(
        _evidence(
            "AAPL",
            close=283.78,
            ema10=291.00,
            sma50=290.00,
            sma200=260.00,
            rsi=41.26,
            macd=-2.24,
            macds=0.53,
            pe=34.36,
            pb=39.09,
        )
    )

    research = writer.research_manager(ctx)
    trader = writer.trader(ctx)

    assert ctx["direction"]["rating"] == "Underweight"
    assert ctx["direction"]["action"] == "Hold"
    assert "Scoring Rule" in research
    assert "Sell requires either price below the 200 SMA" in research
    assert "FINAL TRANSACTION PROPOSAL: **HOLD**" in trader
    assert "Consistency Check" in trader
    assert "200 SMA still holds" in trader


def test_scoring_rule_explains_msft_sell_vs_hold_or_underweight():
    writer = _load_writer()
    ctx = writer._context(
        _evidence(
            "MSFT",
            close=372.97,
            ema10=377.15,
            sma50=410.52,
            sma200=446.27,
            rsi=40.48,
            macd=-13.75,
            macds=-9.66,
            pe=22.23,
        )
    )

    research = writer.research_manager(ctx)
    trader = writer.trader(ctx)

    assert ctx["direction"]["rating"] == "Sell"
    assert "Score Components" in research
    assert "below 200 SMA" in research
    assert "Sell wins over Hold/Underweight" in research
    assert "breakdown below longer-term support" in trader
    assert "FINAL TRANSACTION PROPOSAL: **SELL**" in trader


def test_social_evidence_filters_after_trade_date_and_marks_noisy_low_confidence():
    writer = _load_writer()
    ctx = writer._context(
        _evidence(
            "AAPL",
            close=100,
            ema10=101,
            sma50=102,
            sma200=90,
            rsi=45,
            macd=-1,
            macds=0,
            pe=30,
            stocktwits="\n".join(
                [
                    "[2026-06-28T00:01:00Z · @late · Bullish] $AAPL look-ahead",
                    "[2026-06-27T20:00:00Z · @ok · no-label] $AAPL useful",
                    "[2026-06-27T20:01:00Z · @noise · no-label] $SPY broad market",
                ]
            ),
        )
    )

    report = writer.sentiment_report(ctx)

    assert "look-ahead" not in report
    assert "$AAPL useful" in report
    assert "$SPY broad market" not in report
    assert "**Confidence:** Low-to-Medium" in report
    assert "noisy and retail-heavy" in report


def test_news_report_separates_direct_indirect_and_excludes_irrelevant_items():
    writer = _load_writer()
    news = """### AAPL KGI downgrade to Hold on AI roadmap concerns (source: Broker)
KGI lowered Apple to Hold, citing memory-cost pressure and uncertainty around the AI roadmap.
### Crypto week review (source: Crypto News)
Bitcoin and Ethereum moved this week.
### Alphabet cloud margins improve (source: Market News)
Alphabet reported stronger cloud margins.
"""
    ctx = writer._context(
        _evidence(
            "AAPL",
            close=100,
            ema10=101,
            sma50=102,
            sma200=90,
            rsi=45,
            macd=-1,
            macds=0,
            pe=30,
            news=news,
        )
    )

    report = writer.news_report(ctx)

    assert "Direct AAPL news" in report
    assert "Indirect sector/market news" in report
    assert "Excluded as low relevance" in report
    assert "KGI downgrade to Hold" in report
    assert "memory-cost pressure" in report
    assert "Crypto week review" not in report
    assert "Alphabet cloud margins improve" not in report
