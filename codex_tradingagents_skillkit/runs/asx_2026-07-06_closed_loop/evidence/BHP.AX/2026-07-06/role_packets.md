# Codex Role Evidence Packet: BHP.AX

- Trade date: `2026-07-06`
- Instrument identity: `BHP Group Limited`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for BHP.AX from 2026-06-06 to 2026-07-06
# Total records: 20
# Data retrieved on: 2026-07-06 22:12:36

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-06-09,59.53,60.43,59.04,60.08,12400757,0.0,0.0
2026-06-10,60.55,61.09,59.71,60.2,10886165,0.0,0.0
2026-06-11,59.14,61.19,59.06,60.8,10371932,0.0,0.0
2026-06-12,62.8,63.21,62.2,62.93,8296528,0.0,0.0
2026-06-15,65.19,65.44,64.74,65.18,9724092,0.0,0.0
2026-06-16,65.18,65.5,64.88,65.19,6067233,0.0,0.0
2026-06-17,65.5,65.98,65.18,65.59,5768095,0.0,0.0
2026-06-18,65.47,65.66,65.01,65.04,9245409,0.0,0.0
2026-06-19,63.05,63.25,61.4,61.4,37860909,0.0,0.0
2026-06-22,60.08,61.09,59.91,60.34,9797179,0.0,0.0
2026-06-23,60.71,61.28,59.92,59.92,12325151,0.0,0.0
2026-06-24,59.5,59.74,58.77,59.5,9219630,0.0,0.0
2026-06-25,58.5,59.16,58.22,58.52,9087113,0.0,0.0
2026-06-26,59.5,59.5,58.25,58.99,7522341,0.0,0.0
2026-06-29,58.8,59.82,58.8,59.82,8923197,0.0,0.0
2026-06-30,59.5,59.76,59.17,59.4,9990850,0.0,0.0
2026-07-01,60.4,60.53,59.59,59.92,6864309,0.0,0.0
2026-07-02,59.5,59.79,58.87,59.57,6803178,0.0,0.0
2026-07-03,59.96,60.74,59.45,60.5,5454380,0.0,0.0
2026-07-06,60.4,60.74,59.77,60.02,3594075,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for BHP.AX

- Requested analysis date: 2026-07-06
- Latest trading row used: 2026-07-06
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 60.40 |
| High | 60.74 |
| Low | 59.77 |
| Close | 60.02 |
| Volume | 3594075 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 60.17 |
| close_50_sma | 59.92 |
| close_200_sma | 50.05 |
| rsi | 47.90 |
| boll | 61.15 |
| boll_ub | 65.73 |
| boll_lb | 56.56 |
| macd | -0.22 |
| macds | 0.07 |
| macdh | -0.28 |
| atr | 1.35 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-25 | 60.12 |
| 2026-05-26 | 60.35 |
| 2026-05-27 | 61.28 |
| 2026-05-28 | 60.55 |
| 2026-05-29 | 62.31 |
| 2026-06-01 | 62.48 |
| 2026-06-02 | 63.37 |
| 2026-06-03 | 64.91 |
| 2026-06-04 | 62.80 |
| 2026-06-05 | 61.24 |
| 2026-06-09 | 60.08 |
| 2026-06-10 | 60.20 |
| 2026-06-11 | 60.80 |
| 2026-06-12 | 62.93 |
| 2026-06-15 | 65.18 |
| 2026-06-16 | 65.19 |
| 2026-06-17 | 65.59 |
| 2026-06-18 | 65.04 |
| 2026-06-19 | 61.40 |
| 2026-06-22 | 60.34 |
| 2026-06-23 | 59.92 |
| 2026-06-24 | 59.50 |
| 2026-06-25 | 58.52 |
| 2026-06-26 | 58.99 |
| 2026-06-29 | 59.82 |
| 2026-06-30 | 59.40 |
| 2026-07-01 | 59.92 |
| 2026-07-02 | 59.57 |
| 2026-07-03 | 60.50 |
| 2026-07-06 | 60.02 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-06-06 to 2026-07-06:

2026-07-06: 59.917000198364256
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 59.838600158691406
2026-07-02: 59.749200134277345
2026-07-01: 59.681200103759764
2026-06-30: 59.59300010681152
2026-06-29: 59.518800048828126
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 59.44080001831055
2026-06-25: 59.37939994812012
2026-06-24: 59.331199951171875
2026-06-23: 59.263199920654294
2026-06-22: 59.15179992675781
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 59.024599914550784
2026-06-18: 58.88779991149902
2026-06-17: 58.677599868774415
2026-06-16: 58.42419990539551
2026-06-15: 58.14499984741211
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 57.89259986877441
2026-06-11: 57.64179985046387
2026-06-10: 57.43439987182617
2026-06-09: 57.23779983520508
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-06-06 to 2026-07-06:

2026-07-06: 50.050623950958254
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 49.94664661407471
2026-07-02: 49.84193758010864
2026-07-01: 49.74413564682007
2026-06-30: 49.64365144729614
2026-06-29: 49.546895790100095
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 49.4453904914856
2026-06-25: 49.348967456817626
2026-06-24: 49.25739686965942
2026-06-23: 49.16288898468017
2026-06-22: 49.06745872497559
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 48.97174394607544
2026-06-18: 48.86773963928223
2026-06-17: 48.748223361968996
2026-06-16: 48.62523710250854
2026-06-15: 48.50660284042358
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 48.3871545791626
2026-06-11: 48.27996435165405
2026-06-10: 48.18068807601929
2026-06-09: 48.08676383972168
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-06-06 to 2026-07-06:

2026-07-06: 47.897338963697926
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 49.8979759023692
2026-07-02: 45.82701179049862
2026-07-01: 47.16629410380277
2026-06-30: 44.94664624468937
2026-06-29: 46.40894766027351
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 43.00634621156326
2026-06-25: 41.03787450787576
2026-06-24: 43.978830720215036
2026-06-23: 45.26990161507171
2026-06-22: 46.53854174292188
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 49.80979405593098
2026-06-18: 64.19912411175076
2026-06-17: 66.91117324960935
2026-06-16: 65.93947966453601
2026-06-15: 65.91623891142181
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 60.25081795830355
2026-06-11: 53.448976116375924
2026-06-10: 51.267751319283775
2026-06-09: 50.83996596233151
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-06-06 to 2026-07-06:

2026-07-06: -0.21835332343994196
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: -0.20831373897755157
2026-07-02: -0.24134224108811964
2026-07-01: -0.18529724738462505
2026-06-30: -0.1467044310061567
2026-06-29: -0.042366968174434305
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 0.048658372175239606
2026-06-25: 0.24864093738268167
2026-06-24: 0.5481294858116641
2026-06-23: 0.8226312144396886
2026-06-22: 1.1182662441131797
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 1.4365745164657184
2026-06-18: 1.7140285785665696
2026-06-17: 1.6726114097410232
2026-06-16: 1.539419614385011
2026-06-15: 1.3877535433815993
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 1.1750053787224388
2026-06-11: 1.1154612794124148
2026-06-10: 1.2401093009824535
2026-06-09: 1.4422583033189653
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-06-06 to 2026-07-06:

2026-07-06: 1.3511720263703384
2026-07-05: N/A: Not a trading day (weekend or holiday)
2026-07-04: N/A: Not a trading day (weekend or holiday)
2026-07-03: 1.3804928575755087
2026-07-02: 1.3874537761945982
2026-07-01: 1.413411817666448
2026-06-30: 1.4352129379932537
2026-06-29: 1.4956138158482035
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 1.532199458777783
2026-06-25: 1.553907109452997
2026-06-24: 1.5749769810034677
2026-06-23: 1.6076676940666852
2026-06-22: 1.6267190081986171
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 1.6372357258702956
2026-06-18: 1.4831769825027463
2026-06-17: 1.5472674022430417
2026-06-16: 1.6047492753572903
2026-06-15: 1.6804990083400027
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 1.6166910754253514
2026-06-11: 1.5556673237340624
2026-06-10: 1.5114880983737624
2026-06-09: 1.5216024853167263
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
<no Reddit posts found mentioning BHP.AX across r/wallstreetbets, r/stocks, r/investing in the past 7 days>
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
## BHP.AX News, from 2026-06-29 to 2026-07-06:

### BHP agrees to sell San Manuel property to Faraday Copper (source: Mining Technology)
The agreement provides for BHP to receive a 30% equity interest in Faraday on a fully diluted basis once the deal closes.
Link: https://www.mining-technology.com/news/bhp-sell-san-manuel-property-faraday-copper/

### BHP workers approve Pilbara labour deal, unions cite lingering concerns (source: Reuters)
July 3 (Reuters) - Workers at BHP's South Flank and Mining Area C iron ore operations in Western Australia have voted to approve a new labour agreement, unions said on Friday, while noting that many
Link: https://uk.finance.yahoo.com/news/bhp-workers-approve-pilbara-labour-042057258.html

### AVDE’s 23.6% Annual Gain Shows International Dividends are Outpacing U.S. Markets (source: 24/7 Wall St.)
Avantis International Equity ETF (NYSEARCA:AVDE) gives U.S. investors a single-ticket entry into developed markets outside the United States, and the income stream that comes with it. The fund draws from the MSCI World ex USA IMI Index universe but applies an active value-and-profitability tilt, then collects dividends from the underlying European, Japanese, U.K., and Australian ... AVDE’s 23.6% Annual Gain Shows International Dividends are Outpacing U.S. Markets
Link: https://247wallst.com/investing/2026/07/01/avdes-23-6-annual-gain-shows-international-dividends-are-outpacing-u-s-markets/

### Alcoa Shares Tumble on $5.6 Billion Deal for Mining Assets (source: The Wall Street Journal)
Alcoa shares had one of their worst day since President Trump announced sweeping tariffs in April 2025, ending 8.9% lower after the Pittsburgh company said it would pay up to $5.6 billion for bauxite, alumina and aluminum assets in South Africa, Australia and Brazil.  The BHP spinoff will receive $3.1 billion in cash, newly issued Alcoa stock worth roughly $1 billion that it plans to distribute to shareholders and future payments that could reach $750 million.  The deal comes amid a decline in aluminum prices from near record highs reached when fighting in the Persian Gulf blocked the region's aluminum smelters from global markets.
Link: https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-07-01-2026/card/alcoa-shares-tumble-on-5-6-billion-deal-for-mining-assets-wyPbLHu1gCjNkJRd5gHf?siteid=yhoof2&yptr=yahoo

### BHP’s Next CEO Inherits Buy vs. Build Copper Conundrum (source: The Wall Street Journal)
Brandon Craig, recently BHP’s Americas chief, says he wants to pursue both reliable and more-creative growth in copper.
Link: https://www.wsj.com/business/bhps-next-ceo-inherits-buy-vs-build-copper-conundrum-cb7f875e?siteid=yhoof2&yptr=yahoo


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-29 and 2026-07-06
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for BHP.AX
# Data retrieved on: 2026-07-06 22:12:49

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,74,1275,,Stock Award(Grant) at price 0.00 - 34.47 per share.,STONE EMMA KATE,Officer,,2026-04-02,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for BHP.AX
# Data retrieved on: 2026-07-06 22:12:50

Name: BHP Group Limited
Sector: Basic Materials
Industry: Other Industrial Metals & Mining
Market Cap: 304943038464
PE Ratio (TTM): 20.554794
Forward PE: 15.738625
PEG Ratio: 2.93
Price to Book: 4.168334
EPS (TTM): 2.92
Forward EPS: 3.813548
Dividend Yield: 3.26
Beta: 0.831
52 Week High: 65.98
52 Week Low: 37.56
50 Day Average: 60.0186
200 Day Average: 50.85775
Revenue (TTM): 53987999744
Gross Profit: 44856000512
EBITDA: 26292000768
Net Income: 10243000320
Profit Margin: 0.18972999
Operating Margin: 0.40728
Return on Equity: 0.24712999
Return on Assets: 0.122250006
Debt to Equity: 52.639
Current Ratio: 1.649
Book Value: 14.399037
Free Cash Flow: 8137124864
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for BHP.AX (quarterly)
# Data retrieved on: 2026-07-06 22:12:50

,2025-12-31,2025-06-30,2024-12-31
Treasury Shares Number,,701522.0,
Ordinary Shares Number,5078211653.0,5075290713.0,5072643514.0
Share Issued,5078211653.0,5075992235.0,5072643514.0
Net Debt,14555000000.0,9734000000.0,10635000000.0
Total Debt,28021000000.0,24496000000.0,20195000000.0
Tangible Book Value,48395000000.0,44304000000.0,43755000000.0
Invested Capital,78428000000.0,67731000000.0,65711000000.0
Working Capital,10202000000.0,7191000000.0,8558000000.0
Net Tangible Assets,48395000000.0,44304000000.0,43755000000.0
Capital Lease Obligations,,2953000000.0,
Common Stock Equity,50407000000.0,46228000000.0,45516000000.0
Total Capitalization,74997000000.0,66394000000.0,65220000000.0
Total Equity Gross Minority Interest,55465000000.0,52218000000.0,49597000000.0
Minority Interest,5058000000.0,5990000000.0,4081000000.0
Stockholders Equity,50407000000.0,46228000000.0,45516000000.0
Other Equity Interest,,188000000.0,
Gains Losses Not Affecting Retained Earnings,91000000.0,-1627000000.0,-35000000.0
Other Equity Adjustments,,-1615000000.0,
Foreign Currency Translation Adjustments,,-14000000.0,
Unrealized Gain Loss,,2000000.0,
Treasury Stock,32000000.0,18000000.0,25000000.0
Retained Earnings,45255000000.0,42670000000.0,40612000000.0
Capital Stock,5093000000.0,5015000000.0,4964000000.0
Common Stock,5093000000.0,5015000000.0,4964000000.0
Total Liabilities Net Minority Interest,60547000000.0,56572000000.0,51125000000.0
Total Non Current Liabilities Net Minority Interest,44821000000.0,40933000000.0,38828000000.0
Other Non Current Liabilities,237000000.0,308000000.0,311000000.0
Derivative Product Liabilities,1175000000.0,1056000000.0,1660000000.0
Tradeand Other Payables Non Current,40000000.0,36000000.0,36000000.0
Non Current Deferred Liabilities,3806000000.0,3557000000.0,3585000000.0
Non Current Deferred Revenue,51000000.0,51000000.0,48000000.0
Non Current Deferred Taxes Liabilities,3755000000.0,3506000000.0,3537000000.0
Long Term Debt And Capital Lease Obligation,24590000000.0,22478000000.0,19704000000.0
Long Term Capital Lease Obligation,,2312000000.0,
Long Term Debt,24590000000.0,20166000000.0,19704000000.0
Long Term Provisions,14973000000.0,13498000000.0,13532000000.0
Current Liabilities,15726000000.0,15639000000.0,12297000000.0
Other Current Liabilities,462000000.0,214000000.0,325000000.0
Current Deferred Liabilities,15000000.0,47000000.0,50000000.0
Current Deferred Revenue,15000000.0,47000000.0,50000000.0
Current Debt And Capital Lease Obligation,3431000000.0,2018000000.0,491000000.0
Current Capital Lease Obligation,,641000000.0,
Current Debt,3431000000.0,1337000000.0,491000000.0
Other Current Borrowings,3431000000.0,1336000000.0,491000000.0
Line Of Credit,,1000000.0,
Current Provisions,4200000000.0,5823000000.0,4351000000.0
Payables And Accrued Expenses,7618000000.0,7537000000.0,7080000000.0
Payables,7618000000.0,7537000000.0,7080000000.0
Total Tax Payable,1330000000.0,900000000.0,1048000000.0
Accounts Payable,6288000000.0,6637000000.0,6032000000.0
Total Assets,116012000000.0,108790000000.0,100722000000.0
Total Non Current Assets,90084000000.0,85960000000.0,79867000000.0
Other Non Current Assets,2635000000.0,2135000000.0,1862000000.0
Non Current Deferred Assets,74000000.0,78000000.0,61000000.0
Non Current Deferred Taxes Assets,74000000.0,78000000.0,61000000.0
Non Current Accounts Receivable,104000000.0,137000000.0,155000000.0
Financial Assets,610000000.0,606000000.0,187000000.0
Investments And Advances,4798000000.0,4623000000.0,2729000000.0
Investmentin Financial Assets,506000000.0,516000000.0,1043000000.0
Available For Sale Securities,300000000.0,255000000.0,851000000.0
Financial Assets Designatedas Fair Value Through Profitor Loss Total,206000000.0,261000000.0,192000000.0
Long Term Equity Investment,4292000000.0,4107000000.0,1686000000.0
Goodwill And Other Intangible Assets,2012000000.0,1924000000.0,1761000000.0
Other Intangible Assets,,583000000.0,
Goodwill,,1341000000.0,
Net PPE,79851000000.0,76457000000.0,73112000000.0
Accumulated Depreciation,,-75129000000.0,
Gross PPE,,151586000000.0,
Construction In Progress,,22002000000.0,
Other Properties,,15617000000.0,
Machinery Furniture Equipment,,93385000000.0,
Current Assets,25928000000.0,22830000000.0,20855000000.0
Other Current Assets,167000000.0,176000000.0,193000000.0
Hedging Assets Current,258000000.0,288000000.0,235000000.0
Restricted Cash,,125000000.0,
Inventory,5817000000.0,5538000000.0,5533000000.0
Receivables,5871000000.0,4661000000.0,5036000000.0
Taxes Receivable,419000000.0,545000000.0,728000000.0
Accounts Receivable,5452000000.0,4116000000.0,4308000000.0
Cash Cash Equivalents And Short Term Investments,13815000000.0,12042000000.0,9858000000.0
Other Short Term Investments,349000000.0,273000000.0,298000000.0
Cash And Cash Equivalents,13466000000.0,11769000000.0,9560000000.0

