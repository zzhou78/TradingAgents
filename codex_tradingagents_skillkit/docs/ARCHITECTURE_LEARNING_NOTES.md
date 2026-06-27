# TradingAgents Architecture Learning Notes

Review date: 2026-06-27

Scope: local learning notes for the TradingAgents sandbox only. These notes are not trading advice, not a recommendation engine, and not input for GCAF.

## 1. Main execution flow from CLI command to final report

The installed console command is `tradingagents`, mapped in `pyproject.toml` to `cli.main:app`.

The main CLI command is `analyze` in `cli/main.py`. It accepts checkpoint flags, optionally clears checkpoints, and then calls `run_analysis()`.

High-level runtime flow:

1. `get_user_selections()` collects ticker, date, analyst set, research depth, provider, models, endpoint, output language, and provider-specific reasoning settings.
2. `_build_run_config()` starts from `DEFAULT_CONFIG`, applies user selections, and preserves explicit `TRADINGAGENTS_*` environment overrides for debate rounds and checkpointing.
3. `TradingAgentsGraph` is created with selected analysts, run config, debug streaming enabled, and stats callbacks.
4. The CLI creates a result directory under `config["results_dir"]`, a `reports` subfolder, and `message_tool.log`.
5. The CLI resolves instrument identity once, builds the initial graph state, and streams LangGraph chunks.
6. As chunks arrive, the CLI updates live progress, captures messages/tool calls, and writes interim report sections.
7. The final streamed chunks are merged into `final_state`.
8. The user can save a complete report tree through `write_report_tree()`, and the full report can be displayed in the terminal.

The programmatic path is `TradingAgentsGraph.propagate()`. It resolves memory context, optionally enables checkpointing, runs the graph, logs full state JSON, appends the decision to the memory log, clears successful checkpoints, and returns the final state plus a parsed signal.

## 2. CLI entry point and command structure

Entry point:

- `pyproject.toml`: `tradingagents = "cli.main:app"`
- `cli/main.py`: Typer app named `TradingAgents`

Important CLI modules:

- `cli/main.py`: command, display loop, graph streaming, report prompts, and result writes.
- `cli/utils.py`: ticker/date selection, analyst selection, provider/model selection, endpoint resolution, API-key prompting, and asset-type detection.
- `cli/models.py`: CLI enum-like model values such as analyst and asset types.
- `cli/stats_handler.py`: LLM/tool usage tracking.
- `cli/announcements.py`: optional network call for project announcements.

The CLI is interactive and can prompt for API keys. If a required provider key is missing, `ensure_api_key()` can save it to `.env`. This is convenient but increases the need to keep `.env` ignored and uncommitted.

## 3. Main graph/orchestration class

The main orchestrator is `TradingAgentsGraph` in `tradingagents/graph/trading_graph.py`.

Its key responsibilities:

- Apply config to dataflow routing through `set_config()`.
- Create cache and results directories.
- Instantiate deep and quick LLM clients with provider-specific kwargs.
- Create LangGraph tool nodes for analyst tools.
- Construct `ConditionalLogic`, `GraphSetup`, `Propagator`, `Reflector`, `SignalProcessor`, and `TradingMemoryLog`.
- Compile the workflow.
- Run the workflow through `propagate()` or the CLI's direct streaming path.
- Save final JSON state and report trees.
- Store final decisions in the memory log.

`GraphSetup` in `tradingagents/graph/setup.py` defines the directed graph. It wires selected analyst nodes first, then bull/bear researchers, research manager, trader, aggressive/conservative/neutral risk analysts, and portfolio manager.

## 4. Analyst agents

The analyst stage is configurable. Selected analysts run in a fixed planned order using `build_analyst_execution_plan()`.

### Market / technical analyst

File: `tradingagents/agents/analysts/market_analyst.py`

Purpose:

- Analyze OHLCV and technical indicators.
- Use `get_stock_data`, `get_indicators`, and `get_verified_market_snapshot`.
- Treat the verified snapshot as source of truth for exact price and indicator claims.

Learning value:

- Shows a tool-using analyst pattern where the LLM iterates through tool calls until it has enough data to produce a report.
- Demonstrates a guardrail against fabricated exact market values by requiring a verified market snapshot.

### Sentiment analyst

File: `tradingagents/agents/analysts/sentiment_analyst.py`

