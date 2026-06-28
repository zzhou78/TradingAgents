# Codex Role Evidence Packet: AAPL

- Trade date: `2026-06-27`
- Instrument identity: `Apple Inc.`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for AAPL from 2026-05-28 to 2026-06-27
# Total records: 21
# Data retrieved on: 2026-06-28 21:00:31

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-05-28,310.68,312.8,309.57,312.51,48220400,0.0,0.0
2026-05-29,311.78,315.0,309.53,312.06,70026800,0.0,0.0
2026-06-01,309.63,310.94,305.02,306.31,48849900,0.0,0.0
2026-06-02,307.46,315.45,306.69,315.2,44534700,0.0,0.0
2026-06-03,314.18,316.94,308.85,310.26,50836700,0.0,0.0
2026-06-04,313.23,313.54,309.65,311.23,44869100,0.0,0.0
2026-06-05,312.86,315.17,307.15,307.34,65310500,0.0,0.0
2026-06-08,308.74,317.4,301.17,301.54,77949100,0.0,0.0
2026-06-09,300.28,300.75,287.78,290.55,70108800,0.0,0.0
2026-06-10,290.74,294.75,287.38,291.58,52793300,0.0,0.0
2026-06-11,293.72,297.0,289.59,295.63,42572500,0.0,0.0
2026-06-12,296.03,297.14,289.62,291.13,38742100,0.0,0.0
2026-06-15,294.12,297.78,291.7,296.42,45732600,0.0,0.0
2026-06-16,295.25,300.48,293.97,299.24,39874400,0.0,0.0
2026-06-17,300.85,302.07,294.36,295.95,42745100,0.0,0.0
2026-06-18,298.11,300.57,295.62,298.01,85962200,0.0,0.0
2026-06-22,297.31,302.42,296.76,297.01,44879900,0.0,0.0
2026-06-23,297.54,301.64,294.18,294.3,52010900,0.0,0.0
2026-06-24,295.36,299.7,292.94,293.08,53081900,0.0,0.0
2026-06-25,287.4,288.8,273.75,275.15,107013700,0.0,0.0
2026-06-26,275.0,285.95,274.21,283.78,261693600,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for AAPL

- Requested analysis date: 2026-06-27
- Latest trading row used: 2026-06-26
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 275.00 |
| High | 285.95 |
| Low | 274.21 |
| Close | 283.78 |
| Volume | 261693600 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 291.02 |
| close_50_sma | 291.41 |
| close_200_sma | 269.08 |
| rsi | 41.26 |
| boll | 298.29 |
| boll_ub | 318.33 |
| boll_lb | 278.25 |
| macd | -2.24 |
| macds | 0.53 |
| macdh | -2.77 |
| atr | 8.16 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-14 | 298.21 |
| 2026-05-15 | 300.23 |
| 2026-05-18 | 297.84 |
| 2026-05-19 | 298.97 |
| 2026-05-20 | 302.25 |
| 2026-05-21 | 304.99 |
| 2026-05-22 | 308.82 |
| 2026-05-26 | 308.33 |
| 2026-05-27 | 310.85 |
| 2026-05-28 | 312.51 |
| 2026-05-29 | 312.06 |
| 2026-06-01 | 306.31 |
| 2026-06-02 | 315.20 |
| 2026-06-03 | 310.26 |
| 2026-06-04 | 311.23 |
| 2026-06-05 | 307.34 |
| 2026-06-08 | 301.54 |
| 2026-06-09 | 290.55 |
| 2026-06-10 | 291.58 |
| 2026-06-11 | 295.63 |
| 2026-06-12 | 291.13 |
| 2026-06-15 | 296.42 |
| 2026-06-16 | 299.24 |
| 2026-06-17 | 295.95 |
| 2026-06-18 | 298.01 |
| 2026-06-22 | 297.01 |
| 2026-06-23 | 294.30 |
| 2026-06-24 | 293.08 |
| 2026-06-25 | 275.15 |
| 2026-06-26 | 283.78 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 291.4116479492188
2026-06-25: 291.0597430419922
2026-06-24: 290.72857788085935
2026-06-23: 290.04620666503905
2026-06-22: 289.36501159667966
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 288.62981567382815
2026-06-17: 287.84284912109376
2026-06-16: 286.98918212890624
2026-06-15: 286.17681640625
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 285.36210479736326
2026-06-11: 284.64739868164065
2026-06-10: 283.8059262084961
2026-06-09: 282.9023861694336
2026-06-08: 282.0628060913086
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 281.0851504516602
2026-06-04: 279.9860998535156
2026-06-03: 278.7896670532227
2026-06-02: 277.6096371459961
2026-06-01: 276.26087158203126
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 275.1092886352539
2026-05-28: 273.86228759765623


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 269.075539855957
2026-06-25: 268.8250843048096
2026-06-24: 268.6353789520264
2026-06-23: 268.36504806518553
2026-06-22: 268.08906578063966
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 267.79300201416015
2026-06-17: 267.44831161499025
2026-06-16: 267.1259870910645
2026-06-15: 266.78930671691893
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 266.4564055633545
2026-06-11: 266.14407096862794
2026-06-10: 265.79851676940916
2026-06-09: 265.4762041473389
2026-06-08: 265.14478179931643
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 264.76394371032717
2026-06-04: 264.37679153442383
2026-06-03: 263.97183464050295
2026-06-02: 263.5752178955078
2026-06-01: 263.15983436584474
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 262.7916431427002
2026-05-28: 262.3763538360596


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 41.264905239850854
2026-06-25: 32.21626505426505
2026-06-24: 45.840823823311474
2026-06-23: 47.09933626555723
2026-06-22: 49.92659056179099
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 50.97504659129809
2026-06-17: 48.92330273622317
2026-06-16: 52.160660070512996
2026-06-15: 49.50100406408827
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 44.08616262826677
2026-06-11: 48.16571454883226
2026-06-10: 43.821187441395324
2026-06-09: 42.6867635382876
2026-06-08: 53.36306101714175
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 60.81720503018205
2026-06-04: 66.61215956347895
2026-06-03: 65.85891278463127
2026-06-02: 73.72449671760747
2026-06-01: 67.17304316302064
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 79.00388845028067
2026-05-28: 80.02820835501764


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: -2.236859871247077
2026-06-25: -1.5674827205456836
2026-06-24: 0.18837708853476443
2026-06-23: 0.6011534147573911
2026-06-22: 0.9950437517225623
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 1.207388180935311
2026-06-17: 1.359036697044246
2026-06-16: 1.742572747977647
2026-06-15: 1.8717781229597676
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 2.296590212824583
2026-06-11: 3.344019019912082
2026-06-10: 4.174096966123159
2026-06-09: 5.585229635035603
2026-06-08: 7.409980958920812
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 8.512261721805714
2026-06-04: 9.204813877013919
2026-06-03: 9.55879984360945
2026-06-02: 9.97034133117404
2026-06-01: 9.847612707359929
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 10.45289347960744
2026-05-28: 10.4879552146636


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 8.157540458080954
2026-06-25: 7.881965050860018
2026-06-24: 7.001348010751894
2026-06-23: 7.01991249114627
2026-06-22: 6.986057915645503
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 7.088062088994436
2026-06-17: 7.252527464530066
2026-06-16: 7.21733557928959
2026-06-15: 7.271745257263789
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 7.319572285016052
2026-06-11: 7.304153266074978
2026-06-10: 7.296010927918487
2026-06-09: 7.290319836436255
2026-06-08: 6.792651380344813
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 6.066702988929029
2026-06-04: 5.9164478702889545
2026-06-03: 6.072327348892912
2026-06-02: 5.917122042046935
2026-06-01: 5.669207226170733
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 5.563760970882187
2026-05-28: 5.5709732593575


ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.
```

## Role: social

- Skill: `tradingagents-sentiment-analyst`

### Tool: fetch_stocktwits_messages

- Status: `ok`

```text
Bullish: 6 (20%) · Bearish: 5 (17%) · Unlabeled: 19 · Total: 30 most-recent messages

