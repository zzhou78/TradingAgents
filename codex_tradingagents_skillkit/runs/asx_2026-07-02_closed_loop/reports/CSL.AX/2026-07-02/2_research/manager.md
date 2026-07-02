# Research Manager Report - CSL.AX

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:CSL.AX:2026-07-02:001 | mixed | high | medium | market snapshot | 0 | Hold is ticker-specific here: latest close 117.75 is above the 10 EMA (114.56), above the 50 SMA (109.07), and below the 200 SMA (155.14). The short/intermediate rebound improves the case versus Underweight, but the close remains below the 200 SMA, so long-term confirmation is still missing. | market:CSL.AX:2026-07-02:trend |
| Financial Report Analyst | financial:CSL.AX:2026-07-02:001 | positive | high | medium | filing section extraction | +2 | ASX document and sector-metric records support financial review with gaps disclosed | event:CSL.AX:2026-07-02:financial-report |
| News Analyst | news:CSL.AX:2026-07-02:001 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:CSL.AX:2026-07-02:earnings |
| Sentiment Analyst | social:CSL.AX:2026-07-02:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:CSL.AX:2026-07-02:retail |
| Bear Researcher | fundamentals:CSL.AX:2026-07-02:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:CSL.AX:2026-07-02:valuation-trend |

Score calculation / component weights: 0 market setup (short/intermediate rebound but still below the 200 SMA), +1 official ASX financial-source context, +1 sector metric availability breadth (6 available), -1 evidence-gap/source-depth cap (0 gaps), 0 retail sentiment = Hold with ticker-specific skew.

## Rating Rationale
**Recommendation**: Hold

Hold is ticker-specific here: latest close 117.75 is above the 10 EMA (114.56), above the 50 SMA (109.07), and below the 200 SMA (155.14). The short/intermediate rebound improves the case versus Underweight, but the close remains below the 200 SMA, so long-term confirmation is still missing. Hold beats Buy/Overweight and Sell/Underweight for ticker-specific reasons, not because of a generic ASX coverage caveat. The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Rating-vs-rating selection was explicitly considered; social sentiment alone has zero decision weight.

## Rating-vs-Rating Reasoning
1. Why not Buy / Overweight? Buy/Overweight is not selected because CSL.AX has a short/intermediate rebound but still below the 200 SMA setup and sector metric coverage is 6 available / 0 gap-labelled; that is not enough for an aggressive rating.
2. Why not Sell / Underweight? Sell/Underweight is not selected because the close has recovered above the 10 EMA and 50 SMA; the 200 SMA gap keeps conviction capped rather than forcing a Sell.
3. Which role evidence was decisive? Decisive evidence is Market Analyst (market:CSL.AX:2026-07-02:001, market:CSL.AX:2026-07-02:002, market:CSL.AX:2026-07-02:003, market:CSL.AX:2026-07-02:004) plus Financial Report Analyst / ASX sector metrics (financial:CSL.AX:2026-07-02:017); News (news:CSL.AX:2026-07-02:001) is contextual and Sentiment is low weight.
4. Which sector-specific financial metrics mattered? healthcare metric evidence: R&D is available via financial:CSL.AX:2026-07-02:017.
5. Which evidence gaps capped confidence? Confidence is capped by role-level source limitations and low-confidence retail sentiment from social:CSL.AX:2026-07-02:001, not by sector metrics alone.
6. How market setup changed the final rating. The short/intermediate rebound improves the case versus Underweight, but the close remains below the 200 SMA, so long-term confirmation is still missing.

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:CSL.AX:2026-07-02:001, financial:CSL.AX:2026-07-02:001, news:CSL.AX:2026-07-02:001
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
