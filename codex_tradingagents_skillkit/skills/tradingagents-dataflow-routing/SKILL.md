---
name: tradingagents-dataflow-routing
description: Use when mimicking TradingAgents data access, tool wrappers, vendor routing, ticker normalization, cache/result path safety, optional macro/prediction data, or no-data handling from dataflows source.
---

# TradingAgents Dataflow Routing

Source files scanned:
- `tradingagents/dataflows/interface.py`
- `tradingagents/dataflows/config.py`
- `tradingagents/dataflows/errors.py`
- `tradingagents/dataflows/symbol_utils.py`
- `tradingagents/dataflows/utils.py`
- `tradingagents/dataflows/y_finance.py`
- `tradingagents/dataflows/yfinance_news.py`
- `tradingagents/dataflows/stockstats_utils.py`
- `tradingagents/dataflows/alpha_vantage*.py`
- `tradingagents/dataflows/fred.py`
- `tradingagents/dataflows/polymarket.py`
- `tradingagents/dataflows/reddit.py`
- `tradingagents/dataflows/stocktwits.py`
- `tradingagents/agents/utils/*_tools.py`

Inputs:
- Tool method name, ticker or topic, date range, active config, and selected analyst context.
- Optional vendor settings from `tool_vendors` and category-level `data_vendors`.

Procedure:
1. Call agent tool wrappers, not vendor modules directly, unless auditing source behavior.
2. Use these call shapes:
   - `get_stock_data(symbol, start_date, end_date)`.
   - `get_indicators(symbol, indicator, curr_date, look_back_days)`.
   - `get_fundamentals(ticker, curr_date)`.
   - `get_balance_sheet(ticker, freq, curr_date)`.
   - `get_cashflow(ticker, freq, curr_date)`.
   - `get_income_statement(ticker, freq, curr_date)`.
   - `get_news(ticker, start_date, end_date)`.
   - `get_global_news(curr_date, look_back_days, limit)`.
   - `get_insider_transactions(ticker)`.
   - `get_macro_indicators(indicator, curr_date, look_back_days)`.
   - `get_prediction_markets(topic, limit)`.
3. Let `route_to_vendor` choose implementations; tool_vendors override category data_vendors.
4. Remember: the explicit vendor list is the fallback chain; do not silently use unlisted vendors.
5. Allow `default` to mean all available vendors for that method.
6. Macro and prediction-market categories are optional: failures become `DATA_UNAVAILABLE` sentinel text.
7. Market no-data conditions become `NO_DATA_AVAILABLE`; report unavailability and do not estimate or fabricate values.
8. Preserve ticker identity and filesystem safety with normalization and `safe_ticker_component`.

Output:
- Dataflow call plan and returned evidence blocks for the analyst skills, including explicit no-data or optional-unavailable sentinel text where applicable.

Safety boundaries:
- Do not bypass configured vendor routing just to obtain data.
- Do not write cache, checkpoint, or report files using unsanitized ticker strings.
- Do not use as real trading advice.
- Do not connect to GCAF.