[2026-06-28T09:52:04Z · @chamono1942 · no-label] $AAPL Apple Uses Chinese Semiconductors!
[2026-06-28T09:27:58Z · @CindyConwaysa · Bullish] $IBRX $AAPL       @CindyConwaysa
[2026-06-28T09:23:48Z · @BradBreath · Bullish] $AAPL 💪🏼EVERY BIT OF IT🍏
[2026-06-28T09:22:07Z · @rst1016 · no-label] $AAPL 290 monday???
[2026-06-28T09:21:48Z · @CindyConwaysa · no-label] $AAPL Smart trading is built on planning and patience—never stop learning and act on the best opportunities.
[2026-06-28T09:07:03Z · @Rvazstocksfl · no-label] $AAPL 250 on Monday ?
[2026-06-28T08:52:38Z · @Agayay · Bullish] $MU $DRAM $AAPL $QQQ $SPY   Actually i think we see MEMORY stock rally on Monday.  Due to Apple seeking to buy MEMORY from China. But we all know that it won&#39;t be approved. News proves that MEMORY SHORTAGE IS CRITICAL. Remember, market is always opposite. You panic but market…
[2026-06-28T08:50:15Z · @MicroCapsTrader · no-label] $AAPL Index rebalancing caused the high volumes and random price actions on some of the large caps last Friday. Unless it reclaims $287-289 previous breakout zone, be careful as a meltdown after a bear flag confirmation doesn’t last only a day. So look for reclaims of previous ke…
[2026-06-28T07:57:44Z · @lotharchoo · no-label] June 29 - July 2, 2026  $AAPL: 283.78 Sell   $TSLA: 379.71 Sell  $INTC : 128..32 Buy   $NVDA: 192.53 Sell   $META: 550.25 Sell
[2026-06-28T06:48:56Z · @Himbhas18 · Bearish] $AAPL no one wants to buy expensive POS
[2026-06-28T06:09:33Z · @termalerts · no-label] IPHONE 18 PRICE FORECAST TO SURPASS $1,100 AFTER APPLE&#39;S MACBOOK, IPAD PRICE HIKES $AAPL
[2026-06-28T06:04:38Z · @juanagustin2086 · Bullish] $AAPL
[2026-06-28T06:04:27Z · @QuantMindAI · no-label] Testing $AAPL
[2026-06-28T05:44:44Z · @HEEJIN_J · no-label] $AAPL Apple gets clapped by a nerd they used to bully, now they&#39;re reporting them for school violence lol
[2026-06-28T04:21:46Z · @TheStockShrewd · Bullish] $MU who else is convinced $AAPL news and post-earnings dip is a scheme for institutions to enter 😂😂
[2026-06-28T04:21:06Z · @ns9970 · no-label] $MU $AAPL is this another good vs evil? Who is the aggressor? lol who has the right to defend itself?
[2026-06-28T04:18:57Z · @EconomyEngine · no-label] $QQQ $SPY $TSLA $MSFT $AAPL  🇮🇷🇺🇸 IRGC warns US military bases in the Middle East &quot;will experience hell in the coming days.
[2026-06-28T01:29:08Z · @Kaythu · Bearish] $AAPL The War in Iran continues to escalate big time! There is no such thing as a ceasefire and no such thing as a deal. The fighting continues on both ends. Oil prices are likely to go up yet again! Whats the likelihood the stock market winds up red on Monday and the entire week…
[2026-06-28T00:23:01Z · @PivotPoint_101 · no-label] $SPY  we are no longer accepting Failed YouTubers or http://X.com Gurus  $QQQ $IWM $AAPL
[2026-06-28T00:06:36Z · @Jumper567 · Bearish] $AAPL $MU and then there is $MSFT $GOOG who are silently sulking
[2026-06-28T00:05:45Z · @Jumper567 · Bearish] $AAPL this trash complaining about another trash $MU so it’s ok if they did it but not when others do it to them 🤣🤣🤣🤣🤣
[2026-06-28T00:01:03Z · @ebcnetworks · no-label] $MU this is correct  For decade $AAPL has been buying our chips for $5, gluing it inside a metal box, &amp; selling it to consumers for $99 upgrades &amp; laughing at our attempts to get $7. Now we&#39;re charging them $50 &amp; they turned around &amp; raised prices on their cus…
[2026-06-28T00:00:19Z · @NBman1988 · Bullish] $AMZN $AAPL $BTC.X come to $VELVET.X for 100% returns
[2026-06-27T23:52:17Z · @ResearchTrends09 · no-label] $AAPL
[2026-06-27T23:52:03Z · @ResearchTrends09 · no-label] $AAPL liberal women. Hairy arm pits.
[2026-06-27T23:35:47Z · @Supraman1 · no-label] $MU  $MU $NVDA $SNDK $AAPL $MSFT
[2026-06-27T23:09:17Z · @MorganHoratio · no-label] We closed the week with 11 American 🇺🇸 public companies worth more than $1 Trillion    $NVDA $4.7T    $AAPL $4.2T    $GOOGL $4.1T    $MSFT $2.8T     Anchored by its advanced Vera Rubin architecture and defensive CUDA software ecosystem, NVIDIA commands the global leaderboard at a…
[2026-06-27T23:01:46Z · @johnrivers0110 · Bearish] $WEN 🔺after all this Wendys I&#39;ll be looking into a health care company for all the heart attacks and high cholesterol you gonna have after this stock meets you at 5... The FiB 🔺  $SPCX  $SPY  $BTC.X  $AAPL
[2026-06-27T23:00:40Z · @FibonacciTrader_ · no-label] $AAPL is facing a strategic input-cost problem that the market is slowly starting to price in around the AI cycle.    If memory becomes the key bottleneck in AI infrastructure, Apple won’t stay exposed to rising component costs indefinitely. Near-term, they may bridge supply via …
[2026-06-27T22:32:48Z · @MarketPulsee · no-label] Dumping $AAPL at $282 over the &quot;100-year memory crisis&quot; is brainless. Cook just passes costs to consumers via MacBook price hikes. Gross margins stay untouchable. Keep shorting
```

### Tool: fetch_reddit_posts

- Status: `ok`

```text
r/wallstreetbets — 4 recent posts mentioning AAPL (via RSS feed; scores/comments unavailable):
  [2026-06-28] Webull glitch
    body excerpt: My all stocks has doubled the value
  [2026-06-27] MU $2000 is no longer a meme
    body excerpt: MU just dropped numbers that broke the old memory playbook. Q3 did $41.46B in revenue, up from $9.3B a year ago, EPS $25.11 when the street was looking for like $20. The part that actually got me was the margin, 85%, nobody had that modeled…
  [2026-06-25] That was fun
    body excerpt: submitted by /u/MountainAlive [link] [comments]
  [2026-06-24] Lucky $AAPL and $GOOGL Pump Timings
    body excerpt: Very rarely do I time my exits correctly. So when it happened TWICE this morning on both the AAPL and GOOGL rallies, it's like lightning striking twice. Thank you, bag 7 ❤️