Purpose:

- Pre-fetch Yahoo Finance news, StockTwits messages, and Reddit posts for a seven-day window.
- Inject those blocks into the prompt before the LLM runs.
- Use structured output through `SentimentReport`, falling back to free text when needed.

Learning value:

- Good example of pre-fetching data outside the LLM tool loop to reduce hallucinated social-media claims.
- Shows a structured-output wrapper that can degrade gracefully.

### News analyst

File: `tradingagents/agents/analysts/news_analyst.py`

Purpose:

- Analyze ticker-specific news, global macro news, FRED macro indicators, and Polymarket prediction-market context.
- Use tools: `get_news`, `get_global_news`, `get_macro_indicators`, and `get_prediction_markets`.

Learning value:

- Shows how to combine direct company/asset news with optional macro and event-probability context.
- Also shows the risk of live data drift: current news and prediction-market data can change between runs.

### Fundamentals analyst

File: `tradingagents/agents/analysts/fundamentals_analyst.py`

Purpose:

- Analyze company profile, fundamentals, balance sheet, cash flow, and income statement data.
- Use tools: `get_fundamentals`, `get_balance_sheet`, `get_cashflow`, and `get_income_statement`.

Learning value:

- Shows how a role can be narrowly scoped around one data family.
- For non-stock assets, this path can be less meaningful or unavailable, so the CLI filters fundamentals for crypto.

## 5. Research debate flow

Files:

- `tradingagents/agents/researchers/bull_researcher.py`
- `tradingagents/agents/researchers/bear_researcher.py`
- `tradingagents/agents/managers/research_manager.py`
- `tradingagents/graph/conditional_logic.py`

The bull researcher builds the case for the asset using analyst reports and prior debate context. The bear researcher builds the opposing case and responds to the bull case. Both update `investment_debate_state`.

`ConditionalLogic.should_continue_debate()` alternates between bull and bear until `count >= 2 * max_debate_rounds`, then routes to the Research Manager.

The Research Manager reviews debate history and emits an investment plan using a five-tier scale:

- Buy
- Overweight
- Hold
- Underweight
- Sell

Learning value:

- The flow is a compact example of debate-style agent orchestration.
- The debate state keeps separate bull, bear, shared history, latest response, and count fields.
- The manager transforms free-form debate into a structured downstream plan.

## 6. Trader decision flow

File: `tradingagents/agents/trader/trader.py`

The Trader consumes the Research Manager's plan and instrument context. It produces `trader_investment_plan`, using `TraderProposal` structured output where possible.

The Trader is not a broker. It emits a proposal in natural language/markdown. There is no order-submission integration in the reviewed flow.

Learning value:

- Demonstrates a role that narrows a research plan into a concrete proposal format.
- Also demonstrates why this project must stay learning-only: the language is intentionally trading-oriented and could be mistaken for actionable advice.

## 7. Risk management flow

Files:

- `tradingagents/agents/risk_mgmt/aggressive_debator.py`
- `tradingagents/agents/risk_mgmt/conservative_debator.py`
- `tradingagents/agents/risk_mgmt/neutral_debator.py`
- `tradingagents/graph/conditional_logic.py`

The risk stage starts after the Trader. It cycles among:

- Aggressive Analyst: emphasizes upside and higher-risk opportunity.
- Conservative Analyst: emphasizes capital preservation and downside protection.
- Neutral Analyst: balances the two views.

Each node reads analyst reports, the trader proposal, instrument context, and risk-debate history. Each updates `risk_debate_state`.

`ConditionalLogic.should_continue_risk_analysis()` cycles speakers until `count >= 3 * max_risk_discuss_rounds`, then routes to the Portfolio Manager.

Learning value:

- Useful model of multi-perspective risk review.
- Good example of separate per-speaker histories plus shared history.
- Risk: the debate can create persuasive but still unverified prose.

## 8. Portfolio manager and final decision flow

File: `tradingagents/agents/managers/portfolio_manager.py`

The Portfolio Manager synthesizes:

- Research Manager plan.
- Trader proposal.
- Risk analyst debate history.
- Optional memory-log context from previous decisions and outcomes.
- Instrument context.

It produces `final_trade_decision` using `PortfolioDecision` structured output where possible, then renders markdown for CLI display, logs, memory, and saved reports.

Learning value:

