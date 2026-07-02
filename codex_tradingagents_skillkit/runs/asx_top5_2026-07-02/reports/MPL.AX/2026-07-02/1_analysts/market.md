# Market Analyst Report - MPL.AX

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records market:MPL.AX:2026-07-02:001 through market:MPL.AX:2026-07-02:007.
- Source date for price metrics: 2026-07-02; trade date: 2026-07-02.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | 4.99 | market:MPL.AX:2026-07-02:001 | Reference price |
| 10 EMA | 4.94 | market:MPL.AX:2026-07-02:002 | Close is above 10 EMA |
| 50 SMA | 4.77 | market:MPL.AX:2026-07-02:003 | Close is above 50 SMA |
| 200 SMA | 4.63 | market:MPL.AX:2026-07-02:004 | Close is above 200 SMA |
| RSI 14 | 60.91 | market:MPL.AX:2026-07-02:005 | Momentum oscillator |
| MACD | 0.06 | market:MPL.AX:2026-07-02:006 | Trend momentum |
| ATR 14 | 0.09 | market:MPL.AX:2026-07-02:007 | Volatility / level spacing |

Interpretation: MPL.AX has a constructive but not trend-confirmed because MACD remains negative. This statement is mechanical from the table: the close is above the 10 EMA, above the 50 SMA, and above the 200 SMA. MACD is 0.06, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after 2026-07-02 is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:MPL.AX:2026-07-02:001, market:MPL.AX:2026-07-02:002, market:MPL.AX:2026-07-02:003, market:MPL.AX:2026-07-02:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
