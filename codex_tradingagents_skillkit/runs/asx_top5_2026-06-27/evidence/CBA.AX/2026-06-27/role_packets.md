# Codex Role Evidence Packet: CBA.AX

- Trade date: `2026-06-27`
- Instrument identity: `Commonwealth Bank of Australia`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for CBA.AX from 2026-05-28 to 2026-06-27
# Total records: 21
# Data retrieved on: 2026-06-29 13:53:29

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-05-28,163.0,163.83,160.24,161.41,2007173,0.0,0.0
2026-05-29,161.8,165.02,161.5,165.02,11194839,0.0,0.0
2026-06-01,163.61,164.29,162.07,163.3,1592801,0.0,0.0
2026-06-02,161.0,163.29,160.14,163.0,2110667,0.0,0.0
2026-06-03,163.75,165.44,162.96,164.76,1780123,0.0,0.0
2026-06-04,164.86,164.89,161.7,163.73,1528064,0.0,0.0
2026-06-05,164.48,164.48,160.0,160.9,2383963,0.0,0.0
2026-06-09,160.43,161.96,158.32,160.48,2993060,0.0,0.0
2026-06-10,159.92,161.5,158.8,160.24,2717126,0.0,0.0
2026-06-11,158.6,159.09,156.42,156.42,2555692,0.0,0.0
2026-06-12,158.16,160.3,157.71,159.51,1819896,0.0,0.0
2026-06-15,160.0,162.6,159.91,161.79,1736947,0.0,0.0
2026-06-16,159.25,162.22,158.21,161.88,1409081,0.0,0.0
2026-06-17,162.0,164.17,161.6,163.71,1958334,0.0,0.0
2026-06-18,164.42,165.45,161.92,162.23,2730130,0.0,0.0
2026-06-19,162.15,162.4,160.34,162.4,4968164,0.0,0.0
2026-06-22,162.4,164.13,162.33,163.41,1520823,0.0,0.0
2026-06-23,163.5,164.9,163.06,164.21,2277025,0.0,0.0
2026-06-24,166.38,167.39,164.27,164.79,2754085,0.0,0.0
2026-06-25,164.79,165.65,162.64,162.7,2761711,0.0,0.0
2026-06-26,162.0,163.2,161.28,162.02,2280044,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for CBA.AX