r/stocks: <no posts found mentioning AAPL in the past 7 days>

r/investing: <no posts found mentioning AAPL in the past 7 days>
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
## AAPL News, from 2026-06-20 to 2026-06-27:

### Crypto's brutal week in review: Bitcoin prices, illicit Iranian transactions, & more (source: Yahoo Finance Video)
Scott Melker reviews the week crypto just had, including bitcoin (BTC-USD) prices plummeting, Bitmine (BMNR) joining the Russell 1000 (^RUI), and more. "The Daily Wolf with Scott Melker" airs every day at 12:00 p.m. Tune in for your daily dose of all things crypto. Make sure to also check out Yahoo Finance's new crypto hub to find the latest crypto-related news.
Link: https://finance.yahoo.com/video/cryptos-brutal-week-review-bitcoin-120000992.html

### Apple (AAPL) Plans Mac Chip Roadmap Shift Toward AI-Focused M7 (source: Insider Monkey)
Apple Inc. (NASDAQ:AAPL) is one of the 15 Best AI Stocks That Will Make You Rich in 10 Years. On June 26, 2026, Bloomberg’s Mark Gurman reported that Apple Inc. (NASDAQ:AAPL) is planning a major change to its Mac chip roadmap, citing people with knowledge of the matter. Apple is expected to launch a base […]
Link: https://finance.yahoo.com/technology/ai/articles/apple-aapl-plans-mac-chip-193217551.html

### The Big Paint vs Rare Earth Faceoff: One Stock to Buy Right Now for 2026 and Beyond (source: Motley Fool)
MP Materials fuels EV and defense supply chains; Sherwin-Williams boasts global scale and strong cash flow. Which business model stands out in today's market?
Link: https://www.fool.com/coverage/better-buy/2026/06/27/the-big-paint-vs-rare-earth-faceoff-one-stock-to-buy-right-now-for-2026-and-beyond/

### KGI Securities Downgrades Apple (AAPL) to Hold – Here’s Why (source: Insider Monkey)
Apple Inc. (NASDAQ:AAPL) is one of the best trending AI stocks to watch in 2026. Apple Inc. (NASDAQ:AAPL) was downgraded by KGI Securities to Hold from Outperform on June 22, with the firm setting a price target of $315. In a separate development, Reuters reported on June 17 that CEO Tim Cook told the Wall […]
Link: https://finance.yahoo.com/markets/stocks/articles/kgi-securities-downgrades-apple-aapl-190812337.html

### Apple Just Did Something It Wouldn’t Even Do During COVID, and Wall Street Is Freaking Out (source: 24/7 Wall St.)
Apple (NASDAQ:AAPL) rarely raises prices. That has been a working assumption on Wall Street for roughly two decades. The company absorbs component costs, squeezes suppliers, redesigns around the problem, and protects its margin envelope without making customers pay more for the same box. So when Apple confirmed Friday that it was raising prices an average of ... Apple Just Did Something It Wouldn’t Even Do During COVID, and Wall Street Is Freaking Out
Link: https://247wallst.com/investing/2026/06/27/apple-just-did-something-it-wouldnt-even-do-during-covid-and-wall-street-is-freaking-out/

### Alphabet Stock Falls Below Berkshire’s Buying Price, but GOOG Is Not a Screaming Buy Yet (source: Barchart)
Alphabet shares have fallen below the price levels at which Berkshire Hathaway bought them in the private placement earlier this month. The stock is not a screaming buy yet, though.
Link: https://www.barchart.com/story/news/3015980/alphabet-stock-falls-below-berkshires-buying-price-but-goog-is-not-a-screaming-buy-yet

### Apple Inc. (AAPL) Allows Alternative App Stores and Payments in Brazil Following a Deal with Regulator (source: Insider Monkey)
Apple Inc. (NASDAQ:AAPL) is one of the 10 Best Brain-Computer Interface Stocks to Buy. On June 18, Reuters reported that Apple Inc. (NASDAQ:AAPL) will permit developers in Brazil to distribute iOS apps through alternative marketplaces and use payment options outside its in-app system under an agreement with antitrust regulator CADE. The company said developers using […]
Link: https://tech.yahoo.com/ai/apple-intelligence/articles/apple-inc-aapl-allows-alternative-153221691.html

