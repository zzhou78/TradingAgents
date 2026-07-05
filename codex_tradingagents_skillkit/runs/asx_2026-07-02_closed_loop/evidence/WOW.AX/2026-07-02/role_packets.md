# Codex Role Evidence Packet: WOW.AX

- Trade date: `2026-07-02`
- Instrument identity: `Woolworths Group Limited`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for WOW.AX from 2026-06-02 to 2026-07-02
# Total records: 22
# Data retrieved on: 2026-07-05 15:17:27

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
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
2026-06-29,40.15,40.75,40.04,40.55,1737667,0.0,0.0
2026-06-30,40.5,40.6,39.97,40.03,2447455,0.0,0.0
2026-07-01,39.67,39.9,38.75,39.31,3008386,0.0,0.0
2026-07-02,38.78,39.47,38.63,39.35,2879516,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for WOW.AX

- Requested analysis date: 2026-07-02
- Latest trading row used: 2026-07-02
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 38.78 |
| High | 39.47 |
| Low | 38.63 |
| Close | 39.35 |
| Volume | 2879516 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 39.31 |
| close_50_sma | 36.18 |
| close_200_sma | 31.99 |
| rsi | 64.23 |
| boll | 38.41 |
| boll_ub | 41.24 |
| boll_lb | 35.59 |
| macd | 1.12 |
| macds | 1.10 |
| macdh | 0.03 |
| atr | 0.68 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
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
| 2026-06-29 | 40.55 |
| 2026-06-30 | 40.03 |
| 2026-07-01 | 39.31 |
| 2026-07-02 | 39.35 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-06-02 to 2026-07-02:

2026-07-02: 36.180599746704104
2026-07-01: 36.156599807739255
2026-06-30: 36.126799774169925
2026-06-29: 36.07599983215332
2026-06-28: N/A: Not a trading day (weekend or holiday)
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


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-06-02 to 2026-07-02:

2026-07-02: 31.985961780548095
2026-07-01: 31.92671422958374
2026-06-30: 31.868802633285522
2026-06-29: 31.80679715156555
2026-06-28: N/A: Not a trading day (weekend or holiday)
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


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-06-02 to 2026-07-02:

2026-07-02: 64.22952575059672
2026-07-01: 63.95788785555769
2026-06-30: 73.25678021343322
2026-06-29: 81.17136361465077
2026-06-28: N/A: Not a trading day (weekend or holiday)
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


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-06-02 to 2026-07-02:

2026-07-02: 1.124212967184377
2026-07-01: 1.1921428323778684
2026-06-30: 1.2655782148384063
2026-06-29: 1.2675912294425231
2026-06-28: N/A: Not a trading day (weekend or holiday)
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


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-06-02 to 2026-07-02:

2026-07-02: 0.6836905870335797
2026-07-01: 0.6716667742986328
2026-06-30: 0.6248720046833829
2026-06-29: 0.6244777547807231
2026-06-28: N/A: Not a trading day (weekend or holiday)
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


ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.
```

## Role: social

- Skill: `tradingagents-sentiment-analyst`

### Tool: fetch_stocktwits_messages

- Status: `ok`

```text
<stocktwits unavailable: HTTPError>
```

### Tool: fetch_reddit_posts

- Status: `ok`

```text
<no Reddit posts found mentioning WOW.AX across r/wallstreetbets, r/stocks, r/investing in the past 7 days>
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
## WOW.AX News, from 2026-06-25 to 2026-07-02:

### Australia bans supermarket price-gouging from July (source: Retail Insight Network)
The measures will prevent large supermarket operators from setting prices above supply costs by more than a "reasonable margin".
Link: https://www.retail-insight-network.com/news/australia-bans-supermarket-price-gouging/

### Australia grocery giants set to face “price gouging” laws (source: Just Drinks)
The maximum penalty for every violation will be determined by the greatest of $10m, three times the benefit gained, or 10% of annual turnover.
Link: https://www.just-drinks.com/news/australia-grocery-price-gouging-laws/

### ADUSA tapped a former Amazon exec to helm its business. What does this mean? (source: Grocery Dive)
The grocery company’s nominee for the top role may raise some eyebrows given Amazon’s brick-and-mortar track record, but Claire Peters' appointment could be the key to further omnichannel growth.
Link: https://www.grocerydive.com/news/ahold-delhaize-usa-adusa-ceo-claire-peters-amazon-executive-changes/823756/


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-25 and 2026-07-02
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for WOW.AX
# Data retrieved on: 2026-07-05 15:17:40

,Shares,URL,Text,Insider,Position,Transaction,Start Date,Ownership,Value
0,1000,,,Meyer (Kenneth),Director (Non-Executive),,2026-06-17,D,
1,4027,,Purchase at price 24.97 per share.,Perkins (Scott Redvers),Independent Chairman Of The Board,,2026-06-01,D,100558.0
2,7170,,,Fellows (Tracey),Former,,2026-03-01,D,
3,3158,,,Bray (Warwick),Independent Non-Executive Director,,2026-02-26,D,
4,701,,,Fellows (Tracey),Independent Non-Executive Director,,2026-02-26,D,
5,12738,,,Bardwell (Amanda),Chief Executive Officer,,2025-08-28,D,
6,1592,,,Bray (Warwick),Independent Non-Executive Director,,2025-08-28,D,
7,664,,,Fellows (Tracey),Independent Non-Executive Director,,2025-08-28,D,
8,1103,,,Kramer (Holly S),Independent Non-Executive Director,,2025-08-28,D,
9,2480,,,Davis (Natalie),Divisional Officer,,2025-06-30,D,
10,2229,,,Harrison (Stephen),Chief Financial Officer,,2025-06-30,D,
11,44976,,,Karantoni (Annette),Divisional Officer,,2025-06-30,D,
12,470,,Purchase at price 20.77 per share.,Brenner (Maxine Nicole),Independent Non-Executive Director,,2025-05-06,D,9763.0
13,625,,Purchase at price 21.11 per share.,Brenner (Maxine Nicole),Independent Non-Executive Director,,2025-05-05,D,13193.0
14,1490,,,Bray (Warwick),Independent Non-Executive Director,,2025-02-28,D,
15,620,,,Fellows (Tracey),Independent Non-Executive Director,,2025-02-28,D,
16,1033,,,Kramer (Holly S),Independent Non-Executive Director,,2025-02-28,D,
17,1676,,Purchase at price 19.89 per share.,Fellows (Tracey),Independent Non-Executive Director,,2024-11-07,D,33342.0
18,8000,,Purchase at price 19.66 per share.,Chronican (Philip Wayne),Independent Non-Executive Director,,2024-11-05,D,157275.0
19,8860,,,Bardwell (Amanda),Chief Executive Officer,,2024-09-01,D,
20,1100,,Purchase at price 24.26 per share.,Brenner (Maxine Nicole),Independent Non-Executive Director,,2024-08-30,D,26688.0
21,22569,,,Banducci (Bradford Leon),Chief Executive Officer,,2024-08-29,D,
22,1930,,,Bray (Warwick),Independent Non-Executive Director,,2024-08-29,D,
23,618,,,Fellows (Tracey),Independent Non-Executive Director,,2024-08-29,D,
24,1027,,,Kramer (Holly S),Independent Non-Executive Director,,2024-08-29,D,

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for WOW.AX
# Data retrieved on: 2026-07-05 15:17:40

Name: Woolworths Group Limited
Sector: Consumer Defensive
Industry: Grocery Stores
Market Cap: 48595214336
PE Ratio (TTM): 81.18367
Forward PE: 28.190971
PEG Ratio: 2.16
Price to Book: 10.484976
EPS (TTM): 0.49
Forward EPS: 1.41109
Dividend Yield: 2.26
Beta: 0.27
52 Week High: 40.75
52 Week Low: 25.51
50 Day Average: 36.1744
200 Day Average: 32.4441
Revenue (TTM): 70282002432
Gross Profit: 19207999488
EBITDA: 3300000000
Net Income: 598000000
Profit Margin: 0.00851
Operating Margin: 0.025910001
Return on Equity: 0.1188
Return on Assets: 0.03636
Debt to Equity: 361.53
Current Ratio: 0.557
Book Value: 3.794
Free Cash Flow: 2267749888
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for WOW.AX (quarterly)
# Data retrieved on: 2026-07-05 15:17:40

,2025-06-30
Ordinary Shares Number,1221595333.0
Share Issued,1221595333.0
Net Debt,4236000000.0
Total Debt,17385000000.0
Tangible Book Value,151000000.0
Invested Capital,10371000000.0
Working Capital,-5306000000.0
Net Tangible Assets,151000000.0
Capital Lease Obligations,11874000000.0
Common Stock Equity,4860000000.0
Total Capitalization,10127000000.0
Total Equity Gross Minority Interest,4962000000.0
Minority Interest,102000000.0
Stockholders Equity,4860000000.0
Gains Losses Not Affecting Retained Earnings,-7479000000.0
Other Equity Adjustments,-7545000000.0
Foreign Currency Translation Adjustments,66000000.0
Retained Earnings,6712000000.0
Capital Stock,5627000000.0
Common Stock,5627000000.0
Total Liabilities Net Minority Interest,28867000000.0
Total Non Current Liabilities Net Minority Interest,16570000000.0
Other Non Current Liabilities,58000000.0
Derivative Product Liabilities,46000000.0
Employee Benefits,165000000.0
Non Current Pension And Other Postretirement Benefit Plans,165000000.0
Non Current Deferred Liabilities,61000000.0
Non Current Deferred Taxes Liabilities,61000000.0
Long Term Debt And Capital Lease Obligation,15442000000.0
Long Term Capital Lease Obligation,10175000000.0
Long Term Debt,5267000000.0
Long Term Provisions,798000000.0
Current Liabilities,12297000000.0
Other Current Liabilities,11000000.0
Current Deferred Liabilities,127000000.0
Current Deferred Taxes Liabilities,127000000.0
Current Debt And Capital Lease Obligation,1943000000.0
Current Capital Lease Obligation,1699000000.0
Current Debt,244000000.0
Other Current Borrowings,244000000.0
Pensionand Other Post Retirement Benefit Plans Current,1401000000.0
Current Provisions,732000000.0
Payables And Accrued Expenses,8083000000.0
Payables,8083000000.0
Other Payable,2067000000.0
Accounts Payable,6016000000.0
Total Assets,33829000000.0
Total Non Current Assets,26838000000.0
Other Non Current Assets,27000000.0
Non Current Deferred Assets,1853000000.0
Non Current Deferred Taxes Assets,1853000000.0
Non Current Accounts Receivable,455000000.0
Financial Assets,199000000.0
Investments And Advances,261000000.0
Other Investments,173000000.0
Investmentin Financial Assets,11000000.0
Trading Securities,11000000.0
Long Term Equity Investment,77000000.0
Investmentsin Associatesat Cost,77000000.0
Goodwill And Other Intangible Assets,4709000000.0
Other Intangible Assets,2241000000.0
Goodwill,2468000000.0
Net PPE,19334000000.0
Accumulated Depreciation,-23014000000.0
Gross PPE,42348000000.0
Leases,4641000000.0
Other Properties,23329000000.0
Machinery Furniture Equipment,13036000000.0
Land And Improvements,1342000000.0
Current Assets,6991000000.0
Other Current Assets,17000000.0
Hedging Assets Current,52000000.0
Assets Held For Sale Current,200000000.0
Prepaid Assets,183000000.0
Inventory,4169000000.0
Inventories Adjustments Allowances,-58000000.0
Other Inventories,4227000000.0
Receivables,1095000000.0
Receivables Adjustments Allowances,-6000000.0
Other Receivables,627000000.0
Accounts Receivable,474000000.0
Cash Cash Equivalents And Short Term Investments,1275000000.0
Cash And Cash Equivalents,1275000000.0
Cash Financial,1275000000.0

```

### Tool: get_cashflow

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'WOW.AX' from any configured vendor (no cash flow data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

### Tool: get_income_statement

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'WOW.AX' from any configured vendor (no income statement data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

## Role: financial_report

- Skill: `tradingagents-financial-report-analyst`

### Tool: collect_financial_document_sources

- Status: `ok`

```text
## Financial Document Source Packet: WOW.AX

- Trade date: `2026-07-02`
- Collection status: `ok`
- Market: `ASX`
- ASX code: `WOW`
- As-of rule: Only ASX announcements with announcement/lodgement date <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf |
| asx_fallback_document | available | 2025-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf |
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS |
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS |
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS |
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS |
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/asx-announcements/2024/Woolworths Group 2024 Annual Report.pdf |
| asx_fallback_document | available | 2024-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/asx-announcements/2024/Woolworths Group Limited Appendix 4D and Half-Year Financial Report 2024.pdf |
| asx_fallback_document | available | 2023-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f23/full-year/Woolworths Group 2023 Annual Report and Appendix 4E.pdf |
| asx_fallback_document | available | 2023-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/asx-announcements/h23/Woolworths Group F23 Appendix 4D and Half-Year Financial Report.pdf |
| asx_fallback_document | available | 2022-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2022/half-year/Woolworths Group F22 Appendix 4D and Half-Year Financial Report.pdf |
| asx_fallback_document | available | 2021-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2021/full-year/Woolworths Group 2021 Annual Report.pdf |
| asx_fallback_document | available | 2021-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2021/half-year/Appendix 4D and 2021 Half-Year Financial Report.pdf |
| asx_fallback_document | available | 2020-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2020/full-year/2020 Annual Report_FIN.pdf |
| asx_fallback_document | available | 2020-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2020/half-year/Appendix 4D and 2020 Half-Year Financial Report.pdf |
| asx_fallback_document | available | 2019-12-31 | Sustainability Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2019/full-year/2019 Sustainability Report.pdf |
| asx_fallback_document | available | 2019-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2019/full-year/2019 Annual Report.pdf |
| asx_fallback_document | available | 2019-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2019/half-year/Appendix 4D and 2019 Half-Year Financial Report.pdf |
| asx_fallback_document | available | 2018-12-31 | Sustainability Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2018/full-year/Woolworths Group 2018 Sustainability Report_final.pdf |
| asx_fallback_document | available | 2018-12-31 | Annual Report | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2018/full-year/Woolworths Group 2018 Annual Report_Interactive_PDF_final.pdf |
| asx_fallback_document | available | 2018-12-31 | Appendix 4D | https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/2018/half-year/Appendix 4D and 2018 Half-Year Financial Report .pdf |

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: revenue, income, NPAT