- Requested analysis date: 2026-06-27
- Latest trading row used: 2026-06-26
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 162.00 |
| High | 163.20 |
| Low | 161.28 |
| Close | 162.02 |
| Volume | 2280044 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 162.75 |
| close_50_sma | 166.77 |
| close_200_sma | 164.55 |
| rsi | 46.08 |
| boll | 162.32 |
| boll_ub | 166.50 |
| boll_lb | 158.15 |
| macd | -0.79 |
| macds | -1.30 |
| macdh | 0.51 |
| atr | 3.14 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-15 | 159.40 |
| 2026-05-18 | 160.74 |
| 2026-05-19 | 162.88 |
| 2026-05-20 | 162.64 |
| 2026-05-21 | 164.13 |
| 2026-05-22 | 165.67 |
| 2026-05-25 | 164.60 |
| 2026-05-26 | 164.30 |
| 2026-05-27 | 164.81 |
| 2026-05-28 | 161.41 |
| 2026-05-29 | 165.02 |
| 2026-06-01 | 163.30 |
| 2026-06-02 | 163.00 |
| 2026-06-03 | 164.76 |
| 2026-06-04 | 163.73 |
| 2026-06-05 | 160.90 |
| 2026-06-09 | 160.48 |
| 2026-06-10 | 160.24 |
| 2026-06-11 | 156.42 |
| 2026-06-12 | 159.51 |
| 2026-06-15 | 161.79 |
| 2026-06-16 | 161.88 |
| 2026-06-17 | 163.71 |
| 2026-06-18 | 162.23 |
| 2026-06-19 | 162.40 |
| 2026-06-22 | 163.41 |
| 2026-06-23 | 164.21 |
| 2026-06-24 | 164.79 |
| 2026-06-25 | 162.70 |
| 2026-06-26 | 162.02 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 166.76759979248047
2026-06-25: 167.0893997192383
2026-06-24: 167.49919982910157
2026-06-23: 167.87380004882812
2026-06-22: 168.25359985351562
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 168.6529998779297
2026-06-18: 169.05559997558595
2026-06-17: 169.4152001953125
2026-06-16: 169.6798001098633
2026-06-15: 169.89820007324218
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 170.10040008544922
2026-06-11: 170.26420013427733
2026-06-10: 170.5102001953125
2026-06-09: 170.77800018310546
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 171.03200012207031
2026-06-04: 171.25740020751954
2026-06-03: 171.4052001953125
2026-06-02: 171.59500030517577
2026-06-01: 171.84780029296874
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 172.12900024414063
2026-05-28: 172.3704000854492


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 164.54604232788085
2026-06-25: 164.56751861572266
2026-06-24: 164.57345733642578
2026-06-23: 164.5796035003662
2026-06-22: 164.58815620422362
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 164.60001815795897
2026-06-18: 164.59990783691407
2026-06-17: 164.62980751037597
2026-06-16: 164.6448567199707
2026-06-15: 164.67571685791015
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 164.72207580566408
2026-06-11: 164.7624670410156
2026-06-10: 164.81460777282715
2026-06-09: 164.85366790771485
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 164.9040604400635
2026-06-04: 164.95708961486815
2026-06-03: 164.98906120300293
2026-06-02: 164.9963934326172
2026-06-01: 165.00834693908692
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 165.0089852142334
2026-05-28: 164.99635887145996


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 46.08186889924427
2026-06-25: 47.57268779487526
2026-06-24: 52.41198161661921
2026-06-23: 51.130992161836396
2026-06-22: 49.38594117465554
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 47.17454214508068
2026-06-18: 46.811339510932974
2026-06-17: 49.56638636943136
2026-06-16: 45.911401789949366
2026-06-15: 45.73177407542324
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 41.13358676687982
2026-06-11: 34.10746056762745
2026-06-10: 39.52268354438638
2026-06-09: 39.89217067595233
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 40.507571744657305
2026-06-04: 44.83513798805817
2026-06-03: 46.514567625531384
2026-06-02: 43.134858325397154
2026-06-01: 43.570638467996915
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 46.04726969406784
2026-05-28: 39.32578135647969


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: -0.7875177605997408
2026-06-25: -0.7794955077632153
2026-06-24: -0.8271536973821867
2026-06-23: -1.088751178209975
2026-06-22: -1.3477551310619447
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: -1.5772797909803558
2026-06-18: -1.7444571110892468
2026-06-17: -1.9151533372106826
2026-06-16: -2.255859044981463
2026-06-15: -2.4715834667200056
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: -2.701811152015665
2026-06-11: -2.724220996053475
2026-06-10: -2.3985812644611997
2026-06-09: -2.337004298029939
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: -2.248852276768133
2026-06-04: -2.1463911137153957
2026-06-03: -2.27253881765418
2026-06-02: -2.5053666526803795
2026-06-01: -2.586898497378826
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: -2.68388092992015
2026-05-28: -2.9437549091274207


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 3.1357217355910016
2026-06-25: 3.2292389330252855
2026-06-24: 3.2461038888860045
2026-06-23: 3.25118936681714
2026-06-22: 3.359742676734564
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 3.479722647886622
2026-06-18: 3.5889322701399196
2026-06-17: 3.5934656155893845
2026-06-16: 3.6721943502170533
2026-06-15: 3.646209722784832
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 3.6889941940236888
2026-06-11: 3.674301064116857
2026-06-10: 3.663092890262865
2026-06-09: 3.737177193495225
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 3.7446524091757474
2026-06-04: 3.6880875385324154
2026-06-03: 3.7264017767728896
2026-06-02: 3.822279165175492
2026-06-01: 3.8732234346421164
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 3.94424085667288
2026-05-28: 3.9699516448514425


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
<no Reddit posts found mentioning CBA.AX across r/wallstreetbets, r/stocks, r/investing in the past 7 days>
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
## CBA.AX News, from 2026-06-20 to 2026-06-27:

### Pound Trades Near 2026 Low as UK Political Uncertainty Builds (source: Bloomberg)
(Bloomberg) -- The pound traded near this year’s low on expectations Keir Starmer will set out a timetable for his departure as UK prime minister in coming days. Most Read from BloombergIran Says Hormuz Closed Again as Talks With US Set to OpenIranian Negotiators Said to Still Be Engaged in Talks With USUS, Iran Meet in Switzerland as Trump Threat Angers TehranDOJ Rejects Judge Request to Certify $1.8 Billion Fund NixedTrump’s Fears About Economy Undercut US Leverage in Iran TalksSterling slid a
Link: https://finance.yahoo.com/markets/currencies/articles/pound-trades-near-2026-low-080906468.html

### Oil Climbs After Fresh Trump Threat as US-Iran Peace Talks Begin (source: Bloomberg)
(Bloomberg) -- Oil rose after President Donald Trump threatened strikes on Iran if Hezbollah keeps attacking Israel, raising concerns about progress for peace talks between Washington and Tehran.Most Read from BloombergIran Says Hormuz Closed Again as Talks With US Set to OpenIranian Negotiators Said to Still Be Engaged in Talks With USDOJ Rejects Judge Request to Certify $1.8 Billion Fund NixedUS, Iran Meet in Switzerland as Fresh Trump Threat Angers TehranTrump’s Fears About Economy Undercut U
Link: https://finance.yahoo.com/energy/articles/oil-climbs-fresh-trump-threat-223930542.html


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-20 and 2026-06-27
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for CBA.AX
# Data retrieved on: 2026-06-29 13:53:48

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,450,52288.0,,Purchase at price 116.20 per share.,O'Malley (Paul Francis),Chairman of the Board,,2026-05-19,D
1,312,35771.0,,Purchase at price 114.65 per share.,McAloon (Jane Frances),Director (Non-Executive),,2026-05-18,D
2,530,59599.0,,Purchase at price 112.45 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2026-05-15,D
3,54,6033.0,,Other at price 111.73 per share.,Currie (Alistair),Director (Non-Executive),,2026-05-14,D
4,74,8267.0,,Other at price 111.73 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2026-05-14,D
5,6,717.0,,Acquisition at price 119.53 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2026-03-30,D
6,37,4422.0,,Acquisition at price 119.53 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2026-03-30,D
7,62,7804.0,,Purchase at price 125.88 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2026-02-17,D
8,40,4862.0,,Other at price 121.56 per share.,Currie (Alistair),Director (Non-Executive),,2026-02-12,D
9,67,8144.0,,Other at price 121.56 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2026-02-12,D
10,700,87636.0,,Purchase at price 125.19 per share.,O'Malley (Paul Francis),Chairman of the Board,,2026-02-12,D
11,48,4888.0,,Purchase at price 101.85 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2025-11-17,D
12,41,4228.0,,Purchase at price 103.12 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2025-11-14,D
13,28,2952.0,,Other at price 105.46 per share.,Currie (Alistair),Director (Non-Executive),,2025-11-12,D
14,50,5273.0,,Other at price 105.46 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2025-11-12,D
15,300,,,,McAloon (Jane Frances),Director (Non-Executive),,2025-10-01,D
16,58,6429.0,,Acquisition at price 110.85 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2025-09-29,D
17,39,4323.0,,Acquisition at price 110.85 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2025-09-29,D
18,20490,,,,Comyn (Matthew),Chief Executive Officer,,2025-08-14,D
19,20490,2239804.0,,Sale at price 109.31 per share.,Comyn (Matthew),Chief Executive Officer,,2025-08-14,D
20,49,5356.0,,Purchase at price 109.32 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2025-08-14,D
21,75,8198.0,,Purchase at price 109.32 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2025-08-14,D
22,174,,,,Munroe (Gavin),Divisional Officer,,2025-06-30,D
23,4488,,,,Shortt (Vittoria),Other Executive,,2025-06-30,D
24,15076,,,,Vacy-Lyle (Mike),Divisional Officer,,2025-06-30,D
25,11702,,,,Docherty (Alan),Chief Financial Officer,,2025-06-30,D
26,94,10592.0,,Purchase at price 112.69 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2025-05-21,D
27,105,11365.0,,Purchase at price 108.24 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2025-05-15,D
28,58,6273.0,,Other at price 108.17 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2025-05-15,D
29,67,7247.0,,Other at price 108.17 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2025-05-15,D
30,53,4994.0,,Acquisition at price 94.24 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2025-03-28,D
31,37,3486.0,,Acquisition at price 94.24 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2025-03-28,D
32,6748,,,,Lewis (Sian),Former,,2025-02-16,D
33,10000,,,,Williams (Nigel),Former,,2025-02-16,D
34,75,7878.0,,Other at price 105.05 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2025-02-13,D
35,48,5042.0,,Other at price 105.05 per share.,Howitt (Katherine Neisha),Independent Non-Executive Director,,2025-02-13,D
36,57,5628.0,,Purchase at price 98.75 per share.,Galbo (Julie Birgitte),Independent Non-Executive Director,,2024-11-15,D
37,72,7061.0,,Other at price 98.08 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2024-11-14,D
38,89,8728.0,,Other at price 98.08 per share.,Whitfield (Robert John),Independent Non-Executive Director,,2024-11-14,D
39,2458,,,,Howitt (Katherine Neisha),Independent Non-Executive Director,,2024-10-01,D
40,59,5762.0,,Acquisition at price 97.66 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2024-09-27,D
41,102,9368.0,,Other at price 91.85 per share.,Padbury (Mary Louise),Independent Non-Executive Director,,2024-08-16,D
42,75,6888.0,,Other at price 91.85 per share.,Templeman-Jones (Anne),Independent Non-Executive Director,,2024-08-16,D
43,125,11481.0,,Other at price 91.85 per share.,Whitfield (Robert John),Independent Non-Executive Director,,2024-08-16,D
44,19220,88.0,,Sale at price 0.00 per share.,Comyn (Matthew),Chief Executive Officer,,2024-08-15,D
45,618,,,,Docherty (Alan),Chief Financial Officer,,2024-06-30,D
46,3129,,,,Shortt (Vittoria),Managing Director,,2024-06-30,D
47,5277,,,,Sullivan (Angus),Divisional Officer,,2024-06-30,D
48,27162,,,,Vacy-Lyle (Mike),Divisional Officer,,2024-06-30,D
49,30000,,,,Williams (Nigel),Chief Risk Officer,,2024-06-30,D
50,3108,,,,Lewis (Sian),Divisional Officer,,2024-06-30,D
51,345,,,,Munroe (Gavin),Divisional Officer,,2024-06-30,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for CBA.AX
# Data retrieved on: 2026-06-29 13:53:48