### Stock Market Week Ahead: Rotating, For Now, Away From The AI Boom (source: Investor's Business Daily)
Recent action suggests that hyperscalers and other AI boom stocks may be passing the baton to other stock market sectors.
Link: https://www.investors.com/research/investing-action-plan/stock-market-week-ahead-rotating-for-now-away-from-the-ai-boom/?src=A00220&yptr=yahoo

### Apple Wants to Buy Blacklisted Chinese Memory. Micron Has Nothing to Worry About (source: 24/7 Wall St.)
The AI boom has transformed one of the semiconductor industry’s most cyclical businesses into one of its tightest markets. Memory chips, once plagued by oversupply and collapsing prices, have become one of the biggest bottlenecks for AI infrastructure. That shortage has helped lift Micron Technology (NASDAQ:MU), Samsung Electronics, and SK hynix to record profitability as ... Apple Wants to Buy Blacklisted Chinese Memory. Micron Has Nothing to Worry About
Link: https://247wallst.com/investing/2026/06/27/apple-wants-to-buy-blacklisted-chinese-memory-micron-has-nothing-to-worry-about/

### Apple Seeks US Approval to Buy Chips From Blacklisted CXMT: FT (source: Bloomberg)
(Bloomberg) -- Apple Inc. is pressing the White House for approval to purchase memory chips from a blacklisted Chinese company as it grapples to rein in chip costs, the Financial Times reported on Saturday.Most Read from BloombergLutnick Delayed Canada Bridge Debut to Seek Bigger Cut of Toll RevenueIndonesia Opens Door to Dirty Money to Fund Prabowo’s PlansOman Tells Allies Ships Going Through Hormuz May Have to PayApple Shares Sink After Price Hikes Hit iPads and MacsUS Strikes Iran in Response
Link: https://finance.yahoo.com/technology/articles/apple-seeks-us-approval-buy-074523538.html

### Apple seeks approval to buy chips from blacklisted Chinese company, FT reports (source: Reuters)
Apple is lobbying the Trump administration for clearance to buy memory chips from ChangXin ‌Memory Technologies, a Chinese company the Pentagon has ‌put on a blacklist, the Financial Times reported on Friday.  The iPhone maker ​has lobbied the White House for approval aimed at easing financial pressure on the company from rising memory chip prices, the newspaper said, citing unnamed sources.  The White House, Apple and ‌CXMT did not respond ⁠to requests for comment from Reuters outside business hours.
Link: https://finance.yahoo.com/technology/articles/apple-seeks-approval-buy-chips-032619573.html

### S&P 500, Nasdaq End Week Lower As Investors Rotate Out Of Tech, AI Plays — ON, AAPL, SLS, INFQ, NKE in Focus (source: Stocktwits)
The Dow Jones ended its third consecutive week higher amid cooling oil prices and strength in pharma and materials stocks.
Link: https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-end-week-lower-as-investors-rotate-out-of-tech-ai-plays-on-aapl-sls-infq-nke-in-focus/cZ12ck9R7W9

### Update: Equity Markets Fall as Trump Says Iran Violated Ceasefire (source: MT Newswires)
(Updates with market moves at the end of the day.) US equity benchmarks slipped Friday as Presid
Link: https://finance.yahoo.com/markets/stocks/articles/equity-markets-fall-trump-says-204521099.html

### US stocks recover from tech tremors as oil prices fall (source: AFP)
Wall Street's main stock indices overcame an early bout of tech jitters Friday thanks to buy-the-dip traders, finishing mildly lower, while oil prices fell as shipping traffic resumed through the Strait of Hormuz.While US stocks retreated early, they were saved by investors swooping in to "buy the dip."
Link: https://finance.yahoo.com/markets/world-indices/articles/asian-stocks-drop-again-rollercoaster-022857774.html

### US Equity Indexes Mixed, Mag-7 Lags Amid Micron Technology's Blockbuster Quarterly Results This Week (source: MT Newswires)
US equity indexes were mixed as a decline in technology hit tech-heavy gauges, outweighing a lift in
Link: https://finance.yahoo.com/markets/stocks/articles/us-equity-indexes-mixed-mag-203342644.html

### Stocks to Watch Recap: Micron, Wendy’s, Apple, ON Semiconductor (source: The Wall Street Journal)
↘️ ON Semiconductor (ON): The chip maker agreed to acquire Synaptics (SYNA) in a roughly $7 billion all-stock transaction, as it seeks to push into physical AI. Shares of ON Semiconductor tumbled 24%, while Synaptics’ stock slipped 3.
Link: https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-06-26-2026/card/stocks-to-watch-on-semiconductor-apple-zalando-HXVpEfOkkyL0ye8xKqqr?siteid=yhoof2&yptr=yahoo

### Stock Of The Day: Is The Apple Sell-Off Over? (source: Benzinga)
Apple Inc. (NASDAQ:AAPL) is trading higher on Friday. It has dropped about 12% since the beginning of June. But the sell-off may be over. The shares are oversold and at support — and these can be bullish dynamics. This is why Apple is the Stock of the Day. • What’s driving AAPL shares up today? In February and again in April, Apple ran into resistance at the $275 level. People who sold there thought they made a smart decision when the price dropped afterward. But when the resistance broke, and t
Link: https://finance.yahoo.com/markets/stocks/articles/stock-day-apple-sell-off-201228930.html

### Gadget prices have fallen for decades. Then AI happened. (source: CBS News)
The race to build AI data centers is leading to a global shortage of memory chips, driving up the cost of personal electronics.
Link: https://www.cbsnews.com/news/ai-boom-chip-shortage-gadget-prices-apple-microsoft/

