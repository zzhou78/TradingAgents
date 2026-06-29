# Codex Report Task: MPL.AX Fundamentals Analyst

Ticker: `MPL.AX`
Trade date: `2026-06-27`
Skill to use: `tradingagents-fundamentals-analyst`
Evidence file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\MPL.AX\2026-06-27\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\MPL.AX\2026-06-27\1_analysts\fundamentals.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\MPL.AX\2026-06-27\memory_updates\fundamentals_analyst.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\MPL.AX\2026-06-27\roles\fundamentals.md`

## Forbidden Input Files

- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\MPL.AX\2026-06-27\roles\market.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\MPL.AX\2026-06-27\roles\social.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\MPL.AX\2026-06-27\roles\news.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\MPL.AX\2026-06-27\roles\financial_report.md`

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\MPL.AX\fundamentals_analyst\memory.md`
- `codex_tradingagents_skillkit\memory\MPL.AX\fundamentals_analyst\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\MPL.AX\market_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\news_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\financial_report_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\industry_theme_discovery_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\bull_researcher`
- `codex_tradingagents_skillkit\memory\MPL.AX\bear_researcher`
- `codex_tradingagents_skillkit\memory\MPL.AX\research_manager`
- `codex_tradingagents_skillkit\memory\MPL.AX\trader`
- `codex_tradingagents_skillkit\memory\MPL.AX\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\portfolio_manager`
- `codex_tradingagents_skillkit\memory\MPL.AX\quality_reviewer`

## Instruction

Write the Fundamentals Analyst report from fundamentals evidence only.

## Evidence Brief

- Company: Medibank Private Limited
- Sector: Financial Services
- Industry: Insurance - Specialty
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
