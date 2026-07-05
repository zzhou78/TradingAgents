# Codex Role Evidence Packet: CSL.AX

- Trade date: `2026-07-02`
- Instrument identity: `CSL Limited`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for CSL.AX from 2026-06-02 to 2026-07-02
# Total records: 22
# Data retrieved on: 2026-07-05 15:16:18

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-06-02,94.0,94.14,91.82,92.56,1882432,0.0,0.0
2026-06-03,90.62,92.27,90.0,92.24,1784117,0.0,0.0
2026-06-04,93.85,93.94,92.29,92.59,1782919,0.0,0.0
2026-06-05,93.41,97.91,93.41,97.91,1945984,0.0,0.0
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

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for CSL.AX

- Requested analysis date: 2026-07-02
- Latest trading row used: 2026-07-02
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 116.88 |
| High | 118.60 |
| Low | 116.33 |
| Close | 117.75 |
| Volume | 1298766 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 114.56 |
| close_50_sma | 109.07 |
| close_200_sma | 155.14 |
| rsi | 62.97 |
| boll | 109.47 |
| boll_ub | 124.03 |
| boll_lb | 94.90 |
| macd | 3.06 |
| macds | 1.76 |
| macdh | 1.30 |
| atr | 3.68 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-21 | 100.05 |
| 2026-05-22 | 99.76 |
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

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-06-02 to 2026-07-02:

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
2026-06-05: 119.20140014648437
2026-06-04: 120.06300018310547
2026-06-03: 120.99900024414063
2026-06-02: 121.95000015258789


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-06-02 to 2026-07-02:

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
2026-06-05: 163.70850799560546
2026-06-04: 164.32176376342773
2026-06-03: 164.93595252990724
2026-06-02: 165.5751184463501


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-06-02 to 2026-07-02:

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
2026-06-05: 37.15892842808618
2026-06-04: 21.949736368821032
2026-06-03: 20.778417024999136
2026-06-02: 21.0465689865613


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-06-02 to 2026-07-02:

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
2026-06-05: -7.034740195264632
2026-06-04: -7.704175580712445
2026-06-03: -7.904884354862261
2026-06-02: -8.010445391341321


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-06-02 to 2026-07-02:

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
2026-06-05: 3.3332894200628043
2026-06-04: 3.1804649658969626
2026-06-03: 3.294346534224674
2026-06-02: 3.350834916965513


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
## CSL.AX News, from 2026-06-25 to 2026-07-02:

### European Regulator Calls for Amgen’s Tavneos to Have Authorization Revoked (source: The Wall Street Journal)
The committee is recommending that no new patients start treatment with Tavneos and that existing patients be switched to suitable alternatives.
Link: https://www.wsj.com/health/pharma/european-regulator-calls-for-amgens-tavneos-to-have-authorization-revoked-b3922308?siteid=yhoof2&yptr=yahoo


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-25 and 2026-07-02
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for CSL.AX
# Data retrieved on: 2026-07-05 15:16:31

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
# Data retrieved on: 2026-07-05 15:16:31

Name: CSL Limited
Sector: Healthcare
Industry: Biotechnology
Market Cap: 58336264192
PE Ratio (TTM): 13.610056
Forward PE: 13.246234
PEG Ratio: 1.82
Price to Book: 2.184138
EPS (TTM): 8.95
Forward EPS: 9.195821
Dividend Yield: 3.5
Beta: 0.084
52 Week High: 275.79
52 Week Low: 90.0
50 Day Average: 108.287
200 Day Average: 155.12434
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
Book Value: 55.770283
Free Cash Flow: 1848125056
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for CSL.AX (quarterly)
# Data retrieved on: 2026-07-05 15:16:31

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
# Data retrieved on: 2026-07-05 15:16:32

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
# Data retrieved on: 2026-07-05 15:16:32

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

- Trade date: `2026-07-02`
- Collection status: `ok`
- Market: `ASX`
- ASX code: `CSL`
- As-of rule: Only ASX announcements with announcement/lodgement date <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_fallback_document | available | 2025-12-31 | Full Year Results | https://www.csl.com/pdf/56bf77f4-8eff-40ff-bb67-c890e3a3476e/CSL-FY25-Results-and-Major-Strategic-Initiatives.pdf |
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/17/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/61/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/69/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/77/ |
| asx_fallback_document | available | 2025-12-31 | Cash Flow Statement | https://investors.csl.com/annualreport/2025/95/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/97/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/99/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/107/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/109/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/113/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/115/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/117/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/125/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/129/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/137/ |
| asx_fallback_document | available | 2024-12-31 | Annual Report | https://investors.csl.com/annualreport/2025/139/ |

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

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: R&D

```text
R&D, our portfolio and re-establishing the organisation with a leaner, more agile design. We must accelerate initiatives across a smaller number of sites and with fewer layers of management. We recognise that we must embark on these changes whilst preserving our underlying performance for you, our shareholders, next financial year and in the years to come. One of the key initiatives is the proposal to demerge CSL Seqirus to shareholders, as a substantial ASX-listed entity. There is a clear benefit for both entities in doing this, providing autonomy and allowing each of them to pursue separate growth strategies and focus on their core capabilities. CSL can be proud of the value it has created for shareholders with a decade long commitment to Seqirus but the time is right to free them to chart a successful, independent future. This also will assist us streamlining how our core CSL organisation looks and works. While these changes are among the most significant for our company in the last 20 years, the Board and management team are unified in our optimism in the outlook for both CSL and Seqirus. We remain confident we have the right settings to ensure we deliver sustainable growth for our shareholders and life-changing treatments for our patients. Governance and board renewal Part of my role is to ensure the CSL Board is regularly renewed and this year we were pleased to welcome two more new directors. Dr Brian Daniels is seeking election as a director. He has been a director since December 2024 and has more than 30 years’ experience in clinical development, commercialisation and biotech investing. Dr Daniels led development and medical affairs at Bristol-Myers Squibb and served as director of Danish pharmaceutical company Novo Nordisk until 2021. In June we announced that Cameron Price would join the board as a Non-executive Director effective 1 October. Cameron is a highly respected executive with extensive experience in the risk and legal fields. He has more than 35 years’ experience and from 2014 he was the General Counsel & Chief Risk Officer at the Future Fund, Australia’s sovereign wealth fund, which invests more than $300 billion globally. These new directors bring invaluable skills and expertise to your Board. Dear Shareholders, I am pleased to have this opportunity to share our results and operating review for the 2024/25 financial year on behalf of your Board. I am proud to report that CSL has stayed true to our mission of delivering for patients, communities and shareholders and encourage you to read our Chief Executive Officer’s communication and also that from Dr Megan Clark AC, who chairs our Human Resources and Remuneration Committee. 4 Engagement The Board of Directors has a strong focus on engaging with a broad range of stakeholders both within CSL and externally. To support engagement with these diverse parties the Board always takes time to visit different locations throughout CSL’s global network. In September 2024 the Board visited CSL’s European operations, including manufacturing plants and research and development facilities in Liverpool (UK), Bern (Switzerland) and Marburg (Germany). In June 2025 the Board held its meeting in Amsterdam, Netherlands, where it met with key external stakeholders including health economists, supply chain partners and researchers. We also celebrated the 25th anniversary of our manufacturing facility in Bern. This event underlined how integral CSL’s acquisition of ZLB in 2000 was to our growth and how important the company’s ongoing contribution is to the Swiss economy. I and some of my colleagues spend time each year meeting with our shareholders. These meetings allow us to listen to feedback from our investors, which we value greatly. One topic we know is top of mind for our shareholders is remuneration. Our investors sent a message at the Annual General Meeting in October – and we continue to listen. You can find the details on remuneration on page 61 of this report. We will continue to listen and respond to feedback in relation to our remuneration approach as well as any other issues important to our shareholders. Your Board is confident in the outlook for CSL and for our ability to deliver enduring patient impact in areas of high unmet medical need. Achieving this will allow us to provide sustainable, profitable growth for our shareholders. Once again, on behalf of the Board, I’d like to extend my thanks for your support. “The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done.” Dr Brian McNamee AO Chairman 5 CSL Limited Annual Report 2024/25 CSL Message from the CEO CSL Vifor grew sales, underpinned by our nephrology products and new country launches. Whilst CSL Seqirus was negatively impacted by low influenza immunisation rates, particularly in the United States, this was partially offset by strong demand for avian influenza vaccine for pandemic protection. Throughout this report, you will find detailed information regarding the financial and operating highlights of CSL throughout the financial year. I will also add a few personal reflections of my own. Refocused strategy Having been Chief Executive Officer for two years, I’ve had time to work with my management team to laser focus our priorities and develop our ambition to deliver enduring patient impact in areas of high unmet medical need and to provide durable returns to our shareholders. CSL has a strong track record of sustainable, profitable growth. However, our operating environment has grown increasingly complex with a dynamic geopolitical backdrop and competitive pressures. We need to accelerate our innovation with our current commercial and clinical portfolio to ensure we’re successful through the next decade and our structure is fit for purpose. After many years of significant growth, it is important we
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: plasma collections

```text
plasma collection networks, with collection centres in the US and Europe. Plasma collected at CSL Plasma facilities is used by CSL Behring for the purpose of manufacturing and delivering its life-saving therapies to people in more than 100 countries. + READ MORE PAGES 32–33 CSL Message from the Chair 4 Message from the CEO 6 Performance Year in Review 8 CSL’s Strategy 10 CSL’s Sustainability Strategy 12 Value Creation 14 CSL’s Businesses and Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: margins

```text
margin and increase plasma volumes at a lower cost per litre. Our purpose and our people My final priority is to enable our people to deliver this exciting new future. We will continue to invest in our leaders to build skills, enhance engagement and increase productivity. This will help embed a culture of continuous learning and personal growth to ensure that our staff feel valued, included and engaged in our mission to deliver enduring patient impact. Outlook Over the longer term, like Brian and the Board, I believe your company is in a strong position to deliver on our mission for patients in need, our partners and our shareholders. Our therapies continue to be valued by patients and healthcare systems around the world. CSL Behring will continue to focus on improving gross margins, aided by the completion during the year of the RIKA roll-out across our plasma centres. While the market conditions for CSL Seqirus remain challenging, influenza will continue to impact the public health systems. The ability of a newly separated Seqirus business to pursue its own growth strategy with a dedicated management team and a differentiated strategy ensures it will be well placed to grow market share. At CSL Vifor, the iron market continues to evolve, but we expect to maintain a leadership position and build on the momentum in our nephrology business. I look forward to updating you next year on the progress we make during the 2026 financial year. In the meantime, please take the time to review the wealth of information in this report. As ever, thank you for your support of CSL. “After many years of significant growth, it is important we stay committed to a formula that can deliver for years to come. I believe a simple and focused CSL is best for patients, our people and our shareholders and we have outlined plans to evolve our strategy to re-focus on what makes us unique.” Dr Paul McKenzie Chief Executive Officer and Managing Director CSL Limited 7 CSL Limited Annual Report 2024/25 Year in Review (*) Limited assurance by Deloitte. (**) As at 30 June 2025. Financial Research and development Growth through portfolio development and commercialisation with integrated project focused mindset. Delivered CSL’s portfolio. People Enable CSL’s people to deliver the company’s future. 24,434 (80%) respondents to 2025 Employee Engagement Survey. 72.9%* 2025 Engagement Index. Expansion of mental health benefits via a third party provider to 43 countries for employees and their families. CSL has launched the CSL Community Impact Awards, a new initiative designed to support not-for-profit community organisations focused on health in Australia. 816 participants in the Frontline Leader (FFL) Program 97,789 global recognition moments shared in Celebrate the Promise Program** RiaSTAP® AFD CSL’s human fibrinogen concentrate is making progress in the treatment of acquired fibrinogen deficiency (AFD). In October, the first patient was treated in the Phase III study to evaluate the effectiveness of RiaSTAP® in managing bleeding episodes and to assess its overall safety profile in these patients. Strategically locate capabilities that need to collaborate to increase productivity, reduce complexity and drive innovation. Consolidation of R&D sites to create 6 anchor sites in the US, UK, Switzerland and Australia. + READ MORE ABOUT CSL’S R&D PIPELINE AT WWW.CSL.COM/RESEARCH-ANDDEVELOPMENT/PRODUCT-PIPELINE NPATA attributable to equity holders of US$3.2 billion for the year ended 30 June 2025, up 11% on a reported currency basis when compared to the prior comparable period. Strong growth in immunoglobulins portfolio, up 7% at constant currency. US$11,158m CSL Behring revenue US$2,166m CSL Seqirus revenue US$2,234m CSL Vifor revenue Cashflow from operations was $3,561 million, up 29%. The increase was driven by overall growth in sales, higher profitability and improved working capital management. 8 Performance ANDEMBRY® • Inhibits the top of the HAE cascade by targeting factor XIIa and provides sustained protection from attacks. • Once-monthly dosing reduced HAE attacks by a median of more than 99% and a least squares mean of 89.2%, compared to placebo. ANDEMBRY® (garadacimab), the only treatment targeting factor XIIa for prophylactic use to prevent attacks of hereditary angioedema (HAE) in adult and paediatric patients aged 12 years and older. By targeting factor XIIa, a plasma protein that plays a key role in attacks of swelling in people with HAE, ANDEMBRY® inhibits the top of the HAE cascade to prevent HAE attacks. ANDEMBRY®, the only treatment to offer once-monthly dosing from the start for all patients, is a subcutaneous self-injection delivered in 15 seconds or less via an autoinjector with a citrate-free formula. “ANDEMBRY®, the first monoclonal antibody discovered and developed entirely by CSL, offers people living with this life-threatening condition long-term control over their disease along with a convenient administration method. ANDEMBRY® underscores our longstanding and enduring commitment to better the lives of the patients we serve, including those suffering with HAE. I’d like to thank all the physicians, patients and my colleagues who contributed to this exciting milestone for HAE patients and CSL.” Bill Mezzanotte, MD, Executive Vice President, Head of R&D, CSL. HAE is a rare, chronic, and potentially life-threatening genetic disorder characterised by recurrent and unpredictable attacks of angioedema. Attacks of HAE are often painful and can affect multiple sites of the body, including the abdomen, larynx, face and extremities. HAE occurs in about 1 in 50,000 people of any ethnic group. Optimised launch excellence to outperform competition. Commercial During the period CSL Seqirus was recognised for its global leadership in pre-pandemic preparedness with the award of the vast majority of contracts for H5 avian flu. ANDEMBRY® Approved in the US, European Union (EU), United Kingdom (UK), Japan, Switzerland,
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: debt, liquidity

```text
debt for future growth 14 Performance WHAT CSL DOES THE VALUE CSL CREATES Provide a safe, rewarding and productive workplace for promising futures Powered by research and development to identify new indications for CSL’s existing products, and innovative new products for patients and public health Collaborative partnerships Partnering to expand CSL’s global impact and reach Driven by safety, quality, reliability, and innovation in CSL’s operations, while embedding environmental and social considerations into work practices and responsibly sourcing materials and inputs Seek to provide sustainable financial growth with a focus on revenue and margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 CSL Behring exists to meet the needs of patients with rare and serious diseases, and those suffering from trauma-related bleeding. Plasma-derived therapies (PDTs) form the core of the portfolio. Patients are the core focus. CSL Behring consists of three vertically integrated components that span the journey from donor to patient. In plasma collection the focus is on three areas; enhancing collection efficiency, reducing the unit acquisition cost and providing a world-class experience for donors and communities. CSL Behring’s manufacturing capability is focused on: • fractionating and transforming plasma into a portfolio of innovative PDTs, and • delivering supply of CSL’s recombinant medicines. CSL Behring’s commercial and medical teams around the world are engaged with healthcare providers, payers and key stakeholders, working to meet patient needs and to deliver successful launches of CSL’s life-saving therapies. This helps provide access to more people with rare and serious diseases. One of CSL Behring’s key priorities is sourcing sufficient and sustainable volumes of plasma to meet the growing need for CSL’s medicines. PDTs have a 9–12 month manufacturing cycle, which is more complex than other pharmaceutical products. These products are vital for patients in need, and can transform their lives. CSL Behring commits to reducing the cost per litre of plasma. The aim to increase yield for immunoglobulins (Ig) and albumin through data analytics, smarter plasma allocation and implementing an operational excellence program. In plasma collection, the Rika collection device and individualised nomogram, iNomi™, enables CSL to collect the optimal amount of plasma from donors. These avenues to yield improvement through technology and innovation are critical to CSL’s ability to increase the supply of therapies to patients. There is significant opportunity for continued global immunoglobulin (lg) growth as the market expands. Within this growing market, PRIVIGEN® and HIZENTRA® are expected to gain share. CSL Behring plays a leading role in Ig and will continue to identify expansion opportunities. CSL expects the global haemophilia B market to grow in coming years due to the steady prevalence of the disease and the launch of novel treatments, including gene therapies. As this market grows, CSL Behring will look to expand its portfolio. The hereditary angioedema (HAE) market may also grow due to improved diagnosis rates and new prophylaxis therapies. ANDEMBRY® (garadacimab), CSL’s next generation HAE therapy, is now approved in US, European Union (EU), United Kingdom (UK), Japan, Switzerland, Australia and the United Arab Emirates. It is available in US, Japan, Germany and Greece. CSL Behring has built on its leadership position and continues to innovate across rare and serious diseases. + READ MORE AT INVESTORS.CSL.COM CSL’s Businesses and Outlook US$11,158m CSL Behring revenue 16 Performance The FY2025 financial year was dynamic for the vaccine market and CSL Seqirus generated positive growth. Over the short term, two current trends will likely continue. First, the exciting acceleration of new vaccine technologies. CSL Seqirus is well positioned with its technology platforms (cell-based, adjuvants, and sa‑mRNA). The second trend is reduced rates of immunisation following the pandemic, particularly in the United States. However, the European vaccination market is stabilising. Against this backdrop, CSL Seqirus maintained commercial discipline in a competitive market. The business expects to continue to drive growth through life cycle management, which will allow CSL to deliver ongoing value to public health systems. Seasonal influenza remains one of the most consequential vaccine preventable diseases due to its significant morbidity and mortality, with unmet need across all populations, and with particular risk to the very young, due to immature immune
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/
- Supports claims: guidance, outlook