```text
Revenue 1.7 to 69,077 Profit after tax attributable to equity holders of the parent entity before significant items1 (19.1) to 1,385 Profit after tax attributable to equity holders of the parent entity >100 to 963 1 Significant items for the current period includes the BIG W impairment of $346 million, MyDeal impairment and closure costs of $52 million, Healthylife impairment of $17 million, support office and store operating model redundancy and restructuring costs of $146 million, and other net costs of $8 million, partially offset by an income tax benefit of $147 million. Details relating to dividends 1 CENTS PER SHARE $M 2025 interim dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: EPS, DPS, dividends

```text
earnings per share and a 40 cents per share special dividend declared in F24. In February, the Group highlighted three focus areas to rebuild customer trust, address areas of underperformance and deliver long-term growth for shareholders. We made progress in these three areas during the year with more to be done in F26. We have simplified the way we work with a number of key management changes and established an organisational structure better aligned to our strategic priorities. In Australia, we announced the formation of Woolworths Retail under the leadership of Annette Karantoni, which has brought our own brand and red meat businesses together with Woolworths Supermarkets and Metro. We are on track to deliver $400 million in above-store support office savings by the end of calendar 2025 and are committed to becoming a lower-cost business. This is in addition to our ongoing productivity plan in our retail businesses and supply chain which provided some offset in a period of material wage and other cost growth. Over the last six months we reviewed all our businesses to ensure they each had a credible path to delivering appropriate returns. In June, we announced the closure of the MyDeal customer website and have also consolidated a number of other businesses to enable greater focus on our cornerstone Food business. In F26, we remain focused on improving our performance through the delivery of our strategic priorities. We are confident that if we restore performance in Australian Food, resolve areas of underperformance in the Group and build a better and stronger business for the medium term, we can deliver strong long-term sustainable shareholder returns. Investors Image: Construction of Sydney Chilled & Fresh DC.Normalised growth has been adjusted to remove the impact of the 53rd week in F24. Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 25 1 2 3 4 5 1 Stakeholder review We are partnering across our value chain to support the transition to a low-carbon economy whilst working to protect and regenerate nature and reduce food waste. We aim to reduce our scope 1, 2 and 3 greenhouse gas emissions, as we work towards net-zero emissions across our value chain by 2050. To achieve this we continue to work on emissions reduction opportunities in collaboration with suppliers, industry and government. In F25, our scope 1 and 2 emissions have reduced by 22.9% compared to our F23 baseline. This was supported through focus on sustainable refrigerants, our transition to renewable electricity and our transport decarbonisation programs. More information can be found in our Climate Disclosures on pages 44 to 61. In F24, we adopted Science Based Target initiative (SBTi) guidance which has connected our no-deforestation and emissions reduction goals, highlighting the importance of nature-based solutions within our decarbonisation strategy. In F25, we conducted a nature risk assessment aligned to the Taskforce on Nature-related Financial Disclosures (TNFD) framework. This allowed us to identify and prioritise key nature-related impacts, dependencies, risks and opportunities across our operations and key supply chain commodities. More information can be found in our 2025 Sustainability Report. In F25, 84% of food waste was diverted from landfill in Australian Supermarkets. During the year we made progress on expanding access to organic recycling services with organic waste recycling solutions growing to 150 stores and eight DCs, supporting our efforts to divert organic food waste from landfill. We are committed to reducing and eliminating unnecessary and problematic packaging through the redesign, innovation and reuse of packaging solutions. In F25, we reduced over 3,200 tonnes of virgin plastic packaging and have removed over 20,000 tonnes from circulation since 2018. We also achieved 86% recyclability of our own brand packaging in F25. Following the collapse of REDcycle’s consumer soft plastics program in November 2022, we have been a member of the Soft Plastics Taskforce and Soft Plastics Stewardship Australia (SPSA) to support an in store collection scheme pilot program. At the end of F25, we had in store collection in over 500 supermarkets, enabling access to recycling services to half of the Australian population. As part of the SPSA we have also been partnering with recyclers like Saveboard, Replas, iQRenew and Close the Loop to transform collected soft plastics into various products, including building materials, furniture, and food-grade packaging. Planet 24 Supply chain transformation The Group’s multi-year supply chain transformation program reached a number of key milestones in F25 with the opening of the Moorebank NDC in November 2024 and the opening of the Auburn automated CFC in May 2025. The Moorebank RDC is also nearing completion and is expected to open by the end of the calendar year with automation installation completed and commissioning commenced. Construction has also commenced on the Sydney Chilled & Fresh DC, a multi-storey temperature-controlled DC located in Eastern Creek. The new site will complement our two DCs at Moorebank with connectivity to key motorways that will support improvements to the Fresh offer across the network. The Group’s full year financial performance reflects a challenging year however good progress was made on the Group’s simplification agenda and supply chain transformation. Financial performance and capital management Group sales increased by 1.7% in F25 with normalised sales growth of 3.6%. Excluding Petstock, Group sales increased by a normalised 2.9% with all segments growing sales during the year. Group EBIT before significant items decreased by a normalised 12.6% primarily due to lower EBIT contributions from Australian Food and BIG W. Excluding the estimated impact on Australian Food of industrial action of $95 million in H1, incremental supply chain commissioning and
```

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: management discussion, MD&A, outlook

```text
Financial Review are featured on pages 2–79 of this report and the information in these sections has been verified through the Group’s internal verification process • The Remuneration Report on pages 80–103 and the Financial Statements on pages 105–162 have been audited by Deloitte. This report should be read in conjunction with the other reports that comprise the 2025 reporting suite, including: Woolworths Group’s 2025 annual reporting documents include: Sustainability Report For detailed information on our progress against the Group’s Sustainability Plan 2025. Sustainability Data Pack For detailed data on key sustainability metrics, basis of preparation and glossary. Modern Slavery Statement For detailed information on our progress made to identify, manage and mitigate the specific risks of modern slavery in the Group’s operations and supply chain. Corporate Governance Statement Describes the Group’s corporate governance framework, policies and practices as at 28 August 2025. Where to find ANNUAL REPORT SUSTAINABILITY REPORT SUSTAINABILITY DATA PACK MODERN SLAVERY STATEMENT CORPORATE GOVERNANCE STATEMENT Strategic priorities ● Operational performance ● Financial performance ● Risk management ● ○ ○ Governance, policies and practices ○ ● Board composition ● ● Climate-related disclosures ● ○ ○ Sustainability strategy and governance ○ ● ● Sustainability performance ○ ● ● ● ○ Key: ● Comprehensive ○ Key messages The 2025 reporting suite can be found at www.woolworthsgroup.com.au/reports Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 3 1 2 3 4 5 1 About this report The 2025 Annual Report for the 52 weeks ended 29 June 2025 contains certain non-IFRS financial measures of historical financial performance, balance sheet or cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which Woolworths Group operates. Non-IFRS financial information Non-IFRS financial information should be considered in addition to, and is not intended to be a substitute for, or more important than, IFRS measures. The presentation of non-IFRS measures is in line with Regulatory Guide 230 issued by the Australian Security and Investments Commission in December 2011 to promote full and clear disclosure for investors and other users of financial information and minimise the possibility of being misled by such information. These measures are used by management and the directors as the primary measures of assessing the financial performance of the Group and individual segments. The directors also believe that these non -IFRS measures assist in providing additional meaningful information on the underlying drivers of the business, performance and trends, as well as the financial position of the Woolworths Group. Non-IFRS financial measures are also used to enhance the comparability of information between reporting periods (such as comparable sales), by adjusting for non-recurring or uncontrollable factors which affect IFRS measures, to aid the user in understanding the Woolworths Group’s performance. Consequently, non-IFRS measures are used by the directors and management for performance analysis, planning, reporting and incentive setting purposes and have remained consistent with the prior year. Non-IFRS measures are not subject to audit or review. Disclaimer This report contains forward looking statements, including, but not limited to statements regarding: trends in consumer preferences; commodity prices; goals, targets, plans, strategies and objectives of Woolworths Group; assumed near and long-term scenarios and transition pathways; potential global responses to climate change; regulatory and policy developments; the development and uptake of certain technologies; and the potential effect of possible future events on the value of Woolworths Group. The forward looking statements in this report are based on management’s good faith, current expectations and reflect judgements, assumptions and estimates and other information available as at the date of this report. They are, by their nature, subject to significant uncertainties, many of which are outside Woolworths Group’s control. Actual results, circumstances and developments may differ materially from those expressed in this report and readers are cautioned not to place undue reliance on these forward looking statements. Forward looking statements should therefore be read in conjunction with, and are qualified by reference to the expectations, judgements, assumptions, estimates and other information and risk factors, referred to above. Acknowledgement of Country Woolworths Group acknowledges the many Traditional Owners of the lands across Australia, and pay our respects to their Elders past and present. We recognise their strengths and enduring connection to lands, waters and skies as the Custodians of the oldest continuing cultures on the planet. We are committed to actively contributing to Australia’s reconciliation journey through listening and learning, empowering more diverse voices, caring deeply for our communities and working together for a better tomorrow. ‘A Brave Heart for a Better Tomorrow’ artwork by David Williams of Gilimbaa. 2 Reporting suite The 2025 Annual Report provides a consolidated summary of Woolworths Group’s performance for the financial year ended 29 June 2025, as well as progress against its strategic agenda and Sustainability Plan 2025 to create long-term value for our stakeholders. • The Directors’ Report and Operating Financial Review are featured on pages 2–79 of this report and the information in these sections has been verified through the Group’s internal verification process • The Remuneration Report on pages 80–103 and the Financial Statements on pages 105–162 have
```

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: cash flow statement, operating cash flow

```text
cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which Woolworths Group operates. Non-IFRS financial information Non-IFRS financial information should be considered in addition to, and is not intended to be a substitute for, or more important than, IFRS measures. The presentation of non-IFRS measures is in line with Regulatory Guide 230 issued by the Australian Security and Investments Commission in December 2011 to promote full and clear disclosure for investors and other users of financial information and minimise the possibility of being misled by such information. These measures are used by management and the directors as the primary measures of assessing the financial performance of the Group and individual segments. The directors also believe that these non -IFRS measures assist in providing additional meaningful information on the underlying drivers of the business, performance and trends, as well as the financial position of the Woolworths Group. Non-IFRS financial measures are also used to enhance the comparability of information between reporting periods (such as comparable sales), by adjusting for non-recurring or uncontrollable factors which affect IFRS measures, to aid the user in understanding the Woolworths Group’s performance. Consequently, non-IFRS measures are used by the directors and management for performance analysis, planning, reporting and incentive setting purposes and have remained consistent with the prior year. Non-IFRS measures are not subject to audit or review. Disclaimer This report contains forward looking statements, including, but not limited to statements regarding: trends in consumer preferences; commodity prices; goals, targets, plans, strategies and objectives of Woolworths Group; assumed near and long-term scenarios and transition pathways; potential global responses to climate change; regulatory and policy developments; the development and uptake of certain technologies; and the potential effect of possible future events on the value of Woolworths Group. The forward looking statements in this report are based on management’s good faith, current expectations and reflect judgements, assumptions and estimates and other information available as at the date of this report. They are, by their nature, subject to significant uncertainties, many of which are outside Woolworths Group’s control. Actual results, circumstances and developments may differ materially from those expressed in this report and readers are cautioned not to place undue reliance on these forward looking statements. Forward looking statements should therefore be read in conjunction with, and are qualified by reference to the expectations, judgements, assumptions, estimates and other information and risk factors, referred to above. Acknowledgement of Country Woolworths Group acknowledges the many Traditional Owners of the lands across Australia, and pay our respects to their Elders past and present. We recognise their strengths and enduring connection to lands, waters and skies as the Custodians of the oldest continuing cultures on the planet. We are committed to actively contributing to Australia’s reconciliation journey through listening and learning, empowering more diverse voices, caring deeply for our communities and working together for a better tomorrow. ‘A Brave Heart for a Better Tomorrow’ artwork by David Williams of Gilimbaa. 2 Reporting suite The 2025 Annual Report provides a consolidated summary of Woolworths Group’s performance for the financial year ended 29 June 2025, as well as progress against its strategic agenda and Sustainability Plan 2025 to create long-term value for our stakeholders. • The Directors’ Report and Operating Financial Review are featured on pages 2–79 of this report and the information in these sections has been verified through the Group’s internal verification process • The Remuneration Report on pages 80–103 and the Financial Statements on pages 105–162 have been audited by Deloitte. This report should be read in conjunction with the other reports that comprise the 2025 reporting suite, including: Woolworths Group’s 2025 annual reporting documents include: Sustainability Report For detailed information on our progress against the Group’s Sustainability Plan 2025. Sustainability Data Pack For detailed data on key sustainability metrics, basis of preparation and glossary. Modern Slavery Statement For detailed information on our progress made to identify, manage and mitigate the specific risks of modern slavery in the Group’s operations and supply chain. Corporate Governance Statement Describes the Group’s corporate governance framework, policies and practices as at 28 August 2025. Where to find ANNUAL REPORT SUSTAINABILITY REPORT SUSTAINABILITY DATA PACK MODERN SLAVERY STATEMENT CORPORATE GOVERNANCE STATEMENT Strategic priorities ● Operational performance ● Financial performance ● Risk management ● ○ ○ Governance, policies and practices ○ ● Board composition ● ● Climate-related disclosures ● ○ ○ Sustainability strategy and governance ○ ● ● Sustainability performance ○ ● ● ● ○ Key: ● Comprehensive ○ Key messages The 2025 reporting suite can be found at www.woolworthsgroup.com.au/reports Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 3 1 2 3 4 5 1 About this report The 2025 Annual Report for the 52 weeks ended 29 June 2025 contains certain non-IFRS financial measures of historical financial performance, balance sheet or cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: operating cash flow

```text
Operating cash flow as a percentage of Group net profit after tax before depreciation and amortisation Comparable sales Measure of sales, excluding stores that have been opened or closed in the last 12 months and existing stores where there has been a demonstrable impact from store disruption because of store refurbishment or new store openings/closures Cost of doing business (CODB) Expenses relating to the operation of the business Customer fulfilment centre (CFC) Dedicated online distribution centre DAP Directly-attributable profit only includes costs directly attributable to the B2C eCommerce business, such as picking, packing and delivery costs; CFC and variable DC costs; marketing costs; eCommerce support costs; and CFC and eCommerce-specific asset depreciation DC Distribution centre Direct to Boot (DTB) Where a customer places an online order and drives to a dedicated area where a team member places the order directly in the customer’s boot Everyday Market An integrated online marketplace that allows customers to shop products from other Woolworths Group brands and partners alongside their groceries Funds employed Net assets employed, excluding net tax balances GMV Gross merchandise value Net Promoter Score (NPS) A loyalty measure based on a single question where a customer rates a business on a scale of zero to 10. The score is the net result of the percentage of customers providing a score of nine or 10 (promoters) less the percentage of customers providing a score of zero to six (detractors) NDC National distribution centre n.m. Not meaningful PC+ Primary Connect’s third-party supply chain business Pick up A service which enables collection of online shopping orders in-store or at selected locations Renewal A total store transformation focused on the overall store environment, team, range and process efficiency (including digital) Return on funds employed (ROFE) Calculated as EBIT before significant items for the previous 12 months as a percentage of average (opening, mid and closing) funds employed Sales per square metre Total sales for the previous 12 months by business divided by average trading area of stores and fulfilment centres Total net debt Borrowings less cash balances, including debt hedging derivatives and lease liabilities TRIFR 12-month rolling total recordable injury frequency rate Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 171 1 2 3 4 55 Glossary The key terms and conditions of the subleases between Woolworths Group Limited (Woolworths Group) and Endeavour Group Limited (Endeavour Group) are as follows: TERM DESCRIPTION Head lease The subleases contain an obligation on Endeavour Group to perform and observe Woolworths Group’s obligations as tenant under the head lease that relate to the liquor premises. There is an obligation on Woolworths Group to observe and perform its obligations under the head lease. Commencement date and term The term and further terms of each sublease align with the term and further terms under the relevant head lease, minus one day. Option terms Where Woolworths Group exercises its option to renew the head lease, it must offer a further term to Endeavour Group (provided the further term does not extend beyond 31 December 2040). However, in circumstances where head leases include an obligation to trade as a liquor store, Endeavour Group is obliged to exercise its option if Woolworths Group does. Occupancy costs The rent and outgoings payable are calculated according to the proportion of the area of the liquor premises against the area of the whole premises. All occupancy costs must be paid by Endeavour Group to Woolworths Group, with any adjustments to outgoings to be made at the end of the financial year. Amenity Endeavour Group must not do anything that would detract from the amenity of the supermarket premises or interfere with Woolworths Group’s business. Dealings Endeavour Group must not assign, sublet or license without Woolworths Group’s consent. Consent may be granted or withheld at Woolworths Group’s absolute discretion. A change in control of Endeavour Group is a breach of the sublease. Make good obligations Endeavour Group is required to leave the liquor premises in good and tenantable repair and condition. Endeavour Group must comply with the make good requirements under the head lease. 170 Subleases GLOSSARY 1P Sales of Woolworths Group’s owned merchandise 3P Sales of third-party seller’s merchandise Active eCom customer Customers that have made a purchase online in the last four weeks AGW Australian Grocery Wholesalers AI Artificial Intelligence B2B Business to business B2C Business to customer Cash realisation ratio (CRR) Operating cash flow as a percentage of Group net profit after tax before depreciation and amortisation Comparable sales Measure of sales, excluding stores that have been opened or closed in the last 12 months and existing stores where there has been a demonstrable impact from store disruption because of store refurbishment or new store openings/closures Cost of doing business (CODB) Expenses relating to the operation of the business Customer fulfilment centre (CFC) Dedicated online distribution centre DAP Directly-attributable profit only includes costs directly attributable to the B2C eCommerce business, such as picking, packing and delivery costs; CFC and variable DC costs; marketing costs; eCommerce support costs; and CFC and eCommerce-specific asset depreciation DC Distribution centre Direct to Boot (DTB) Where a customer places an online order and drives to a dedicated area where a team member places the order directly in the customer’s boot Everyday Market An integrated online marketplace that allows customers to shop products from other Woolworths Group brands and partners alongside their groceries Funds employed Net assets employed, excluding net tax balances GMV Gross merchandise value Net Promoter Score (NPS) A
```

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: free cash flow, cash movement

