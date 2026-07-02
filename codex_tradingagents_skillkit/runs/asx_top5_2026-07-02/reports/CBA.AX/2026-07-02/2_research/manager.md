# Research Manager Report - CBA.AX

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:CBA.AX:2026-07-02:001 | negative | high | medium | market snapshot | -2 | negative across short, intermediate, and long-term trend measures | market:CBA.AX:2026-07-02:trend |
| Financial Report Analyst | financial:CBA.AX:2026-07-02:014 | positive | high | medium | filing section extraction | +2 | Exhibit 99.1 and 10-Q sections support financial quality | event:CBA.AX:2026-07-02:earnings |
| News Analyst | news:CBA.AX:2026-07-02:001 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:CBA.AX:2026-07-02:earnings |
| Sentiment Analyst | social:CBA.AX:2026-07-02:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:CBA.AX:2026-07-02:retail |
| Bear Researcher | fundamentals:CBA.AX:2026-07-02:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:CBA.AX:2026-07-02:valuation-trend |

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
* Evidence references: market:CBA.AX:2026-07-02:001, financial:CBA.AX:2026-07-02:014, news:CBA.AX:2026-07-02:001
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