```text
Outlook 16 Global Manufacturing Presence 19 Platforms, Therapeutic Areas and Product Portfolio 20 Material Risks 24 Healthier World Healthier Communities 27 Healthier Environment 35 IN THIS REPORT ANNUAL GENERAL MEETING The 2025 Annual General Meeting (AGM) of CSL Limited (ABN 99 051 588 348) will be held on Tuesday, 28 October 2025 at 10 a.m. (Melbourne time) at RACV City Club, Level 17, 501 Bourke St, Melbourne 3000. Governance Governance 40 Directors’ Report Remuneration Report 61 Financial Report Financial Report 90 Shareholder Information Shareholder Information 138 Key Performance Data Summary 141 Glossary 143 Corporate Directory 144 Sections which are read as part of the Operating and Financial Review (see page 52) 2025 19/8 Annual results and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 3/10 Final dividend paid 28/10 Annual General Meeting 31/12 Half Year ends 2026 10/2 Half Year results and interim dividend announcement 10/3 Shares trade ex‑dividend 11/3 Record date for interim dividend 9/4 Interim dividend paid 30/6 Full Year ends 18/8 Annual profit and final dividend announcement 9/9 Shares trade ex‑dividend 10/9 Record date for final dividend 2/10 Final dividend paid 27/10 Annual General Meeting 31/12 Half Year ends CSL CALENDAR ABOUT THIS REPORT This Annual Report combines CSL’s financial and non‑financial performance in one comprehensive report, linking CSL’s sustainability and strategic priorities to its business results. Unless otherwise stated, this report covers CSL’s controlled entities as disclosed within its consolidated entity disclosure statement included in the financial report. This 2025 Annual Report is a summary of CSL’s operations and activities for the year ended 30 June 2025 and financial position as at 30 June 2025. This report covers CSL’s global operations, including subsidiaries, unless otherwise noted. A reference to CSL, CSL Group, we, us and our and similar expressions refer collectively to CSL Limited and its related bodies corporate. Please refer to the inside back cover to read the legal notice and the disclaimers as they relate to forward looking statements, non-IFRS financial information and trademarks. + READ MORE AT INVESTORS.CSL.COM 1 CSL Limited Annual Report 2024/25 CSL CSL is a global biopharma company working to create enduring impact for patients and public health. OUR GLOBAL MANUFACTURING AND OFFICE PRESENCE OUR BUSINESS US$15.6b in annual revenue 100+ countries that CSL provides lifesaving products to patients US$2.92 dividend per share for 2025 CSL uses its deep expertise in plasma-derived therapies, vaccines and biotechnology to deliver medicines for serious and complex diseases such as haemophilia, immune deficiencies, influenza and iron deficiency anaemia. CSL innovates at every step of the process. It pioneers therapies and vaccines, improves patients’ and donors’ experiences, broadens access to treatments, and tackles complexity at scale through specialised manufacturing processes. Helping address unmet medical needs is what sets CSL apart. CSL’s focus on diseases where it has a fundamental advantage in understanding the disease and the science; and medicines with a high degree of specialist expertise or manufacturing differentiation. 29,000+ employees globally United States Puerto Rico 2 Leading the Way in Treating Rare and Serious Diseases CSL Behring discovers, develops and delivers innovative therapies for people living with a range of rare and serious health conditions. Securing Health for All of Us CSL Seqirus is a major contributor to the prevention of influenza globally and a transcontinental partner in pandemic preparedness. Changing the Game in Iron Deficiency and Nephrology CSL Vifor is a global partner of choice for pharmaceuticals and innovative leading therapies in iron deficiency and nephrology. + READ MORE ON PAGE 16 + READ MORE ON PAGE 17 + READ MORE ON PAGE 18 Australia Japan China Germany Netherlands United Kingdom Spain Switzerland Italy Hungary 3 CSL Limited Annual Report 2024/25 CSL Message from the Chair The past year has been significant to say the least with a great deal of uncertainty in the external environment. Our CEO Paul McKenzie is settling into the second year of his tenure and along with his leadership team is working with the Board of Directors to address some shortcomings in the way our business currently operates and in charting a path for continuing growth. CSL is a truly global company, and we have the flexibility and resilience to cope with shifting external trends. We also have the financial strength to make decisions now that will enhance shareholder value in the future. Your Directors and management team are focused on what we can control and, despite the complexity, the company has delivered strong financial results. This is due to the great work of our staff who work across 100 different countries. Focused strategy While CSL has a strong track record of sustainable, profitable growth, our operating environment has become increasingly complex and competitive. A company of our size must and does constantly evolve its strategy to deal with such changing times. We must also recognise that not all our investments have performed as we had anticipated. The detail in this report shows our strategic ambition of delivering enduring patient impact in areas of high unmet medical need. This underpins value creation for shareholders into the future. It’s what we’ve always done, but how we deliver on that ambition needs adjustment – our organisation needs to return to a more productive one. . We remain focused on five core therapeutic areas – but particularly in areas where CSL is uniquely positioned to outperform our competitors. In order to improve clinical and commercial execution, CSL has embarked on a series of strategic initiatives to help reduce cost and complexity. Although this is painful and has a significant cost impact in the coming
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
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: revenue, income, NPAT

```text
revenue and margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: R&D

```text
research and development to identify new indications for CSL’s existing products, and innovative new products for patients and public health Collaborative partnerships Partnering to expand CSL’s global impact and reach Driven by safety, quality, reliability, and innovation in CSL’s operations, while embedding environmental and social considerations into work practices and responsibly sourcing materials and inputs Seek to provide sustainable financial growth with a focus on revenue and margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: margins

```text
margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/17/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/17/

```text
CSL 2025 Annual Report – Page 17 1 16 Table of Contents 18 148 CSL 2025 Annual Report WHAT CSL DOES THE VALUE CSL CREATES Provide a safe, rewarding and productive workplace for promising futures Powered by research and development to identify new indications for CSL’s existing products, and innovative new products for patients and public health Collaborative partnerships Partnering to expand CSL’s global impact and reach Driven by safety, quality, reliability, and innovation in CSL’s operations, while embedding environmental and social considerations into work practices and responsibly sourcing materials and inputs Seek to provide sustainable financial growth with a focus on revenue and margins Empowering CSL’s people through rewarding jobs, career development opportunities and professional training, while creating economic opportunities for CSL’s people and their communities. A healthier society, with enhanced scientific knowledge and skills through strong collaborations and positive outcomes, leading partnerships and high standards of integrity in development of CSL’s products. Creating economic opportunities for CSL’s business partners and the communities they operate in. CSL works with partners allowing the Company to create shared value, while extending capabilities throughout the value chain. Producing life-saving and life-protecting products for public health. CSL’s facilities are critical for the development and manufacture of CSL’s products, while providing a safe and productive workplace. Protecting global health and the wellbeing of individuals, families, businesses and communities from life‑threatening and/or complications resulting from influenza. Saving and/or improving the quality of life of hundreds and thousands of people with rare and serious diseases. Healthier people are able to participate and contribute to society, both socially and economically. See Healthier World page 26 for more. Delivering consistent, profitable and responsible growth for CSL’s investors, which fuels innovation and economic prosperity for multiple stakeholders. 15 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: risks

```text
risk assessment procedures, including an understanding of internal control, and the procedures performed in response to the assessed risks. The procedures performed in a limited assurance engagement vary in nature and timing from, and are less in extent than for a reasonable assurance engagement. Consequently, the level of assurance obtained in a limited assurance engagement is substantially lower than the assurance that would have been obtained had a reasonable assurance engagement been performed. Accordingly, we do not express a reasonable assurance opinion on whether the Subject Matter Information has been prepared, in all material respects, in accordance with the Criteria. Our procedures included: • Inquiries with relevant key personnel to obtain an understanding of the process for collating and preparing the respective Subject Matter Information; • Undertaking walkthroughs of key systems and processes for collating, calculating and reporting the Subject Matter Information; • Inspection of the supporting process documentation developed to support the collation, calculation and reporting process of the Subject Matter Information and investigating further where required; • Performing analytical review procedures on the Subject Matter Information and/or relevant supporting documentation; • Selection on a sample basis item to test the Subject Matter Information and agree to relevant supporting documentation; and • Review of the Selected Sustainability Metrics and Disclosures in the CSL 2025 Annual Report and CSL 2025 Corporate Governance Statement, and reconciliation to underlying workings and information. Other information The Directors of CSL are responsible for the other information. The other information comprises other Sustainability information in the CSL 2025 Annual Report and CSL 2025 Corporate Governance Statement but does not include the Subject Matter Information and our assurance report thereon. Our limited assurance conclusion does not cover the other information, and we do not express any form of assurance conclusion thereon. In connection with our assurance engagement on the Subject Matter Information, our responsibility is to read the other information identified above and, in doing so, consider whether the other information is materially inconsistent with the Subject Matter Information or our knowledge obtained in the assurance engagement, or otherwise appears to be materially misstated. If, based on the work we have performed, we conclude there is a material misstatement of this other information, we are required to report that fact. We have nothing to report in this regard. 59 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/61/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/61/

```text
CSL 2025 Annual Report – Page 61 1 60 Table of Contents 62 148 CSL 2025 Annual Report c) for designing, establishing and maintaining an effective system of internal control over its operations and financial reporting, including, without limitation, systems designed to ensure achievement of its control objectives and its compliance with applicable laws and regulations; d) for the preparation of the Subject Matter Information that is free from material misstatement, whether due to fraud or error; e) for selecting and applying measurement methodologies, and making estimates that are reasonable in the circumstances; f) for selecting the Criteria and ensuring that the Criteria is appropriately described and/or referred to in the CSL 2025 Annual Report and CSL 2025 Corporate Governance Statement; g) to provide us with: i. access to all information of which Directors of CSL are aware that is relevant for the purpose of this assurance engagement; ii. additional information that we may request from Directors of CSL for the purpose of this assurance engagement; and iii. unrestricted access to persons within CSL from whom we determine it necessary to obtain evidence; and h) for the electronic presentation of the Subject Matter Information and our limited assurance report on CSL’s website Responsibilities of the Assurance Practitioner Our responsibility is to express a limited assurance conclusion on the preparation of CSL’s Subject Matter Information, in all material respects, in accordance with the Criteria based on the procedures we have performed and evidence we have obtained. ASAE 3000 requires that we plan and perform our procedures to obtain limited assurance about whether anything has come to our attention that causes us to believe that CSL’s Subject Matter Information has not been prepared, in all material respects, in accordance with the Criteria for the reporting period 1 July 2024 to 30 June 2025. A limited assurance engagement in accordance on CSL’s Subject Matter Information involves identifying areas where a material misstatement of the Subject Matter Information is likely to arise, performing procedures to address the areas identified and considering the process used to prepare the Subject Matter Information. A limited assurance engagement is substantially less in scope than a reasonable assurance engagement in relation to both the risk assessment procedures, including an understanding of internal control, and the procedures performed in response to the assessed risks. The procedures performed in a limited assurance engagement vary in nature and timing from, and are less in extent than for a reasonable assurance engagement. Consequently, the level of assurance obtained in a limited assurance engagement is substantially lower than the assurance that would have been obtained had a reasonable assurance engagement been performed. Accordingly, we do not express a reasonable assurance opinion on whether the Subject Matter Information has been prepared, in all material respects, in accordance with the Criteria. Our procedures included: • Inquiries with relevant key personnel to obtain an understanding of the process for collating and preparing the respective Subject Matter Information; • Undertaking walkthroughs of key systems and processes for collating, calculating and reporting the Subject Matter Information; • Inspection of the supporting process documentation developed to support the collation, calculation and reporting process of the Subject Matter Information and investigating further where required; • Performing analytical review procedures on the Subject Matter Information and/or relevant supporting documentation; • Selection on a sample basis item to test the Subject Matter Information and agree to relevant supporting documentation; and • Review of the Selected Sustainability Metrics and Disclosures in the CSL 2025 Annual Report and CSL 2025 Corporate Governance Statement, and reconciliation to underlying workings and information. Other information The Directors of CSL are responsible for the other information. The other information comprises other Sustainability information in the CSL 2025 Annual Report and CSL 2025 Corporate Governance Statement but does not include the Subject Matter Information and our assurance report thereon. Our limited assurance conclusion does not cover the other information, and we do not express any form of assurance conclusion thereon. In connection with our assurance engagement on the Subject Matter Information, our responsibility is to read the other information identified above and, in doing so, consider whether the other information is materially inconsistent with the Subject Matter Information or our knowledge obtained in the assurance engagement, or otherwise appears to be materially misstated. If, based on the work we have performed, we conclude there is a material misstatement of this other information, we are required to report that fact. We have nothing to report in this regard. 59 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: revenue, income, NPAT

```text
NPAT as a STI measure CSL continues to believe NPATA is the right measure for the business at this time. However, recognising there are different views on this matter we have increased reporting and transparency of the reconciliation of NPATA to NPAT. We note: ‒ T he Board gave careful consideration to the relative merits of NPATA and NPAT and will continue to use NPATA for the CSL STI plan at this time, primarily because it reflects underlying performance, is more readily influenced by Management in any given year and is consistent with the approach of global peers. ‒ N PATA continues to be the metric used to measure and drive business performance, as well as setting guidance. ‒ N PAT continues to be used in determining LTI outcomes. ‒ W e report both NPATA and NPAT, including any adjustments made (which are set out in note 1 to the Financial Statements). Additional disclosure of the target setting process is set out in section 3.4 below. At the 2024 AGM, shareholders asked questions on the following topics, and CSL’s response is included. Topic CSL’s Response Quantum of CEO reward is too high and potential increase to LTI ‒ C SL needs to attract, engage and retain executive talent. The executive remuneration framework needs to provide flexibility to address talent challenges in various markets and allows CSL to compete with other large global pharmaceutical companies. ‒ W hen determining increases to reward, the Board considers the individual’s experience, performance and internal and external relativities. ‒ T he majority of the CEO’s reward is variable (STI and LTI) and at risk – creating strong alignment between reward and shareholder outcomes and is aligned to CSL’s pay for performance philosophy and focus on driving growth and long-term sustainable performance. ‒ A t 30 June 2025, Dr McKenzie sits around 70% of the global pharmaceutical/biotechnology peer group TDC median, driven by his lower target LTI quantum. No change to the CEO’s LTI opportunity (as a percentage of FR) will be made in 2026. How are NED fees structured and how much are they paid? ‒ C SL’s NEDs are paid fees for their Board responsibilities and contribution to Board committees. NED fees are set at a level to appropriately compensate suitably qualified directors, with the requisite experience and expertise. ‒ NEDs do not receive any performance related remuneration. ‒ T he Board monitors the practice of global Australian listed companies and those listed in European and US markets to ensure a competitive structure and fee arrangement is in place. ‒ S ection 8 of the Report provides the detail on NED fee arrangements, and in 2026 there will be no increase to NED fees. 67 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: EPS, DPS, dividends

