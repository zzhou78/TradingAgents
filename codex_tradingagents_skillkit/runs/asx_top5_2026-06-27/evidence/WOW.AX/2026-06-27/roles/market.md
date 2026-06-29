# Codex Role Evidence Packet: WOW.AX / market

- Trade date: `2026-06-27`
- Instrument identity: `Woolworths Group Limited`
- Skill: `tradingagents-market-analyst`

Read only this packet when acting this analyst role. Do not inspect other analyst role packets until the workflow advances to a downstream debate stage.

## Role: market

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for WOW.AX from 2026-05-28 to 2026-06-27
# Total records: 21
# Data retrieved on: 2026-06-29 13:54:32

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-05-28,34.8,35.06,34.64,34.94,1961645,0.0,0.0
2026-05-29,35.0,35.23,34.68,35.23,6130955,0.0,0.0
2026-06-01,34.81,35.14,34.48,35.06,1306915,0.0,0.0
2026-06-02,34.71,35.02,34.26,34.41,2496839,0.0,0.0
2026-06-03,34.3,35.19,34.25,35.09,1890873,0.0,0.0
2026-06-04,35.29,35.59,35.14,35.26,1427129,0.0,0.0
2026-06-05,35.26,35.8,35.1,35.69,1754868,0.0,0.0
2026-06-09,36.0,36.63,35.9,36.48,2781321,0.0,0.0
2026-06-10,36.58,37.63,36.58,37.63,2237739,0.0,0.0
2026-06-11,37.68,38.09,37.63,38.09,2377238,0.0,0.0
2026-06-12,38.15,38.5,38.09,38.33,2199640,0.0,0.0
2026-06-15,38.19,38.46,37.95,38.23,3411482,0.0,0.0
2026-06-16,38.01,38.28,37.88,38.26,1501664,0.0,0.0
2026-06-17,37.99,38.2,37.73,37.78,2278310,0.0,0.0
2026-06-18,37.75,38.3,37.7,38.12,3777467,0.0,0.0
2026-06-19,38.2,38.42,37.92,38.32,5103756,0.0,0.0
2026-06-22,38.01,38.55,38.01,38.55,1438982,0.0,0.0
2026-06-23,38.6,38.8,38.4,38.74,2019982,0.0,0.0
2026-06-24,38.81,39.38,38.76,39.37,3127670,0.0,0.0
2026-06-25,39.5,40.1,39.43,39.94,2464394,0.0,0.0
2026-06-26,39.8,40.24,39.52,40.24,1677574,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for WOW.AX

