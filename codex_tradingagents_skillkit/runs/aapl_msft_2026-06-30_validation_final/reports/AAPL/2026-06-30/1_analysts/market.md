# Market Analyst

## Tool Outputs Used

- get_verified_market_snapshot and market_data_evidence: market:AAPL:2026-06-30:001, market:AAPL:2026-06-30:009, market:AAPL:2026-06-30:010, market:AAPL:2026-06-30:011.

## Quantitative Regime / Tool Outputs

Latest close: 281.74. 10 EMA: 289.33. 50 SMA: 291.78. 200 SMA: 269.35.
RSI: 39.91. MACD: -2.9. ATR: 8.18. Volume: 66368400.
The latest close is below the 10 EMA and below the 50 SMA. It is above the 200 SMA, based on market:AAPL:2026-06-30:011.
Interpretation: near-term weak, long-term support intact. This is a paper-study technical read, not a broker instruction.

## Evidence Gaps

The market packet uses the latest verified close from 2026-06-29; it does not include intraday confirmation after that close.

## Memory Update

* Durable facts to retain: AAPL market_analyst used market:AAPL:2026-06-30:001 for this 2026-06-30 validation run.
* Prior mistake to avoid: Do not override current evidence with template language.
* Open questions: Refresh evidence for any later trade date.
* Evidence references: market:AAPL:2026-06-30:001
* Staleness / expiry: Expires after 2026-06-30.
