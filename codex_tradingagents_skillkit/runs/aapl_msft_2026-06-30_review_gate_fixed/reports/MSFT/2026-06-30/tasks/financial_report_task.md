# Codex Report Task: MSFT Financial Report

Ticker: `MSFT`
Trade date: `2026-06-30`
Skill to use: `tradingagents-financial-report-analyst`
Evidence file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\1_analysts\financial_report.md`
Memory update file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\memory_updates\financial_report_analyst.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\1_analysts\market.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\1_analysts\sentiment.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\1_analysts\news.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\1_analysts\fundamentals.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\roles\financial_report.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\evidence.json`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\financial_report\section_records.json`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\financial_report\evidence_ledger.jsonl`

## Forbidden Input Files

- None declared.

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\MSFT\financial_report_analyst\memory.md`
- `codex_tradingagents_skillkit\memory\MSFT\financial_report_analyst\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\MSFT\market_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\sentiment_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\news_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\industry_theme_discovery_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\bull_researcher`
- `codex_tradingagents_skillkit\memory\MSFT\bear_researcher`
- `codex_tradingagents_skillkit\memory\MSFT\research_manager`
- `codex_tradingagents_skillkit\memory\MSFT\trader`
- `codex_tradingagents_skillkit\memory\MSFT\aggressive_risk_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\conservative_risk_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\neutral_risk_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\portfolio_manager`
- `codex_tradingagents_skillkit\memory\MSFT\quality_reviewer`

## Instruction

Read the structured fundamentals packet plus market-aware financial document packet: section-level 10-K/10-Q records and 8-K Exhibit 99.1 for US tickers; ASX announcements, annual reports, Appendix 4E/4D, results presentations, and investor materials for ASX tickers. Write financial_report.md with a claim-source table and cite the source section supporting each substantive claim. Python must not classify themes or financial-report conclusions. If a needed section or exhibit is unavailable, state the evidence gap.

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
- `## Claim-Source Table`

Every major claim must cite a source section or exhibit. Mark missing capex, guidance, segment, income statement, balance sheet, or cash-flow detail as an evidence gap.

## RoleExecutionContract

```json
{
  "role": "financial_report_analyst",
  "allowed_inputs": [
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\reports\\MSFT\\2026-06-30\\1_analysts\\market.md",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\reports\\MSFT\\2026-06-30\\1_analysts\\sentiment.md",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\reports\\MSFT\\2026-06-30\\1_analysts\\news.md",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\reports\\MSFT\\2026-06-30\\1_analysts\\fundamentals.md",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\roles\\financial_report.md",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\evidence.json",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\financial_report\\section_records.json",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\financial_report\\evidence_ledger.jsonl"
  ],
  "forbidden_inputs": [
    "future_filings",
    "uncited_memory",
    "unsupported_management_commentary"
  ],
  "allowed_memory": [
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MSFT\\financial_report_analyst\\memory.md",
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MSFT\\financial_report_analyst\\memory.json"
  ],
  "forbidden_memory": [
    "other_role_memory",
    "other_ticker_memory"
  ],
  "required_tools": [
    "collect_financial_document_sources",
    "financial_document_evidence",
    "financial_claim_source_validator"
  ],
  "optional_tools": [
    "sec_filing_lookup",
    "asx_announcement_lookup",
    "company_ir_search",
    "pdf_text_extraction"
  ],
  "required_output_sections": [
    "Tool Outputs Used",
    "Source coverage table",
    "Claim-Source Table",
    "Evidence gaps",
    "Memory Update"
  ],
  "required_evidence_citations": [
    "evidence_id",
    "source_type",
    "section_name",
    "filing_date",
    "evidence_gap"
  ],
  "quality_gate": "financial_report_claim_source_gate",
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




## Financial Report Evidence Boundaries

- Python section records are not final financial judgments.
- Do not make major financial claims without section evidence IDs or explicit evidence gaps.
- Treat 8-K cover pages as source-routing evidence unless the cover page itself contains the cited fact.
- Prefer Exhibit 99.1 for earnings-release claims when available.




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
