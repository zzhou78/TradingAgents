# Market Analyst Report - MSFT

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records market:MSFT:2026-07-06:001 through market:MSFT:2026-07-06:007.
- Source date for price metrics: 2026-07-06; trade date: 2026-07-06.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | 386.74 | market:MSFT:2026-07-06:001 | Reference price |
| 10 EMA | 380.64 | market:MSFT:2026-07-06:002 | Close is above 10 EMA |
| 50 SMA | 406.31 | market:MSFT:2026-07-06:003 | Close is below 50 SMA |
| 200 SMA | 443.19 | market:MSFT:2026-07-06:004 | Close is below 200 SMA |
| RSI 14 | 48.16 | market:MSFT:2026-07-06:005 | Momentum oscillator |
| MACD | -8.57 | market:MSFT:2026-07-06:006 | Trend momentum |
| ATR 14 | 12.79 | market:MSFT:2026-07-06:007 | Volatility / level spacing |

Interpretation: MSFT has a short rebound inside a still-negative intermediate and long-term trend. This statement is mechanical from the table: the close is above the 10 EMA, below the 50 SMA, and below the 200 SMA. MACD is -8.57, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after 2026-07-06 is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:MSFT:2026-07-06:001, market:MSFT:2026-07-06:002, market:MSFT:2026-07-06:003, market:MSFT:2026-07-06:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