```text
EPS continue to be aligned with shareholder interests and are appropriate measures of CSL’s long-term performance. Recognising the shareholder concerns around threshold payout, we have reduced the quantum payable for the ROIC threshold from 50% to 33%. During the year, significant focus was placed on ensuring a more robust process was undertaken in LTI target setting, including: ‒ C onsidering market guidance when determining LTI targets – in addition to CSL’s budget, forecast and historical financial performance. ‒ O btaining additional scenario modeling, including the impact of different market and internal conditions on company performance and remuneration outcomes. The Board believes the ROIC and EPS targets for the FY26 LTI award (which will be granted towards the end of calendar year 2025 and will be included in the 2025 Notice of AGM) are appropriate and aligns executive reward with the shareholder experience. We note: ‒ CSL uses statutory reporting for LTI measures. ‒ A one -year holding lock after vesting further aligns executive and shareholder experience. LTI Board discretion on LTI award outcomes CSL acknowledges the concerns raised regarding the quantum of the downward adjustment applied to the former CEO’s LTI award vesting following the acquisition of Vifor Pharma in 2022. The Board is committed to ongoing vigilance when exercising discretion following major corporate events. We note: ‒ U nder CSL’s governance framework, joint meetings across the Audit and Risk Management Committee and the Human Resources and Remuneration Committee are undertaken, to review how all significant risks have been managed and ask whether any downward discretion to remuneration is required. STI Use of NPATA rather than NPAT as a STI measure CSL continues to believe NPATA is the right measure for the business at this time. However, recognising there are different views on this matter we have increased reporting and transparency of the reconciliation of NPATA to NPAT. We note: ‒ T he Board gave careful consideration to the relative merits of NPATA and NPAT and will continue to use NPATA for the CSL STI plan at this time, primarily because it reflects underlying performance, is more readily influenced by Management in any given year and is consistent with the approach of global peers. ‒ N PATA continues to be the metric used to measure and drive business performance, as well as setting guidance. ‒ N PAT continues to be used in determining LTI outcomes. ‒ W e report both NPATA and NPAT, including any adjustments made (which are set out in note 1 to the Financial Statements). Additional disclosure of the target setting process is set out in section 3.4 below. At the 2024 AGM, shareholders asked questions on the following topics, and CSL’s response is included. Topic CSL’s Response Quantum of CEO reward is too high and potential increase to LTI ‒ C SL needs to attract, engage and retain executive talent. The executive remuneration framework needs to provide flexibility to address talent challenges in various markets and allows CSL to compete with other large global pharmaceutical companies. ‒ W hen determining increases to reward, the Board considers the individual’s experience, performance and internal and external relativities. ‒ T he majority of the CEO’s reward is variable (STI and LTI) and at risk – creating strong alignment between reward and shareholder outcomes and is aligned to CSL’s pay for performance philosophy and focus on driving growth and long-term sustainable performance. ‒ A t 30 June 2025, Dr McKenzie sits around 70% of the global pharmaceutical/biotechnology peer group TDC median, driven by his lower target LTI quantum. No change to the CEO’s LTI opportunity (as a percentage of FR) will be made in 2026. How are NED fees structured and how much are they paid? ‒ C SL’s NEDs are paid fees for their Board responsibilities and contribution to Board committees. NED fees are set at a level to appropriately compensate suitably qualified directors, with the requisite experience and expertise. ‒ NEDs do not receive any performance related remuneration. ‒ T he Board monitors the practice of global Australian listed companies and those listed in European and US markets to ensure a competitive structure and fee arrangement is in place. ‒ S ection 8 of the Report provides the detail on NED fee arrangements, and in 2026 there will be no increase to NED fees. 67 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: outlook, management commentary

```text
guidance when determining LTI targets – in addition to CSL’s budget, forecast and historical financial performance. ‒ O btaining additional scenario modeling, including the impact of different market and internal conditions on company performance and remuneration outcomes. The Board believes the ROIC and EPS targets for the FY26 LTI award (which will be granted towards the end of calendar year 2025 and will be included in the 2025 Notice of AGM) are appropriate and aligns executive reward with the shareholder experience. We note: ‒ CSL uses statutory reporting for LTI measures. ‒ A one -year holding lock after vesting further aligns executive and shareholder experience. LTI Board discretion on LTI award outcomes CSL acknowledges the concerns raised regarding the quantum of the downward adjustment applied to the former CEO’s LTI award vesting following the acquisition of Vifor Pharma in 2022. The Board is committed to ongoing vigilance when exercising discretion following major corporate events. We note: ‒ U nder CSL’s governance framework, joint meetings across the Audit and Risk Management Committee and the Human Resources and Remuneration Committee are undertaken, to review how all significant risks have been managed and ask whether any downward discretion to remuneration is required. STI Use of NPATA rather than NPAT as a STI measure CSL continues to believe NPATA is the right measure for the business at this time. However, recognising there are different views on this matter we have increased reporting and transparency of the reconciliation of NPATA to NPAT. We note: ‒ T he Board gave careful consideration to the relative merits of NPATA and NPAT and will continue to use NPATA for the CSL STI plan at this time, primarily because it reflects underlying performance, is more readily influenced by Management in any given year and is consistent with the approach of global peers. ‒ N PATA continues to be the metric used to measure and drive business performance, as well as setting guidance. ‒ N PAT continues to be used in determining LTI outcomes. ‒ W e report both NPATA and NPAT, including any adjustments made (which are set out in note 1 to the Financial Statements). Additional disclosure of the target setting process is set out in section 3.4 below. At the 2024 AGM, shareholders asked questions on the following topics, and CSL’s response is included. Topic CSL’s Response Quantum of CEO reward is too high and potential increase to LTI ‒ C SL needs to attract, engage and retain executive talent. The executive remuneration framework needs to provide flexibility to address talent challenges in various markets and allows CSL to compete with other large global pharmaceutical companies. ‒ W hen determining increases to reward, the Board considers the individual’s experience, performance and internal and external relativities. ‒ T he majority of the CEO’s reward is variable (STI and LTI) and at risk – creating strong alignment between reward and shareholder outcomes and is aligned to CSL’s pay for performance philosophy and focus on driving growth and long-term sustainable performance. ‒ A t 30 June 2025, Dr McKenzie sits around 70% of the global pharmaceutical/biotechnology peer group TDC median, driven by his lower target LTI quantum. No change to the CEO’s LTI opportunity (as a percentage of FR) will be made in 2026. How are NED fees structured and how much are they paid? ‒ C SL’s NEDs are paid fees for their Board responsibilities and contribution to Board committees. NED fees are set at a level to appropriately compensate suitably qualified directors, with the requisite experience and expertise. ‒ NEDs do not receive any performance related remuneration. ‒ T he Board monitors the practice of global Australian listed companies and those listed in European and US markets to ensure a competitive structure and fee arrangement is in place. ‒ S ection 8 of the Report provides the detail on NED fee arrangements, and in 2026 there will be no increase to NED fees. 67 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: risks

```text
Risk Management Committee and the Human Resources and Remuneration Committee are undertaken, to review how all significant risks have been managed and ask whether any downward discretion to remuneration is required. STI Use of NPATA rather than NPAT as a STI measure CSL continues to believe NPATA is the right measure for the business at this time. However, recognising there are different views on this matter we have increased reporting and transparency of the reconciliation of NPATA to NPAT. We note: ‒ T he Board gave careful consideration to the relative merits of NPATA and NPAT and will continue to use NPATA for the CSL STI plan at this time, primarily because it reflects underlying performance, is more readily influenced by Management in any given year and is consistent with the approach of global peers. ‒ N PATA continues to be the metric used to measure and drive business performance, as well as setting guidance. ‒ N PAT continues to be used in determining LTI outcomes. ‒ W e report both NPATA and NPAT, including any adjustments made (which are set out in note 1 to the Financial Statements). Additional disclosure of the target setting process is set out in section 3.4 below. At the 2024 AGM, shareholders asked questions on the following topics, and CSL’s response is included. Topic CSL’s Response Quantum of CEO reward is too high and potential increase to LTI ‒ C SL needs to attract, engage and retain executive talent. The executive remuneration framework needs to provide flexibility to address talent challenges in various markets and allows CSL to compete with other large global pharmaceutical companies. ‒ W hen determining increases to reward, the Board considers the individual’s experience, performance and internal and external relativities. ‒ T he majority of the CEO’s reward is variable (STI and LTI) and at risk – creating strong alignment between reward and shareholder outcomes and is aligned to CSL’s pay for performance philosophy and focus on driving growth and long-term sustainable performance. ‒ A t 30 June 2025, Dr McKenzie sits around 70% of the global pharmaceutical/biotechnology peer group TDC median, driven by his lower target LTI quantum. No change to the CEO’s LTI opportunity (as a percentage of FR) will be made in 2026. How are NED fees structured and how much are they paid? ‒ C SL’s NEDs are paid fees for their Board responsibilities and contribution to Board committees. NED fees are set at a level to appropriately compensate suitably qualified directors, with the requisite experience and expertise. ‒ NEDs do not receive any performance related remuneration. ‒ T he Board monitors the practice of global Australian listed companies and those listed in European and US markets to ensure a competitive structure and fee arrangement is in place. ‒ S ection 8 of the Report provides the detail on NED fee arrangements, and in 2026 there will be no increase to NED fees. 67 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/69/
- Supports claims: guidance, outlook

```text
guidance when determining LTI targets – in addition to CSL’s budget, forecast and historical financial performance. ‒ O btaining additional scenario modeling, including the impact of different market and internal conditions on company performance and remuneration outcomes. The Board believes the ROIC and EPS targets for the FY26 LTI award (which will be granted towards the end of calendar year 2025 and will be included in the 2025 Notice of AGM) are appropriate and aligns executive reward with the shareholder experience. We note: ‒ CSL uses statutory reporting for LTI measures. ‒ A one -year holding lock after vesting further aligns executive and shareholder experience. LTI Board discretion on LTI award outcomes CSL acknowledges the concerns raised regarding the quantum of the downward adjustment applied to the former CEO’s LTI award vesting following the acquisition of Vifor Pharma in 2022. The Board is committed to ongoing vigilance when exercising discretion following major corporate events. We note: ‒ U nder CSL’s governance framework, joint meetings across the Audit and Risk Management Committee and the Human Resources and Remuneration Committee are undertaken, to review how all significant risks have been managed and ask whether any downward discretion to remuneration is required. STI Use of NPATA rather than NPAT as a STI measure CSL continues to believe NPATA is the right measure for the business at this time. However, recognising there are different views on this matter we have increased reporting and transparency of the reconciliation of NPATA to NPAT. We note: ‒ T he Board gave careful consideration to the relative merits of NPATA and NPAT and will continue to use NPATA for the CSL STI plan at this time, primarily because it reflects underlying performance, is more readily influenced by Management in any given year and is consistent with the approach of global peers. ‒ N PATA continues to be the metric used to measure and drive business performance, as well as setting guidance. ‒ N PAT continues to be used in determining LTI outcomes. ‒ W e report both NPATA and NPAT, including any adjustments made (which are set out in note 1 to the Financial Statements). Additional disclosure of the target setting process is set out in section 3.4 below. At the 2024 AGM, shareholders asked questions on the following topics, and CSL’s response is included. Topic CSL’s Response Quantum of CEO reward is too high and potential increase to LTI ‒ C SL needs to attract, engage and retain executive talent. The executive remuneration framework needs to provide flexibility to address talent challenges in various markets and allows CSL to compete with other large global pharmaceutical companies. ‒ W hen determining increases to reward, the Board considers the individual’s experience, performance and internal and external relativities. ‒ T he majority of the CEO’s reward is variable (STI and LTI) and at risk – creating strong alignment between reward and shareholder outcomes and is aligned to CSL’s pay for performance philosophy and focus on driving growth and long-term sustainable performance. ‒ A t 30 June 2025, Dr McKenzie sits around 70% of the global pharmaceutical/biotechnology peer group TDC median, driven by his lower target LTI quantum. No change to the CEO’s LTI opportunity (as a percentage of FR) will be made in 2026. How are NED fees structured and how much are they paid? ‒ C SL’s NEDs are paid fees for their Board responsibilities and contribution to Board committees. NED fees are set at a level to appropriately compensate suitably qualified directors, with the requisite experience and expertise. ‒ NEDs do not receive any performance related remuneration. ‒ T he Board monitors the practice of global Australian listed companies and those listed in European and US markets to ensure a competitive structure and fee arrangement is in place. ‒ S ection 8 of the Report provides the detail on NED fee arrangements, and in 2026 there will be no increase to NED fees. 67 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/69/

