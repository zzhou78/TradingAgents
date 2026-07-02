# Market Analyst Report - CBA.AX

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records market:CBA.AX:2026-07-02:001 through market:CBA.AX:2026-07-02:007.
- Source date for price metrics: 2026-07-02; trade date: 2026-07-02.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | 161.14 | market:CBA.AX:2026-07-02:001 | Reference price |
| 10 EMA | 162.47 | market:CBA.AX:2026-07-02:002 | Close is below 10 EMA |
| 50 SMA | 165.51 | market:CBA.AX:2026-07-02:003 | Close is below 50 SMA |
| 200 SMA | 164.47 | market:CBA.AX:2026-07-02:004 | Close is below 200 SMA |
| RSI 14 | 44.79 | market:CBA.AX:2026-07-02:005 | Momentum oscillator |
| MACD | -0.71 | market:CBA.AX:2026-07-02:006 | Trend momentum |
| ATR 14 | 3.11 | market:CBA.AX:2026-07-02:007 | Volatility / level spacing |

Interpretation: CBA.AX has a negative across short, intermediate, and long-term trend measures. This statement is mechanical from the table: the close is below the 10 EMA, below the 50 SMA, and below the 200 SMA. MACD is -0.71, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after 2026-07-02 is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:CBA.AX:2026-07-02:001, market:CBA.AX:2026-07-02:002, market:CBA.AX:2026-07-02:003, market:CBA.AX:2026-07-02:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
