---
name: tradingagents-evidence-and-reasoning-auditor
description: Use when a Codex TradingAgents workflow is complete or near-complete and needs evidence substrate, metric extraction, independence, and reasoning-validity audit before review-ready status.
---

# TradingAgents Evidence And Reasoning Auditor

It is not a trading decision role. It must not set Research Manager rating, Trader action, Portfolio Manager stance, or real trading instruction.

Core principle: Bull/Bear debate attacks the investment case. This auditor attacks whether evidence is trustworthy, extracted correctly, interpreted correctly, and reasoned into rating/action/stance validly.

Run after Portfolio Manager and before Quality Reviewer / final completion gate. It may also run earlier after analyst reports when evidence quality is uncertain. Do not replace Bull/Bear debate.

## Audit Sections

Produce:
- `## Summary Verdict`: exactly `pass`, `pass_with_warnings`, or `fail`.
- `## Critical Findings`: only issues that could materially mislead the user or invalidate review-ready status.
- `## Warnings`: usefulness reductions that do not invalidate completion.
- `## Evidence References`: cite exact files, evidence IDs, metric rows, report sections, or validator outputs.
- `## Required Remediation`: smallest fix for each critical finding.
- `## Regression Tests Needed`: tests to prevent recurrence.
- `## Do Not Change`: workflow parts that must remain unchanged.

## Required Attacks

### Evidence Reliability Attack
Check material evidence used by Research Manager, Trader, Risk Analysts, and Portfolio Manager. Flag wrong metric-value labels, dense-table values without row/column mapping, TOC/header/footer/footnote/navigation values used as metrics, low-confidence snippets treated as high-confidence, weak metric statuses counted as clean directional evidence, repeated evidence counted as independent confirmation, and missing evidence IDs.

### Metric-Value Attachment Attack
For each ASX sector metric audit row, inspect `metric_name`, `extracted_value_or_phrase`, `clean_metric_value`, `metric_value_status`, `association_score`, `association_reason`, `table_mapping_confidence`, `table_mapping_reason`, `supporting_sentence`, `row_label`, `column_label`, `cell_value`, and `raw_row_text`.

Rules:
- If supporting text has many numbers, require row_label, column_label, and table_mapping_confidence.
- If row/column mapping is unavailable, do not count the metric as clean directional evidence.
- `table_row_unparsed`, `context_only`, `metric_mentioned_only`, and `unavailable` must not be strong supportive/adverse evidence.
- If a clean value is populated, `metric_value_status` must be `value_extracted` and association_score must meet the accepted threshold.

### Dense Table Attack
Flag clean metric values from dense table-like text when there are more than four numeric values, multiple financial row labels, parenthesised current/prior/variance values, missing row_label or column_label, or table_mapping_confidence below threshold. Downgrade to `table_row_unparsed` unless row/column mapping proves the value.

### Evidence Independence Attack
News facts, social reaction, Bull/Bear restatements, Risk restatements, and Portfolio restatements are not independent confirmation unless independence_group_id or source distinction is clear. Repeated role mentions are not new evidence.

### Reasoning Logic Attack
Flag Research Manager rating not justified by evidence winner, Hold as default rather than balanced evidence, directional rating without directional evidence, Trader action mechanically driven by moving averages, missing rating/action tension explanation, risk debate repetition without risk-specific challenge, Portfolio stance ignoring risk debate, and confidence stronger than evidence quality supports.

### Role Separation Attack
Confirm Research Manager uses Buy / Overweight / Hold / Underweight / Sell; Trader uses BUY / HOLD / SELL; Portfolio Manager gives risk-adjusted stance; moving averages only modify confidence, timing, confirmation, invalidation, or trend conflict; Trader action remains a paper-study proposal.

### Cross-Ticker Differentiation Attack
If all tickers receive the same debate winner, rating, or action, flag possible differentiation failure unless evidence justifies it. Each ticker still needs ticker-specific metric, market, evidence-gap, and role reasoning.

### Validator Blind-Spot Attack
Assume validators may be incomplete. State what could still be wrong, which failure mode is untested, and which regression test should be added.

## Completion Rule

Use this rule:

`review_ready = quality_gate_passed AND evidence_reasoning_audit_has_no_critical_findings`

Do not use:

`review_ready = quality_gate_passed`

Required final status fields:

```json
{
  "quality_gate_passed": true,
  "evidence_reasoning_audit_status": "pass | pass_with_warnings | fail",
  "evidence_reasoning_critical_findings": [],
  "review_ready": true
}
```

If the auditor returns `fail`, create remediation tasks and keep the loop running. If it returns `pass_with_warnings`, review-ready is allowed only when warnings are non-critical and recorded.

## Do Not Change

Keep the existing TradingAgents role sequence, Bull/Bear debate, Research Manager rating, Trader action, Portfolio stance, paper-study boundary, ASX metric extraction safeguards, dense-table `table_row_unparsed` behavior, quality validators, and remediation loop.

Safety boundaries:
- Do not use as real trading advice.
- Do not connect to GCAF.
