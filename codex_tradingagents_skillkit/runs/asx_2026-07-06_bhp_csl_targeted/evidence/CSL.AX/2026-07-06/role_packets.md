# Codex Role Evidence Packet: CSL.AX

- Trade date: `2026-07-06`
- Instrument identity: `CSL Limited`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for CSL.AX from 2026-06-06 to 2026-07-06
# Total records: 20
# Data retrieved on: 2026-07-08 19:48:44

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-06-09,97.95,99.82,96.88,99.47,2260104,0.0,0.0
2026-06-10,99.0,103.3,97.84,102.95,1938109,0.0,0.0
2026-06-11,102.43,108.46,102.15,107.23,2802061,0.0,0.0
2026-06-12,107.68,110.17,106.9,107.51,1951556,0.0,0.0
2026-06-15,107.4,108.37,105.24,105.53,1951611,0.0,0.0
2026-06-16,105.0,106.7,104.74,106.25,1612791,0.0,0.0
2026-06-17,106.0,107.48,105.42,106.79,1732200,0.0,0.0
2026-06-18,106.7,108.44,105.9,108.08,2564654,0.0,0.0
2026-06-19,108.58,116.32,108.5,116.32,8157009,0.0,0.0
2026-06-22,116.25,116.29,110.89,112.88,2612502,0.0,0.0
2026-06-23,114.12,115.8,111.69,112.04,1683171,0.0,0.0
2026-06-24,114.47,117.11,112.67,114.99,1826320,0.0,0.0
2026-06-25,116.0,118.88,115.76,117.65,2066413,0.0,0.0
2026-06-26,114.6,117.14,114.39,114.87,2308629,0.0,0.0
2026-06-29,113.0,116.5,112.4,115.39,1458143,0.0,0.0
2026-06-30,116.0,116.54,113.69,114.74,1606736,0.0,0.0
2026-07-01,115.83,118.37,115.52,118.37,1537670,0.0,0.0
2026-07-02,116.88,118.6,116.33,117.75,1298766,0.0,0.0
2026-07-03,120.0,122.21,118.93,121.81,1442210,0.0,0.0
2026-07-06,121.85,125.0,120.75,124.23,1481014,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for CSL.AX

- Requested analysis date: 2026-07-06
- Latest trading row used: 2026-07-06
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 121.85 |
| High | 125.00 |
| Low | 120.75 |
| Close | 124.23 |
| Volume | 1481014 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 117.40 |
| close_50_sma | 108.81 |
| close_200_sma | 154.40 |
| rsi | 70.22 |
| boll | 112.24 |
| boll_ub | 125.26 |
| boll_lb | 99.22 |
| macd | 3.96 |
| macds | 2.48 |
| macdh | 1.48 |
| atr | 3.78 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-25 | 98.47 |
| 2026-05-26 | 96.90 |
| 2026-05-27 | 99.26 |
| 2026-05-28 | 97.59 |
| 2026-05-29 | 96.61 |
| 2026-06-01 | 94.20 |
| 2026-06-02 | 92.56 |
| 2026-06-03 | 92.24 |
| 2026-06-04 | 92.59 |
| 2026-06-05 | 97.91 |
| 2026-06-09 | 99.47 |
| 2026-06-10 | 102.95 |
| 2026-06-11 | 107.23 |
| 2026-06-12 | 107.51 |
| 2026-06-15 | 105.53 |
| 2026-06-16 | 106.25 |
| 2026-06-17 | 106.79 |
| 2026-06-18 | 108.08 |
| 2026-06-19 | 116.32 |
| 2026-06-22 | 112.88 |
| 2026-06-23 | 112.04 |
| 2026-06-24 | 114.99 |
| 2026-06-25 | 117.65 |
| 2026-06-26 | 114.87 |
| 2026-06-29 | 115.39 |
| 2026-06-30 | 114.74 |
| 2026-07-01 | 118.37 |
| 2026-07-02 | 117.75 |
| 2026-07-03 | 121.81 |
| 2026-07-06 | 124.23 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-06-06 to 2026-07-06:

2026-07-06: 108.81340026855469
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 108.92880020141601
2026-07-02: 109.07260025024414
2026-07-01: 109.30140029907227
2026-06-30: 109.67400024414063
2026-06-29: 110.12760025024414
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 110.56240036010742
2026-06-25: 111.01600036621093
2026-06-24: 111.45180038452149
2026-06-23: 111.91360046386718
2026-06-22: 112.41860031127929
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 112.94480041503907
2026-06-18: 113.42300033569336
2026-06-17: 114.10500015258789
2026-06-16: 114.77540008544922
2026-06-15: 115.42899993896485
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 116.16179992675781
2026-06-11: 116.82719985961914
2026-06-10: 117.49899993896484
2026-06-09: 118.30380004882812
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-06-06 to 2026-07-06:

2026-07-06: 154.40129585266112
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 154.75922588348388
2026-07-02: 155.14273235321045
2026-07-01: 155.55068531036378
2026-06-30: 155.9682247161865
2026-06-29: 156.4204016494751
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 156.85940639495848
2026-06-25: 157.32628540039062
2026-06-24: 157.77437740325928
2026-06-23: 158.2406029510498
2026-06-22: 158.70147426605226
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 159.16595306396485
2026-06-18: 159.5925908279419
2026-06-17: 160.06896800994872
2026-06-16: 160.56106658935548
2026-06-15: 161.06864990234374
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 161.5789060974121
2026-06-11: 162.0939500808716
2026-06-10: 162.6077102661133
2026-06-09: 163.14892127990723
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-06-06 to 2026-07-06:

2026-07-06: 70.22003601822738
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 67.75271670162022
2026-07-02: 62.97372981164552
2026-07-01: 64.32551961705836
2026-06-30: 59.612175808688825
2026-06-29: 60.9511614916746
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 60.28855120783694
2026-06-25: 65.83432038918696
2026-06-24: 62.793439473618406
2026-06-23: 59.03910048914229
2026-06-22: 60.65743824334437
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 67.71602152188072
2026-06-18: 56.44178234606675
2026-06-17: 54.11221355601585
2026-06-16: 53.1380185919021
2026-06-15: 51.8730158325015
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 55.71343635772726
2026-06-11: 55.2786683906319
2026-06-10: 48.038070628622265
2026-06-09: 40.801742970652086
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-06-06 to 2026-07-06:

2026-07-06: 3.9602410839269737
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 3.479664196421325
2026-07-02: 3.062060625706252
2026-07-01: 2.8978891195855425
2026-06-30: 2.5830679122000646
2026-06-29: 2.513270171391497
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 2.3214442425406645
2026-06-25: 2.0957832534826792
2026-06-24: 1.4942192316877794
2026-06-23: 0.9755074279143372
2026-06-22: 0.5996166705130292
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 0.025594779637245324
2026-06-18: -1.0576929700912245
2026-06-17: -1.5859958358685873
2026-06-16: -2.105887824630827
2026-06-15: -2.683846046893578
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: -3.3091839292462026
2026-06-11: -4.2608092200931935
2026-06-10: -5.384944763317208
2026-06-09: -6.305641553044495
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-06-06 to 2026-07-06:

2026-07-06: 3.775928613593286
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 3.739461583869692
2026-07-02: 3.6840356222848487
2026-07-01: 3.792807851455497
2026-06-30: 3.8053311567357255
2026-06-29: 3.878433882058544
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 3.861390451899886
2026-06-25: 3.9076510915667644
2026-06-24: 3.9090089147912512
2026-06-23: 3.819701931711792
2026-06-22: 3.7973712641241173
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 3.6717844148124508
2026-06-18: 3.3203833802772897
2026-06-17: 3.380412800642671
2026-06-16: 3.4815982128916265
2026-06-15: 3.5986442996930834
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 3.6346934856069724
2026-06-11: 3.6627470888793225
2026-06-10: 3.459112437362828
2026-06-09: 3.30519749301634
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


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
<no Reddit posts found mentioning CSL.AX across r/wallstreetbets, r/stocks, r/investing in the past 7 days>
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
No news found for CSL.AX between 2026-06-29 and 2026-07-06
```

### Tool: get_global_news

- Status: `ok`

```text
## Global Market News, from 2026-06-29 to 2026-07-06:

### BIO-key Showcases Passwordless & Biometric Identity Solutions at Jordan Banking Cybersecurity Workshop in Amman on July 6th (source: GlobeNewswire)
Link: https://finance.yahoo.com/technology/ai/articles/bio-key-showcases-passwordless-biometric-080000707.html


