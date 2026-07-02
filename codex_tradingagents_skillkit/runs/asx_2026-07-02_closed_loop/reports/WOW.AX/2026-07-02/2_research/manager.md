# Research Manager Report - WOW.AX

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:WOW.AX:2026-07-02:001 | positive | high | medium | market snapshot | +1 | Hold is ticker-specific here: latest close 39.35 is above the 10 EMA (39.31), above the 50 SMA (36.18), and above the 200 SMA (31.99). The above-all-averages setup removes the technical objection to Hold, but the rating is capped because the Research Manager needs stronger sector metric breadth and cleaner source depth before Overweight. | market:WOW.AX:2026-07-02:trend |
| Financial Report Analyst | financial:WOW.AX:2026-07-02:001 | positive | high | medium | filing section extraction | +2 | ASX document and sector-metric records support financial review with gaps disclosed | event:WOW.AX:2026-07-02:financial-report |
| News Analyst | news:WOW.AX:2026-07-02:003 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:WOW.AX:2026-07-02:earnings |
| Sentiment Analyst | social:WOW.AX:2026-07-02:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:WOW.AX:2026-07-02:retail |
| Bear Researcher | fundamentals:WOW.AX:2026-07-02:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:WOW.AX:2026-07-02:valuation-trend |

Score calculation / component weights: +1 market setup (positive across 10 EMA, 50 SMA, and 200 SMA), +1 official ASX financial-source context, +1 sector metric availability breadth (5 available), -1 evidence-gap/source-depth cap (0 gaps), 0 retail sentiment = Hold with ticker-specific skew.

## Rating Rationale
**Recommendation**: Hold

Hold is ticker-specific here: latest close 39.35 is above the 10 EMA (39.31), above the 50 SMA (36.18), and above the 200 SMA (31.99). The above-all-averages setup removes the technical objection to Hold, but the rating is capped because the Research Manager needs stronger sector metric breadth and cleaner source depth before Overweight. Hold beats Buy/Overweight and Sell/Underweight for ticker-specific reasons, not because of a generic ASX coverage caveat. The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Rating-vs-rating selection was explicitly considered; social sentiment alone has zero decision weight.

## Rating-vs-Rating Reasoning
1. Why not Buy / Overweight? Buy/Overweight is not selected because WOW.AX has a positive across 10 EMA, 50 SMA, and 200 SMA setup and sector metric coverage is 5 available / 0 gap-labelled; that is not enough for an aggressive rating.
2. Why not Sell / Underweight? Sell/Underweight is not selected because price is above the 10 EMA, 50 SMA, and 200 SMA, so market evidence does not support a bearish rating without a separate negative financial catalyst.
3. Which role evidence was decisive? Decisive evidence is Market Analyst (market:WOW.AX:2026-07-02:001, market:WOW.AX:2026-07-02:002, market:WOW.AX:2026-07-02:003, market:WOW.AX:2026-07-02:004) plus Financial Report Analyst / ASX sector metrics (financial:WOW.AX:2026-07-02:016); News (news:WOW.AX:2026-07-02:003) is contextual and Sentiment is low weight.
4. Which sector-specific financial metrics mattered? retailers metric evidence: Sales growth is available via financial:WOW.AX:2026-07-02:016.
5. Which evidence gaps capped confidence? Confidence is capped by role-level source limitations and low-confidence retail sentiment from social:WOW.AX:2026-07-02:001, not by sector metrics alone.
6. How market setup changed the final rating. The above-all-averages setup removes the technical objection to Hold, but the rating is capped because the Research Manager needs stronger sector metric breadth and cleaner source depth before Overweight.

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:WOW.AX:2026-07-02:001, financial:WOW.AX:2026-07-02:001, news:WOW.AX:2026-07-02:003
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
