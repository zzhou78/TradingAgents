# Market Analyst Report - CBA.AX

## Tool Outputs Used
- get_verified_market_snapshot via market evidence records market:CBA.AX:2026-07-06:001 through market:CBA.AX:2026-07-06:007.
- Source date for price metrics: 2026-07-06; trade date: 2026-07-06.

## Quantitative Regime / Tool Outputs
| Metric | Value | Evidence ID | Relation / use |
|---|---:|---|---|
| Latest close | 164.66 | market:CBA.AX:2026-07-06:001 | Reference price |
| 10 EMA | 163.25 | market:CBA.AX:2026-07-06:002 | Close is above 10 EMA |
| 50 SMA | 165.15 | market:CBA.AX:2026-07-06:003 | Close is below 50 SMA |
| 200 SMA | 164.47 | market:CBA.AX:2026-07-06:004 | Close is above 200 SMA |
| RSI 14 | 52.67 | market:CBA.AX:2026-07-06:005 | Momentum oscillator |
| MACD | -0.28 | market:CBA.AX:2026-07-06:006 | Trend momentum |
| ATR 14 | 3.06 | market:CBA.AX:2026-07-06:007 | Volatility / level spacing |

Interpretation: CBA.AX has a mixed technical regime. This statement is mechanical from the table: the close is above the 10 EMA, below the 50 SMA, and above the 200 SMA. MACD is -0.28, so momentum confirmation is not clean even where price has recovered above a moving average.

## Evidence Gaps
- Intraday price action after 2026-07-06 is not used.
- The market analyst does not make a fundamental recommendation from technical metrics alone.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:CBA.AX:2026-07-06:001, market:CBA.AX:2026-07-06:002, market:CBA.AX:2026-07-06:003, market:CBA.AX:2026-07-06:004
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
