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
4. Flag unsupported reasoning, missing ambiguity, overconfident social/news interpretation, contradictory ratings/actions, and unexplained primary drivers.
5. Fail or warn when financial_report.md is missing; financial report source coverage is unclear; fundamentals only lists ratios and omits financial statement data; industry_theme.md is missing; themes are preconfigured without evidence support; complete_report.md omits Financial Report Analyst or Industry / Theme Discovery Analyst sections; Research Manager ignores material financial-report or theme evidence; Portfolio Manager merely repeats Trader; or quality_gate.json passes despite missing role outputs.
6. Fail or warn when the News Analyst treats political-trading or celebrity-trading headlines as material without a direct link to company fundamentals, regulation, price action, or sentiment.
7. Require fixes that are specific enough for Codex to apply in a second report-writing pass.

Output:
- `quality_review.md`: concise narrative review with issues and required fixes.
- `quality_gate.json`: machine-readable gate result.

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