```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for CSL.AX
# Data retrieved on: 2026-07-08 19:48:56

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,1036,71079.0,,Purchase at price 68.61 per share.,Hewson (Carolyn Judith),Independent Non-Executive Director,,2026-06-01,D
1,1100,77260.0,,Purchase at price 70.24 per share.,Naylor (Gordon),Director (Non-Executive),,2026-05-26,D
2,2540,179125.0,,Purchase at price 70.52 per share.,Watkins (Alison Mary),Independent Non-Executive Director,,2026-05-15,D
3,214,,,,Watkins (Alison Mary),Independent Non-Executive Director,,2026-02-17,D
4,244,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2026-02-17,D
5,153,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2026-02-17,D
6,433,,,,McNamee (Brian Anthony),Independent Non-Executive Director,,2026-02-17,D
7,183,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2026-02-17,D
8,67797,,,,Naylor (Gordon),Director (Non-Executive),,2025-12-01,D
9,3400,,,,Daniels (Brian M.D.),Non-Independent Executive Director,,2025-11-18,D
10,723,,,,McDonald (Marie Elizabeth),Former,,2025-10-28,D
11,3296,,,,Price (Cameron Bruce),Independent Non-Executive Director,,2025-10-01,D
12,8101,,,,McKenzie (Paul F),Chief Executive Officer,,2025-09-01,D
13,3699,136.0,,Sale at price 0.04 per share.,McKenzie (Paul F),Chief Executive Officer,,2025-09-01,D
14,176,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2025-08-22,D
15,110,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2025-08-22,D
16,88,,,,McDonald (Marie Elizabeth),Independent Non-Executive Director,,2025-08-22,D
17,312,,,,McNamee (Brian Anthony),Independent Non-Executive Chairman,,2025-08-22,D
18,132,,,,Clark (Megan Elizabeth),Independent Non-Executive Director,,2025-08-22,D
19,132,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2025-08-22,D
20,154,,,,Watkins (Alison Mary),Independent Non-Executive Director,,2025-08-22,D
21,2953,,,,Schmeltz (Andy),Other Executive,,2025-06-30,D
22,3056,,,,Linton (Joy),Chief Financial Officer,,2025-06-30,D
23,200,31917.0,,Purchase at price 159.59 per share.,Clark (Megan Elizabeth),Independent Non-Executive Director,,2025-03-17,D
24,132,,,,Clark (Megan Elizabeth),Independent Non-Executive Director,,2025-02-19,D
25,132,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2025-02-19,D
26,176,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2025-02-19,D
27,110,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2025-02-19,D
28,88,,,,McDonald (Marie Elizabeth),Independent Non-Executive Director,,2025-02-19,D
29,313,,,,McNamee (Brian Anthony),Independent Non-Executive Chairman,,2025-02-19,D
30,154,,,,Watkins (Alison Mary),Independent Non-Executive Director,,2025-02-19,D
31,4000,755891.0,,Sale at price 188.97 per share.,McKenzie (Paul F),Chief Executive Officer,,2024-10-31,D
32,3779,204.0,,Sale at price 0.05 per share.,McKenzie (Paul F),Chief Executive Officer,,2024-09-03,D
33,8275,,,,McKenzie (Paul F),Chief Executive Officer,,2024-09-02,D
34,114,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2024-08-16,D
35,338,,,,Maskell (Duncan John Ph.D.),Independent Non-Executive Director,,2024-08-16,D
36,1855,,,,McDonald (Marie Elizabeth),Independent Non-Executive Director,,2024-08-16,D
37,343,,,,McNamee (Brian Anthony),Independent Non-Executive Chairman,,2024-08-16,D
38,169,,,,Watkins (Alison Mary),Independent Non-Executive Director,,2024-08-16,D
39,145,,,,Clark (Megan Elizabeth),Independent Non-Executive Director,,2024-08-16,D
40,145,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2024-08-16,D
41,193,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2024-08-16,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for CSL.AX
# Data retrieved on: 2026-07-08 19:48:56

Name: CSL Limited
Sector: Healthcare
Industry: Biotechnology
Market Cap: 59528757248
PE Ratio (TTM): 13.888268
Forward PE: 13.547594
PEG Ratio: 1.82
Price to Book: 2.2268584
EPS (TTM): 8.95
Forward EPS: 9.175061
Dividend Yield: 3.43
Beta: 0.084
52 Week High: 275.79
52 Week Low: 90.0
50 Day Average: 108.0366
200 Day Average: 154.40425
Revenue (TTM): 15406999552
Gross Profit: 7992000000
EBITDA: 4840000000
Net Income: 1396000000
Profit Margin: 0.09061
Operating Margin: 0.31649
Return on Equity: 0.06662
Return on Assets: 0.06578
Debt to Equity: 54.438
Current Ratio: 2.571
Book Value: 55.81855
Free Cash Flow: 1848125056
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for CSL.AX (quarterly)
# Data retrieved on: 2026-07-08 19:48:57

,2024-12-31
Ordinary Shares Number,484206716.0
Share Issued,484206716.0
Net Debt,10440000000.0
Total Debt,11964000000.0
Tangible Book Value,2277000000.0
Invested Capital,30523000000.0
Working Capital,5234000000.0
Net Tangible Assets,2277000000.0
Common Stock Equity,18559000000.0
Total Capitalization,27885000000.0
Total Equity Gross Minority Interest,20546000000.0
Minority Interest,1987000000.0
Stockholders Equity,18559000000.0
Gains Losses Not Affecting Retained Earnings,652000000.0
Other Equity Adjustments,652000000.0
Retained Earnings,17331000000.0
Capital Stock,576000000.0
Common Stock,576000000.0
Total Liabilities Net Minority Interest,17901000000.0
Total Non Current Liabilities Net Minority Interest,11827000000.0
Other Non Current Liabilities,528000000.0
Employee Benefits,298000000.0
Non Current Pension And Other Postretirement Benefit Plans,298000000.0
Non Current Deferred Liabilities,1520000000.0
Non Current Deferred Taxes Liabilities,1520000000.0
Long Term Debt And Capital Lease Obligation,9326000000.0
Long Term Debt,9326000000.0
Long Term Provisions,155000000.0
Current Liabilities,6074000000.0
Current Deferred Liabilities,205000000.0
Current Deferred Taxes Liabilities,205000000.0
Current Debt And Capital Lease Obligation,2638000000.0
Current Debt,2638000000.0
Other Current Borrowings,2638000000.0
Current Provisions,254000000.0
Payables And Accrued Expenses,2977000000.0
Payables,2977000000.0
Accounts Payable,2977000000.0
Total Assets,38447000000.0
Total Non Current Assets,27139000000.0
Other Non Current Assets,165000000.0
Defined Pension Benefit,45000000.0
Non Current Deferred Assets,868000000.0
Non Current Deferred Taxes Assets,868000000.0
Investments And Advances,178000000.0
Other Investments,178000000.0
Goodwill And Other Intangible Assets,16282000000.0
Other Intangible Assets,16282000000.0
Net PPE,9601000000.0
Gross PPE,9601000000.0
Machinery Furniture Equipment,9601000000.0
Current Assets,11308000000.0
Current Deferred Assets,39000000.0
Current Deferred Taxes Assets,39000000.0
Inventory,6139000000.0
Receivables,3606000000.0
Accounts Receivable,3606000000.0
Cash Cash Equivalents And Short Term Investments,1524000000.0
Cash And Cash Equivalents,1524000000.0
Cash Financial,1524000000.0

```

### Tool: get_cashflow

- Status: `ok`

```text
# Cash Flow data for CSL.AX (quarterly)
# Data retrieved on: 2026-07-08 19:48:57

,2024-12-31
Free Cash Flow,726000000.0
Repayment Of Debt,-216000000.0
Issuance Of Debt,83000000.0
Issuance Of Capital Stock,19000000.0
Capital Expenditure,-533000000.0
Interest Paid Supplemental Data,219000000.0
Income Tax Paid Supplemental Data,311000000.0
End Cash Position,1524000000.0
Beginning Cash Position,1643000000.0
Effect Of Exchange Rate Changes,-50000000.0
Changes In Cash,-69000000.0
Financing Cash Flow,-962000000.0
Cash Flow From Continuing Financing Activities,-962000000.0
Net Other Financing Charges,-45000000.0
Cash Dividends Paid,-803000000.0
Common Stock Dividend Paid,-803000000.0
Net Common Stock Issuance,19000000.0
Common Stock Issuance,19000000.0
Net Issuance Payments Of Debt,-133000000.0
Net Long Term Debt Issuance,-133000000.0
Long Term Debt Payments,-216000000.0
Long Term Debt Issuance,83000000.0
Investing Cash Flow,-366000000.0
Cash Flow From Continuing Investing Activities,-366000000.0
Net Investment Purchase And Sale,-13000000.0
Purchase Of Investment,-13000000.0
Net Business Purchase And Sale,180000000.0
Sale Of Business,180000000.0
Net Intangibles Purchase And Sale,-155000000.0
Purchase Of Intangibles,-155000000.0
Net PPE Purchase And Sale,-378000000.0
Purchase Of PPE,-378000000.0
Cash Flowsfromusedin Operating Activities Direct,1259000000.0
Taxes Refund Paid Direct,-311000000.0
Interest Received Direct,222000000.0
Interest Paid Direct,-219000000.0
Classesof Cash Receiptsfrom Operating Activities,1567000000.0
Other Cash Receiptsfrom Operating Activities,1567000000.0

```

