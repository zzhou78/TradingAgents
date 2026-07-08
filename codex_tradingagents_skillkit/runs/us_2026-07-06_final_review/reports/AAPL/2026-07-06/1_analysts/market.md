# Market Analyst Report - AAPL

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records market:AAPL:2026-07-06:001 through market:AAPL:2026-07-06:007.
- Source date for price metrics: 2026-07-06; trade date: 2026-07-06.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | 312.66 | market:AAPL:2026-07-06:001 | Reference price |
| 10 EMA | 297.06 | market:AAPL:2026-07-06:002 | Close is above 10 EMA |
| 50 SMA | 294.25 | market:AAPL:2026-07-06:003 | Close is above 50 SMA |
| 200 SMA | 270.70 | market:AAPL:2026-07-06:004 | Close is above 200 SMA |
| RSI 14 | 62.44 | market:AAPL:2026-07-06:005 | Momentum oscillator |
| MACD | 0.89 | market:AAPL:2026-07-06:006 | Trend momentum |
| ATR 14 | 8.63 | market:AAPL:2026-07-06:007 | Volatility / level spacing |

Interpretation: AAPL has a constructive but not trend-confirmed because MACD remains negative. This statement is mechanical from the table: the close is above the 10 EMA, above the 50 SMA, and above the 200 SMA. MACD is 0.89, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after 2026-07-06 is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:AAPL:2026-07-06:001, market:AAPL:2026-07-06:002, market:AAPL:2026-07-06:003, market:AAPL:2026-07-06:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