```

### Tool: get_cashflow

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'BHP.AX' from any configured vendor (no cash flow data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

### Tool: get_income_statement

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'BHP.AX' from any configured vendor (no income statement data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

## Role: financial_report

- Skill: `tradingagents-financial-report-analyst`

### Tool: collect_financial_document_sources

- Status: `ok`

```text
## Financial Document Source Packet: BHP.AX

- Trade date: `2026-07-06`
- Collection status: `ok`
- Market: `ASX`
- ASX code: `BHP`
- As-of rule: Only ASX announcements with announcement/lodgement date <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://www.bhp.com/investor-hub/reports-and-presentations/annual-report |
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf |

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: revenue, income, NPAT
- Unavailable reason: revenue_income_npat was not identified in extracted ASX document text.

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: EPS, DPS, dividends
- Unavailable reason: eps_dps was not identified in extracted ASX document text.

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: management discussion, MD&A, outlook

```text
outlook Ethics and Business Conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Tax and transparency Non-Operated Joint Ventures Corporate governance Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent Copper Metallurgical coal Nickel Potash Iron ore Australia Brazil Canada - Jansen Chile Peru - Antamina United States Offices 2026 Financial Results 2025 Financial Results 2024 Financial Results 2023 Financial Results Annual Report 2025 Economic Contribution Report 2025 Past reports BHP Shareholder Q&A sessions Meetings Presentations and briefings Financial Calendar Current share price Shareholder online services Dividends Capital Management Program Demerger taxation information Boiler Room scams Onshore petroleum divestment Shareholder FAQs Offer for Anglo American Materiality assessment Social value Social investment Forum on corporate responsibility Sustainability-related risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulatory information Our position on climate change Operational GHG emission reductions Carbon offsets and natural climate solutions Value chain GHG emission reductions Transition to a net zero economy Physical climate-related risk and adaptation Advocacy on climate policy Equitable change and transition Climate Transition Action Plan Climate and nature Capability and culture Local communities Economic contribution Indigenous peoples Human rights Modern slavery statement BHP Foundation Health Safety Sexual harassment What are Tailings Storage Facilities? Tailings Storage Facility management Releases Image gallery Reports and Presentations Australia country program Canada country program Chile country program BHP Foundation board and governance How to speak up Look out for one another Care for our people and planet Work with integrity Protect our company Protect and respect information FutureFit Operations Services New to industry pathways in Australia Why BHP Canada Chile Malaysia and the Philippines Singapore Australia Rest of the world Australian programs Singapore programs US programs LGBT+ Inclusion BHP Inclusion and Diversity Storybook Our Global Inclusion and Diversity Council Wellbeing resources All investor resources Financial results & Operational reviews Annual reports Economic Contribution report Presentations & Briefings Economic & Commodity Outlook Dividends Shareholder online services Annual General meetings Shareholder Q&As Share price Corporate actions & historical share information Frequently Asked Questions Key contacts Ethics & business conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent How to speak up Look out for one another Care for our people & our planet Work with integrity Protect our company Protect & respect information Follow us on Home Investor hub Reports and presentations Annual Reports Annual Report 2025 How we create and deliver value. In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Read the report Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. Ross McEwan Chair Read the full message FY2025 at a glance Find out more about our 2025 results and performance 2Mt Record annual copper production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model Positioning for growth People Downloads We delivered another strong set of results in FY2025 enabled by our great people, the disciplined application of our strategy, world-class assets, operational excellence and through financial rigour underpinned by our Capital Allocation Framework (CAF). This enabled the Board to announce a final dividend of 60 US cents per share, taking the total dividends for the year to 110 US cents per share, or US$5.6 billion. Our approach aims to balance investment in growth with shareholder returns – as reflected in our dividend payout ratio of 55 per cent for
```

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: cash flow statement, operating cash flow

```text
operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we can control, with healthy volume growth and disciplined cost management. We saw record production volumes in iron ore and copper, and increased our steelmaking coal production on the prior financial year, excluding Blackwater and Daunia which we divested in CY2024. Importantly, we continued to be disciplined with our costs. Escondida delivered an 18 per cent unit cost reduction and WAIO remains the lowest-cost major iron ore producer in the world. Across the group, unit costs at our major assets were down 4.7 per cent year-on-year. 5 Value-adding investments and resilient balance sheet In FY2025, we invested US$9.8 billion in capital and exploration expenditure. We also invested US$2.1 billion to acquire a 50 per cent interest in the Josemaria and Filo del Sol deposits and form the Vicuña joint venture with Lundin Mining. The Filo del Sol deposit is one of the largest copper deposit discoveries in the last 30 years. With net debt of US$12.9 billion, our balance sheet remains strong. The resilience of our portfolio, track record of stable operations and robust financial performance has led to our improved debt servicing capacity. Accordingly, we are revising our net debt target range to US$10 billion to US$20 billion (from US$5 billion to US$15 billion). This will unlock the power of our balance sheet for our pipeline of projects we expect will deliver great value for our shareholders, partners and other stakeholders well into the future. How we create and deliver value The keys to our successful past and exciting future are the same – our people, capabilities, scale, portfolio and, in more recent times, the unique overarching way we work through the BHP Operating System (BOS). BOS differentiates our approach, makes improvement central to everyone’s role and provides for sustainable operating excellence year after year. We seek to use our capital carefully and effectively. We operate our assets efficiently. We have an overriding focus on safety. We embrace technology and innovation. We have a clear strategy and proven record of execution against it. We grow value through our large, long-life, quality assets in materials that improve standards of living and support decarbonisation and digitalisation, and through our differentiated focus on social value, which is integral to how we operate. We seek to extract materials as efficiently and effectively as we can while seeking to appropriately manage impacts on the planet. We choose to partner with peers, suppliers and customers where we believe we can innovate or create value together. View our business model Our portfolio A resource mix for today – and for the future. We have copper, which is used in electrification and renewable power and is important for digitalisation. We have iron ore, which is essential for making steel needed for construction, including renewables infrastructure. Our higher-quality steelmaking coal is used in the blast furnace process for making steel. We are developing a world-class potash asset. Potash is used in fertilisers to assist with food security for a growing population and more sustainable land use. We are also a major producer of uranium and gold, which are by-products of our copper production. Read more Social value< We are committed to social value and the responsible provision of commodities the world needs to develop, decarbonise and digitise. Social value creates business value. In FY2025, we continued to refine our approach to social value. We have a 2030 social value scorecard to monitor our progress. Each year since first publishing the social value scorecard in June 2022, we have reported performance against key metrics and the milestones for that year and set out new short-term milestones for the next year to demonstrate the pathway to FY2030. Read more See our 2030 social value scorecard Exceptional performance Enabled by the BHP Operating System (BOS), operational excellence underpins strong returns and investment growth. FY2025 was a standout year for BHP, marked by record production, continued sector-leading margins and disciplined capital allocation. At WAIO, we are the world’s lowest-cost major iron ore producer and have been for six years, and we have the best track record of delivering production against guidance amongst our competitors. BOS is our unique overarching management system that enables the right culture, routines, behaviours and leadership to deliver stable operating excellence and leading safety performance. It provides us with a competitive edge. Read more With our clear strategy and focus on creating and sustaining the right portfolio of the best assets with enhanced growth optionality, BHP is well placed to capitalise on the changes shaping our world. As the global population grows and urbanises and the world pursues decarbonisation, electrification and digitalisation, we are positioning our portfolio and pursuing multiple growth options to increase our exposure to these megatrends. Read more Unlocking growth at our assets Our biggest near-term growth levers are improving productivity at our existing assets and unlocking more of their potential. We have significant opportunities in our world-leading copper portfolio. These projects have potential to enable significant total annual copper production through the 2030s. Read more Growth through exploration, focused on copper In FY2025, we continued to strengthen our exploration portfolio, focusing primarily on copper opportunities. Our efforts spanned early-stage greenfield exploration, strategic alliances and the expansion of our Xplor accelerator program. Read more Safety Nothing is more important than protecting
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: operating cash flow

```text
operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we can control, with healthy volume growth and disciplined cost management. We saw record production volumes in iron ore and copper, and increased our steelmaking coal production on the prior financial year, excluding Blackwater and Daunia which we divested in CY2024. Importantly, we continued to be disciplined with our costs. Escondida delivered an 18 per cent unit cost reduction and WAIO remains the lowest-cost major iron ore producer in the world. Across the group, unit costs at our major assets were down 4.7 per cent year-on-year. 5 Value-adding investments and resilient balance sheet In FY2025, we invested US$9.8 billion in capital and exploration expenditure. We also invested US$2.1 billion to acquire a 50 per cent interest in the Josemaria and Filo del Sol deposits and form the Vicuña joint venture with Lundin Mining. The Filo del Sol deposit is one of the largest copper deposit discoveries in the last 30 years. With net debt of US$12.9 billion, our balance sheet remains strong. The resilience of our portfolio, track record of stable operations and robust financial performance has led to our improved debt servicing capacity. Accordingly, we are revising our net debt target range to US$10 billion to US$20 billion (from US$5 billion to US$15 billion). This will unlock the power of our balance sheet for our pipeline of projects we expect will deliver great value for our shareholders, partners and other stakeholders well into the future. How we create and deliver value The keys to our successful past and exciting future are the same – our people, capabilities, scale, portfolio and, in more recent times, the unique overarching way we work through the BHP Operating System (BOS). BOS differentiates our approach, makes improvement central to everyone’s role and provides for sustainable operating excellence year after year. We seek to use our capital carefully and effectively. We operate our assets efficiently. We have an overriding focus on safety. We embrace technology and innovation. We have a clear strategy and proven record of execution against it. We grow value through our large, long-life, quality assets in materials that improve standards of living and support decarbonisation and digitalisation, and through our differentiated focus on social value, which is integral to how we operate. We seek to extract materials as efficiently and effectively as we can while seeking to appropriately manage impacts on the planet. We choose to partner with peers, suppliers and customers where we believe we can innovate or create value together. View our business model Our portfolio A resource mix for today – and for the future. We have copper, which is used in electrification and renewable power and is important for digitalisation. We have iron ore, which is essential for making steel needed for construction, including renewables infrastructure. Our higher-quality steelmaking coal is used in the blast furnace process for making steel. We are developing a world-class potash asset. Potash is used in fertilisers to assist with food security for a growing population and more sustainable land use. We are also a major producer of uranium and gold, which are by-products of our copper production. Read more Social value< We are committed to social value and the responsible provision of commodities the world needs to develop, decarbonise and digitise. Social value creates business value. In FY2025, we continued to refine our approach to social value. We have a 2030 social value scorecard to monitor our progress. Each year since first publishing the social value scorecard in June 2022, we have reported performance against key metrics and the milestones for that year and set out new short-term milestones for the next year to demonstrate the pathway to FY2030. Read more See our 2030 social value scorecard Exceptional performance Enabled by the BHP Operating System (BOS), operational excellence underpins strong returns and investment growth. FY2025 was a standout year for BHP, marked by record production, continued sector-leading margins and disciplined capital allocation. At WAIO, we are the world’s lowest-cost major iron ore producer and have been for six years, and we have the best track record of delivering production against guidance amongst our competitors. BOS is our unique overarching management system that enables the right culture, routines, behaviours and leadership to deliver stable operating excellence and leading safety performance. It provides us with a competitive edge. Read more With our clear strategy and focus on creating and sustaining the right portfolio of the best assets with enhanced growth optionality, BHP is well placed to capitalise on the changes shaping our world. As the global population grows and urbanises and the world pursues decarbonisation, electrification and digitalisation, we are positioning our portfolio and pursuing multiple growth options to increase our exposure to these megatrends. Read more Unlocking growth at our assets Our biggest near-term growth levers are improving productivity at our existing assets and unlocking more of their potential. We have significant opportunities in our world-leading copper portfolio. These projects have potential to enable significant total annual copper production through the 2030s. Read more Growth through exploration, focused on copper In FY2025, we continued to strengthen our exploration portfolio, focusing primarily on copper opportunities. Our efforts spanned early-stage greenfield exploration, strategic alliances and the expansion of our Xplor accelerator program. Read more Safety Nothing is more important than protecting
```

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: free cash flow, cash movement
- Unavailable reason: free_cash_flow_or_cash_movement was not identified in extracted ASX document text.

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: cash, debt, gearing, capital

```text
Debt investors Consensus estimates Sustainability approach Value chain sustainability Nature and environmental performance Climate change Social performance Ethics and business conduct People Safety and health Tailings storage facilities BHP Foundation Australia Global careers Indigenous peoples and BHP Graduate and student programs Recruitment process Life at BHP Culture and rewards Inclusion and diversity Health and safety Fraudulent email scams News & publication library Image gallery BHP Insights Why work with us Find opportunities Become a supplier New and existing suppliers Global outlook Ethics and Business Conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Tax and transparency Non-Operated Joint Ventures Corporate governance Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent Copper Metallurgical coal Nickel Potash Iron ore Australia Brazil Canada - Jansen Chile Peru - Antamina United States Offices 2026 Financial Results 2025 Financial Results 2024 Financial Results 2023 Financial Results Annual Report 2025 Economic Contribution Report 2025 Past reports BHP Shareholder Q&A sessions Meetings Presentations and briefings Financial Calendar Current share price Shareholder online services Dividends Capital Management Program Demerger taxation information Boiler Room scams Onshore petroleum divestment Shareholder FAQs Offer for Anglo American Materiality assessment Social value Social investment Forum on corporate responsibility Sustainability-related risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulatory information Our position on climate change Operational GHG emission reductions Carbon offsets and natural climate solutions Value chain GHG emission reductions Transition to a net zero economy Physical climate-related risk and adaptation Advocacy on climate policy Equitable change and transition Climate Transition Action Plan Climate and nature Capability and culture Local communities Economic contribution Indigenous peoples Human rights Modern slavery statement BHP Foundation Health Safety Sexual harassment What are Tailings Storage Facilities? Tailings Storage Facility management Releases Image gallery Reports and Presentations Australia country program Canada country program Chile country program BHP Foundation board and governance How to speak up Look out for one another Care for our people and planet Work with integrity Protect our company Protect and respect information FutureFit Operations Services New to industry pathways in Australia Why BHP Canada Chile Malaysia and the Philippines Singapore Australia Rest of the world Australian programs Singapore programs US programs LGBT+ Inclusion BHP Inclusion and Diversity Storybook Our Global Inclusion and Diversity Council Wellbeing resources All investor resources Financial results & Operational reviews Annual reports Economic Contribution report Presentations & Briefings Economic & Commodity Outlook Dividends Shareholder online services Annual General meetings Shareholder Q&As Share price Corporate actions & historical share information Frequently Asked Questions Key contacts Ethics & business conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent How to speak up Look out for one another Care for our people & our planet Work with integrity Protect our company Protect & respect information Follow us on Home Investor hub Reports and presentations Annual Reports Annual Report 2025 How we create and deliver value. In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Read the report Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. Ross McEwan Chair Read the full message FY2025 at a glance Find out more about our 2025 results and performance 2Mt Record annual copper production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: segment performance, sector metrics