```text
cash movements 467 (138) n.m. Cash from operating activities before interest and tax 6,174 5,863 5.3% Interest paid – leases (597) (570) 4.7% Net interest paid – non-leases (226) (160) 41.3% Tax paid (801) (774) 3.5% Total cash provided by operating activities 4,550 4,359 4.4% Total cash used in investing activities (1,926) (2,277) (15.4)% Cash flow before purchase of additional equity interest, lease payments and dividends 2,624 2,082 26.0% Payments for the purchase of additional equity interest in subsidiaries (422) – n.m. Repayment of principal component of lease liabilities (1,223) (1,138) 7.5 % Dividends paid and payments for shares held in trust (1,689) (1,232) 37.1% Net cash flow (710) (288) 146.5% Cash realisation ratio (%) 1 103 97 1 F25 and F24 cash realisation ratio excludes significant items. Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 29 1 2 3 4 5 1 Group balance sheet as at 29 June 2025 $ MILLION 29 JUNE 2025 30 JUNE 2024 CHANGE Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201) Net investment in inventory (1,847) (1,628) (219) Trade, other receivables and prepayments 1,390 1,358 32 Other creditors, provisions and other liabilities (4,890) (4,590) (300) Property, plant and equipment and investments 10,433 10,319 114 Net assets held for sale 200 162 38 Intangible assets 4,709 4,873 (164) Lease assets 9,162 9,604 (442) Other assets 387 390 (3) Total funds employed 19,544 20,488 (944) Net tax balances 1,665 1,261 404 Net assets employed 21,209 21,74 9 (540) Cash and borrowings (4,236) (3,280) (956) Derivatives 121 (80) 201 Net debt (including derivatives excluding lease liabilities) (4,115) (3,360) (755) Lease liabilities (11 ,874) (12,144) 270 Total net debt (including derivatives) (15,989) (15,504) (485) Put option liabilities over non-controlling interests (258) (675) 417 Net assets 4,962 5,570 (608) Non-controlling interests 102 162 (60) Shareholders’ equity 4,860 5,408 (548) Total equity 4,962 5,570 (608) Inventories of $4,169 million were largely unchanged on the prior year. Lower inventory holdings in Australian Food, New Zealand Food and Australian B2B were partially offset by higher inventory in BIG W reflecting the earlier receipt of Spring/ Summer clothing compared to the prior year. Closing inventory days decreased 1.3 days. Trade payables of $6,016 million increased by $201 million compared to the prior year mainly driven by a favourable timing of payments in New Zealand Food. Other creditors, provisions and other liabilities of $4,890 million increased by $300 million driven mainly by employee-related accruals and provisions as a result of salaries and wages growth, an increase in workers compensation provisions and an increase in GST driven by higher sales and timing of GST payments. Property, plant and equipment and investments of $10,433 million was largely unchanged on the prior year with investment in new stores, property development, refurbishments of existing stores, supply chain and IT infrastructure offset by depreciation, asset impairments, property assets transferred to held for sale and a $383 million decline in investments following the sale of the Group’s final tranche of Endeavour Group in September 2024. Intangible assets of $4,709 million decreased by $164 million with the amortisation and impairment expense exceeding software additions and goodwill related to The Kitchenary Group (City Kitchen) acquisition. Lease assets of $9,162 million decreased by $442 million as lease asset depreciation, impairment of BIG W leases and terminations more than offset new lease additions relating to Moorebank RDC, store growth and remeasurements. Net tax balances of $1,665 million increased by $404 million driven by an increase in net deferred tax assets and higher tax instalments paid in the current year compared to the income statement expense. Net debt (including derivatives and excluding lease liabilities) of $4,115 million increased by $755 million mainly driven by the payment of the special dividend of 40 cents per share reflecting the return of proceeds on the prior year sale of a tranche of Endeavour Group shares. The acquisition of the remaining interest in PFD for $401 million was largely funded by the net proceeds of $383 million from the sale of the final tranche of Endeavour Group shares in September. Put option liabilities over non-controlling interests of $258 million decreased by $417 million mainly reflecting the acquisition of the remaining non-controlling interest in PFD. Group financial performance 28 EBITDA before significant items decreased 4.9% to $5,707 million mainly reflecting lower EBITDA from Australian Food and BIG W, as well as the 53rd week in the prior year. This was partially offset by an improvement in New Zealand Food, Australian B2B and a full year contribution from Petstock. Decrease in inventories of $44 million reflects lower inventory holdings in Australian Food, New Zealand Food and Australian B2B partially offset by higher inventory holdings in BIG W. Increase in trade payables of $171 million was largely driven by the timing of payments for New Zealand Food. Net change in other working capital and non-cash items was an inflow of $235 million during F25 primarily due to an increase in accruals, the non-cash share-based payment expense and increased GST partially offset by non-cash gains on disposal of property, plant and equipment. Cash from operating activities before interest and tax increased 5.3% to $6,174 million driven by favourable working capital movements partially offset by a decrease in EBITDA. Interest paid – leases increased 4.7% to $597 million reflecting new property leases in F25 and the full year impact of the inclusion of Petstock. Net interest paid – non-leases was $226 million, an increase of 41.3% compared to the prior year due to higher average net debt and upfront borrowing and refinancing costs. Tax
```

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: cash, debt, gearing, capital

```text
cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which Woolworths Group operates. Non-IFRS financial information Non-IFRS financial information should be considered in addition to, and is not intended to be a substitute for, or more important than, IFRS measures. The presentation of non-IFRS measures is in line with Regulatory Guide 230 issued by the Australian Security and Investments Commission in December 2011 to promote full and clear disclosure for investors and other users of financial information and minimise the possibility of being misled by such information. These measures are used by management and the directors as the primary measures of assessing the financial performance of the Group and individual segments. The directors also believe that these non -IFRS measures assist in providing additional meaningful information on the underlying drivers of the business, performance and trends, as well as the financial position of the Woolworths Group. Non-IFRS financial measures are also used to enhance the comparability of information between reporting periods (such as comparable sales), by adjusting for non-recurring or uncontrollable factors which affect IFRS measures, to aid the user in understanding the Woolworths Group’s performance. Consequently, non-IFRS measures are used by the directors and management for performance analysis, planning, reporting and incentive setting purposes and have remained consistent with the prior year. Non-IFRS measures are not subject to audit or review. Disclaimer This report contains forward looking statements, including, but not limited to statements regarding: trends in consumer preferences; commodity prices; goals, targets, plans, strategies and objectives of Woolworths Group; assumed near and long-term scenarios and transition pathways; potential global responses to climate change; regulatory and policy developments; the development and uptake of certain technologies; and the potential effect of possible future events on the value of Woolworths Group. The forward looking statements in this report are based on management’s good faith, current expectations and reflect judgements, assumptions and estimates and other information available as at the date of this report. They are, by their nature, subject to significant uncertainties, many of which are outside Woolworths Group’s control. Actual results, circumstances and developments may differ materially from those expressed in this report and readers are cautioned not to place undue reliance on these forward looking statements. Forward looking statements should therefore be read in conjunction with, and are qualified by reference to the expectations, judgements, assumptions, estimates and other information and risk factors, referred to above. Acknowledgement of Country Woolworths Group acknowledges the many Traditional Owners of the lands across Australia, and pay our respects to their Elders past and present. We recognise their strengths and enduring connection to lands, waters and skies as the Custodians of the oldest continuing cultures on the planet. We are committed to actively contributing to Australia’s reconciliation journey through listening and learning, empowering more diverse voices, caring deeply for our communities and working together for a better tomorrow. ‘A Brave Heart for a Better Tomorrow’ artwork by David Williams of Gilimbaa. 2 Reporting suite The 2025 Annual Report provides a consolidated summary of Woolworths Group’s performance for the financial year ended 29 June 2025, as well as progress against its strategic agenda and Sustainability Plan 2025 to create long-term value for our stakeholders. • The Directors’ Report and Operating Financial Review are featured on pages 2–79 of this report and the information in these sections has been verified through the Group’s internal verification process • The Remuneration Report on pages 80–103 and the Financial Statements on pages 105–162 have been audited by Deloitte. This report should be read in conjunction with the other reports that comprise the 2025 reporting suite, including: Woolworths Group’s 2025 annual reporting documents include: Sustainability Report For detailed information on our progress against the Group’s Sustainability Plan 2025. Sustainability Data Pack For detailed data on key sustainability metrics, basis of preparation and glossary. Modern Slavery Statement For detailed information on our progress made to identify, manage and mitigate the specific risks of modern slavery in the Group’s operations and supply chain. Corporate Governance Statement Describes the Group’s corporate governance framework, policies and practices as at 28 August 2025. Where to find ANNUAL REPORT SUSTAINABILITY REPORT SUSTAINABILITY DATA PACK MODERN SLAVERY STATEMENT CORPORATE GOVERNANCE STATEMENT Strategic priorities ● Operational performance ● Financial performance ● Risk management ● ○ ○ Governance, policies and practices ○ ● Board composition ● ● Climate-related disclosures ● ○ ○ Sustainability strategy and governance ○ ● ● Sustainability performance ○ ● ● ● ○ Key: ● Comprehensive ○ Key messages The 2025 reporting suite can be found at www.woolworthsgroup.com.au/reports Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 3 1 2 3 4 5 1 About this report The 2025 Annual Report for the 52 weeks ended 29 June 2025 contains certain non-IFRS financial measures of historical financial performance, balance sheet or cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: segment performance, sector metrics

```text
segment. Group NPAT declined by a normalised 17.1% 1 reflecting lower earnings and higher net finance costs. The Board declared a fully franked final dividend of 45 cents bringing the full year dividend to 84 cents, representing a payout ratio of 74.1% . Reflecting the Group's performance and shareholder outcomes, the long-term incentive did not pay out. The short-term incentive achieved a partial vesting with customer, sales and safety achieving outcomes between Target and Stretch. A one-off Accelerator Incentive was also introduced in January 2025 for select senior leaders (excluding the CEO) to ensure focus on driving the Group’s immediate priorities, build momentum and realign Group initiatives under the new leadership. This incentive was designed to serve separately and in addition to the core metrics of ongoing importance within our STI and LTI plans. The incentive was split into two tranches with immediate H2 F25 targets on earnings and cost savings in tranche 1 while tranche 2 consisted of additional metrics over an 18-month performance period. More information can be found in this year’s Remuneration Report. Message from the Chair I am pleased to present our Annual Report for 2025. This has been an important year as the Group refocused its priorities to better respond to a challenging and competitive trading environment. Importantly, the foundations of the Group remain strong and we have clear plans in place to improve our performance and capitalise on the significant long-term growth opportunities ahead of us. 1 Before significant items. 2 New Zealand dollars. 6 Commitment to safety Last year I spoke about the Board’s commitment to review the F23 STI based on the outcomes of the formal investigations into the two tragic fatalities in that year. SafeWork NSW’s investigation of the Jesmond supermarket fatality in November 2022 resulted in no further action being taken. However, in June this year, SafeWork NSW finalised its investigation, and commenced legal proceedings against Woolworths Group, in relation to the fatality at the Sydney Regional Distribution Centre in June 2023. Following careful consideration of the findings of SafeWork NSW, the Board has applied a further discretionary reduction to the executives in roles with responsibility for safety within distribution centres at that time. Over the past two years, we have reviewed our safety strategy and action plans including revising safety metrics for the Group. Good progress has been made with each of the three key safety metrics: Severity Score, Total Recordable Injury Frequency Rate (TRIFR), and the new metric, High Potential (HiPo) Learning Events, achieving an outcome between Target and Stretch in F25. Through focused efforts on risk reduction, proactive injury prevention and early care, we achieved a 6.2% reduction in TRIFR in F25. In addition, reduced injury severity and frequency led to an improved Injury Severity Score. HiPo Learning Events have led to a number of preventative initiatives across the Group including work done to address falls from heights as outlined on page 20 of this report. The Board is committed to upholding the highest safety standards for the Group to ensure we maintain the strong foundation and culture that keeps all our team members, customers and contractors safe. Meaningful progress on sustainability This year marks the end of our five-year 2025 Sustainability Plan with meaningful progress achieved across key focus areas. Notable highlights over the plan period include the Group’s efforts to support our community through $480 million in direct contributions, delivering over 165 million meals to people in need through our partners, addressing modern slavery in our supply chain, and removing over 20,000 tonnes of virgin plastic from our own brand products. More information can be found in this year’s Sustainability Report. Launching in F26 is the next iteration of the Group’s sustainability agenda, focused on the areas where we can drive the most significant impact including sustainable food systems, waste and circularity, affordable nutritious food, social impact and advancing human rights. I look forward to reporting our progress as part of this important agenda in the years ahead. Board updates I was pleased to announce in August the appointment of Ken Meyer to the Woolworths Group Board as a non-executive Director. We are delighted to have someone with the depth of Ken’s food and grocery retail experience join the Woolworths Group Board. Ken’s entire career, helping to build Whole Foods Market and subsequently his experience in private equity, has been about food retailing and excellence in fresh and grocery innovation. This expertise will further strengthen the Board and align with our focus on retail excellence and fresh food. Holly Kramer will retire at the conclusion of the 2025 AGM after more than nine years of service as a non-executive Director. I would like to sincerely thank Holly for her dedication and valuable contribution to the Group over the past decade, in particular as Chair of our Sustainability Committee. Looking ahead The Board is committed to support management to address underperformance, reinforce a discipline of making every dollar count and simplifying the business to drive better outcomes and accountability. Good progress has been made on reducing costs with $400 million in above-store savings on track to be delivered by the end of calendar 2025, along with decisions to close the MyDeal customer website and consolidate a number of businesses to improve performance and elevate focus on our cornerstone Food business. With the Board’s support, a number of key management changes and an updated organisational structure was established in June to further increase accountability and better align focus to the Group’s strategic priorities. F26 will be an important year for rebuilding momentum across the Group as our leaders set about executing our priorities to deliver
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: outlook, management commentary