### How To Invest: 5 Tips For Dealing With This Stock Market (source: Investor's Business Daily)
The power trend has generated impressive gains. Get ready to deal with whatever comes next with five guidelines for how to invest.
Link: https://www.investors.com/how-to-invest/how-to-invest-nvidia-apple-stock-market-trends/?src=A00220&yptr=yahoo


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-20 and 2026-06-27
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for AAPL
# Data retrieved on: 2026-06-28 21:00:44

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,116,34236.0,,Sale at price 295.14 per share.,BORDERS BEN,Officer,,2026-06-16,D
1,240,,,,BORDERS BEN,Officer,,2026-06-15,D
2,30104,,,,NEWSTEAD JENNIFER,General Counsel,,2026-06-15,D
3,65000,0.0,,Stock Gift at price 0.00 per share.,LEVINSON ARTHUR D,Director,,2026-05-27,D
4,50000,15551000.0,,Sale at price 311.02 per share.,LEVINSON ARTHUR D,Director,,2026-05-27,D
5,1274,369460.0,,Sale at price 290.00 per share.,BORDERS BEN,Officer,,2026-05-08,D
6,5000,0.0,,Stock Gift at price 0.00 per share.,LEVINSON ARTHUR D,Director,,2026-05-06,D
7,250000,71189722.0,,Sale at price 284.57 - 285.04 per share.,LEVINSON ARTHUR D,Director,,2026-05-06,D
8,1534,421850.0,,Sale at price 275.00 per share.,PAREKH KEVAN,Chief Financial Officer,,2026-04-23,D
9,10928,,,,PAREKH KEVAN,Chief Financial Officer,,2026-04-15,D
10,1717,,,,BORDERS BEN,Officer,,2026-04-15,D
11,30002,7660875.0,,Sale at price 255.12 - 255.82 per share.,O'BRIEN DEIRDRE,Officer,,2026-04-02,D
12,64949,16512198.0,,Sale at price 251.25 - 256.00 per share.,COOK TIMOTHY D,Chief Executive Officer,,2026-04-02,D
13,64317,,,,KHAN SABIH,Chief Operating Officer,,2026-04-01,D
14,64317,,,,O'BRIEN DEIRDRE,Officer,,2026-04-01,D
15,131576,,,,COOK TIMOTHY D,Chief Executive Officer,,2026-04-01,D
16,60208,,,,NEWSTEAD JENNIFER,General Counsel,,2026-03-13,D
17,1113,0.0,,Stock Gift at price 0.00 per share.,LEVINSON ARTHUR D,Director,,2026-02-26,D
18,1255,,,,AUSTIN WANDA M,Director,,2026-01-30,D
19,1255,,,,GORSKY ALEX,Director,,2026-01-30,D
20,1255,,,,WAGNER SUSAN L,Director,,2026-01-30,D
21,1255,,,,JUNG ANDREA,Director,,2026-01-30,D
22,1255,,,,LOZANO MONICA C.,Director,,2026-01-30,D
23,1113,,,,LEVINSON ARTHUR D,Director,,2026-01-30,D
24,1255,,,,SUGAR RONALD D,Director,,2026-01-30,D
25,3750,0.0,,Stock Gift at price 0.00 per share.,ADAMS KATHERINE L,General Counsel,,2025-11-12,D
26,3752,1017655.0,,Sale at price 271.23 per share.,KONDO CHRISTOPHER,Officer,,2025-11-07,D
27,4199,1038787.0,,Sale at price 245.89 - 248.73 per share.,PAREKH KEVAN,Chief Financial Officer,,2025-10-16,D
28,7371,,,,KONDO CHRISTOPHER,Officer,,2025-10-15,D
29,16457,,,,PAREKH KEVAN,Chief Financial Officer,,2025-10-15,D
30,43013,11071078.0,,Sale at price 257.36 - 258.08 per share.,O'BRIEN DEIRDRE,Officer,,2025-10-02,D
31,129963,33375723.0,,Sale at price 254.83 - 257.57 per share.,COOK TIMOTHY D,Chief Executive Officer,,2025-10-02,D
32,47125,12101154.0,,Sale at price 254.83 - 257.54 per share.,ADAMS KATHERINE L,General Counsel,,2025-10-02,D
33,92403,,,,KHAN SABIH,Chief Operating Officer,,2025-10-01,D
34,92403,,,,O'BRIEN DEIRDRE,Officer,,2025-10-01,D
35,277206,,,,COOK TIMOTHY D,Chief Executive Officer,,2025-10-01,D
36,92403,,,,ADAMS KATHERINE L,General Counsel,,2025-10-01,D
37,90000,20886300.0,,Sale at price 232.07 per share.,LEVINSON ARTHUR D,Director,,2025-08-28,D
38,435,0.0,,Stock Gift at price 0.00 per share.,KONDO CHRISTOPHER,Officer,,2025-08-25,D
39,34821,7772047.0,,Sale at price 223.20 per share.,O'BRIEN DEIRDRE,Officer,,2025-08-08,D
40,4486,933955.0,,Sale at price 208.19 per share.,KONDO CHRISTOPHER,Officer,,2025-05-12,D
41,4570,941420.0,,Sale at price 206.00 per share.,PAREKH KEVAN,Chief Financial Officer,,2025-04-23,D
42,16458,,,,PAREKH KEVAN,Chief Financial Officer,,2025-04-15,D
43,7373,,,,KONDO CHRISTOPHER,Officer,,2025-04-15,D
44,108136,24184658.0,,Sale at price 221.77 - 224.76 per share.,COOK TIMOTHY D,Chief Executive Officer,,2025-04-02,D
45,38822,8683252.0,,Sale at price 221.68 - 224.62 per share.,ADAMS KATHERINE L,General Counsel,,2025-04-02,D
46,35493,7950691.0,,Sale at price 223.48 - 225.03 per share.,WILLIAMS JEFFREY E,Chief Operating Officer,,2025-04-02,D
47,74535,,,,O'BRIEN DEIRDRE,Officer,,2025-04-01,D
48,218568,,,,COOK TIMOTHY D,Chief Executive Officer,,2025-04-01,D
49,74535,,,,ADAMS KATHERINE L,General Counsel,,2025-04-01,D
50,74535,,,,WILLIAMS JEFFREY E,Chief Operating Officer,,2025-04-01,D
51,1516,343147.0,,Sale at price 226.35 per share.,LEVINSON ARTHUR D,Director,,2025-02-03,D
52,1516,,,,AUSTIN WANDA M,Director,,2025-01-31,D
53,1516,,,,GORSKY ALEX,Director,,2025-01-31,D
54,1516,,,,WAGNER SUSAN L,Director,,2025-01-31,D
55,1516,,,,JUNG ANDREA,Director,,2025-01-31,D
56,1516,,,,LOZANO MONICA C.,Director,,2025-01-31,D
57,1516,,,,LEVINSON ARTHUR D,Director,,2025-01-31,D
58,1516,,,,SUGAR RONALD D,Director,,2025-01-31,D
59,100000,24997395.0,,Sale at price 248.61 - 251.10 per share.,WILLIAMS JEFFREY E,Chief Operating Officer,,2024-12-16,I
60,200000,45464500.0,,Sale at price 224.68 - 229.28 per share.,LEVINSON ARTHUR D,Director,,2024-11-19,D
61,4130,945233.0,,Sale at price 228.87 per share.,KONDO CHRISTOPHER,Officer,,2024-11-18,D
62,8000,0.0,,Stock Gift at price 0.00 per share.,ADAMS KATHERINE L,General Counsel,,2024-11-05,D
63,8115,,,,KONDO CHRISTOPHER,Officer,,2024-10-15,D
64,59305,13433769.0,,Sale at price 226.52 per share.,MAESTRI LUCA,Chief Financial Officer,,2024-10-04,D
65,61019,13843382.0,,Sale at price 226.72 - 227.13 per share.,O'BRIEN DEIRDRE,Officer,,2024-10-02,D
66,223986,50276355.0,,Sale at price 223.75 - 226.57 per share.,COOK TIMOTHY D,Chief Executive Officer,,2024-10-02,D
67,61019,13802297.0,,Sale at price 223.79 - 227.24 per share.,ADAMS KATHERINE L,General Counsel,,2024-10-02,D
68,59730,13550148.0,,Sale at price 226.80 - 227.22 per share.,WILLIAMS JEFFREY E,Chief Operating Officer,,2024-10-02,D
69,127282,,,,MAESTRI LUCA,Chief Financial Officer,,2024-10-01,D
70,127282,,,,O'BRIEN DEIRDRE,Officer,,2024-10-01,D
71,477301,,,,COOK TIMOTHY D,Chief Executive Officer,,2024-10-01,D
72,127282,,,,ADAMS KATHERINE L,General Counsel,,2024-10-01,D
73,127282,,,,WILLIAMS JEFFREY E,Chief Operating Officer,,2024-10-01,D
74,8706,1958850.0,,Sale at price 225.00 per share.,KONDO CHRISTOPHER,Officer,,2024-08-15,D
75,5178,1121037.0,,Sale at price 216.50 per share.,KONDO CHRISTOPHER,Officer,,2024-08-09,D
76,4500,0.0,,Stock Gift at price 0.00 per share.,ADAMS KATHERINE L,General Counsel,,2024-08-07,D
77,100000,20643512.0,,Sale at price 206.42 - 207.05 per share.,ADAMS KATHERINE L,General Counsel,,2024-08-05,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for AAPL
# Data retrieved on: 2026-06-28 21:00:44

