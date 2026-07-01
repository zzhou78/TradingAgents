# Codex TradingAgents Expert Role Workflow Design

Status: design accepted for phased implementation. No role is considered upgraded until it has tools, tests, evidence ledger output, report integration, and quality checks.

## Goal

Convert the Codex TradingAgents skillkit from a prompt-preparation workflow into a Codex-led expert role workflow. Upstream TradingAgents Python remains a useful data provider, but it is not the reasoning engine. Codex acts each specialist role, using structured tool outputs, role-specific skills, local Python helpers, and quality gates.

## Responsibility Boundary

Python may:

- collect source records from approved tools;
- extract text, metadata, dates, tables, and sections;
- normalize tickers, dates, URLs, source names, and schemas;
- deduplicate repeated source records;
- candidate-classify source relevance, event type, freshness, and data quality;
- calculate repeatable metrics;
- validate schemas, evidence coverage, and report contracts;
- write structured evidence files for Codex to interpret.

Python must not:

- decide Buy, Sell, Hold, Overweight, or Underweight;
- write final investment judgments;
- state final news impact, final thesis direction, or portfolio action;
- override Codex role interpretation;
- replace missing evidence with memory or template language.

Codex roles must:

- identify the role's evidence need before concluding;
- select approved tools or request approval for new tools when evidence is missing;
- interpret Python/tool outputs as a specialist analyst;
- cite evidence IDs and source outputs for material claims;
- state uncertainty, evidence gaps, and limitations;
- write role reports that can be validated by hard gates and the Quality Reviewer.

## Evidence Ledger Schema

All material tool outputs used by a role must be recorded in a machine-readable ledger. The first implementation should use JSON Lines so tools can append entries safely.

```json
{
  "evidence_id": "news:AAPL:2026-06-29:001",
  "ticker": "AAPL",
  "trade_date": "2026-06-29",
  "role": "news_analyst",
  "tool_name": "news_article_evidence",
  "tool_version": "0.1.0",
  "source_url": "https://example.com/article",
  "source_date": "2026-06-28",
  "retrieval_time": "2026-06-29T10:15:00+10:00",
  "as_of_validity": {
    "valid_for_trade_date": true,
    "reason": "source_date is on or before trade_date"
  },
  "confidence": "medium",
  "limitations": ["snippet_only"],
  "structured_output_path": "codex_tradingagents_skillkit/runs/.../evidence/news/article_cards.json",
  "report_sections_using_it": ["News Analyst"]
}
```

Required fields:

- `evidence_id`
- `ticker`
- `trade_date`
- `role`
- `tool_name`
- `tool_version`
- `source_url`
- `source_date`
- `retrieval_time`
- `as_of_validity`
- `confidence`
- `limitations`
- `structured_output_path`
- `report_sections_using_it`

The ledger records evidence availability and quality. It does not record final investment conclusions.

## RoleExecutionContract Schema

Each role must have a contract that is persisted into `workflow_state.json` and repeated in the generated task prompt.

```json
{
  "role": "news_analyst",
  "allowed_inputs": [
    "codex_tradingagents_skillkit/runs/.../evidence/AAPL/2026-06-29/roles/news.md",
    "codex_tradingagents_skillkit/runs/.../evidence/AAPL/2026-06-29/news/article_cards.json",
    "codex_tradingagents_skillkit/runs/.../evidence/AAPL/2026-06-29/news/evidence_ledger.jsonl"
  ],
  "forbidden_inputs": ["future_articles", "uncited_memory", "raw_social_feed_as_news"],
  "allowed_memory": ["codex_tradingagents_skillkit/memory/AAPL/news_analyst/memory.md"],
  "forbidden_memory": ["other_role_memory", "other_ticker_memory"],
  "required_tools": ["candidate_news_search", "news_article_evidence", "news_evidence_ledger_validator"],
  "optional_tools": ["browser_full_text_check", "company_ir_search"],
  "required_output_sections": ["Tool Outputs Used", "Article Evidence Cards", "News Impact Summary", "Evidence Gaps", "Memory Update"],
  "required_evidence_citations": ["evidence_id", "source_url", "source_date", "full_text_status"],
  "quality_gate": "news_analyst_quality_gate",
  "memory_update_schema": {
    "durable_facts_to_retain": ["string"],
    "prior_mistakes_to_avoid": ["string"],
    "open_questions": ["string"],
    "evidence_references": ["evidence_id"],
    "staleness_or_expiry": "string"
  }
}
```