```text
production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model Positioning for growth People Downloads We delivered another strong set of results in FY2025 enabled by our great people, the disciplined application of our strategy, world-class assets, operational excellence and through financial rigour underpinned by our Capital Allocation Framework (CAF). This enabled the Board to announce a final dividend of 60 US cents per share, taking the total dividends for the year to 110 US cents per share, or US$5.6 billion. Our approach aims to balance investment in growth with shareholder returns – as reflected in our dividend payout ratio of 55 per cent for FY2025. Strong results We can deliver a dividend of this scale because of our resilient portfolio and disciplined operational delivery, achieved amid a volatile external environment. We achieved an underlying EBITDA of US$26 billion, with a 53 per cent margin. We have averaged a margin of over 50 per cent for the past 20 years, which is a testament to our consistency and a sign of the resilience and stability of BHP. This year, we generated net operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we can control, with healthy volume growth and disciplined cost management. We saw record production volumes in iron ore and copper, and increased our steelmaking coal production on the prior financial year, excluding Blackwater and Daunia which we divested in CY2024. Importantly, we continued to be disciplined with our costs. Escondida delivered an 18 per cent unit cost reduction and WAIO remains the lowest-cost major iron ore producer in the world. Across the group, unit costs at our major assets were down 4.7 per cent year-on-year. 5 Value-adding investments and resilient balance sheet In FY2025, we invested US$9.8 billion in capital and exploration expenditure. We also invested US$2.1 billion to acquire a 50 per cent interest in the Josemaria and Filo del Sol deposits and form the Vicuña joint venture with Lundin Mining. The Filo del Sol deposit is one of the largest copper deposit discoveries in the last 30 years. With net debt of US$12.9 billion, our balance sheet remains strong. The resilience of our portfolio, track record of stable operations and robust financial performance has led to our improved debt servicing capacity. Accordingly, we are revising our net debt target range to US$10 billion to US$20 billion (from US$5 billion to US$15 billion). This will unlock the power of our balance sheet for our pipeline of projects we expect will deliver great value for our shareholders, partners and other stakeholders well into the future. How we create and deliver value The keys to our successful past and exciting future are the same – our people, capabilities, scale, portfolio and, in more recent times, the unique overarching way we work through the BHP Operating System (BOS). BOS differentiates our approach, makes improvement central to everyone’s role and provides for sustainable operating excellence year after year. We seek to use our capital carefully and effectively. We operate our assets efficiently. We have an overriding focus on safety. We embrace technology and innovation. We have a clear strategy and proven record of execution against it. We grow value through our large, long-life, quality assets in materials that improve standards of living and support decarbonisation and digitalisation, and through our differentiated focus on social value, which is integral to how we operate. We seek to extract materials as efficiently and effectively as we can while seeking to appropriately manage impacts on the planet. We choose to partner with peers, suppliers and customers where we believe we can innovate or create value together. View our business model Our portfolio A resource mix for today – and for the future. We have copper, which is used in electrification and renewable power and is important for digitalisation. We have iron ore, which is essential for making steel needed for construction, including renewables infrastructure. Our higher-quality steelmaking coal is used in the blast furnace process for making steel. We are developing a world-class potash asset. Potash is used in fertilisers to
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: outlook, management commentary

```text
outlook Ethics and Business Conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Tax and transparency Non-Operated Joint Ventures Corporate governance Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent Copper Metallurgical coal Nickel Potash Iron ore Australia Brazil Canada - Jansen Chile Peru - Antamina United States Offices 2026 Financial Results 2025 Financial Results 2024 Financial Results 2023 Financial Results Annual Report 2025 Economic Contribution Report 2025 Past reports BHP Shareholder Q&A sessions Meetings Presentations and briefings Financial Calendar Current share price Shareholder online services Dividends Capital Management Program Demerger taxation information Boiler Room scams Onshore petroleum divestment Shareholder FAQs Offer for Anglo American Materiality assessment Social value Social investment Forum on corporate responsibility Sustainability-related risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulatory information Our position on climate change Operational GHG emission reductions Carbon offsets and natural climate solutions Value chain GHG emission reductions Transition to a net zero economy Physical climate-related risk and adaptation Advocacy on climate policy Equitable change and transition Climate Transition Action Plan Climate and nature Capability and culture Local communities Economic contribution Indigenous peoples Human rights Modern slavery statement BHP Foundation Health Safety Sexual harassment What are Tailings Storage Facilities? Tailings Storage Facility management Releases Image gallery Reports and Presentations Australia country program Canada country program Chile country program BHP Foundation board and governance How to speak up Look out for one another Care for our people and planet Work with integrity Protect our company Protect and respect information FutureFit Operations Services New to industry pathways in Australia Why BHP Canada Chile Malaysia and the Philippines Singapore Australia Rest of the world Australian programs Singapore programs US programs LGBT+ Inclusion BHP Inclusion and Diversity Storybook Our Global Inclusion and Diversity Council Wellbeing resources All investor resources Financial results & Operational reviews Annual reports Economic Contribution report Presentations & Briefings Economic & Commodity Outlook Dividends Shareholder online services Annual General meetings Shareholder Q&As Share price Corporate actions & historical share information Frequently Asked Questions Key contacts Ethics & business conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent How to speak up Look out for one another Care for our people & our planet Work with integrity Protect our company Protect & respect information Follow us on Home Investor hub Reports and presentations Annual Reports Annual Report 2025 How we create and deliver value. In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Read the report Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. Ross McEwan Chair Read the full message FY2025 at a glance Find out more about our 2025 results and performance 2Mt Record annual copper production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model Positioning for growth People Downloads We delivered another strong set of results in FY2025 enabled by our great people, the disciplined application of our strategy, world-class assets, operational excellence and through financial rigour underpinned by our Capital Allocation Framework (CAF). This enabled the Board to announce a final dividend of 60 US cents per share, taking the total dividends for the year to 110 US cents per share, or US$5.6 billion. Our approach aims to balance investment in growth with shareholder returns – as reflected in our dividend payout ratio of 55 per cent for
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: dividends, capital management

```text
Capital Management Program Demerger taxation information Boiler Room scams Onshore petroleum divestment Shareholder FAQs Offer for Anglo American Materiality assessment Social value Social investment Forum on corporate responsibility Sustainability-related risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulatory information Our position on climate change Operational GHG emission reductions Carbon offsets and natural climate solutions Value chain GHG emission reductions Transition to a net zero economy Physical climate-related risk and adaptation Advocacy on climate policy Equitable change and transition Climate Transition Action Plan Climate and nature Capability and culture Local communities Economic contribution Indigenous peoples Human rights Modern slavery statement BHP Foundation Health Safety Sexual harassment What are Tailings Storage Facilities? Tailings Storage Facility management Releases Image gallery Reports and Presentations Australia country program Canada country program Chile country program BHP Foundation board and governance How to speak up Look out for one another Care for our people and planet Work with integrity Protect our company Protect and respect information FutureFit Operations Services New to industry pathways in Australia Why BHP Canada Chile Malaysia and the Philippines Singapore Australia Rest of the world Australian programs Singapore programs US programs LGBT+ Inclusion BHP Inclusion and Diversity Storybook Our Global Inclusion and Diversity Council Wellbeing resources All investor resources Financial results & Operational reviews Annual reports Economic Contribution report Presentations & Briefings Economic & Commodity Outlook Dividends Shareholder online services Annual General meetings Shareholder Q&As Share price Corporate actions & historical share information Frequently Asked Questions Key contacts Ethics & business conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent How to speak up Look out for one another Care for our people & our planet Work with integrity Protect our company Protect & respect information Follow us on Home Investor hub Reports and presentations Annual Reports Annual Report 2025 How we create and deliver value. In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Read the report Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. Ross McEwan Chair Read the full message FY2025 at a glance Find out more about our 2025 results and performance 2Mt Record annual copper production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model Positioning for growth People Downloads We delivered another strong set of results in FY2025 enabled by our great people, the disciplined application of our strategy, world-class assets, operational excellence and through financial rigour underpinned by our Capital Allocation Framework (CAF). This enabled the Board to announce a final dividend of 60 US cents per share, taking the total dividends for the year to 110 US cents per share, or US$5.6 billion. Our approach aims to balance investment in growth with shareholder returns – as reflected in our dividend payout ratio of 55 per cent for FY2025. Strong results We can deliver a dividend of this scale because of our resilient portfolio and disciplined operational delivery, achieved amid a volatile external environment. We achieved an underlying EBITDA of US$26 billion, with a 53 per cent margin. We have averaged a margin of over 50 per cent for the past 20 years, which is a testament to our consistency and a sign of the resilience and stability of BHP. This year, we generated net operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we
```

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: capex, commitments

```text
Commitment to Culture and Community Pilbara Air Quality Program Pilbara surplus water scheme success Project Rise Protecting Australias unique fauna River health partnerships in Queensland Australia Enhancing species baselines using a novel monitoring technique Virtual Future Fit Academy 2024 reports BHP Annual Report 2024 pdf BHP Annual Report 2024 (ESEF/iXBRL with built-in iXBRL viewer) xml BHP Annual Report 2024 (ESEF/iXBRL) zip BHP Form 20-F 2024 pdf BHP Climate Transition Action Plan 2024, subject to updates of certain aspects of our assumptions and plans in the BHP Annual Report 2025, Operating and Financial Review 9.8 – Climate change pdf BHP Economic Contribution Report 2024 pdf BHP Economic Contribution Report 2024 XML xml BHP Economic Contribution Report Extract 2024 pdf BHP Modern Slavery Statement 2024 pdf BHP GHG Emissions Calculation Methodology 2024 pdf BHP ESG Standards and Databook 2024 xlsx Límite organizativo de los informes de sostenibilidad, definiciones y cláusulas de exención de responsabilidad pdf Sustainability reporting organisational boundary, definitions and disclaimers pdf 2024 case studies Bamboo flexible work crew BMA Water Allocation Comunidad Mineras Embedding and sustaining sexual harassment elimination in BHPs workplaces Inclusion and Diversity Leadership Forum Operational Services Maintenance Redesign Team Reducing welding fume exposure at Olympic Dam Western Australia Iron Ore Finish and Fill Women Without Limits in Pampa Norte Building strong partnerships at Jansen Indigenous Partners Relationship Health Results 2024 Pilbara Air Quality Program Annual Report 2025 Download and read our 2025 Annual Report BHP Annual Report 2025 pdf Modern Slavery Statement Our work to combat modern slavery and build more resilient and ethical supply chains supports our purpose: to bring people and resources together to build a better world. Economic Contribution Report 2025 BHP has a strong commitment to the highest standards of corporate governance and transparency. Sustainability Report We know our stakeholders and partners are increasingly focused on our sustainability performance and use it as a key determinant in assessing BHP and our industry. Past reports 2024 2023 2022 2021 2020 FY24 Reports BHP Annual Report 2024 pdf BHP Annual Report 2024 (ESEF/iXBRL with built-in iXBRL viewer) xml BHP Annual Report 2024 (ESEF/iXBRL) zip BHP Form 20-F 2024 pdf BHP Climate Transition Action Plan 2024, subject to updates of certain aspects of our assumptions and plans in the BHP Annual Report 2025, Operating and Financial Review 9.8 – Climate change pdf BHP Economic Contribution Report 2024 pdf BHP Economic Contribution Report 2024 XML xml BHP Economic Contribution Report Extract 2024 pdf BHP Modern Slavery Statement 2024 pdf BHP GHG Emissions Calculation Methodology 2024 pdf BHP ESG Standards and Databook 2024 xlsx Límite organizativo de los informes de sostenibilidad, definiciones y cláusulas de exención de responsabilidad pdf Sustainability reporting organisational boundary, definitions and disclaimers pdf FY23 Reports BHP Annual Report 2023 pdf BHP Annual Report 2023 (ESEF/iXBRL with built-in iXBRL viewer) xhtml BHP Annual Report 2023 (ESEF/iXBRL) zip BHP Letter from the People and Remuneration Committee Chair 2023 pdf BHP Economic Contribution Report 2023 pdf BHP Economic Contribution Report 2023 XML xml BHP Modern Slavery Statement 2023 pdf BHP ESG Standards and Databook 2023 xlsx BHP Scopes 1, 2 and 3 Emissions Calculation Methodology 2023 pdf Sustainability reporting organisational boundary, definitions and disclaimers pdf FY22 Reports BHP Annual Report 2022 pdf BHP Annual Report 2022 (ESEF/iXBRL with built-in IXBRL viewer) xhtml BHP Annual Report 2022 (ESEF/iXBRL) zip BHP Economic Contribution Report pdf BHP Economic Contribution Report (XML) xml BHP Modern Slavery Statement 2022 pdf BHP Scope 1, 2 and 3 GHG Emissions Calculation Methodology 2022 pdf BHP ESG Standards and Databook 2022 xlsx Sustainability reporting organisational boundary and disclaimers pdf FY21 Reports BHP Annual Report 2021 pdf Economic Contribution Report 2021 pdf BHP Economic Contribution Report 2021 XML xml ESG Standards and Databook 2021 xlsx BHP Scope 1, 2 and 3 GHG Emissions Calculation Methodology 2021 pdf FY20 Reports BHP Annual Report 2020 pdf BHP Group Plc - Economic Contribution Report 2020 pdf Economic Contribution Report 2020 (XML) xml ESG Standards and databook 2020 xlsx © BHP 2026 About What we do Investors Sustainability Careers News Suppliers Contact us Follow us on Privacy Policy Modern Slavery Act Statement Terms of
```

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: risks

