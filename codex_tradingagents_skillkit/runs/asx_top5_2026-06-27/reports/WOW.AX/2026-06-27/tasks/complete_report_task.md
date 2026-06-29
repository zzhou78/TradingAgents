# Codex Report Task: WOW.AX Complete Report

Ticker: `WOW.AX`
Trade date: `2026-06-27`
Skill to use: `tradingagents-run-persistence`
Evidence file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\WOW.AX\2026-06-27\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\complete_report.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\memory_updates\complete_report.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\1_analysts\financial_report.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\1_analysts\industry_theme.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\2_research\bull_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\2_research\bear_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\2_research\manager.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\3_trading\trader.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\4_risk\aggressive_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\4_risk\conservative_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\4_risk\neutral_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\WOW.AX\2026-06-27\5_portfolio\decision.md`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\WOW.AX\portfolio_manager\memory.md`
- `codex_tradingagents_skillkit\memory\WOW.AX\portfolio_manager\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\WOW.AX\market_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\news_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\financial_report_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\industry_theme_discovery_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\bull_researcher`
- `codex_tradingagents_skillkit\memory\WOW.AX\bear_researcher`
- `codex_tradingagents_skillkit\memory\WOW.AX\research_manager`
- `codex_tradingagents_skillkit\memory\WOW.AX\trader`
- `codex_tradingagents_skillkit\memory\WOW.AX\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\quality_reviewer`

## Instruction

Assemble complete_report.md from Codex-written role reports and run the hard contract validator.

## Evidence Brief

- Company: Woolworths Group Limited
- Sector: Consumer Defensive
- Industry: Grocery Stores
- Evidence roles: 5
- financial_report: collect_financial_document_sources
- fundamentals: get_balance_sheet, get_cashflow, get_fundamentals, get_income_statement
- market: get_indicators:atr, get_indicators:close_200_sma, get_indicators:close_50_sma, get_indicators:macd, get_indicators:rsi, get_stock_data, get_verified_market_snapshot
- news: get_global_news, get_insider_transactions, get_news
- social: fetch_reddit_posts, fetch_stocktwits_messages

## Boundaries

- Python prepared this task file only; it did not write investment reasoning.
- Codex must write the actual report output using the named skill.
- Read only the allowed input files.
- Read only the allowed memory files.
- Do not inspect other role memory.
- At the end, write a memory update for this role only.
- Memory must not override current evidence; if memory conflicts with current evidence, state the conflict explicitly.
- Python must not classify themes or financial-report conclusions.
- Keep raw feeds in evidence files unless the relevant skill explicitly asks for short representative examples.
- If online sources or filings are unavailable, state the evidence gap.
- Do not use as real trading advice.
- Do not connect to GCAF.

## Required Memory Update Footer

Every role output must end with:

```markdown
## Memory Update

* Durable facts to retain:
* Prior mistake to avoid:
* Open questions:
* Evidence references:
* Staleness / expiry:
```