```text
CSL 2025 Annual Report – Page 69 1 68 Table of Contents 70 148 CSL 2025 Annual Report Topic CSL’s Response LTI ROIC performance threshold was perceived as not sufficiently challenging The Board believes the LTI measures of ROIC and EPS continue to be aligned with shareholder interests and are appropriate measures of CSL’s long-term performance. Recognising the shareholder concerns around threshold payout, we have reduced the quantum payable for the ROIC threshold from 50% to 33%. During the year, significant focus was placed on ensuring a more robust process was undertaken in LTI target setting, including: ‒ C onsidering market guidance when determining LTI targets – in addition to CSL’s budget, forecast and historical financial performance. ‒ O btaining additional scenario modeling, including the impact of different market and internal conditions on company performance and remuneration outcomes. The Board believes the ROIC and EPS targets for the FY26 LTI award (which will be granted towards the end of calendar year 2025 and will be included in the 2025 Notice of AGM) are appropriate and aligns executive reward with the shareholder experience. We note: ‒ CSL uses statutory reporting for LTI measures. ‒ A one -year holding lock after vesting further aligns executive and shareholder experience. LTI Board discretion on LTI award outcomes CSL acknowledges the concerns raised regarding the quantum of the downward adjustment applied to the former CEO’s LTI award vesting following the acquisition of Vifor Pharma in 2022. The Board is committed to ongoing vigilance when exercising discretion following major corporate events. We note: ‒ U nder CSL’s governance framework, joint meetings across the Audit and Risk Management Committee and the Human Resources and Remuneration Committee are undertaken, to review how all significant risks have been managed and ask whether any downward discretion to remuneration is required. STI Use of NPATA rather than NPAT as a STI measure CSL continues to believe NPATA is the right measure for the business at this time. However, recognising there are different views on this matter we have increased reporting and transparency of the reconciliation of NPATA to NPAT. We note: ‒ T he Board gave careful consideration to the relative merits of NPATA and NPAT and will continue to use NPATA for the CSL STI plan at this time, primarily because it reflects underlying performance, is more readily influenced by Management in any given year and is consistent with the approach of global peers. ‒ N PATA continues to be the metric used to measure and drive business performance, as well as setting guidance. ‒ N PAT continues to be used in determining LTI outcomes. ‒ W e report both NPATA and NPAT, including any adjustments made (which are set out in note 1 to the Financial Statements). Additional disclosure of the target setting process is set out in section 3.4 below. At the 2024 AGM, shareholders asked questions on the following topics, and CSL’s response is included. Topic CSL’s Response Quantum of CEO reward is too high and potential increase to LTI ‒ C SL needs to attract, engage and retain executive talent. The executive remuneration framework needs to provide flexibility to address talent challenges in various markets and allows CSL to compete with other large global pharmaceutical companies. ‒ W hen determining increases to reward, the Board considers the individual’s experience, performance and internal and external relativities. ‒ T he majority of the CEO’s reward is variable (STI and LTI) and at risk – creating strong alignment between reward and shareholder outcomes and is aligned to CSL’s pay for performance philosophy and focus on driving growth and long-term sustainable performance. ‒ A t 30 June 2025, Dr McKenzie sits around 70% of the global pharmaceutical/biotechnology peer group TDC median, driven by his lower target LTI quantum. No change to the CEO’s LTI opportunity (as a percentage of FR) will be made in 2026. How are NED fees structured and how much are they paid? ‒ C SL’s NEDs are paid fees for their Board responsibilities and contribution to Board committees. NED fees are set at a level to appropriately compensate suitably qualified directors, with the requisite experience and expertise. ‒ NEDs do not receive any performance related remuneration. ‒ T he Board monitors the practice of global Australian listed companies and those listed in European and US markets to ensure a competitive structure and fee arrangement is in place. ‒ S ection 8 of the Report provides the detail on NED fee arrangements, and in 2026 there will be no increase to NED fees. 67 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: revenue, income, NPAT

```text
revenue for CSL Behring; ‒ Albumin Growth ‒ D eliver Hemgenix and Garadacimab launches; Below Target Target Above Target KPI 2: Realise value from organizational efficiencies ‒ A ccelerate key gross margin recovery programs in Operations ‒ A ccelerate key gross margin recovery programs in Plasma Below Target Target Above Target KPI 3: Advance Promising Futures for CSL’s people ‒ T alent management initiatives; ‒ S uccessful operating model changes implementation in Commercial & Plasma. 75 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: margins

```text
margin ‒ D elivery of CSL Operating System (COS) savings ‒ D rive value from Strategic Partnerships ‒ R eduction in growth of Inventory A Schmeltz 50% 100% 200% 87% Overall individual performance 87% of target, with an individual weighting outcome of 39% against the target of 45% Below Target Target Above Target KPI 1: Drive top line growth ‒ I ncrease in revenue for CSL Behring; ‒ Albumin Growth ‒ D eliver Hemgenix and Garadacimab launches; Below Target Target Above Target KPI 2: Realise value from organizational efficiencies ‒ A ccelerate key gross margin recovery programs in Operations ‒ A ccelerate key gross margin recovery programs in Plasma Below Target Target Above Target KPI 3: Advance Promising Futures for CSL’s people ‒ T alent management initiatives; ‒ S uccessful operating model changes implementation in Commercial & Plasma. 75 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/77/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/77/

```text
CSL 2025 Annual Report – Page 77 1 76 Table of Contents 78 148 CSL 2025 Annual Report KMP Individual performance outcomes Targets J Linton 50% 100% 200% 94% Overall individual performance was 94% of target, with an individual weighting outcome of 33% against the target of 35% Below Target Target Above Target KPI 1: Deliver growth plans ‒ R obust plans in place to deliver NPATA growth Below Target Target Above Target KPI 2: CSL Strategy Refresh ‒ A pproved and aligned compelling growth story, supported by robust financial projections Below Target Target Above Target KPI 3: Lead a high performing finance function ‒ O rganisation design implemented and cost savings realised for the affiliate finance function; and ‒ E mployee engagement outcomes. Below Target Target Above Target KPI 4: Drive performance across the enterprise ‒ G rowth in Behring margin ‒ D elivery of CSL Operating System (COS) savings ‒ D rive value from Strategic Partnerships ‒ R eduction in growth of Inventory A Schmeltz 50% 100% 200% 87% Overall individual performance 87% of target, with an individual weighting outcome of 39% against the target of 45% Below Target Target Above Target KPI 1: Drive top line growth ‒ I ncrease in revenue for CSL Behring; ‒ Albumin Growth ‒ D eliver Hemgenix and Garadacimab launches; Below Target Target Above Target KPI 2: Realise value from organizational efficiencies ‒ A ccelerate key gross margin recovery programs in Operations ‒ A ccelerate key gross margin recovery programs in Plasma Below Target Target Above Target KPI 3: Advance Promising Futures for CSL’s people ‒ T alent management initiatives; ‒ S uccessful operating model changes implementation in Commercial & Plasma. 75 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
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

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: debt, liquidity

```text
borrowings 97 2,058 Repayment of borrowings (832) (2,017) Principal payments of lease liabilities (89) (99) Net cash outflow from financing activities (2,241) (1,284) Net increase in cash and cash equivalents 470 221 Cash and cash equivalents at the beginning of the financial year 1,643 1,509 Exchange rate variations on foreign cash and cash equivalent balances 44 (87) Cash and cash equivalents at the end of the year 2,157 1,643 Reconciliation of cash and cash equivalents in the statement of cash flows: Cash and cash equivalents 2,157 1,657 Bank overdrafts — (14) Cash and cash equivalents at the end of the year 2,157 1,643 The consolidated statement of cash flows should be read in conjunction with the accompanying notes. 93 Consolidated Statement of Cash Flows For the Year Ended 30 June 2025 93 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://investors.csl.com/annualreport/2025/95/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

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
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: revenue, income, NPAT

```text
income are not reclassified from equity to the profit or loss until the disposal of the operation. If an entity in the Group has undertaken transactions in foreign currency, these transactions are translated into that entity’s functional currency using the exchange rates prevailing at the dates of the transactions. Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in other comprehensive income (OCI) and in the foreign currency translation reserve (FCTR) in equity. d. Material accounting policies Material accounting policies that summarise the measurement basis used and are relevant to an understanding of the financial statements are provided throughout the notes to the financial statements. There were no material changes in accounting policies during the year ended 30 June 2025, nor did the introduction of new accounting standards lead to any change in measurement or disclosure in these financial statements. The Group has not adopted any accounting standards that are issued but not yet effective. e. Key judgements and estimates In the process of applying the Group’s accounting policies, a number of judgements and estimates of future events are required. Material judgements and estimates are found in the following notes: Note 3: Revenue and Expenses Page 99 Note 4: Tax Page 101 Note 5: Inventories Page 103 Note 6: People Costs Page 104 Note 8: Intangible Assets Page 106 Note 11: Financial Risk Management Page 110 The Group has assessed the impact of climate risk on its financial reporting. The impact assessment principally focuses on key judgement areas, being the valuation and useful lives of intangible and tangible assets and the identification and valuation of provisions and contingent liabilities. No material accounting impacts or changes to judgements or other required disclosures have resulted from the assessment. While the assessment did not have a material impact for the year ended 30 June 2025, this may change in future periods as the Group regularly updates its assessment of the impact of the lower carbon economy. f. The notes to the financial statements The notes to these financial statements have been organised into logical groupings to help users find and understand the information they need. Where possible, related information has been provided in the same place. More detailed information (for example, valuation methodologies and certain reconciliations) has been placed at the rear of the document and cross-referenced where necessary. CSL has also reviewed the notes for materiality and relevance and provided additional information where it is helpful to an understanding of the Group’s performance. 95 95 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: risks

```text
Risk Management Page 110 The Group has assessed the impact of climate risk on its financial reporting. The impact assessment principally focuses on key judgement areas, being the valuation and useful lives of intangible and tangible assets and the identification and valuation of provisions and contingent liabilities. No material accounting impacts or changes to judgements or other required disclosures have resulted from the assessment. While the assessment did not have a material impact for the year ended 30 June 2025, this may change in future periods as the Group regularly updates its assessment of the impact of the lower carbon economy. f. The notes to the financial statements The notes to these financial statements have been organised into logical groupings to help users find and understand the information they need. Where possible, related information has been provided in the same place. More detailed information (for example, valuation methodologies and certain reconciliations) has been placed at the rear of the document and cross-referenced where necessary. CSL has also reviewed the notes for materiality and relevance and provided additional information where it is helpful to an understanding of the Group’s performance. 95 95 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in other comprehensive income (OCI) and in the foreign currency translation reserve (FCTR) in equity. d. Material accounting policies Material accounting policies that summarise the measurement basis used and are relevant to an understanding of the financial statements are provided throughout the notes to the financial statements. There were no material changes in accounting policies during the year ended 30 June 2025, nor did the introduction of new accounting standards lead to any change in measurement or disclosure in these financial statements. The Group has not adopted any accounting standards that are issued but not yet effective. e. Key judgements and estimates In the process of applying the Group’s accounting policies, a number of judgements and estimates of future events are required. Material judgements and estimates are found in the following notes: Note 3: Revenue and Expenses Page 99 Note 4: Tax Page 101 Note 5: Inventories Page 103 Note 6: People Costs Page 104 Note 8: Intangible Assets Page 106 Note 11: Financial Risk Management Page 110 The Group has assessed the impact of climate risk on its financial reporting. The impact assessment principally focuses on key judgement areas, being the valuation and useful lives of intangible and tangible assets and the identification and valuation of provisions and contingent liabilities. No material accounting impacts or changes to judgements or other required disclosures have resulted from the assessment. While the assessment did not have a material impact for the year ended 30 June 2025, this may change in future periods as the Group regularly updates its assessment of the impact of the lower carbon economy. f. The notes to the financial statements The notes to these financial statements have been organised into logical groupings to help users find and understand the information they need. Where possible, related information has been provided in the same place. More detailed information (for example, valuation methodologies and certain reconciliations) has been placed at the rear of the document and cross-referenced where necessary. CSL has also reviewed the notes for materiality and relevance and provided additional information where it is helpful to an understanding of the Group’s performance. 95 95 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/97/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/97/

```text
CSL 2025 Annual Report – Page 97 1 96 Table of Contents 98 148 CSL 2025 Annual Report c. Foreign currency While the presentation currency of the Group is US dollars, entities in the Group may have other functional currencies, reflecting the currency of the primary economic environment in which the relevant entity operates. The parent entity, CSL Limited, has a functional currency of US dollars. Any exchange differences arising from the translation of a foreign operation previously recognised in other comprehensive income are not reclassified from equity to the profit or loss until the disposal of the operation. If an entity in the Group has undertaken transactions in foreign currency, these transactions are translated into that entity’s functional currency using the exchange rates prevailing at the dates of the transactions. Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in other comprehensive income (OCI) and in the foreign currency translation reserve (FCTR) in equity. d. Material accounting policies Material accounting policies that summarise the measurement basis used and are relevant to an understanding of the financial statements are provided throughout the notes to the financial statements. There were no material changes in accounting policies during the year ended 30 June 2025, nor did the introduction of new accounting standards lead to any change in measurement or disclosure in these financial statements. The Group has not adopted any accounting standards that are issued but not yet effective. e. Key judgements and estimates In the process of applying the Group’s accounting policies, a number of judgements and estimates of future events are required. Material judgements and estimates are found in the following notes: Note 3: Revenue and Expenses Page 99 Note 4: Tax Page 101 Note 5: Inventories Page 103 Note 6: People Costs Page 104 Note 8: Intangible Assets Page 106 Note 11: Financial Risk Management Page 110 The Group has assessed the impact of climate risk on its financial reporting. The impact assessment principally focuses on key judgement areas, being the valuation and useful lives of intangible and tangible assets and the identification and valuation of provisions and contingent liabilities. No material accounting impacts or changes to judgements or other required disclosures have resulted from the assessment. While the assessment did not have a material impact for the year ended 30 June 2025, this may change in future periods as the Group regularly updates its assessment of the impact of the lower carbon economy. f. The notes to the financial statements The notes to these financial statements have been organised into logical groupings to help users find and understand the information they need. Where possible, related information has been provided in the same place. More detailed information (for example, valuation methodologies and certain reconciliations) has been placed at the rear of the document and cross-referenced where necessary. CSL has also reviewed the notes for materiality and relevance and provided additional information where it is helpful to an understanding of the Group’s performance. 95 95 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
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

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: segment revenue

```text
segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: R&D

```text
Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/99/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/99/