Name: Apple Inc.
Sector: Technology
Industry: Consumer Electronics
Market Cap: 4167977926656
PE Ratio (TTM): 34.35593
Forward PE: 29.532974
PEG Ratio: 2.29
Price to Book: 39.088154
EPS (TTM): 8.26
Forward EPS: 9.60892
Dividend Yield: 0.38
Beta: 1.086
52 Week High: 317.4
52 Week Low: 199.26
50 Day Average: 291.4978
200 Day Average: 269.45886
Revenue (TTM): 451442016256
Gross Profit: 216070995968
EBITDA: 159975997440
Net Income: 122575003648
Profit Margin: 0.27152002
Operating Margin: 0.32275
Return on Equity: 1.4147099
Return on Assets: 0.26229
Debt to Equity: 79.548
Current Ratio: 1.07
Book Value: 7.26
Free Cash Flow: 101090746368
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for AAPL (quarterly)
# Data retrieved on: 2026-06-28 21:00:44

,2026-03-31,2025-12-31,2025-09-30,2025-06-30,2025-03-31,2024-12-31,2024-09-30
Ordinary Shares Number,14667688000.0,14697926000.0,14773260000.0,14856722000.0,14939315000.0,,
Share Issued,14667688000.0,14697926000.0,14773260000.0,14856722000.0,14939315000.0,,
Net Debt,39139000000.0,45192000000.0,62723000000.0,65429000000.0,70024000000.0,,
Total Debt,84711000000.0,90509000000.0,98657000000.0,101698000000.0,98186000000.0,,
Tangible Book Value,85157000000.0,88190000000.0,73733000000.0,65830000000.0,66796000000.0,,
Invested Capital,191202000000.0,178699000000.0,172390000000.0,167528000000.0,164982000000.0,,
Working Capital,9473000000.0,-4263000000.0,-17674000000.0,-18629000000.0,-25897000000.0,,
Net Tangible Assets,85157000000.0,88190000000.0,73733000000.0,65830000000.0,66796000000.0,,
Common Stock Equity,106491000000.0,88190000000.0,73733000000.0,65830000000.0,66796000000.0,,
Total Capitalization,180895000000.0,164875000000.0,152061000000.0,148260000000.0,145362000000.0,,
Total Equity Gross Minority Interest,106491000000.0,88190000000.0,73733000000.0,65830000000.0,66796000000.0,,
Stockholders Equity,106491000000.0,88190000000.0,73733000000.0,65830000000.0,66796000000.0,,
Gains Losses Not Affecting Retained Earnings,-5375000000.0,-4854000000.0,-5571000000.0,-6369000000.0,-6363000000.0,,
Other Equity Adjustments,-5375000000.0,-4854000000.0,-5571000000.0,-6369000000.0,-6363000000.0,,
Retained Earnings,12359000000.0,-2177000000.0,-14264000000.0,-17607000000.0,-15552000000.0,,
Capital Stock,99507000000.0,95221000000.0,93568000000.0,89806000000.0,88711000000.0,,
Common Stock,99507000000.0,95221000000.0,93568000000.0,89806000000.0,88711000000.0,,
Total Liabilities Net Minority Interest,264591000000.0,291107000000.0,285508000000.0,265665000000.0,264437000000.0,,
Total Non Current Liabilities Net Minority Interest,129950000000.0,128740000000.0,119877000000.0,124545000000.0,119866000000.0,,
Other Non Current Liabilities,55546000000.0,52055000000.0,41549000000.0,42115000000.0,41300000000.0,,
Tradeand Other Payables Non Current,,,,,,,9254000000.0
Long Term Debt And Capital Lease Obligation,74404000000.0,76685000000.0,78328000000.0,82430000000.0,78566000000.0,,
Long Term Debt,74404000000.0,76685000000.0,78328000000.0,82430000000.0,78566000000.0,,
Current Liabilities,134641000000.0,162367000000.0,165631000000.0,141120000000.0,144571000000.0,,
Other Current Liabilities,57654000000.0,68543000000.0,44452000000.0,62499000000.0,61849000000.0,,
Current Deferred Liabilities,9331000000.0,9413000000.0,9055000000.0,8979000000.0,8976000000.0,,
Current Deferred Revenue,9331000000.0,9413000000.0,9055000000.0,8979000000.0,8976000000.0,,
Current Debt And Capital Lease Obligation,10307000000.0,13824000000.0,20329000000.0,19268000000.0,19620000000.0,,
Current Debt,10307000000.0,13824000000.0,20329000000.0,19268000000.0,19620000000.0,,
Other Current Borrowings,8310000000.0,11827000000.0,12350000000.0,9345000000.0,13638000000.0,,
Commercial Paper,1997000000.0,1997000000.0,7979000000.0,9923000000.0,5982000000.0,,
Payables And Accrued Expenses,57349000000.0,70587000000.0,91795000000.0,50374000000.0,54126000000.0,,
Current Accrued Expenses,,,8919000000.0,,,,
Payables,57349000000.0,70587000000.0,82876000000.0,50374000000.0,54126000000.0,,
Total Tax Payable,,,13016000000.0,,,,26601000000.0
Income Tax Payable,,,13016000000.0,,,,26601000000.0
Accounts Payable,57349000000.0,70587000000.0,69860000000.0,50374000000.0,54126000000.0,,
Total Assets,371082000000.0,379297000000.0,359241000000.0,331495000000.0,331233000000.0,,
Total Non Current Assets,226968000000.0,221193000000.0,211284000000.0,209004000000.0,212559000000.0,,
Other Non Current Assets,77430000000.0,93146000000.0,62950000000.0,82882000000.0,81259000000.0,,
Non Current Deferred Assets,,,20777000000.0,,,,19499000000.0
Non Current Deferred Taxes Assets,,,20777000000.0,,,,19499000000.0
Investments And Advances,78088000000.0,77888000000.0,77723000000.0,77614000000.0,84424000000.0,,
Investmentin Financial Assets,78088000000.0,77888000000.0,77723000000.0,77614000000.0,84424000000.0,,
Available For Sale Securities,78088000000.0,77888000000.0,77723000000.0,77614000000.0,84424000000.0,,
Goodwill And Other Intangible Assets,21334000000.0,,,,,,
Net PPE,50116000000.0,50159000000.0,49834000000.0,48508000000.0,46876000000.0,,
Accumulated Depreciation,-77441000000.0,-77161000000.0,-76014000000.0,-75803000000.0,-74303000000.0,,
Gross PPE,127557000000.0,127320000000.0,125848000000.0,124311000000.0,121179000000.0,,
Leases,,,15091000000.0,,,,14233000000.0
Machinery Furniture Equipment,,,83420000000.0,,,,80205000000.0
Land And Improvements,,,27337000000.0,,,,24690000000.0
Properties,,,0.0,,,,0.0
Current Assets,144114000000.0,158104000000.0,147957000000.0,122491000000.0,118674000000.0,,
Other Current Assets,15349000000.0,15002000000.0,14585000000.0,14359000000.0,14109000000.0,,
Inventory,6747000000.0,5875000000.0,5718000000.0,5925000000.0,6269000000.0,,
Finished Goods,,,,3637000000.0,3596000000.0,4119000000.0,
Raw Materials,,,,2288000000.0,2673000000.0,2792000000.0,
Receivables,53511000000.0,70320000000.0,72957000000.0,46835000000.0,49798000000.0,,
Other Receivables,23172000000.0,30399000000.0,33180000000.0,19278000000.0,23662000000.0,,
Accounts Receivable,30339000000.0,39921000000.0,39777000000.0,27557000000.0,26136000000.0,,
Cash Cash Equivalents And Short Term Investments,68507000000.0,66907000000.0,54697000000.0,55372000000.0,48498000000.0,,
Other Short Term Investments,22935000000.0,21590000000.0,18763000000.0,19103000000.0,20336000000.0,,
Cash And Cash Equivalents,45572000000.0,45317000000.0,35934000000.0,36269000000.0,28162000000.0,,
Cash Equivalents,15832000000.0,14491000000.0,7667000000.0,9583000000.0,3101000000.0,,
Cash Financial,29740000000.0,30826000000.0,28267000000.0,26686000000.0,25061000000.0,,

