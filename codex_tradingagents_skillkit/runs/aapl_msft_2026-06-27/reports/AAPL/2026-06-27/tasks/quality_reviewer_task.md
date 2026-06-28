# Codex Report Task: AAPL Quality Reviewer

Ticker: `AAPL`
Trade date: `2026-06-27`
Skill to use: `tradingagents-quality-reviewer`
Evidence file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-27\evidence\AAPL\2026-06-27\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-27\reports\AAPL\2026-06-27\6_quality\quality_review.md`

## Instruction

Review complete_report.md, role reports, and evidence summary; write quality_review.md and quality_gate.json.

## Evidence Brief

- Company: Apple Inc.
- Sector: Technology
- Industry: Consumer Electronics
- Evidence roles: 5
- financial_report: collect_financial_document_sources
- fundamentals: get_balance_sheet, get_cashflow, get_fundamentals, get_income_statement
- market: get_indicators:atr, get_indicators:close_200_sma, get_indicators:close_50_sma, get_indicators:macd, get_indicators:rsi, get_stock_data, get_verified_market_snapshot
- news: get_global_news, get_insider_transactions, get_news
- social: fetch_reddit_posts, fetch_stocktwits_messages

## Boundaries

- Python prepared this task file only; it did not write investment reasoning.
- Codex must write the actual report output using the named skill.
- Python must not classify themes or financial-report conclusions.
- Keep raw feeds in evidence files unless the relevant skill explicitly asks for short representative examples.
- If online sources or filings are unavailable, state the evidence gap.
- Do not use as real trading advice.
- Do not connect to GCAF.