```text
commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder information 168 Subleases 170 Glossary 171 Company directory 173 Delivering for our stakeholders Read more about how we delivered for our stakeholders in F25. Our medium-term strategic priorities Read more on our three key strategic priorities to deliver our potential. See pages 6–9 See pages 10–11 See pages 18–26 Messages from the Chair and CEO Read about our Chair and CEO’s reflections on F25. Woolworths Group is an Everyday Retail Group, anchored in the strength of Food. In F25 we took action to position the Group for long-term sustainable growth. We will continue to rebuild customer trust through compelling value and retail execution excellence, simplify the way we work and become a more focused retailer with a differentiated Food offer at our core. We remain purpose-led and committed to delivering better experiences for a better tomorrow. Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 1 1 2 3 4 5 1 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder information 168 Subleases 170 Glossary 171 Company directory 173 Delivering for our stakeholders Read more about how we delivered for our stakeholders in F25. Our medium-term strategic priorities Read more on our three key strategic priorities to deliver our potential. See pages 6–9 See pages 10–11 See pages 18–26 Messages from the Chair and CEO Read about our Chair and CEO’s reflections on F25. Woolworths Group is an Everyday Retail Group, anchored in the strength of Food. In F25 we took action to position the Group for long-term sustainable growth. We will continue to rebuild customer trust through compelling value and retail execution excellence, simplify the way we work and become a more focused retailer with a differentiated Food offer at our core. We remain purpose-led and committed to delivering better experiences for a better tomorrow. Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 1 1 2 3 4 5 1 About this report The 2025 Annual Report for the 52 weeks ended 29 June 2025 contains certain non-IFRS financial measures of historical financial performance, balance sheet or cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which Woolworths Group operates. Non-IFRS financial information Non-IFRS financial information should be considered in addition to, and is not intended to be a substitute for, or more important than, IFRS measures. The presentation of non-IFRS measures is in line with Regulatory Guide 230 issued by the Australian Security and Investments Commission in December 2011 to promote full and clear disclosure for investors and other users of financial information and minimise the possibility of being misled by such information. These measures are used by management and the directors as the primary measures of assessing the financial performance of the Group and individual segments. The directors also believe that these non -IFRS measures assist in providing additional meaningful information on the underlying drivers of the business, performance and trends, as well as the financial position of the Woolworths Group. Non-IFRS financial measures are also used to enhance the comparability of information between reporting periods (such as comparable sales), by adjusting for non-recurring or uncontrollable factors which affect IFRS measures, to aid the user in understanding the Woolworths Group’s performance. Consequently, non-IFRS measures are used by the directors and management for
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: dividends, capital management

```text
dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder information 168 Subleases 170 Glossary 171 Company directory 173 Delivering for our stakeholders Read more about how we delivered for our stakeholders in F25. Our medium-term strategic priorities Read more on our three key strategic priorities to deliver our potential. See pages 6–9 See pages 10–11 See pages 18–26 Messages from the Chair and CEO Read about our Chair and CEO’s reflections on F25. Woolworths Group is an Everyday Retail Group, anchored in the strength of Food. In F25 we took action to position the Group for long-term sustainable growth. We will continue to rebuild customer trust through compelling value and retail execution
```

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: capex, commitments

```text
Commitment to safety Last year I spoke about the Board’s commitment to review the F23 STI based on the outcomes of the formal investigations into the two tragic fatalities in that year. SafeWork NSW’s investigation of the Jesmond supermarket fatality in November 2022 resulted in no further action being taken. However, in June this year, SafeWork NSW finalised its investigation, and commenced legal proceedings against Woolworths Group, in relation to the fatality at the Sydney Regional Distribution Centre in June 2023. Following careful consideration of the findings of SafeWork NSW, the Board has applied a further discretionary reduction to the executives in roles with responsibility for safety within distribution centres at that time. Over the past two years, we have reviewed our safety strategy and action plans including revising safety metrics for the Group. Good progress has been made with each of the three key safety metrics: Severity Score, Total Recordable Injury Frequency Rate (TRIFR), and the new metric, High Potential (HiPo) Learning Events, achieving an outcome between Target and Stretch in F25. Through focused efforts on risk reduction, proactive injury prevention and early care, we achieved a 6.2% reduction in TRIFR in F25. In addition, reduced injury severity and frequency led to an improved Injury Severity Score. HiPo Learning Events have led to a number of preventative initiatives across the Group including work done to address falls from heights as outlined on page 20 of this report. The Board is committed to upholding the highest safety standards for the Group to ensure we maintain the strong foundation and culture that keeps all our team members, customers and contractors safe. Meaningful progress on sustainability This year marks the end of our five-year 2025 Sustainability Plan with meaningful progress achieved across key focus areas. Notable highlights over the plan period include the Group’s efforts to support our community through $480 million in direct contributions, delivering over 165 million meals to people in need through our partners, addressing modern slavery in our supply chain, and removing over 20,000 tonnes of virgin plastic from our own brand products. More information can be found in this year’s Sustainability Report. Launching in F26 is the next iteration of the Group’s sustainability agenda, focused on the areas where we can drive the most significant impact including sustainable food systems, waste and circularity, affordable nutritious food, social impact and advancing human rights. I look forward to reporting our progress as part of this important agenda in the years ahead. Board updates I was pleased to announce in August the appointment of Ken Meyer to the Woolworths Group Board as a non-executive Director. We are delighted to have someone with the depth of Ken’s food and grocery retail experience join the Woolworths Group Board. Ken’s entire career, helping to build Whole Foods Market and subsequently his experience in private equity, has been about food retailing and excellence in fresh and grocery innovation. This expertise will further strengthen the Board and align with our focus on retail excellence and fresh food. Holly Kramer will retire at the conclusion of the 2025 AGM after more than nine years of service as a non-executive Director. I would like to sincerely thank Holly for her dedication and valuable contribution to the Group over the past decade, in particular as Chair of our Sustainability Committee. Looking ahead The Board is committed to support management to address underperformance, reinforce a discipline of making every dollar count and simplifying the business to drive better outcomes and accountability. Good progress has been made on reducing costs with $400 million in above-store savings on track to be delivered by the end of calendar 2025, along with decisions to close the MyDeal customer website and consolidate a number of businesses to improve performance and elevate focus on our cornerstone Food business. With the Board’s support, a number of key management changes and an updated organisational structure was established in June to further increase accountability and better align focus to the Group’s strategic priorities. F26 will be an important year for rebuilding momentum across the Group as our leaders set about executing our priorities to deliver on our strategy. Under Amanda’s leadership, Woolworths Group is looking ahead with measured and determined confidence. We have world-class assets and capabilities across the Group that give us a unique competitive advantage and significant potential. Realising that potential rests on us staying true to our purpose while intensifying our focus on delivery and performance. I want to take this moment to acknowledge the passing of former Executive Chairman Paul Simons AM in May of this year. Paul led Woolworths Limited from 1987 to 1995 during a pivotal time in our company’s history and will be remembered for instilling important customer values into the business which remain as relevant today as they were in Paul’s time. Finally, I want to thank all of our team members across the Group, who despite the various challenges of this year, remained focused on putting our customers first. Scott Perkins Chair Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 7 1 2 3 4 5 1 Strong foundations with clear plans for sustainable growth F25 performance The Group’s performance reflects a series of challenges which resulted in financial outcomes that fell short of expectations with Group EBIT declining by a normalised 12.6% 1. A combination of ongoing value-seeking behaviours from customers, necessary action taken to reduce shelf prices as well as material supply chain disruption from extended industrial action in Victoria contributed to Australian Food EBIT declining by a normalised 10.5% 1, well below our
```

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: risks

```text
impairment of $346 million, MyDeal impairment and closure costs of $52 million, Healthylife impairment of $17 million, support office and store operating model redundancy and restructuring costs of $146 million, and other net costs of $8 million, partially offset by an income tax benefit of $147 million. Details relating to dividends 1 CENTS PER SHARE $M 2025 interim dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder information 168 Subleases 170 Glossary 171 Company directory 173 Delivering for our stakeholders Read more about how we delivered for our stakeholders in F25. Our medium-term strategic priorities Read more on our three key strategic priorities to deliver our potential. See pages 6–9
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: one-off items

```text
impairment of $346 million, MyDeal impairment and closure costs of $52 million, Healthylife impairment of $17 million, support office and store operating model redundancy and restructuring costs of $146 million, and other net costs of $8 million, partially offset by an income tax benefit of $147 million. Details relating to dividends 1 CENTS PER SHARE $M 2025 interim dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder information 168 Subleases 170 Glossary 171 Company directory 173 Delivering for our stakeholders Read more about how we delivered for our stakeholders in F25. Our medium-term strategic priorities Read more on our three key strategic priorities to deliver our potential. See pages 6–9
```

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
Revenue 1.7 to 69,077 Profit after tax attributable to equity holders of the parent entity before significant items1 (19.1) to 1,385 Profit after tax attributable to equity holders of the parent entity >100 to 963 1 Significant items for the current period includes the BIG W impairment of $346 million, MyDeal impairment and closure costs of $52 million, Healthylife impairment of $17 million, support office and store operating model redundancy and restructuring costs of $146 million, and other net costs of $8 million, partially offset by an income tax benefit of $147 million. Details relating to dividends 1 CENTS PER SHARE $M 2025 interim dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: segment table, product table, sector metrics

```text
Product stewardship More information on our sustainability progress across our value chain can be found in the 2025 Sustainability Report Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 15 1 2 3 4 5 1 Our value chain The farming and sourcing of raw materials is fundamental to delivering fresh, quality food and the production of quality own brand products. Sustainable food systems Our focus is on supporting sustainable food systems through climate and nature-focused actions. We aim for net-zero emissions across our value chain by 2050, aligned with a 1.5° C pathway. We partner with suppliers to responsibly manage natural resources via sustainable sourcing and animal welfare programs. In F26, we will continue to mitigate impacts by reducing emissions, building resilience and protecting nature-based assets that food systems rely on. Privacy and cyber security Cyber security is considered a macro risk factor and we proactively consider our cyber risk on a regular basis as part of our risk management practices. With the growth of our online business and increased traffic to our digital channels, we have continued to invest in our cybersecurity expertise and controls. We exercise ongoing due diligence and have a proactive program. Human rights and responsible sourcing The Group’s Human Rights Program comprises four pillars and is the overarching way we manage key human rights risks, including worker exploitation and modern slavery across our supply chain. Emissions reduction and climate resilience This year we achieved a 22.9% reduction in scope 1 and 2 emissions from our F23 baseline. Our approach to absolute emissions reduction includes energy efficiency programs, the transition to renewable electricity, refrigerant management and transport decarbonisation. We also continue to invest in our supply chain network to build resilience and better support regional communities during adverse weather events and natural disasters. As a retailer we collect data to provide better and personalised shopping experiences. We also leverage transformative technologies to optimise our operations. Maintaining strong and collaborative relationships with our suppliers, processors and packaging partners is essential to delivering great quality products at great value. The strength and resilience of our supply chain is critical in ensuring our retail network is properly stocked to maintain high levels of availability and choice for our customers. Agriculture Data, tech & AI Suppliers Logistics Our approach 14 The scale of Woolworths Group’s extensive value chain is a source of competitive advantage and reflects the connected nature of our operations which supports the delivery of long-term growth and our ambition for a better tomorrow. Reducing hunger and food waste We seek to apply an end-to-end approach across our value chain to redistribute edible food and reduce hunger and food waste. In F25, we donated over 43 million meals via our food relief partners. We also strengthened our organic waste recycling efforts, diverting 84% of organic food waste from landfill, with organic waste recycling solutions now available in 1,025 Australian Supermarkets. Holistic wellbeing We aim to create safe workplaces and invest in our team’s holistic wellbeing, both mental and physical. We launched our new Group-wide safety promise of ‘Our Place – We’re safer together’ and made progress on strengthening our safety foundations. We also continued our focus on material safety risk management, including plant and vehicle-related incidents. Health We’ve been making progress on making healthy eating easier by reformulating hundreds of our own brand products with 87% of own brand products achieving a Health Star Rating of 3.5 stars or above. Sustainable packaging Since 2018 we have removed over 20,000 tonnes of virgin plastic packaging from circulation with 85% of our own brand packaging using recycled content. In F25, we re-established soft plastic recycling services in over 500 stores across Australia. Our retail businesses provide Australian and New Zealand customers with their food and everyday needs both in store and online, supported by our service businesses and Group capabilities. Our team members are critical in serving our customers and ensuring we’re providing great shopping experiences while maintaining a safe and inclusive work environment. Providing our customers with great value products and convenient shopping experiences is critical to the success of our business. Minimising food waste and plastic packaging across our value chain helps us to reduce our environmental impact while supporting efforts to mitigate food insecurity. Retail & B2B Our Team Customers Product stewardship More information on our sustainability progress across our value chain can be found in the 2025 Sustainability Report Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 15 1 2 3 4 5 1 Our operating context It’s important that we understand and respond to the key macro trends that create both opportunities and risks for our business. More information on our risk management approach can be found on pages 62–69. Market drivers Customers remain highly value-focused and value-seeking behaviour continued in a competitive retail environment. While there are early signs of customer sentiment improving, customers are buying more on special with promotional penetration increasing on the prior year. The shift to convenience is also continuing, reflected in the growth of digital and eCommerce, with more customers using digital tools to help plan their shop and manage their budgets. • Offered deeper and more frequent promotions • Launched, Lower Shelf Price, lowering the prices on over 500 products with an average price decrease of 10% across the range • Increased the number of affordable own brand
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: sales growth

```text
comparable sales), by adjusting for non-recurring or uncontrollable factors which affect IFRS measures, to aid the user in understanding the Woolworths Group’s performance. Consequently, non-IFRS measures are used by the directors and management for performance analysis, planning, reporting and incentive setting purposes and have remained consistent with the prior year. Non-IFRS measures are not subject to audit or review. Disclaimer This report contains forward looking statements, including, but not limited to statements regarding: trends in consumer preferences; commodity prices; goals, targets, plans, strategies and objectives of Woolworths Group; assumed near and long-term scenarios and transition pathways; potential global responses to climate change; regulatory and policy developments; the development and uptake of certain technologies; and the potential effect of possible future events on the value of Woolworths Group. The forward looking statements in this report are based on management’s good faith, current expectations and reflect judgements, assumptions and estimates and other information available as at the date of this report. They are, by their nature, subject to significant uncertainties, many of which are outside Woolworths Group’s control. Actual results, circumstances and developments may differ materially from those expressed in this report and readers are cautioned not to place undue reliance on these forward looking statements. Forward looking statements should therefore be read in conjunction with, and are qualified by reference to the expectations, judgements, assumptions, estimates and other information and risk factors, referred to above. Acknowledgement of Country Woolworths Group acknowledges the many Traditional Owners of the lands across Australia, and pay our respects to their Elders past and present. We recognise their strengths and enduring connection to lands, waters and skies as the Custodians of the oldest continuing cultures on the planet. We are committed to actively contributing to Australia’s reconciliation journey through listening and learning, empowering more diverse voices, caring deeply for our communities and working together for a better tomorrow. ‘A Brave Heart for a Better Tomorrow’ artwork by David Williams of Gilimbaa. 2 Reporting suite The 2025 Annual Report provides a consolidated summary of Woolworths Group’s performance for the financial year ended 29 June 2025, as well as progress against its strategic agenda and Sustainability Plan 2025 to create long-term value for our stakeholders. • The Directors’ Report and Operating Financial Review are featured on pages 2–79 of this report and the information in these sections has been verified through the Group’s internal verification process • The Remuneration Report on pages 80–103 and the Financial Statements on pages 105–162 have been audited by Deloitte. This report should be read in conjunction with the other reports that comprise the 2025 reporting suite, including: Woolworths Group’s 2025 annual reporting documents include: Sustainability Report For detailed information on our progress against the Group’s Sustainability Plan 2025. Sustainability Data Pack For detailed data on key sustainability metrics, basis of preparation and glossary. Modern Slavery Statement For detailed information on our progress made to identify, manage and mitigate the specific risks of modern slavery in the Group’s operations and supply chain. Corporate Governance Statement Describes the Group’s corporate governance framework, policies and practices as at 28 August 2025. Where to find ANNUAL REPORT SUSTAINABILITY REPORT SUSTAINABILITY DATA PACK MODERN SLAVERY STATEMENT CORPORATE GOVERNANCE STATEMENT Strategic priorities ● Operational performance ● Financial performance ● Risk management ● ○ ○ Governance, policies and practices ○ ● Board composition ● ● Climate-related disclosures ● ○ ○ Sustainability strategy and governance ○ ● ● Sustainability performance ○ ● ● ● ○ Key: ● Comprehensive ○ Key messages The 2025 reporting suite can be found at www.woolworthsgroup.com.au/reports Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 3 1 2 3 4 5 1 About this report The 2025 Annual Report for the 52 weeks ended 29 June 2025 contains certain non-IFRS financial measures of historical financial performance, balance sheet or cash flows. Non-IFRS financial measures are financial measures other than those defined or specified under all relevant accounting standards and may not be directly comparable with other companies’ measures but are common practice in the industry in which Woolworths Group operates. Non-IFRS financial information Non-IFRS financial information should be considered in addition to, and is not intended to be a substitute for, or more important than, IFRS measures. The presentation of non-IFRS measures is in line with Regulatory Guide 230 issued by the Australian Security and Investments Commission in December 2011 to promote full and clear disclosure for investors and other users of financial information and minimise the possibility of being misled by such information. These measures are used by management and the directors as the primary measures of assessing the financial performance of the Group and individual segments. The directors also believe that these non -IFRS measures assist in providing additional meaningful information on the underlying drivers of the business, performance and trends, as well as the financial position of the Woolworths Group. Non-IFRS financial measures are also used to enhance the comparability of information between reporting periods (such as comparable sales), by adjusting for non-recurring or uncontrollable factors which affect IFRS measures, to aid the user in understanding the Woolworths Group’s performance. Consequently, non-IFRS measures are used by the directors and management for
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: EBIT margin

