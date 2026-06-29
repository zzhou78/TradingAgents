# Codex Role Evidence Packet: CSL.AX

- Trade date: `2026-06-27`
- Instrument identity: `CSL Limited`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for CSL.AX from 2026-05-28 to 2026-06-27
# Total records: 21
# Data retrieved on: 2026-06-29 13:53:50

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-05-28,97.8,98.29,97.1,97.59,1491376,0.0,0.0
2026-05-29,96.4,97.56,95.16,96.61,5891391,0.0,0.0
2026-06-01,97.95,98.79,93.74,94.2,1773731,0.0,0.0
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

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for CSL.AX

- Requested analysis date: 2026-06-27
- Latest trading row used: 2026-06-26
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 114.60 |
| High | 117.14 |
| Low | 114.39 |
| Close | 114.87 |
| Volume | 2308629 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 111.76 |
| close_50_sma | 110.56 |
| close_200_sma | 156.86 |
| rsi | 60.29 |
| boll | 104.93 |
| boll_ub | 121.89 |
| boll_lb | 87.97 |
| macd | 2.32 |
| macds | 0.24 |
| macdh | 2.09 |
| atr | 3.86 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-15 | 97.96 |
| 2026-05-18 | 96.22 |
| 2026-05-19 | 98.69 |
| 2026-05-20 | 98.47 |
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

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-05-28 to 2026-06-27:

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
2026-06-01: 122.86880020141602
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 123.67720016479493
2026-05-28: 124.5050001525879


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-05-28 to 2026-06-27:

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
2026-06-05: 163.7085082244873
2026-06-04: 164.32176399230957
2026-06-03: 164.93595283508301
2026-06-02: 165.57511882781984
2026-06-01: 166.43627147674562
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 167.2845882034302
2026-05-28: 168.11953762054443


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-05-28 to 2026-06-27:

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
2026-06-05: 37.15892842808835
2026-06-04: 21.949736368835353
2026-06-03: 20.77841702501458
2026-06-02: 21.04656898657673
2026-06-01: 22.423733698461092
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 24.622205297260976
2026-05-28: 25.56875700784208


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-05-28 to 2026-06-27:

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
2026-06-05: -7.034740195266352
2026-06-04: -7.704175580714292
2026-06-03: -7.904884354864265
2026-06-02: -8.010445391343481
2026-06-01: -8.061245877503183
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: -8.175813041292983
2026-05-28: -8.448503677162478


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-05-28 to 2026-06-27:

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
2026-06-05: 3.333289420063269
2026-06-04: 3.1804649658974626
2026-06-03: 3.294346534225212
2026-06-02: 3.3508349169660927
2026-06-01: 3.4255147372390247
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 3.300554097660655
2026-05-28: 3.3675203608821476


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
## CSL.AX News, from 2026-06-20 to 2026-06-27:

### European Regulator Calls for Amgen’s Tavneos to Have Authorization Revoked (source: The Wall Street Journal)
The committee is recommending that no new patients start treatment with Tavneos and that existing patients be switched to suitable alternatives.
Link: https://www.wsj.com/health/pharma/european-regulator-calls-for-amgens-tavneos-to-have-authorization-revoked-b3922308?siteid=yhoof2&yptr=yahoo


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-20 and 2026-06-27
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for CSL.AX
# Data retrieved on: 2026-06-29 13:54:09

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
42,2114,,,,Schmeltz (Andy),Other Executive,,2024-06-30,D
43,396,,,,Linton (Joy),Chief Financial Officer,,2024-06-30,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for CSL.AX
# Data retrieved on: 2026-06-29 13:54:09

Name: CSL Limited
Sector: Healthcare
Industry: Biotechnology
Market Cap: 55644782592
PE Ratio (TTM): 12.982123
Forward PE: 12.506229
PEG Ratio: 1.82
Price to Book: 2.069857
EPS (TTM): 8.95
Forward EPS: 9.29057
Dividend Yield: 3.71
Beta: 0.094
52 Week High: 275.79
52 Week Low: 90.0
50 Day Average: 109.778
200 Day Average: 157.1502
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
Book Value: 56.13432
Free Cash Flow: 1848125056
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for CSL.AX (quarterly)
# Data retrieved on: 2026-06-29 13:54:09

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
# Data retrieved on: 2026-06-29 13:54:10

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
# Data retrieved on: 2026-06-29 13:54:10

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

- Status: `error`

```text
## Financial Document Source Packet: CSL.AX

- Trade date: `2026-06-27`
- Collection status: `error`
- Market: `ASX`
- ASX code: `CSL`

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_announcements | error |  |  | HTTP Error 404:  |

```
