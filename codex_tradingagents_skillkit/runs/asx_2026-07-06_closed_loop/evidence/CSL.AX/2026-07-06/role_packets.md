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
# Data retrieved on: 2026-07-06 22:14:37

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
2026-07-06,121.85,125.0,120.75,124.23,1356014,0.0,0.0

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
| Volume | 1356014 |

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
2026-06-17: 160.0689679336548
2026-06-16: 160.56106651306152
2026-06-15: 161.0686498260498
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 161.5789059448242
2026-06-11: 162.09394992828368
2026-06-10: 162.6077101135254
2026-06-09: 163.14892105102538
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-06-06 to 2026-07-06:

2026-07-06: 70.22003601823093
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 67.75271670162375
2026-07-02: 62.97372981164885
2026-07-01: 64.32551961706197
2026-06-30: 59.6121758086921
2026-06-29: 60.951161491678185
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 60.28855120784047
2026-06-25: 65.8343203891919
2026-06-24: 62.793439473623145
2026-06-23: 59.03910048914662
2026-06-22: 60.657438243349226
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 67.71602152188804
2026-06-18: 56.4417823460725
2026-06-17: 54.11221355602102
2026-06-16: 53.138018591906985
2026-06-15: 51.873015832506006
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 55.71343635773377
2026-06-11: 55.278668390638295
2026-06-10: 48.038070628625995
2026-06-09: 40.80174297065214
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-06-06 to 2026-07-06:

2026-07-06: 3.9602410839273574
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 3.479664196421737
2026-07-02: 3.0620606257066925
2026-07-01: 2.8978891195860115
2026-06-30: 2.583067912200576
2026-06-29: 2.513270171392051
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 2.3214442425412614
2026-06-25: 2.0957832534833187
2026-06-24: 1.4942192316884615
2026-06-23: 0.9755074279150762
2026-06-22: 0.5996166705138393
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 0.025594779638112186
2026-06-18: -1.0576929700902724
2026-06-17: -1.5859958358675783
2026-06-16: -2.1058878246297468
2026-06-15: -2.6838460468924126
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: -3.309183929244938
2026-06-11: -4.260809220091829
2026-06-10: -5.384944763315744
2026-06-09: -6.305641553042918
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-06-06 to 2026-07-06:

2026-07-06: 3.7759286135931798
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 3.739461583869578
2026-07-02: 3.6840356222847257
2026-07-01: 3.7928078514553647
2026-06-30: 3.805331156735583
2026-06-29: 3.87843388205839
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 3.861390451899721
2026-06-25: 3.9076510915665867
2026-06-24: 3.90900891479106
2026-06-23: 3.819701931711586
2026-06-22: 3.7973712641238957
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 3.671784414812212
2026-06-18: 3.320383380277032
2026-06-17: 3.3804128006423944
2026-06-16: 3.4815982128913285
2026-06-15: 3.598644299692763
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 3.634693485606627
2026-06-11: 3.6627470888789504
2026-06-10: 3.4591124373624274
2026-06-09: 3.3051974930159087
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
No global news found between 2026-06-29 and 2026-07-06
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for CSL.AX
# Data retrieved on: 2026-07-06 22:14:51

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,1036,71079.0,,Purchase at price 68.61 per share.,Hewson (Carolyn Judith),Independent Non-Executive Director,,2026-06-01,D
1,1100,77260.0,,Purchase at price 70.24 per share.,Naylor (Gordon),Director (Non-Executive),,2026-05-26,D
2,2540,179125.0,,Purchase at price 70.52 per share.,Watkins (Alison Mary),Independent Non-Executive Director,,2026-05-15,D
3,433,,,,McNamee (Brian Anthony),Independent Non-Executive Director,,2026-02-17,D
4,214,,,,Watkins (Alison Mary),Independent Non-Executive Director,,2026-02-17,D
5,183,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2026-02-17,D
6,244,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2026-02-17,D
7,153,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2026-02-17,D
8,67797,,,,Naylor (Gordon),Director (Non-Executive),,2025-12-01,D
9,3400,,,,Daniels (Brian M.D.),Non-Independent Executive Director,,2025-11-18,D
10,723,,,,McDonald (Marie Elizabeth),Former,,2025-10-28,D
11,3296,,,,Price (Cameron Bruce),Independent Non-Executive Director,,2025-10-01,D
12,8101,,,,McKenzie (Paul F),Chief Executive Officer,,2025-09-01,D
13,3699,136.0,,Sale at price 0.04 per share.,McKenzie (Paul F),Chief Executive Officer,,2025-09-01,D
14,132,,,,Clark (Megan Elizabeth),Independent Non-Executive Director,,2025-08-22,D
15,132,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2025-08-22,D
16,176,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2025-08-22,D
17,110,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2025-08-22,D
18,88,,,,McDonald (Marie Elizabeth),Independent Non-Executive Director,,2025-08-22,D
19,312,,,,McNamee (Brian Anthony),Independent Non-Executive Chairman,,2025-08-22,D
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
34,145,,,,Clark (Megan Elizabeth),Independent Non-Executive Director,,2024-08-16,D
35,145,,,,Cuthbertson (Robert Andrew),Independent Non-Executive Director,,2024-08-16,D
36,193,,,,Hewson (Carolyn Judith),Independent Non-Executive Director,,2024-08-16,D
37,114,,,,Lewis (Samantha Louise),Independent Non-Executive Director,,2024-08-16,D
38,338,,,,Maskell (Duncan John Ph.D.),Independent Non-Executive Director,,2024-08-16,D
39,1855,,,,McDonald (Marie Elizabeth),Independent Non-Executive Director,,2024-08-16,D
40,343,,,,McNamee (Brian Anthony),Independent Non-Executive Chairman,,2024-08-16,D
41,169,,,,Watkins (Alison Mary),Independent Non-Executive Director,,2024-08-16,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for CSL.AX
# Data retrieved on: 2026-07-06 22:14:51

