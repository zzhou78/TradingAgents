# Codex Report Task: MPL.AX Market Analyst

Ticker: `MPL.AX`
Trade date: `2026-07-02`
Skill to use: `tradingagents-market-analyst`
Evidence file: `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\reports\MPL.AX\2026-07-02\1_analysts\market.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\reports\MPL.AX\2026-07-02\memory_updates\market_analyst.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\roles\market.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\market\quantitative_observations.json`
- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\market\evidence_ledger.jsonl`

## Forbidden Input Files

- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\roles\social.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\roles\news.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\roles\fundamentals.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-02_closed_loop\evidence\MPL.AX\2026-07-02\roles\financial_report.md`

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\MPL.AX\market_analyst\memory.md`
- `codex_tradingagents_skillkit\memory\MPL.AX\market_analyst\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\MPL.AX\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\news_analyst`
- `codex_tradingagents_skillkit\memory\MPL.AX\fundamentals_analyst`
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

Write the Market Analyst report from the market evidence only.

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
- `## Quantitative Regime / Tool Outputs`

Use verified market snapshots, OHLCV data, moving averages, RSI, MACD, ATR, volume, and trend/regime evidence. Do not make template claims that conflict with actual indicator values.

## RoleExecutionContract

```json
{
  "role": "market_analyst",
  "allowed_inputs": [
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-02_closed_loop\\evidence\\MPL.AX\\2026-07-02\\roles\\market.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-02_closed_loop\\evidence\\MPL.AX\\2026-07-02\\market\\quantitative_observations.json",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-02_closed_loop\\evidence\\MPL.AX\\2026-07-02\\market\\evidence_ledger.jsonl"
  ],
  "forbidden_inputs": [
    "future_prices",
    "uncited_memory",
    "template_trend_claims"
  ],
  "allowed_memory": [
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MPL.AX\\market_analyst\\memory.md",
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MPL.AX\\market_analyst\\memory.json"
  ],
  "forbidden_memory": [
    "other_role_memory",
    "other_ticker_memory"
  ],
  "required_tools": [
    "get_verified_market_snapshot",
    "get_stock_data",
    "get_indicators",
    "market_data_evidence",
    "market_metric_consistency_validator"
  ],
  "optional_tools": [
    "market_calendar_check",
    "yfinance_cache_review"
  ],
  "required_output_sections": [
    "Tool Outputs Used",
    "Quantitative Regime / Tool Outputs",
    "Evidence Gaps",
    "Memory Update"
  ],
  "required_evidence_citations": [
    "evidence_id",
    "metric_name",
    "value",
    "relation",
    "source_date"
  ],
  "quality_gate": "market_metric_consistency_gate",
  "memory_update_schema": {
    "durable_facts_to_retain": [
      "string"
    ],
    "prior_mistakes_to_avoid": [
      "string"
    ],
    "open_questions": [
      "string"
    ],
    "evidence_references": [
      "evidence_id"
    ],
    "staleness_or_expiry": "string"
  }
}
```






## Market Analyst Evidence Boundaries

- Python metric observations are not final technical judgments.
- Do not make price-versus-moving-average claims without metric evidence IDs.
- Latest close, 10 EMA, 50 SMA, 200 SMA, RSI, MACD, ATR, and volume claims must match metric evidence.
- If metric evidence is missing, state the evidence gap instead of using template language.


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