### Tool: get_income_statement

- Status: `ok`

```text
# Income Statement data for CSL.AX (quarterly)
# Data retrieved on: 2026-07-08 19:48:57

,2024-12-31
Tax Effect Of Unusual Items,0.0
Tax Rate For Calcs,0.190551
Normalized EBITDA,3229000000.0
Net Income From Continuing Operation Net Minority Interest,2007000000.0
Reconciled Depreciation,476000000.0
Reconciled Cost Of Revenue,3934000000.0
EBITDA,3229000000.0
EBIT,2753000000.0
Net Interest Income,-222000000.0
Interest Expense,213000000.0
Interest Income,18000000.0
Normalized Income,2007000000.0
Net Income From Continuing And Discontinued Operation,2007000000.0
Diluted Average Shares,485956416.0
Basic Average Shares,483879837.0
Diluted EPS,4.13
Basic EPS,4.15
Net Income Common Stockholders,2007000000.0
Net Income,2007000000.0
Minority Interests,-49000000.0
Net Income Including Noncontrolling Interests,2056000000.0
Net Income Continuous Operations,2056000000.0
Tax Provision,484000000.0
Pretax Income,2540000000.0
Other Income Expense,309000000.0
Other Non Operating Income Expenses,309000000.0
Net Non Operating Interest Income Expense,-222000000.0
Total Other Finance Cost,27000000.0
Interest Expense Non Operating,213000000.0
Interest Income Non Operating,18000000.0
Operating Income,1977000000.0
Operating Expense,2302000000.0
Depreciation Amortization Depletion Income Statement,476000000.0
Depreciation And Amortization In Income Statement,476000000.0
Amortization,209000000.0
Amortization Of Intangibles Income Statement,209000000.0
Depreciation Income Statement,267000000.0
Research And Development,646000000.0
Selling General And Administration,1180000000.0
Selling And Marketing Expense,754000000.0
General And Administrative Expense,426000000.0
Other Gand A,426000000.0
Gross Profit,4279000000.0
Cost Of Revenue,3934000000.0
Total Revenue,8213000000.0
Operating Revenue,8213000000.0

```

## Role: financial_report

- Skill: `tradingagents-financial-report-analyst`

### Tool: collect_financial_document_sources

- Status: `ok`

```text
## Financial Document Source Packet: CSL.AX

- Trade date: `2026-07-06`
- Collection status: `ok`
- Market: `ASX`
- ASX code: `CSL`
- As-of rule: Only ASX announcements with announcement/lodgement date <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/ |
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://www.csl.com/pdf/56bf77f4-8eff-40ff-bb67-c890e3a3476e/CSL-FY25-Results-and-Major-Strategic-Initiatives.pdf |

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: revenue, income, NPAT

```text
Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../94/ Anchor Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 3 ../3/ Anchor Table of Contents ../toc/ Anchor 5 ../5/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 18 ../18/ Anchor Table of Contents ../toc/ Anchor 20 ../20/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 92 ../92/ Anchor Table of Contents ../toc/ Anchor 94 ../94/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 96 ../96/ Anchor Table of Contents ../toc/ Anchor 98 ../98/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 142 ../142/ Anchor Table of Contents ../toc/ Anchor 144 ../144/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 4 ../4/ Anchor Table of Contents ../toc/ Anchor 6 ../6/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ __TABLE_ROW__ page=1 table=1 row=0 title=online_annual_report_table_1 | Cover | 1 __TABLE_ROW__ page=1 table=1 row=1 title=online_annual_report_table_1 | Table of Contents | 3 __TABLE_ROW__ page=1 table=1 row=2 title=online_annual_report_table_1 | Message from the Chair | 6 __TABLE_ROW__ page=1 table=1 row=3 title=online_annual_report_table_1 | Message from the CEO | 8 __TABLE_ROW__ page=1 table=1 row=4 title=online_annual_report_table_1 | Year in Review | 10 __TABLE_ROW__ page=1 table=1 row=5 title=online_annual_report_table_1 | CSL strategy | 12 __TABLE_ROW__ page=1 table=1 row=6 title=online_annual_report_table_1 | CSL'S Sustainability Strategy | 14 __TABLE_ROW__ page=1 table=1 row=7 title=online_annual_report_table_1 | Value Creation | 16 __TABLE_ROW__ page=1 table=1 row=8 title=online_annual_report_table_1 | CSL'S Businesses and Outlook | 18 __TABLE_ROW__ page=1 table=1 row=9 title=online_annual_report_table_1 | Global Manufacturing Presence | 20 __TABLE_ROW__ page=1 table=1 row=10 title=online_annual_report_table_1 | Platforms, Therapeutic Areas and Product Portfolio | 22 __TABLE_ROW__ page=1 table=1 row=11 title=online_annual_report_table_1 | Material Risks | 26 __TABLE_ROW__ page=1 table=1 row=12 title=online_annual_report_table_1 | Healthier World | 28 __TABLE_ROW__ page=1 table=1 row=13 title=online_annual_report_table_1 | Healthier Communities | 29 __TABLE_ROW__ page=1 table=1 row=14 title=online_annual_report_table_1 | Healthier Environment | 37 __TABLE_ROW__ page=1 table=1 row=15 title=online_annual_report_table_1 | Board of Directors | 44 __TABLE_ROW__ page=1 table=1 row=16 title=online_annual_report_table_1 | Leadership Team | 48 __TABLE_ROW__ page=1 table=1 row=17 title=online_annual_report_table_1 | Governance | 52 __TABLE_ROW__ page=1 table=1 row=18 title=online_annual_report_table_1 | Directors' Report | 54 __TABLE_ROW__ page=1 table=1 row=19 title=online_annual_report_table_1 | Auditor's Independence Declaration | 58 __TABLE_ROW__ page=1 table=1 row=20 title=online_annual_report_table_1 | Independent Limited Assurance Report | 59 __TABLE_ROW__ page=1 table=1 row=21 title=online_annual_report_table_1 | Remuneration Report | 63 __TABLE_ROW__ page=1 table=1 row=22 title=online_annual_report_table_1 | Consolidated Statement of Comprehensive Income | 92 __TABLE_ROW__ page=1 table=1 row=23 title=online_annual_report_table_1 | Consolidated Balance Sheet | 92 __TABLE_ROW__ page=1 table=1 row=24 title=online_annual_report_table_1 | Consolidated Statement of Changes in Equity | 94 __TABLE_ROW__ page=1 table=1 row=25 title=online_annual_report_table_1 | Consolidated Statement of Cash Flows | 94 __TABLE_ROW__ page=1 table=1 row=26 title=online_annual_report_table_1 | Notes to the Financial Statements | 96 __TABLE_ROW__ page=1 table=1 row=27 title=online_annual_report_table_1 | Consolidated Entity Disclosure Statement | 132 __TABLE_ROW__ page=1 table=1 row=28 title=online_annual_report_table_1 | Directors' Declaration | 135 __TABLE_ROW__ page=1 table=1 row=29 title=online_annual_report_table_1 | Independent Auditor's Report | 136 __TABLE_ROW__ page=1 table=1 row=30 title=online_annual_report_table_1 | Shareholder Information | 140 __TABLE_ROW__ page=1 table=1 row=31 title=online_annual_report_table_1 | Key Performance Data Summary | 142 __TABLE_ROW__ page=1 table=1 row=32 title=online_annual_report_table_1 | Glossary | 145 __TABLE_ROW__ page=1 table=1 row=33 title=online_annual_report_table_1 | Corporate Directory | 146 Page metadata Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving Page metadata CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: EPS, DPS, dividends

```text
dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our approach to R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the value it has created for shareholders with a decade long commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of
```

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: management discussion, MD&A, outlook