- Requested analysis date: 2026-06-27
- Latest trading row used: 2026-06-26
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 39.80 |
| High | 40.24 |
| Low | 39.52 |
| Close | 40.24 |
| Volume | 1677574 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 38.82 |
| close_50_sma | 36.00 |
| close_200_sma | 31.74 |
| rsi | 79.97 |
| boll | 37.44 |
| boll_ub | 40.95 |
| boll_lb | 33.93 |
| macd | 1.20 |
| macds | 0.95 |
| macdh | 0.24 |
| atr | 0.62 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-15 | 32.98 |
| 2026-05-18 | 32.98 |
| 2026-05-19 | 34.21 |
| 2026-05-20 | 34.43 |
| 2026-05-21 | 34.49 |
| 2026-05-22 | 34.68 |
| 2026-05-25 | 34.75 |
| 2026-05-26 | 34.49 |
| 2026-05-27 | 34.62 |
| 2026-05-28 | 34.94 |
| 2026-05-29 | 35.23 |
| 2026-06-01 | 35.06 |
| 2026-06-02 | 34.41 |
| 2026-06-03 | 35.09 |
| 2026-06-04 | 35.26 |
| 2026-06-05 | 35.69 |
| 2026-06-09 | 36.48 |
| 2026-06-10 | 37.63 |
| 2026-06-11 | 38.09 |
| 2026-06-12 | 38.33 |
| 2026-06-15 | 38.23 |
| 2026-06-16 | 38.26 |
| 2026-06-17 | 37.78 |
| 2026-06-18 | 38.12 |
| 2026-06-19 | 38.32 |
| 2026-06-22 | 38.55 |
| 2026-06-23 | 38.74 |
| 2026-06-24 | 39.37 |
| 2026-06-25 | 39.94 |
| 2026-06-26 | 40.24 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 36.000799865722655
2026-06-25: 35.9313998413086
2026-06-24: 35.86759986877441
2026-06-23: 35.821599884033205
2026-06-22: 35.78999984741211
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 35.755599899291994
2026-06-18: 35.73279991149902
2026-06-17: 35.70599990844727
2026-06-16: 35.7007999420166
2026-06-15: 35.6757999420166
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 35.642199935913084
2026-06-11: 35.60379989624023
2026-06-10: 35.575599899291994
2026-06-09: 35.54799987792969
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 35.54579986572266
2026-06-04: 35.55959991455078
2026-06-03: 35.581999969482425
2026-06-02: 35.60979995727539
2026-06-01: 35.649999923706055
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 35.68359992980957
2026-05-28: 35.69939994812012


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 31.741845932006836
2026-06-25: 31.678592882156373
2026-06-24: 31.615308752059935
2026-06-23: 31.555467290878298
2026-06-22: 31.49803496360779
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 31.441947774887083
2026-06-18: 31.384442291259766
2026-06-17: 31.331394128799438
2026-06-16: 31.282268524169922
2026-06-15: 31.23098600387573
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 31.177617092132568
2026-06-11: 31.124574661254883
2026-06-10: 31.09660327911377
2026-06-09: 31.066993894577028
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 31.045614004135132
2026-06-04: 31.030566358566283
2026-06-03: 31.013439025878906
2026-06-02: 30.995119743347168
2026-06-01: 30.980686626434327
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 30.962663192749023
2026-05-28: 30.944421787261962


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 79.97365318769866
2026-06-25: 78.75947945416164
2026-06-24: 76.21534392045594
2026-06-23: 72.88172022535234
2026-06-22: 71.77380142277075
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 70.41518204662178
2026-06-18: 69.21885426010432
2026-06-17: 67.12003308671213
2026-06-16: 73.70851478456476
2026-06-15: 73.55788618844632
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 74.88593562607443
2026-06-11: 73.83310919497966
2026-06-10: 71.72338753883584
2026-06-09: 65.21226335779808
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 59.22275825743482
2026-06-04: 55.336084926735374
2026-06-03: 53.71660256719244
2026-06-02: 46.51303625021797
2026-06-01: 53.96867125284401
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 56.154623405634375
2026-05-28: 53.148603082853974


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 1.1987773763184961
2026-06-25: 1.125072502459652
2026-06-24: 1.0451793559684646
2026-06-23: 0.9860403727422735
2026-06-22: 0.960360294532606
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 0.9329600026404279
2026-06-18: 0.9078350743418895
2026-06-17: 0.8829253697315238
2026-06-16: 0.8729071750962447
2026-06-15: 0.798550803459932
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 0.6950841713222076
2026-06-11: 0.5427307580402356
2026-06-10: 0.36481467041454607
2026-06-09: 0.17925892105804309
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 0.05690597202620751
2026-06-04: -0.019652149295666277
2026-06-03: -0.07330045272065888
2026-06-02: -0.1234001034872847
2026-06-01: -0.11631417061533966
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: -0.17176007463022813
2026-05-28: -0.25733978641630983


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 0.6178991909582667
2026-06-25: 0.6100451886702007
2026-06-24: 0.60120233481265
2026-06-23: 0.5982179459791279
2026-06-22: 0.6134656563481653
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 0.6191167902574592
2026-06-18: 0.6282796202772637
2026-06-17: 0.6304550930585076
2026-06-16: 0.6381825018094024
2026-06-15: 0.6561197112334429
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 0.6673598181334613
2026-06-11: 0.6871567389581807
2026-06-10: 0.7046304046878364
2026-06-09: 0.6703710876731387
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 0.6496302143090532
2026-06-04: 0.6457555567220994
2026-06-03: 0.6569675226237994
2026-06-02: 0.6351958992326314
2026-06-01: 0.6225184259614637
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 0.6127121510354224
2026-05-28: 0.617536221341182


ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.
```