```text
EBIT margin decreasing by a normalised 82 bps to 5.4%. In H2, EBIT declined by a normalised 8.1% with an EBIT margin of 5.5%. F25 EBIT was impacted by supply chain commissioning and dual-running costs of $111 million ($73 million incremental) and $95 million associated with industrial action in H1. Excluding these impacts, F25 EBIT would have declined by a normalised 5.0% or 4.9% in H2. Woolworths Food Retail F25 EBIT of $2,532 million decreased by a normalised 13.3% with the EBIT margin declining by 93 bps on a normalised basis to 5.0%. WooliesX DAP & EBIT increased by a normalised 27.5% to $428 million. During the year 32 new Mini Woolies were opened, bringing the total to 100 locations across Australia at the end of F25. Soft plastics recycling services were restored to 500 stores across Australia and together with our customers, we provided the equivalent of 31 million meals to Australians in need through our food relief partners. Woolworths Supermarkets continued to support communities impacted by adverse weather events in NSW and Qld through direct community contributions via the Woolworths Group Foundation and the donation of essential items. 32 Launch of new Scan&Go Trolleys During the year Woolworths Supermarkets launched Australia’s first digital trolleys, allowing customers to scan and bag items and track their spend as they shop. The digital trolleys are the next evolution of the Scan&Go technology which was first launched in 2018 to help make shopping easier for customers. Using their Everyday Rewards card, customers can unlock a tablet device from the front of store, attach it to their trolley and start shopping. The digital trolleys are now available in 15 stores and help customers track their spending as they shop and check out faster using the pin pad at the dedicated Scan&Go checkout. Woolworths Food Retail sales performance $ MILLION F25 (52 WEEKS) F24 (53 WEEKS) CHANGE CHANGE NORMALISED Woolworths Supermarkets (store-originated) 41,958 42,426 (1.1)% 0.7% Metro (store-originated) 1,597 1,571 1.7% 3.7% Pick up eCommerce sales 2,939 2,459 19.5% 21.7% Sales to customers visiting a store 46,494 46,456 0.1% 1.9% Delivery eCommerce sales (including MILKRUN) 4,370 3,889 12.4% 14.7% Woolworths Food Retail (Stores and eCommerce) 50,864 50,345 1.0% 2.9% Normalised growth has been adjusted to remove the impact of the 53rd week in F24. Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 33 1 2 3 4 5 2 Australian Food Business review Despite some availability impacts caused by supply chain disruption in H1, Grocery Food (ex Tobacco) saw strong growth driven by Health & Wellness, Drinks and Frozen Food with sales momentum improving in H2 driven by successful Back to School and Easter events. Modest inflation in Fruit & Vegetables and item growth in Chilled and Meat, Poultry and Seafood contributed to Fresh growth. In Everyday Needs, sales and item growth was broadly in line with the prior year driven by increased competition in Pet and Baby Needs. Own and Exclusive Brand sales grew 5.0% in F25, outperforming branded sales growth as customers continued to recognise the strong value of own and exclusive brands. Long Life sales increased 6.3% with growth in Pantry, Drinks, Frozen Food, Snacking and Household Care the highlights. Fresh sales increased by 5.0% with Fruit & Vegetables and Meat growing in the high single digits. Long Life and Fresh growth was partially offset by a decline in General Merchandise sales. Average prices (ex Tobacco) declined 0.2% in Q4 compared to the prior year, marking the sixth consecutive quarter of lower prices for customers. Fruit & Vegetables inflation in the quarter was due to cycling a period of abundant supply in the prior year, particularly in avocados, as well as unfavourable growing conditions for berries. Deflation in Long Life categories such as Pantry, Snacking, Freezer and Everyday Needs was partially offset by higher Meat prices. Sales per square metre increased by a normalised 1.8% with sales growth higher than average space growth of 1.1%. During the year, six net new stores opened and 68 renewals were completed. Gross margin (%) decreased by 25 bps (-46 bps ex Tobacco) to 28.6%. Key drivers include livestock inflation that was not fully passed onto customers, price investment, stockloss increases and mix impacts as customers traded into own brand and deeper promotions, as well as previously disclosed supply chain commissioning and dual-running costs. This was partially offset by category mix benefits including a 30% decline in Tobacco sales, improved commodity sourcing and strong Cartology and service income growth. CODB (%) increased by a normalised 56 bps to 23.3% reflecting the 4.25% increase in store team wages and superannuation from July and a lower mix of in-store sales. Productivity initiatives during the year provided some offset to higher cost growth including enhanced inventory routines, electronic shelf labels and eCommerce picking optimisation. Depreciation and amortisation increased by a normalised 6.9% driven by new stores, renewals, supply chain and technology and digital investments. Australian Food F25 EBIT of $2,753 million declined by a normalised 10.5% with the EBIT margin decreasing by a normalised 82 bps to 5.4%. In H2, EBIT declined by a normalised 8.1% with an EBIT margin of 5.5%. F25 EBIT was impacted by supply chain commissioning and dual-running costs of $111 million ($73 million incremental) and $95 million associated with industrial action in H1. Excluding these impacts, F25 EBIT would have declined by a normalised 5.0% or 4.9% in H2. Woolworths Food Retail F25 EBIT of $2,532 million decreased by a normalised 13.3% with the EBIT margin declining by 93 bps on a normalised basis to 5.0%. WooliesX DAP & EBIT increased by a normalised 27.5% to $428 million. During the year 32 new Mini Woolies were opened, bringing the total to 100
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: inventory

```text
Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201) Net investment in inventory (1,847) (1,628) (219) Trade, other receivables and prepayments 1,390 1,358 32 Other creditors, provisions and other liabilities (4,890) (4,590) (300) Property, plant and equipment and investments 10,433 10,319 114 Net assets held for sale 200 162 38 Intangible assets 4,709 4,873 (164) Lease assets 9,162 9,604 (442) Other assets 387 390 (3) Total funds employed 19,544 20,488 (944) Net tax balances 1,665 1,261 404 Net assets employed 21,209 21,74 9 (540) Cash and borrowings (4,236) (3,280) (956) Derivatives 121 (80) 201 Net debt (including derivatives excluding lease liabilities) (4,115) (3,360) (755) Lease liabilities (11 ,874) (12,144) 270 Total net debt (including derivatives) (15,989) (15,504) (485) Put option liabilities over non-controlling interests (258) (675) 417 Net assets 4,962 5,570 (608) Non-controlling interests 102 162 (60) Shareholders’ equity 4,860 5,408 (548) Total equity 4,962 5,570 (608) Inventories of $4,169 million were largely unchanged on the prior year. Lower inventory holdings in Australian Food, New Zealand Food and Australian B2B were partially offset by higher inventory in BIG W reflecting the earlier receipt of Spring/ Summer clothing compared to the prior year. Closing inventory days decreased 1.3 days. Trade payables of $6,016 million increased by $201 million compared to the prior year mainly driven by a favourable timing of payments in New Zealand Food. Other creditors, provisions and other liabilities of $4,890 million increased by $300 million driven mainly by employee-related accruals and provisions as a result of salaries and wages growth, an increase in workers compensation provisions and an increase in GST driven by higher sales and timing of GST payments. Property, plant and equipment and investments of $10,433 million was largely unchanged on the prior year with investment in new stores, property development, refurbishments of existing stores, supply chain and IT infrastructure offset by depreciation, asset impairments, property assets transferred to held for sale and a $383 million decline in investments following the sale of the Group’s final tranche of Endeavour Group in September 2024. Intangible assets of $4,709 million decreased by $164 million with the amortisation and impairment expense exceeding software additions and goodwill related to The Kitchenary Group (City Kitchen) acquisition. Lease assets of $9,162 million decreased by $442 million as lease asset depreciation, impairment of BIG W leases and terminations more than offset new lease additions relating to Moorebank RDC, store growth and remeasurements. Net tax balances of $1,665 million increased by $404 million driven by an increase in net deferred tax assets and higher tax instalments paid in the current year compared to the income statement expense. Net debt (including derivatives and excluding lease liabilities) of $4,115 million increased by $755 million mainly driven by the payment of the special dividend of 40 cents per share reflecting the return of proceeds on the prior year sale of a tranche of Endeavour Group shares. The acquisition of the remaining interest in PFD for $401 million was largely funded by the net proceeds of $383 million from the sale of the final tranche of Endeavour Group shares in September. Put option liabilities over non-controlling interests of $258 million decreased by $417 million mainly reflecting the acquisition of the remaining non-controlling interest in PFD. Group financial performance 28 EBITDA before significant items decreased 4.9% to $5,707 million mainly reflecting lower EBITDA from Australian Food and BIG W, as well as the 53rd week in the prior year. This was partially offset by an improvement in New Zealand Food, Australian B2B and a full year contribution from Petstock. Decrease in inventories of $44 million reflects lower inventory holdings in Australian Food, New Zealand Food and Australian B2B partially offset by higher inventory holdings in BIG W. Increase in trade payables of $171 million was largely driven by the timing of payments for New Zealand Food. Net change in other working capital and non-cash items was an inflow of $235 million during F25 primarily due to an increase in accruals, the non-cash share-based payment expense and increased GST partially offset by non-cash gains on disposal of property, plant and equipment. Cash from operating activities before interest and tax increased 5.3% to $6,174 million driven by favourable working capital movements partially offset by a decrease in EBITDA. Interest paid – leases increased 4.7% to $597 million reflecting new property leases in F25 and the full year impact of the inclusion of Petstock. Net interest paid – non-leases was $226 million, an increase of 41.3% compared to the prior year due to higher average net debt and upfront borrowing and refinancing costs. Tax paid of $801 million increased by 3.5% reflecting higher tax payments related to the F24 tax return paid in F25 and modestly higher instalment payments during the year. Payments for the purchase of PPE and intangible assets of $2,528 million was broadly in line with the prior year with an increase in spend on renewals and eCommerce offset by lower supply chain and IT spend. Payments for the purchases of businesses, net of cash acquired of $84 million mainly reflects the purchase of the remaining 77% of The Kitchenary not previously owned by Woolworths Group. Proceeds from the sale of businesses and investments, net of cash disposed of $408 million primarily reflects the net proceeds received on the sale of the Group’s remaining ownership interest in Endeavour Group. Payments for the purchase of additional equity interests in subsidiaries of $422 million mainly reflects the purchase of the remaining 35% interest in PFD. Repayment of lease liabilities of $1,223 million increased on the prior year reflecting new property leases
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: capex

```text
capex for energy efficiency and emissions reduction. Across the value chain, increased cost of goods due to higher commodity prices. • Scope 1 and 2 emissions reduction targets are being pursued through initiatives focused on low ‑carbon refrigerants, energy efficiency, renewable electricity and transport decarbonisation • An internal shadow carbon price (ISCP) pilot continues to help consider the financial implications of GHG emissions in strategic decision ‑making for major business investments. • Scope 3 emissions reduction targets are being pursued through the 2025 Sustainability Plan’s focus on strategic initiatives which drive collaboration, education, innovation, investment and advocacy. Refer to the 2025 Sustainability Report for more information. Timeframe Scenario sensitivity Risk concentration Short Medium Long 1.5°C 2.0°C >3.0°C Infrastructure Value chain – Increased costs due to carbon pricing mechanismsTransition Woolworths Group Annual Report 2025 Performance highlights Business review Directors’ Report Financial Report Other information 51 1 2 3 4 5 2 Updated scenarios and time horizons Since 2020, Woolworths Group has used climate scenario analysis to understand how different future climate pathways could affect performance over time. This year, the analysis was narrowed from four to three scenarios 1, also aligning with AASB S2 reporting requirements, which require a low ‑warming (1.5°C) and a high‑warming (>2.5°C) scenario. All scenarios were informed by external expert guidance, and recent climate science and government policy. By analysing these diverse scenarios, the Group will continue to identify and plan for potential strategic advantages and business risk mitigation across short (0–3 years), medium (4–10 years), and long ‑term (11–25 years) time horizons. These timeframes help to consider typical planning cycles, as well as balance the longer ‑term nature of climate impacts. Further information on the assumptions and methodology used in scenario analysis will be provided in future reports, as part of AASB S2 aligned disclosures. Net Zero (1.5°C) SSP1-1.9 Delayed Transition (2.0°C) SSP1-2.6 Climate Distress (>3.0°C) SSP3-7.0 Bold climate action, supported by strong policies and significant investment in innovation, limits global warming to 1.4–1.5°C by 2100. Early investments in clean energy transition, adaptation measures, and sustainable farming practices effectively safeguard food production, despite climate change impacts. As the economy transitions away from emissions intensive activity, household purchasing power recovers. Delayed but strong climate action post‑2030, coupled with a rapid economic shift, limits global warming to below 2°C by 2100. The transition to a low‑carbon economy faces initial delays, leading to increased costs for clean energy, decarbonised transport, and sustainable agriculture. Hampering of economic activity puts downward pressure on household purchasing power, with a slower recovery due to the delayed economic transition. Under current emissions policies, global warming surpasses 3°C by 2100. The increased frequency and severity of extreme weather events cause significant damage to assets and infrastructure, exacerbate food productivity losses, and severely disrupt supply chains. Rising global material and energy costs disproportionately impact economies, increasing the cost of living while households face reduced spending power due to weaker economic activity. Climate-related risks Woolworths Group recognises the potential impacts that climate change and the transition to a low ‑carbon economy can have on its operations and value. These climate ‑related risks specifically address the challenges in protecting existing value, requiring strategies to mitigate potential negative effects and support adaptation and resilience. 1 Last year’s 2.7°C scenario was removed as an optional fourth scenario. The high warming scenario was updated from 4.4°C to >3°C (SSP3 ‑7 .0). This change reflects a more plausible future for the retail sector, as SSP3 ‑7 .0 better accounts for existing international and national mitigation efforts while still enabling the Group to stress ‑test against severe physical climate impacts. Risk description: Increased frequency and severity of acute weather events (e.g. storms, floods, bushfires) and chronic weather shifts (e.g. sea level rise) causing damage and disruptions to stores, DCs and logistics routes. Impact (current and future) Mitigation underway Current: In F25, extreme weather (storms, flooding), caused 98 days of disruption to operations and led to damage at stores and DCs. Future: May lead to increased costs for repairs and maintenance; adverse insurance impacts which could include higher premiums, larger retention levels, location exclusion zones and a reduction in the availability of insurance capacity; increased supply chain costs due to rerouting; and trading losses from lost sales and lost stock. • Climate risks are factored into future network planning and new site developments, including future flood risk considered as part of the approval process. • The store renewal program includes resilience upgrades, such as external connection points for generators to maintain power during outages. • Management structures in place to support ongoing resilience planning for severe weather events. This includes implementing defensive measures like sandbags for flood‑risk stores and team training on their effective use. Timeframe Scenario sensitivity Risk concentration Short Medium Long 1.5°C 2.0°C >3.0°C Infrastructure Value chain Stores, DCs, transport networks Chronic and acute weather events causing disruption and damage to operationsPhysical 50 Key Anticipated onset of risk or opportunity Estimated full impact of risk or opportunity Low likelihood Moderate likelihood High likelihood Suppliers, processors and packaging Warehouse and distribution Customers Retail businesses and services Agriculture and raw
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf
- Supports claims: dividends

```text
dividends 1 CENTS PER SHARE $M 2025 interim dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1 Performance highlights About this report 2 About Woolworths Group 4 Message from the Chair 6 Message from the CEO 8 Medium-term strategic priorities 10 Our business model 12 Our value chain 14 Our operating context 16 Delivering for our stakeholders 18 Group financial performance 26 SECTION 2 Business review Australian Food 30 Australian B2B 36 New Zealand Food 38 W Living 40 Climate-related disclosures 44 Risk management approach 62 SECTION 3 Directors’ Report Governance 70 Board of Directors 72 Group Executive Committee 75 Directors’ Statutory Report 78 Remuneration Report 80 SECTION 4 Financial Report Auditor’s Independence Declaration 104 Financial Report 105 Directors’ Declaration 163 Independent Auditor’s Report 164 SECTION 5 Other information Shareholder information 168 Subleases 170 Glossary 171 Company directory 173 Delivering for our stakeholders Read more about how we delivered for our stakeholders in F25. Our medium-term strategic priorities Read more on our three key strategic priorities to deliver our potential. See pages 6–9 See pages 10–11 See pages 18–26 Messages from the Chair and CEO Read about our Chair and CEO’s reflections on F25. Woolworths Group is an Everyday Retail Group, anchored in the strength of Food. In F25 we took action to position the Group for long-term sustainable growth. We will continue to rebuild customer trust through
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf

```text
27 August 2025 ASX Market Announcements Ofﬁce Australian Securities Exchange 20 Bridge Street Sydney NSW 2000 Appendix 4E and Annual Report Attached for release is the Woolworths Group Appendix 4E and 2025 Annual Report for the year ended 29 June 2025. Authorised by: Dom Millgate, Group Company Secretary For further information contact Investors and analysts Paul van Meurs Head of Investor Relations +61 407 521 651 Media Woolworths Press Ofﬁce media@woolworths.com.au +61 2 8885 1033 Woolworths Group Limited ABN 88 000 014 675 1 Woolworths Way, Bella Vista NSW 2153 Current reporting period (52 weeks) 1 July 2024 to 29 June 2025 Prior corresponding period (53 weeks) 26 June 2023 to 30 June 2024 Results for announcement to the market Key information % CHANGE $M Revenue 1.7 to 69,077 Profit after tax attributable to equity holders of the parent entity before significant items1 (19.1) to 1,385 Profit after tax attributable to equity holders of the parent entity >100 to 963 1 Significant items for the current period includes the BIG W impairment of $346 million, MyDeal impairment and closure costs of $52 million, Healthylife impairment of $17 million, support office and store operating model redundancy and restructuring costs of $146 million, and other net costs of $8 million, partially offset by an income tax benefit of $147 million. Details relating to dividends 1 CENTS PER SHARE $M 2025 interim dividend paid on 23 April 2025 39 476 2025 final dividend declared on 27 August 2025 2,3 45 5504 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 final dividend is 3 September 2025. 3 The 2025 final dividend is payable on or around 26 September 2025 and is not provided for as at 29 June 2025. 4 Represents the anticipated dividend based on the shares on issue as at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 final dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of ten trading days commencing on 5 September 2025. The last date for receipt of election notices for the DRP is 4 September 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 26 September 2025 to satisfy its obligations under the DRP. Net tangible assets per share AS AT 29 JUNE 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE Net tangible assets per share 1 12.4 43.8 1 Net tangible assets per share is calculated as net assets of $4,962 million (2024: $5,570 million) adjusted for intangible assets of $4,709 million (2024: $4,873 million) and non-controlling interests of $102 million (2024: $162 million) and is based on the closing number of fully paid ordinary shares of 1,221,595,333 (2024: 1,221,588,831). Details of subsidiaries, associates and joint ventures Entities that the Group gained control of or incorporated During the period ended 29 June 2025, the Group gained control of or incorporated the following entities: COMPANY COUNTRY OF INCORPORATION INCORPORATION OR ACQUISITION DATE ACN 681 603 234 Pty Ltd Australia 6 November 2024 Hypersonic Technologies Inc. USA 14 August 2024 Big Dog Australia Pty Ltd Australia 24 February 2025 Big Dog Pet Foods Pty Ltd Australia 24 February 2025 Chris Essex Holdings Pty Ltd Australia 24 February 2025 Golp Pty Ltd Australia 24 February 2025 Timepet Pty Ltd Australia 24 February 2025 GDL Rx No11 Limited New Zealand 28 May 2025 Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E Entities that the Group gained control of or incorporated (continued) In addition, on 2 June 2025, the Group acquired 100% of the issued share capital in The Kitchenary Holdings Pty Ltd, indirectly increasing its ownership interest in The Kitchenary Pty Ltd (B & J City Kitchen Pty Ltd) from 23% to 100% of the issued share capital. As a result, the Group gained control of the following entities: COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Alors Holdings Pty Ltd Australia 2 June 2025 The Kitchenary Holdings Pty Ltd Australia 2 June 2025 The Kitchenary NZ Pty Ltd Australia 2 June 2025 The Kitchenary Pty Ltd Australia 2 June 2025 Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 29 JUNE 2025 30 JUNE 2024 173 Burke Rd JV Pty Ltd 50.1% 50.1% Quantium Telstra Pty Ltd 1 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% W23 Global Fund LP 20.0% 20.0% W23 Global GP LLP 20.0% 20.0% FutureFeed Pty Ltd 12.4% 12.4% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4E disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance and other factors affecting the results for the current period, are contained in the 2025 Annual Report and accompanying F25 Full Year Profit and Dividend Announcement. The Consolidated Financial Statements contained within the 2025 Annual Report, of which this report is based upon, have been audited by Deloitte Touche Tohmatsu. Details of subsidiaries, associates and joint ventures (continued) Appendix 4E – Preliminary Final Report under ASX Listing Rule 4.3A Woolworths Group Limited Appendix 4E potential Realising our 2025 Annual Report WOOLWORTHS GROUP LIMITED ABN 88 000 014 675 Contents SECTION 1
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: revenue, income, NPAT

```text
Revenue 3.7 to 35,930 Profit attributable to equity holders of the parent entity before significant items (20.6) to 739 Profit attributable to equity holders of the parent entity >100 to 739 Details relating to dividends 1 CENTS PER SHARE $M 2024 interim dividend paid on 11 April 2024 47 574 2024 final dividend paid on 30 September 2024 57 696 2024 special dividend paid on 30 September 2024 40 489 2025 interim dividend declared on 26 February 2025 2,3 39 4764 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 interim dividend is 6 March 2025. 3 The 2025 interim dividend is payable on or around 23 April 2025, and is not provided for as at 5 January 2025. 4 Represents the anticipated dividend based on the shares on issue at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 interim dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of 10 trading days commencing on 10 March 2025, rounded to the nearest cent. The last date for receipt of election notices for the DRP is 7 March 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 23 April 2025 to satisfy its obligations under the DRP . Net tangible assets per share AS AT 5 JANUARY 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE 31 DECEMBER 2023 CENTS PER SHARE Net tangible assets per share 1 24.8 43.8 73.6 1 Net tangible assets is calculated as net assets excluding intangible assets and non-controlling interest and is based on the closing number of shares at the respective reporting date. Details of subsidiaries, associates and joint ventures Entities that the Group incorporated or gained control of during the current reporting period COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Hypersonic Technologies Inc. United States 14 August 2024 A.C.N. 681 603 234 PTY. LTD. Australia 6 November 2024 Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D i Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 5 JANUARY 2025 30 JUNE 2024 31 DECEMBER 2023 173 Burke Rd JV Pty Ltd 50.1% 50.1% 50.1% Quantium Telstra Pty Ltd1 49.9% 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% 40.0% Sherpa (Aust) Pty Ltd – 27.0% 27.0% B & J City Kitchen Pty Ltd 23.0% 23.0% 23.0% W23 Global Fund LP 20.0% 20.0% – W23 Global GP LLP 20.0% 20.0% – FutureFeed Pty Ltd 12.4% 12.4% 13.8% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4D disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance, and other factors affecting the results for the current period are contained in the Half-Year Financial Report 2025 and Press Release (F25 Half-Year Profit and Dividend Announcement). The Consolidated Financial Statements contained within the Half-Year Financial Report 2025, upon which this report is based, have been reviewed by Deloitte Touche Tohmatsu. Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D ii Woolworths Group Limited ABN 88 000 014 675 Half-Year Financial Report 2025 Directors’ Report 2 Auditor’s Independence Declaration 3 Consolidated Financial Statements Consolidated Statement of Profit or Loss 4 Consolidated Statement of Other Comprehensive Income or Loss 5 Consolidated Statement of Financial Position 6 Consolidated Statement of Changes in Equity 7 Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: cash flow statement, operating cash flow

```text
Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the basic loss per share calculation as the effect of share rights expected to vest was anti-dilutive and excluded from the calculation). The above Consolidated Statement of Profit or Loss should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Profit or Loss 4 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Profit/(loss) for the period 741 (773) Other comprehensive income/(loss) Items that may be subsequently reclassified to profit or loss, net of tax Effective portion of changes in the fair value of cash flow hedges 58 (22) Foreign currency translation of foreign operations (8) 25 Items that will not be subsequently reclassified to profit or loss, net of tax Fair value gain on equity investments designated as at fair value through other comprehensive income 1 – Other
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: free cash flow, cash movement

```text
Net cash provided by operating activities 1,899 2,582 Cash flows from investing activities Proceeds from the sale of property, plant and equipment 142 124 Payments for property, plant and equipment and intangible assets (1,218) (1,315) Proceeds from the sale of subsidiaries and investments, net of cash disposed 408 – Payments for the purchase of businesses – (8) Payments for the purchase of investments – (2) Advances to non-related parties (10) – Dividends received – 12 Net cash used in investing activities (678) (1,189) Cash flows from financing activities Repayment of the principal component of lease liabilities (674) (652) Proceeds from borrowings 8 2,093 784 Repayment of borrowings 8 (1,043) (351) Dividends paid 9 (1,185) (598) Dividends paid to non-controlling interests (3) (15) Payments for the purchase of additional equity interests in subsidiaries (420) – Payment for shares held in trust 10 (1) (1) Net cash used in financing activities (1,233) (833) Net (decrease)/increase in cash and cash equivalents (12) 560 Effect of exchange rate changes on cash and cash equivalents 3 1 Cash and cash equivalents at start of period 1,298 1,135 Cash and cash equivalents at end of period 2 1,289 1,696 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 Included in cash and cash equivalents is $633 million (30 June 2024: $683 million) relating to receivables from credit card merchants for electronic funds transfers, and credit card and debit card point of sale transactions. The above Consolidated Statement of Cash Flows should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Cash Flows 8 Woolworths Group Half-Year Financial Report 2025 1 General information Woolworths Group Limited (the Company) is a for-profit company incorporated and domiciled in Australia. The Half-Year Financial Report of the Company is for the 27-week period ended 5 January 2025 and comprises the Company and its subsidiaries (together referred to as the Group). The comparative period is the 27-week period ended 31 December 2023. The Half-Year Financial Report was authorised for issue by the Directors on 26 February 2025. 1.1 Statement of compliance The Half-Year Financial Report of the Group is a general purpose condensed financial report prepared in accordance with the Corporations Act 2001 and Australian Accounting Standard AASB 134 Interim Financial Reporting (AASB 134). Compliance with AASB 134 ensures compliance with International Financial Reporting Standard IAS 34 Interim Financial Reporting. The Half-Year Financial Report does not include all of the information required for a full Financial Report, and should be read in conjunction with the Company’s Financial Report for the 53-week period ended 30 June 2024 (2024 Financial Report), and any public announcements by Woolworths Group Limited and its subsidiaries during the half-year in accordance with continuous disclosure obligations under the Corporations Act 2001 and ASX Listing Rules. 1.2 Basis of preparation 1.2.1 Basis of accounting All amounts are presented in Australian dollars and have been rounded to the nearest million dollars unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. The accounting policies applied in the preparation of the Half-Year Financial Report are consistent with those applied in the 2024 Financial Report. These accounting policies are consistent with Australian Accounting Standards and International Financial Reporting Standards. On 3 January 2024, the Group acquired a 55% controlling interest in PETstock Pty Ltd (Petstock) and consolidated its results from this date onwards. As such, the results of Petstock were not included within the comparative period ended 31 December 2023. Certain comparative amounts have been restated to conform with the current period’s presentation. This includes the impact from the following: • The establishment of a new operating segment, W Living, where, in accordance with AASB 8 Operating Segments (AASB 8), the Group restated the amounts presented in the prior period to reflect W Living as a separate segment; and • The reporting of intersegment sales to better reflect how each segment would be reported if it was a standalone business. Previously, the Group eliminated intersegment sales within each reportable segment. Refer to Note 5 for further details. 1.2.2 Going concern The Directors have, at the time of approving the Half-Year Financial Report, a reasonable expectation that the Group has adequate resources to continue in operational existence for the foreseeable future. The going concern basis of accounting has been determined after taking into consideration all available information at the time of approving the Half-Year Financial Report. Notwithstanding that the Group’s working capital position is in a net current liability position as at 5 January 2025 of $4,720 million (30 June 2024: net current liability position of $5,828 million), the Directors continually monitor the Group’s working capital position, including forecast working capital requirements, and are satisfied that the Group’s current cash reserves, expected cash flows from operations and available facilities will enable the Group to pay its debts as and when they fall due. The net current liability position is principally due to the fast turning nature of inventories, the timing of payments to suppliers, the use of available funds to support investments that are classified as non-current assets, and the Group’s current lease obligations. 1.3 New accounting Standards and Interpretations The Group has adopted all the new and revised Standards and Interpretations issued by the Australian Accounting Standards Board that are relevant to its operations and effective for annual reporting periods beginning on or after 1 July
```

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: cash, debt, gearing, capital

```text
Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the basic loss per share calculation as the effect of share rights expected to vest was anti-dilutive and excluded from the calculation). The above Consolidated Statement of Profit or Loss should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Profit or Loss 4 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Profit/(loss) for the period 741 (773) Other comprehensive income/(loss) Items that may be subsequently reclassified to profit or loss, net of tax Effective portion of changes in the fair value of cash flow hedges 58 (22) Foreign currency translation of foreign operations (8) 25 Items that will not be subsequently reclassified to profit or loss, net of tax Fair value gain on equity investments designated as at fair value through other comprehensive income 1 – Other comprehensive income for
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: segment performance, sector metrics

```text
segment, W Living, where, in accordance with AASB 8 Operating Segments (AASB 8), the Group restated the amounts presented in the prior period to reflect W Living as a separate segment; and • The reporting of intersegment sales to better reflect how each segment would be reported if it was a standalone business. Previously, the Group eliminated intersegment sales within each reportable segment. Refer to Note 5 for further details. 1.2.2 Going concern The Directors have, at the time of approving the Half-Year Financial Report, a reasonable expectation that the Group has adequate resources to continue in operational existence for the foreseeable future. The going concern basis of accounting has been determined after taking into consideration all available information at the time of approving the Half-Year Financial Report. Notwithstanding that the Group’s working capital position is in a net current liability position as at 5 January 2025 of $4,720 million (30 June 2024: net current liability position of $5,828 million), the Directors continually monitor the Group’s working capital position, including forecast working capital requirements, and are satisfied that the Group’s current cash reserves, expected cash flows from operations and available facilities will enable the Group to pay its debts as and when they fall due. The net current liability position is principally due to the fast turning nature of inventories, the timing of payments to suppliers, the use of available funds to support investments that are classified as non-current assets, and the Group’s current lease obligations. 1.3 New accounting Standards and Interpretations The Group has adopted all the new and revised Standards and Interpretations issued by the Australian Accounting Standards Board that are relevant to its operations and effective for annual reporting periods beginning on or after 1 July 2024, which did not have a material impact on the financial statements of the Group. The Group has not early adopted any Standards, Interpretations or amendments that have been issued but are not yet effective. Condensed Notes to the Consolidated Financial Statements for the half-year ended 5 January 2025 9 Woolworths Group Half-Year Financial Report 2025 1.4 Critical accounting estimates and judgements In applying the Group’s accounting policies, the Directors are required to make estimates, judgements and assumptions that affect amounts reported in this Half-Year Financial Report. The estimates, judgements and assumptions are based on historical experience, adjusted for current market conditions and other factors that are believed to be reasonable under the circumstances, and are reviewed on a regular basis. Actual results may differ from these estimates. The estimates, judgements and assumptions which involve a higher degree of complexity or that have a significant risk of causing a material adjustment to the amounts recognised in the Consolidated Financial Statements include impairment of non-financial assets (refer to Note 7), provisions and other financial assets and liabilities as disclosed below. 1.4.1 Provisions Included in provisions is the team member remediation provision, which represents the Group’s best estimates of the expenditure required to settle the Group’s obligations under the General Retail Industry Award (GRIA) as well as other modern awards, enterprise agreements (EAs), and statutory entitlements for both salaried and hourly paid team members across the Group. The critical accounting estimates and judgements required to measure the team member remediation provision include, but are not limited to, discount rates, expected future salary and wage levels, periods of service, wage growth and future inflation. TEAM MEMBER REMEDIATION PROVISIONS End-to-end payroll review During the 2021 financial period, the Group established an end-to-end review across the Group’s payroll systems and processes to test and ensure compliance with the Group’s obligations under the GRIA as well as other modern awards, EAs, and statutory entitlements for both salaried and hourly paid team members across the Group. As part of this review, certain areas of non-compliance were identified. The Group has applied extensive resources to the review and analysis of its records, and the calculation of the likely remediation to affected team members. Notwithstanding this, uncertainty remains in relation to the Group’s exposure as engagement with team members and the relevant regulators remains in progress. During the 2023 financial period, the Group concluded its compliance testing and finalised remediation estimates relating to its multi-year review program across the relevant awards and EAs covering all employees, including the Group’s supply chain operations. There were no material new payroll remediation items identified during the current period. As at 5 January 2025, the Group has recognised $175 million (30 June 2024: $199 million) of team member remediation provisions of which $114 million (30 June 2024: $137 million) relates to hourly paid team members and $61 million (30 June 2024: $62 million) relates to salaried team members. The provisions recognised as at 5 January 2025 represent the Group’s best estimate of the remaining payroll remediation obligations. The provisions remain subject to verification, finalisation of payments to the respective team members, and the outcomes from any further interactions with the relevant regulatory bodies. Hourly paid team members As at 5 January 2025, the Group has a remaining provision of $114 million relating to team member payment shortfalls (including interest and on-costs) as a result of non-compliance with EAs for hourly paid team members. As at 5 January 2025, total payments of $154 million have been made to impacted hourly paid team members and any changes as a result of new information will be treated as a change in accounting estimate and will be recognised in the Consolidated
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: outlook, management commentary

```text
commentary on significant features of the operating performance, results of segments, trends in performance, and other factors affecting the results for the current period are contained in the Half-Year Financial Report 2025 and Press Release (F25 Half-Year Profit and Dividend Announcement). The Consolidated Financial Statements contained within the Half-Year Financial Report 2025, upon which this report is based, have been reviewed by Deloitte Touche Tohmatsu. Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D ii Woolworths Group Limited ABN 88 000 014 675 Half-Year Financial Report 2025 Directors’ Report 2 Auditor’s Independence Declaration 3 Consolidated Financial Statements Consolidated Statement of Profit or Loss 4 Consolidated Statement of Other Comprehensive Income or Loss 5 Consolidated Statement of Financial Position 6 Consolidated Statement of Changes in Equity 7 Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: dividends, capital management