```text
CSL 2025 Annual Report – Page 99 1 98 Table of Contents 100 148 CSL 2025 Annual Report Segment information has been adjusted to exclude impairment and amortisation of acquired intellectual property (IP) and non-recurring items resulting from business acquisition and disposals. NPATA represents the statutory net profit after tax before impairment and amortisation of acquired IP and non-recurring items resulting from business acquisitions and disposals (as referenced above). Refer to the next page for the reconciliation between the segment information and statutory results. CSL Behring CSL Seqirus CSL Vifor Consolidated Entity US$m 2025 2024 2025 2024 2025 2024 2025 2024 Sales and service revenue 10,930 10,334 1,906 1,896 2,199 2,029 15,035 14,259 Influenza pandemic facility reservation fees — — 179 172 — — 179 172 Royalty and license revenue 190 235 — — 26 24 216 259 Other income 38 39 81 60 9 11 128 110 Total segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 Segment gross profit % 50.6% 49.7% 58.0% 61.9% 69.2% 68.5 % 54.3% 54.1% Selling and marketing expenses (937) (903) (230) (196) (449) (457) (1,616) (1,556) Segment operating result 4,704 4,372 1,027 1,122 1,096 956 6,827 6,450 Segment operating result % 42.2% 41.2% 47.4% 52.7% 49.1% 46.3 % 43.9% 43.6% Research and development expenses (1,359) (1,428) General and administrative expenses (1,000) (825) Underlying EBIT 4,468 4,197 Finance costs (448) (476) Finance income 38 39 Profit before tax 4,058 3,760 Income tax expense (645) (722) NPATA 3,413 3,038 - Attributable to CSL shareholders 3,219 2,907 - Attributable to non-controlling interests 194 131 Underlying EBIT 4,468 4,197 Non-recurring items related to CSL Vifor acquisition — (84) Net gain on business disposals 30 — Amortisation of other intangibles (excluding acquired IP)1 5 5 20 16 7 7 104 109 Depreciation1 335 337 59 60 23 25 549 528 EBITDA2 5,044 4,714 1,106 1,198 1,126 988 5,151 4,750 97 1 Depreciation and amortisation expenses (excluding IP) of $204m (2024: $187m) relate to non-segment expenditure and are not allocated to segments. 2 The Group's EBITDA of $5,151m (2024: $4,750m) represents statutory operating profit (EBIT) of $4,134m (2024: $3,812m) as reported in the consolidated income statement adding back total depreciation and amortisation expense of $1,017m (2024: $938m) (Note 3). The Group's EBITDA includes $2,125m (2024: $2,150m) of costs that are not allocated to segments. The costs are primarily attributable to centralised activities being R&D and general and administration. 97 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/107/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/107/

```text
CSL 2025 Annual Report – Page 107 1 106 Table of Contents 108 148 CSL 2025 Annual Report Retain and Grow Plan (RGP) Executive Performance and Alignment Plan (EPA) Non-Executive Director Plan (NED) Global Employee Share Plan (GESP) Total Number Weighted average exercise price (A$) Number Weighted average exercise price (A$) Number Weighted average exercise price (A$) Number Weighted average exercise price (A$) Number Outstanding at beginning of year 1,587,097 — 582,924 — 1,592 — 130,490 238.83 2,302,103 Granted during year 850,621 — 231,015 — 2,721 — 280,635 212.15 1,364,992 Exercised during year (806,109) — (90,681) — (2,769) — (250,787) 231.92 (1,150,346) Forfeited during year (126,730) — (120,893) — (148) — — — (247,771) GESP true-up — — — — — — (9,110) 238.83 (9,110) Closing balance at end of year 1,504,879 — 602,365 — 1,396 — 151,228 203.56 2,259,868 The share price at the dates of exercise (expressed as a weighted average) by equity instrument type, is as follows: 2025 2024 RGP A$303.80 A$269.40 EPA A$307.14 A$269.09 NED A$283.43 A$274.48 GESP A$279.38 A$277.98 b. Key Management Personnel Disclosures The remuneration of key management personnel is in Section 9 of the Directors’ Report and has been audited. Total compensation for key management personnel 2025 2024 US$ US$ Total of short term remuneration elements 10,304,999 9,092,275 Total of post-employment elements 384,100 357,797 Total of other long term elements 23,368 22,205 Total share-based payments 7,944,730 8,634,867 Total of all remuneration elements 18,657,197 18,107,144 105 105 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: revenue, income, NPAT

```text
income for the amount by which the asset’s carrying amount exceeds its recoverable amount. The recoverable amount is the higher of an asset’s fair value less costs to sell and value in use. For the purpose of assessing impairment, assets are grouped at the lowest levels for which there are separately identifiable cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: cash flow statement, operating cash flow

```text
cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: cash, debt, gearing, capital

```text
cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: segment performance, sector metrics

```text
segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: risks

```text
Impairment of intangible assets Assets with finite lives are reviewed for impairment whenever events or changes in circumstances indicate that the carrying amount may not be recoverable. Intangible assets that have an indefinite useful life (including goodwill) or not yet ready for use are tested annually for impairment or more frequently if events or changes in circumstances indicate that they may be impaired. An impairment loss is recognised in the statement of comprehensive income for the amount by which the asset’s carrying amount exceeds its recoverable amount. The recoverable amount is the higher of an asset’s fair value less costs to sell and value in use. For the purpose of assessing impairment, assets are grouped at the lowest levels for which there are separately identifiable cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: one-off items

```text
Impairment of intangible assets Assets with finite lives are reviewed for impairment whenever events or changes in circumstances indicate that the carrying amount may not be recoverable. Intangible assets that have an indefinite useful life (including goodwill) or not yet ready for use are tested annually for impairment or more frequently if events or changes in circumstances indicate that they may be impaired. An impairment loss is recognised in the statement of comprehensive income for the amount by which the asset’s carrying amount exceeds its recoverable amount. The recoverable amount is the higher of an asset’s fair value less costs to sell and value in use. For the purpose of assessing impairment, assets are grouped at the lowest levels for which there are separately identifiable cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
assets outside of business combinations is recognised as a financial liability only when a non-contingent obligation arises (i.e. when milestone is met). The determination of whether the payment should be capitalised or expensed is usually based on the substance of the contingent payment and whether it is expected to give rise to future economic benefits that will flow to the Group. If the milestones paid are for regulatory approval and a sales target, they are likely to meet the capitalisation criteria, and would be accumulated into the cost of the intangible. Changes in the fair value of contingent consideration liabilities acquired in a business combination in subsequent periods are recognised in research and development expenses for early-stage products and as cost of sales for currently marketed products. The effect of unwinding the discount over time for contingent consideration liabilities is recognised in finance costs. Software Costs incurred in developing or acquiring software licenses and information systems that contribute future financial benefits are capitalised. These include external direct costs of materials and service and payroll costs of employees’ time spent on the project. Amortisation is calculated on a straight-line basis over periods generally ranging from 3 to 10 years. IT development costs include only those costs directly attributable to the development phase and are only recognised following completion of technical feasibility, where the Group has the intention and ability to use the asset. Amortisation of intangible assets The useful lives of intangible assets are assessed to be either finite or indefinite. The amortisation period and method is reviewed at each financial year end at a minimum. Intangible assets with indefinite useful lives are not amortised. The useful life of these intangibles is reviewed each reporting period. Impairment of intangible assets Assets with finite lives are reviewed for impairment whenever events or changes in circumstances indicate that the carrying amount may not be recoverable. Intangible assets that have an indefinite useful life (including goodwill) or not yet ready for use are tested annually for impairment or more frequently if events or changes in circumstances indicate that they may be impaired. An impairment loss is recognised in the statement of comprehensive income for the amount by which the asset’s carrying amount exceeds its recoverable amount. The recoverable amount is the higher of an asset’s fair value less costs to sell and value in use. For the purpose of assessing impairment, assets are grouped at the lowest levels for which there are separately identifiable cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: R&D

```text
research and development expenses for early-stage products and as cost of sales for currently marketed products. The effect of unwinding the discount over time for contingent consideration liabilities is recognised in finance costs. Software Costs incurred in developing or acquiring software licenses and information systems that contribute future financial benefits are capitalised. These include external direct costs of materials and service and payroll costs of employees’ time spent on the project. Amortisation is calculated on a straight-line basis over periods generally ranging from 3 to 10 years. IT development costs include only those costs directly attributable to the development phase and are only recognised following completion of technical feasibility, where the Group has the intention and ability to use the asset. Amortisation of intangible assets The useful lives of intangible assets are assessed to be either finite or indefinite. The amortisation period and method is reviewed at each financial year end at a minimum. Intangible assets with indefinite useful lives are not amortised. The useful life of these intangibles is reviewed each reporting period. Impairment of intangible assets Assets with finite lives are reviewed for impairment whenever events or changes in circumstances indicate that the carrying amount may not be recoverable. Intangible assets that have an indefinite useful life (including goodwill) or not yet ready for use are tested annually for impairment or more frequently if events or changes in circumstances indicate that they may be impaired. An impairment loss is recognised in the statement of comprehensive income for the amount by which the asset’s carrying amount exceeds its recoverable amount. The recoverable amount is the higher of an asset’s fair value less costs to sell and value in use. For the purpose of assessing impairment, assets are grouped at the lowest levels for which there are separately identifiable cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: debt, liquidity

```text
debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/109/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/109/

```text
CSL 2025 Annual Report – Page 109 1 108 Table of Contents 110 148 CSL 2025 Annual Report Contingent consideration in connection with the purchase of individual assets outside of business combinations is recognised as a financial liability only when a non-contingent obligation arises (i.e. when milestone is met). The determination of whether the payment should be capitalised or expensed is usually based on the substance of the contingent payment and whether it is expected to give rise to future economic benefits that will flow to the Group. If the milestones paid are for regulatory approval and a sales target, they are likely to meet the capitalisation criteria, and would be accumulated into the cost of the intangible. Changes in the fair value of contingent consideration liabilities acquired in a business combination in subsequent periods are recognised in research and development expenses for early-stage products and as cost of sales for currently marketed products. The effect of unwinding the discount over time for contingent consideration liabilities is recognised in finance costs. Software Costs incurred in developing or acquiring software licenses and information systems that contribute future financial benefits are capitalised. These include external direct costs of materials and service and payroll costs of employees’ time spent on the project. Amortisation is calculated on a straight-line basis over periods generally ranging from 3 to 10 years. IT development costs include only those costs directly attributable to the development phase and are only recognised following completion of technical feasibility, where the Group has the intention and ability to use the asset. Amortisation of intangible assets The useful lives of intangible assets are assessed to be either finite or indefinite. The amortisation period and method is reviewed at each financial year end at a minimum. Intangible assets with indefinite useful lives are not amortised. The useful life of these intangibles is reviewed each reporting period. Impairment of intangible assets Assets with finite lives are reviewed for impairment whenever events or changes in circumstances indicate that the carrying amount may not be recoverable. Intangible assets that have an indefinite useful life (including goodwill) or not yet ready for use are tested annually for impairment or more frequently if events or changes in circumstances indicate that they may be impaired. An impairment loss is recognised in the statement of comprehensive income for the amount by which the asset’s carrying amount exceeds its recoverable amount. The recoverable amount is the higher of an asset’s fair value less costs to sell and value in use. For the purpose of assessing impairment, assets are grouped at the lowest levels for which there are separately identifiable cash flows (cash generating units), other than goodwill that is monitored at the segment level. Impairment losses recognised in respect of cash generating units are allocated first to reduce the carrying amount of any goodwill allocated to cash generating units, and then to reduce the carrying amount of the other assets in the unit on a pro-rata basis. Key Judgements and Estimates The Group's impairment assessment requires significant judgement. Determining whether goodwill, indefinite lived intangibles and in development intangibles have been impaired requires estimation of the recoverable amount of cash generating units based on value-in-use calculations. The calculations use cash flow projections based on operating budgets and a ten-year strategic business plan, after which a terminal value, based on our view of the longer term growth profile of the business unit is applied. Cash flows have been discounted using an implied pre-tax discount rate of 9.5% (2024: 9.8%) which is calculated with reference to external analyst views, long-term government bond rates and long-term cost of debt. The determination of cash flows over the life of an asset requires judgement in assessing the future demand for the Group’s products, climate related impacts, any changes in the price and cost of those products and of other costs incurred by the Group. Factors considered in the exercise of our judgement include the progress of the research project, time to market and the anticipated competitive landscape. These factors require judgement and may change in future periods, the impairment analysis takes into account the latest available information. Management considers that there are no reasonably foreseeable changes in assumptions (including change in tariffs) that would, in isolation, result in the impairment of goodwill at 30 June 2025. 107 107 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: revenue, income, NPAT

```text
Profit after tax sensitivity to general movement of 1% Monetary items, including financial asset and liabilities, denominated in currencies other than the functional currency of an operation are revalued at the end of each reporting period to its functional currency and the associated gain or loss is taken to the profit or loss. The following chart is based on depreciation of the actual rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net monetary assets/liabilities denominated in non-functional currency of various Group entities. Amounts shown are rounded to the nearest US$m. The below sensitivity analysis is not representative of all the inherent foreign exchange risk as the year end exposure does not reflect the exposure during the year including transactional exposure in respect of non-functional currency revenue and expenses. The movement in the foreign exchange rates could vary from the sensitivity rate used. Further, the Group is exposed to foreign exchange volatility in emerging markets, such as Argentina, Turkey and Mexico. US$m 2025 2024 AUD EUR CHF GBP CNY -5 0 5 Translation of net investments in foreign operations – Equity sensitivity to general movement of 1% Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in the FCTR in equity. The following chart is based on depreciation of the actual exchange rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net assets/liabilities (excluding investments in subsidiaries) of the foreign currency denominated financial statements of various Group entities. Amounts shown are rounded to the nearest US$m. US$m 2025 2024 AUD EUR CHF GBP CNY 0 5 10 15 20 b. Interest Rate Risk As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to investments of cash and cash equivalents would have changed the Group’s profit after tax by approximately $15m (2024: $12m). This calculation is based on applying a 1% movement to the total of the Group’s cash and cash equivalents at year end. As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to floating rate unsecured bank loans would have changed the Group’s profit after tax by approximately $11m (2024: $16m). This calculation is based on applying a 1% movement to the total of the Group’s floating rate unsecured bank loans (excluding bank overdrafts) at year end. 111 111 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: cash flow statement, operating cash flow

```text
cash flows from sales and purchases in foreign currencies to protect the Group against exchange rate movements. There are no material outstanding foreign exchange forward contracts at 30 June 2025 and 2024. Translation of non-functional currency monetary items – Profit after tax sensitivity to general movement of 1% Monetary items, including financial asset and liabilities, denominated in currencies other than the functional currency of an operation are revalued at the end of each reporting period to its functional currency and the associated gain or loss is taken to the profit or loss. The following chart is based on depreciation of the actual rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net monetary assets/liabilities denominated in non-functional currency of various Group entities. Amounts shown are rounded to the nearest US$m. The below sensitivity analysis is not representative of all the inherent foreign exchange risk as the year end exposure does not reflect the exposure during the year including transactional exposure in respect of non-functional currency revenue and expenses. The movement in the foreign exchange rates could vary from the sensitivity rate used. Further, the Group is exposed to foreign exchange volatility in emerging markets, such as Argentina, Turkey and Mexico. US$m 2025 2024 AUD EUR CHF GBP CNY -5 0 5 Translation of net investments in foreign operations – Equity sensitivity to general movement of 1% Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in the FCTR in equity. The following chart is based on depreciation of the actual exchange rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net assets/liabilities (excluding investments in subsidiaries) of the foreign currency denominated financial statements of various Group entities. Amounts shown are rounded to the nearest US$m. US$m 2025 2024 AUD EUR CHF GBP CNY 0 5 10 15 20 b. Interest Rate Risk As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to investments of cash and cash equivalents would have changed the Group’s profit after tax by approximately $15m (2024: $12m). This calculation is based on applying a 1% movement to the total of the Group’s cash and cash equivalents at year end. As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to floating rate unsecured bank loans would have changed the Group’s profit after tax by approximately $11m (2024: $16m). This calculation is based on applying a 1% movement to the total of the Group’s floating rate unsecured bank loans (excluding bank overdrafts) at year end. 111 111 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: cash, debt, gearing, capital

```text
cash flows from sales and purchases in foreign currencies to protect the Group against exchange rate movements. There are no material outstanding foreign exchange forward contracts at 30 June 2025 and 2024. Translation of non-functional currency monetary items – Profit after tax sensitivity to general movement of 1% Monetary items, including financial asset and liabilities, denominated in currencies other than the functional currency of an operation are revalued at the end of each reporting period to its functional currency and the associated gain or loss is taken to the profit or loss. The following chart is based on depreciation of the actual rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net monetary assets/liabilities denominated in non-functional currency of various Group entities. Amounts shown are rounded to the nearest US$m. The below sensitivity analysis is not representative of all the inherent foreign exchange risk as the year end exposure does not reflect the exposure during the year including transactional exposure in respect of non-functional currency revenue and expenses. The movement in the foreign exchange rates could vary from the sensitivity rate used. Further, the Group is exposed to foreign exchange volatility in emerging markets, such as Argentina, Turkey and Mexico. US$m 2025 2024 AUD EUR CHF GBP CNY -5 0 5 Translation of net investments in foreign operations – Equity sensitivity to general movement of 1% Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in the FCTR in equity. The following chart is based on depreciation of the actual exchange rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net assets/liabilities (excluding investments in subsidiaries) of the foreign currency denominated financial statements of various Group entities. Amounts shown are rounded to the nearest US$m. US$m 2025 2024 AUD EUR CHF GBP CNY 0 5 10 15 20 b. Interest Rate Risk As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to investments of cash and cash equivalents would have changed the Group’s profit after tax by approximately $15m (2024: $12m). This calculation is based on applying a 1% movement to the total of the Group’s cash and cash equivalents at year end. As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to floating rate unsecured bank loans would have changed the Group’s profit after tax by approximately $11m (2024: $16m). This calculation is based on applying a 1% movement to the total of the Group’s floating rate unsecured bank loans (excluding bank overdrafts) at year end. 111 111 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: risks

