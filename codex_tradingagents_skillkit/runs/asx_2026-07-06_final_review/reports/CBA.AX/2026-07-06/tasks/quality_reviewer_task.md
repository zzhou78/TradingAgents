# Codex Report Task: CBA.AX Quality Reviewer

Ticker: `CBA.AX`
Trade date: `2026-07-06`
Skill to use: `tradingagents-quality-reviewer`
Evidence file: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\evidence\CBA.AX\2026-07-06\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\6_quality\quality_review.md`
Memory update file: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\memory_updates\quality_review.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\1_analysts\financial_report.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\1_analysts\industry_theme.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\2_research\bull_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\2_research\bear_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\2_research\manager.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\3_trading\trader.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\4_risk\aggressive_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\4_risk\conservative_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\4_risk\neutral_round_1.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\5_portfolio\decision.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\CBA.AX\2026-07-06\complete_report.md`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\evidence\CBA.AX\2026-07-06\evidence.json`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\evidence\CBA.AX\2026-07-06\stage_inputs\quality_review\input_records.json`
- `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\evidence\CBA.AX\2026-07-06\stage_inputs\quality_review\evidence_ledger.jsonl`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\CBA.AX\quality_reviewer\memory.md`
- `codex_tradingagents_skillkit\memory\CBA.AX\quality_reviewer\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\CBA.AX\market_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\news_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\financial_report_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\industry_theme_discovery_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\bull_researcher`
- `codex_tradingagents_skillkit\memory\CBA.AX\bear_researcher`
- `codex_tradingagents_skillkit\memory\CBA.AX\research_manager`
- `codex_tradingagents_skillkit\memory\CBA.AX\trader`
- `codex_tradingagents_skillkit\memory\CBA.AX\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\CBA.AX\portfolio_manager`

## Instruction

Review complete_report.md, role reports, evidence summary, and structured evidence files; write quality_review.md and quality_gate.json. Flag political-trading or celebrity-trading news that is treated as material without a direct company impact path. Do not pass review-grade completion when all news article cards are snippet-only, extracted MD&A is unavailable, an earnings 8-K has only cover-page evidence without Exhibit 99.1 or equivalent, or no cash-flow statement section is extracted.

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
- `## Quality Gate Findings`

Reject generic role text unsupported by tool outputs. ASX reports are not complete when ASX source collection fails; quality_gate.json must be failed until official ASX or investor-relations evidence is available or the gap is explicitly unresolved. For US reports, fail review-grade completion when structured evidence is only shallow: all news cards are snippet-only, extracted MD&A is unavailable, an earnings-related 8-K has no Exhibit 99.1 or equivalent earnings-release exhibit, or cash-flow statement sections are unavailable.

## RoleExecutionContract

```json
{
  "role": "quality_reviewer",
  "allowed_inputs": [
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\1_analysts\\market.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\1_analysts\\sentiment.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\1_analysts\\news.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\1_analysts\\fundamentals.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\1_analysts\\financial_report.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\1_analysts\\industry_theme.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\2_research\\bull_round_1.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\2_research\\bear_round_1.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\2_research\\manager.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\3_trading\\trader.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\4_risk\\aggressive_round_1.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\4_risk\\conservative_round_1.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\4_risk\\neutral_round_1.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\5_portfolio\\decision.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\reports\\CBA.AX\\2026-07-06\\complete_report.md",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\evidence\\CBA.AX\\2026-07-06\\evidence.json",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\evidence\\CBA.AX\\2026-07-06\\stage_inputs\\quality_review\\input_records.json",
    "codex_tradingagents_skillkit\\runs\\asx_2026-07-06_final_review\\evidence\\CBA.AX\\2026-07-06\\stage_inputs\\quality_review\\evidence_ledger.jsonl"
  ],
  "forbidden_inputs": [
    "ignore_hard_validator_errors",
    "uncited_memory"
  ],
  "allowed_memory": [
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\CBA.AX\\quality_reviewer\\memory.md",
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\CBA.AX\\quality_reviewer\\memory.json"
  ],
  "forbidden_memory": [
    "other_role_memory",
    "other_ticker_memory"
  ],
  "required_tools": [
    "validate_quality_review",
    "stage_input_evidence",
    "evidence_ledger_consistency_check"
  ],
  "optional_tools": [
    "complete_report_validator"
  ],
  "required_output_sections": [
    "Tool Outputs Used",
    "Quality Gate Findings",
    "Evidence Gaps",
    "Memory Update"
  ],
  "required_evidence_citations": [
    "evidence_id",
    "role_report",
    "validator_error",
    "required_fix"
  ],
  "quality_gate": "quality_reviewer_gate",
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

- Company: Commonwealth Bank of Australia
- Sector: Financial Services
- Industry: Banks - Diversified
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