```text
dividend paid on 11 April 2024 47 574 2024 final dividend paid on 30 September 2024 57 696 2024 special dividend paid on 30 September 2024 40 489 2025 interim dividend declared on 26 February 2025 2,3 39 4764 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 interim dividend is 6 March 2025. 3 The 2025 interim dividend is payable on or around 23 April 2025, and is not provided for as at 5 January 2025. 4 Represents the anticipated dividend based on the shares on issue at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 interim dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of 10 trading days commencing on 10 March 2025, rounded to the nearest cent. The last date for receipt of election notices for the DRP is 7 March 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 23 April 2025 to satisfy its obligations under the DRP . Net tangible assets per share AS AT 5 JANUARY 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE 31 DECEMBER 2023 CENTS PER SHARE Net tangible assets per share 1 24.8 43.8 73.6 1 Net tangible assets is calculated as net assets excluding intangible assets and non-controlling interest and is based on the closing number of shares at the respective reporting date. Details of subsidiaries, associates and joint ventures Entities that the Group incorporated or gained control of during the current reporting period COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Hypersonic Technologies Inc. United States 14 August 2024 A.C.N. 681 603 234 PTY. LTD. Australia 6 November 2024 Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D i Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 5 JANUARY 2025 30 JUNE 2024 31 DECEMBER 2023 173 Burke Rd JV Pty Ltd 50.1% 50.1% 50.1% Quantium Telstra Pty Ltd1 49.9% 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% 40.0% Sherpa (Aust) Pty Ltd – 27.0% 27.0% B & J City Kitchen Pty Ltd 23.0% 23.0% 23.0% W23 Global Fund LP 20.0% 20.0% – W23 Global GP LLP 20.0% 20.0% – FutureFeed Pty Ltd 12.4% 12.4% 13.8% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4D disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance, and other factors affecting the results for the current period are contained in the Half-Year Financial Report 2025 and Press Release (F25 Half-Year Profit and Dividend Announcement). The Consolidated Financial Statements contained within the Half-Year Financial Report 2025, upon which this report is based, have been reviewed by Deloitte Touche Tohmatsu. Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D ii Woolworths Group Limited ABN 88 000 014 675 Half-Year Financial Report 2025 Directors’ Report 2 Auditor’s Independence Declaration 3 Consolidated Financial Statements Consolidated Statement of Profit or Loss 4 Consolidated Statement of Other Comprehensive Income or Loss 5 Consolidated Statement of Financial Position 6 Consolidated Statement of Changes in Equity 7 Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing
```

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: capex, commitments

```text
Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the basic loss per share calculation as the effect of share rights expected to vest was anti-dilutive and excluded from the calculation). The above Consolidated Statement of Profit or Loss should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Profit or Loss 4 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Profit/(loss) for the period 741 (773) Other comprehensive income/(loss) Items that may be subsequently reclassified to profit or loss, net of tax Effective portion of changes in the fair value of cash flow hedges 58 (22) Foreign currency translation of foreign operations (8) 25 Items that will not be subsequently reclassified to profit or loss, net of tax Fair value gain on equity investments designated as at fair value through other comprehensive income 1 – Other comprehensive income for the period 51 3 Total comprehensive income/(loss) for the period 792 (770) Total comprehensive income/(loss) for the period attributable to: Equity holders of the parent entity 790 (778) Non-controlling interests 2 8 Total comprehensive income/(loss) for the period 792 (770) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024.
```

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: risks

```text
Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the basic loss per share calculation as the effect of share rights expected to vest was anti-dilutive and excluded from the calculation). The above Consolidated Statement of Profit or Loss should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Profit or Loss 4 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Profit/(loss) for the period 741 (773) Other comprehensive income/(loss) Items that may be subsequently reclassified to profit or loss, net of tax Effective portion of changes in the fair value of cash flow hedges 58 (22) Foreign currency translation of foreign operations (8) 25 Items that will not be subsequently reclassified to profit or loss, net of tax Fair value gain on equity investments designated as at fair value through other comprehensive income 1 – Other comprehensive income for the period 51 3 Total comprehensive income/(loss) for the period 792 (770) Total comprehensive income/(loss) for the period attributable to: Equity holders of the parent entity 790 (778) Non-controlling interests 2 8 Total comprehensive income/(loss) for the
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: one-off items

```text
Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the basic loss per share calculation as the effect of share rights expected to vest was anti-dilutive and excluded from the calculation). The above Consolidated Statement of Profit or Loss should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Profit or Loss 4 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Profit/(loss) for the period 741 (773) Other comprehensive income/(loss) Items that may be subsequently reclassified to profit or loss, net of tax Effective portion of changes in the fair value of cash flow hedges 58 (22) Foreign currency translation of foreign operations (8) 25 Items that will not be subsequently reclassified to profit or loss, net of tax Fair value gain on equity investments designated as at fair value through other comprehensive income 1 – Other comprehensive income for the period 51 3 Total comprehensive income/(loss) for the period 792 (770) Total comprehensive income/(loss) for the period attributable to: Equity holders of the parent entity 790 (778) Non-controlling interests 2 8 Total comprehensive income/(loss) for the
```

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
assets per share AS AT 5 JANUARY 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE 31 DECEMBER 2023 CENTS PER SHARE Net tangible assets per share 1 24.8 43.8 73.6 1 Net tangible assets is calculated as net assets excluding intangible assets and non-controlling interest and is based on the closing number of shares at the respective reporting date. Details of subsidiaries, associates and joint ventures Entities that the Group incorporated or gained control of during the current reporting period COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Hypersonic Technologies Inc. United States 14 August 2024 A.C.N. 681 603 234 PTY. LTD. Australia 6 November 2024 Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D i Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 5 JANUARY 2025 30 JUNE 2024 31 DECEMBER 2023 173 Burke Rd JV Pty Ltd 50.1% 50.1% 50.1% Quantium Telstra Pty Ltd1 49.9% 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% 40.0% Sherpa (Aust) Pty Ltd – 27.0% 27.0% B & J City Kitchen Pty Ltd 23.0% 23.0% 23.0% W23 Global Fund LP 20.0% 20.0% – W23 Global GP LLP 20.0% 20.0% – FutureFeed Pty Ltd 12.4% 12.4% 13.8% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4D disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance, and other factors affecting the results for the current period are contained in the Half-Year Financial Report 2025 and Press Release (F25 Half-Year Profit and Dividend Announcement). The Consolidated Financial Statements contained within the Half-Year Financial Report 2025, upon which this report is based, have been reviewed by Deloitte Touche Tohmatsu. Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D ii Woolworths Group Limited ABN 88 000 014 675 Half-Year Financial Report 2025 Directors’ Report 2 Auditor’s Independence Declaration 3 Consolidated Financial Statements Consolidated Statement of Profit or Loss 4 Consolidated Statement of Other Comprehensive Income or Loss 5 Consolidated Statement of Financial Position 6 Consolidated Statement of Changes in Equity 7 Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: segment table, product table, sector metrics

```text
segment would be reported if it was a standalone business. Previously, the Group eliminated intersegment sales within each reportable segment. Refer to Note 5 for further details. 1.2.2 Going concern The Directors have, at the time of approving the Half-Year Financial Report, a reasonable expectation that the Group has adequate resources to continue in operational existence for the foreseeable future. The going concern basis of accounting has been determined after taking into consideration all available information at the time of approving the Half-Year Financial Report. Notwithstanding that the Group’s working capital position is in a net current liability position as at 5 January 2025 of $4,720 million (30 June 2024: net current liability position of $5,828 million), the Directors continually monitor the Group’s working capital position, including forecast working capital requirements, and are satisfied that the Group’s current cash reserves, expected cash flows from operations and available facilities will enable the Group to pay its debts as and when they fall due. The net current liability position is principally due to the fast turning nature of inventories, the timing of payments to suppliers, the use of available funds to support investments that are classified as non-current assets, and the Group’s current lease obligations. 1.3 New accounting Standards and Interpretations The Group has adopted all the new and revised Standards and Interpretations issued by the Australian Accounting Standards Board that are relevant to its operations and effective for annual reporting periods beginning on or after 1 July 2024, which did not have a material impact on the financial statements of the Group. The Group has not early adopted any Standards, Interpretations or amendments that have been issued but are not yet effective. Condensed Notes to the Consolidated Financial Statements for the half-year ended 5 January 2025 9 Woolworths Group Half-Year Financial Report 2025 1.4 Critical accounting estimates and judgements In applying the Group’s accounting policies, the Directors are required to make estimates, judgements and assumptions that affect amounts reported in this Half-Year Financial Report. The estimates, judgements and assumptions are based on historical experience, adjusted for current market conditions and other factors that are believed to be reasonable under the circumstances, and are reviewed on a regular basis. Actual results may differ from these estimates. The estimates, judgements and assumptions which involve a higher degree of complexity or that have a significant risk of causing a material adjustment to the amounts recognised in the Consolidated Financial Statements include impairment of non-financial assets (refer to Note 7), provisions and other financial assets and liabilities as disclosed below. 1.4.1 Provisions Included in provisions is the team member remediation provision, which represents the Group’s best estimates of the expenditure required to settle the Group’s obligations under the General Retail Industry Award (GRIA) as well as other modern awards, enterprise agreements (EAs), and statutory entitlements for both salaried and hourly paid team members across the Group. The critical accounting estimates and judgements required to measure the team member remediation provision include, but are not limited to, discount rates, expected future salary and wage levels, periods of service, wage growth and future inflation. TEAM MEMBER REMEDIATION PROVISIONS End-to-end payroll review During the 2021 financial period, the Group established an end-to-end review across the Group’s payroll systems and processes to test and ensure compliance with the Group’s obligations under the GRIA as well as other modern awards, EAs, and statutory entitlements for both salaried and hourly paid team members across the Group. As part of this review, certain areas of non-compliance were identified. The Group has applied extensive resources to the review and analysis of its records, and the calculation of the likely remediation to affected team members. Notwithstanding this, uncertainty remains in relation to the Group’s exposure as engagement with team members and the relevant regulators remains in progress. During the 2023 financial period, the Group concluded its compliance testing and finalised remediation estimates relating to its multi-year review program across the relevant awards and EAs covering all employees, including the Group’s supply chain operations. There were no material new payroll remediation items identified during the current period. As at 5 January 2025, the Group has recognised $175 million (30 June 2024: $199 million) of team member remediation provisions of which $114 million (30 June 2024: $137 million) relates to hourly paid team members and $61 million (30 June 2024: $62 million) relates to salaried team members. The provisions recognised as at 5 January 2025 represent the Group’s best estimate of the remaining payroll remediation obligations. The provisions remain subject to verification, finalisation of payments to the respective team members, and the outcomes from any further interactions with the relevant regulatory bodies. Hourly paid team members As at 5 January 2025, the Group has a remaining provision of $114 million relating to team member payment shortfalls (including interest and on-costs) as a result of non-compliance with EAs for hourly paid team members. As at 5 January 2025, total payments of $154 million have been made to impacted hourly paid team members and any changes as a result of new information will be treated as a change in accounting estimate and will be recognised in the Consolidated Statement of Profit or Loss in the period in which the new information is available. Salaried team members On 30 October 2019, the Group disclosed that a number of salaried team members had not been paid in full compliance with the Group’s obligations under the
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: sales growth
- Unavailable reason: sales growth was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: EBIT margin
- Unavailable reason: EBIT margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: inventory