```text
Risk management approach The Group uses sensitivity analysis (together with other methods) to measure the extent of financial risks and decide if they need to be mitigated. If so, the Group’s policy is to use derivative financial instruments, such as foreign exchange contracts and interest rate swap and forward contracts, to support its objective of achieving financial targets while seeking to protect future financial security. The aim is to reduce the impact of short-term fluctuations in currency or interest rates on the Group’s earnings. Derivatives are exclusively used for this purpose and not as trading or other speculative instruments. a. Foreign Exchange Risk The US dollar is the predominant functional currency within the Group and as a result, currency exposures arise from transactions and balances in currencies other than the US dollar. The Group's potential currency exposures that could impact the profit or loss comprise: • translational exposure in respect of non-functional currency monetary items • transactional exposure in respect of non-functional currency expenditure and revenues • translational exposure in respect of non-USD functional currency expenditure and revenues to the Group's presentation currency (USD) The objective of management is to match the contracts with committed future cash flows from sales and purchases in foreign currencies to protect the Group against exchange rate movements. There are no material outstanding foreign exchange forward contracts at 30 June 2025 and 2024. Translation of non-functional currency monetary items – Profit after tax sensitivity to general movement of 1% Monetary items, including financial asset and liabilities, denominated in currencies other than the functional currency of an operation are revalued at the end of each reporting period to its functional currency and the associated gain or loss is taken to the profit or loss. The following chart is based on depreciation of the actual rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net monetary assets/liabilities denominated in non-functional currency of various Group entities. Amounts shown are rounded to the nearest US$m. The below sensitivity analysis is not representative of all the inherent foreign exchange risk as the year end exposure does not reflect the exposure during the year including transactional exposure in respect of non-functional currency revenue and expenses. The movement in the foreign exchange rates could vary from the sensitivity rate used. Further, the Group is exposed to foreign exchange volatility in emerging markets, such as Argentina, Turkey and Mexico. US$m 2025 2024 AUD EUR CHF GBP CNY -5 0 5 Translation of net investments in foreign operations – Equity sensitivity to general movement of 1% Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in the FCTR in equity. The following chart is based on depreciation of the actual exchange rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net assets/liabilities (excluding investments in subsidiaries) of the foreign currency denominated financial statements of various Group entities. Amounts shown are rounded to the nearest US$m. US$m 2025 2024 AUD EUR CHF GBP CNY 0 5 10 15 20 b. Interest Rate Risk As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to investments of cash and cash equivalents would have changed the Group’s profit after tax by approximately $15m (2024: $12m). This calculation is based on applying a 1% movement to the total of the Group’s cash and cash equivalents at year end. As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to floating rate unsecured bank loans would have changed the Group’s profit after tax by approximately $11m (2024: $16m). This calculation is based on applying a 1% movement to the total of the Group’s floating rate unsecured bank loans (excluding bank overdrafts) at year end. 111 111 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in the FCTR in equity. The following chart is based on depreciation of the actual exchange rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net assets/liabilities (excluding investments in subsidiaries) of the foreign currency denominated financial statements of various Group entities. Amounts shown are rounded to the nearest US$m. US$m 2025 2024 AUD EUR CHF GBP CNY 0 5 10 15 20 b. Interest Rate Risk As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to investments of cash and cash equivalents would have changed the Group’s profit after tax by approximately $15m (2024: $12m). This calculation is based on applying a 1% movement to the total of the Group’s cash and cash equivalents at year end. As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to floating rate unsecured bank loans would have changed the Group’s profit after tax by approximately $11m (2024: $16m). This calculation is based on applying a 1% movement to the total of the Group’s floating rate unsecured bank loans (excluding bank overdrafts) at year end. 111 111 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/113/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/113/

```text
CSL 2025 Annual Report – Page 113 1 112 Table of Contents 114 148 CSL 2025 Annual Report Risk management approach The Group uses sensitivity analysis (together with other methods) to measure the extent of financial risks and decide if they need to be mitigated. If so, the Group’s policy is to use derivative financial instruments, such as foreign exchange contracts and interest rate swap and forward contracts, to support its objective of achieving financial targets while seeking to protect future financial security. The aim is to reduce the impact of short-term fluctuations in currency or interest rates on the Group’s earnings. Derivatives are exclusively used for this purpose and not as trading or other speculative instruments. a. Foreign Exchange Risk The US dollar is the predominant functional currency within the Group and as a result, currency exposures arise from transactions and balances in currencies other than the US dollar. The Group's potential currency exposures that could impact the profit or loss comprise: • translational exposure in respect of non-functional currency monetary items • transactional exposure in respect of non-functional currency expenditure and revenues • translational exposure in respect of non-USD functional currency expenditure and revenues to the Group's presentation currency (USD) The objective of management is to match the contracts with committed future cash flows from sales and purchases in foreign currencies to protect the Group against exchange rate movements. There are no material outstanding foreign exchange forward contracts at 30 June 2025 and 2024. Translation of non-functional currency monetary items – Profit after tax sensitivity to general movement of 1% Monetary items, including financial asset and liabilities, denominated in currencies other than the functional currency of an operation are revalued at the end of each reporting period to its functional currency and the associated gain or loss is taken to the profit or loss. The following chart is based on depreciation of the actual rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net monetary assets/liabilities denominated in non-functional currency of various Group entities. Amounts shown are rounded to the nearest US$m. The below sensitivity analysis is not representative of all the inherent foreign exchange risk as the year end exposure does not reflect the exposure during the year including transactional exposure in respect of non-functional currency revenue and expenses. The movement in the foreign exchange rates could vary from the sensitivity rate used. Further, the Group is exposed to foreign exchange volatility in emerging markets, such as Argentina, Turkey and Mexico. US$m 2025 2024 AUD EUR CHF GBP CNY -5 0 5 Translation of net investments in foreign operations – Equity sensitivity to general movement of 1% Where the functional currency of a subsidiary is not US dollars, the subsidiary’s assets and liabilities are translated on consolidation to US dollars using the exchange rates prevailing at the reporting date, and its profit or loss is translated at average exchange rates. All resulting exchange differences are recognised in the FCTR in equity. The following chart is based on depreciation of the actual exchange rate of US dollars to AUD, EUR, CHF, GBP and CNY as at 30 June 2025 and 2024 by 1% and applying these adjusted rates to the net assets/liabilities (excluding investments in subsidiaries) of the foreign currency denominated financial statements of various Group entities. Amounts shown are rounded to the nearest US$m. US$m 2025 2024 AUD EUR CHF GBP CNY 0 5 10 15 20 b. Interest Rate Risk As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to investments of cash and cash equivalents would have changed the Group’s profit after tax by approximately $15m (2024: $12m). This calculation is based on applying a 1% movement to the total of the Group’s cash and cash equivalents at year end. As at 30 June 2025, it is estimated that a general movement of one percentage point in the interest rates applicable to floating rate unsecured bank loans would have changed the Group’s profit after tax by approximately $11m (2024: $16m). This calculation is based on applying a 1% movement to the total of the Group’s floating rate unsecured bank loans (excluding bank overdrafts) at year end. 111 111 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: revenue, income, NPAT

```text
income over the period of the borrowings. Borrowings are classified as current liabilities unless the Group has an unconditional right to defer settlement of the liability for at least 12 months after the reporting date. Lease liabilities The Group recognises lease liabilities measured at the present value of lease payments to be made over the lease term. In calculating the present value of lease payments, the Group uses the incremental borrowing rate of the lessee at the lease commencement date. The lease payments include fixed payments (including in-substance fixed payments, extension and purchase option reasonably certain to be exercised) less any lease incentives receivable, variable lease payments that depend on an index or a rate, and amounts expected to be paid under residual value guarantees. 113 113 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: cash, debt, gearing, capital

```text
debt on an undiscounted basis by facility (US$m). US$m Private Placement QDI Bank and Other Borrowings 144A FY26 FY27 FY28 FY29 FY30 FY31 FY32 FY33 FY34 FY35 FY38 FY42 FY52 FY54 FY62 0 250 500 750 1000 1250 1500 The following table analyses the Group’s interest-bearing liabilities and borrowings: 2025 2024 Interest-bearing liabilities and borrowings US$m US$m Current Bank overdraft – unsecured — 14 Bank and other borrowings – unsecured 282 571 Senior notes – unsecured 413 263 Lease liabilities 109 96 804 944 Non-current Bank and other borrowings – unsecured 1,222 1,393 Senior notes – unsecured 2,713 3,076 Senior 144A notes – unsecured 5,206 5,202 Lease liabilities 1,553 1,568 10,694 11,239 Interest-bearing liabilities and borrowings Interest-bearing liabilities and borrowings are recognised initially at fair value, net of transaction costs incurred. Subsequent to initial recognition, interest-bearing liabilities and borrowings are stated at amortised cost, with any difference between the proceeds (net of transaction costs) and the redemption value recognised in the statement of comprehensive income over the period of the borrowings. Borrowings are classified as current liabilities unless the Group has an unconditional right to defer settlement of the liability for at least 12 months after the reporting date. Lease liabilities The Group recognises lease liabilities measured at the present value of lease payments to be made over the lease term. In calculating the present value of lease payments, the Group uses the incremental borrowing rate of the lessee at the lease commencement date. The lease payments include fixed payments (including in-substance fixed payments, extension and purchase option reasonably certain to be exercised) less any lease incentives receivable, variable lease payments that depend on an index or a rate, and amounts expected to be paid under residual value guarantees. 113 113 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: risks

```text
Risk The following chart summarises the Group's maturity profile of debt on an undiscounted basis by facility (US$m). US$m Private Placement QDI Bank and Other Borrowings 144A FY26 FY27 FY28 FY29 FY30 FY31 FY32 FY33 FY34 FY35 FY38 FY42 FY52 FY54 FY62 0 250 500 750 1000 1250 1500 The following table analyses the Group’s interest-bearing liabilities and borrowings: 2025 2024 Interest-bearing liabilities and borrowings US$m US$m Current Bank overdraft – unsecured — 14 Bank and other borrowings – unsecured 282 571 Senior notes – unsecured 413 263 Lease liabilities 109 96 804 944 Non-current Bank and other borrowings – unsecured 1,222 1,393 Senior notes – unsecured 2,713 3,076 Senior 144A notes – unsecured 5,206 5,202 Lease liabilities 1,553 1,568 10,694 11,239 Interest-bearing liabilities and borrowings Interest-bearing liabilities and borrowings are recognised initially at fair value, net of transaction costs incurred. Subsequent to initial recognition, interest-bearing liabilities and borrowings are stated at amortised cost, with any difference between the proceeds (net of transaction costs) and the redemption value recognised in the statement of comprehensive income over the period of the borrowings. Borrowings are classified as current liabilities unless the Group has an unconditional right to defer settlement of the liability for at least 12 months after the reporting date. Lease liabilities The Group recognises lease liabilities measured at the present value of lease payments to be made over the lease term. In calculating the present value of lease payments, the Group uses the incremental borrowing rate of the lessee at the lease commencement date. The lease payments include fixed payments (including in-substance fixed payments, extension and purchase option reasonably certain to be exercised) less any lease incentives receivable, variable lease payments that depend on an index or a rate, and amounts expected to be paid under residual value guarantees. 113 113 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: debt, liquidity

```text
debt on an undiscounted basis by facility (US$m). US$m Private Placement QDI Bank and Other Borrowings 144A FY26 FY27 FY28 FY29 FY30 FY31 FY32 FY33 FY34 FY35 FY38 FY42 FY52 FY54 FY62 0 250 500 750 1000 1250 1500 The following table analyses the Group’s interest-bearing liabilities and borrowings: 2025 2024 Interest-bearing liabilities and borrowings US$m US$m Current Bank overdraft – unsecured — 14 Bank and other borrowings – unsecured 282 571 Senior notes – unsecured 413 263 Lease liabilities 109 96 804 944 Non-current Bank and other borrowings – unsecured 1,222 1,393 Senior notes – unsecured 2,713 3,076 Senior 144A notes – unsecured 5,206 5,202 Lease liabilities 1,553 1,568 10,694 11,239 Interest-bearing liabilities and borrowings Interest-bearing liabilities and borrowings are recognised initially at fair value, net of transaction costs incurred. Subsequent to initial recognition, interest-bearing liabilities and borrowings are stated at amortised cost, with any difference between the proceeds (net of transaction costs) and the redemption value recognised in the statement of comprehensive income over the period of the borrowings. Borrowings are classified as current liabilities unless the Group has an unconditional right to defer settlement of the liability for at least 12 months after the reporting date. Lease liabilities The Group recognises lease liabilities measured at the present value of lease payments to be made over the lease term. In calculating the present value of lease payments, the Group uses the incremental borrowing rate of the lessee at the lease commencement date. The lease payments include fixed payments (including in-substance fixed payments, extension and purchase option reasonably certain to be exercised) less any lease incentives receivable, variable lease payments that depend on an index or a rate, and amounts expected to be paid under residual value guarantees. 113 113 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/115/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/115/

```text
CSL 2025 Annual Report – Page 115 1 114 Table of Contents 116 148 CSL 2025 Annual Report d. Funding and Liquidity Risk The following chart summarises the Group's maturity profile of debt on an undiscounted basis by facility (US$m). US$m Private Placement QDI Bank and Other Borrowings 144A FY26 FY27 FY28 FY29 FY30 FY31 FY32 FY33 FY34 FY35 FY38 FY42 FY52 FY54 FY62 0 250 500 750 1000 1250 1500 The following table analyses the Group’s interest-bearing liabilities and borrowings: 2025 2024 Interest-bearing liabilities and borrowings US$m US$m Current Bank overdraft – unsecured — 14 Bank and other borrowings – unsecured 282 571 Senior notes – unsecured 413 263 Lease liabilities 109 96 804 944 Non-current Bank and other borrowings – unsecured 1,222 1,393 Senior notes – unsecured 2,713 3,076 Senior 144A notes – unsecured 5,206 5,202 Lease liabilities 1,553 1,568 10,694 11,239 Interest-bearing liabilities and borrowings Interest-bearing liabilities and borrowings are recognised initially at fair value, net of transaction costs incurred. Subsequent to initial recognition, interest-bearing liabilities and borrowings are stated at amortised cost, with any difference between the proceeds (net of transaction costs) and the redemption value recognised in the statement of comprehensive income over the period of the borrowings. Borrowings are classified as current liabilities unless the Group has an unconditional right to defer settlement of the liability for at least 12 months after the reporting date. Lease liabilities The Group recognises lease liabilities measured at the present value of lease payments to be made over the lease term. In calculating the present value of lease payments, the Group uses the incremental borrowing rate of the lessee at the lease commencement date. The lease payments include fixed payments (including in-substance fixed payments, extension and purchase option reasonably certain to be exercised) less any lease incentives receivable, variable lease payments that depend on an index or a rate, and amounts expected to be paid under residual value guarantees. 113 113 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: cash flow statement, operating cash flow

```text
cash flows, using rates currently available for debt of similar terms, credit risk and remaining maturities. Other financial liabilities also includes contingent consideration liabilities from past business combinations. These liabilities are recorded as non-current financial liabilities at fair value (Note 14), which are then remeasured at each subsequent reporting date at fair value through profit or loss. The fair value estimations typically depend on factors such as technical milestones or market performance, and are adjusted for the probability of their likelihood of potential future payments, and are appropriately discounted to reflect the impact of time. As at 30 June 2025, the maximum amount of undiscounted potential future milestone payments relating to historical business combinations ("contingent consideration liabilities from business combinations") are $470m (2024: $470m). Key Judgements and Estimates Contingent consideration liabilities are valued with reference to our judgement of the expected probability and timing of potential future milestone payments, based upon level 3 inputs under the fair value hierarchy, which is then discounted to a present value using appropriate discount rates with reference to the Group's incremental borrowing rates. Valuation of financial instruments Financial instruments measured and carried at fair value are categorised as follows: • Level 1: Items traded with quoted prices in active markets for identical liabilities • Level 2: Items with significantly observable inputs other than quoted prices in active markets • Level 3: Items with unobservable inputs (not based on observable market data) The group had the following financial assets and liabilities measured at fair value: 2025 2024 Financial assets/(liabilities) measured at fair value US$m US$m Publicly traded securities – FVOCI Level 1 35 12 Venture fund assets – FVTPL Level 3 140 126 Contingent consideration assets (earn-out receivable) Level 3 28 25 Contingent consideration liabilities from business combinations Level 3 (227) (220) There were no transfers between Level 1 and Level 2 during the year, or any transfers into Level 3. 115 115 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: cash, debt, gearing, capital