Name: CSL Limited
Sector: Healthcare
Industry: Biotechnology
Market Cap: 59495235584
PE Ratio (TTM): 13.864956
Forward PE: 13.511346
PEG Ratio: 1.82
Price to Book: 2.2278514
EPS (TTM): 8.96
Forward EPS: 9.194495
Dividend Yield: 3.43
Beta: 0.084
52 Week High: 275.79
52 Week Low: 90.0
50 Day Average: 108.1352
200 Day Average: 154.75555
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
Book Value: 55.76225
Free Cash Flow: 1848125056
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for CSL.AX (quarterly)
# Data retrieved on: 2026-07-06 22:14:53

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
# Data retrieved on: 2026-07-06 22:14:53

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
# Data retrieved on: 2026-07-06 22:14:53

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
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://www.csl.com/pdf/56bf77f4-8eff-40ff-bb67-c890e3a3476e/CSL-FY25-Results-and-Major-Strategic-Initiatives.pdf |
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/ |
| asx_fallback_document | available | 2025-12-31 | Cash Flow Statement | https://investors.csl.com/annualreport/2025/95/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/99/ |

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: revenue, income, NPAT

```text
revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our approach to R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the value it has created for shareholders with a decade long commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf
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
Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming
```

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

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
Cash, equity and debt for future growth 14 Performance WHAT CSL DOES THE VALUE CSL CREATES Provide a safe, rewarding and productive workplace for promising futures Powered by research and development to identify new indications for CSL’s existing products, and innovative new products for patients and public health Collaborative partnerships Partnering to expand CSL’s global impact and reach Driven by safety, quality, reliability, and innovation in CSL’s operations, while embedding environmental and social considerations into work practices and responsibly sourcing materials and inputs Seek to provide sustainable financial growth with a focus on revenue and margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 CSL Behring exists to meet the needs of patients with rare and serious diseases, and those suffering from trauma-related bleeding. Plasma-derived therapies (PDTs) form the core of the portfolio. Patients are the core focus. CSL Behring consists of three vertically integrated components that span the journey from donor to patient. In plasma collection the focus is on three areas; enhancing collection efficiency, reducing the unit acquisition cost and providing a world-class experience for donors and communities. CSL Behring’s manufacturing capability is focused on: • fractionating and transforming plasma into a portfolio of innovative PDTs, and • delivering supply of CSL’s recombinant medicines. CSL Behring’s commercial and medical teams around the world are engaged with healthcare providers, payers and key stakeholders, working to meet patient needs and to deliver successful launches of CSL’s life-saving therapies. This helps provide access to more people with rare and serious diseases. One of CSL Behring’s key priorities is sourcing sufficient and sustainable volumes of plasma to meet the growing need for CSL’s medicines. PDTs have a 9–12 month manufacturing cycle, which is more complex than other pharmaceutical products. These products are vital for patients in need, and can transform their lives. CSL Behring commits to reducing the cost per litre of plasma. The aim to increase yield for immunoglobulins (Ig) and albumin through data analytics, smarter plasma allocation and implementing an operational excellence program. In plasma collection, the Rika collection device and individualised nomogram, iNomi™, enables CSL to collect the optimal amount of plasma from donors. These avenues to yield improvement through technology and innovation are critical to CSL’s ability to increase the supply of therapies to patients. There is significant opportunity for continued global immunoglobulin (lg) growth as the market expands. Within this growing market, PRIVIGEN® and HIZENTRA® are expected to gain share. CSL Behring plays a leading role in Ig and will continue to identify expansion opportunities. CSL expects the global haemophilia B market to grow in coming years due to the steady prevalence of the disease and the launch of novel treatments, including gene therapies. As this market grows, CSL Behring will look to expand its portfolio. The hereditary angioedema (HAE) market may also grow due to improved diagnosis rates and new prophylaxis therapies. ANDEMBRY® (garadacimab), CSL’s next generation HAE therapy, is now approved in US, European Union (EU), United Kingdom (UK), Japan, Switzerland, Australia and the United Arab Emirates. It is available in US, Japan, Germany and Greece. CSL Behring has built on its leadership position and continues to innovate across rare and serious diseases. + READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$11,158m CSL Behring revenue 16 Performance The FY2025 financial year was dynamic for the vaccine market and CSL Seqirus generated positive growth. Over the short term, two current trends will likely continue. First, the exciting acceleration of new vaccine technologies. CSL Seqirus is well positioned with its technology platforms (cell-based, adjuvants, and sa‑mRNA). The second trend is reduced rates of immunisation following the pandemic, particularly in the United States. However, the European vaccination market is stabilising. Against this backdrop, CSL Seqirus maintained commercial discipline in a competitive market. The business expects to continue to drive growth through life cycle management, which will allow CSL to deliver ongoing value to public health systems. Seasonal influenza remains one of the most consequential vaccine preventable diseases due to its significant morbidity and mortality, with unmet need across all populations, and with particular risk to the very young, due to
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment performance, sector metrics