```text
Outlook ../18/ Anchor Global Manufacturing Presence ../20/ Anchor Platforms, Therapeutic Areas and Product Portfolio ../22/ Anchor Material Risks ../26/ Anchor Healthier World ../28/ Anchor Healthier Communities ../29/ Anchor Healthier Environment ../37/ Anchor Board of Directors ../44/ Anchor Leadership Team ../48/ Anchor Governance ../52/ Anchor Directors' Report ../54/ Anchor Auditor's Independence Declaration ../58/ Anchor Independent Limited Assurance Report ../59/ Anchor Remuneration Report ../63/ Anchor Consolidated Statement of Comprehensive Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../94/ Anchor Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 3 ../3/ Anchor Table of Contents ../toc/ Anchor 5 ../5/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 18 ../18/ Anchor Table of Contents ../toc/ Anchor 20 ../20/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 92 ../92/ Anchor Table of Contents ../toc/ Anchor 94 ../94/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 96 ../96/ Anchor Table of Contents ../toc/ Anchor 98 ../98/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 142 ../142/ Anchor Table of Contents ../toc/ Anchor 144 ../144/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 4 ../4/ Anchor Table of Contents ../toc/ Anchor 6 ../6/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ __TABLE_ROW__ page=1 table=1 row=0 title=online_annual_report_table_1 | Cover | 1 __TABLE_ROW__ page=1 table=1 row=1 title=online_annual_report_table_1 | Table of Contents | 3 __TABLE_ROW__ page=1 table=1 row=2 title=online_annual_report_table_1 | Message from the Chair | 6 __TABLE_ROW__ page=1 table=1 row=3 title=online_annual_report_table_1 | Message from the CEO | 8 __TABLE_ROW__ page=1 table=1 row=4 title=online_annual_report_table_1 | Year in Review | 10 __TABLE_ROW__ page=1 table=1 row=5 title=online_annual_report_table_1 | CSL strategy | 12 __TABLE_ROW__ page=1 table=1 row=6 title=online_annual_report_table_1 | CSL'S Sustainability Strategy | 14 __TABLE_ROW__ page=1 table=1 row=7 title=online_annual_report_table_1 | Value Creation | 16 __TABLE_ROW__ page=1 table=1 row=8 title=online_annual_report_table_1 | CSL'S Businesses and Outlook | 18 __TABLE_ROW__ page=1 table=1 row=9 title=online_annual_report_table_1 | Global Manufacturing Presence | 20 __TABLE_ROW__ page=1 table=1 row=10 title=online_annual_report_table_1 | Platforms, Therapeutic Areas and Product Portfolio | 22 __TABLE_ROW__ page=1 table=1 row=11 title=online_annual_report_table_1 | Material Risks | 26 __TABLE_ROW__ page=1 table=1 row=12 title=online_annual_report_table_1 | Healthier World | 28 __TABLE_ROW__ page=1 table=1 row=13 title=online_annual_report_table_1 | Healthier Communities | 29 __TABLE_ROW__ page=1 table=1 row=14 title=online_annual_report_table_1 | Healthier Environment | 37 __TABLE_ROW__ page=1 table=1 row=15 title=online_annual_report_table_1 | Board of Directors | 44 __TABLE_ROW__ page=1 table=1 row=16 title=online_annual_report_table_1 | Leadership Team | 48 __TABLE_ROW__ page=1 table=1 row=17 title=online_annual_report_table_1 | Governance | 52 __TABLE_ROW__ page=1 table=1 row=18 title=online_annual_report_table_1 | Directors' Report | 54 __TABLE_ROW__ page=1 table=1 row=19 title=online_annual_report_table_1 | Auditor's Independence Declaration | 58 __TABLE_ROW__ page=1 table=1 row=20 title=online_annual_report_table_1 | Independent Limited Assurance Report | 59 __TABLE_ROW__ page=1 table=1 row=21 title=online_annual_report_table_1 | Remuneration Report | 63 __TABLE_ROW__ page=1 table=1 row=22 title=online_annual_report_table_1 | Consolidated Statement of Comprehensive Income | 92 __TABLE_ROW__ page=1 table=1 row=23 title=online_annual_report_table_1 | Consolidated Balance Sheet | 92 __TABLE_ROW__ page=1 table=1 row=24 title=online_annual_report_table_1 | Consolidated Statement of Changes in Equity | 94 __TABLE_ROW__ page=1 table=1 row=25 title=online_annual_report_table_1 | Consolidated Statement of Cash Flows | 94 __TABLE_ROW__ page=1 table=1 row=26 title=online_annual_report_table_1 | Notes to the Financial Statements | 96 __TABLE_ROW__ page=1 table=1 row=27 title=online_annual_report_table_1 | Consolidated Entity Disclosure Statement | 132 __TABLE_ROW__ page=1 table=1 row=28 title=online_annual_report_table_1 | Directors' Declaration | 135 __TABLE_ROW__ page=1 table=1 row=29 title=online_annual_report_table_1 | Independent Auditor's Report | 136 __TABLE_ROW__ page=1 table=1 row=30 title=online_annual_report_table_1 | Shareholder Information | 140 __TABLE_ROW__ page=1 table=1 row=31
```

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: cash flow statement, operating cash flow