```

### Tool: get_cashflow

- Status: `ok`

```text
# Cash Flow data for AAPL (quarterly)
# Data retrieved on: 2026-06-28 21:00:45

,2026-03-31,2025-12-31,2025-09-30,2025-06-30,2025-03-31,2024-12-31,2024-09-30
Free Cash Flow,26731000000.0,51552000000.0,26486000000.0,24405000000.0,20881000000.0,,
Repurchase Of Capital Stock,-12288000000.0,-24701000000.0,-20132000000.0,-21075000000.0,-25898000000.0,,
Repayment Of Debt,-5751000000.0,-8074000000.0,-1185000000.0,-1770000000.0,976000000.0,,
Issuance Of Debt,,,0.0,,,,0.0
Capital Expenditure,-1971000000.0,-2373000000.0,-3242000000.0,-3462000000.0,-3071000000.0,,
Income Tax Paid Supplemental Data,16963000000.0,3434000000.0,6037000000.0,5649000000.0,13032000000.0,,
End Cash Position,45572000000.0,45317000000.0,35934000000.0,36269000000.0,28162000000.0,,
Beginning Cash Position,45317000000.0,35934000000.0,36269000000.0,28162000000.0,30299000000.0,,
Changes In Cash,255000000.0,9383000000.0,-335000000.0,8107000000.0,-2137000000.0,,
Financing Cash Flow,-22279000000.0,-39656000000.0,-27476000000.0,-24833000000.0,-29006000000.0,,
Cash Flow From Continuing Financing Activities,-22279000000.0,-39656000000.0,-27476000000.0,-24833000000.0,-29006000000.0,,
Net Other Financing Charges,-418000000.0,-2960000000.0,-265000000.0,-2524000000.0,-326000000.0,,
Cash Dividends Paid,-3822000000.0,-3921000000.0,-3862000000.0,-3945000000.0,-3758000000.0,,
Common Stock Dividend Paid,-3822000000.0,-3921000000.0,-3862000000.0,-3945000000.0,-3758000000.0,,
Net Common Stock Issuance,-12288000000.0,-24701000000.0,-20132000000.0,-21075000000.0,-25898000000.0,,
Common Stock Payments,-12288000000.0,-24701000000.0,-20132000000.0,-21075000000.0,-25898000000.0,,
Net Issuance Payments Of Debt,-5751000000.0,-8074000000.0,-3217000000.0,2711000000.0,976000000.0,,
Net Short Term Debt Issuance,-1000000.0,-5910000000.0,-1967000000.0,3903000000.0,3976000000.0,,
Short Term Debt Payments,-1000000.0,-5910000000.0,,3903000000.0,3976000000.0,-7944000000.0,
Net Long Term Debt Issuance,-5750000000.0,-2164000000.0,-1250000000.0,-1192000000.0,-3000000000.0,,
Long Term Debt Payments,-5750000000.0,-2164000000.0,-1250000000.0,-5673000000.0,-3000000000.0,,
Long Term Debt Issuance,,,0.0,,,,0.0
Investing Cash Flow,-6168000000.0,-4886000000.0,-2587000000.0,5073000000.0,2917000000.0,,
Cash Flow From Continuing Investing Activities,-6168000000.0,-4886000000.0,-2587000000.0,5073000000.0,2917000000.0,,
Net Other Investing Changes,-1430000000.0,-154000000.0,-505000000.0,-340000000.0,-32000000.0,,
Net Investment Purchase And Sale,-2767000000.0,-2359000000.0,1160000000.0,8875000000.0,6020000000.0,,
Sale Of Investment,16972000000.0,10334000000.0,7976000000.0,14024000000.0,12338000000.0,,
Purchase Of Investment,-19739000000.0,-12693000000.0,-6816000000.0,-5149000000.0,-6318000000.0,,
Net PPE Purchase And Sale,-1971000000.0,-2373000000.0,-3242000000.0,-3462000000.0,-3071000000.0,,
Purchase Of PPE,-1971000000.0,-2373000000.0,-3242000000.0,-3462000000.0,-3071000000.0,,
Operating Cash Flow,28702000000.0,53925000000.0,29728000000.0,27867000000.0,23952000000.0,,
Cash Flow From Continuing Operating Activities,28702000000.0,53925000000.0,29728000000.0,27867000000.0,23952000000.0,,
Change In Working Capital,-6654000000.0,5548000000.0,-5707000000.0,-2034000000.0,-6507000000.0,,
Change In Other Current Liabilities,-5232000000.0,12533000000.0,4085000000.0,418000000.0,-3581000000.0,,
Change In Other Current Assets,-4079000000.0,-10250000000.0,-3081000000.0,-1745000000.0,-5310000000.0,,
Change In Payables And Accrued Expense,-13145000000.0,848000000.0,19381000000.0,-3875000000.0,-7933000000.0,,
Change In Payable,-13145000000.0,848000000.0,19381000000.0,-3875000000.0,-7933000000.0,,
Change In Account Payable,-13145000000.0,848000000.0,19381000000.0,-3875000000.0,-7933000000.0,,
Change In Inventory,-873000000.0,-211000000.0,177000000.0,365000000.0,643000000.0,,
Change In Receivables,16675000000.0,2628000000.0,-26269000000.0,2803000000.0,9674000000.0,,
Changes In Account Receivables,9448000000.0,-153000000.0,-12367000000.0,-1581000000.0,3669000000.0,,
Other Non Cash Items,-1189000000.0,-528000000.0,1659000000.0,469000000.0,-208000000.0,,
Stock Based Compensation,3528000000.0,3594000000.0,3183000000.0,3168000000.0,3226000000.0,,
Depreciation Amortization Depletion,3439000000.0,3214000000.0,3127000000.0,2830000000.0,2661000000.0,,
Depreciation And Amortization,3439000000.0,3214000000.0,3127000000.0,2830000000.0,2661000000.0,,
Net Income From Continuing Operations,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0,,