```text
risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulatory information Our position on climate change Operational GHG emission reductions Carbon offsets and natural climate solutions Value chain GHG emission reductions Transition to a net zero economy Physical climate-related risk and adaptation Advocacy on climate policy Equitable change and transition Climate Transition Action Plan Climate and nature Capability and culture Local communities Economic contribution Indigenous peoples Human rights Modern slavery statement BHP Foundation Health Safety Sexual harassment What are Tailings Storage Facilities? Tailings Storage Facility management Releases Image gallery Reports and Presentations Australia country program Canada country program Chile country program BHP Foundation board and governance How to speak up Look out for one another Care for our people and planet Work with integrity Protect our company Protect and respect information FutureFit Operations Services New to industry pathways in Australia Why BHP Canada Chile Malaysia and the Philippines Singapore Australia Rest of the world Australian programs Singapore programs US programs LGBT+ Inclusion BHP Inclusion and Diversity Storybook Our Global Inclusion and Diversity Council Wellbeing resources All investor resources Financial results & Operational reviews Annual reports Economic Contribution report Presentations & Briefings Economic & Commodity Outlook Dividends Shareholder online services Annual General meetings Shareholder Q&As Share price Corporate actions & historical share information Frequently Asked Questions Key contacts Ethics & business conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent How to speak up Look out for one another Care for our people & our planet Work with integrity Protect our company Protect & respect information Follow us on Home Investor hub Reports and presentations Annual Reports Annual Report 2025 How we create and deliver value. In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Read the report Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. Ross McEwan Chair Read the full message FY2025 at a glance Find out more about our 2025 results and performance 2Mt Record annual copper production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model Positioning for growth People Downloads We delivered another strong set of results in FY2025 enabled by our great people, the disciplined application of our strategy, world-class assets, operational excellence and through financial rigour underpinned by our Capital Allocation Framework (CAF). This enabled the Board to announce a final dividend of 60 US cents per share, taking the total dividends for the year to 110 US cents per share, or US$5.6 billion. Our approach aims to balance investment in growth with shareholder returns – as reflected in our dividend payout ratio of 55 per cent for FY2025. Strong results We can deliver a dividend of this scale because of our resilient portfolio and disciplined operational delivery, achieved amid a volatile external environment. We achieved an underlying EBITDA of US$26 billion, with a 53 per cent margin. We have averaged a margin of over 50 per cent for the past 20 years, which is a testament to our consistency and a sign of the resilience and stability of BHP. This year, we generated net operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we can control, with healthy volume growth and disciplined cost management. We saw record production volumes in iron ore and copper, and increased our steelmaking coal production on the prior financial year, excluding Blackwater and Daunia which we divested in
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: one-off items
- Unavailable reason: one_off_items was not identified in extracted ASX document text.

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we can control, with healthy volume growth and disciplined cost management. We saw record production volumes in iron ore and copper, and increased our steelmaking coal production on the prior financial year, excluding Blackwater and Daunia which we divested in CY2024. Importantly, we continued to be disciplined with our costs. Escondida delivered an 18 per cent unit cost reduction and WAIO remains the lowest-cost major iron ore producer in the world. Across the group, unit costs at our major assets were down 4.7 per cent year-on-year. 5 Value-adding investments and resilient balance sheet In FY2025, we invested US$9.8 billion in capital and exploration expenditure. We also invested US$2.1 billion to acquire a 50 per cent interest in the Josemaria and Filo del Sol deposits and form the Vicuña joint venture with Lundin Mining. The Filo del Sol deposit is one of the largest copper deposit discoveries in the last 30 years. With net debt of US$12.9 billion, our balance sheet remains strong. The resilience of our portfolio, track record of stable operations and robust financial performance has led to our improved debt servicing capacity. Accordingly, we are revising our net debt target range to US$10 billion to US$20 billion (from US$5 billion to US$15 billion). This will unlock the power of our balance sheet for our pipeline of projects we expect will deliver great value for our shareholders, partners and other stakeholders well into the future. How we create and deliver value The keys to our successful past and exciting future are the same – our people, capabilities, scale, portfolio and, in more recent times, the unique overarching way we work through the BHP Operating System (BOS). BOS differentiates our approach, makes improvement central to everyone’s role and provides for sustainable operating excellence year after year. We seek to use our capital carefully and effectively. We operate our assets efficiently. We have an overriding focus on safety. We embrace technology and innovation. We have a clear strategy and proven record of execution against it. We grow value through our large, long-life, quality assets in materials that improve standards of living and support decarbonisation and digitalisation, and through our differentiated focus on social value, which is integral to how we operate. We seek to extract materials as efficiently and effectively as we can while seeking to appropriately manage impacts on the planet. We choose to partner with peers, suppliers and customers where we believe we can innovate or create value together. View our business model Our portfolio A resource mix for today – and for the future. We have copper, which is used in electrification and renewable power and is important for digitalisation. We have iron ore, which is essential for making steel needed for construction, including renewables infrastructure. Our higher-quality steelmaking coal is used in the blast furnace process for making steel. We are developing a world-class potash asset. Potash is used in fertilisers to assist with food security for a growing population and more sustainable land use. We are also a major producer of uranium and gold, which are by-products of our copper production. Read more Social value< We are committed to social value and the responsible provision of commodities the world needs to develop, decarbonise and digitise. Social value creates business value. In FY2025, we continued to refine our approach to social value. We have a 2030 social value scorecard to monitor our progress. Each year since first publishing the social value scorecard in June 2022, we have reported performance against key metrics and the milestones for that year and set out new short-term milestones for the next year to demonstrate the pathway to FY2030. Read more See our 2030 social value scorecard Exceptional performance Enabled by the BHP Operating System (BOS), operational excellence underpins strong returns and investment growth. FY2025 was a standout year for BHP, marked by record production, continued sector-leading margins and disciplined capital allocation. At WAIO, we are the world’s lowest-cost major iron ore producer and have been for six years, and we have the best track record of delivering production against guidance amongst our competitors. BOS is our unique overarching management system that enables the right culture, routines, behaviours and leadership to deliver stable operating excellence and leading safety performance. It provides us with a competitive edge. Read more With our clear strategy and focus on creating and sustaining the right portfolio of the best assets with enhanced growth optionality, BHP is well placed to capitalise on the changes shaping our world. As the global population grows and urbanises and the world pursues decarbonisation, electrification and digitalisation, we are positioning our portfolio and pursuing multiple growth options to increase our exposure to these megatrends. Read more Unlocking growth at our assets Our biggest near-term growth levers are improving productivity at our existing assets and unlocking more of their potential. We have significant opportunities in our world-leading copper portfolio. These projects have potential to enable significant total annual copper production through the 2030s. Read more Growth through exploration, focused on copper In FY2025, we continued to strengthen our exploration portfolio, focusing primarily on copper opportunities. Our efforts spanned early-stage greenfield exploration, strategic alliances and the expansion of our Xplor accelerator program. Read more Safety Nothing is more important than protecting
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report
- Supports claims: segment table, product table, sector metrics

```text
production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets 5 Calculated on a copper equivalent production weighted average basis, based on FY2025 average realised prices for major assets including Escondida, Spence, Copper SA, WAIO and BMA. We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. Mike Henry CEO Read the full message Financial results Financial results Our business model Positioning for growth People Downloads We delivered another strong set of results in FY2025 enabled by our great people, the disciplined application of our strategy, world-class assets, operational excellence and through financial rigour underpinned by our Capital Allocation Framework (CAF). This enabled the Board to announce a final dividend of 60 US cents per share, taking the total dividends for the year to 110 US cents per share, or US$5.6 billion. Our approach aims to balance investment in growth with shareholder returns – as reflected in our dividend payout ratio of 55 per cent for FY2025. Strong results We can deliver a dividend of this scale because of our resilient portfolio and disciplined operational delivery, achieved amid a volatile external environment. We achieved an underlying EBITDA of US$26 billion, with a 53 per cent margin. We have averaged a margin of over 50 per cent for the past 20 years, which is a testament to our consistency and a sign of the resilience and stability of BHP. This year, we generated net operating cash flow of US$18.7 billion. After an adjusted effective tax rate including royalties of 44.6 per cent, our underlying attributable profit was US$10.2 billion. Our return on capital employed was strong at 20.6 per cent. Strong performance in areas we can control We continue to perform well in the areas we can control, with healthy volume growth and disciplined cost management. We saw record production volumes in iron ore and copper, and increased our steelmaking coal production on the prior financial year, excluding Blackwater and Daunia which we divested in CY2024. Importantly, we continued to be disciplined with our costs. Escondida delivered an 18 per cent unit cost reduction and WAIO remains the lowest-cost major iron ore producer in the world. Across the group, unit costs at our major assets were down 4.7 per cent year-on-year. 5 Value-adding investments and resilient balance sheet In FY2025, we invested US$9.8 billion in capital and exploration expenditure. We also invested US$2.1 billion to acquire a 50 per cent interest in the Josemaria and Filo del Sol deposits and form the Vicuña joint venture with Lundin Mining. The Filo del Sol deposit is one of the largest copper deposit discoveries in the last 30 years. With net debt of US$12.9 billion, our balance sheet remains strong. The resilience of our portfolio, track record of stable operations and robust financial performance has led to our improved debt servicing capacity. Accordingly, we are revising our net debt target range to US$10 billion to US$20 billion (from US$5 billion to US$15 billion). This will unlock the power of our balance sheet for our pipeline of projects we expect will deliver great value for our shareholders, partners and other stakeholders well into the future. How we create and deliver value The keys to our successful past and exciting future are the same – our people, capabilities, scale, portfolio and, in more recent times, the unique overarching way we work through the BHP Operating System (BOS). BOS differentiates our approach, makes improvement central to everyone’s role and provides for sustainable operating excellence year after year. We seek to use our capital carefully and effectively. We operate our assets efficiently. We have an overriding focus on safety. We embrace technology and innovation. We have a clear strategy and proven record of execution against it. We grow value through our large, long-life, quality assets in materials that improve standards of living and support decarbonisation and digitalisation, and through our differentiated focus on social value, which is integral to how we operate. We seek to extract materials as efficiently and effectively as we can while seeking to appropriately manage impacts on the planet. We choose to partner with peers, suppliers and customers where we believe we can innovate or create value together. View our business model Our portfolio A resource mix for today – and for the future. We have copper, which is used in electrification and renewable power and is important for digitalisation. We have iron ore, which is essential for making steel needed for construction, including renewables infrastructure. Our higher-quality steelmaking coal is used in the blast furnace process for making steel. We are developing a world-class potash asset. Potash is used in fertilisers to assist with food security for a growing
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://www.bhp.com/investor-hub/reports-and-presentations/annual-report

```text
Annual Report 2025 Search --> --> 🔍 --> Search Contact us English ES | Español 中文 | Chinese --> English ES | Español 中文 | Chinese Home --> About What we do Investor Hub Sustainability Careers News & Publications Suppliers Contact us Why our work matters Our future Our history Our strategy Operating ethically Our businesses Board & management Corporate governance Our code Products Global locations Reports & presentations Shareholder information Financial Calendar Market announcements Debt investors Consensus estimates Sustainability approach Value chain sustainability Nature and environmental performance Climate change Social performance Ethics and business conduct People Safety and health Tailings storage facilities BHP Foundation Australia Global careers Indigenous peoples and BHP Graduate and student programs Recruitment process Life at BHP Culture and rewards Inclusion and diversity Health and safety Fraudulent email scams News & publication library Image gallery BHP Insights Why work with us Find opportunities Become a supplier New and existing suppliers Global outlook Ethics and Business Conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Tax and transparency Non-Operated Joint Ventures Corporate governance Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent Copper Metallurgical coal Nickel Potash Iron ore Australia Brazil Canada - Jansen Chile Peru - Antamina United States Offices 2026 Financial Results 2025 Financial Results 2024 Financial Results 2023 Financial Results Annual Report 2025 Economic Contribution Report 2025 Past reports BHP Shareholder Q&A sessions Meetings Presentations and briefings Financial Calendar Current share price Shareholder online services Dividends Capital Management Program Demerger taxation information Boiler Room scams Onshore petroleum divestment Shareholder FAQs Offer for Anglo American Materiality assessment Social value Social investment Forum on corporate responsibility Sustainability-related risk management Modern slavery statement Water Shared Water Challenges Biodiversity and land Closure Regulatory information Our position on climate change Operational GHG emission reductions Carbon offsets and natural climate solutions Value chain GHG emission reductions Transition to a net zero economy Physical climate-related risk and adaptation Advocacy on climate policy Equitable change and transition Climate Transition Action Plan Climate and nature Capability and culture Local communities Economic contribution Indigenous peoples Human rights Modern slavery statement BHP Foundation Health Safety Sexual harassment What are Tailings Storage Facilities? Tailings Storage Facility management Releases Image gallery Reports and Presentations Australia country program Canada country program Chile country program BHP Foundation board and governance How to speak up Look out for one another Care for our people and planet Work with integrity Protect our company Protect and respect information FutureFit Operations Services New to industry pathways in Australia Why BHP Canada Chile Malaysia and the Philippines Singapore Australia Rest of the world Australian programs Singapore programs US programs LGBT+ Inclusion BHP Inclusion and Diversity Storybook Our Global Inclusion and Diversity Council Wellbeing resources All investor resources Financial results & Operational reviews Annual reports Economic Contribution report Presentations & Briefings Economic & Commodity Outlook Dividends Shareholder online services Annual General meetings Shareholder Q&As Share price Corporate actions & historical share information Frequently Asked Questions Key contacts Ethics & business conduct Competition law compliance Industry associations Interacting with governments Planning the closure of assets Social value Stewardship of our products Minerals Americas Minerals Australia Commercial BHP Ventures BHP Xplor BHP Invent How to speak up Look out for one another Care for our people & our planet Work with integrity Protect our company Protect & respect information Follow us on Home Investor hub Reports and presentations Annual Reports Annual Report 2025 How we create and deliver value. In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Read the report Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. Ross McEwan Chair Read the full message FY2025 at a glance Find out more about our 2025 results and performance 2Mt Record annual copper production, including highest copper production in 17 years at Escondida, a record at Spence and record Q4 production at Copper South Australia. 5% Reduction in operational GHG emissions (Scopes 1 and 2 emissions from our operated assets) from FY2024 1 US$46.8bn Our total economic contribution 2 US$19.5bn Profit from operations in FY2025 110 USc Shareholder cash dividends per share for FY2025 US$10.4bn Total payments to governments in FY2025 2 18% Reduction in high potential injury frequency on FY2024. 4 41.3% We have achieved gender balance across our employee workforce, with female employee representation reaching 41.3 per cent at 30 June 2025. 3 US$853m Record Indigenous procurement spend, up 40% on FY2024 1 For more information on the calculation of this metric and on our GHG emissions targets and goals, refer to OFR 9.8 2 For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025. 3 For more information on this metric and how we define gender balance refer to OFR 9.5. 4 Combined employee and contractor frequency per 1 million
```

### Section: asx_fallback_document / revenue_income_npat

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: revenue, income, NPAT