```text
Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 3 ../3/ Anchor Table of Contents ../toc/ Anchor 5 ../5/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 18 ../18/ Anchor Table of Contents ../toc/ Anchor 20 ../20/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 92 ../92/ Anchor Table of Contents ../toc/ Anchor 94 ../94/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 96 ../96/ Anchor Table of Contents ../toc/ Anchor 98 ../98/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 142 ../142/ Anchor Table of Contents ../toc/ Anchor 144 ../144/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 4 ../4/ Anchor Table of Contents ../toc/ Anchor 6 ../6/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ __TABLE_ROW__ page=1 table=1 row=0 title=online_annual_report_table_1 | Cover | 1 __TABLE_ROW__ page=1 table=1 row=1 title=online_annual_report_table_1 | Table of Contents | 3 __TABLE_ROW__ page=1 table=1 row=2 title=online_annual_report_table_1 | Message from the Chair | 6 __TABLE_ROW__ page=1 table=1 row=3 title=online_annual_report_table_1 | Message from the CEO | 8 __TABLE_ROW__ page=1 table=1 row=4 title=online_annual_report_table_1 | Year in Review | 10 __TABLE_ROW__ page=1 table=1 row=5 title=online_annual_report_table_1 | CSL strategy | 12 __TABLE_ROW__ page=1 table=1 row=6 title=online_annual_report_table_1 | CSL'S Sustainability Strategy | 14 __TABLE_ROW__ page=1 table=1 row=7 title=online_annual_report_table_1 | Value Creation | 16 __TABLE_ROW__ page=1 table=1 row=8 title=online_annual_report_table_1 | CSL'S Businesses and Outlook | 18 __TABLE_ROW__ page=1 table=1 row=9 title=online_annual_report_table_1 | Global Manufacturing Presence | 20 __TABLE_ROW__ page=1 table=1 row=10 title=online_annual_report_table_1 | Platforms, Therapeutic Areas and Product Portfolio | 22 __TABLE_ROW__ page=1 table=1 row=11 title=online_annual_report_table_1 | Material Risks | 26 __TABLE_ROW__ page=1 table=1 row=12 title=online_annual_report_table_1 | Healthier World | 28 __TABLE_ROW__ page=1 table=1 row=13 title=online_annual_report_table_1 | Healthier Communities | 29 __TABLE_ROW__ page=1 table=1 row=14 title=online_annual_report_table_1 | Healthier Environment | 37 __TABLE_ROW__ page=1 table=1 row=15 title=online_annual_report_table_1 | Board of Directors | 44 __TABLE_ROW__ page=1 table=1 row=16 title=online_annual_report_table_1 | Leadership Team | 48 __TABLE_ROW__ page=1 table=1 row=17 title=online_annual_report_table_1 | Governance | 52 __TABLE_ROW__ page=1 table=1 row=18 title=online_annual_report_table_1 | Directors' Report | 54 __TABLE_ROW__ page=1 table=1 row=19 title=online_annual_report_table_1 | Auditor's Independence Declaration | 58 __TABLE_ROW__ page=1 table=1 row=20 title=online_annual_report_table_1 | Independent Limited Assurance Report | 59 __TABLE_ROW__ page=1 table=1 row=21 title=online_annual_report_table_1 | Remuneration Report | 63 __TABLE_ROW__ page=1 table=1 row=22 title=online_annual_report_table_1 | Consolidated Statement of Comprehensive Income | 92 __TABLE_ROW__ page=1 table=1 row=23 title=online_annual_report_table_1 | Consolidated Balance Sheet | 92 __TABLE_ROW__ page=1 table=1 row=24 title=online_annual_report_table_1 | Consolidated Statement of Changes in Equity | 94 __TABLE_ROW__ page=1 table=1 row=25 title=online_annual_report_table_1 | Consolidated Statement of Cash Flows | 94 __TABLE_ROW__ page=1 table=1 row=26 title=online_annual_report_table_1 | Notes to the Financial Statements | 96 __TABLE_ROW__ page=1 table=1 row=27 title=online_annual_report_table_1 | Consolidated Entity Disclosure Statement | 132 __TABLE_ROW__ page=1 table=1 row=28 title=online_annual_report_table_1 | Directors' Declaration | 135 __TABLE_ROW__ page=1 table=1 row=29 title=online_annual_report_table_1 | Independent Auditor's Report | 136 __TABLE_ROW__ page=1 table=1 row=30 title=online_annual_report_table_1 | Shareholder Information | 140 __TABLE_ROW__ page=1 table=1 row=31 title=online_annual_report_table_1 | Key Performance Data Summary | 142 __TABLE_ROW__ page=1 table=1 row=32 title=online_annual_report_table_1 | Glossary | 145 __TABLE_ROW__ page=1 table=1 row=33 title=online_annual_report_table_1 | Corporate Directory | 146 Page metadata Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving Page metadata CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Page metadata CSL Behring exists to meet the needs of patients with rare and serious
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: cash, debt, gearing, capital

```text
Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 3 ../3/ Anchor Table of Contents ../toc/ Anchor 5 ../5/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 18 ../18/ Anchor Table of Contents ../toc/ Anchor 20 ../20/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 92 ../92/ Anchor Table of Contents ../toc/ Anchor 94 ../94/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 96 ../96/ Anchor Table of Contents ../toc/ Anchor 98 ../98/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 142 ../142/ Anchor Table of Contents ../toc/ Anchor 144 ../144/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 4 ../4/ Anchor Table of Contents ../toc/ Anchor 6 ../6/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ __TABLE_ROW__ page=1 table=1 row=0 title=online_annual_report_table_1 | Cover | 1 __TABLE_ROW__ page=1 table=1 row=1 title=online_annual_report_table_1 | Table of Contents | 3 __TABLE_ROW__ page=1 table=1 row=2 title=online_annual_report_table_1 | Message from the Chair | 6 __TABLE_ROW__ page=1 table=1 row=3 title=online_annual_report_table_1 | Message from the CEO | 8 __TABLE_ROW__ page=1 table=1 row=4 title=online_annual_report_table_1 | Year in Review | 10 __TABLE_ROW__ page=1 table=1 row=5 title=online_annual_report_table_1 | CSL strategy | 12 __TABLE_ROW__ page=1 table=1 row=6 title=online_annual_report_table_1 | CSL'S Sustainability Strategy | 14 __TABLE_ROW__ page=1 table=1 row=7 title=online_annual_report_table_1 | Value Creation | 16 __TABLE_ROW__ page=1 table=1 row=8 title=online_annual_report_table_1 | CSL'S Businesses and Outlook | 18 __TABLE_ROW__ page=1 table=1 row=9 title=online_annual_report_table_1 | Global Manufacturing Presence | 20 __TABLE_ROW__ page=1 table=1 row=10 title=online_annual_report_table_1 | Platforms, Therapeutic Areas and Product Portfolio | 22 __TABLE_ROW__ page=1 table=1 row=11 title=online_annual_report_table_1 | Material Risks | 26 __TABLE_ROW__ page=1 table=1 row=12 title=online_annual_report_table_1 | Healthier World | 28 __TABLE_ROW__ page=1 table=1 row=13 title=online_annual_report_table_1 | Healthier Communities | 29 __TABLE_ROW__ page=1 table=1 row=14 title=online_annual_report_table_1 | Healthier Environment | 37 __TABLE_ROW__ page=1 table=1 row=15 title=online_annual_report_table_1 | Board of Directors | 44 __TABLE_ROW__ page=1 table=1 row=16 title=online_annual_report_table_1 | Leadership Team | 48 __TABLE_ROW__ page=1 table=1 row=17 title=online_annual_report_table_1 | Governance | 52 __TABLE_ROW__ page=1 table=1 row=18 title=online_annual_report_table_1 | Directors' Report | 54 __TABLE_ROW__ page=1 table=1 row=19 title=online_annual_report_table_1 | Auditor's Independence Declaration | 58 __TABLE_ROW__ page=1 table=1 row=20 title=online_annual_report_table_1 | Independent Limited Assurance Report | 59 __TABLE_ROW__ page=1 table=1 row=21 title=online_annual_report_table_1 | Remuneration Report | 63 __TABLE_ROW__ page=1 table=1 row=22 title=online_annual_report_table_1 | Consolidated Statement of Comprehensive Income | 92 __TABLE_ROW__ page=1 table=1 row=23 title=online_annual_report_table_1 | Consolidated Balance Sheet | 92 __TABLE_ROW__ page=1 table=1 row=24 title=online_annual_report_table_1 | Consolidated Statement of Changes in Equity | 94 __TABLE_ROW__ page=1 table=1 row=25 title=online_annual_report_table_1 | Consolidated Statement of Cash Flows | 94 __TABLE_ROW__ page=1 table=1 row=26 title=online_annual_report_table_1 | Notes to the Financial Statements | 96 __TABLE_ROW__ page=1 table=1 row=27 title=online_annual_report_table_1 | Consolidated Entity Disclosure Statement | 132 __TABLE_ROW__ page=1 table=1 row=28 title=online_annual_report_table_1 | Directors' Declaration | 135 __TABLE_ROW__ page=1 table=1 row=29 title=online_annual_report_table_1 | Independent Auditor's Report | 136 __TABLE_ROW__ page=1 table=1 row=30 title=online_annual_report_table_1 | Shareholder Information | 140 __TABLE_ROW__ page=1 table=1 row=31 title=online_annual_report_table_1 | Key Performance Data Summary | 142 __TABLE_ROW__ page=1 table=1 row=32 title=online_annual_report_table_1 | Glossary | 145 __TABLE_ROW__ page=1 table=1 row=33 title=online_annual_report_table_1 | Corporate Directory | 146 Page metadata Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving Page metadata CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Page metadata CSL Behring exists to meet the needs of patients with rare and serious diseases, and those
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment performance, sector metrics

