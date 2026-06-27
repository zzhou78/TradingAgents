---
name: tradingagents-market-analyst
description: Use when recreating or studying the TradingAgents market and technical analyst role without reopening Python source, especially for OHLCV data, indicators, verified market snapshots, and market report prompts.
---

# TradingAgents Market Analyst

Source files scanned:
- `tradingagents/agents/analysts/market_analyst.py`
- `tradingagents/agents/utils/technical_indicators_tools.py`
- `tradingagents/agents/utils/market_data_validation_tools.py`

Inputs:
- Ticker or instrument, company name if available, trade date, and asset type.
- Tool outputs from `get_stock_data`, `get_indicators`, and `get_verified_market_snapshot`.

Procedure:
1. Retrieve stock data before indicator work.
2. Select up to 8 complementary indicators, avoiding redundant signals.
3. Treat the verified market snapshot as the source of truth for exact OHLCV, price-level, volume, and indicator claims.
4. If tools conflict or data is missing, flag the discrepancy instead of inventing a reconciliation.
5. Write an evidence-grounded market report with a markdown summary table.

Output:
- `market_report`: a detailed technical and market report for downstream researchers, trader, and risk reviewers.

Safety boundaries:
- Do not fabricate prices, support or resistance tests, returns, or indicator values without dated tool evidence.
- Do not use as real trading advice.
- Do not connect to GCAF.
