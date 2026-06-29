# Codex Report Task: BHP.AX Industry Theme Discovery

Ticker: `BHP.AX`
Trade date: `2026-06-27`
Skill to use: `tradingagents-industry-theme-discovery-analyst`
Evidence file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\BHP.AX\2026-06-27\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\1_analysts\industry_theme.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\memory_updates\industry_theme_discovery_analyst.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\reports\BHP.AX\2026-06-27\1_analysts\financial_report.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-06-27\evidence\BHP.AX\2026-06-27\evidence.json`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\BHP.AX\industry_theme_discovery_analyst\memory.md`
- `codex_tradingagents_skillkit\memory\BHP.AX\industry_theme_discovery_analyst\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\BHP.AX\market_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\news_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\financial_report_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\bull_researcher`
- `codex_tradingagents_skillkit\memory\BHP.AX\bear_researcher`
- `codex_tradingagents_skillkit\memory\BHP.AX\research_manager`
- `codex_tradingagents_skillkit\memory\BHP.AX\trader`
- `codex_tradingagents_skillkit\memory\BHP.AX\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\BHP.AX\portfolio_manager`
- `codex_tradingagents_skillkit\memory\BHP.AX\quality_reviewer`

## Instruction

Discover current industry themes and subthemes from the evidence, current online research packet, filings, and investor materials when available. Do not force-fit a preconfigured taxonomy. Python must not classify themes or financial-report conclusions. If online sources or filings are unavailable, state the evidence gap.

## Required Tool-Using Expert Workflow

1. Identify the role's evidence gap before writing conclusions.
2. Use the available tool outputs in the allowed input files first.
3. If a repeatable calculation, extraction, scoring, comparison, or validation is needed, use or request a Python tool instead of hand-waving.
4. Cite tool outputs and source files for every material claim.
5. State uncertainty and evidence gaps; do not replace missing evidence with assumptions or memory.
6. Include a `## Tool Outputs Used` section listing the concrete tools, source files, or upstream role outputs used.
7. Include an `## Evidence Gaps` section when source coverage is sparse, failed, or snippet-only.


Role-specific required sections:
- `## Tool Outputs Used`

## Evidence Brief

- Company: BHP Group Limited
- Sector: Basic Materials
- Industry: Other Industrial Metals & Mining
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