```text
income and retirement. Over the past five years, BHP has delivered more than US$50 billion in cash dividends to our shareholders. Our Capital Allocation Framework (CAF) promotes discipline in all our capital decisions and prioritises capital for safety and maintenance, balance sheet strength and a minimum dividend payout ratio of 50 per cent of underlying attributable profit at every reporting period. For FY2025, your Board determined dividends totalling 110 US cents a share. This represents a total distribution to shareholders of US$5.6 billion, or 55 per cent of the underlying attributable profit for FY2025. Building for the future Our performance allows us to plan for and invest in value adding growth projects. BHP has a strong growth pipeline of organic and greenfield projects in copper, iron ore and potash. Our growth strategy generates greater exposure to commodities that the world needs to reduce greenhouse gas emissions and as the population grows, continues to urbanise and seeks higher living standards. Continuing to evolve As we have for the past 140 years, we continued to position BHP’s portfolio to align to the global trends shaping our future. We have reshaped BHP’s portfolio to increase our exposure to future-facing commodities and higher-quality steelmaking materials. Our iron ore business is a critical part of our future and we have extended our lead as the lowest-cost major iron ore producer globally. We have achieved a world-leading position in copper, which is key to renewable energy, electric vehicles and data centres. We are developing a position in potash that will contribute to food security and more sustainable land use. We have focused our steelmaking coal portfolio on higher-quality coals preferred by our customers to produce steel for cities and infrastructure for decarbonisation. Today, we have a portfolio and options for growth that leave us well positioned to provide the commodities the world will need more of in the decades to come. Looking ahead Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. In FY2025, we showed that the consistent execution of our clear and simple strategy delivers results. BHP is an outstanding business in great shape and I am confident we can continue to create value for you, our partners and many other stakeholders in the year ahead and for decades to come. I look forward to meeting you at our Annual General Meeting. Thank you for your continued support. Ross McEwan Chair Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live.” 4 BHP Annual Report 2025 __PDF_PAGE__ page=7 Chief Executive Officer’s review Dear Shareholders, In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance. Most importantly, we did so safely. Nothing matters more than the safety of our people. We had no fatalities, and our total recordable injury and high potential injury frequency measures were both lower than the prior year. This improvement has been driven by significant investments in engineering controls through our Fatality Elimination Program, continuous improvement of how leaders support their teams through Field Leadership and the operating discipline delivered through the BHP Operating System. Executing well and delivering on our promises builds trust. Combined with the quality of our assets and the attractiveness of our chosen commodities, this gives us resilience and the foundation for long-term value growth. Mining now in the global spotlight We’re seeing an increasing focus on critical minerals supply and supply chain security across the globe. This is happening against a backdrop of growing geopolitical and trade tensions, and reflects a growing understanding and acceptance of the critical role mining will play in supporting national security, energy transitions and technology development. There is also a clearer recognition of the significant economic opportunity that accompanies investment in resources projects. Many resources producing nations are taking aggressive steps to improve competitiveness and to attract global capital to invest in new resource project opportunities. We continue to advocate for policies that drive productivity, encourage investment and spur economic growth. We engage with political leaders, policymakers and industry counterparts regularly, making the case for the settings to unlock resources for the shared benefit of nations, our sector and your company. Creating social value Our approach to social value and sustainability differentiates BHP and is essential to the creation of long-term shareholder value. We’re seeing practical challenges affect the pace of the global energy transition, including the development of the necessary technology at competitive cost. BHP’s climate commitments remain unchanged and we remain on track to meet our FY2030 operational decarbonisation target. We continue to partner with First Nations and Indigenous peoples around the world. Over 90 per cent of BHP’s operations are located on or near the traditional lands of Indigenous peoples – and we seek to build long-term relationships based on trust and mutual benefit. The significant uplift in our spend with Indigenous businesses during the year is a clear demonstration of this. We’re focused on building multi-year partnerships that enable Indigenous businesses to secure investment, grow with confidence and build their capability to provide goods and services to large companies like BHP. A culture
```

### Section: asx_fallback_document / eps_dps

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: EPS, DPS, dividends

```text
Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and voluntary investment in social projects across the communities where we operate during the year. This was 87% of our total economic contribution. __PDF_PAGE__ page=6 Chair’s review Dear Shareholders, I am pleased to provide BHP’s Annual Report for FY2025. It is an honour and a privilege to be your new Chair. Your Board and I are excited about the future of this great company. I want to acknowledge the contribution of my predecessor, Ken MacKenzie, who led the Board as Chair for seven years. I thank Ken for his outstanding service to the Board and BHP during his tenure. Ken leaves a lasting legacy at BHP. In times of global uncertainty, stability and resilience matter. BHP has stood for both for 140 years. What we do matters. The world needs more of the materials we produce to develop, decarbonise and digitalise. BHP has a substantial role to play in producing the vital materials the world needs and in contributing to the success of the global economy. We remain well positioned to meet global demand for the commodities we produce in order to create long-term value for our shareholders, local communities, customers, suppliers and partners. Rewarding shareholders BHP has a simple, clear strategy that is resilient amid any operating environment. Executing this strategy has allowed us to perform well through mining and economic cycles. The company performed strongly in FY2025, generating significant cash flow. Healthy cash returns are important for shareholders, including the hundreds of thousands of retail shareholders who rely on BHP to support their income and retirement. Over the past five years, BHP has delivered more than US$50 billion in cash dividends to our shareholders. Our Capital Allocation Framework (CAF) promotes discipline in all our capital decisions and prioritises capital for safety and maintenance, balance sheet strength and a minimum dividend payout ratio of 50 per cent of underlying attributable profit at every reporting period. For FY2025, your Board determined dividends totalling 110 US cents a share. This represents a total distribution to shareholders of US$5.6 billion, or 55 per cent of the underlying attributable profit for FY2025. Building for the future Our performance allows us to plan for and invest in value adding growth projects. BHP has a strong growth pipeline of organic and greenfield projects in copper, iron ore and potash. Our growth strategy generates greater exposure to commodities that the world needs to reduce greenhouse gas emissions and as the population grows, continues to urbanise and seeks higher living standards. Continuing to evolve As we have for the past 140 years, we continued to position BHP’s portfolio to align to the global trends shaping our future. We have reshaped BHP’s portfolio to increase our exposure to future-facing commodities and higher-quality steelmaking materials. Our iron ore business is a critical part of our future and we have extended our lead as the lowest-cost major iron ore producer globally. We have achieved a world-leading position in copper, which is key to renewable energy, electric vehicles and data centres. We are developing a position in potash that will contribute to food security and more sustainable land use. We have focused our steelmaking coal portfolio on higher-quality coals preferred by our customers to produce steel for cities and infrastructure for decarbonisation. Today, we have a portfolio and options for growth that leave us well positioned to provide the commodities the world will need more of in the decades to come. Looking ahead Your company is well placed to meet the challenges of our rapidly changing world. It is the combination of our outstanding people, world-class assets and execution excellence that creates long-term value for our shareholders and for the communities where we live. In FY2025, we showed that the consistent execution of our clear and simple strategy delivers results. BHP is an outstanding business in great shape and I am confident we can continue to create value for you, our partners and many other stakeholders in the year ahead and for decades to come. I look forward to meeting you at our Annual General Meeting. Thank you for your continued support. Ross McEwan Chair Your company is well placed to meet the challenges of our rapidly changing world. It
```

### Section: asx_fallback_document / management_discussion_analysis

- Section name: management_discussion_analysis
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: management discussion, MD&A, outlook

```text
Operating and Financial Review 1 Why BHP 6 2 Our business 8 2.1 Our portfolio 8 2.2 Where we operate 10 3 Our key differentiators 11 4 Positioning for growth 12 5 Financial review 13 Chief Financial Officer’s review 13 5.1 Group overview 14 5.2 Key performance indicators 14 5.3 Financial results 15 5.4 Debt and sources of liquidity 17 6 Our assets 19 6.1 Copper 19 6.2 Iron ore 21 6.3 Coal 22 6.4 Potash 23 6.5 Nickel 24 6.6 Commercial 24 7 How we manage risk 25 8 Safety 27 9 Sustainability 29 9.1 Our sustainability approach 29 9.2 Sustainability governance 30 9.3 Material sustainability topics (including human rights) 30 9.4 2030 goals and social value scorecard 31 9.5 People 33 9.6 Health 35 9.7 Ethics and business conduct 37 9.8 Climate change 39 9.9 Nature and environmental performance 53 9.10 Tailings storage facilities 57 9.11 Community 57 9.12 Indigenous peoples 59 9.13 Value chain sustainability 61 9.14 Independent Assurance Report to the Management and Directors of BHP Group Limited 62 10 Samarco 64 11 Risk factors 66 12 Performance by commodity 72 12.1 Copper 72 12.2 Iron ore 73 12.3 Coal 73 12.4 Other assets 74 12.5 Impact of changes to commodity prices 74 13 Non-IFRS financial information 75 13.1 Definition and calculation of non-IFRS financial information 84 13.2 Definition and calculation of principal factors 85 14 Other information 86 14.1 Company details 86 14.2 Forward-looking statements 86 Corporate Governance Statement 1 Corporate governance at BHP 87 2 FY2025 corporate governance highlights 87 3 BHP’s governance structure 88 4 Board composition and succession 89 5 Board Committees 94 6 Management 96 7 Shareholders and reporting 97 8 Culture and conduct 98 9 Risk management and assurance 99 10 US requirements 100 Directors’ Report 1 Review of operations, principal activities and state of affairs 101 2 Directors 101 3 Share interests 102 4 Share capital and buy-back programs 102 5 Group Company Secretary 102 6 Indemnities and insurance 102 7 Dividends 103 8 Auditors 103 9 Non-audit services 103 10 Exploration, research and development 103 11 ASIC Instrument 2016/191 103 12 Proceedings on behalf of BHP Group Limited 103 13 Performance in relation to environmental regulation 103 14 Additional information 103 Remuneration Report Letter from the People and Remuneration Committee Chair 104 Remuneration at a glance 105 Our Key Management Personnel 106 Remuneration Governance 106 Paying competitively 107 Key terms of our variable remuneration framework and equity plans 108 Remuneration mix 109 Remuneration for Executive KMP 110 Remuneration for Non-executive Directors 113 Statutory remuneration and other disclosures 114 Additional Information 1 Information on mining operations 188 2 Financial information summary 198 3 Financial information by commodity 199 4 Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female
```

### Section: asx_fallback_document / cash_flow_statement

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: cash flow statement, operating cash flow

```text
operating cash flow Maintenance and decarbonisation capital Strong balance sheet Excess cash Minimum 50% payout ratio dividend 50 Maximise value and returns Exceptional performance Operating excellence Enabled by BOS, operational excellence underpins strong returns and investment growth. FY2025 was a standout year for BHP, marked by record production, continued sector-leading margins and disciplined capital allocation. We are the world’s lowest-cost major iron ore producer and have been for six years, and we have the best track record of delivering production against guidance amongst our competitors. Operating and financial strength The strength of our portfolio, our operating excellence and financial rigour from our disciplined application of the CAF enable us to deliver strong and consistent returns. We achieved net operating cash flow of US$18.7 billion in FY2025. Our net operating cash flow has been more than US$15 billion for all but one of the past 16 years. Over the past decade, our EBITDA margin has averaged 55 per cent and it is approximately 10 percentage points above our closest major competitor. Project excellence Project excellence is a major focus and we continue to build strong capability in this area. We have a disciplined approach to the execution of projects with focus on predictability and efficiency, as shown through our delivery of the South Flank mine and the Port Debottlenecking Project 1 at WAIO, and the Spence Growth Option in Chile. Technology and innovation In FY2025, we launched a refreshed Technology Strategy to accelerate the role of technology as a key enabler of our business. This strategy positions us to harness data, digital solutions and innovation to improve safety, enhance productivity and unlock long-term value across our global operations. Technology supports every part of our value chain – from exploration and processing to production and logistics. We use automation, artificial intelligence (AI) and data analytics to manage risk, improve asset performance and support our decision-making. Our systems achieve critical technology service availability nearly 100 per cent of the time, supporting the safe and continuous operation of our operated assets and functions. From a safety perspective, our strategy involves assessing new technologies, such as proximity and edge detection systems on mobile equipment and vehicles. AI is also expected to play an increasingly prominent role in our operations and business. By improving how we use data and digital tools, we aim to shorten innovation cycles, reduce operational variability and accelerate value creation. These efforts are already delivering results in areas such as maintenance optimisation, supply chain planning and frontline safety. For more information refer to OFR 8 1. Based on a ‘point-in-time’ snapshot of employees as at 30 June 2025, including employees on extended absence. Contractor data is collected from internal organisation systems and averaged for a 10-month period, July 2024 to April 2025. 2. Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets. 11 Overview Additional InformationFinancial StatementsGovernanceContents Operating and Financial Review __PDF_PAGE__ page=14 With our clear strategy and focus on creating and sustaining the right portfolio of the best assets with enhanced growth optionality, BHP is well placed to capitalise on the changes shaping our world. Our global copper growth program Our biggest near-term growth levers are improving productivity at our existing assets and unlocking more of their potential. We have significant opportunities in our world-leading copper portfolio. These projects have potential to enable significant total annual copper production through the 2030s. In Chile, we have a strong pipeline of organic growth options with attractive returns across our Escondida and Pampa Norte assets, which we expect will enable copper production in Chile to average ~1.4 Mtpa through the 2030s. In South Australia, we are assessing the pathway to deliver >500 kilotonnes per annum (ktpa) of copper production (>700 ktpa CuEq) and a strategy to deliver up to 650 ktpa copper production from the 100 per cent-owned Copper South Australia. During FY2025, we have further optimised the sequence of this growth program. Vicuña: an exciting new venture BHP is pleased to be partnering with Canada’s Lundin Mining in the Vicuña joint venture, an exciting new copper growth opportunity for both companies in Argentina and Chile. In January 2025, BHP and Lundin Mining formed the Vicuña joint venture to hold the combined Josemaria and Filo del Sol projects located on the Argentina-Chile border. The joint venture will create a long-term partnership between BHP and Lundin Mining to jointly develop an emerging copper district with world-class potential. The proximity of Josemaria and Filo del Sol allows for infrastructure to be shared between the deposits, with greater economies of scale and increased optionality for staged expansions, as well as the incorporation of future exploration as the development matures. Unlocking further iron ore growth at WAIO WAIO has been the world’s lowest-cost major iron ore producer for the last six years. WAIO was designed with an initial capacity of 240 Mtpa (100 per cent basis). In FY2025, WAIO produced a record 290 Mt (100 per cent basis) demonstrating supply chain excellence from pit to port. We have approved the commissioning of a sixth car dumper (CD6) and related infrastructure at Port Hedland for a total investment of ~US$0.9 billion.1 CD6 will create capacity to maintain production of >305 Mtpa (100 per cent basis) from Q4 FY2028 through a period of planned major CD renewals beginning in FY2029. It will also improve our ore blending and screening capability at the port. Our position in potash Potash is a fertiliser and can enable more efficient and sustainable farming. We believe potash is going to be
```

### Section: asx_fallback_document / operating_cash_flow

- Section name: operating_cash_flow
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: operating cash flow