```text
Segment Information 96 Note 2: Business Disposals 99 Note Page metadata Shareholder Information CSL’s 20 largest shareholders as at 31 July 2025 Rank Name Units % Units 1 HSBC CUSTODY NOMINEES (AUSTRALIA) LIMITED 166,361,570 34.36 2 Page metadata CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR Page metadata The FY2025 financial year was dynamic for the vaccine market and CSL Seqirus generated positive growth. Over the short term, two current trends will likely Page metadata Consolidated Entity 2025 2024 Notes US$m US$m CURRENT ASSETS Cash and cash equivalents 11 2,157 1,657 Receivables and contract assets 14 3,141 2,895 Inventories Page metadata c. Foreign currency While the presentation currency of the Group is US dollars, entities in the Group may have other functional currencies, reflecting the Page metadata Key Performance Data Summary Performance Summary Performance Indicator Measure 22/23 23/24 24/25 More in 24/25 Annual Report (page reference) Operating revenue Page metadata Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare CSL 2025 Annual Report Table of Contents 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 CSL 2025 Annual Report Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving products to patients in more than 100 countries and employs over 29,000 people. + READ MORE PAGE 18 INNOVATION EXCELLENCE AND INNOVATION CSL is one of the world’s largest collectors of human plasma CSL Plasma operates one of the world’s largest and most sophisticated plasma collection networks, with collection centres in the US and Europe. Plasma collected at CSL Plasma facilities is used by CSL Behring for the purpose of manufacturing and delivering its life-saving therapies to people in more than 100 countries. + READ MORE PAGES 32–33 CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Businesses and Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: outlook, management commentary

```text
Outlook ../18/ Anchor Global Manufacturing Presence ../20/ Anchor Platforms, Therapeutic Areas and Product Portfolio ../22/ Anchor Material Risks ../26/ Anchor Healthier World ../28/ Anchor Healthier Communities ../29/ Anchor Healthier Environment ../37/ Anchor Board of Directors ../44/ Anchor Leadership Team ../48/ Anchor Governance ../52/ Anchor Directors' Report ../54/ Anchor Auditor's Independence Declaration ../58/ Anchor Independent Limited Assurance Report ../59/ Anchor Remuneration Report ../63/ Anchor Consolidated Statement of Comprehensive Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../94/ Anchor Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 3 ../3/ Anchor Table of Contents ../toc/ Anchor 5 ../5/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 18 ../18/ Anchor Table of Contents ../toc/ Anchor 20 ../20/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 92 ../92/ Anchor Table of Contents ../toc/ Anchor 94 ../94/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 96 ../96/ Anchor Table of Contents ../toc/ Anchor 98 ../98/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 142 ../142/ Anchor Table of Contents ../toc/ Anchor 144 ../144/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 4 ../4/ Anchor Table of Contents ../toc/ Anchor 6 ../6/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ __TABLE_ROW__ page=1 table=1 row=0 title=online_annual_report_table_1 | Cover | 1 __TABLE_ROW__ page=1 table=1 row=1 title=online_annual_report_table_1 | Table of Contents | 3 __TABLE_ROW__ page=1 table=1 row=2 title=online_annual_report_table_1 | Message from the Chair | 6 __TABLE_ROW__ page=1 table=1 row=3 title=online_annual_report_table_1 | Message from the CEO | 8 __TABLE_ROW__ page=1 table=1 row=4 title=online_annual_report_table_1 | Year in Review | 10 __TABLE_ROW__ page=1 table=1 row=5 title=online_annual_report_table_1 | CSL strategy | 12 __TABLE_ROW__ page=1 table=1 row=6 title=online_annual_report_table_1 | CSL'S Sustainability Strategy | 14 __TABLE_ROW__ page=1 table=1 row=7 title=online_annual_report_table_1 | Value Creation | 16 __TABLE_ROW__ page=1 table=1 row=8 title=online_annual_report_table_1 | CSL'S Businesses and Outlook | 18 __TABLE_ROW__ page=1 table=1 row=9 title=online_annual_report_table_1 | Global Manufacturing Presence | 20 __TABLE_ROW__ page=1 table=1 row=10 title=online_annual_report_table_1 | Platforms, Therapeutic Areas and Product Portfolio | 22 __TABLE_ROW__ page=1 table=1 row=11 title=online_annual_report_table_1 | Material Risks | 26 __TABLE_ROW__ page=1 table=1 row=12 title=online_annual_report_table_1 | Healthier World | 28 __TABLE_ROW__ page=1 table=1 row=13 title=online_annual_report_table_1 | Healthier Communities | 29 __TABLE_ROW__ page=1 table=1 row=14 title=online_annual_report_table_1 | Healthier Environment | 37 __TABLE_ROW__ page=1 table=1 row=15 title=online_annual_report_table_1 | Board of Directors | 44 __TABLE_ROW__ page=1 table=1 row=16 title=online_annual_report_table_1 | Leadership Team | 48 __TABLE_ROW__ page=1 table=1 row=17 title=online_annual_report_table_1 | Governance | 52 __TABLE_ROW__ page=1 table=1 row=18 title=online_annual_report_table_1 | Directors' Report | 54 __TABLE_ROW__ page=1 table=1 row=19 title=online_annual_report_table_1 | Auditor's Independence Declaration | 58 __TABLE_ROW__ page=1 table=1 row=20 title=online_annual_report_table_1 | Independent Limited Assurance Report | 59 __TABLE_ROW__ page=1 table=1 row=21 title=online_annual_report_table_1 | Remuneration Report | 63 __TABLE_ROW__ page=1 table=1 row=22 title=online_annual_report_table_1 | Consolidated Statement of Comprehensive Income | 92 __TABLE_ROW__ page=1 table=1 row=23 title=online_annual_report_table_1 | Consolidated Balance Sheet | 92 __TABLE_ROW__ page=1 table=1 row=24 title=online_annual_report_table_1 | Consolidated Statement of Changes in Equity | 94 __TABLE_ROW__ page=1 table=1 row=25 title=online_annual_report_table_1 | Consolidated Statement of Cash Flows | 94 __TABLE_ROW__ page=1 table=1 row=26 title=online_annual_report_table_1 | Notes to the Financial Statements | 96 __TABLE_ROW__ page=1 table=1 row=27 title=online_annual_report_table_1 | Consolidated Entity Disclosure Statement | 132 __TABLE_ROW__ page=1 table=1 row=28 title=online_annual_report_table_1 | Directors' Declaration | 135 __TABLE_ROW__ page=1 table=1 row=29 title=online_annual_report_table_1 | Independent Auditor's Report | 136 __TABLE_ROW__ page=1 table=1 row=30 title=online_annual_report_table_1 | Shareholder Information | 140 __TABLE_ROW__ page=1 table=1 row=31
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: dividends, capital management

```text
dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our approach to R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the
```

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: capex, commitments

```text
commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of delivering for patients, communities and shareholders and encourage you to read our Chief Executive Officer’s communication and also that from Dr Megan Clark AC, who chairs our Human Resources and Remuneration Committee. 4 Engagement The Board of Directors has a strong focus on engaging with a broad range of stakeholders both within CSL and externally. To support engagement with these diverse parties the Board always takes time to visit different locations throughout CSL’s global network. In September 2024 the Board visited CSL’s European operations, including manufacturing plants and research and development facilities in Liverpool (UK), Bern (Switzerland) and Marburg (Germany). In June 2025 the Board held its meeting in Amsterdam, Netherlands, where it met with key external stakeholders including health economists, supply chain partners and researchers. We also celebrated the 25th anniversary of our manufacturing facility in Bern. This event underlined how integral CSL’s acquisition of ZLB in 2000 was to our growth and how important the company’s ongoing contribution is to the Swiss economy. I and some of my colleagues spend time each year meeting with our shareholders. These meetings allow us to listen to feedback from our investors, which we value greatly. One topic we know is top of mind for our shareholders is remuneration. Our investors sent a message at the Annual General Meeting in October – and we continue to listen. You can find the details on remuneration on page 61 of this report. We will continue to listen and respond to feedback in relation to our remuneration approach as well as any other issues important to our shareholders. Your Board is confident in the outlook for CSL and for our ability to deliver enduring patient impact in areas of high unmet medical need. Achieving this will allow us to provide sustainable, profitable growth for our shareholders. Once again, on behalf of the Board, I’d like to extend my thanks for your support. “The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done.” Dr Brian McNamee AO Chairman 5 CSL Limited Annual Report 2024/25 CSL Message from the CEO CSL Vifor grew sales, underpinned by our nephrology products and new country launches. Whilst CSL Seqirus was negatively impacted by low influenza immunisation rates, particularly in the United States, this was partially offset by strong demand for avian influenza vaccine for pandemic protection. Throughout this report, you will find detailed information regarding the financial and operating highlights of CSL throughout the financial year. I will also add a few personal reflections of my own. Refocused strategy Having been Chief Executive Officer for two years, I’ve had time to work with my management team to laser focus our priorities and develop our ambition to deliver enduring patient impact in areas of high unmet medical need and to provide durable returns to our shareholders. CSL has a strong track record of sustainable, profitable growth. However, our operating environment has grown increasingly complex with a dynamic geopolitical backdrop and competitive pressures. We need to accelerate our innovation with our current commercial and clinical portfolio to ensure we’re successful through the next decade and our structure is fit for purpose. After many years of significant growth, it is important we stay committed to a winning formula that can deliver for years to come. I believe a simple and focused CSL is best for patients, our people and our shareholders and we have outlined plans to evolve our strategy to re-focus on what makes us unique: Patients: who need durable, effective treatments for, and protection from, serious diseases. Diseases: where we have a fundamental advantage in understanding the disease and science. Medicines: with a high degree of specialist expertise or manufacturing differentiation. My Priorities To achieve this, I’ve laid out three key priorities for the 2026 financial year and I’m pleased to report we are making good progress on them all. The first priority is to drive growth through the
```

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: risks