Name: Commonwealth Bank of Australia
Sector: Financial Services
Industry: Banks - Diversified
Market Cap: 272138141696
PE Ratio (TTM): 26.20773
Forward PE: 24.2087
PEG Ratio: 3.49
Price to Book: 3.5236425
EPS (TTM): 6.21
Forward EPS: 6.72279
Dividend Yield: 3.06
Beta: 0.802
52 Week High: 186.83
52 Week Low: 146.98
50 Day Average: 166.421
200 Day Average: 165.47266
Revenue (TTM): 28466999296
Gross Profit: 28466999296
Net Income: 10403000320
Profit Margin: 0.36354
Operating Margin: 0.55507
Return on Equity: 0.13644
Return on Assets: 0.0076599997
Book Value: 46.188
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for CBA.AX (quarterly)
# Data retrieved on: 2026-06-29 13:53:49

,2025-12-31,2025-06-30,2024-12-31
Treasury Shares Number,1338636.0,1620212.0,1463595.0
Ordinary Shares Number,1672123722.0,1671842146.0,1671998763.0
Share Issued,1673462358.0,1673462358.0,1673462358.0
Net Debt,117533000000.0,158452000000.0,121070000000.0
Total Debt,207438000000.0,216232000000.0,203847000000.0
Tangible Book Value,68936000000.0,70694000000.0,67481000000.0
Invested Capital,284670000000.0,292731000000.0,279111000000.0
Net Tangible Assets,68936000000.0,70694000000.0,67481000000.0
Common Stock Equity,77232000000.0,78776000000.0,75264000000.0
Total Capitalization,284670000000.0,292731000000.0,279111000000.0
Total Equity Gross Minority Interest,77232000000.0,78776000000.0,75264000000.0
Minority Interest,,,0.0
Stockholders Equity,77232000000.0,78776000000.0,75264000000.0
Treasury Stock,195000000.0,215000000.0,189000000.0
Retained Earnings,45019000000.0,43974000000.0,42578000000.0
Capital Stock,33775000000.0,33775000000.0,33775000000.0
Common Stock,33775000000.0,33775000000.0,33775000000.0
Total Liabilities Net Minority Interest,1331496000000.0,1275023000000.0,1233302000000.0
Derivative Product Liabilities,22477000000.0,22493000000.0,36012000000.0
Long Term Debt And Capital Lease Obligation,207438000000.0,216232000000.0,203847000000.0
Payables,33379000000.0,40492000000.0,28020000000.0
Other Payable,32982000000.0,28275000000.0,27599000000.0
Total Tax Payable,397000000.0,780000000.0,421000000.0
Accounts Payable,,11437000000.0,
Total Assets,1408728000000.0,1353799000000.0,1308566000000.0
Defined Pension Benefit,,596000000.0,
Investments And Advances,253035000000.0,174651000000.0,232590000000.0
Investmentin Financial Assets,253035000000.0,173832000000.0,231819000000.0
Available For Sale Securities,115686000000.0,107651000000.0,103026000000.0
Financial Assets Designatedas Fair Value Through Profitor Loss Total,117676000000.0,51000000.0,87650000000.0
Trading Securities,,41411000000.0,
Long Term Equity Investment,,819000000.0,771000000.0
Goodwill And Other Intangible Assets,8296000000.0,8082000000.0,7783000000.0
Other Intangible Assets,3026000000.0,2793000000.0,2501000000.0
Goodwill,5270000000.0,5289000000.0,5282000000.0
Net PPE,3537000000.0,3563000000.0,3629000000.0
Prepaid Assets,,850000000.0,
Receivables,,4899000000.0,
Taxes Receivable,,30000000.0,
Cash And Cash Equivalents,89905000000.0,55503000000.0,82777000000.0
Cash Financial,82606000000.0,54381000000.0,76498000000.0
Cash Cash Equivalents And Federal Funds Sold,89905000000.0,134409000000.0,82777000000.0

```

### Tool: get_cashflow

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'CBA.AX' from any configured vendor (no cash flow data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

### Tool: get_income_statement

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'CBA.AX' from any configured vendor (no income statement data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

## Role: financial_report

- Skill: `tradingagents-financial-report-analyst`

### Tool: collect_financial_document_sources

- Status: `error`

```text
## Financial Document Source Packet: CBA.AX

- Trade date: `2026-06-27`
- Collection status: `error`
- Market: `ASX`
- ASX code: `CBA`

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_announcements | error |  |  | HTTP Error 404:  |

```