```text
operating cash flow Maintenance and decarbonisation capital Strong balance sheet Excess cash Minimum 50% payout ratio dividend 50 Maximise value and returns Exceptional performance Operating excellence Enabled by BOS, operational excellence underpins strong returns and investment growth. FY2025 was a standout year for BHP, marked by record production, continued sector-leading margins and disciplined capital allocation. We are the world’s lowest-cost major iron ore producer and have been for six years, and we have the best track record of delivering production against guidance amongst our competitors. Operating and financial strength The strength of our portfolio, our operating excellence and financial rigour from our disciplined application of the CAF enable us to deliver strong and consistent returns. We achieved net operating cash flow of US$18.7 billion in FY2025. Our net operating cash flow has been more than US$15 billion for all but one of the past 16 years. Over the past decade, our EBITDA margin has averaged 55 per cent and it is approximately 10 percentage points above our closest major competitor. Project excellence Project excellence is a major focus and we continue to build strong capability in this area. We have a disciplined approach to the execution of projects with focus on predictability and efficiency, as shown through our delivery of the South Flank mine and the Port Debottlenecking Project 1 at WAIO, and the Spence Growth Option in Chile. Technology and innovation In FY2025, we launched a refreshed Technology Strategy to accelerate the role of technology as a key enabler of our business. This strategy positions us to harness data, digital solutions and innovation to improve safety, enhance productivity and unlock long-term value across our global operations. Technology supports every part of our value chain – from exploration and processing to production and logistics. We use automation, artificial intelligence (AI) and data analytics to manage risk, improve asset performance and support our decision-making. Our systems achieve critical technology service availability nearly 100 per cent of the time, supporting the safe and continuous operation of our operated assets and functions. From a safety perspective, our strategy involves assessing new technologies, such as proximity and edge detection systems on mobile equipment and vehicles. AI is also expected to play an increasingly prominent role in our operations and business. By improving how we use data and digital tools, we aim to shorten innovation cycles, reduce operational variability and accelerate value creation. These efforts are already delivering results in areas such as maintenance optimisation, supply chain planning and frontline safety. For more information refer to OFR 8 1. Based on a ‘point-in-time’ snapshot of employees as at 30 June 2025, including employees on extended absence. Contractor data is collected from internal organisation systems and averaged for a 10-month period, July 2024 to April 2025. 2. Combined employee and contractor frequency per 1 million hours worked. Excludes OZ Minerals Brazil assets. 11 Overview Additional InformationFinancial StatementsGovernanceContents Operating and Financial Review __PDF_PAGE__ page=14 With our clear strategy and focus on creating and sustaining the right portfolio of the best assets with enhanced growth optionality, BHP is well placed to capitalise on the changes shaping our world. Our global copper growth program Our biggest near-term growth levers are improving productivity at our existing assets and unlocking more of their potential. We have significant opportunities in our world-leading copper portfolio. These projects have potential to enable significant total annual copper production through the 2030s. In Chile, we have a strong pipeline of organic growth options with attractive returns across our Escondida and Pampa Norte assets, which we expect will enable copper production in Chile to average ~1.4 Mtpa through the 2030s. In South Australia, we are assessing the pathway to deliver >500 kilotonnes per annum (ktpa) of copper production (>700 ktpa CuEq) and a strategy to deliver up to 650 ktpa copper production from the 100 per cent-owned Copper South Australia. During FY2025, we have further optimised the sequence of this growth program. Vicuña: an exciting new venture BHP is pleased to be partnering with Canada’s Lundin Mining in the Vicuña joint venture, an exciting new copper growth opportunity for both companies in Argentina and Chile. In January 2025, BHP and Lundin Mining formed the Vicuña joint venture to hold the combined Josemaria and Filo del Sol projects located on the Argentina-Chile border. The joint venture will create a long-term partnership between BHP and Lundin Mining to jointly develop an emerging copper district with world-class potential. The proximity of Josemaria and Filo del Sol allows for infrastructure to be shared between the deposits, with greater economies of scale and increased optionality for staged expansions, as well as the incorporation of future exploration as the development matures. Unlocking further iron ore growth at WAIO WAIO has been the world’s lowest-cost major iron ore producer for the last six years. WAIO was designed with an initial capacity of 240 Mtpa (100 per cent basis). In FY2025, WAIO produced a record 290 Mt (100 per cent basis) demonstrating supply chain excellence from pit to port. We have approved the commissioning of a sixth car dumper (CD6) and related infrastructure at Port Hedland for a total investment of ~US$0.9 billion.1 CD6 will create capacity to maintain production of >305 Mtpa (100 per cent basis) from Q4 FY2028 through a period of planned major CD renewals beginning in FY2029. It will also improve our ore blending and screening capability at the port. Our position in potash Potash is a fertiliser and can enable more efficient and sustainable farming. We believe potash is going to be
```

### Section: asx_fallback_document / free_cash_flow_or_cash_movement

- Section name: free_cash_flow_or_cash_movement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: free cash flow, cash movement

```text
cash movements in FY2025. Year ended 30 June 2025 US$M 2024 US$M Net debt at the beginning of the period (9,120) (11,166) Net operating cash flows 18,692 20,665 Net investing cash flows (13,350) (8,762) Net financing cash flows (5,971) (11,669) Net (decrease)/increase in cash and cash equivalents (629) 234 Carrying value of interest bearing liability net (proceeds)/repayments (2,454) 2,236 Carrying value of debt related instruments settlements 147 321 Carrying value of cash management related instruments proceeds (195) (361) Fair value change on hedged loans1 (263) 214 Fair value change on hedged derivatives 1 290 (188) Foreign currency exchange rate changes on cash and cash equivalents 24 (159) Lease additions (excluding leases associated with index-linked freight contracts) (547) (429) Divestment of subsidiaries and operations − 60 Other (177) 118 Non-cash movements (673) (384) Net debt at the end of the period (12,924) (9,120) 1. The Group hedges against the volatility in both exchange and interest rates on debt, and also exchange rates on cash, with associated movements in derivatives reported in Other financial assets/liabilities as effective hedged derivatives (cross currency and interest rate swaps), in accordance with accounting standards. For more information refer to Financial Statements note 24 ‘Financial risk management’. Dividends Our dividend policy provides for a minimum 50 per cent payout of Underlying attributable profit at every reporting period. The minimum dividend payment for the second half of FY2025 was US$0.50 per share. The Board determined to pay an additional amount of US$0.10 per share, taking the final dividend to US$0.60 per share (US$3.0 billion). In total, cash dividends of US$5.6 billion (US$1.10 per share) have been determined for FY2025. 5 Financial review continued 18 BHP Annual Report 2025 __PDF_PAGE__ page=21 6 Our assets 6.1 Copper Escondida Overview Escondida (BHP ownership: 57.5 per cent), located in the Atacama Desert in northern Chile, is a leading producer of copper concentrate and cathodes, with by-products including gold and silver. Escondida’s two open-cut pits feed three concentrator plants, as well as two leaching operations. Key developments in FY2025 Escondida achieved its highest production in 17 years, increasing 16 per cent year-on-year due to record concentrator throughput, improved recoveries, higher concentrator feed grade of 1.02 per cent (FY2024: 0.88 per cent) and the Full SaL leaching project, which achieved first production in Q4 FY2025. Escondida Norte pit achieved the first full autonomous haulage in FY2025 with 33 trucks operating at the end of June 2025. Escondida successfully completed negotiations for a new collective agreement with the Union N°1 of Operators and Maintainers, effective for 36 months from 2 August 2024; the associated industrial action prior to the finalisation of negotiations did not have a material impact on production during Q1 as a result of mitigating actions taken by management, including mine resequencing and prioritisation of ore movement. Escondida also completed negotiations with the Union N°3 of Operators and Maintainers, effective for 36 months from 20 December 2024. Full SaL, a BHP-designed leaching technology, delivered first production during FY2025. We expect it to produce ~410 kt in copper cathodes at Escondida over a 10-year period through improved recoveries and shorter leach cycle times. In November 2024, we outlined our attractive Escondida Growth Program at our Chilean copper site tour, with low capital intensity options in both concentrator and leaching pathways. Since then, we have identified several positive initiatives to improve the capital efficiency, production profile and value of the Escondida growth program. Near term these include several low capital intensity initiatives that can be executed immediately across the Laguna Seca concentrators; while we also plan to extend the life of the Los Colorados concentrator by ~6–12 months and, in parallel, optimise the demolition process to allow earlier access to high grade PL2 zone ore to offset the impact of this extension. Our permitting strategy has progressed as expected and the first permit submitted in March 2025 will enable critical works to achieve our optimised production plan. Permitting for the new concentrator is under preparation and will be submitted by the end of FY2026. We continue to study various leaching technologies, with each at different stages of evaluation. CHILE BOLIVIA ARGENTINA PERU Iquique Pacific Ocean Tocopilla Antofagasta Mejillones Calama Pica Spence Minera Escondida Cerro Colorado CHILE BOLIVIA ARGENTINA PERU Iquique Pacific Ocean Tocopilla Antofagasta Mejillones Calama Pica Spence Minera Escondida Cerro Colorado Chile Bolivia Existing operations Township Escondida and Pampa Norte Production for FY2026 is expected to be between 1,150 and 1,250 kt. Concentrator feed grade for FY2026 is expected to be lower than FY2025 at approximately 0.85 per cent. Pampa Norte Overview Pampa Norte (BHP ownership: 100 per cent) consists of two assets in the Atacama Desert in northern Chile – Spence and Cerro Colorado. Both are open-cut mines. Spence produces copper cathodes and copper concentrate, with by-products including gold, silver and molybdenum. Cerro Colorado produced copper cathodes up until the asset entered temporary care and maintenance in December 2023. Key developments in FY2025 Spence copper production increased 5 per cent to a record 268 kt due to improved stacked feed grade. Concentrator throughput, feed grade and recovery were broadly in line with the prior period. Production at Spence for FY2026 is expected to be between 230 and 250 kt due to expected lower concentrator feed grades and increased volume of transitional ore processed. Cerro Colorado transitioned to temporary care and maintenance in December 2023 and we are continuing to study the application of BHP’s SaL 1 leaching technology to
```

### Section: asx_fallback_document / cash_debt_gearing

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: cash, debt, gearing, capital

```text
Debt and sources of liquidity 17 6 Our assets 19 6.1 Copper 19 6.2 Iron ore 21 6.3 Coal 22 6.4 Potash 23 6.5 Nickel 24 6.6 Commercial 24 7 How we manage risk 25 8 Safety 27 9 Sustainability 29 9.1 Our sustainability approach 29 9.2 Sustainability governance 30 9.3 Material sustainability topics (including human rights) 30 9.4 2030 goals and social value scorecard 31 9.5 People 33 9.6 Health 35 9.7 Ethics and business conduct 37 9.8 Climate change 39 9.9 Nature and environmental performance 53 9.10 Tailings storage facilities 57 9.11 Community 57 9.12 Indigenous peoples 59 9.13 Value chain sustainability 61 9.14 Independent Assurance Report to the Management and Directors of BHP Group Limited 62 10 Samarco 64 11 Risk factors 66 12 Performance by commodity 72 12.1 Copper 72 12.2 Iron ore 73 12.3 Coal 73 12.4 Other assets 74 12.5 Impact of changes to commodity prices 74 13 Non-IFRS financial information 75 13.1 Definition and calculation of non-IFRS financial information 84 13.2 Definition and calculation of principal factors 85 14 Other information 86 14.1 Company details 86 14.2 Forward-looking statements 86 Corporate Governance Statement 1 Corporate governance at BHP 87 2 FY2025 corporate governance highlights 87 3 BHP’s governance structure 88 4 Board composition and succession 89 5 Board Committees 94 6 Management 96 7 Shareholders and reporting 97 8 Culture and conduct 98 9 Risk management and assurance 99 10 US requirements 100 Directors’ Report 1 Review of operations, principal activities and state of affairs 101 2 Directors 101 3 Share interests 102 4 Share capital and buy-back programs 102 5 Group Company Secretary 102 6 Indemnities and insurance 102 7 Dividends 103 8 Auditors 103 9 Non-audit services 103 10 Exploration, research and development 103 11 ASIC Instrument 2016/191 103 12 Proceedings on behalf of BHP Group Limited 103 13 Performance in relation to environmental regulation 103 14 Additional information 103 Remuneration Report Letter from the People and Remuneration Committee Chair 104 Remuneration at a glance 105 Our Key Management Personnel 106 Remuneration Governance 106 Paying competitively 107 Key terms of our variable remuneration framework and equity plans 108 Remuneration mix 109 Remuneration for Executive KMP 110 Remuneration for Non-executive Directors 113 Statutory remuneration and other disclosures 114 Additional Information 1 Information on mining operations 188 2 Financial information summary 198 3 Financial information by commodity 199 4 Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and
```

### Section: asx_fallback_document / segment_product_performance

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: segment performance, sector metrics

```text
Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and voluntary investment in social projects across the communities where we operate during the year. This was 87% of our total economic contribution. __PDF_PAGE__ page=6 Chair’s review Dear Shareholders, I am pleased to provide BHP’s Annual Report for FY2025. It is an honour and a privilege to be your new Chair. Your Board and I are excited about the future of this great company. I want to acknowledge the contribution of my predecessor, Ken MacKenzie, who led the Board as Chair for seven years. I thank Ken for his outstanding service to the Board and BHP during his tenure. Ken leaves a lasting legacy at BHP. In times of global uncertainty, stability and resilience matter. BHP has stood for both for 140 years. What we do matters. The world needs more of the materials we produce to develop, decarbonise and digitalise. BHP has a substantial role to play in producing the vital materials the world needs and in contributing to the success of the global economy. We remain well positioned to meet global demand for the commodities we produce in order to create long-term value for our shareholders, local communities, customers, suppliers and partners. Rewarding shareholders BHP has a simple, clear strategy that is resilient amid any operating environment. Executing this strategy has allowed us to perform well through mining and economic cycles. The company performed strongly in FY2025, generating significant cash flow. Healthy cash returns are important for shareholders, including the hundreds of thousands of retail shareholders who rely on BHP to support their income and retirement. Over the past five years, BHP has delivered more than US$50 billion in cash dividends to our shareholders. Our Capital Allocation Framework (CAF) promotes discipline in all our capital decisions and prioritises capital for safety and maintenance, balance sheet strength and a minimum dividend payout ratio of 50 per cent of underlying attributable profit at every reporting period. For FY2025, your Board determined dividends totalling 110 US cents a share. This represents a total distribution to shareholders of US$5.6 billion, or 55 per cent of the underlying attributable profit for FY2025. Building for the future Our performance allows us to plan for and invest in value adding growth projects. BHP has a strong growth pipeline of organic and greenfield projects in copper, iron ore and potash. Our growth strategy generates greater exposure to commodities that the world needs to reduce greenhouse gas emissions and
```

### Section: asx_fallback_document / management_commentary_outlook

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: outlook, management commentary