## Tool And Plugin Security

Codex may discover tools freely and may use already-approved tools. Codex must not do any of the following without user approval:

- install new tools or plugins;
- grant credentials;
- use new external plugins;
- use browser or computer-use actions that could affect real trading;
- use broker/order tools.

Broker/order tools are never allowed in this workflow.

Every proposed tool must be reviewed for:

- source reliability;
- data freshness;
- rate limits;
- reproducibility;
- cacheability;
- permissions;
- credential exposure;
- network behavior;
- file write scope;
- compliance and terms constraints.

## Hard Workflow Gates

The final `complete_report.md` must not be marked as a completed successful review when:

- required source collection fails;
- a required role output is pending;
- evidence ledger entries are missing for material role claims;
- a role report omits required sections;
- a News Analyst impact label is unsupported by an article evidence card;
- a snippet-only article is treated as high confidence;
- post-trade-date evidence is used without being marked invalid;
- an ASX financial report source collection fails for an ASX company.

Documented limitations may keep a validation artifact useful for debugging, but
they do not override review-grade hard gates. When a hard gate fails, the
workflow must produce a remediation plan instead of marking the report
successful.

## Quality Remediation Feedback Loop

The workflow must actively improve after quality failures:

- quality validation emits specific failures;
- a remediation planner maps each failure to a root-cause category;
- the plan names affected code areas, required tests, and rerun commands;
- Codex implements the collector, extractor, prompt, validator, or report
  integration fix;
- AAPL/MSFT or other nominated tickers are rerun to prove the fix.

The remediation plan is machine-readable and must include:

- `failed_gate`;
- `root_cause_category`;
- `affected_files`;
- `required_fix`;
- `required_tests`;
- `rerun_command`;
- `blocking_for_review_grade`;
- `status`.

Python may diagnose workflow and extraction failures, generate remediation
tasks, and validate before/after evidence. Python must not turn those tasks into
final investment judgments.

## Standing Auto-Remediation Approval

The user has approved Option 1 as the default behavior for all future TradingAgents workflows. When the quality gate fails, Codex must treat the next
remediation item as an approved continuation of the same workflow. Codex should
do not ask the user to proceed and should do the following:

- read `quality_remediation_plan.json` and `next_remediation_task.md`;
- implement the required collector, extractor, validator, skill, prompt, or
  report-integration fix with tests;
- rerun evidence collection, task preparation, role/report generation, and the
  workflow controller for the affected ticker set;
- repeat until the quality gate passes or a true external blocker is
  documented.

This approval does not authorize new plugin installs, credentials, broker/order
tools, real trading actions, or browser/computer-use actions that could affect
real trading. Those still require explicit approval.

## Role Upgrade Definition

A role is upgraded only when all of the following are true:

- the role has a RoleExecutionContract;
- the role has at least one role-specific tool or structured evidence adapter;
- the tool writes evidence ledger entries;
- the generated task prompt includes the contract and evidence paths;
- the role report has required evidence citations;
- tests cover tool behavior, ledger schema, report integration, and quality gates;
- Quality Reviewer checks the role-specific failure modes.

## Role Design Matrix

