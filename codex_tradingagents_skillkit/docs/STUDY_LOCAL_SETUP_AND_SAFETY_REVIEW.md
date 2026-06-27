# TradingAgents Local Setup and Safety Review

Review date: 2026-06-27

Local sandbox: `C:\Users\Yaozhou Ma\Documents\TradingAgents`

Source reviewed: `TauricResearch/TradingAgents`, upstream `main` at `85946c2f60768ab2dae23a5a36cd927662feef94`

Branch: `study/local-setup-review`

## 1. Executive summary

TradingAgents is suitable as a local learning sandbox for studying multi-agent LLM orchestration, provider routing, market-data abstraction, checkpointing, and report generation. It should not be used for real trading decisions. The project produces LLM-generated trading-style recommendations and report artifacts, but this review found no broker API integration or real order-submission path in the checked-out code.

Local setup succeeded with Python 3.13.13 because Python 3.12 was not installed on this machine. The project declares `requires-python = ">=3.10"` and the full test suite passed under 3.13.13.

The requested fork-backed workflow is not complete because no `zzhou78/TradingAgents` fork was found. This sandbox is currently fetched from upstream only; it has no `origin` remote and should not be pushed until a personal fork exists.

## 2. Repository and fork status

GitHub connector access showed repositories under `zzhou78`, but not `TradingAgents`. A direct `git ls-remote https://github.com/zzhou78/TradingAgents.git HEAD` returned `Repository not found`. Therefore, this review did not configure `origin` as a fork.

Current remotes:

```text
upstream https://github.com/TauricResearch/TradingAgents.git (fetch)
upstream https://github.com/TauricResearch/TradingAgents.git (push)
```

Expected future remote state after a fork is created:

```text
origin   https://github.com/zzhou78/TradingAgents.git
upstream https://github.com/TauricResearch/TradingAgents.git
```

Do not push this branch to `upstream`. Create or confirm the fork first, then add `origin` and push only to `origin study/local-setup-review`.

## 3. Local environment requirements

The README recommends Python 3.12 and the Dockerfile uses `python:3.12-slim`. On this machine, `py -3.12 --version` reported no suitable runtime, while `python --version` reported Python 3.13.13.