```text
debt. At 30 June 2025, the total fixed rate debt (excluding lease liabilities) has a carrying amount of $8,343m (2024: $8,180m) and a fair value of $7,687m (2024: $7,571m). Fair value is calculated based on the discounted expected principal and interest cash flows, using rates currently available for debt of similar terms, credit risk and remaining maturities. Other financial liabilities also includes contingent consideration liabilities from past business combinations. These liabilities are recorded as non-current financial liabilities at fair value (Note 14), which are then remeasured at each subsequent reporting date at fair value through profit or loss. The fair value estimations typically depend on factors such as technical milestones or market performance, and are adjusted for the probability of their likelihood of potential future payments, and are appropriately discounted to reflect the impact of time. As at 30 June 2025, the maximum amount of undiscounted potential future milestone payments relating to historical business combinations ("contingent consideration liabilities from business combinations") are $470m (2024: $470m). Key Judgements and Estimates Contingent consideration liabilities are valued with reference to our judgement of the expected probability and timing of potential future milestone payments, based upon level 3 inputs under the fair value hierarchy, which is then discounted to a present value using appropriate discount rates with reference to the Group's incremental borrowing rates. Valuation of financial instruments Financial instruments measured and carried at fair value are categorised as follows: • Level 1: Items traded with quoted prices in active markets for identical liabilities • Level 2: Items with significantly observable inputs other than quoted prices in active markets • Level 3: Items with unobservable inputs (not based on observable market data) The group had the following financial assets and liabilities measured at fair value: 2025 2024 Financial assets/(liabilities) measured at fair value US$m US$m Publicly traded securities – FVOCI Level 1 35 12 Venture fund assets – FVTPL Level 3 140 126 Contingent consideration assets (earn-out receivable) Level 3 28 25 Contingent consideration liabilities from business combinations Level 3 (227) (220) There were no transfers between Level 1 and Level 2 during the year, or any transfers into Level 3. 115 115 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: risks

```text
risk and remaining maturities. Other financial liabilities also includes contingent consideration liabilities from past business combinations. These liabilities are recorded as non-current financial liabilities at fair value (Note 14), which are then remeasured at each subsequent reporting date at fair value through profit or loss. The fair value estimations typically depend on factors such as technical milestones or market performance, and are adjusted for the probability of their likelihood of potential future payments, and are appropriately discounted to reflect the impact of time. As at 30 June 2025, the maximum amount of undiscounted potential future milestone payments relating to historical business combinations ("contingent consideration liabilities from business combinations") are $470m (2024: $470m). Key Judgements and Estimates Contingent consideration liabilities are valued with reference to our judgement of the expected probability and timing of potential future milestone payments, based upon level 3 inputs under the fair value hierarchy, which is then discounted to a present value using appropriate discount rates with reference to the Group's incremental borrowing rates. Valuation of financial instruments Financial instruments measured and carried at fair value are categorised as follows: • Level 1: Items traded with quoted prices in active markets for identical liabilities • Level 2: Items with significantly observable inputs other than quoted prices in active markets • Level 3: Items with unobservable inputs (not based on observable market data) The group had the following financial assets and liabilities measured at fair value: 2025 2024 Financial assets/(liabilities) measured at fair value US$m US$m Publicly traded securities – FVOCI Level 1 35 12 Venture fund assets – FVTPL Level 3 140 126 Contingent consideration assets (earn-out receivable) Level 3 28 25 Contingent consideration liabilities from business combinations Level 3 (227) (220) There were no transfers between Level 1 and Level 2 during the year, or any transfers into Level 3. 115 115 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
assets Other financial assets include equity securities (publicly traded securities) carried at fair value through OCI (FVOCI) which are not held for trading. The value of the publicly traded securities depends on the share price quoted on the corresponding stock exchange. The Group also has investments in venture funds which are not publicly traded and are carried at fair value through the profit or loss (FVTPL). The value of the venture funds depends on the net asset value of the underlying investments and not directly on a share index. Other financial assets also includes an earn-out receivable acquired from a past business combination. The earn-out will become due based on a variety of factors including future earnings over a period of seven years ending 30 June 2028. The receivable is classified as a financial asset and is remeasured at each reporting period at FVTPL. Interest-bearing and other financial liabilities The carrying amount of the interest-bearing liabilities approximates the fair value, with the exception of the Group's fixed interest rate debt. At 30 June 2025, the total fixed rate debt (excluding lease liabilities) has a carrying amount of $8,343m (2024: $8,180m) and a fair value of $7,687m (2024: $7,571m). Fair value is calculated based on the discounted expected principal and interest cash flows, using rates currently available for debt of similar terms, credit risk and remaining maturities. Other financial liabilities also includes contingent consideration liabilities from past business combinations. These liabilities are recorded as non-current financial liabilities at fair value (Note 14), which are then remeasured at each subsequent reporting date at fair value through profit or loss. The fair value estimations typically depend on factors such as technical milestones or market performance, and are adjusted for the probability of their likelihood of potential future payments, and are appropriately discounted to reflect the impact of time. As at 30 June 2025, the maximum amount of undiscounted potential future milestone payments relating to historical business combinations ("contingent consideration liabilities from business combinations") are $470m (2024: $470m). Key Judgements and Estimates Contingent consideration liabilities are valued with reference to our judgement of the expected probability and timing of potential future milestone payments, based upon level 3 inputs under the fair value hierarchy, which is then discounted to a present value using appropriate discount rates with reference to the Group's incremental borrowing rates. Valuation of financial instruments Financial instruments measured and carried at fair value are categorised as follows: • Level 1: Items traded with quoted prices in active markets for identical liabilities • Level 2: Items with significantly observable inputs other than quoted prices in active markets • Level 3: Items with unobservable inputs (not based on observable market data) The group had the following financial assets and liabilities measured at fair value: 2025 2024 Financial assets/(liabilities) measured at fair value US$m US$m Publicly traded securities – FVOCI Level 1 35 12 Venture fund assets – FVTPL Level 3 140 126 Contingent consideration assets (earn-out receivable) Level 3 28 25 Contingent consideration liabilities from business combinations Level 3 (227) (220) There were no transfers between Level 1 and Level 2 during the year, or any transfers into Level 3. 115 115 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: debt, liquidity

```text
debt. At 30 June 2025, the total fixed rate debt (excluding lease liabilities) has a carrying amount of $8,343m (2024: $8,180m) and a fair value of $7,687m (2024: $7,571m). Fair value is calculated based on the discounted expected principal and interest cash flows, using rates currently available for debt of similar terms, credit risk and remaining maturities. Other financial liabilities also includes contingent consideration liabilities from past business combinations. These liabilities are recorded as non-current financial liabilities at fair value (Note 14), which are then remeasured at each subsequent reporting date at fair value through profit or loss. The fair value estimations typically depend on factors such as technical milestones or market performance, and are adjusted for the probability of their likelihood of potential future payments, and are appropriately discounted to reflect the impact of time. As at 30 June 2025, the maximum amount of undiscounted potential future milestone payments relating to historical business combinations ("contingent consideration liabilities from business combinations") are $470m (2024: $470m). Key Judgements and Estimates Contingent consideration liabilities are valued with reference to our judgement of the expected probability and timing of potential future milestone payments, based upon level 3 inputs under the fair value hierarchy, which is then discounted to a present value using appropriate discount rates with reference to the Group's incremental borrowing rates. Valuation of financial instruments Financial instruments measured and carried at fair value are categorised as follows: • Level 1: Items traded with quoted prices in active markets for identical liabilities • Level 2: Items with significantly observable inputs other than quoted prices in active markets • Level 3: Items with unobservable inputs (not based on observable market data) The group had the following financial assets and liabilities measured at fair value: 2025 2024 Financial assets/(liabilities) measured at fair value US$m US$m Publicly traded securities – FVOCI Level 1 35 12 Venture fund assets – FVTPL Level 3 140 126 Contingent consideration assets (earn-out receivable) Level 3 28 25 Contingent consideration liabilities from business combinations Level 3 (227) (220) There were no transfers between Level 1 and Level 2 during the year, or any transfers into Level 3. 115 115 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/117/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/117/

```text
CSL 2025 Annual Report – Page 117 1 116 Table of Contents 118 148 CSL 2025 Annual Report Other financial assets Other financial assets include equity securities (publicly traded securities) carried at fair value through OCI (FVOCI) which are not held for trading. The value of the publicly traded securities depends on the share price quoted on the corresponding stock exchange. The Group also has investments in venture funds which are not publicly traded and are carried at fair value through the profit or loss (FVTPL). The value of the venture funds depends on the net asset value of the underlying investments and not directly on a share index. Other financial assets also includes an earn-out receivable acquired from a past business combination. The earn-out will become due based on a variety of factors including future earnings over a period of seven years ending 30 June 2028. The receivable is classified as a financial asset and is remeasured at each reporting period at FVTPL. Interest-bearing and other financial liabilities The carrying amount of the interest-bearing liabilities approximates the fair value, with the exception of the Group's fixed interest rate debt. At 30 June 2025, the total fixed rate debt (excluding lease liabilities) has a carrying amount of $8,343m (2024: $8,180m) and a fair value of $7,687m (2024: $7,571m). Fair value is calculated based on the discounted expected principal and interest cash flows, using rates currently available for debt of similar terms, credit risk and remaining maturities. Other financial liabilities also includes contingent consideration liabilities from past business combinations. These liabilities are recorded as non-current financial liabilities at fair value (Note 14), which are then remeasured at each subsequent reporting date at fair value through profit or loss. The fair value estimations typically depend on factors such as technical milestones or market performance, and are adjusted for the probability of their likelihood of potential future payments, and are appropriately discounted to reflect the impact of time. As at 30 June 2025, the maximum amount of undiscounted potential future milestone payments relating to historical business combinations ("contingent consideration liabilities from business combinations") are $470m (2024: $470m). Key Judgements and Estimates Contingent consideration liabilities are valued with reference to our judgement of the expected probability and timing of potential future milestone payments, based upon level 3 inputs under the fair value hierarchy, which is then discounted to a present value using appropriate discount rates with reference to the Group's incremental borrowing rates. Valuation of financial instruments Financial instruments measured and carried at fair value are categorised as follows: • Level 1: Items traded with quoted prices in active markets for identical liabilities • Level 2: Items with significantly observable inputs other than quoted prices in active markets • Level 3: Items with unobservable inputs (not based on observable market data) The group had the following financial assets and liabilities measured at fair value: 2025 2024 Financial assets/(liabilities) measured at fair value US$m US$m Publicly traded securities – FVOCI Level 1 35 12 Venture fund assets – FVTPL Level 3 140 126 Contingent consideration assets (earn-out receivable) Level 3 28 25 Contingent consideration liabilities from business combinations Level 3 (227) (220) There were no transfers between Level 1 and Level 2 during the year, or any transfers into Level 3. 115 115 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: EPS, DPS, dividends

```text
EPS growth and Return on Invested Capital (ROIC). • The Retain and Grow Plan (RGP) grants Restricted Share Units (RSU) to qualifying employees. Participation in the RGP plan is broader than in the EPA plan. Vesting is subject to continuing employment and satisfactory performance. EPA grants generally vest on their third anniversary. RGP grants generally vest in equal tranches on their first, second and third anniversaries of the grant. For EPA and RGP commencement benefit awards, vesting dates are reviewed and determined on a case by case basis and will vary. A face value equity allocation methodology, being a five day volume weighted average share price based on the market price of a CSL share at the time of grant is used to determine the number of units granted to a participant. There is no exercise price payable on PSUs and RSUs. The fair value of the awards granted is estimated at the date of grant using an adjusted form of the Black-Scholes model, considering the terms and conditions upon which the PSUs and RSUs were granted. The following RGP and EPA grants were issued during the year ended 30 June 2025: Date of grant PSUs RSUs 1 September 2024 230,341 829,884 1 March 2025 674 20,737 The Non-Executive Directors Plan The Non-Executive Directors (NED) pay a minimum of 20% of their pre-tax base fee in return for a grant of rights, each right entitling a NED to acquire one CSL share at no cost (shares purchased on market). There is a nominated restriction period of three to fifteen years, after which the NED will have access to their shares. On 21 August 2024 and 19 February 2025, a total of 2,721 rights were granted under the NED Rights Plan with vesting through to August 2025. Global Employee Share Plan The Global Employee Share Plan (GESP) allows employees to make contributions from post-tax salary up to a maximum of A$12,000 (or equivalent) per six month contribution period. Employees receive shares at a 15% discount to the applicable market rate over the five day period up to and including the first and last ASX trading days of the six month period, whichever is the lower. Recognition and measurement The fair value of awards granted are recognised as an employee benefit expense with a corresponding increase in equity. Fair value is independently measured at grant date and recognised over the period during which the employees become unconditionally entitled to the award. Fair value is independently determined using a combination of the Binomial and Black-Scholes valuation methodologies, including Monte Carlo simulation, considering the terms and conditions on which the awards were granted. The fair value of the awards granted excludes the impact of any non-market vesting conditions, which are included in assumptions about the number of awards that are expected to vest. At each reporting date, the number of awards that are expected to vest is revised. The employee benefit expense recognised each period considers the most recent estimate of the number of awards that are expected to vest. No expense is recognised for awards that do not ultimately vest, except where the vesting is conditional upon a market condition and that market condition is not met. The Group does not have any awards with a market condition as at 30 June 2025. 123 123 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/125/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/125/

```text
CSL 2025 Annual Report – Page 125 1 124 Table of Contents 126 148 CSL 2025 Annual Report b. Share-based payments Long Term Incentives CSL has the following awards available under its shared-based payment plans: • The Executive Performance and Alignment Plan (EPA) grants Performance Share Units (PSU) to qualifying executives. Vesting is subject to continuing employment, satisfactory performance and achievement of absolute return measures which include EPS growth and Return on Invested Capital (ROIC). • The Retain and Grow Plan (RGP) grants Restricted Share Units (RSU) to qualifying employees. Participation in the RGP plan is broader than in the EPA plan. Vesting is subject to continuing employment and satisfactory performance. EPA grants generally vest on their third anniversary. RGP grants generally vest in equal tranches on their first, second and third anniversaries of the grant. For EPA and RGP commencement benefit awards, vesting dates are reviewed and determined on a case by case basis and will vary. A face value equity allocation methodology, being a five day volume weighted average share price based on the market price of a CSL share at the time of grant is used to determine the number of units granted to a participant. There is no exercise price payable on PSUs and RSUs. The fair value of the awards granted is estimated at the date of grant using an adjusted form of the Black-Scholes model, considering the terms and conditions upon which the PSUs and RSUs were granted. The following RGP and EPA grants were issued during the year ended 30 June 2025: Date of grant PSUs RSUs 1 September 2024 230,341 829,884 1 March 2025 674 20,737 The Non-Executive Directors Plan The Non-Executive Directors (NED) pay a minimum of 20% of their pre-tax base fee in return for a grant of rights, each right entitling a NED to acquire one CSL share at no cost (shares purchased on market). There is a nominated restriction period of three to fifteen years, after which the NED will have access to their shares. On 21 August 2024 and 19 February 2025, a total of 2,721 rights were granted under the NED Rights Plan with vesting through to August 2025. Global Employee Share Plan The Global Employee Share Plan (GESP) allows employees to make contributions from post-tax salary up to a maximum of A$12,000 (or equivalent) per six month contribution period. Employees receive shares at a 15% discount to the applicable market rate over the five day period up to and including the first and last ASX trading days of the six month period, whichever is the lower. Recognition and measurement The fair value of awards granted are recognised as an employee benefit expense with a corresponding increase in equity. Fair value is independently measured at grant date and recognised over the period during which the employees become unconditionally entitled to the award. Fair value is independently determined using a combination of the Binomial and Black-Scholes valuation methodologies, including Monte Carlo simulation, considering the terms and conditions on which the awards were granted. The fair value of the awards granted excludes the impact of any non-market vesting conditions, which are included in assumptions about the number of awards that are expected to vest. At each reporting date, the number of awards that are expected to vest is revised. The employee benefit expense recognised each period considers the most recent estimate of the number of awards that are expected to vest. No expense is recognised for awards that do not ultimately vest, except where the vesting is conditional upon a market condition and that market condition is not met. The Group does not have any awards with a market condition as at 30 June 2025. 123 123 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: cash, debt, gearing, capital

