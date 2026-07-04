---
name: tradingagents-quality-reviewer
description: Use when a completed Codex TradingAgents report needs a second-pass quality review against evidence, role reports, and report consistency.
---

# TradingAgents Quality Reviewer

Inputs:
- `complete_report.md`
- role reports
- evidence summary
- evidence files when needed for dispute resolution

Procedure:
1. Read the complete report, role reports, and evidence summary before judging.
2. Check whether claims are supported by evidence, whether key risks are explained, and whether role conclusions conflict.
3. Treat `validate_complete_report.py` as a hard contract validator only; this skill is the analytical quality gate.
4. Use `## Tool Outputs Used` to record validators, evidence files, role reports, and source packets inspected.
5. Flag unsupported reasoning, missing ambiguity, overconfident social/news interpretation, contradictory ratings/actions, and unexplained primary drivers.
6. Fail or warn when financial_report.md is missing; financial report source coverage is unclear; fundamentals only lists ratios and omits financial statement data; industry_theme.md is missing; themes are preconfigured without evidence support; complete_report.md omits Financial Report Analyst or Industry / Theme Discovery Analyst sections; Research Manager ignores material financial-report or theme evidence; Portfolio Manager merely repeats Trader; or quality_gate.json passes despite quality errors.
7. Fail completed role reports that omit Tool Outputs Used, Article Evidence Cards for News Analyst, Quantitative Regime / Tool Outputs for Market Analyst, Claim-Source Table for Financial Report Analyst, or Structured Evidence Matrix for Research Manager.
8. ASX reports are not complete when ASX source collection fails. If official ASX announcements or investor-relations evidence cannot be collected, fail quality_gate.json or leave completion pending with an explicit evidence gap.
9. Fail ASX review-grade completion when `complete_report.md` is missing, `financial_report.md` is pending, ASX source collection is `error` without an explicit external blocker, sector-specific metrics are missing without evidence-gap disclosure, ASX financial strength/weakness claims lack section or metric evidence, or report folder trade date and report trade date disagree.
10. Fail or warn when the News Analyst treats political-trading or celebrity-trading headlines as material without a direct link to company fundamentals, regulation, price action, or sentiment.
11. Fail pending role outputs unless the final gate explicitly documents a limitation and leaves normal completion pending.
12. Require fixes that are specific enough for Codex to apply in a second report-writing pass.
13. A failed quality gate is not a terminal artifact. Ensure `quality_remediation_plan.json` and `next_remediation_task.md` exist, then Codex must implement the next remediation task, rerun the evidence/report workflow, and continue until the quality gate passes or a true external blocker is documented.

## News Analyst Evidence Gate

Fail the report when:
- news impact label lacks article evidence citation;
- snippet-only news evidence cannot be high confidence;
- all available news article cards are snippet-only and the report is presented as review-grade complete;
- News Analyst uses post-trade-date evidence as valid;
- News Analyst omits article evidence cards for material news claims.

## Financial Report Analyst Evidence Gate

Fail the report when:
- financial claim lacks section evidence citation;
- financial evidence gap missing for unavailable section;
- structured financial evidence lacks extracted MD&A;
- an earnings-related 8-K cover page is available but Exhibit 99.1 or equivalent earnings-release exhibit is unavailable;
- structured financial evidence lacks any extracted cash-flow statement section;
- Financial Report Analyst makes management-commentary, guidance, segment, capex, liquidity, risk-factor, income-statement, balance-sheet, or cash-flow claims without `evidence_id` citation or an explicit evidence gap;
- Financial Report Analyst treats an 8-K cover page as the full earnings release when Exhibit 99.1 is unavailable.

## Market Analyst Evidence Gate

Fail the report when:
- market.md is still pending;
- market moving-average claim conflicts with metric evidence;
- Market Analyst makes latest close, 10 EMA, 50 SMA, 200 SMA, RSI, MACD, ATR, volume, support, resistance, trend, or momentum claims without metric `evidence_id` citations;
- stale or missing metrics are presented as current evidence instead of evidence gaps.

## Full Workflow Evidence Gates

