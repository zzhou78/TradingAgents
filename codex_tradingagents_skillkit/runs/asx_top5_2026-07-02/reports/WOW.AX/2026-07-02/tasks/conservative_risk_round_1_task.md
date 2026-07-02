# Codex Report Task: WOW.AX Conservative Risk Round 1

Ticker: `WOW.AX`
Trade date: `2026-07-02`
Skill to use: `tradingagents-conservative-risk-analyst`
Evidence file: `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\evidence\WOW.AX\2026-07-02\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\4_risk\conservative_round_1.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\memory_updates\conservative_risk_round_1.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\1_analysts\financial_report.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\1_analysts\industry_theme.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\2_research\manager.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\3_trading\trader.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\reports\WOW.AX\2026-07-02\4_risk\aggressive_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\evidence\WOW.AX\2026-07-02\stage_inputs\conservative_risk_round_1\input_records.json`
- `codex_tradingagents_skillkit\runs\asx_top5_2026-07-02\evidence\WOW.AX\2026-07-02\stage_inputs\conservative_risk_round_1\evidence_ledger.jsonl`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\WOW.AX\conservative_risk_analyst\memory.md`
- `codex_tradingagents_skillkit\memory\WOW.AX\conservative_risk_analyst\memory.json`

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
- `codex_tradingagents_skillkit\memory\WOW.AX\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\WOW.AX\portfolio_manager`
- `codex_tradingagents_skillkit\memory\WOW.AX\quality_reviewer`

## Instruction

Write the conservative risk view, focused on downside, drawdown, valuation, liquidity, and evidence gaps; directly challenge unsupported upside assumptions.

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
- `## Downside Case`
- `## Unsupported Upside Challenges`

The conservative case must challenge unsupported upside assumptions with evidence.

## RoleExecutionContract

```json
{
  "role": "conservative_risk_analyst",
  "allowed_inputs": [
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\1_analysts\\market.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\1_analysts\\sentiment.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\1_analysts\\news.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\1_analysts\\fundamentals.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\1_analysts\\financial_report.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\1_analysts\\industry_theme.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\2_research\\manager.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\3_trading\\trader.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\reports\\WOW.AX\\2026-07-02\\4_risk\\aggressive_round_1.md",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\evidence\\WOW.AX\\2026-07-02\\stage_inputs\\conservative_risk_round_1\\input_records.json",
    "codex_tradingagents_skillkit\\runs\\asx_top5_2026-07-02\\evidence\\WOW.AX\\2026-07-02\\stage_inputs\\conservative_risk_round_1\\evidence_ledger.jsonl"
  ],
  "forbidden_inputs": [
    "unsupported_downside_template",
    "uncited_memory"
  ],
  "allowed_memory": [
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\WOW.AX\\conservative_risk_analyst\\memory.md",
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\WOW.AX\\conservative_risk_analyst\\memory.json"
  ],
  "forbidden_memory": [
    "other_role_memory",
    "other_ticker_memory"
  ],
  "required_tools": [
    "stage_input_evidence",
    "downside_risk_checklist"
  ],
  "optional_tools": [
    "drawdown_scenario_check"
  ],
  "required_output_sections": [
    "Tool Outputs Used",
    "Downside Case",
    "Unsupported Upside Challenges",
    "Response To Aggressive",
    "Memory Update"
  ],
  "required_evidence_citations": [
    "evidence_id",
    "downside_driver",
    "evidence_gap",
    "confidence"
  ],
  "quality_gate": "conservative_risk_evidence_gate",
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