```text
risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of delivering for patients, communities and shareholders and encourage you to read our Chief Executive Officer’s communication and also that from Dr Megan Clark AC, who chairs our Human Resources and Remuneration Committee. 4 Engagement The Board of Directors has a strong focus on engaging with a broad range of stakeholders both within CSL and externally. To support engagement with these diverse parties the Board always takes time to visit different locations throughout CSL’s global network. In September 2024 the Board visited CSL’s European operations, including manufacturing plants and research and development facilities in Liverpool (UK), Bern (Switzerland) and Marburg (Germany). In June 2025 the Board held its meeting in Amsterdam, Netherlands, where it met with key external stakeholders including health economists, supply chain partners and researchers. We also celebrated the 25th anniversary of our manufacturing facility in Bern. This event underlined how integral CSL’s acquisition of ZLB in 2000 was to our growth and how important the company’s ongoing contribution is to the Swiss economy. I and some of my colleagues spend time each year meeting with our shareholders. These meetings allow us to listen to feedback from our investors, which we value greatly. One topic we know is top of mind for our shareholders is remuneration. Our investors sent a message at the Annual General Meeting in October – and we continue to listen. You can find the details on remuneration on page 61 of this report. We will continue to listen and respond to feedback in relation to our remuneration approach as well as any other issues important to our shareholders. Your Board is confident in the outlook for CSL and for our ability to deliver enduring patient impact in areas of high unmet medical need. Achieving this will allow us to provide sustainable, profitable growth for our shareholders. Once again, on behalf of the Board, I’d like to extend my thanks for your support. “The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done.” Dr Brian McNamee AO Chairman 5 CSL Limited Annual Report 2024/25 CSL Message from the CEO CSL Vifor grew sales, underpinned by our nephrology products and new country launches. Whilst CSL Seqirus was negatively impacted by low influenza immunisation rates, particularly in the United States, this was partially offset by strong demand for avian influenza vaccine for pandemic protection. Throughout this report, you will find detailed information regarding the financial and operating highlights of CSL throughout the financial year. I will also add a few personal reflections of my own. Refocused strategy Having been Chief Executive Officer for two years, I’ve had time to work with my management team to laser focus our priorities and develop our ambition to deliver enduring patient impact in areas of high unmet medical need and to provide durable returns to our shareholders. CSL has a strong track record of sustainable, profitable growth. However, our operating environment has grown increasingly complex with a dynamic geopolitical backdrop and competitive pressures. We need to accelerate our innovation with our current commercial and clinical portfolio to ensure we’re successful through the next decade and our structure is fit for purpose. After many years of significant growth, it is important we stay committed to a winning formula that can deliver for years to come. I believe a simple and focused CSL is best for patients, our people and our shareholders and we have outlined plans to evolve our strategy to re-focus on what makes us unique: Patients: who need durable, effective treatments for, and protection from, serious diseases. Diseases: where we have a fundamental advantage in understanding the disease and science. Medicines: with a high degree of specialist expertise or manufacturing differentiation. My Priorities To achieve this, I’ve laid out three key priorities for the 2026 financial year and I’m pleased to report we are making good progress on them all. The first priority is to drive growth through the evolution of our portfolio development and commercialisation process. We will build an optimal portfolio of new therapies in our pipeline through an integrated approach. This will include closer collaboration between our R&D, business development and commercialisation teams. We will focus on areas where we are uniquely positioned to outperform our competitors and decide where we support our internal capabilities and where we seek to complete our portfolio through external partnerships. We can’t do everything on our own, in some areas we’re going to need partners. This will require changes in how we conduct R&D as we simplify our operating model, reduce duplication, improve efficiencies and consolidate our footprint around key global biotech hubs. We also announced plans to combine the commercial and medical functions of the Behring and Vifor businesses. We will continue to develop and deliver initiatives in our existing businesses like Ig and albumin yield enhancements and launch new products like Hemgenix, Andembry and Filspari. We will also continue to defend and grow Ig and iron volumes and CSL Seqirus will continue to expand geographic and customers segments in influenza. During the year there was no
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
ASSETS Cash and cash equivalents 11 2,157 1,657 Receivables and contract assets 14 3,141 2,895 Inventories Page metadata c. Foreign currency While the presentation currency of the Group is US dollars, entities in the Group may have other functional currencies, reflecting the Page metadata Key Performance Data Summary Performance Summary Performance Indicator Measure 22/23 23/24 24/25 More in 24/25 Annual Report (page reference) Operating revenue Page metadata Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare CSL 2025 Annual Report Table of Contents 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 CSL 2025 Annual Report Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving products to patients in more than 100 countries and employs over 29,000 people. + READ MORE PAGE 18 INNOVATION EXCELLENCE AND INNOVATION CSL is one of the world’s largest collectors of human plasma CSL Plasma operates one of the world’s largest and most sophisticated plasma collection networks, with collection centres in the US and Europe. Plasma collected at CSL Plasma facilities is used by CSL Behring for the purpose of manufacturing and delivering its life-saving therapies to people in more than 100 countries. + READ MORE PAGES 32–33 CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Businesses and Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment table, product table, sector metrics

```text
Product Portfolio ../22/ Anchor Material Risks ../26/ Anchor Healthier World ../28/ Anchor Healthier Communities ../29/ Anchor Healthier Environment ../37/ Anchor Board of Directors ../44/ Anchor Leadership Team ../48/ Anchor Governance ../52/ Anchor Directors' Report ../54/ Anchor Auditor's Independence Declaration ../58/ Anchor Independent Limited Assurance Report ../59/ Anchor Remuneration Report ../63/ Anchor Consolidated Statement of Comprehensive Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../94/ Anchor Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 3 ../3/ Anchor Table of Contents ../toc/ Anchor 5 ../5/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 18 ../18/ Anchor Table of Contents ../toc/ Anchor 20 ../20/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 92 ../92/ Anchor Table of Contents ../toc/ Anchor 94 ../94/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 96 ../96/ Anchor Table of Contents ../toc/ Anchor 98 ../98/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 142 ../142/ Anchor Table of Contents ../toc/ Anchor 144 ../144/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 4 ../4/ Anchor Table of Contents ../toc/ Anchor 6 ../6/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ __TABLE_ROW__ page=1 table=1 row=0 title=online_annual_report_table_1 | Cover | 1 __TABLE_ROW__ page=1 table=1 row=1 title=online_annual_report_table_1 | Table of Contents | 3 __TABLE_ROW__ page=1 table=1 row=2 title=online_annual_report_table_1 | Message from the Chair | 6 __TABLE_ROW__ page=1 table=1 row=3 title=online_annual_report_table_1 | Message from the CEO | 8 __TABLE_ROW__ page=1 table=1 row=4 title=online_annual_report_table_1 | Year in Review | 10 __TABLE_ROW__ page=1 table=1 row=5 title=online_annual_report_table_1 | CSL strategy | 12 __TABLE_ROW__ page=1 table=1 row=6 title=online_annual_report_table_1 | CSL'S Sustainability Strategy | 14 __TABLE_ROW__ page=1 table=1 row=7 title=online_annual_report_table_1 | Value Creation | 16 __TABLE_ROW__ page=1 table=1 row=8 title=online_annual_report_table_1 | CSL'S Businesses and Outlook | 18 __TABLE_ROW__ page=1 table=1 row=9 title=online_annual_report_table_1 | Global Manufacturing Presence | 20 __TABLE_ROW__ page=1 table=1 row=10 title=online_annual_report_table_1 | Platforms, Therapeutic Areas and Product Portfolio | 22 __TABLE_ROW__ page=1 table=1 row=11 title=online_annual_report_table_1 | Material Risks | 26 __TABLE_ROW__ page=1 table=1 row=12 title=online_annual_report_table_1 | Healthier World | 28 __TABLE_ROW__ page=1 table=1 row=13 title=online_annual_report_table_1 | Healthier Communities | 29 __TABLE_ROW__ page=1 table=1 row=14 title=online_annual_report_table_1 | Healthier Environment | 37 __TABLE_ROW__ page=1 table=1 row=15 title=online_annual_report_table_1 | Board of Directors | 44 __TABLE_ROW__ page=1 table=1 row=16 title=online_annual_report_table_1 | Leadership Team | 48 __TABLE_ROW__ page=1 table=1 row=17 title=online_annual_report_table_1 | Governance | 52 __TABLE_ROW__ page=1 table=1 row=18 title=online_annual_report_table_1 | Directors' Report | 54 __TABLE_ROW__ page=1 table=1 row=19 title=online_annual_report_table_1 | Auditor's Independence Declaration | 58 __TABLE_ROW__ page=1 table=1 row=20 title=online_annual_report_table_1 | Independent Limited Assurance Report | 59 __TABLE_ROW__ page=1 table=1 row=21 title=online_annual_report_table_1 | Remuneration Report | 63 __TABLE_ROW__ page=1 table=1 row=22 title=online_annual_report_table_1 | Consolidated Statement of Comprehensive Income | 92 __TABLE_ROW__ page=1 table=1 row=23 title=online_annual_report_table_1 | Consolidated Balance Sheet | 92 __TABLE_ROW__ page=1 table=1 row=24 title=online_annual_report_table_1 | Consolidated Statement of Changes in Equity | 94 __TABLE_ROW__ page=1 table=1 row=25 title=online_annual_report_table_1 | Consolidated Statement of Cash Flows | 94 __TABLE_ROW__ page=1 table=1 row=26 title=online_annual_report_table_1 | Notes to the Financial Statements | 96 __TABLE_ROW__ page=1 table=1 row=27 title=online_annual_report_table_1 | Consolidated Entity Disclosure Statement | 132 __TABLE_ROW__ page=1 table=1 row=28 title=online_annual_report_table_1 | Directors' Declaration | 135 __TABLE_ROW__ page=1 table=1 row=29 title=online_annual_report_table_1 | Independent Auditor's Report | 136 __TABLE_ROW__ page=1 table=1 row=30 title=online_annual_report_table_1 | Shareholder Information | 140 __TABLE_ROW__ page=1 table=1 row=31 title=online_annual_report_table_1 | Key Performance Data Summary | 142 __TABLE_ROW__ page=1 table=1 row=32
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment revenue