```text
Inventories 4,470 4,187 3,999 Other financial assets 6 91 23 22 Current tax receivable 61 – – Other current assets 308 221 251 7,304 6,791 6,964 Assets held for sale 80 200 352 Total current assets 7,384 6,991 7,316 Non-current assets Trade and other receivables 145 129 126 Other financial assets 6 272 600 999 Lease assets 9,505 9,604 9,432 Property, plant and equipment 9,953 9,678 9,136 Intangible assets 4,827 4,873 4,198 Investments accounted for using the equity method 79 78 69 Deferred tax assets 1,609 1,647 1,586 Other non-current assets 314 336 345 Total non-current assets 26,704 26,945 25,891 Total assets 34,088 33,936 33,207 Current liabilities Trade and other payables 8,115 7,762 8,096 Lease liabilities 1,563 1,599 1,629 Borrowings 8 423 712 596 Current tax payable 13 303 243 Other financial liabilities 6 287 689 263 Provisions 1,695 1,706 1,709 Other current liabilities 8 10 13 12,104 12,781 12,549 Liabilities directly associated with assets held for sale – 38 – Total current liabilities 12,104 12,819 12,549 Non-current liabilities Lease liabilities 10,378 10,545 10,206 Borrowings 8 5,258 3,866 3,636 Other financial liabilities 6 78 126 647 Provisions 954 894 852 Deferred tax liability 62 83 53 Other non-current liabilities 28 33 33 Total non-current liabilities 16,758 15,547 15,427 Total liabilities 28,862 28,366 27,976 Net assets 5,226 5,570 5,231 Equity Contributed equity 10 5,649 5,604 5,645 Reserves (7, 487) (7,609) (7,646) Retained earnings 6,967 7,413 7,098 Equity attributable to equity holders of the parent entity 5,129 5,408 5,097 Non-controlling interests 97 162 134 Total equity 5,226 5,570 5,231 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. The above Consolidated Statement of Financial Position should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Financial Position 6 Woolworths Group Half-Year Financial Report 2025 ATTRIBUTABLE TO EQUITY HOLDERS OF THE PARENT ENTITY HALF-YEAR ENDED 5 JANUARY 20251 SHARE CAPITAL $M SHARES HELD IN TRUST $M RESERVES $M RETAINED EARNINGS $M TOTAL $M NON- CONTROLLING INTERESTS $M TOTAL EQUITY $M Balance at 30 June 2024 5,665 (61) (7,609) 7, 413 5,408 162 5,570 Profit for the period – – – 739 739 2 741 Other comprehensive income for the period – – 51 – 51 – 51 Total comprehensive income for the period – – 51 739 790 2 792 Dividends paid – – – (1,185) (1,185) – (1,185) Issue/(transfer) of shares to satisfy employee long-term incentive plans – 46 (46) – – – – Purchase of shares by the Woolworths Employee Share Trust – (1) – – (1) – (1) Purchase of additional equity interests in subsidiaries – – 68 – 68 (68) – Share-based payments expense – – 51 – 51 1 52 Deferred tax on share-based payments expense – – (2) – (2) – (2) Balance at 5 January 2025 5,665 (16) (7, 487) 6,967 5,129 97 5,226 ATTRIBUTABLE TO EQUITY HOLDERS OF THE PARENT ENTITY HALF-YEAR ENDED 31 DECEMBER 2023 SHARE CAPITAL $M SHARES HELD IN TRUST $M RESERVES $M RETAINED EARNINGS $M TOTAL $M NON- CONTROLLING INTERESTS $M TOTAL EQUITY $M Balance at 25 June 2023 5,556 (150) (7,567 ) 8,586 6,425 140 6,565 (Loss)/profit for the period – – – (781) (781) 8 (773) Other comprehensive income for the period – – 3 – 3 – 3 Total comprehensive income/(loss) for the period – – 3 (781) (778) 8 (770) Dividends paid – – – (707) (707) (15) (722) Issue/(transfer) of shares to satisfy employee long-term incentive plans – 131 (131) – – – – Issue of shares to satisfy the dividend reinvestment plan 109 – – – 109 – 109 Purchase of shares by the Woolworths Employee Share Trust – (1) – – (1) – (1) Derecognition on loss of significant influence over associate – – (3) – (3) – (3) Share-based payments expense – – 52 – 52 1 53 Balance at 31 December 2023 5,665 (20) (7,646) 7,098 5,097 134 5,231 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. The above Consolidated Statement of Changes in Equity should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Changes in Equity 7 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Cash flows from operating activities Receipts from customers 38,157 36,841 Payments to suppliers and employees (35,138) (33,435) Payments for the interest component of lease liabilities (356) (333) Net finance costs paid on borrowings (105) (67) Income tax paid (659) (424) Net cash provided by operating activities 1,899 2,582 Cash flows from investing activities Proceeds from the sale of property, plant and equipment 142 124 Payments for property, plant and equipment and intangible assets (1,218) (1,315) Proceeds from the sale of subsidiaries and investments, net of cash disposed 408 – Payments for the purchase of businesses – (8) Payments for the purchase of investments – (2) Advances to non-related parties (10) – Dividends received – 12 Net cash used in investing activities (678) (1,189) Cash flows from financing activities Repayment of the principal component of lease liabilities (674) (652) Proceeds from borrowings 8 2,093 784 Repayment of borrowings 8 (1,043) (351) Dividends paid 9 (1,185) (598) Dividends paid to non-controlling interests (3) (15) Payments for the purchase of additional equity interests in subsidiaries (420) – Payment for shares held in trust 10 (1) (1) Net cash used in financing activities (1,233) (833) Net (decrease)/increase in cash and cash equivalents (12) 560 Effect of exchange rate changes on cash and cash equivalents 3 1 Cash and cash equivalents at start of period 1,298 1,135 Cash and cash equivalents at end of period 2 1,289 1,696 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 Included in cash and cash equivalents is $633 million
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: capex

```text
capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025. Scott Perkins Chair Amanda Bardwell Managing Director and Chief Executive Officer 2 Woolworths Group Half-Year Financial Report 2025 Auditor’s Independence Declaration 26 February 2025 Board of Directors Woolworths Group Limited 1 Woolworths Way Bella Vista NSW 2153 Dear Board Members Auditor’s Independence Declaration – Woolworths Group Limited In accordance with section 307C of the Corporations Act 2001, we are pleased to provide the following declaration of independence to the Board of Directors of Woolworths Group Limited. As lead audit partners for the review of the financial report of Woolworths Group Limited for the half-year ended 5 January 2025, we declare that to the best of our knowledge and belief, there have been no contraventions of: (i) the auditor independence requirements of the Corporations Act 2001 in relation to the review; and (ii) any applicable code of professional conduct in relation to the review. Yours faithfully DELOITTE TOUCHE TOHMATSU Tom Imbesi Travis Simkin Partner Partner Chartered Accountants Chartered Accountants Liability limited by a scheme approved under Professional Standards Legislation. Member of Deloitte Asia Pacific Limited and the Deloitte organisation. Deloitte Touche Tohmatsu A.B.N. 74 490 121 060 Quay Quarter Tower Level 46, 50 Bridge St Sydney NSW 2000 Tel: +61 (0) 2 9322 7000 www.deloitte.com.au 3 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED NOTE 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Revenue 2 35,930 34,635 Cost of sales (26,154) (25,154) Gross profit 9,776 9,481 Other income 2 135 154 Branch expenses 2 3 (6,359) (5,910) Administration expenses 2 3 (2,101) (3,747) Earnings/(loss) before interest and tax 1,451 (22) Net finance costs 4 (416) (358) Profit/(loss) before income tax 1,035 (380) Income tax expense (294) (393) Profit/(loss) for the period 741 (773) Profit/(loss) for the period attributable to: Equity holders of the parent entity 739 (781) Non-controlling interests 2 8 Profit/(loss) for the period 741 (773) Earnings/(loss) per share attributable to equity holders of the parent entity CENTS CENTS Basic earnings/(loss) per share 3 60.5 (64.1) Diluted earnings/(loss) per share 4 60.2 (64.1) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note 1.2 for further details. 2 In the prior period, administration expenses included a $1,492 million impairment of goodwill in New Zealand Food and a $209 million loss relating to the loss of significant influence over Endeavour Group Limited and branch expenses included a $13 million impairment relating to the transformation and rebranding of Countdown stores to Woolworths New Zealand. 3 Weighted average number of shares used to calculate basic earnings/(loss) per share is 1,220.7 million (2024: 1,218.7 million), net of shares held in trust. 4 Weighted average number of shares used in the diluted earnings/(loss) per share calculation is 1,227.1 million (2024: 1,218.7 million, which is the same as used in the basic loss per share calculation as the effect of share rights expected to vest was anti-dilutive and excluded from the calculation). The above Consolidated Statement of Profit or Loss should be read in conjunction with the accompanying Condensed Notes to the Consolidated Financial Statements. Consolidated Statement of Profit or Loss 4 Woolworths Group Half-Year Financial Report 2025 HALF-YEAR ENDED 5 JANUARY 20251 $M 31 DECEMBER 2023 $M Profit/(loss) for the period 741 (773) Other comprehensive income/(loss) Items that may be subsequently reclassified to profit or loss, net of tax Effective portion of changes in the fair value of cash flow hedges 58 (22) Foreign currency translation of foreign operations (8) 25 Items that will not be subsequently reclassified to profit or loss, net of tax Fair value gain on equity investments designated as at fair value through other comprehensive income 1 – Other comprehensive income for the period 51 3 Total comprehensive income/(loss) for the period 792 (770) Total comprehensive income/(loss) for the period attributable to: Equity holders of the parent entity 790 (778) Non-controlling interests 2 8 Total comprehensive income/(loss) for the period 792 (770) 1 Includes the results of PETstock Pty Ltd, which was acquired on 3 January 2024. Refer to Note
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf
- Supports claims: dividends

```text
dividends 1 CENTS PER SHARE $M 2024 interim dividend paid on 11 April 2024 47 574 2024 final dividend paid on 30 September 2024 57 696 2024 special dividend paid on 30 September 2024 40 489 2025 interim dividend declared on 26 February 2025 2,3 39 4764 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 interim dividend is 6 March 2025. 3 The 2025 interim dividend is payable on or around 23 April 2025, and is not provided for as at 5 January 2025. 4 Represents the anticipated dividend based on the shares on issue at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 interim dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of 10 trading days commencing on 10 March 2025, rounded to the nearest cent. The last date for receipt of election notices for the DRP is 7 March 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 23 April 2025 to satisfy its obligations under the DRP . Net tangible assets per share AS AT 5 JANUARY 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE 31 DECEMBER 2023 CENTS PER SHARE Net tangible assets per share 1 24.8 43.8 73.6 1 Net tangible assets is calculated as net assets excluding intangible assets and non-controlling interest and is based on the closing number of shares at the respective reporting date. Details of subsidiaries, associates and joint ventures Entities that the Group incorporated or gained control of during the current reporting period COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Hypersonic Technologies Inc. United States 14 August 2024 A.C.N. 681 603 234 PTY. LTD. Australia 6 November 2024 Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D i Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 5 JANUARY 2025 30 JUNE 2024 31 DECEMBER 2023 173 Burke Rd JV Pty Ltd 50.1% 50.1% 50.1% Quantium Telstra Pty Ltd1 49.9% 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% 40.0% Sherpa (Aust) Pty Ltd – 27.0% 27.0% B & J City Kitchen Pty Ltd 23.0% 23.0% 23.0% W23 Global Fund LP 20.0% 20.0% – W23 Global GP LLP 20.0% 20.0% – FutureFeed Pty Ltd 12.4% 12.4% 13.8% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4D disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance, and other factors affecting the results for the current period are contained in the Half-Year Financial Report 2025 and Press Release (F25 Half-Year Profit and Dividend Announcement). The Consolidated Financial Statements contained within the Half-Year Financial Report 2025, upon which this report is based, have been reviewed by Deloitte Touche Tohmatsu. Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D ii Woolworths Group Limited ABN 88 000 014 675 Half-Year Financial Report 2025 Directors’ Report 2 Auditor’s Independence Declaration 3 Consolidated Financial Statements Consolidated Statement of Profit or Loss 4 Consolidated Statement of Other Comprehensive Income or Loss 5 Consolidated Statement of Financial Position 6 Consolidated Statement of Changes in Equity 7 Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year, and up to the date of this report, are: Non-Executive Directors S Perkins (Chair) W Bray M Brenner J Carr-Smith P Chronican T Fellows H Kramer K Tesija Executive Director A Bardwell (Managing Director and Chief Executive Officer, appointed 21 February 2024, effective 1 September 2024) B Banducci (Managing Director and Chief Executive Officer, retired 1 September 2024) Review and results of operations Refer to F25 Half-Year Profit and Dividend Announcement for the 27 weeks ended 5 January 2025. Rounding of amounts The Half-Year Financial Report is presented in Australian dollars and amounts have been rounded to the nearest million dollars, unless otherwise stated, in accordance with ASIC Corporations (Rounding in Financial/Directors’ Reports) Instrument 2016/191. Auditor’s Independence Declaration The Auditor’s Independence Declaration is set out on page 3. The Half-Year Financial Report is made in accordance with a resolution of the Directors of the Company on 26 February 2025.
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/h1/2855253.pdf

```text
26 February 2025 ASX Market Announcements Ofﬁce Australian Securities Exchange 20 Bridge Street Sydney NSW 2000 Appendix 4D and Half-Year Financial Report Attached for release to the market are the ASX Appendix 4D and the Half-Year Financial Report for the period ended 5 January 2025. Authorised by: Dom Millgate, Group Company Secretary For further information contact Investors and analysts Paul van Meurs Head of Investor Relations +61 407 521 651 Media Woolworths Press Ofﬁce media@woolworths.com.au +61 2 8885 1033 Woolworths Group Limited ABN 88 000 014 675 1 Woolworths Way, Bella Vista NSW 2153 Current reporting period 1 July 2024 to 5 January 2025 Prior corresponding period 26 June 2023 to 31 December 2023 Results for announcement to the market Key information % CHANGE $M Revenue 3.7 to 35,930 Profit attributable to equity holders of the parent entity before significant items (20.6) to 739 Profit attributable to equity holders of the parent entity >100 to 739 Details relating to dividends 1 CENTS PER SHARE $M 2024 interim dividend paid on 11 April 2024 47 574 2024 final dividend paid on 30 September 2024 57 696 2024 special dividend paid on 30 September 2024 40 489 2025 interim dividend declared on 26 February 2025 2,3 39 4764 1 All dividends are fully franked at a 30% tax rate. 2 Record date for determining entitlement to the 2025 interim dividend is 6 March 2025. 3 The 2025 interim dividend is payable on or around 23 April 2025, and is not provided for as at 5 January 2025. 4 Represents the anticipated dividend based on the shares on issue at the date of this report. This value will change if there are any shares issued between the date of this report and the ex-dividend date. The Dividend Reinvestment Plan (DRP) remains active. Eligible shareholders may participate in the DRP in respect of all or part of their shareholding. There is currently no DRP discount applied and no limit on the number of shares that can participate in the DRP. Shares will be allocated to shareholders under the DRP for the 2025 interim dividend at an amount equal to the average of the daily volume weighted average market price of ordinary shares of the Company traded on the ASX over the period of 10 trading days commencing on 10 March 2025, rounded to the nearest cent. The last date for receipt of election notices for the DRP is 7 March 2025. The Company intends to purchase shares on-market and transfer these to participants on or around 23 April 2025 to satisfy its obligations under the DRP . Net tangible assets per share AS AT 5 JANUARY 2025 CENTS PER SHARE 30 JUNE 2024 CENTS PER SHARE 31 DECEMBER 2023 CENTS PER SHARE Net tangible assets per share 1 24.8 43.8 73.6 1 Net tangible assets is calculated as net assets excluding intangible assets and non-controlling interest and is based on the closing number of shares at the respective reporting date. Details of subsidiaries, associates and joint ventures Entities that the Group incorporated or gained control of during the current reporting period COMPANY COUNTRY OF INCORPORATION ACQUISITION DATE Hypersonic Technologies Inc. United States 14 August 2024 A.C.N. 681 603 234 PTY. LTD. Australia 6 November 2024 Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D i Details of associates and joint ventures LEGAL OWNERSHIP INTEREST AS AT 5 JANUARY 2025 30 JUNE 2024 31 DECEMBER 2023 173 Burke Rd JV Pty Ltd 50.1% 50.1% 50.1% Quantium Telstra Pty Ltd1 49.9% 49.9% 49.9% NP Fulfilment Group Pty Limited 40.0% 40.0% 40.0% Sherpa (Aust) Pty Ltd – 27.0% 27.0% B & J City Kitchen Pty Ltd 23.0% 23.0% 23.0% W23 Global Fund LP 20.0% 20.0% – W23 Global GP LLP 20.0% 20.0% – FutureFeed Pty Ltd 12.4% 12.4% 13.8% 1 The Quantium Group Holdings Pty Limited, a subsidiary of the Group, holds a 49.9% ownership interest in this entity, which it classifies as an investment in associate and applies the equity method of accounting. Other Additional Appendix 4D disclosure requirements and further information, including commentary on significant features of the operating performance, results of segments, trends in performance, and other factors affecting the results for the current period are contained in the Half-Year Financial Report 2025 and Press Release (F25 Half-Year Profit and Dividend Announcement). The Consolidated Financial Statements contained within the Half-Year Financial Report 2025, upon which this report is based, have been reviewed by Deloitte Touche Tohmatsu. Appendix 4D under ASX Listing Rule 4.2A Woolworths Group Limited Appendix 4D ii Woolworths Group Limited ABN 88 000 014 675 Half-Year Financial Report 2025 Directors’ Report 2 Auditor’s Independence Declaration 3 Consolidated Financial Statements Consolidated Statement of Profit or Loss 4 Consolidated Statement of Other Comprehensive Income or Loss 5 Consolidated Statement of Financial Position 6 Consolidated Statement of Changes in Equity 7 Consolidated Statement of Cash Flows 8 Condensed Notes to the Consolidated Financial Statements 1 General information 9 2 Revenue and other income 11 3 Branch and administration expenses 12 4 Net finance costs 12 5 Reportable segments 12 6 Other financial assets and liabilities 14 7 Impairment of non-financial assets 14 8 Borrowings 16 9 Dividends 17 10 Contributed equity 17 11 Commitments for capital expenditure 18 12 Contingent liabilities 18 13 Subsequent events 18 Directors’ Declaration 19 Independent Auditor’s Review Report 20 Half-Year Financial Report 2025 Table of Contents 1Woolworths Group Half-Year Financial Report 2025 Directors’ Report This Half-Year Financial Report is presented by the Directors in respect of Woolworths Group Limited (the Company) and the entities it controlled at the end of, or during, the half-year ended 5 January 2025 (the Group). In order to comply with the provisions of the Corporations Act 2001, the Directors’ Report is as follows: The Directors The Directors of the Company at any time during or since the end of the half-year,
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: sales growth
- Unavailable reason: sales growth was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: EBIT margin
- Unavailable reason: EBIT margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: inventory
- Unavailable reason: inventory was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: capex
- Unavailable reason: capex was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS
- Supports claims: dividends
- Unavailable reason: dividend was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Amanda_Bardwell-AVS

```text
Smart Crop Video Viewer
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: sales growth
- Unavailable reason: sales growth was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: EBIT margin
- Unavailable reason: EBIT margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: inventory
- Unavailable reason: inventory was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: capex
- Unavailable reason: capex was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS
- Supports claims: dividends
- Unavailable reason: dividend was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Annette_Karantoni-AVS

```text
Smart Crop Video Viewer
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: sales growth
- Unavailable reason: sales growth was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: EBIT margin
- Unavailable reason: EBIT margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: inventory
- Unavailable reason: inventory was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: capex
- Unavailable reason: capex was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS
- Supports claims: dividends
- Unavailable reason: dividend was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-New_Zealand_Food-AVS

```text
Smart Crop Video Viewer
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: sales growth
- Unavailable reason: sales growth was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: EBIT margin
- Unavailable reason: EBIT margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: inventory
- Unavailable reason: inventory was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: capex
- Unavailable reason: capex was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS
- Supports claims: dividends
- Unavailable reason: dividend was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-Dan_Hake-AVS

```text
Smart Crop Video Viewer
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_sales_growth
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: sales growth
- Unavailable reason: sales growth was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_ebit_margin
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: EBIT margin
- Unavailable reason: EBIT margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_inventory
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: inventory
- Unavailable reason: inventory was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: capex
- Unavailable reason: capex was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_dividends
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS
- Supports claims: dividends
- Unavailable reason: dividend was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://woolworthsgroup.scene7.com/s7viewers/html5/SmartCropVideoViewer.html?asset=woolworthsgroupltd/Woolworths_Group_F25_Full_Year_Results-WooliesX-AVS

```text
Smart Crop Video Viewer
```

```
