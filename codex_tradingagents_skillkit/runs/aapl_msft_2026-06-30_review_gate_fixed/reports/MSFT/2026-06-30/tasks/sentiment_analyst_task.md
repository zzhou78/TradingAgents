# Codex Report Task: MSFT Sentiment Analyst

Ticker: `MSFT`
Trade date: `2026-06-30`
Skill to use: `tradingagents-sentiment-analyst`
Evidence file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\evidence.json`
Output file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\1_analysts\sentiment.md`
Memory update file: `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\reports\MSFT\2026-06-30\memory_updates\sentiment_analyst.md`

## Allowed Input Files

- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\roles\social.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\social\social_summary.json`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\social\evidence_ledger.jsonl`

## Forbidden Input Files

- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\roles\market.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\roles\news.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\roles\fundamentals.md`
- `codex_tradingagents_skillkit\runs\aapl_msft_2026-06-30_review_gate_fixed\evidence\MSFT\2026-06-30\roles\financial_report.md`

## Allowed Memory Files

- `codex_tradingagents_skillkit\memory\MSFT\sentiment_analyst\memory.md`
- `codex_tradingagents_skillkit\memory\MSFT\sentiment_analyst\memory.json`

## Forbidden Memory Roots

- `codex_tradingagents_skillkit\memory\MSFT\market_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\news_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\fundamentals_analyst`
- `codex_tradingagents_skillkit\memory\MSFT\financial_report_analyst`
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

Write the Sentiment Analyst report from the social evidence only; summarize social evidence instead of dumping raw feeds.

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
- Social evidence processing table from the Sentiment Analyst skill.

Summarize social evidence only; do not paste full raw feeds or infer institutional sentiment from retail feeds.

## RoleExecutionContract

```json
{
  "role": "sentiment_analyst",
  "allowed_inputs": [
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\roles\\social.md",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\social\\social_summary.json",
    "codex_tradingagents_skillkit\\runs\\aapl_msft_2026-06-30_review_gate_fixed\\evidence\\MSFT\\2026-06-30\\social\\evidence_ledger.jsonl"
  ],
  "forbidden_inputs": [
    "future_social_posts",
    "raw_feed_dump_in_final_report",
    "institutional_sentiment_inference"
  ],
  "allowed_memory": [
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MSFT\\sentiment_analyst\\memory.md",
    "C:\\Users\\Yaozhou Ma\\Documents\\TradingAgents\\codex_tradingagents_skillkit\\memory\\MSFT\\sentiment_analyst\\memory.json"
  ],
  "forbidden_memory": [
    "other_role_memory",
    "other_ticker_memory"
  ],
  "required_tools": [
    "fetch_stocktwits_messages",
    "fetch_reddit_posts",
    "social_evidence_processing"
  ],
  "optional_tools": [
    "social_rate_limit_review"
  ],
  "required_output_sections": [
    "Tool Outputs Used",
    "Social Evidence Processing Rules",
    "Evidence Gaps",
    "Memory Update"
  ],
  "required_evidence_citations": [
    "evidence_id",
    "source",
    "items_reviewed",
    "usable_ticker_relevant_items",
    "confidence"
  ],
  "quality_gate": "sentiment_social_evidence_gate",
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
