# Market Analyst Report - MSFT

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records market:MSFT:2026-07-02:001 through market:MSFT:2026-07-02:007.
- Source date for price metrics: 2026-07-02; trade date: 2026-07-02.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | 386.57 | market:MSFT:2026-07-02:001 | Reference price |
| 10 EMA | 378.57 | market:MSFT:2026-07-02:002 | Close is above 10 EMA |
| 50 SMA | 407.14 | market:MSFT:2026-07-02:003 | Close is below 50 SMA |
| 200 SMA | 443.77 | market:MSFT:2026-07-02:004 | Close is below 200 SMA |
| RSI 14 | 48.08 | market:MSFT:2026-07-02:005 | Momentum oscillator |
| MACD | -10.11 | market:MSFT:2026-07-02:006 | Trend momentum |
| ATR 14 | 12.72 | market:MSFT:2026-07-02:007 | Volatility / level spacing |

Interpretation: MSFT has a short rebound inside a still-negative intermediate and long-term trend. This statement is mechanical from the table: the close is above the 10 EMA, below the 50 SMA, and below the 200 SMA. MACD is -10.11, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after 2026-07-02 is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:MSFT:2026-07-02:001, market:MSFT:2026-07-02:002, market:MSFT:2026-07-02:003, market:MSFT:2026-07-02:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
