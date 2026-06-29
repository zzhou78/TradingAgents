# Codex Report Task: CSL.AX Quality Reviewer

Ticker: `CSL.AX`
Trade date: `2026-06-27`
Skill to use: `tradingagents-quality-reviewer`
Evidence file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\CSL.AX\2026-06-27\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\6_quality\quality_review.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\memory_updates\quality_review.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\1_analysts\financial_report.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\1_analysts\industry_theme.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\2_research\bull_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\2_research\bear_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\2_research\manager.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\3_trading\trader.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\4_risk\aggressive_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\4_risk\conservative_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\4_risk\neutral_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\5_portfolio\decision.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\CSL.AX\2026-06-27\complete_report.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\CSL.AX\2026-06-27\evidence.json`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\CSL.AX\quality_reviewer\memory.md`
- `codex_tradingagents_skillkit\memory\CSL.AX\quality_reviewer\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\CSL.AX\market_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\news_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\financial_report_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\industry_theme_discovery_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\bull_researcher`
- `codex_tradingagents_skillkit\memory\CSL.AX\bear_researcher`
- `codex_tradingagents_skillkit\memory\CSL.AX\research_manager`
- `codex_tradingagents_skillkit\memory\CSL.AX\trader`
- `codex_tradingagents_skillkit\memory\CSL.AX\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\CSL.AX\portfolio_manager`

## Instruction

Review complete_report.md, role reports, and evidence summary; write quality_review.md and quality_gate.json. Flag political-trading or celebrity-trading news that is treated as material without a direct company impact path.

## Evidence Brief

- Company: CSL Limited
- Sector: Healthcare
- Industry: Biotechnology
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