```text
segment. This growth is driven by demographic trends such as an aging population, the increasing prevalence of CKD risk factors – including diabetes, hypertension, and cardiovascular disease – and the rising demand for innovative treatment options. Looking ahead, CSL continues to launch excellence in nephrology and to expand its position in the renal disease market. Strategic partnerships have remained a cornerstone of CSL Vifor’s growth model throughout fiscal year 2025. Internal and external collaborations continue to play a pivotal role in advancing CSL’s objectives. Joint efforts with CSL Behring have unlocked new opportunities, including the launch of FERINJECT® in Canada and the introduction of new vial sizes for ZEMAIRA® in the United States. Similarly collaboration with CSL Seqirus in Europe has leveraged CSL’s global capabilities while adapting to local market needs delivering meaningful value to patients and contributing to enterprise-wide sustainable growth. + READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$2,234m CSL Vifor revenue 18 Performance 19 CSL Limited Annual Report 2024/25 Global Manufacturing Presence St. Gallen, Switzerland Across the three businesses, CSL operates the following highly advanced manufacturing facilities. Holly Springs NC, US Liverpool, UK Parkville, Australia Tullamarine, Australia Broadmeadows, Australia Bern, Switzerland Kankakee IL, US Marburg, Germany Platforms, Therapeutic Areas and Product Portfolio CSL research and development leverages its expertise in four strategic platforms – plasma protein technology; recombinant protein technology; cell and genetic medicines; and vaccines technology. PLATFORMS Plasma Protein Technology Recombinant Protein Technology Genetic Medicine Vaccines Technology THERAPEUTIC AREAS These platforms underpin CSL’s five therapeutic areas: 20 Performance Immunoglobulins Building on CSL’s long heritage of providing patients with immunoglobulin products, CSL continues to optimise the patient experience by developing more convenient and flexible ways to dose and administer immunoglobulin products. CSL’s focus is on serving patients with serious immunologic and neurologic diseases, including primary and secondary immunodeficiencies (PID/SID) and chronic inflammatory demyelinating polyneuropathy (CIDP). CSL’s commitment to innovation is reflected in its exploration of inhaled immunoglobulin as a potential treatment for patients with bronchiectasis, complementing the established ZEMAIRA®/RESPREEZA® product for Alpha-1 Antitrypsin deficiency. Guided by the needs and experiences of patients, CSL is advancing an integrated, patient-centric approach that offers greater convenience and improved patient outcomes. Transplant and Immunology In Transplant and Immunology, CSL is leveraging its deep scientific expertise in immunomodulatory mechanisms to unlock synergies between alloimmune and autoimmune diseases. The goal is to bring life-changing solutions to patients in both transplant and immunology. In Immunology, CSL continues to build on its 40-year legacy in hereditary angioedema (HAE) by expanding our portfolio of therapies to provide optimal treatments for the full range of HAE patients. This includes the recent regulatory approval of ANDEMBRY®, a first-in-class, home-grown recombinant monoclonal antibody, in major markets including the United States, European Union, United Kingdom, Japan, Switzerland, Australia and the United Arab Emirates. Looking ahead, CSL is focused on advancing its leadership in immunology with innovative treatments for select autoimmune diseases of high unmet need, reinforcing its commitment to improving patient outcomes across chronic, complex immune-mediated conditions. Despite advances in transplantation improving short‑term survival, long-term survival remains suboptimal. Therefore, CSL is committed to developing therapies to address conditions that may lead to transplant failure. In haematopoietic stem cell transplantation, acute graft‑versus‑host disease (GvHD) is a life-threatening type of rejection and a leading cause of post-transplant morbidity and mortality. There remains a significant unmet need for more effective, less toxic GvHD therapies and CSL is investigating ZEMAIRA® (Alpha-1 Antitrypsin, AAT) for the prevention and treatment of acute GvHD. For solid organ transplant recipients, CSL is advancing therapies to address immune responses that may lead to transplant organ failure, ideally with less toxic treatment regimens and addressing ischemia reperfusion injury (IRI) which can damage the allograft when blood flow is re-introduced. Haematology Improving and extending the lives of patients with rare bleeding disorders is the focus of CSL’s haematology therapeutic area. Significant progress has been achieved in recent years in the treatment of haemophilia A and B through the introduction of innovative recombinant coagulation factor medicines and HEMGENIX® (etranacogene dezaparvovec), an AAV5 (adeno‑associated virus) gene therapy for the treatment of haemophilia B. CSL’s efforts in haematology focus on addressing the high unmet needs of patients with sickle cell disease, with a dual focus on acute treatment of vaso-occlusive crises and effective prophylaxis to reduce the frequency of sickle cell related events. Additionally, CSL is advancing innovative therapies targeting benign haematological conditions, particularly in haemostasis and thrombosis where there is a high unmet need. With a suite of therapies, CSL is also focused on patient blood management (PBM), aiming to reduce reliance on allogeneic blood product transfusions with the use of coagulation factor concentrates wherever available. CSL’s R&D studies include fibrinogen and prothrombin factor concentrates for use in surgical settings with high risk of major bleeding, as well as intravenous iron therapies to support pre- and post-operative anaemia management. Cardiovascular and Renal Extending the lives of patients
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: outlook, management commentary

```text
Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming
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
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment table, product table, sector metrics

