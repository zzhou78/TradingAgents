# Research Manager Report - WOW.AX

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:WOW.AX:2026-07-02:001 | negative | high | medium | market snapshot | -2 | constructive but not trend-confirmed because MACD remains negative | market:WOW.AX:2026-07-02:trend |
| Financial Report Analyst | financial:WOW.AX:2026-07-02:001 | positive | high | medium | filing section extraction | +2 | ASX document and sector-metric records support financial review with gaps disclosed | event:WOW.AX:2026-07-02:financial-report |
| News Analyst | news:WOW.AX:2026-07-02:003 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:WOW.AX:2026-07-02:earnings |
| Sentiment Analyst | social:WOW.AX:2026-07-02:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:WOW.AX:2026-07-02:retail |
| Bear Researcher | fundamentals:WOW.AX:2026-07-02:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:WOW.AX:2026-07-02:valuation-trend |

Score calculation / component weights: 0 market/technical balance, +1 available official-source evidence, 0 low-confidence sentiment, -1 unavailable section risk = 0.

## Rating Rationale
**Recommendation**: Hold

Hold beats Buy because ASX source coverage is uneven and any missing MD&A, cash-flow, or segment section must be treated as an evidence gap; it beats Sell where available official-source records still support a reviewable base case and the quality gate has not identified a completed negative fundamental case. The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Hold vs Sell/Buy was explicitly considered: Hold beats Hold or Sell only to the degree justified above; social sentiment alone has zero decision weight.

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:WOW.AX:2026-07-02:001, financial:WOW.AX:2026-07-02:001, news:WOW.AX:2026-07-02:003
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
