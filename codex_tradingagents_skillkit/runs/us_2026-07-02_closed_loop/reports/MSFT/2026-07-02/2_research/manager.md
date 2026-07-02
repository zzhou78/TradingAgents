# Research Manager Report - MSFT

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:MSFT:2026-07-02:001 | negative | high | medium | market snapshot | -2 | short rebound inside a still-negative intermediate and long-term trend | market:MSFT:2026-07-02:trend |
| Financial Report Analyst | financial:MSFT:2026-07-02:022 | positive | high | medium | filing section extraction | +2 | Exhibit 99.1 and 10-Q sections support financial review with gaps disclosed | event:MSFT:2026-07-02:financial-report |
| News Analyst | news:MSFT:2026-07-02:033 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:MSFT:2026-07-02:earnings |
| Sentiment Analyst | social:MSFT:2026-07-02:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:MSFT:2026-07-02:retail |
| Bear Researcher | fundamentals:MSFT:2026-07-02:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:MSFT:2026-07-02:valuation-trend |

Score calculation / component weights: -2 market trend, +2 financial quality, +1 earnings/news, 0 low-confidence retail sentiment, -1 capex/trend risk = 0 with negative technical skew.

## Rating Rationale
**Recommendation**: Underweight

Underweight beats Hold because the strongest financial evidence is positive, but the market evidence still shows the close below both 50 SMA and 200 SMA; it does not become Sell because the company fundamentals and Exhibit 99.1 evidence remain strong and price is above the 10 EMA. The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Rating-vs-rating selection was explicitly considered; social sentiment alone has zero decision weight.

## Rating-vs-Rating Reasoning
1. Why not Buy / Overweight? Underweight beats Hold because the strongest financial evidence is positive, but the market evidence still shows the close below both 50 SMA and 200 SMA; it does not become Sell because the company fundamentals and Exhibit 99.1 evidence remain strong and price is above the 10 EMA.
2. Why not Sell / Underweight? Underweight is not a Sell because the evidence mix is not a clean long-term breakdown or negative fundamental case.
3. Decisive role evidence: Market and Financial Report evidence outweighed low-confidence social evidence.
4. Sector-specific financial metrics: not applicable for non-ASX tickers in this workflow.
5. Evidence gaps capping confidence: social data is low confidence and news/filing evidence remains as-of-date limited.
6. Market setup impact: short rebound inside a still-negative intermediate and long-term trend.

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:MSFT:2026-07-02:001, financial:MSFT:2026-07-02:022, news:MSFT:2026-07-02:033
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