```text
Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming financial year, these measures will drive further growth through transforming our
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/

```text
CSL 2025 Annual Report Table of Contents 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 CSL 2025 Annual Report Driven by Our Promise Annual Report 2024/25 Our ambition is to deliver enduring patient impact in areas of high unmet medical need. CSL provides lifesaving products to patients in more than 100 countries and employs over 29,000 people. + READ MORE PAGE 18 INNOVATION EXCELLENCE AND INNOVATION CSL is one of the world’s largest collectors of human plasma CSL Plasma operates one of the world’s largest and most sophisticated plasma collection networks, with collection centres in the US and Europe. Plasma collected at CSL Plasma facilities is used by CSL Behring for the purpose of manufacturing and delivering its life-saving therapies to people in more than 100 countries. + READ MORE PAGES 32–33 CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Businesses and Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: revenue, income, NPAT

```text
income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: cash flow statement, operating cash flow

```text
Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: free cash flow, cash movement

```text
Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: cash, debt, gearing, capital

```text
Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/95/

```text
CSL 2025 Annual Report – Page 95 1 94 Table of Contents 96 148 CSL 2025 Annual Report Consolidated Entity 2025 2024 Notes US$m US$m Cash Flows from Operating Activities Profit before income tax expense 3,724 3,375 Adjustments for: Depreciation and amortisation 1,017 938 Inventory provisions 163 177 Share-based payment expense 149 169 Provision for expected credit losses 6 4 Finance costs, net 410 437 Net gain on business disposals 2 (30) — Loss/(gain) on disposal of property, plant and equipment 11 (2) Unrealised foreign exchange losses 25 53 Changes in operating assets and liabilities: Increase in receivables and contract assets (314) (766) Increase in inventories (628) (780) Increase in trade and other payables 319 445 Decrease in provisions and other liabilities (242) (70) Income tax paid (637) (784) Finance costs paid, net (412) (432) Net cash inflow from operating activities 3,561 2,764 Cash flows from Investing Activities Payments for property, plant and equipment (636) (847) Payments for intangible assets (362) (409) Net proceeds from business disposals 2 180 — Payments for financial assets (13) (3) Payments for other assets (19) — Net cash outflow from investing activities (850) (1,259) Cash flows from Financing Activities Proceeds from issue of shares 17 40 Dividends paid to CSL Limited shareholders 10 (1,334) (1,192) Dividends paid to non-controlling interests 22 (100) (74) Proceeds from borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: revenue, income, NPAT

```text
profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: segment performance, sector metrics

```text
Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: risks

```text
impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: one-off items

```text
impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: segment table, product table, sector metrics

```text
Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/99/

```text
CSL 2025 Annual Report – Page 99 1 98 Table of Contents 100 148 CSL 2025 Annual Report Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

```