| Role | Expert behavior | Tool/Python responsibility | Hard quality expectation |
|---|---|---|---|
| Market Analyst | Quantitative market technician | OHLCV, indicators, trend regime, volatility, support/resistance calculations | No claim may conflict with verified price, SMA/EMA, RSI, MACD, volume, or as-of date |
| Sentiment Analyst | Retail-social evidence evaluator | Social feed parsing, ticker relevance filtering, label counts, spam/noise flags | No raw feed dump; low confidence for sparse, noisy, unlabeled, or cross-ticker feeds |
| News Analyst | Event and materiality analyst | Candidate search, full-text/snippet extraction, dedupe, article cards, evidence ledger | Impact labels invalid without article cards; snippet-only lowers confidence |
| Fundamentals Analyst | Statement and sector metric analyst | Statement extraction, ratio calculations, sector-specific metric preparation | Must separate raw statement data from Codex interpretation |
| Financial Report Analyst | Filing and management-commentary specialist | SEC/ASX/IR document discovery, section/exhibit extraction, table extraction | Each major claim cites a source section or exhibit |
| Industry / Theme Discovery | Evidence-grounded theme mapper | Theme candidate extraction, clustering support, source linking | No preconfigured theme unless evidence supports it |
| Bull Researcher | Strongest evidence-backed positive thesis | Evidence matrix reading, upside checklist, falsification extraction | Must cite strongest evidence and answer Bear's strongest argument |
| Bear Researcher | Strongest evidence-backed negative thesis | Evidence matrix reading, downside checklist, falsification extraction | Must cite strongest evidence and answer Bull's strongest argument |
| Research Manager | Evidence-weighing decision maker | Structured evidence matrix and optional scoring arithmetic | No rating without direction, materiality, confidence, tool output, weight, and reason |
| Trader | Paper proposal translator | Technical levels, reference price, invalidation and confirmation checks | Final action must match reasoning; Sell requires support break or material negative setup |
| Aggressive Risk | Opportunity-risk advocate | Upside asymmetry and catalyst checklist | Must acknowledge concrete failure points |
| Conservative Risk | Capital-preservation advocate | Drawdown, liquidity, valuation, and adverse scenario checklist | Must challenge unsupported upside and evidence gaps |
| Neutral Risk | Risk debate referee | Compare aggressive and conservative evidence quality | Must not force compromise when evidence is one-sided |
| Portfolio Manager | Final risk-adjusted decision maker | Synthesis of research, trader, and risk debate outputs | Must not merely repeat Trader; must state risk debate impact |
| Quality Reviewer | Independent analytical validator | Hard validators, evidence ledger checks, contradiction checks | Must fail generic unsupported role text |
| Run Persistence / Orchestrator | Workflow state controller | Role contracts, allowed inputs, pending gates, report tree | Must prevent successful completion with pending or failed required stages |

## Phase Strategy

Phase 1 upgrades News Analyst only. Other roles keep their current contracts until they receive the same full treatment. This avoids broad superficial edits.

Phase 1 deliverables:

- News evidence schema and ledger writer;
- News article card extraction/normalization helper;
- News RoleExecutionContract integration;
- News task prompt integration;
- News quality gate validation;
- tests for extraction, ledger, task prompt, and quality failure modes.

## Overall High-Level Upgrade Plan

The full workflow upgrade should proceed in narrow, reviewable phases. A role is not upgraded just because its prompt text changes. Each phase must add tools, tests, ledger output where relevant, report integration, and quality checks.

### Phase 0: Shared Contracts And Gates

Purpose: establish the workflow infrastructure that every upgraded role will reuse.

Scope:

- evidence ledger schema;
- RoleExecutionContract schema;
- tool/security/data-quality review template;
- pending-output completion gate;
- common validator helpers;
- report/task prompt rendering for contracts.

Exit criteria:

- `workflow_state.json` can carry role contracts;
- generated task prompts show allowed inputs, forbidden inputs, memory rules, required tools, and required sections;
- validators can block successful completion when required role outputs are pending.

### Phase 1: News Analyst

Purpose: make the News Analyst an evidence-card-based event analyst.

Scope:

- candidate news collection integration;
- full-text vs snippet-only distinction;
- article deduplication;
- article evidence cards;
- News evidence ledger;
- News impact-label quality gates.

Exit criteria:

- impact labels are invalid unless supported by article evidence cards;
- snippet-only evidence cannot be high confidence;
- post-trade-date news is invalid for the trade date unless explicitly marked unusable;
- Codex, not Python, writes final event impact interpretation.

Detailed implementation plan: `docs/superpowers/plans/2026-06-29-news-analyst-phase-1.md`.

### Phase 2: Financial Report Analyst

Purpose: make financial document analysis section-level and source-cited.

Scope:

- SEC 10-K / 10-Q section extraction;
- 8-K Exhibit 99.1 extraction;
- ASX announcement and investor-relations source routing;
- PDF text/table extraction;
- claim-source table validation.

Exit criteria:

- every major financial-report claim cites a document section, exhibit, or structured fundamentals packet;
- missing capex, guidance, liquidity, risk, segment, or statement detail is recorded as an evidence gap;
- ASX source collection failure blocks normal ASX company review completion.

### Phase 3: Market Analyst

Purpose: make market analysis quantitative and internally consistent.

Scope:

- verified market snapshot ledger entries;
- indicator calculation records;
- trend/regime classification support;
- volatility and support/resistance helpers;
- contradiction checks against latest close, moving averages, RSI, MACD, and as-of date.

Exit criteria:

- no market report can claim price is above a level when verified data says it is below;
- every technical regime claim cites a tool output;
- Market Analyst report includes quantitative regime evidence and limitations.

### Phase 4: Fundamentals Analyst