```text
Cash and cash equivalents 178 189 Receivables and contract assets 543 557 Inventories 363 297 Total Current Assets 1,084 1,043 NON-CURRENT ASSETS Property, plant and equipment 2,232 2,105 Deferred tax assets 157 136 Intangible assets 41 23 Retirement benefit assets 3 2 Other financial assets 18,796 18,866 Other non-current assets 189 2,003 Total Non-Current assets 21,418 23,135 TOTAL ASSETS 22,502 24,178 CURRENT LIABILITIES Trade and other payables 453 606 Provisions 77 58 Interest-bearing liabilities and borrowings 320 163 Other current liabilities 2 — Total Current Liabilities 852 827 NON-CURRENT LIABILITIES Trade and other payables 915 2,315 Interest-bearing liabilities and borrowings 1,146 1,340 Provisions 48 46 Other non-current liabilities 27 25 Total Non-Current Liabilities 2,136 3,726 TOTAL LIABILITIES 2,988 4,553 NET ASSETS 19,514 19,625 EQUITY Contributed equity 574 557 Reserves 523 574 Retained earnings 18,417 18,494 TOTAL EQUITY 19,514 19,625 2025 2024 Summary of movements in retained earnings of the Consolidated Closed Group US$m US$m Retained earnings at beginning of the financial year 18,494 18,084 Net profit for the year 1,257 1,602 Dividends paid to CSL Limited shareholders (1,334) (1,192) Retained earnings at the end of the financial year 18,417 18,494 127 127 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
ASSETS Cash and cash equivalents 178 189 Receivables and contract assets 543 557 Inventories 363 297 Total Current Assets 1,084 1,043 NON-CURRENT ASSETS Property, plant and equipment 2,232 2,105 Deferred tax assets 157 136 Intangible assets 41 23 Retirement benefit assets 3 2 Other financial assets 18,796 18,866 Other non-current assets 189 2,003 Total Non-Current assets 21,418 23,135 TOTAL ASSETS 22,502 24,178 CURRENT LIABILITIES Trade and other payables 453 606 Provisions 77 58 Interest-bearing liabilities and borrowings 320 163 Other current liabilities 2 — Total Current Liabilities 852 827 NON-CURRENT LIABILITIES Trade and other payables 915 2,315 Interest-bearing liabilities and borrowings 1,146 1,340 Provisions 48 46 Other non-current liabilities 27 25 Total Non-Current Liabilities 2,136 3,726 TOTAL LIABILITIES 2,988 4,553 NET ASSETS 19,514 19,625 EQUITY Contributed equity 574 557 Reserves 523 574 Retained earnings 18,417 18,494 TOTAL EQUITY 19,514 19,625 2025 2024 Summary of movements in retained earnings of the Consolidated Closed Group US$m US$m Retained earnings at beginning of the financial year 18,494 18,084 Net profit for the year 1,257 1,602 Dividends paid to CSL Limited shareholders (1,334) (1,192) Retained earnings at the end of the financial year 18,417 18,494 127 127 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: debt, liquidity

```text
borrowings 320 163 Other current liabilities 2 — Total Current Liabilities 852 827 NON-CURRENT LIABILITIES Trade and other payables 915 2,315 Interest-bearing liabilities and borrowings 1,146 1,340 Provisions 48 46 Other non-current liabilities 27 25 Total Non-Current Liabilities 2,136 3,726 TOTAL LIABILITIES 2,988 4,553 NET ASSETS 19,514 19,625 EQUITY Contributed equity 574 557 Reserves 523 574 Retained earnings 18,417 18,494 TOTAL EQUITY 19,514 19,625 2025 2024 Summary of movements in retained earnings of the Consolidated Closed Group US$m US$m Retained earnings at beginning of the financial year 18,494 18,084 Net profit for the year 1,257 1,602 Dividends paid to CSL Limited shareholders (1,334) (1,192) Retained earnings at the end of the financial year 18,417 18,494 127 127 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/129/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/129/

```text
CSL 2025 Annual Report – Page 129 1 128 Table of Contents 130 148 CSL 2025 Annual Report Consolidated Closed Group 2025 2024 Balance Sheet US$m US$m CURRENT ASSETS Cash and cash equivalents 178 189 Receivables and contract assets 543 557 Inventories 363 297 Total Current Assets 1,084 1,043 NON-CURRENT ASSETS Property, plant and equipment 2,232 2,105 Deferred tax assets 157 136 Intangible assets 41 23 Retirement benefit assets 3 2 Other financial assets 18,796 18,866 Other non-current assets 189 2,003 Total Non-Current assets 21,418 23,135 TOTAL ASSETS 22,502 24,178 CURRENT LIABILITIES Trade and other payables 453 606 Provisions 77 58 Interest-bearing liabilities and borrowings 320 163 Other current liabilities 2 — Total Current Liabilities 852 827 NON-CURRENT LIABILITIES Trade and other payables 915 2,315 Interest-bearing liabilities and borrowings 1,146 1,340 Provisions 48 46 Other non-current liabilities 27 25 Total Non-Current Liabilities 2,136 3,726 TOTAL LIABILITIES 2,988 4,553 NET ASSETS 19,514 19,625 EQUITY Contributed equity 574 557 Reserves 523 574 Retained earnings 18,417 18,494 TOTAL EQUITY 19,514 19,625 2025 2024 Summary of movements in retained earnings of the Consolidated Closed Group US$m US$m Retained earnings at beginning of the financial year 18,494 18,084 Net profit for the year 1,257 1,602 Dividends paid to CSL Limited shareholders (1,334) (1,192) Retained earnings at the end of the financial year 18,417 18,494 127 127 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: margins

```text
margins realised. Given the significant value of inventories, global distribution, intra-group transactions, including the complexity involved in eliminating unrealised profits, and judgements in determining whether inventory is carried at the lower of cost and net realisable value, we consider the existence and valuation of inventories to be a key audit matter. Our procedures included, but were not limited to: • Understanding the policies, processes and relevant controls that management has in place in respect of the existence and valuation of inventory; • Assessing the existence of inventory and recording any resulting adjustments by: o Understanding the Group’s stock take procedures. o Confirming the physical existence of inventory, including attendance at stock takes. o Evaluating the results from stock takes performed and validating that variances have been appropriately recognised. • Assessing the valuation of inventory by: o Assessing the determination of inventory cost, including evaluating the appropriateness of standard costs and the recognition of variances between standard and actual costs. o Evaluating the carrying value of inventories, including any provisions required, to ensure inventory is carried at the lower of cost and net realisable value at 30 June 2025. o Assessing the Group’s transfer pricing principles and recalculating the resulting elimination of unrealised profit on sale of inventories between group entities. We also assessed the adequacy of the disclosures in Note 5 to the financial statements. Other Information The directors are responsible for the other information. The other information comprises the information included in the Group’s annual report for the year ended 30 June 2025 but does not include the financial report and our auditor’s report thereon. Our opinion on the financial report does not cover the other information and we do not express any form of assurance conclusion thereon, with the exception of the Remuneration Report and our related assurance opinion. 135 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/137/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/137/

```text
CSL 2025 Annual Report – Page 137 1 136 Table of Contents 138 148 CSL 2025 Annual Report Key Audit Matter How the scope of our audit responded to the Key Audit Matter Existence and valuation of inventory including the elimination of intergroup profit. Refer to Note 5 Inventories At 30 June 2025, the carrying value of the Group’s inventories, which are recorded at the lower of cost and net realisable value, was $6,466 million. Inventory is held at a number of geographically diverse locations across the globe, some of which are managed by third parties. The Group’s accounting for inventories is complex due to the nature of products being manufactured requiring multiple inputs into the determination of cost and the need to ensure the effect of intragroup inventory sales and the capitalisation and amortisation of purchase price and other manufacturing variances within the Group, are appropriately considered in the determination of costs. Furthermore, inventory provisions may be recognised in relation to raw materials, work in progress and finished goods based on a number of factors including expiry dates, selling prices and margins realised. Given the significant value of inventories, global distribution, intra-group transactions, including the complexity involved in eliminating unrealised profits, and judgements in determining whether inventory is carried at the lower of cost and net realisable value, we consider the existence and valuation of inventories to be a key audit matter. Our procedures included, but were not limited to: • Understanding the policies, processes and relevant controls that management has in place in respect of the existence and valuation of inventory; • Assessing the existence of inventory and recording any resulting adjustments by: o Understanding the Group’s stock take procedures. o Confirming the physical existence of inventory, including attendance at stock takes. o Evaluating the results from stock takes performed and validating that variances have been appropriately recognised. • Assessing the valuation of inventory by: o Assessing the determination of inventory cost, including evaluating the appropriateness of standard costs and the recognition of variances between standard and actual costs. o Evaluating the carrying value of inventories, including any provisions required, to ensure inventory is carried at the lower of cost and net realisable value at 30 June 2025. o Assessing the Group’s transfer pricing principles and recalculating the resulting elimination of unrealised profit on sale of inventories between group entities. We also assessed the adequacy of the disclosures in Note 5 to the financial statements. Other Information The directors are responsible for the other information. The other information comprises the information included in the Group’s annual report for the year ended 30 June 2025 but does not include the financial report and our auditor’s report thereon. Our opinion on the financial report does not cover the other information and we do not express any form of assurance conclusion thereon, with the exception of the Remuneration Report and our related assurance opinion. 135 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: management discussion, MD&A, outlook
- Unavailable reason: management_discussion_analysis was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: cash flow statement, operating cash flow
- Unavailable reason: cash_flow_statement was not identified in extracted ASX document text.

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: cash, debt, gearing, capital
- Unavailable reason: cash_debt_gearing was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: segment performance, sector metrics
- Unavailable reason: segment_product_performance was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: outlook, management commentary
- Unavailable reason: management_commentary_outlook was not identified in extracted ASX document text.

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: dividends, capital management
- Unavailable reason: dividends_capital_management was not identified in extracted ASX document text.

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: capex, commitments
- Unavailable reason: capex_commitments was not identified in extracted ASX document text.

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: risks
- Unavailable reason: material_risks was not identified in extracted ASX document text.

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement
- Unavailable reason: financial_statement_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: segment table, product table, sector metrics
- Unavailable reason: segment_product_tables was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_segment_revenue
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: segment revenue
- Unavailable reason: segment revenue was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_r_and_d
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: R&D
- Unavailable reason: R&D was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_plasma_collections
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: plasma collections
- Unavailable reason: plasma collections was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_margins
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: margins
- Unavailable reason: margin was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_debt
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: debt, liquidity
- Unavailable reason: net debt was not identified in extracted ASX document text.

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_guidance
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2024-12-31`
- URL: https://investors.csl.com/annualreport/2025/139/
- Supports claims: guidance, outlook
- Unavailable reason: guidance was not identified in extracted ASX document text.

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://investors.csl.com/annualreport/2025/139/

```text
CSL 2025 Annual Report – Page 139 1 138 Table of Contents 140 148 CSL 2025 Annual Report • Evaluate the overall presentation, structure and content of the financial report, including the disclosures, and whether the financial report represents the underlying transactions and events in a manner that achieves fair presentation. • Plan and perform the group audit to obtain sufficient appropriate audit evidence regarding the financial information of the entities or business activities within the Group as a basis for forming an opinion on the Group financial report. We are responsible for the direction, supervision and review of the audit work performed for the purposes of the group audit. We remain solely responsible for our audit opinion. We communicate with the directors regarding, among other matters, the planned scope and timing of the audit and significant audit findings, including any significant deficiencies in internal control that we identify during our audit. We also provide the directors with a statement that we have complied with relevant ethical requirements regarding independence, and to communicate with them all relationships and other matters that may reasonably be thought to bear on our independence, and where applicable, actions taken to eliminate threats or safeguards applied. From the matters communicated with the directors, we determine those matters that were of most significance in the audit of the financial report of the current period and are therefore the key audit matters. We describe these matters in our auditor’s report unless law or regulation precludes public disclosure about the matter or when, in extremely rare circumstances, we determine that a matter should not be communicated in our report because the adverse consequences of doing so would reasonably be expected to outweigh the public interest benefits of such communication. Report on the Remuneration Report Opinion on the Remuneration Report We have audited the Remuneration Report included in the Directors’ Report for the year ended 30 June 2025. In our opinion, the Remuneration Report of CSL Limited, for the year ended 30 June 2025, complies with section 300A of the Corporations Act 2001. Responsibilities The directors of the Company are responsible for the preparation and presentation of the Remuneration Report in accordance with section 300A of the Corporations Act 2001. Our responsibility is to express an opinion on the Remuneration Report, based on our audit conducted in accordance with Australian Auditing Standards. DELOITTE TOUCHE TOHMATSU Andrew Griffiths Genevra Cavallo Partner Partner Chartered Accountants Chartered Accountants Sydney, NSW Melbourne, VIC 18 August 2025 18 August 2025 137 CSL Limited Annual Report 2024/25 Made with FlippingBook RkJQdWJsaXNoZXIy MjE2NDg3
```

```