Fail the report when:
- sentiment report includes raw social feed instead of summary;
- Reddit is treated as required;
- Reddit unavailable or rate-limited status is treated as neutral sentiment;
- social sentiment is described as institutional sentiment when the evidence is StockTwits, Reddit, or another retail-only source;
- sentiment conclusion is based only on raw bullish/bearish counts or platform labels;
- high confidence is assigned to retail-only, sparse, noisy, spam/meme, or low-reasoning social evidence;
- Sentiment Analyst treats News Analyst article cards as independent sentiment evidence instead of event context;
- social reaction is described as confirming news when posts merely repeat headlines without reasoning;
- fundamentals claim lacks statement evidence citation;
- research evidence matrix missing direction, materiality, confidence, tool output, weight, or reason;
- research evidence matrix omits independence groups when News and Sentiment both support a material claim;
- Research Manager double-counts the same event across News, Sentiment, Bull/Bear, Risk, or duplicated news articles;
- research manager rating lacks rating-vs-rating justification;
- ASX Research Manager report omits ticker-specific moving-average facts, sector metric evidence, or explicit evidence gaps;
- multiple tickers in the same run use near-identical Research Manager rationale despite materially different market, financial, or sector evidence;
- generic "ASX source coverage is uneven" is the sole reason for Hold;
- complete_report.md omits or dilutes the Research Manager's rating-vs-rating reasoning, especially for ASX tickers where the final report must carry the actual 10 EMA / 50 SMA / 200 SMA setup, decisive role evidence, sector metric or evidence gap, and why-not-Buy / why-not-Sell reasoning;
- Research Manager rating is basically a moving-average rule, Trader BUY/SELL is triggered only by price above/below moving averages, complete_report.md hides rating/action tension, or all roles collapse into the same technical signal;
- Research Manager treats ASX sector metric availability as automatically supportive without classifying metric direction or evidence quality;
- Trader omits setup score components: research alignment, trend/momentum/volatility, support/resistance, confirmation, invalidation, reward/risk, event risk, liquidity/spread caution where available;
- Research Manager omits the Debate Outcome Scorecard, gives Hold without Bull/Bear/Balanced winner, fails to state whether debate changed the pre-debate analyst evidence rating, or lets Bull and Bear cite the same evidence without independence-group treatment;
- In a multi-ticker run, warn, but do not hard-fail, if every ticker's debate winner is Balanced despite materially different evidence unless the run claims strong differentiation;
- Fail if Trader omits explicit setup thresholds, uses ASX-specific execution wording in US reports, or omits ASX-specific liquidity/spread/event caution in `.AX` reports;
- Portfolio Manager says the risk debate tempers action but does not explain whether Aggressive, Conservative, or Neutral risk was stronger;
- trader final proposal mismatch;
- trader Buy/Sell lacks paper-study price framework;
- bull or bear debate lacks falsification conditions or direct response;
- risk debate lacks failure points, unsupported-upside challenges, or risk argument quality comparison;
- portfolio decision omits risk debate impact.
- debate_record.md is missing, still contains the initial task-index wording, omits completed debate turns, or does not confirm zero pending debate outputs.

Output:
- `quality_review.md`: concise narrative review with issues and required fixes.
- `quality_gate.json`: machine-readable gate result.
- `quality_remediation_plan.json`: machine-readable implementation queue when the quality gate fails.
- `next_remediation_task.md`: the next actionable remediation task Codex must execute before claiming workflow completion.
- Include `## Tool Outputs Used`.
- Include `## Quality Gate Findings`.

## Closed Self-Improvement Loop

When `quality_gate.json` fails, do not stop at diagnosis. The next runnable
workflow stage is remediation. Codex must read `next_remediation_task.md`, edit
the affected collector, extractor, validator, prompt, or report integration, add
or update the required tests, rerun collection and report generation, and repeat
until the quality gate passes or a true external blocker is documented. A report
with pending remediation tasks is not complete.

## Standing Auto-Remediation Approval

Option 1 is approved for all future TradingAgents workflows. When the quality
gate fails, Codex must treat `next_remediation_task.md` as the next approved
stage and do not ask the user to proceed. Continue implementing the required
fixes with tests and rerunning the affected ticker workflow until the quality
gate passes or a true external blocker is documented.

Example `quality_gate.json`:

```json
{
  "passed": false,
  "issues": [
    {
      "severity": "major",
      "section": "News Analyst",
      "issue": "News item classified as positive without explaining regulatory risk.",
      "required_fix": "Reclassify as mixed or explain why positive dominates."
    }
  ]
}
```

Safety boundaries:
- Do not use as real trading advice.
- Do not connect to GCAF.