```text
forecast or production target and investors should not rely on this aspirational statement when making any investment decisions. The statement is aspirational as it is contingent on potential increases in production rates, as well as potential from non-operated joint ventures and exploration programs (which are uncertain and may not be realised). The pathway is subject to the completion of technical studies to support Mineral Resource and Ore Reserves estimates, capital allocation, regulatory approvals, market capacity and, in certain cases, the development of exploration assets, in which factors are uncertain. 2. BHP internal analysis based on WAIO C1 reported unit costs compared to publicly available unit costs reported by major competitors (including Fortescue, Rio Tinto and Vale), adjusted based on publicly available financial information. 8 BHP Annual Report 2025 __PDF_PAGE__ page=11 Third-consecutive full-year production record 263 Mt 1% on FY2024 Focusing on higher-quality product 18 Mt 19% on FY2024 Steelmaking coal We continue to focus our steelmaking coal operations in Queensland on higher-quality product and have one of the lowest GHG emission production intensities of benchmarked export steelmaking coal mines.3 Excluding the contribution of the Blackwater and Daunia mines, which were divested in FY2024, production increased 5 per cent to 18 Mt in FY2025 (36 Mt 100 per cent basis). Raw coal inventory levels increased 12 per cent. The strong performance was underpinned by improved truck productivity and led to increased production across all open-cut mines. Our focus on rebuilding raw coal inventory enabled us to stabilise operating performance We are developing one of the world’s largest potash mines in Canada. Jansen will increase our product diversification, customer base and operating footprint, and expand our business into a future growth market. Jansen Stage 1 (JS1) was 68 per cent complete by the end of FY2025. In July 2025, we announced updates relating to the Jansen potash project. We estimate capital expenditure for JS1 to increase from our original estimate of US$5.7 billion to be in the range of US$7.0 billion to US$7.4 billion including contingencies, and first production to revert back to the original schedule of mid-CY2027. We expect to update the market on JS1’s timing and optimised capital expenditure estimate in the second half of FY2026. Major global producer by the end of the decade US$7.0–US$7.4bn Estimated capital expenditure for Jansen Stage 1 Potash 3. For CY2024, the GHG emissions intensity of our production of our commodities is estimated to rank in the first quartile for our iron ore and sitting across first and second quartiles for copper and steelmaking coal mines of global mining operations analysed by CRU. This analysis is based on CY2024 data from CRU (as CRU data is prepared on a calendar year basis) and includes CRU’s assumptions and estimates of BHP’s operations. For more information on how the GHG emission intensity for our iron ore, and copper, and steelmaking coal mines has been calculated and compared refer to the BHP ESG Standards and Databook 2025 available at bhp.com/ESGSD2025. We have decided to extend the execution of JS2 by two years, shifting first production from FY2029 to FY2031, as part of our regular review of capex sequencing under the Capital Allocation Framework. JS2’s capital expenditure remains under review and we expect to update the market on JS2’s optimised capital expenditure estimate in the second half of FY2026. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. For more information refer to OFR 6.4 across the asset and increase production despite geotechnical challenges at Broadmeadow and a 36 per cent year-on-year increase in rainfall. Production for FY2026 is expected to increase to between 18 and 20 Mt (36 and 40 Mt on a 100 per cent basis), weighted to the second half, while unit costs are expected to decrease with guidance between US$116/t and US$128/t as we push to further improve productivity. Our focus on improving value chain stability will continue into CY2027 as we continue to rebuild raw coal inventory to sustainable levels and normalising strip ratios. For more information refer to OFR 6.3 9 Overview Additional InformationFinancial StatementsGovernanceContents Operating and Financial Review __PDF_PAGE__ page=12 2.2 Where we operate 2 Our business continued Total payments to governments3 (US$) $6.8bn Australia $10.4bn Global total We remain one of the largest taxpayers in Australia, contributing US$6.8 billion in FY2025. During the last decade, we paid US$98.1 billion globally in taxes, royalties and other payments to governments, including US$78.1 billion in Australia.” Vandita Pant Chief Financial Officer $49m Canada $3.2bn Chile $290m Rest of the world4 NickelPotashCoalIron oreCopper Australia Chile Canada Rest of the world4 1. This includes contribution to suppliers, wages and benefits for employees, dividends, taxes and royalties, and voluntary social investment. For more information refer to the Economic Contribution Report 2025. 2. Based on a ‘point-in-time’ snapshot of employees as at 30 June 2025, including employees on extended absence. Contractor data is collected from internal organisation systems and averaged for a 10-month period, July 2024 to April 2025. 3. For more information refer to the Economic Contribution Report 2025. 4. Rest of the world includes consolidation adjustments. No. of employees and contractors2 91,304 Global total 5,875 35,911 2,696 46,822 Payments to suppliers3 (US$) $24.8bn Global total $2.5bn $7.3bn $1.8bn $13.2bn Total economic contribution1 (US$) $46.8bn Global total $3.6bn $11.4bn $2.0bn $29.8bn Western Australia Iron Ore Western Australia Nickel BHP Mitsubishi Alliance NSW Energy Coal Copper South Australia London Gurgaon Singapore Perth Adelaide Melbourne Brisbane Kuala Lumpur Manila
```

### Section: asx_fallback_document / dividends_capital_management

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: dividends, capital management

```text
buy-back programs 102 5 Group Company Secretary 102 6 Indemnities and insurance 102 7 Dividends 103 8 Auditors 103 9 Non-audit services 103 10 Exploration, research and development 103 11 ASIC Instrument 2016/191 103 12 Proceedings on behalf of BHP Group Limited 103 13 Performance in relation to environmental regulation 103 14 Additional information 103 Remuneration Report Letter from the People and Remuneration Committee Chair 104 Remuneration at a glance 105 Our Key Management Personnel 106 Remuneration Governance 106 Paying competitively 107 Key terms of our variable remuneration framework and equity plans 108 Remuneration mix 109 Remuneration for Executive KMP 110 Remuneration for Non-executive Directors 113 Statutory remuneration and other disclosures 114 Additional Information 1 Information on mining operations 188 2 Financial information summary 198 3 Financial information by commodity 199 4 Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and voluntary investment in social projects across the communities where we operate during the year. This was 87% of our total economic contribution. __PDF_PAGE__ page=6 Chair’s review Dear Shareholders, I am pleased to provide BHP’s Annual Report for FY2025. It is an honour and a privilege to be your new Chair. Your Board and I are excited about the future of this great company. I want to acknowledge the contribution of my predecessor, Ken MacKenzie, who led the Board as Chair for seven years. I thank Ken for his outstanding service to the Board and BHP during his tenure. Ken leaves a lasting legacy at BHP. In times of global uncertainty, stability and resilience matter. BHP has stood for both for 140 years. What we do matters. The world needs more of the materials we produce to develop, decarbonise and digitalise. BHP has a substantial role to play in producing the vital materials the world needs and in contributing to the success of the global economy. We remain well positioned to meet global demand for the commodities we produce in order to create long-term value for our shareholders, local communities, customers, suppliers and partners. Rewarding shareholders BHP has a simple, clear strategy that is resilient amid any operating environment. Executing this strategy has allowed us to perform well through mining and economic cycles. The company performed strongly in FY2025, generating significant cash flow. Healthy cash returns are important for shareholders, including the hundreds of thousands of retail shareholders who rely on BHP to support their income and retirement. Over the
```

### Section: asx_fallback_document / capex_commitments

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: capex, commitments

```text
commitments remain unchanged and we remain on track to meet our FY2030 operational decarbonisation target. We continue to partner with First Nations and Indigenous peoples around the world. Over 90 per cent of BHP’s operations are located on or near the traditional lands of Indigenous peoples – and we seek to build long-term relationships based on trust and mutual benefit. The significant uplift in our spend with Indigenous businesses during the year is a clear demonstration of this. We’re focused on building multi-year partnerships that enable Indigenous businesses to secure investment, grow with confidence and build their capability to provide goods and services to large companies like BHP. A culture and system for high performance Everything we achieve starts with our 90,000 strong workforce. This year we reached our global employee gender balance ambition of 40 per cent female representation early, and improved year-on-year performance against our Indigenous employee participation targets in Australia, Canada and Chile. Our efforts to build a better BHP, with a more inclusive, collaborative and respectful culture, have underpinned this achievement, and contributed to a safer, more productive and more reliable BHP. We have built a track record of operational excellence over recent years, underpinned by the BHP Operating System. In FY2025, we achieved copper production of over 2 million tonnes for the first time – and have lifted copper production by 28 per cent since FY2022. In steelmaking coal, improved operational productivity helped us increase production at BMA, excluding Blackwater and Daunia which were divested in April 2024. At Western Australia Iron Ore, we achieved record production while maintaining our position as the world’s lowest cost major iron ore producer, now for the sixth year in a row. Project delivery We are embedding the BHP Operating System in the way we plan and execute our capital projects as well. We recognise that reliable, capital efficient development of assets and infrastructure is critical to enabling our growth and to maximising shareholder returns. On Jansen Stage 1, a combination of inflation and cost escalation, design development and scope changes, and lower productivity on certain aspects of the project have resulted in a revision of our costs for construction. This is disappointing. It is not representative of the performance we have seen on BHP projects more broadly, nor what we aspire to. We’re taking steps to improve performance on Jansen Stage 1 and we’ll be applying what we learn to strengthen project delivery across the board at BHP. Winning strategy, clear path for growth Our simple, clear strategy drives strong results and long-term value growth. We’ve reshaped our portfolio in anticipation of the megatrends playing out around us, including our position in copper. A much greater proportion of our EBITDA – 45 per cent in FY2025 – now comes from copper. And we’re pursuing more copper growth from our existing assets and through strategic partnerships, including our newly formed Vicuña joint venture which holds copper deposits on the Argentina-Chile border. Through the disciplined application of our Capital Allocation Framework, we seek to sustain our assets, maintain a strong balance sheet and balance attractive shareholder returns and investment in our growth. The quality of our assets and our pipeline of compelling growth prospects gives us added optionality. This allows us to deliberately and strategically choose how we grow value for shareholders. To support our growth, we’re putting our strong balance sheet to work. We’ve optimised our net debt target range to US$10 billion to US$20 billion. This reflects the significant improvement in our operational performance and portfolio since it was last set. A clear future We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System. This allows us to deliver industry-leading margins, high returns and funds for our growth – a unique combination that underpins our strength, consistency and resilience through the cycle. I am confident that BHP is positioned to deliver attractive value and growth for you in the years ahead. Thank you for your continued support. Mike Henry Chief Executive Officer We have world-leading assets and we operate them well – underpinned by the sustained focus and capability building that comes through the BHP Operating System.” 5 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=8 1 Why BHP 13 August 2025 marked 140 years since seven ordinary people gathered on a small plot of ground at Broken Hill in outback New South Wales, Australia. They had no idea the silver, lead and zinc mine they had established would become one of the world’s biggest companies and a global leader in the resources industry, BHP. Since then, BHP has produced many of the vital resources the world needs to grow and develop. Materials integral to what we use and do every day. Over the last 140 years our business has remained steadfastly resilient through mining cycles regardless of what has been happening in the world around us. We have done this by continually evolving our portfolio, by our ongoing drive to be the world’s best mining operator and by applying financial discipline to the decisions we make. We have built our business by investing, expanding and reshaping it to meet the changing demands of the world. Providing rewarding jobs and careers for hundreds of thousands of people. Making valuable contributions to the countries, regions and communities where we operate. Rewarding our shareholders with dividends and strong returns. Today, BHP is the world’s largest mining company by market capitalisation.1 We have world-leading operations across the globe producing materials vital for a better world. And we are positioned and ready
```

### Section: asx_fallback_document / material_risks

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: risks

```text
risk 25 8 Safety 27 9 Sustainability 29 9.1 Our sustainability approach 29 9.2 Sustainability governance 30 9.3 Material sustainability topics (including human rights) 30 9.4 2030 goals and social value scorecard 31 9.5 People 33 9.6 Health 35 9.7 Ethics and business conduct 37 9.8 Climate change 39 9.9 Nature and environmental performance 53 9.10 Tailings storage facilities 57 9.11 Community 57 9.12 Indigenous peoples 59 9.13 Value chain sustainability 61 9.14 Independent Assurance Report to the Management and Directors of BHP Group Limited 62 10 Samarco 64 11 Risk factors 66 12 Performance by commodity 72 12.1 Copper 72 12.2 Iron ore 73 12.3 Coal 73 12.4 Other assets 74 12.5 Impact of changes to commodity prices 74 13 Non-IFRS financial information 75 13.1 Definition and calculation of non-IFRS financial information 84 13.2 Definition and calculation of principal factors 85 14 Other information 86 14.1 Company details 86 14.2 Forward-looking statements 86 Corporate Governance Statement 1 Corporate governance at BHP 87 2 FY2025 corporate governance highlights 87 3 BHP’s governance structure 88 4 Board composition and succession 89 5 Board Committees 94 6 Management 96 7 Shareholders and reporting 97 8 Culture and conduct 98 9 Risk management and assurance 99 10 US requirements 100 Directors’ Report 1 Review of operations, principal activities and state of affairs 101 2 Directors 101 3 Share interests 102 4 Share capital and buy-back programs 102 5 Group Company Secretary 102 6 Indemnities and insurance 102 7 Dividends 103 8 Auditors 103 9 Non-audit services 103 10 Exploration, research and development 103 11 ASIC Instrument 2016/191 103 12 Proceedings on behalf of BHP Group Limited 103 13 Performance in relation to environmental regulation 103 14 Additional information 103 Remuneration Report Letter from the People and Remuneration Committee Chair 104 Remuneration at a glance 105 Our Key Management Personnel 106 Remuneration Governance 106 Paying competitively 107 Key terms of our variable remuneration framework and equity plans 108 Remuneration mix 109 Remuneration for Executive KMP 110 Remuneration for Non-executive Directors 113 Statutory remuneration and other disclosures 114 Additional Information 1 Information on mining operations 188 2 Financial information summary 198 3 Financial information by commodity 199 4 Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and voluntary investment in social projects across the communities where we operate during the year. This was 87% of our total economic contribution. __PDF_PAGE__
```

### Section: asx_fallback_document / one_off_items

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: one-off items