```

### Tool: get_income_statement

- Status: `ok`

```text
# Income Statement data for AAPL (quarterly)
# Data retrieved on: 2026-06-28 21:00:45

,2026-03-31,2025-12-31,2025-09-30,2025-06-30,2025-03-31
Tax Effect Of Unusual Items,0.0,0.0,0.0,0.0,0.0
Tax Rate For Calcs,0.175,0.175,0.162724,0.164,0.154555
Normalized EBITDA,39324000000.0,54066000000.0,35554000000.0,31032000000.0,32250000000.0
Net Income From Continuing Operation Net Minority Interest,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Reconciled Depreciation,3439000000.0,3214000000.0,3127000000.0,2830000000.0,2661000000.0
Reconciled Cost Of Revenue,56403000000.0,74525000000.0,54125000000.0,50318000000.0,50492000000.0
EBITDA,39324000000.0,54066000000.0,35554000000.0,31032000000.0,32250000000.0
EBIT,35885000000.0,50852000000.0,32427000000.0,28202000000.0,29589000000.0
Normalized Income,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Net Income From Continuing And Discontinued Operation,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Total Expenses,75299000000.0,92904000000.0,70039000000.0,65834000000.0,65770000000.0
Total Operating Income As Reported,35885000000.0,50852000000.0,32427000000.0,28202000000.0,29589000000.0
Diluted Average Shares,14725873000.0,14810356000.0,14863609000.0,14948179000.0,15056133000.0
Basic Average Shares,14673278000.0,14748158000.0,14815307000.0,14902886000.0,14994082000.0
Diluted EPS,2.01,2.84,1.85,1.57,1.65
Basic EPS,2.02,2.85,1.85,1.57,1.65
Diluted NI Availto Com Stockholders,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Net Income Common Stockholders,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Net Income,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Net Income Including Noncontrolling Interests,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Net Income Continuous Operations,29578000000.0,42097000000.0,27466000000.0,23434000000.0,24780000000.0
Tax Provision,6255000000.0,8905000000.0,5338000000.0,4597000000.0,4530000000.0
Pretax Income,35833000000.0,51002000000.0,32804000000.0,28031000000.0,29310000000.0
Other Income Expense,-52000000.0,150000000.0,377000000.0,-171000000.0,-279000000.0
Other Non Operating Income Expenses,-52000000.0,150000000.0,377000000.0,-171000000.0,-279000000.0
Operating Income,35885000000.0,50852000000.0,32427000000.0,28202000000.0,29589000000.0
Operating Expense,18896000000.0,18379000000.0,15914000000.0,15516000000.0,15278000000.0
Research And Development,11419000000.0,10887000000.0,8866000000.0,8866000000.0,8550000000.0
Selling General And Administration,7477000000.0,7492000000.0,7048000000.0,6650000000.0,6728000000.0
Gross Profit,54781000000.0,69231000000.0,48341000000.0,43718000000.0,44867000000.0
Cost Of Revenue,56403000000.0,74525000000.0,54125000000.0,50318000000.0,50492000000.0
Total Revenue,111184000000.0,143756000000.0,102466000000.0,94036000000.0,95359000000.0
Operating Revenue,111184000000.0,143756000000.0,102466000000.0,94036000000.0,95359000000.0

```
