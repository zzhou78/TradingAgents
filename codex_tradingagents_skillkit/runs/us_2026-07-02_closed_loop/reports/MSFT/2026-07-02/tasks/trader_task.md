# Codex Report Task: MSFT Trader

Ticker: `MSFT`
Trade date: `2026-07-02`
Skill to use: `tradingagents-trader`
Evidence file: `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\evidence\MSFT\2026-07-02\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\3_trading\trader.md`
Memory update file: `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\memory_updates\trader.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\1_analysts\financial_report.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\1_analysts\industry_theme.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\reports\MSFT\2026-07-02\2_research\manager.md`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\evidence\MSFT\2026-07-02\stage_inputs\trader\input_records.json`
- `codex_tradingagents_skillkit\runs\us_2026-07-02_closed_loop\evidence\MSFT\2026-07-02\stage_inputs\trader\evidence_ledger.jsonl`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\MSFT\trader\memory.md`
- `codex_tradingagents_skillkit\memory\MSFT\trader\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\MSFT\market_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\news_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\financial_report_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\industry_theme_discovery_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\bull_researcher`
- `codex_tradingagents_skillkit\memory\MSFT\bear_researcher`
- `codex_tradingagents_skillkit\memory\MSFT\research_manager`
- `codex_tradingagents_skillkit\memory\MSFT\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\portfolio_manager`
- `codex_tradingagents_skillkit\memory\MSFT\quality_reviewer`

## Instruction

Translate the Research Manager plan into a paper Trader Proposal with a matching FINAL TRANSACTION PROPOSAL line. For Buy or Sell, include a labelled Paper-study price framework with reference price or entry zone, invalidation level, and first confirmation or target level.

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
- `## Action Consistency Check`
- `## Setup Quality Assessment`
- `## Setup Thresholds`
- `## Paper-study price framework`
- `FINAL TRANSACTION PROPOSAL`

The final transaction proposal must match the reasoning and cite the Research Manager and market evidence used. Explicitly state BUY/HOLD/SELL setup score thresholds and explain why a high positive or negative score can remain HOLD when research alignment or execution confirmation is missing.

## RoleExecutionContract

```json
{
  "role": "trader",
  "allowed_inputs": [
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\1_analysts\\market.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\1_analysts\\sentiment.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\1_analysts\\news.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\1_analysts\\fundamentals.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\1_analysts\\financial_report.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\1_analysts\\industry_theme.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\reports\\MSFT\\2026-07-02\\2_research\\manager.md",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\evidence\\MSFT\\2026-07-02\\stage_inputs\\trader\\input_records.json",
    "codex_tradingagents_skillkit\\runs\\us_2026-07-02_closed_loop\\evidence\\MSFT\\2026-07-02\\stage_inputs\\trader\\evidence_ledger.jsonl"
  ],
  "forbidden_inputs": [
    "live_order_tool",
    "broker_tool",
    "action_reasoning_mismatch"
  ],
  "allowed_memory": [
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MSFT\\trader\\memory.md",
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MSFT\\trader\\memory.json"
  ],
  "forbidden_memory": [
    "other_role_memory",
    "other_ticker_memory"
  ],
  "required_tools": [
    "stage_input_evidence",
    "trader_action_consistency_validator"
  ],
  "optional_tools": [
    "paper_price_framework_check"
  ],
  "required_output_sections": [
    "Tool Outputs Used",
    "Action Consistency Check",
    "Paper-study price framework",
    "FINAL TRANSACTION PROPOSAL",
    "Memory Update"
  ],
  "required_evidence_citations": [
    "evidence_id",
    "reference_price",
    "confirmation_level",
    "invalidation_level"
  ],
  "quality_gate": "trader_action_consistency_gate",
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








## Evidence Brief

- Company: Microsoft Corporation
- Sector: Technology
- Industry: Software - Infrastructure
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