- Shows a final arbiter pattern that combines upstream summaries and a debate transcript.
- Shows how persistent memory is injected into final decision prompts.

Safety note:

- The final output uses buy/sell-style language. In this sandbox it is a learning artifact only, not an investing instruction.

## 9. LLM provider configuration

Core files:

- `tradingagents/default_config.py`
- `tradingagents/llm_clients/api_key_env.py`
- `tradingagents/llm_clients/factory.py`
- `tradingagents/llm_clients/openai_client.py`
- `cli/utils.py`

Provider selection starts in the CLI or environment variables. `DEFAULT_CONFIG` supports overrides such as:

- `TRADINGAGENTS_LLM_PROVIDER`
- `TRADINGAGENTS_DEEP_THINK_LLM`
- `TRADINGAGENTS_QUICK_THINK_LLM`
- `TRADINGAGENTS_LLM_BACKEND_URL`
- `TRADINGAGENTS_OUTPUT_LANGUAGE`
- `TRADINGAGENTS_MAX_DEBATE_ROUNDS`
- `TRADINGAGENTS_MAX_RISK_ROUNDS`
- `TRADINGAGENTS_CHECKPOINT_ENABLED`
- `TRADINGAGENTS_TEMPERATURE`

`api_key_env.py` maps providers to key environment variables. Cloud providers normally require keys; local Ollama has no key; generic OpenAI-compatible endpoints have an optional key.

`factory.py` routes native providers such as Anthropic, Google, Azure, and Bedrock to dedicated clients. OpenAI-compatible providers share `OpenAIClient` and a provider registry in `openai_client.py`.

OpenAI-compatible providers include OpenAI, xAI, DeepSeek, Qwen, GLM, MiniMax, OpenRouter, Mistral, Kimi, Groq, NVIDIA, Ollama, and custom OpenAI-compatible endpoints.

Learning value:

- Centralizing API-key mappings and provider specs makes the provider surface easier to audit.
- Local endpoints are a safer learning path than paid cloud LLM calls.

## 10. Market data vendor routing

Core file: `tradingagents/dataflows/interface.py`

The routing layer maps abstract tool methods to vendor implementations:

- Core stock APIs: yfinance or Alpha Vantage.
- Technical indicators: yfinance or Alpha Vantage.
- Fundamental data: yfinance or Alpha Vantage.
- News data: yfinance or Alpha Vantage.
- Macro data: FRED.
- Prediction markets: Polymarket.

Defaults in `DEFAULT_CONFIG` use yfinance for stock, technical, fundamental, and news data; FRED for macro data; and Polymarket for prediction markets.

Important routing behavior:

- Explicit vendor configuration is respected as the actual fallback chain.
- It does not silently fall back to vendors the user did not configure.
- Optional macro and prediction-market categories degrade to sentinel messages if unavailable.
- Core categories surface real errors more strongly.
- No-data cases are turned into explicit "do not fabricate" messages.

Learning value:

- The routing layer is one of the most useful design ideas: tools call stable abstract methods while vendor choice remains configurable.
- The explicit fallback chain is safer than hidden fallback because data provenance stays clearer.

## 11. Memory, cache, checkpoint, and local storage behaviour

Default storage root:

- `~/.tradingagents`

Default paths from `DEFAULT_CONFIG`:

- Results/logs: `~/.tradingagents/logs`
- Data cache: `~/.tradingagents/cache`
- Memory log: `~/.tradingagents/memory/trading_memory.md`

Memory:

- `TradingMemoryLog` appends markdown entries with decision text and pending outcome state.
- Later same-ticker runs try to resolve outcomes through yfinance returns and write reflections.
- The Portfolio Manager can receive same-ticker and cross-ticker memory context.

Cache:

- yfinance indicator data is cached under `data_cache_dir`.
- Ticker path components are validated with `safe_ticker_component()` before interpolation into filesystem paths.
- Empty or stale data is rejected rather than reused.

Checkpoints:

- Checkpointing is opt-in through config or CLI flag.
- `get_checkpointer()` creates per-ticker SQLite checkpoint databases under `<data_cache_dir>/checkpoints/<TICKER>.db`.
- Thread IDs are deterministic per ticker/date.
- Successful completion clears the matching checkpoint rows.

Results:

- CLI runs write message/tool logs and report sections under the configured results directory.
- Programmatic runs can save the same report tree through `TradingAgentsGraph.save_reports()`.

Safety note:

- Memory, cache, logs, checkpoints, and reports can contain prompts, outputs, tickers, and model-generated decisions. They should remain local and ignored unless deliberately reviewed and sanitized.

## 12. Report/output generation

Core file: `tradingagents/reporting.py`

`write_report_tree()` writes:

- `1_analysts/market.md`
- `1_analysts/sentiment.md`
- `1_analysts/news.md`
- `1_analysts/fundamentals.md`
- `2_research/bull.md`
- `2_research/bear.md`
- `2_research/manager.md`
- `3_trading/trader.md`
- `4_risk/aggressive.md`
- `4_risk/conservative.md`
- `4_risk/neutral.md`
- `5_portfolio/decision.md`
- `complete_report.md`

The CLI also writes interim report markdown during streaming and prompts the user to save a final report after analysis.

Learning value:

- The report-tree structure is easy to inspect and separates stages cleanly.
- It is useful for studying agent traces, but generated reports should not be pushed by default because they may include API outputs and decision-like language.

## 13. Test structure and current coverage

The test suite is under `tests/` and configured by `pyproject.toml`.

Major coverage areas visible from test file names:

- Provider and model configuration: OpenAI, Anthropic, Google, DeepSeek, MiniMax, OpenRouter, Bedrock, Ollama, OpenAI-compatible endpoints.
- API-key environment mapping and env overrides.
- CLI config precedence and CLI symbol handling.
- Vendor routing and vendor error behavior.
- yfinance stale data and no-data handling.
- Alpha Vantage hardening.
- FRED and Polymarket integrations.
- News look-ahead behavior.
- Symbol normalization and safe ticker path handling.
- Market data validation and tool nodes.
- Checkpoint resume behavior.
- Memory log behavior.
- Structured agents.
- Reporting output.
- Signal processing and rating parsing.
- i18n coverage.

Current local verification result before these notes:

- `pip check`: clean.
- `tradingagents --help`: works.
- `ruff check`: clean.
- `pytest -q`: `490 passed, 2 skipped, 16 warnings, 69 subtests passed`.

## 14. What is useful for learning

Useful ideas to study:

- LangGraph state-machine orchestration of specialized roles.
- Explicit graph edges and conditional routing.
- Separating analysis, debate, trading proposal, risk review, and final decision roles.
- Structured output with free-text fallback.
- Centralized provider registry and API-key mapping.
- Environment-variable override pattern.
- Data-vendor abstraction and explicit fallback chains.
- Ticker path validation before filesystem writes.
- Checkpointing per ticker/date.
- Report-tree output for inspectable agent traces.
- Tests for stale data, no-data, provider routing, and checkpoint behavior.

These are architectural ideas to learn from, not code to transplant into another project.

## 15. What should not be copied into GCAF

Do not copy TradingAgents code, prompts, outputs, report files, memory files, cache files, generated decisions, or strategy language into GCAF.

Specifically do not copy:

- Any buy/sell/hold prompt language.
- Any final decision output.
- Any TradingAgents-generated opportunity, allocation, or trade idea.
- Any local `.env` or provider-key handling file containing real credentials.
- Any memory-log or report artifact.
- Any data cache or checkpoint database.
- Any broker-style symbol behavior into execution workflows without separate review.

At most, study broad design patterns conceptually, such as source-backed report trees, explicit vendor routing, and safety checks around local artifacts.

## 16. What would be dangerous for real-money use

Danger areas:

- LLM-generated analysis can be wrong, non-deterministic, or persuasive without being reliable.
- Live data sources can be stale, incomplete, rate-limited, or unavailable.
- News, social, Reddit, and prediction-market data can be noisy or manipulated.
- Memory injection can reinforce earlier bad decisions.
- Tool outputs and LLM outputs may mix facts, interpretations, and speculation.
- Cloud LLM calls can incur cost.
- API keys can be accidentally persisted to `.env` by the CLI prompt flow.
- Generated reports can sound like real trading instructions.
- Any future broker integration would materially increase risk and is out of scope for this learning sandbox.

Strict boundary:

TradingAgents output must remain learning output only. It must not be used to make portfolio decisions, create broker orders, generate GCAF opportunities, or update any real investment workflow.