```text
impairment in relation to WAN assets, partially offset by US$0.7 billion (after tax) gain on divestment of the Blackwater and Daunia mines. For more information on Exceptional items refer to Financial Statements note 3 ‘Exceptional items’ 15 Overview Additional InformationFinancial StatementsGovernanceContents Operating and Financial Review __PDF_PAGE__ page=18 5 Financial review continued Revenue of US$51.3 billion decreased by US$4.4 billion, or 8 per cent from FY2024. This decrease was mainly due to lower average realised prices for iron ore and coal combined with the transition of WAN into temporary suspension in December 2024 and the divestment of Blackwater and Daunia in April 2024. The decrease was partially offset by higher average realised prices for copper combined with higher copper sales volumes. Higher sales volumes were driven by record copper production primarily due to Escondida higher concentrator feed grade and throughput due to operational improvements, mine sequencing and productive movement and record production at Spence from improved operating performance. Although WAIO also achieved a production record, sales volumes were lower due to increased weather impacts from Tropical Cyclone Zelia and Tropical Storm Sean. For information on our average realised prices and production of our commodities refer to OFR 12 Other income of US$0.4 billion decreased by US$0.9 billion, or 71 per cent from FY2024 largely reflecting the exceptional US$0.9 billion (before tax) gain on divestment of Blackwater and Daunia recognised in FY2024. Total expenses excluding net finance costs of US$32.3 billion decreased by US$4.4 billion, or 12 per cent from FY2024. This primarily reflected the prior period impact of the US$3.8 billion (before tax) impairment of WAN assets combined with lower government royalties of US$1.0 billion in the current year due to lower realised iron ore and coal prices. Raw materials and consumables costs decreased by US$0.6 billion, mainly due to the transition of WAN into temporary suspension in December 2024 and the divestment of Blackwater and Daunia in April 2024. These were partially offset by net inventory movements of US$0.7 billion across the Group and higher wages and salaries of US$0.4 billion primarily due to inflation. Profit from equity accounted investments, related impairments and expenses of US$0.2 billion increased by US$2.8 billion from a loss of US$2.7 billion in FY2024 predominantly due to Samarco dam failure impacts in the prior period. For more information on the total impact of the Samarco dam failure provision and impairment charges connected with equity accounted investments refer to Financial Statements note 3 ‘Exceptional items’ and Financial Statements note 13 ‘Impairment of non-current assets’ respectively Net finance costs of US$1.1 billion decreased by US$0.4 billion, or 25 per cent, from FY2024 primarily reflecting the impact of lower interest rates on the unwind of discounting on provisions combined with higher capitalised interest, mainly in relation to Potash projects. For more information on net finance costs refer to Financial Statements note 23 ‘Net finance costs’ Total taxation expense of US$7.2 billion increased by US$0.8 billion, or 12 per cent from FY2024 primarily due to the non-recurrence of a tax benefit of US$1.1 billion in relation to the impairment of WAN assets recognised in the prior period, the impact of a full year of higher Chilean mining taxes (effective 1 January 2024) and also higher tax in line with higher Chilean profits. For more information on income tax expense refer to Financial Statements note 6 ‘Income tax expense’ Principal factors that affect Underlying EBITDA The following table and commentary describe the impact of the principal factors1 that affected Underlying EBITDA for FY2025 compared with FY2024. US$M Year ended 30 June 2024 29,016 Net price impact: Change in sales prices (4,580) Lower average realised prices for iron ore and coal, partially offset by higher average realised prices for copper. Price-linked costs 875 Lower iron ore and coal royalties in line with lower prices. (3,705) Change in volumes 2,215 Record copper production primarily due to Escondida higher concentrator feed grade and throughput due to operational improvements, mine sequencing and productive movement and record production at Spence from improved operating performance, partially offset by Copper SA slightly lower production volumes due to a weather-related power outage in Q2 FY2025. Copper SA sales volumes were slightly higher due to inventory drawdown. Record WAIO production despite sales volumes being lower due to increased weather impacts from Tropical Cyclone Zelia and Tropical Storm Sean, and planned Rail Technology Programme tie-ins. BMA strong performance, supported by improved truck productivity and inventory drawdown, helped mitigate wet weather and geotechnical challenges. Change in controllable cash costs: Operating cash costs (893) Higher costs at Escondida driven by one-off labour-related costs combined with higher operational and maintenance contractor costs to support higher material movement. Spence and Copper SA were higher due to finished goods inventory drawdowns. WAIO higher costs reflected additional planned shutdowns and to support higher material movement, partly offset by favourable inventory movements. BMA and NSWEC were higher due to inventory drawdowns to mitigate the impacts of wet weather, geotechnical conditions, and reduced truck availability, respectively. Exploration and business development (60) (953) Change in other costs: Exchange rates 354 Impact of movements in the Australian dollar and Chilean peso against the US dollar. Inflation on costs (538) Impact of inflation on the Group’s cost base. Fuel, energy, and consumable price movements 148 Predominantly lower diesel prices, partially offset by higher electricity and explosives prices. Non-cash 392 Higher stripping capitalisation
```

### Section: asx_fallback_document / financial_statement_tables

- Section name: financial_statement_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: financial statement table, income statement, balance sheet, cash flow statement

```text
assets 19 6.1 Copper 19 6.2 Iron ore 21 6.3 Coal 22 6.4 Potash 23 6.5 Nickel 24 6.6 Commercial 24 7 How we manage risk 25 8 Safety 27 9 Sustainability 29 9.1 Our sustainability approach 29 9.2 Sustainability governance 30 9.3 Material sustainability topics (including human rights) 30 9.4 2030 goals and social value scorecard 31 9.5 People 33 9.6 Health 35 9.7 Ethics and business conduct 37 9.8 Climate change 39 9.9 Nature and environmental performance 53 9.10 Tailings storage facilities 57 9.11 Community 57 9.12 Indigenous peoples 59 9.13 Value chain sustainability 61 9.14 Independent Assurance Report to the Management and Directors of BHP Group Limited 62 10 Samarco 64 11 Risk factors 66 12 Performance by commodity 72 12.1 Copper 72 12.2 Iron ore 73 12.3 Coal 73 12.4 Other assets 74 12.5 Impact of changes to commodity prices 74 13 Non-IFRS financial information 75 13.1 Definition and calculation of non-IFRS financial information 84 13.2 Definition and calculation of principal factors 85 14 Other information 86 14.1 Company details 86 14.2 Forward-looking statements 86 Corporate Governance Statement 1 Corporate governance at BHP 87 2 FY2025 corporate governance highlights 87 3 BHP’s governance structure 88 4 Board composition and succession 89 5 Board Committees 94 6 Management 96 7 Shareholders and reporting 97 8 Culture and conduct 98 9 Risk management and assurance 99 10 US requirements 100 Directors’ Report 1 Review of operations, principal activities and state of affairs 101 2 Directors 101 3 Share interests 102 4 Share capital and buy-back programs 102 5 Group Company Secretary 102 6 Indemnities and insurance 102 7 Dividends 103 8 Auditors 103 9 Non-audit services 103 10 Exploration, research and development 103 11 ASIC Instrument 2016/191 103 12 Proceedings on behalf of BHP Group Limited 103 13 Performance in relation to environmental regulation 103 14 Additional information 103 Remuneration Report Letter from the People and Remuneration Committee Chair 104 Remuneration at a glance 105 Our Key Management Personnel 106 Remuneration Governance 106 Paying competitively 107 Key terms of our variable remuneration framework and equity plans 108 Remuneration mix 109 Remuneration for Executive KMP 110 Remuneration for Non-executive Directors 113 Statutory remuneration and other disclosures 114 Additional Information 1 Information on mining operations 188 2 Financial information summary 198 3 Financial information by commodity 199 4 Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and voluntary investment in social projects across
```

### Section: asx_fallback_document / segment_product_tables

- Section name: segment_product_tables
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: segment table, product table, sector metrics

```text
Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions (Scopes 1 and 2 from our operated assets)4 5% on FY2024 and we remain on track to achieve our medium-term target by FY2030 Indigenous partnerships7 US$853m up 40% on FY2024 Record Indigenous procurement spend Achieving gender balance5 41.3% Female employee representation at 30 June 2025 We achieved our aspirational goal of gender balance by CY2025, having started this journey at 17.6% female employee representation in CY2016 Total economic contribution6 US$46.8bn We contributed US$40.5bn to suppliers, contractors, employees, governments and voluntary investment in social projects across the communities where we operate during the year. This was 87% of our total economic contribution. __PDF_PAGE__ page=6 Chair’s review Dear Shareholders, I am pleased to provide BHP’s Annual Report for FY2025. It is an honour and a privilege to be your new Chair. Your Board and I are excited about the future of this great company. I want to acknowledge the contribution of my predecessor, Ken MacKenzie, who led the Board as Chair for seven years. I thank Ken for his outstanding service to the Board and BHP during his tenure. Ken leaves a lasting legacy at BHP. In times of global uncertainty, stability and resilience matter. BHP has stood for both for 140 years. What we do matters. The world needs more of the materials we produce to develop, decarbonise and digitalise. BHP has a substantial role to play in producing the vital materials the world needs and in contributing to the success of the global economy. We remain well positioned to meet global demand for the commodities we produce in order to create long-term value for our shareholders, local communities, customers, suppliers and partners. Rewarding shareholders BHP has a simple, clear strategy that is resilient amid any operating environment. Executing this strategy has allowed us to perform well through mining and economic cycles. The company performed strongly in FY2025, generating significant cash flow. Healthy cash returns are important for shareholders, including the hundreds of thousands of retail shareholders who rely on BHP to support their income and retirement. Over the past five years, BHP has delivered more than US$50 billion in cash dividends to our shareholders. Our Capital Allocation Framework (CAF) promotes discipline in all our capital decisions and prioritises capital for safety and maintenance, balance sheet strength and a minimum dividend payout ratio of 50 per cent of underlying attributable profit at every reporting period. For FY2025, your Board determined dividends totalling 110 US cents a share. This represents a total distribution to shareholders of US$5.6 billion, or 55 per cent of the underlying attributable profit for FY2025. Building for the future Our performance allows us to plan for and invest in value adding growth projects. BHP has a strong growth pipeline of organic and greenfield projects in copper, iron ore and potash. Our growth strategy generates greater exposure to commodities that the world needs to reduce greenhouse gas emissions and
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_production
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: production

```text
2.1 Our portfolio Record group copper production 2.02 Mt 8% on FY2024 Copper We are one of the world’s largest copper
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_realised_price
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: realised price

```text
Includes the fair value of contingent payments based on 35% revenue share to BMA, subject to average realised prices achieved by the Assets exceeding thresholds of US$159/tonne in the 12 month period 12 months post completion, US$134/tonne
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_unit_cost_aisc
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: unit cost, AISC

```text
Production for FY2026 is expected to increase to between 18 and 20 Mt (36 and 40 Mt on a 100 per cent basis), weighted to the second half, while unit costs are expected to decrease with guidance between US$116/t and US$128/t as we push to
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_capex
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: capex

```text
Major global producer by the end of the decade US$7.0–US$7.4bn Estimated capital expenditure for Jansen Stage 1 Potash
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_reserves_resources
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: reserves, resources

```text
2025 US$M Cash flow hedging reserve Cost of hedging reserve Gross Tax Net Gross Tax Net Total At the beginning of the financial year 40 (13) 27 (10) 3 (7) 20 Add: Change in fair value of hedging instrument recognised in OCI 330 (99) 231 16
```

### Section: asx_fallback_document / sector_metric

- Section name: sector_metric_commodity_exposure
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf
- Supports claims: commodity exposure

```text
Refer to note 2 ‘Revenue’, which presents current and prior year revenue by
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://www.bhp.com/-/media/documents/investors/annual-reports/2025/250819_bhpannualreport2025.pdf

```text
__PDF_PAGE__ page=1 Bringing people and resources together to build a better world Annual Report 2025 __PDF_PAGE__ page=2 Cover photo Escondida, Chile Contents Overview Our performance highlights 2 Chair’s review 4 Chief Executive Officer’s review 5 Operating and Financial Review 1 Why BHP 6 2 Our business 8 2.1 Our portfolio 8 2.2 Where we operate 10 3 Our key differentiators 11 4 Positioning for growth 12 5 Financial review 13 Chief Financial Officer’s review 13 5.1 Group overview 14 5.2 Key performance indicators 14 5.3 Financial results 15 5.4 Debt and sources of liquidity 17 6 Our assets 19 6.1 Copper 19 6.2 Iron ore 21 6.3 Coal 22 6.4 Potash 23 6.5 Nickel 24 6.6 Commercial 24 7 How we manage risk 25 8 Safety 27 9 Sustainability 29 9.1 Our sustainability approach 29 9.2 Sustainability governance 30 9.3 Material sustainability topics (including human rights) 30 9.4 2030 goals and social value scorecard 31 9.5 People 33 9.6 Health 35 9.7 Ethics and business conduct 37 9.8 Climate change 39 9.9 Nature and environmental performance 53 9.10 Tailings storage facilities 57 9.11 Community 57 9.12 Indigenous peoples 59 9.13 Value chain sustainability 61 9.14 Independent Assurance Report to the Management and Directors of BHP Group Limited 62 10 Samarco 64 11 Risk factors 66 12 Performance by commodity 72 12.1 Copper 72 12.2 Iron ore 73 12.3 Coal 73 12.4 Other assets 74 12.5 Impact of changes to commodity prices 74 13 Non-IFRS financial information 75 13.1 Definition and calculation of non-IFRS financial information 84 13.2 Definition and calculation of principal factors 85 14 Other information 86 14.1 Company details 86 14.2 Forward-looking statements 86 Corporate Governance Statement 1 Corporate governance at BHP 87 2 FY2025 corporate governance highlights 87 3 BHP’s governance structure 88 4 Board composition and succession 89 5 Board Committees 94 6 Management 96 7 Shareholders and reporting 97 8 Culture and conduct 98 9 Risk management and assurance 99 10 US requirements 100 Directors’ Report 1 Review of operations, principal activities and state of affairs 101 2 Directors 101 3 Share interests 102 4 Share capital and buy-back programs 102 5 Group Company Secretary 102 6 Indemnities and insurance 102 7 Dividends 103 8 Auditors 103 9 Non-audit services 103 10 Exploration, research and development 103 11 ASIC Instrument 2016/191 103 12 Proceedings on behalf of BHP Group Limited 103 13 Performance in relation to environmental regulation 103 14 Additional information 103 Remuneration Report Letter from the People and Remuneration Committee Chair 104 Remuneration at a glance 105 Our Key Management Personnel 106 Remuneration Governance 106 Paying competitively 107 Key terms of our variable remuneration framework and equity plans 108 Remuneration mix 109 Remuneration for Executive KMP 110 Remuneration for Non-executive Directors 113 Statutory remuneration and other disclosures 114 Additional Information 1 Information on mining operations 188 2 Financial information summary 198 3 Financial information by commodity 199 4 Production 201 5 Major projects 203 6 Mineral Resources and Ore Reserves 204 7 People – performance data 217 8 Legal proceedings 218 9 Shareholder information 221 10 Glossary 227 Financial Statements 1 Consolidated Financial Statements 118 2 Consolidated entity disclosure statement 177 3 Directors’ declaration 181 4 Lead auditor’s independence declaration under Section 307C of the Australian Corporations Act 2001 182 5 Independent auditor’s report to the members of BHP Group Limited 183 BHP Annual Report 2025 BHP Group Limited ABN 49 004 028 077 Annual Report 2025 Economic Contribution Report 2025 Modern Slavery Statement 2025 ESG Standards and Databook 2025 2025 Annual Reporting Suite __PDF_PAGE__ page=3 In FY2025, we made good progress on strengthening our pipeline of attractive growth options in copper and potash, and delivered another strong year of operational and financial performance.” Mike Henry Chief Executive Officer Copper PotashCoalIron ore 1Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview __PDF_PAGE__ page=4 Our performance highlights Resilience and growth Record copper production Highest production in 17 years at Escondida, a record at Spence and record quarterly production in Q4 at Copper South Australia. Record iron ore production Third-consecutive year of record production at WAIO, as we again demonstrated supply chain excellence from pit to port. Steelmaking coal production lift¹ Queensland steelmaking coal volumes rose 5% with improved truck productivity offsetting heavy wet weather and geotechnical challenges. First potash estimated mid-CY2027 Jansen Stage 1 is 68% complete. Jansen is a world-class asset and is expected to have operating costs at the low end of the cost curve when fully ramped up. 2 BHP Annual Report 2025 Dividend per share 110USc FY2024: 146 USc Profit from operations US$19.5bn FY2024: US$17.5 bn Underlying earnings per share² 200.2USc FY2024: 269.5 USc Total payments to governments US$10.4bn FY2024: US$11.2 bn __PDF_PAGE__ page=5 3 Operating and Financial Review Additional InformationFinancial StatementsGovernanceContents Overview 1. Excluding the contribution of the Blackwater and Daunia mines, divested by BMA on 2 April 2024. 2. For more information on Non-IFRS Financial Information refer to OFR 13. 3. Combined employee and contractor frequency per 1 m illion hours worked. Excludes OZ Minerals Brazil assets. 4. For more information on the calculation of this metric and on our GHG emissions targets and goals refer to OFR 9.8. 5. For more information on this metric and how we define gender balance refer to OFR 9.5. 6. For more information on our total economic contribution, refer to the BHP Economic Contribution Report 2025 . 7. For more information on this metric refer to OFR 9.12. High potential injury frequency³ Fatalities 18% From FY2024 0 FY2024:1 Operational greenhouse gas emissions
```

```