Purpose: make fundamentals analysis statement-grounded and sector-aware.

Scope:

- income statement, balance sheet, and cash-flow normalization;
- ratio calculation helpers;
- sector-specific metric adapters for banks, miners/resources, healthcare, consumer, and technology where available;
- evidence gaps for unsupported sector metrics.

Exit criteria:

- Fundamentals Analyst separates raw statement data from Codex interpretation;
- sector-specific metrics are used where available;
- generic ratio-only reports fail quality review.

### Phase 5: Sentiment Analyst

Purpose: make social sentiment evidence-filtered rather than raw-feed-driven.

Scope:

- social item relevance classification;
- spam/joke/low-information filtering;
- bullish/bearish/neutral count summaries;
- Reddit availability and rate-limit recording;
- confidence downgrades for noisy or sparse evidence.

Exit criteria:

- final report summarizes social evidence and does not paste raw feeds;
- retail social evidence is not presented as institutional sentiment;
- confidence reflects usable item counts and source limitations.

### Phase 6: Industry / Theme Discovery Analyst

Purpose: make theme discovery evidence-grounded rather than taxonomy-driven.

Scope:

- theme candidate extraction from news, filings, presentations, and sector sources;
- theme/subtheme evidence cards;
- tailwind/headwind/mixed/irrelevant classification support;
- confidence and evidence-gap recording.

Exit criteria:

- no preconfigured theme is accepted without evidence links;
- theme relevance to the ticker is explicit;
- Research Manager receives usable theme evidence with confidence and limitations.

### Phase 7: Bull And Bear Researchers

Purpose: make debate adversarial, evidence-cited, and falsifiable.

Scope:

- Bull evidence matrix reader;
- Bear evidence matrix reader;
- direct response tracking;
- strongest-counterargument extraction;
- falsification condition recording.

Exit criteria:

- Bull cites strongest positive evidence and states what would disprove the thesis;
- Bear cites strongest negative evidence and states what would disprove the thesis;
- each side directly answers the other side's strongest argument.

### Phase 8: Research Manager

Purpose: make final research ratings auditable.

Scope:

- mandatory structured evidence matrix;
- direction, materiality, confidence, weight, tool output, and reason fields;
- optional scoring arithmetic with visible components;
- rating-vs-rating explanation, especially Sell vs Hold vs Underweight.

Exit criteria:

- no Buy/Hold/Sell/Underweight/Overweight conclusion without an evidence matrix;
- Sell decisions explain why Sell beats Hold or Underweight;
- primary driver of rating is visible and source-backed.

### Phase 9: Trader

Purpose: make trade proposals consistent with research and market evidence.

Scope:

- action consistency checker;
- Buy/Sell price framework validator;
- reference price, confirmation level, invalidation level, and optional target extraction;
- Sell support-break/material-negative-setup checks.

Exit criteria:

- Trader `Action` matches `FINAL TRANSACTION PROPOSAL`;
- Buy/Sell proposals include a paper-study price framework;
- Sell is blocked unless supported by below-200-SMA evidence or a separately documented material negative setup.

### Phase 10: Risk Debate Roles

Purpose: make risk debate useful rather than repetitive.

Scope:

- Aggressive opportunity checklist;
- Conservative downside checklist;
- Neutral evidence-quality comparison;
- direct response tracking across risk rounds.

Exit criteria:

- Aggressive acknowledges failure points;
- Conservative challenges specific unsupported upside assumptions;
- Neutral states which risk argument is stronger and why.

### Phase 11: Portfolio Manager

Purpose: make final decision risk-adjusted and not a Trader repeat.

Scope:

- risk debate synthesis;
- research/trader/risk alignment check;
- financial-report and industry-theme impact check;
- final invalidation/improvement conditions.

Exit criteria:

- Portfolio Manager states risk debate impact;
- final rating distinguishes technical/momentum Sell from fundamental Sell;
- decision cites upstream role evidence and unresolved gaps.

### Phase 12: Quality Reviewer And Persistence Hardening

Purpose: enforce the full workflow end to end.

Scope:

- cross-role contradiction checks;
- missing evidence ledger checks;
- unsupported claim detection;
- stale or cross-role memory leakage checks;
- `complete_report.md` success gate;
- `quality_gate.json` consistency checks.

Exit criteria:

- `complete_report.md` cannot be accepted when required roles are pending or source collection failed;
- `quality_gate.json` cannot pass while hard validator errors exist;
- Quality Reviewer findings are specific enough for a second report-writing pass.