```text
US$11,158m CSL Behring revenue US$2,166m CSL Seqirus revenue US$2,234m CSL Vifor revenue Cashflow from operations was $3,561 million, up
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: R&D

```text
R&D investment US$ million 1,266†^ 1,428¶^ 1,359¶^ 106 Clinical trials in operation Number 60 60 59 30 Safety and quality Regulatory audits of manufacturing facilities and plasma collection centres Number 475†^ 479#^ 403#^ 33 Safety related recalls of
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: plasma collections

```text
+ READ MORE PAGE 18 INNOVATION EXCELLENCE AND INNOVATION CSL is one of the world’s largest collectors of human plasma CSL Plasma operates one of the world’s largest and most sophisticated plasma collection networks, with collection centres
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: margins

```text
+ READ MORE ABOUT CSL’S R&D PIPELINE AT WWW.CSL.COM/RESEARCH-ANDDEVELOPMENT/PRODUCT-PIPELINE NPATA attributable to equity holders of US$3.2 billion for the year ended 30 June 2025, up 11% on a reported currency basis when compared to the
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: debt, liquidity

```text
assets 11 203 163 Other non-current assets 14 189 158 Total Non-Current Assets 27,554 27,254 TOTAL ASSETS 39,404 38,022 CURRENT LIABILITIES Trade and other payables 14 3,461 3,345 Interest-bearing liabilities and borrowings 11 804 944 Current tax liabilities 280 176 Provisions 15 270 475 Liabilities held for sale 2 — 10 Total Current Liabilities 4,815 4,950 NON-CURRENT LIABILITIES Interest-bearing liabilities and borrowings 11 10,694 11,239 Retirement benefit liabilities 17 308 282 Deferred tax liabilities 4 1,510 1,514 Provisions 15 155 186 Other non-current liabilities 14 515 450 Total
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: guidance, outlook

```text
While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/

```text
Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/toc/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/3/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/18/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/92/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/96/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/142/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/4/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/19/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/93/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/97/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/143/ Section CSL 2025 Annual Report Section Linked report page https://investors.csl.com/annualreport/2025/5/ Section CSL 2025 Annual Report Anchor Table of Contents ./toc/ Anchor 2 ./2/ Anchor 3 ./3/ Anchor 4 ./4/ Anchor 5 ./5/ Anchor 6 ./6/ Anchor 7 ./7/ Anchor 8 ./8/ Anchor 9 ./9/ Anchor 10 ./10/ Anchor 11 ./11/ Anchor 12 ./12/ Anchor 13 ./13/ Anchor 14 ./14/ Anchor 15 ./15/ Anchor 16 ./16/ Anchor 17 ./17/ Anchor 18 ./18/ Anchor 19 ./19/ Anchor 20 ./20/ Anchor 21 ./21/ Anchor 22 ./22/ Anchor 23 ./23/ Anchor 24 ./24/ Anchor 25 ./25/ Anchor 26 ./26/ Anchor 27 ./27/ Anchor 28 ./28/ Anchor 29 ./29/ Anchor 30 ./30/ Anchor 31 ./31/ Anchor 32 ./32/ Anchor 33 ./33/ Anchor 34 ./34/ Anchor 35 ./35/ Anchor 36 ./36/ Anchor 37 ./37/ Anchor 38 ./38/ Anchor 39 ./39/ Anchor 40 ./40/ Anchor 41 ./41/ Anchor 42 ./42/ Anchor 43 ./43/ Anchor 44 ./44/ Anchor 45 ./45/ Anchor 46 ./46/ Anchor 47 ./47/ Anchor 48 ./48/ Anchor 49 ./49/ Anchor 50 ./50/ Anchor 51 ./51/ Anchor 52 ./52/ Anchor 53 ./53/ Anchor 54 ./54/ Anchor 55 ./55/ Anchor 56 ./56/ Anchor 57 ./57/ Anchor 58 ./58/ Anchor 59 ./59/ Anchor 60 ./60/ Anchor 61 ./61/ Anchor 62 ./62/ Anchor 63 ./63/ Anchor 64 ./64/ Anchor 65 ./65/ Anchor 66 ./66/ Anchor 67 ./67/ Anchor 68 ./68/ Anchor 69 ./69/ Anchor 70 ./70/ Anchor 71 ./71/ Anchor 72 ./72/ Anchor 73 ./73/ Anchor 74 ./74/ Anchor 75 ./75/ Anchor 76 ./76/ Anchor 77 ./77/ Anchor 78 ./78/ Anchor 79 ./79/ Anchor 80 ./80/ Anchor 81 ./81/ Anchor 82 ./82/ Anchor 83 ./83/ Anchor 84 ./84/ Anchor 85 ./85/ Anchor 86 ./86/ Anchor 87 ./87/ Anchor 88 ./88/ Anchor 89 ./89/ Anchor 90 ./90/ Anchor 91 ./91/ Anchor 92 ./92/ Anchor 93 ./93/ Anchor 94 ./94/ Anchor 95 ./95/ Anchor 96 ./96/ Anchor 97 ./97/ Anchor 98 ./98/ Anchor 99 ./99/ Anchor 100 ./100/ Anchor 101 ./101/ Anchor 102 ./102/ Anchor 103 ./103/ Anchor 104 ./104/ Anchor 105 ./105/ Anchor 106 ./106/ Anchor 107 ./107/ Anchor 108 ./108/ Anchor 109 ./109/ Anchor 110 ./110/ Anchor 111 ./111/ Anchor 112 ./112/ Anchor 113 ./113/ Anchor 114 ./114/ Anchor 115 ./115/ Anchor 116 ./116/ Anchor 117 ./117/ Anchor 118 ./118/ Anchor 119 ./119/ Anchor 120 ./120/ Anchor 121 ./121/ Anchor 122 ./122/ Anchor 123 ./123/ Anchor 124 ./124/ Anchor 125 ./125/ Anchor 126 ./126/ Anchor 127 ./127/ Anchor 128 ./128/ Anchor 129 ./129/ Anchor 130 ./130/ Anchor 131 ./131/ Anchor 132 ./132/ Anchor 133 ./133/ Anchor 134 ./134/ Anchor 135 ./135/ Anchor 136 ./136/ Anchor 137 ./137/ Anchor 138 ./138/ Anchor 139 ./139/ Anchor 140 ./140/ Anchor 141 ./141/ Anchor 142 ./142/ Anchor 143 ./143/ Anchor 144 ./144/ Anchor 145 ./145/ Anchor 146 ./146/ Anchor 147 ./147/ Anchor 148 ./148/ Anchor Made with FlippingBook ./files/publication/ Anchor 1 ../ Anchor 148 ../148/ Anchor Cover ../ Anchor Table of Contents ../3/ Anchor Message from the Chair ../6/ Anchor Message from the CEO ../8/ Anchor Year in Review ../10/ Anchor CSL strategy ../12/ Anchor CSL'S Sustainability Strategy ../14/ Anchor Value Creation ../16/ Anchor CSL'S Businesses and Outlook ../18/ Anchor Global Manufacturing Presence ../20/ Anchor Platforms, Therapeutic Areas and Product Portfolio ../22/ Anchor Material Risks ../26/ Anchor Healthier World ../28/ Anchor Healthier Communities ../29/ Anchor Healthier Environment ../37/ Anchor Board of Directors ../44/ Anchor Leadership Team ../48/ Anchor Governance ../52/ Anchor Directors' Report ../54/ Anchor Auditor's Independence Declaration ../58/ Anchor Independent Limited Assurance Report ../59/ Anchor Remuneration Report ../63/ Anchor Consolidated Statement of Comprehensive Income ../92/ Anchor Consolidated Balance Sheet ../92/ Anchor Consolidated Statement of Changes in Equity ../94/ Anchor Consolidated Statement of Cash Flows ../94/ Anchor Notes to the Financial Statements ../96/ Anchor Consolidated Entity Disclosure Statement ../132/ Anchor Directors' Declaration ../135/ Anchor Independent Auditor's Report ../136/ Anchor Shareholder Information ../140/ Anchor Key Performance Data Summary ../142/ Anchor Glossary ../145/ Anchor Corporate Directory ../146/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 2 ../2/ Anchor Table of Contents ../toc/ Anchor 4 ../4/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 17 ../17/ Anchor Table of Contents ../toc/ Anchor 19 ../19/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 91 ../91/ Anchor Table of Contents ../toc/ Anchor 93 ../93/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 95 ../95/ Anchor Table of Contents ../toc/ Anchor 97 ../97/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../ Anchor 141 ../141/ Anchor Table of Contents ../toc/ Anchor 143 ../143/ Anchor 148 ../148/ Anchor Made with FlippingBook ../files/publication/ Anchor 1 ../
```

```
