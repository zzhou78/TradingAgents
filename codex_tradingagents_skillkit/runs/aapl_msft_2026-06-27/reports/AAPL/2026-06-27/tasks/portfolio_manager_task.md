# Codex Report Task: AAPL Portfolio Manager

Ticker: `AAPL`
Trade date: `2026-06-27`
Skill to use: `tradingagents-portfolio-manager`
Evidence file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-27\evidence\AAPL\2026-06-27\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-27\reports\AAPL\2026-06-27\5_portfolio\decision.md`

## Instruction

Synthesize the trader proposal and risk debate into the final paper portfolio decision.

## Evidence Brief

- Company: Apple Inc.
- Sector: Technology
- Industry: Consumer Electronics
- Evidence roles: 4
- fundamentals: get_balance_sheet, get_cashflow, get_fundamentals, get_income_statement
- market: get_indicators:atr, get_indicators:close_200_sma, get_indicators:close_50_sma, get_indicators:macd, get_indicators:rsi, get_stock_data, get_verified_market_snapshot
- news: get_global_news, get_insider_transactions, get_news
- social: fetch_reddit_posts, fetch_stocktwits_messages

## Boundaries

- Python prepared this task file only; it did not write investment reasoning.
- Codex must write the actual report output using the named skill.
- Keep raw feeds in evidence files unless the relevant skill explicitly asks for short representative examples.
- Do not use as real trading advice.
- Do not connect to GCAF.