Local setup performed:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item -LiteralPath .env.example -Destination .env -Force
```

The local `.env` was copied from `.env.example` and left with blank placeholders only.

## 4. Python and dependency requirements

`pyproject.toml` declares:

- package: `tradingagents`
- version: `0.3.0`
- Python: `>=3.10`
- console script: `tradingagents = "cli.main:app"`

Core dependencies include LangChain/LangGraph packages, provider SDK wrappers, `pandas`, `requests`, `yfinance`, `stockstats`, `questionary`, `rich`, `typer`, `python-dotenv`, `redis`, and `langgraph-checkpoint-sqlite`.

Development dependencies are `ruff`, `pytest`, and `pytest-subtests`.

Optional dependency group:

- `bedrock`: `langchain-aws>=1.5.0`

Docker setup is present via `Dockerfile` and `docker-compose.yml`. Docker runs the app as a non-root `appuser` and mounts a named volume at `/home/appuser/.tradingagents`. An Ollama profile is available with `tradingagents-ollama`.

## 5. Online account/API-key requirements

At least one LLM provider is normally required for cloud LLM use. Local Ollama and generic local OpenAI-compatible endpoints can run without a cloud LLM key if a local model server is available.

| Service | Required or optional | Account/API key needed | Environment variable | Risk/cost note |
| --- | --- | --- | --- | --- |
| OpenAI | Required if provider selected | Yes | `OPENAI_API_KEY` | Paid API usage; LLM output is not investment advice. |
| Google Gemini | Required if provider selected | Yes | `GOOGLE_API_KEY` | Paid or quota-limited API usage. |
| Anthropic | Required if provider selected | Yes | `ANTHROPIC_API_KEY` | Paid API usage. |
| xAI | Required if provider selected | Yes | `XAI_API_KEY` | Paid API usage. |
| DeepSeek | Required if provider selected | Yes | `DEEPSEEK_API_KEY` | Paid or quota-limited API usage. |
| Qwen international | Required if provider selected | Yes | `DASHSCOPE_API_KEY` | Region-specific account. |
| Qwen China | Required if provider selected | Yes | `DASHSCOPE_CN_API_KEY` | Region-specific account. |
| GLM / Z.AI | Required if provider selected | Yes | `ZHIPU_API_KEY` | Region-specific account. |
| GLM China / BigModel | Required if provider selected | Yes | `ZHIPU_CN_API_KEY` | Region-specific account. |
| MiniMax global | Required if provider selected | Yes | `MINIMAX_API_KEY` | Region-specific account. |
| MiniMax China | Required if provider selected | Yes | `MINIMAX_CN_API_KEY` | Region-specific account. |
| OpenRouter | Required if provider selected | Yes | `OPENROUTER_API_KEY` | Aggregated provider billing and model routing. |
| Mistral | Required if provider selected | Yes | `MISTRAL_API_KEY` | Paid API usage. |
| Kimi / Moonshot | Required if provider selected | Yes | `MOONSHOT_API_KEY` | Paid API usage. |
| Groq | Required if provider selected | Yes | `GROQ_API_KEY` | Paid or quota-limited API usage. |
| NVIDIA NIM | Required if provider selected | Yes | `NVIDIA_API_KEY` | Paid or quota-limited API usage. |
| Azure OpenAI | Required if provider selected | Yes | `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT_NAME` | Enterprise credentials; keep `.env.enterprise` local only. |
| AWS Bedrock | Required if provider selected | AWS credentials, not a single API key | `AWS_DEFAULT_REGION`, optional `AWS_PROFILE`, standard AWS credential chain | Can incur AWS costs; optional extra not installed by default. |
| Ollama | Optional local provider | No cloud key | `OLLAMA_BASE_URL` optional | Requires local or remote Ollama server and pulled model. |
| OpenAI-compatible local endpoint | Optional local provider | Usually no key for local servers | `TRADINGAGENTS_LLM_BACKEND_URL`, optional `OPENAI_COMPATIBLE_API_KEY` | Good study path if using LM Studio, vLLM, llama.cpp, or a local relay. |
| yfinance / Yahoo Finance | Default market-data path | No key | none | Requires internet; may rate-limit, return stale data, or change availability. |
| Alpha Vantage | Optional market-data vendor | Yes | `ALPHA_VANTAGE_API_KEY` | Free tier is rate-limited; paid tiers cost money. |
| FRED | Optional macro-data vendor | Yes | `FRED_API_KEY` | Free key; used for macro time series. |
| Polymarket Gamma API | Optional prediction-market vendor | No key | none | Live public market probabilities; not a forecast guarantee. |
| Broker account | Not required | Do not configure | none | No broker integration should be added for this study sandbox. |

## 6. Local storage paths and files created

Default local storage comes from `tradingagents/default_config.py`:

- results/logs: `~/.tradingagents/logs`
- data cache: `~/.tradingagents/cache`
- memory log: `~/.tradingagents/memory/trading_memory.md`
- checkpoints: `~/.tradingagents/cache/checkpoints/<TICKER>.db` when checkpointing is enabled

The CLI also writes under the configured `results_dir`, including:

- `<results_dir>/<ticker>/<analysis_date>/reports/*.md`
- `<results_dir>/<ticker>/<analysis_date>/message_tool.log`
- `<results_dir>/<ticker>/TradingAgentsStrategy_logs/full_states_log_<date>.json`

Files/folders created during this review:

- `.venv/` local virtual environment
- `.env` copied from `.env.example` with blank placeholders

No LLM analysis run was executed, so no TradingAgents report, checkpoint, or memory-log output was intentionally created.

## 7. Security and secret-handling review

`.env.example` and `.env.enterprise.example` contain blank placeholder values only. The CLI can prompt for missing provider keys and persist them to `.env` via `python-dotenv`, so `.env` must never be committed.

`.gitignore` was updated to cover the requested patterns:

- `.env`
- `.env.*`
- `!.env.example`
- `!.env.enterprise.example`
- `*.key`
- `*.pem`
- `*.p12`
- `*.pfx`
- `.tradingagents/`
- `logs/`
- `cache/`
- `checkpoints/`
- `results/`
- existing `reports/` and `.env.enterprise`

Secret checks performed:

```powershell
git check-ignore -v .env
git check-ignore -v .env.local .env.enterprise sample.key sample.pem sample.p12 sample.pfx
git check-ignore -v .tradingagents/ logs/ cache/ checkpoints/ results/ reports/
git ls-files | Select-String -Pattern '.env|key|pem|p12|pfx'
rg -n 'sk-[A-Za-z0-9_-]{20,}' --glob '!.venv/**'
rg -n 'AKIA[0-9A-Z]{16}' --glob '!.venv/**'
rg -n 'BEGIN .*PRIVATE KEY' --glob '!.venv/**'
rg -n 'API_KEY=.+[^=\s]' .env .env.example .env.enterprise.example --glob '!.venv/**'
```

Results:

- `.env` is ignored.
- Runtime and credential patterns are ignored.
- Tracked secret-like file names are limited to example files, tests, and source code.
- The simple secret-pattern scans found no matches.
- `gitleaks` is not installed in this environment, so a full gitleaks scan was not run.

## 8. Test and verification results

Commands run:

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\tradingagents.exe --help
.\.venv\Scripts\python.exe -m ruff check
.\.venv\Scripts\python.exe -m pytest -q
```

Results:

- `pip check`: no broken requirements found.
- `tradingagents --help`: command starts and shows CLI options.
- `ruff check`: all checks passed.
- `pytest -q`: `490 passed, 2 skipped, 16 warnings, 69 subtests passed in 107.17s`.

Skipped tests:

- Bedrock provider test skipped because `langchain_aws` was not installed; that dependency is optional.
- DeepSeek live API test skipped because `DEEPSEEK_API_KEY` was not set; this is expected and avoids live API usage.

No expensive LLM calls, broad live market experiments, or broker calls were run.

## 9. Code architecture summary

CLI entry point:

- `pyproject.toml` maps `tradingagents` to `cli.main:app`.
- `cli/main.py` defines the Typer CLI and `analyze` command.

Main graph/orchestration:

- `tradingagents/graph/trading_graph.py` defines `TradingAgentsGraph`.
- `tradingagents/graph/setup.py` builds the LangGraph `StateGraph`.
- `tradingagents/graph/conditional_logic.py`, `propagation.py`, `signal_processing.py`, `reflection.py`, and `checkpointer.py` provide workflow control, state propagation, signal parsing, reflection, and checkpoint support.

Agent components:

- Analysts: `tradingagents/agents/analysts/`
- Researchers: `tradingagents/agents/researchers/`
- Trader: `tradingagents/agents/trader/trader.py`
- Risk management: `tradingagents/agents/risk_mgmt/`
- Managers: `tradingagents/agents/managers/research_manager.py` and `portfolio_manager.py`
- Structured schemas: `tradingagents/agents/schemas.py`

Data vendor routing:

- `tradingagents/dataflows/interface.py` maps abstract tools to `yfinance`, `alpha_vantage`, `fred`, and `polymarket`.
- Defaults in `tradingagents/default_config.py` use `yfinance` for stock, technical, fundamental, and news data; `fred` for macro data; and `polymarket` for prediction markets.

LLM provider configuration:

- `tradingagents/llm_clients/api_key_env.py` maps providers to environment variables.
- `tradingagents/llm_clients/openai_client.py` contains the OpenAI-compatible provider registry.
- `tradingagents/llm_clients/factory.py` routes native Anthropic, Google, Azure, Bedrock, and OpenAI-compatible clients.
- `cli/utils.py` defines interactive provider/model selection and key prompting.

Persistence:

- Memory log: `tradingagents/agents/utils/memory.py`
- Checkpoints: `tradingagents/graph/checkpointer.py`
- Report tree writer: `tradingagents/reporting.py`
- Full state JSON logs: `TradingAgentsGraph._log_state`

Test coverage:

- The `tests/` directory includes broad coverage for provider config, env overrides, symbol normalization, vendor routing, data freshness, memory log behavior, checkpoint resume, CLI config precedence, structured agents, and report writing.

## 10. Safety concerns

No broker API packages or order-submission code were found in this review. However, the project intentionally uses trading language and can generate buy/sell/hold style outputs. Those outputs are LLM-generated research artifacts only.

Risk areas:

- LLM outputs can be non-deterministic, wrong, or overconfident.
- Live market/news/social/prediction-market data can change, be stale, be rate-limited, or be unavailable.
- Running cloud LLM providers can incur cost.
- The CLI can persist API keys into `.env` if the user pastes them interactively.
- The default memory log persists prior decisions under `~/.tradingagents`, which could influence future runs.
- Report and log files may contain model outputs, ticker choices, prompts, and tool-call summaries.
- `cli/announcements.py` and `cli/utils.py` can make network calls for announcements and OpenRouter model lists during interactive use.
- The code includes web/API calls through `requests`, `urllib`, and `yfinance`.

Important boundary: do not connect this sandbox to GCAF data files, outputs, SQLite databases, reports, allocation policy, opportunities, execution fills, or approved actions.

## 11. What can be learned from this project

Useful study topics:

- LangGraph orchestration of multi-role agents.
- Separation of analyst, research, trader, risk, and portfolio-manager roles.
- Provider abstraction across native and OpenAI-compatible LLM APIs.
- Environment-variable-driven local configuration.
- Data-vendor routing with explicit fallback behavior.
- Defensive handling for missing/stale market data.
- Checkpointing with SQLite.
- Persistent memory/log design and its tradeoffs.
- CLI UX for configuring multi-step LLM workflows.

These ideas can be studied conceptually, but TradingAgents code and outputs must not be copied into GCAF.

## 12. What must not be used for real investing

Do not use this project to:

- Make real buy/sell/hold decisions.
- Produce GCAF opportunities or approved actions.
- Generate real broker instructions.
- Submit broker orders.
- Backfill or mutate GCAF holdings, cash, classifications, opportunities, approved actions, fills, SQLite data, reports, or policies.
- Treat LLM-generated reports as investment advice.
- Store or commit real API keys.
- Push `.env`, local logs, caches, checkpoints, memory files, or generated reports to GitHub.

## 13. Recommendation for next study step

Create a personal GitHub fork first, then add it as `origin`:

```powershell
git remote add origin https://github.com/zzhou78/TradingAgents.git
git remote -v
```

After that, push the existing local commit only to the fork branch and optionally open a draft PR for personal notes. For any later runtime experiment, use a harmless ticker such as `SPY` or `AAPL`, shallow research depth, no broker integration, and either a local LLM endpoint or explicit approval before any paid cloud LLM calls.
