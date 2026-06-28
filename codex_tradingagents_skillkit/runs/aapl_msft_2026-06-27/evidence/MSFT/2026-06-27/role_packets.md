# Codex Role Evidence Packet: MSFT

- Trade date: `2026-06-27`
- Instrument identity: `Microsoft Corporation`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for MSFT from 2026-05-28 to 2026-06-27
# Total records: 21
# Data retrieved on: 2026-06-28 21:00:45

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-05-28,412.98,429.49,412.67,426.99,47250500,0.0,0.0
2026-05-29,432.55,450.33,432.36,450.24,79654400,0.0,0.0
2026-06-01,464.84,466.32,458.27,460.52,53628900,0.0,0.0
2026-06-02,446.88,453.5,440.43,441.31,37036800,0.0,0.0
2026-06-03,438.45,440.39,424.25,427.34,39037000,0.0,0.0
2026-06-04,435.81,436.15,426.41,428.05,26899500,0.0,0.0
2026-06-05,428.34,429.47,414.4,416.67,34782200,0.0,0.0
2026-06-08,414.14,417.16,408.56,411.74,32086700,0.0,0.0
2026-06-09,409.03,411.98,398.48,403.41,35317300,0.0,0.0
2026-06-10,398.55,405.04,397.16,397.36,32576000,0.0,0.0
2026-06-11,395.21,396.85,384.0,390.34,47224100,0.0,0.0
2026-06-12,391.43,391.74,382.27,390.74,34865800,0.0,0.0
2026-06-15,396.8,401.75,392.85,399.76,32266400,0.0,0.0
2026-06-16,395.79,396.84,390.69,393.83,31506800,0.0,0.0
2026-06-17,390.25,390.37,377.32,378.91,41987800,0.0,0.0
2026-06-18,377.82,381.37,373.28,379.4,59714200,0.0,0.0
2026-06-22,375.74,381.63,367.07,367.34,45171100,0.0,0.0
2026-06-23,372.38,377.22,370.67,373.94,40647600,0.0,0.0
2026-06-24,371.57,378.88,364.78,365.46,44509900,0.0,0.0
2026-06-25,362.77,364.23,349.2,352.83,66179000,0.0,0.0
2026-06-26,357.15,376.61,355.43,372.97,186112200,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for MSFT

- Requested analysis date: 2026-06-27
- Latest trading row used: 2026-06-26
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 357.15 |
| High | 376.61 |
| Low | 355.43 |
| Close | 372.97 |
| Volume | 186112200 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 377.15 |
| close_50_sma | 410.52 |
| close_200_sma | 446.27 |
| rsi | 40.48 |
| boll | 400.11 |
| boll_ub | 459.65 |
| boll_lb | 340.56 |
| macd | -13.75 |
| macds | -9.66 |
| macdh | -4.09 |
| atr | 13.20 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-14 | 408.55 |
| 2026-05-15 | 421.01 |
| 2026-05-18 | 422.62 |
| 2026-05-19 | 416.52 |
| 2026-05-20 | 420.15 |
| 2026-05-21 | 419.09 |
| 2026-05-22 | 418.57 |
| 2026-05-26 | 416.03 |
| 2026-05-27 | 412.67 |
| 2026-05-28 | 426.99 |
| 2026-05-29 | 450.24 |
| 2026-06-01 | 460.52 |
| 2026-06-02 | 441.31 |
| 2026-06-03 | 427.34 |
| 2026-06-04 | 428.05 |
| 2026-06-05 | 416.67 |
| 2026-06-08 | 411.74 |
| 2026-06-09 | 403.41 |
| 2026-06-10 | 397.36 |
| 2026-06-11 | 390.34 |
| 2026-06-12 | 390.74 |
| 2026-06-15 | 399.76 |
| 2026-06-16 | 393.83 |
| 2026-06-17 | 378.91 |
| 2026-06-18 | 379.40 |
| 2026-06-22 | 367.34 |
| 2026-06-23 | 373.94 |
| 2026-06-24 | 365.46 |
| 2026-06-25 | 352.83 |
| 2026-06-26 | 372.97 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 410.5219696044922
2026-06-25: 411.2691949462891
2026-06-24: 412.05780334472655
2026-06-23: 412.4193896484375
2026-06-22: 412.34195922851563
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 412.44043395996096
2026-06-17: 412.32285400390623
2026-06-16: 412.1743621826172
2026-06-15: 411.7392449951172
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 411.19710205078127
2026-06-11: 410.7537365722656
2026-06-10: 410.33433654785154
2026-06-09: 409.5508209228516
2026-06-08: 408.6025994873047
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 407.67138122558595
2026-06-04: 406.74274353027346
2026-06-03: 405.62043212890626
2026-06-02: 404.7170776367187
2026-06-01: 403.51177185058594
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 402.06495666503906
2026-05-28: 400.8790222167969


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 446.2722749328613
2026-06-25: 446.88379150390625
2026-06-24: 447.5949649047852
2026-06-23: 448.22708892822266
2026-06-22: 448.8812547302246
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 449.55540283203123
2026-06-17: 450.16810821533204
2026-06-16: 450.79106430053713
2026-06-15: 451.35407760620114
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 451.8730320739746
2026-06-11: 452.41373443603516
2026-06-10: 452.96746704101565
2026-06-09: 453.5008563232422
2026-06-08: 453.98913940429685
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 454.43900207519533
2026-06-04: 454.88430404663086
2026-06-03: 455.3090660095215
2026-06-02: 455.7526062011719
2026-06-01: 456.1377548217773
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 456.41742904663084
2026-05-28: 456.7914601135254


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 40.482414506149695
2026-06-25: 28.76292883166267
2026-06-24: 32.48810369420689
2026-06-23: 35.3418191704048
2026-06-22: 30.958966947022148
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 34.982445721779655
2026-06-17: 34.66208738437896
2026-06-16: 40.27273126652913
2026-06-15: 42.83146004141534
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 37.19546537460398
2026-06-11: 36.939469897063596
2026-06-10: 39.56781082884556
2026-06-09: 41.95688626770651
2026-06-08: 45.466701181294255
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 47.65765704994542
2026-06-04: 53.14708757565234
2026-06-03: 52.832337302090636
2026-06-02: 60.22430304502888
2026-06-01: 73.32367188647409
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 70.09099947815089
2026-05-28: 59.88083487873983


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: -13.754531420546527
2026-06-25: -14.108447858521401
2026-06-24: -12.304340469935426
2026-06-23: -11.108635311554679
2026-06-22: -10.28431987802503
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: -8.410602905008886
2026-06-17: -7.124649677706827
2026-06-16: -5.32978455750191
2026-06-15: -4.480485379547133
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: -3.935084275669851
2026-06-11: -2.263314561347613
2026-06-10: -0.05588089926015982
2026-06-09: 2.047657452037811
2026-06-08: 4.086751338590943
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 5.781788883326726
2026-06-04: 7.359208422435415
2026-06-03: 8.106838030838446
2026-06-02: 9.015457671450463
2026-06-01: 8.621652685957201
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 6.037682062705642
2026-05-28: 3.698465876553712


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 13.20489118177869
2026-06-25: 12.391421366584984
2026-06-24: 12.093839991087915
2026-06-23: 11.939519520901168
2026-06-22: 12.097943723831065
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 11.908554967310863
2026-06-17: 12.202290246497036
2026-06-16: 11.870929554070129
2026-06-15: 12.086385110212547
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 12.169183213642357
2026-06-11: 12.376812597714608
2026-06-10: 12.301183924341693
2026-06-09: 12.641274619843939
2026-06-08: 12.575218821370395
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 12.881004415051532
2026-06-04: 12.712619575884823
2026-06-03: 12.941283371385579
2026-06-02: 12.624459203138796
2026-06-01: 12.050187115850198
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 11.740200194773765
2026-05-28: 10.847908183764776


ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.
```

## Role: social

- Skill: `tradingagents-sentiment-analyst`

### Tool: fetch_stocktwits_messages

- Status: `ok`

```text
Bullish: 10 (33%) · Bearish: 6 (20%) · Unlabeled: 14 · Total: 30 most-recent messages

[2026-06-28T10:10:20Z · @mynameisplissken · Bullish] $MSFT excited for monday. hope it opens above 380
[2026-06-28T10:07:35Z · @Michelroro123_ · Bullish] $MSFT When a stock like Microsoft worth over $2.7 trillion moves up over 5% in a single day on 186M+ volume, it is physically impossible for retail investors to cause it only institutions aggressive buying. This was massive institutional buying Hoping for rally.
[2026-06-28T06:54:42Z · @GlobalMarketBulletin · no-label] $MSFT Microsoft (MSFT) is pouring money into Azure, AI infrastructure, Copilot, and enterprise software growth. While margin pressure is making some analysts cautious, this blue-chip technology stock may still have one of the strongest wealth-building stories in the market. https…
[2026-06-28T06:19:48Z · @TheStockShrewd · Bullish] $MU BTW, after next quarters EPS, if this retains its P/E ratio of ≈ 27 the stock will be worth $2008   $QQQ $SPY $MSFT
[2026-06-28T05:13:48Z · @TheStockShrewd · Bullish] $MSFT Burry investment and institutional buying has potential to turn the sentiment around.  I think we’ll see $450 soon, who even cares about capex anymore on a company who continues to grow earnings lol. Micron just proved nobody cares
[2026-06-28T04:53:32Z · @TheStockShrewd · Bullish] $NKE yikes big bull trap with low price action but zero earnings to push  Rather buy $MSFT $META $MU instead
[2026-06-28T04:45:42Z · @TheStockShrewd · Bearish] $NKE so this deserves a higher PE than $META , $MSFT , and $MU ?   Yea… holding out until low $30 s
[2026-06-28T04:18:57Z · @EconomyEngine · no-label] $QQQ $SPY $TSLA $MSFT $AAPL  🇮🇷🇺🇸 IRGC warns US military bases in the Middle East &quot;will experience hell in the coming days.
[2026-06-28T03:48:17Z · @TheStockShrewd · Bullish] $MU $NVDA $META  $MSFT
[2026-06-28T03:19:32Z · @NetflixUser · Bearish] $MSFT U.S. strikes on Iranian military sites. U.S. Navy and Air Force fighter jets conducted the strikes on military targets at multiple locations in and near the Strait of Hormuz, CENTCOM said on Saturday night.  The new strikes follow Bahrain&amp;#39;s claim that Iranian drones…
[2026-06-28T02:10:43Z · @GlobalMarketBulletin · no-label] $AMZN $GOOGL $META $MSFT $NVDA These five technology giants are not just big names anymore. They are building the future of artificial intelligence, cloud infrastructure, AI chips, digital advertising, smart glasses, and autonomous networks which can make you a millionaire. https…
[2026-06-28T01:47:37Z · @spacechimp · no-label] $MSFT boolish for msft?
[2026-06-28T01:45:22Z · @Kaythu · Bearish] $MSFT WAR AGAIN!!!!!!
[2026-06-28T01:26:32Z · @Kaythu · Bearish] $MSFT The War with Iran continues!! There is no such thing as a ceasefire and no such thing as a deal. The fighting continues on both ends. Oil prices are likely to go up yet again! Whats the likelihood the stock market winds up red on Monday and the entire week as a result going…
[2026-06-28T01:13:59Z · @funkymonkey_ · Bullish] $APP $MSFT $NOW $SPY  Well said, it’s like a rubber band till it snaps 🚀  ⬇️
[2026-06-28T01:01:20Z · @Lolz122445666 · Bullish] $MSFT Entire Week will  be green.  Massive rotation is about to happen.
[2026-06-28T00:46:58Z · @Lost2much21 · Bullish] $MSFT is so extremely oversold that the  &quot; big short&quot; guy is betting big that this more than doubles in 2 years.  Read that again  December 2028 LEAP call options on Microsoft with a $700 strike price
[2026-06-28T00:34:12Z · @morgangj · no-label] $MSFT
[2026-06-28T00:32:47Z · @Dailytune · Bullish] $MSFT Funny how bears think US striking Iran will make this go red. Did the peace deal make this go green? I think more investors/funds will start to derisk now from semis and rotate back to safety in Mag7 for the summer break while they&#39;re at 52 week lows
[2026-06-28T00:23:33Z · @___dog___ · no-label] $QQQ $SPY $GOOGL $AMZN $MSFT
[2026-06-28T00:14:49Z · @EconomyEngine · no-label] $QQQ $SPY $GOOGL $AMZN $MSFT Kuwait says its air defenses are currently confronting hostile missile and drone attacks, shortly after Bahrain activated their sirens due to Iranian attacks.🔴🔴🔴🔴
[2026-06-28T00:14:01Z · @NetflixUser · Bearish] $MSFT Iran war back on! US resuming strikes and ceasefire / MOU toast. Should be a deep red Monday. Grats bears!
[2026-06-28T00:06:36Z · @Jumper567 · Bearish] $AAPL $MU and then there is $MSFT $GOOG who are silently sulking
[2026-06-28T00:06:35Z · @K_Money11 · no-label] $MSFT $NVDA $QQQ $SPY $TSLA  “They better stop or else!!!”-Future trump tweet.🤦‍♂️
[2026-06-28T00:05:27Z · @ranthor · no-label] @ITradeOnceADay lol, biggest? We have companies with losses and comical revenues going for ipo with 2 Trillion valuations…and that’s not scam but this is?  $MSFT lost more than entire bitcoin market cap in just 3 weeks, spcx is valued twice as mucb…Nvidia lost 1 trillion in marke…
[2026-06-28T00:04:48Z · @OptionsPlayers · no-label] $INTC $MSFT Glad you are enjoying. What’s your next target in the OP Vault?
[2026-06-28T00:04:32Z · @EconomyEngine · no-label] $QQQ $SPY $NVDA $TSLA $MSFT Iran launches strikes on US military assets in Bahrain, explosions reported.🔴🔴🔴🔴
[2026-06-28T00:00:39Z · @pnvoss · no-label] $SPY sticking to top 5. Oversold conditions can surge any moment. Down 13% might add $APP $MSFT or $NOW probably now.   China could surge back. Can&#39;t sell this oversold.   They keep running stocks from extremes to extremes. Very hard to time.
[2026-06-27T23:35:47Z · @Supraman1 · no-label] $MU  $MU $NVDA $SNDK $AAPL $MSFT
[2026-06-27T23:34:03Z · @Probably_Drunk · no-label] $MSFT My plans tonight you ask?  Well me and Netflixusers mom are going to go out for a nice dinner, and then we&#39;re gonna go back to her place to watch Netflix and.....
```

### Tool: fetch_reddit_posts

- Status: `ok`

```text
r/wallstreetbets: <no posts found mentioning MSFT in the past 7 days>

r/stocks: <no posts found mentioning MSFT in the past 7 days>

r/investing — 2 recent posts mentioning MSFT (via RSS feed; scores/comments unavailable):
  [2026-06-25] If you're not buying MSFT/MSFU at these prices what are you even doing?
    body excerpt: MSFT is something like ~$10 (2-3%) from it's November 2021 price. The company is printing money, with something like 18% revenue growth for 8 consecutive quarters. It's literally cheaper now than the April 2025 tariff crash. Biggest bargain…
  [2026-06-23] The Piping hot Current Market Condition
    body excerpt: Right now feels like a house of cards that is about to topple. A rally that started in the midst of a fresh war has gone on far longer that imagined. While stocks break ATHs repeatedly in a short span of time, prices are swinging erraticall…
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
## MSFT News, from 2026-06-20 to 2026-06-27:

### Microsoft (MSFT): One of the Best Cloud Computing Stocks to Buy According to Hedge Funds (source: Insider Monkey)
Microsoft Corporation (NASDAQ:MSFT) is one of the Best Cloud Computing Stocks to Buy According to Hedge Funds. On June 22, the company announced one of the largest single capacity additions in its history. In Pecos, Texas, Microsoft Corporation (NASDAQ:MSFT) plans to build a new data center campus, which further expands its global data center capacity by ~2 […]
Link: https://finance.yahoo.com/technology/articles/microsoft-msft-one-best-cloud-221720086.html

### Wix (WIX) Brings Wix Harmony Into Microsoft 365 Copilot Chat (source: Simply Wall St.)
Wix.com (NasdaqGS:WIX) is integrating its Wix Harmony website creation platform with Microsoft 365 Copilot through the OpenAI Apps SDK. The collaboration allows users to build and manage Wix Harmony websites directly inside the Microsoft 365 Copilot chat interface using natural language prompts. Users can access the wider Wix ecosystem from within Microsoft 365, aiming to streamline online presence creation and day to day business management. For investors watching Wix.com at a share price...
Link: https://finance.yahoo.com/markets/stocks/articles/wix-wix-brings-wix-harmony-220728893.html

### Teradata (TDC) Expands Cloud Partnerships As VantageCloud Adoption Picks Up (source: Simply Wall St.)
Teradata (NYSE:TDC) reports growing momentum in its cloud business tied to adoption of its VantageCloud platform. The company highlights new and expanded partnerships with major cloud providers, including AWS, Microsoft Azure, and Google Cloud. These developments point to a larger shift in Teradata’s model toward cloud based data and AI services for data intensive customers. Teradata is best known for helping large organizations manage and analyze complex data, and its VantageCloud platform...
Link: https://finance.yahoo.com/markets/stocks/articles/teradata-tdc-expands-cloud-partnerships-210700161.html

### Microsoft (MSFT)-Backed OpenAI May Wait Until 2027 for IPO (source: Insider Monkey)
Microsoft Corporation (NASDAQ:MSFT) is one of the 15 Best AI Stocks That Will Make You Rich in 10 Years. On June 26, 2026, Microsoft Corporation (NASDAQ:MSFT)-backed OpenAI is leaning toward waiting until next year for its public listing, the New York Times’ Rob Copeland and Mike Isaac reported, citing three people involved in the company’s […]
Link: https://finance.yahoo.com/technology/ai/articles/microsoft-msft-backed-openai-may-193218688.html

### Is Amazon.com (AMZN) One of the Top Trending US Stocks to Buy Now? (source: Insider Monkey)
Amazon.com, Inc. (NASDAQ:AMZN) is one of the top trending US stocks to buy now. Reuters reported on June 19 that Amazon.com, Inc. (NASDAQ:AMZN) announced on Friday that its Indian operations reached a significant milestone in water conservation. This came at a time when global tech giants are facing mounting pressure regarding their use of resources […]
Link: https://finance.yahoo.com/markets/stocks/articles/amazon-com-amzn-one-top-192057945.html

### Nancy Pelosi places big bets on two surging tech stocks (source: TheStreet)
Few congressional portfolios attract as much scrutiny as Nancy Pelosi's. Her husband, Paul Pelosi, who executes the family's trades, has previously disclosed bets on Microsoft and Alphabet that outpaced the S&P 500. His latest moves may draw even more attention. Investing.com ...
Link: https://www.thestreet.com/investing/stocks/nancy-pelosi-uber-intel-call-options

### Here’s What JPMorgan Thinks About Microsoft (MSFT) and Chevron’s 20-Year Agreement (source: Insider Monkey)
Microsoft Corporation (NASDAQ:MSFT) is one of the best trending AI stocks to watch in 2026. Following Microsoft Corporation (NASDAQ:MSFT) and Chevron’s signing of a 20-year agreement to supply natural-gas- fired power to a data-center campus in West Texas, JPMorgan stated that it considers the offtake as durable and believes “the most compelling element of the […]
Link: https://finance.yahoo.com/markets/stocks/articles/jpmorgan-thinks-microsoft-msft-chevron-190905266.html

### Cloudflare (NET) Announces New Initiative With Major Web Browsers (source: Insider Monkey)
Cloudflare, Inc. (NYSE:NET) is one of the best trending AI stocks to watch in 2026. Cloudflare, Inc. (NYSE:NET) announced on June 22 a new initiative with major Web browsers, including Google Chrome, Mozilla Firefox, and Microsoft Edge, focused on developing and submitting for “standardization a privacy-preserving protocol to help humans and bots prove that their […]
Link: https://finance.yahoo.com/technology/articles/cloudflare-net-announces-initiative-major-183903297.html

### EU Targets Microsoft (MSFT) and Amazon Cloud Units for Big Tech “Gatekeeper” Rules, Reuters Reports (source: Insider Monkey)
Microsoft Corporation (NASDAQ:MSFT) is one of the safe stocks for beginners to buy in 2026. Reuters reported on June 25 that, according to EU antitrust regulators, Amazon and Microsoft Corporation’s (NASDAQ:MSFT) cloud computing services should be designated as “gatekeepers” under landmark tech rules. This step would subject them to strict obligations aimed at curbing market […]
Link: https://finance.yahoo.com/technology/articles/eu-targets-microsoft-msft-amazon-183743473.html

### Why Investors Should Avoid Nebius Stock (source: Barchart)
Nebius has multiple potential negative catalysts and a very high valuation.
Link: https://www.barchart.com/story/news/3016917/why-investors-should-avoid-nebius-stock

### Commvault Systems (CVLT) Is Up 7.7% After Native Azure AI Cyber Resilience Deal - What's Changed (source: Simply Wall St.)
In late June 2026, Commvault announced a multiyear partnership with Microsoft to make its AI-driven cyber resilience technologies available as a native ISV service on Microsoft Azure, enabling enterprises to deploy, procure, and manage Commvault Cloud directly within the Azure platform. This move embeds Commvault more deeply into a very large cloud ecosystem, potentially accelerating adoption of its subscription-based resilience offerings across highly regulated industries seeking secure AI...
Link: https://finance.yahoo.com/markets/stocks/articles/commvault-systems-cvlt-7-7-180619817.html

### Michael Burry doubles down on beaten-down China tech (source: TheStreet)
The man who predicted the 2008 housing crash is making another contrarian call, and this time his sights are set on China. Hedge fund manager Michael Burry, who became famous after the film "The Big Short" chronicled his bet against subprime mortgages, revealed on Thursday, June 25, that he added ...
Link: https://www.thestreet.com/investing/stocks/jd-stock-michael-burry-doubles-down-beaten-down-china-tech


```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-20 and 2026-06-27
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for MSFT
# Data retrieved on: 2026-06-28 21:01:03

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,5004,0,,Stock Award(Grant) at price 0.00 per share.,JOLLA ALICE L,Officer,,2026-06-15,D
1,4500,1812780,,Sale at price 402.84 per share.,NUMOTO TAKESHI,Officer,,2026-06-10,D
2,2500,1031125,,Sale at price 412.45 per share.,NUMOTO TAKESHI,Officer,,2026-06-08,D
3,149,0,,Stock Award(Grant) at price 0.00 per share.,LIST TERI,Director,,2026-06-05,D
4,15,0,,Stock Award(Grant) at price 0.00 per share.,DI SIBIO CARMINE,Director,,2026-06-05,D
5,149,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2026-06-05,D
6,149,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2026-06-05,D
7,15500,7145314,,Sale at price 460.99 per share.,ALTHOFF JUDSON,Officer,,2026-06-01,D
8,1262,519242,,Sale at price 411.34 per share.,COLEMAN AMY,Officer,,2026-05-14,D
9,12320,5045643,,Sale at price 409.52 per share.,HOGAN KATHLEEN T,Officer,,2026-03-06,D
10,5000,1986750,,Purchase at price 397.35 per share.,STANTON JOHN W.,Director,,2026-02-18,D
11,145,0,,Stock Award(Grant) at price 0.00 per share.,LIST TERI,Director,,2026-01-30,D
12,145,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2026-01-30,D
13,145,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2026-01-30,D
14,145,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2026-01-30,D
15,150,0,,Stock Gift at price 0.00 per share.,HOGAN KATHLEEN T,Officer,,2025-12-10,D
16,2850,1364352,,Sale at price 478.72 per share.,NUMOTO TAKESHI,Officer,,2025-12-04,D
17,130,0,,Stock Award(Grant) at price 0.00 per share.,LIST TERI,Director,,2025-12-04,D
18,130,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2025-12-04,D
19,130,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2025-12-04,D
20,130,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2025-12-04,D
21,12750,6266829,,Sale at price 491.52 per share.,ALTHOFF JUDSON,Officer,,2025-12-02,D
22,3463,0,,Stock Gift at price 0.00 per share.,ALTHOFF JUDSON,Officer,,2025-11-20,D
23,3977,0,,Stock Gift at price 0.00 per share.,NADELLA SATYA,Chief Executive Officer,,2025-11-10,D
24,10000,0,,Stock Gift at price 0.00 per share.,SMITH BRADFORD LEE,President,,2025-11-06,D
25,38500,19967707,,Sale at price 518.49 - 519.21 per share.,SMITH BRADFORD LEE,President,,2025-11-03,D
26,6513,0,,Stock Award(Grant) at price 0.00 per share.,HOGAN KATHLEEN T,Officer,,2025-09-15,D
27,26151,0,,Stock Award(Grant) at price 0.00 per share.,ALTHOFF JUDSON,Officer,,2025-09-15,D
28,11583,0,,Stock Award(Grant) at price 0.00 per share.,NUMOTO TAKESHI,Officer,,2025-09-15,D
29,4022,0,,Stock Award(Grant) at price 0.00 per share.,COLEMAN AMY,Officer,,2025-09-15,D
30,4358,0,,Stock Award(Grant) at price 0.00 per share.,COLEMAN AMY,Officer,,2025-09-15,D
31,26151,0,,Stock Award(Grant) at price 0.00 per share.,SMITH BRADFORD LEE,President,,2025-09-15,D
32,26151,0,,Stock Award(Grant) at price 0.00 per share.,HOOD AMY E,Chief Financial Officer,,2025-09-15,D
33,125,0,,Stock Award(Grant) at price 0.00 per share.,LIST TERI,Director,,2025-09-10,D
34,125,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2025-09-10,D
35,125,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2025-09-10,D
36,125,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2025-09-10,D
37,149205,75315121,,Sale at price 503.00 - 507.56 per share.,NADELLA SATYA,Chief Executive Officer,,2025-09-03,D
38,20386,0,,Stock Award(Grant) at price 0.00 per share.,HOGAN KATHLEEN T,Officer,,2025-09-02,D
39,45220,0,,Stock Award(Grant) at price 0.00 per share.,ALTHOFF JUDSON,Officer,,2025-09-02,D
40,17223,0,,Stock Award(Grant) at price 0.00 per share.,NUMOTO TAKESHI,Officer,,2025-09-02,D
41,47877,0,,Stock Award(Grant) at price 0.00 per share.,SMITH BRADFORD LEE,President,,2025-09-02,D
42,308870,0,,Stock Award(Grant) at price 0.00 per share.,NADELLA SATYA,Chief Executive Officer,,2025-09-02,D
43,54053,0,,Stock Award(Grant) at price 0.00 per share.,HOOD AMY E,Chief Financial Officer,,2025-09-02,D
44,3813,0,,Stock Award(Grant) at price 0.00 per share.,JOLLA ALICE L,Officer,,2025-08-29,D
45,4850,2557506,,Sale at price 525.56 - 528.56 per share.,NUMOTO TAKESHI,Officer,,2025-08-12,D
46,20000,0,,Stock Gift at price 0.00 per share.,SMITH BRADFORD LEE,President,,2025-08-11,D
47,132,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2025-06-10,D
48,132,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2025-06-10,D
49,132,0,,Stock Award(Grant) at price 0.00 per share.,LIST-STOLL TERI L.,Director,,2025-06-10,D
50,132,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2025-06-10,D
51,3000,1389000,,Sale at price 463.00 per share.,NUMOTO TAKESHI,Officer,,2025-06-03,D
52,1000,460008,,Sale at price 460.01 per share.,NUMOTO TAKESHI,Officer,,2025-05-30,D
53,21500,9756152,,Sale at price 453.77 per share.,HOGAN KATHLEEN T,Officer,,2025-05-21,D
54,16000,7330817,,Sale at price 457.97 - 458.46 per share.,ALTHOFF JUDSON,Officer,,2025-05-19,D
55,13242,5985886,,Sale at price 452.01 per share.,COLEMAN AMY,Officer,,2025-05-15,D
56,3842,1684498,,Sale at price 390.57 - 438.82 per share.,SMITH BRADFORD LEE,President,,2025-05-05,D
57,81000,35302945,,Sale at price 433.17 - 436.29 per share.,SMITH BRADFORD LEE,President,,2025-05-05,D
58,3842,1450221,,Purchase at price 377.46 per share.,SMITH BRADFORD LEE,President,,2025-04-23,D
59,10370,0,,Stock Award(Grant) at price 0.00 per share.,COLEMAN AMY,Officer,,2025-04-15,D
60,151,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2025-01-31,D
61,151,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2025-01-31,D
62,151,0,,Stock Award(Grant) at price 0.00 per share.,LIST-STOLL TERI L.,Director,,2025-01-31,D
63,151,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2025-01-31,D
64,2500,1118530,,Sale at price 447.41 per share.,NUMOTO TAKESHI,Officer,,2024-12-09,D
65,132,0,,Stock Award(Grant) at price 0.00 per share.,LIST TERI,Director,,2024-12-09,D
66,132,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2024-12-09,D
67,132,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2024-12-09,D
68,132,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2024-12-09,D
69,2000,874634,,Sale at price 437.32 per share.,NUMOTO TAKESHI,Officer,,2024-12-04,D
70,3500,1500662,,Sale at price 423.48 - 430.87 per share.,NUMOTO TAKESHI,Officer,,2024-12-02,D
71,25000,10425000,,Sale at price 417.00 per share.,ALTHOFF JUDSON,Officer,,2024-11-22,D
72,1000,414720,,Sale at price 414.72 per share.,NUMOTO TAKESHI,Officer,,2024-11-22,D
73,4719,0,,Stock Gift at price 0.00 per share.,NADELLA SATYA,Chief Executive Officer,,2024-11-13,D
74,7200,3050340,,Sale at price 423.66 per share.,YOUNG CHRISTOPHER DAVID,Officer,,2024-11-12,D
75,7912,0,,Stock Award(Grant) at price 0.00 per share.,HOGAN KATHLEEN T,Officer,,2024-09-16,D
76,8990,0,,Stock Award(Grant) at price 0.00 per share.,YOUNG CHRISTOPHER DAVID,Officer,,2024-09-16,D
77,23374,0,,Stock Award(Grant) at price 0.00 per share.,ALTHOFF JUDSON,Officer,,2024-09-16,D
78,8511,0,,Stock Award(Grant) at price 0.00 per share.,NUMOTO TAKESHI,Officer,,2024-09-16,D
79,23374,0,,Stock Award(Grant) at price 0.00 per share.,SMITH BRADFORD LEE,President,,2024-09-16,D
80,23374,0,,Stock Award(Grant) at price 0.00 per share.,HOOD AMY E,Chief Financial Officer,,2024-09-16,D
81,17377,7156892,,Sale at price 411.85 per share.,HOGAN KATHLEEN T,Officer,,2024-09-10,D
82,2500,1027608,,Sale at price 411.04 per share.,NUMOTO TAKESHI,Officer,,2024-09-10,D
83,12500,0,,Stock Gift at price 0.00 per share.,SMITH BRADFORD LEE,President,,2024-09-10,D
84,40000,16103553,,Sale at price 402.59 - 403.30 per share.,SMITH BRADFORD LEE,President,,2024-09-09,D
85,146,0,,Stock Award(Grant) at price 0.00 per share.,STANTON JOHN W.,Director,,2024-09-06,D
86,146,0,,Stock Award(Grant) at price 0.00 per share.,MASON MARK A.L.,Director,,2024-09-06,D
87,146,0,,Stock Award(Grant) at price 0.00 per share.,LIST-STOLL TERI L.,Director,,2024-09-06,D
88,146,0,,Stock Award(Grant) at price 0.00 per share.,SCHARF CHARLES W,Director,,2024-09-06,D
89,38000,15600794,,Sale at price 410.55 per share.,HOOD AMY E,Chief Financial Officer,,2024-09-05,D
90,78353,32017224,,Sale at price 404.98 - 410.82 per share.,NADELLA SATYA,Chief Executive Officer,,2024-09-04,D
91,2450,0,,Stock Gift at price 0.00 per share.,HOOD AMY E,Chief Financial Officer,,2024-09-04,D
92,17224,0,,Stock Award(Grant) at price 0.00 per share.,HOGAN KATHLEEN T,Officer,,2024-09-03,D
93,19573,0,,Stock Award(Grant) at price 0.00 per share.,YOUNG CHRISTOPHER DAVID,Officer,,2024-09-03,D
94,32881,0,,Stock Award(Grant) at price 0.00 per share.,ALTHOFF JUDSON,Officer,,2024-09-03,D
95,14552,0,,Stock Award(Grant) at price 0.00 per share.,NUMOTO TAKESHI,Officer,,2024-09-03,D
96,40448,0,,Stock Award(Grant) at price 0.00 per share.,SMITH BRADFORD LEE,President,,2024-09-03,D
97,260949,0,,Stock Award(Grant) at price 0.00 per share.,NADELLA SATYA,Chief Executive Officer,,2024-09-03,D
98,45668,0,,Stock Award(Grant) at price 0.00 per share.,HOOD AMY E,Chief Financial Officer,,2024-09-03,D
99,4411,0,,Stock Award(Grant) at price 0.00 per share.,JOLLA ALICE L,Officer,,2024-08-30,D
100,14398,6009898,,Sale at price 417.41 per share.,NADELLA SATYA,Chief Executive Officer,,2024-08-23,I

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for MSFT
# Data retrieved on: 2026-06-28 21:01:03

Name: Microsoft Corporation
Sector: Technology
Industry: Software - Infrastructure
Market Cap: 2770583420928
PE Ratio (TTM): 22.227055
Forward PE: 19.256187
PEG Ratio: 1.15
Price to Book: 6.686806
EPS (TTM): 16.78
Forward EPS: 19.36884
Dividend Yield: 0.98
Beta: 1.103
52 Week High: 555.45
52 Week Low: 349.2
50 Day Average: 410.9738
200 Day Average: 447.9875
Revenue (TTM): 318272995328
Gross Profit: 217409994752
EBITDA: 184457003008
Net Income: 125215997952
Profit Margin: 0.39341998
Operating Margin: 0.46326
Return on Equity: 0.34013999
Return on Assets: 0.14814
Debt to Equity: 30.271
Current Ratio: 1.283
Book Value: 55.777
Free Cash Flow: 37011251200
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for MSFT (quarterly)
# Data retrieved on: 2026-06-28 21:01:04

,2026-03-31,2025-12-31,2025-09-30,2025-06-30,2025-03-31,2024-12-31,2024-09-30
Ordinary Shares Number,7429000000.0,7428838066.0,7433087554.0,7434158655.0,7433982235.0,,
Share Issued,7429000000.0,7428838066.0,7433087554.0,7434158655.0,7433982235.0,,
Net Debt,8157000000.0,15966000000.0,14359000000.0,12909000000.0,14053000000.0,,
Total Debt,56965000000.0,57607000000.0,60556000000.0,60588000000.0,60567000000.0,,
Tangible Book Value,275381000000.0,250964000000.0,222343000000.0,201366000000.0,178594000000.0,,
Invested Capital,454629000000.0,431137000000.0,406284000000.0,386630000000.0,364772000000.0,,
Working Capital,38668000000.0,50185000000.0,54070000000.0,49913000000.0,42438000000.0,,
Net Tangible Assets,275381000000.0,250964000000.0,222343000000.0,201366000000.0,178594000000.0,,
Capital Lease Obligations,16703000000.0,17345000000.0,17348000000.0,17437000000.0,17686000000.0,,
Common Stock Equity,414367000000.0,390875000000.0,363076000000.0,343479000000.0,321891000000.0,,
Total Capitalization,445790000000.0,426300000000.0,398452000000.0,383631000000.0,361773000000.0,,
Total Equity Gross Minority Interest,414367000000.0,390875000000.0,363076000000.0,343479000000.0,321891000000.0,,
Stockholders Equity,414367000000.0,390875000000.0,363076000000.0,343479000000.0,321891000000.0,,
Gains Losses Not Affecting Retained Earnings,-3228000000.0,-2702000000.0,-2761000000.0,-3347000000.0,-4833000000.0,,
Other Equity Adjustments,-3228000000.0,-2702000000.0,-2761000000.0,-3347000000.0,-4833000000.0,,
Retained Earnings,302526000000.0,280789000000.0,254873000000.0,237731000000.0,219759000000.0,,
Capital Stock,115069000000.0,112788000000.0,110964000000.0,109095000000.0,106965000000.0,,
Common Stock,115069000000.0,112788000000.0,110964000000.0,109095000000.0,106965000000.0,,
Total Liabilities Net Minority Interest,279861000000.0,274427000000.0,273275000000.0,275524000000.0,240733000000.0,,
Total Non Current Liabilities Net Minority Interest,143200000000.0,144422000000.0,138279000000.0,134306000000.0,126527000000.0,,
Other Non Current Liabilities,61481000000.0,58852000000.0,53588000000.0,45186000000.0,38536000000.0,,
Tradeand Other Payables Non Current,27941000000.0,27256000000.0,26569000000.0,25986000000.0,25061000000.0,,
Non Current Deferred Liabilities,5652000000.0,5544000000.0,5398000000.0,5545000000.0,5362000000.0,,
Non Current Deferred Revenue,2753000000.0,2668000000.0,2546000000.0,2710000000.0,2840000000.0,,
Non Current Deferred Taxes Liabilities,2899000000.0,2876000000.0,2852000000.0,2835000000.0,2522000000.0,,
Long Term Debt And Capital Lease Obligation,48126000000.0,52770000000.0,52724000000.0,57589000000.0,57568000000.0,,
Long Term Capital Lease Obligation,16703000000.0,17345000000.0,17348000000.0,17437000000.0,17686000000.0,,
Long Term Debt,31423000000.0,35425000000.0,35376000000.0,40152000000.0,39882000000.0,,
Current Liabilities,136661000000.0,130005000000.0,134996000000.0,141218000000.0,114206000000.0,,
Other Current Liabilities,24552000000.0,24311000000.0,22741000000.0,25020000000.0,22937000000.0,,
Current Deferred Liabilities,50924000000.0,51376000000.0,58987000000.0,64555000000.0,44636000000.0,,
Current Deferred Revenue,50924000000.0,51376000000.0,58987000000.0,64555000000.0,44636000000.0,,
Current Debt And Capital Lease Obligation,8839000000.0,4837000000.0,7832000000.0,2999000000.0,2999000000.0,,
Current Debt,8839000000.0,4837000000.0,7832000000.0,2999000000.0,2999000000.0,,
Other Current Borrowings,,,,2999000000.0,2999000000.0,5248000000.0,2249000000.0
Commercial Paper,,,,0.0,0.0,0.0,0.0
Pensionand Other Post Retirement Benefit Plans Current,11270000000.0,10103000000.0,9201000000.0,13709000000.0,10579000000.0,,
Payables And Accrued Expenses,41076000000.0,39378000000.0,36235000000.0,34935000000.0,33055000000.0,,
Payables,41076000000.0,39378000000.0,36235000000.0,34935000000.0,33055000000.0,,
Total Tax Payable,3563000000.0,2050000000.0,3655000000.0,7211000000.0,6805000000.0,,
Income Tax Payable,3563000000.0,2050000000.0,3655000000.0,7211000000.0,6805000000.0,,
Accounts Payable,37513000000.0,37328000000.0,32580000000.0,27724000000.0,26250000000.0,,
Total Assets,694228000000.0,665302000000.0,636351000000.0,619003000000.0,562624000000.0,,
Total Non Current Assets,518899000000.0,485112000000.0,447285000000.0,427872000000.0,405980000000.0,,
Other Non Current Assets,38599000000.0,37770000000.0,39435000000.0,40565000000.0,38234000000.0,,
Financial Assets,0.0,0.0,1182000000.0,272000000.0,273000000.0,,
Investments And Advances,33683000000.0,21202000000.0,10283000000.0,15133000000.0,15762000000.0,,
Investmentin Financial Assets,33683000000.0,21202000000.0,10283000000.0,2460000000.0,2275000000.0,,
Available For Sale Securities,10346000000.0,1620000000.0,2510000000.0,2460000000.0,2275000000.0,,
Financial Assets Designatedas Fair Value Through Profitor Loss Total,23337000000.0,19582000000.0,7773000000.0,,,,
Long Term Equity Investment,,,,12673000000.0,13487000000.0,13304000000.0,14278000000.0
Goodwill And Other Intangible Assets,138986000000.0,139911000000.0,140733000000.0,142113000000.0,143297000000.0,,
Other Intangible Assets,19325000000.0,20289000000.0,21236000000.0,22604000000.0,23968000000.0,,
Goodwill,119661000000.0,119622000000.0,119497000000.0,119509000000.0,119329000000.0,,
Net PPE,307631000000.0,286229000000.0,255652000000.0,229789000000.0,208414000000.0,,
Accumulated Depreciation,-111723000000.0,-104950000000.0,-98880000000.0,-93653000000.0,-87074000000.0,,
Gross PPE,419354000000.0,391179000000.0,354532000000.0,323442000000.0,295488000000.0,,
Leases,15444000000.0,14500000000.0,13610000000.0,12117000000.0,,,
Other Properties,24403000000.0,25103000000.0,24791000000.0,24823000000.0,295488000000.0,,
Machinery Furniture Equipment,197434000000.0,177892000000.0,154248000000.0,139243000000.0,,,
Buildings And Improvements,172260000000.0,163986000000.0,152433000000.0,137921000000.0,,,
Land And Improvements,9813000000.0,9698000000.0,9450000000.0,9338000000.0,,,
Properties,0.0,0.0,0.0,0.0,,,
Current Assets,175329000000.0,180190000000.0,189066000000.0,191131000000.0,156644000000.0,,
Other Current Assets,35797000000.0,33134000000.0,33030000000.0,25723000000.0,24478000000.0,,
Hedging Assets Current,44000000.0,6000000.0,7000000.0,10000000.0,6000000.0,,
Inventory,1219000000.0,1059000000.0,1130000000.0,938000000.0,848000000.0,,
Finished Goods,,,,,508000000.0,557000000.0,1127000000.0
Work In Process,,,,,13000000.0,7000000.0,11000000.0
Raw Materials,,,,,327000000.0,345000000.0,488000000.0
Receivables,60041000000.0,56535000000.0,52894000000.0,69905000000.0,51700000000.0,,
Accounts Receivable,60041000000.0,56535000000.0,52894000000.0,69905000000.0,51700000000.0,,
Allowance For Doubtful Accounts Receivable,-794000000.0,-729000000.0,-687000000.0,-944000000.0,-695000000.0,,
Gross Accounts Receivable,60835000000.0,57264000000.0,53581000000.0,70849000000.0,52395000000.0,,
Cash Cash Equivalents And Short Term Investments,78228000000.0,89456000000.0,102005000000.0,94555000000.0,79612000000.0,,
Other Short Term Investments,46123000000.0,65160000000.0,73156000000.0,64313000000.0,50784000000.0,,
Cash And Cash Equivalents,32105000000.0,24296000000.0,28849000000.0,30242000000.0,28828000000.0,,
Cash Equivalents,19374000000.0,14075000000.0,17483000000.0,18531000000.0,18148000000.0,,
Cash Financial,12731000000.0,10221000000.0,11366000000.0,11711000000.0,10680000000.0,,

```

### Tool: get_cashflow

- Status: `ok`

```text
# Cash Flow data for MSFT (quarterly)
# Data retrieved on: 2026-06-28 21:01:04

,2026-03-31,2025-12-31,2025-09-30,2025-06-30,2025-03-31,2024-12-31,2024-09-30
Free Cash Flow,15803000000.0,5882000000.0,25663000000.0,25568000000.0,20299000000.0,,
Repurchase Of Capital Stock,-4627000000.0,-7415000000.0,-5650000000.0,-4546000000.0,-4781000000.0,,
Repayment Of Debt,0.0,-3000000000.0,0.0,0.0,-2250000000.0,,
Issuance Of Debt,,,,0.0,0.0,0.0,0.0
Issuance Of Capital Stock,541000000.0,259000000.0,689000000.0,548000000.0,546000000.0,,
Capital Expenditure,-30876000000.0,-29876000000.0,-19394000000.0,-17079000000.0,-16745000000.0,,
End Cash Position,32105000000.0,24296000000.0,28849000000.0,30242000000.0,28828000000.0,,
Beginning Cash Position,24296000000.0,28849000000.0,30242000000.0,28828000000.0,17482000000.0,,
Effect Of Exchange Rate Changes,-114000000.0,11000000.0,-92000000.0,183000000.0,52000000.0,,
Changes In Cash,7923000000.0,-4564000000.0,-1301000000.0,1231000000.0,11294000000.0,,
Financing Cash Flow,-11351000000.0,-17617000000.0,-11799000000.0,-10844000000.0,-13036000000.0,,
Cash Flow From Continuing Financing Activities,-11351000000.0,-17617000000.0,-11799000000.0,-10844000000.0,-13036000000.0,,
Net Other Financing Charges,-509000000.0,-699000000.0,-669000000.0,-677000000.0,-382000000.0,,
Cash Dividends Paid,-6756000000.0,-6762000000.0,-6169000000.0,-6169000000.0,-6169000000.0,,
Common Stock Dividend Paid,-6756000000.0,-6762000000.0,-6169000000.0,-6169000000.0,-6169000000.0,,
Net Common Stock Issuance,-4086000000.0,-7156000000.0,-4961000000.0,-3998000000.0,-4235000000.0,,
Common Stock Payments,-4627000000.0,-7415000000.0,-5650000000.0,-4546000000.0,-4781000000.0,,
Common Stock Issuance,541000000.0,259000000.0,689000000.0,548000000.0,546000000.0,,
Net Issuance Payments Of Debt,0.0,-3000000000.0,0.0,0.0,-2250000000.0,,
Net Short Term Debt Issuance,0.0,0.0,0.0,0.0,0.0,,
Short Term Debt Payments,,0.0,,,,0.0,
Net Long Term Debt Issuance,0.0,-3000000000.0,0.0,0.0,-2250000000.0,,
Long Term Debt Payments,0.0,-3000000000.0,0.0,0.0,-2250000000.0,,
Long Term Debt Issuance,,,,0.0,0.0,0.0,0.0
Investing Cash Flow,-27405000000.0,-22705000000.0,-34559000000.0,-30572000000.0,-12714000000.0,,
Cash Flow From Continuing Investing Activities,-27405000000.0,-22705000000.0,-34559000000.0,-30572000000.0,-12714000000.0,,
Net Other Investing Changes,-2599000000.0,-637000000.0,-6209000000.0,2642000000.0,604000000.0,,
Net Investment Purchase And Sale,6328000000.0,8263000000.0,-8378000000.0,-14392000000.0,4408000000.0,,
Sale Of Investment,18334000000.0,18108000000.0,9293000000.0,7239000000.0,8882000000.0,,
Purchase Of Investment,-12006000000.0,-9845000000.0,-17671000000.0,-21631000000.0,-4474000000.0,,
Net Business Purchase And Sale,-258000000.0,-455000000.0,-578000000.0,-1743000000.0,-981000000.0,,
Purchase Of Business,-258000000.0,-455000000.0,-578000000.0,-1743000000.0,-981000000.0,,
Net PPE Purchase And Sale,-30876000000.0,-29876000000.0,-19394000000.0,-17079000000.0,-16745000000.0,,
Purchase Of PPE,-30876000000.0,-29876000000.0,-19394000000.0,-17079000000.0,-16745000000.0,,
Operating Cash Flow,46679000000.0,35758000000.0,45057000000.0,42647000000.0,37044000000.0,,
Cash Flow From Continuing Operating Activities,46183000000.0,35758000000.0,45057000000.0,42647000000.0,36038000000.0,,
Change In Working Capital,331000000.0,-9632000000.0,-218000000.0,3303000000.0,2042000000.0,,
Change In Other Working Capital,2130000000.0,-8403000000.0,-8362000000.0,19404000000.0,266000000.0,,
Change In Other Current Liabilities,923000000.0,1609000000.0,-5984000000.0,4079000000.0,2448000000.0,,
Change In Other Current Assets,-174000000.0,-669000000.0,-1556000000.0,-3268000000.0,558000000.0,,
Change In Payables And Accrued Expense,2320000000.0,1197000000.0,-614000000.0,-652000000.0,1179000000.0,,
Change In Payable,2320000000.0,1197000000.0,-614000000.0,-652000000.0,1179000000.0,,
Change In Account Payable,2320000000.0,1197000000.0,-614000000.0,-652000000.0,1179000000.0,,
Change In Tax Payable,,,,,1298000000.0,-3395000000.0,1016000000.0
Change In Income Tax Payable,,,,,1298000000.0,-3395000000.0,1016000000.0
Change In Inventory,-161000000.0,70000000.0,-192000000.0,-81000000.0,52000000.0,,
Change In Receivables,-4707000000.0,-3436000000.0,16490000000.0,-16179000000.0,-2461000000.0,,
Changes In Account Receivables,-4707000000.0,-3436000000.0,16490000000.0,-16179000000.0,-2461000000.0,,
Other Non Cash Items,496000000.0,,,,1006000000.0,,
Stock Based Compensation,3081000000.0,3219000000.0,2983000000.0,3073000000.0,2980000000.0,,
Unrealized Gain Loss On Investment Securities,-1621000000.0,,635000000.0,36000000.0,-135000000.0,-25000000.0,
Asset Impairment Charge,37000000.0,,14000000.0,45000000.0,24000000.0,867000000.0,
Deferred Tax,2602000000.0,4446000000.0,2491000000.0,-2221000000.0,-2244000000.0,,
Deferred Income Tax,2602000000.0,4446000000.0,2491000000.0,-2221000000.0,-2244000000.0,,
Depreciation Amortization Depletion,10167000000.0,9198000000.0,13061000000.0,11203000000.0,7734000000.0,,
Depreciation And Amortization,10167000000.0,9198000000.0,13061000000.0,11203000000.0,7734000000.0,,
Depreciation,10167000000.0,9198000000.0,13061000000.0,11203000000.0,7734000000.0,,
Operating Gains Losses,-192000000.0,-9931000000.0,-1656000000.0,-25000000.0,-187000000.0,,
Gain Loss On Investment Securities,-192000000.0,,-1656000000.0,-25000000.0,-187000000.0,134000000.0,
Net Income From Continuing Operations,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0,,

```

### Tool: get_income_statement

- Status: `ok`

```text
# Income Statement data for MSFT (quarterly)
# Data retrieved on: 2026-06-28 21:01:04

,2026-03-31,2025-12-31,2025-09-30,2025-06-30,2025-03-31
Tax Effect Of Unusual Items,281390000.0,65200000.0,187150000.0,495125.091979,69660000.0
Tax Rate For Calcs,0.19,0.2,0.19,0.165042,0.18
Normalized EBITDA,48804000000.0,57854000000.0,47075000000.0,44431000000.0,39318000000.0
Total Unusual Items,1481000000.0,326000000.0,985000000.0,3000000.0,387000000.0
Total Unusual Items Excluding Goodwill,1481000000.0,326000000.0,985000000.0,3000000.0,387000000.0
Net Income From Continuing Operation Net Minority Interest,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Reconciled Depreciation,10167000000.0,9198000000.0,13061000000.0,11203000000.0,7734000000.0
Reconciled Cost Of Revenue,26828000000.0,25978000000.0,24043000000.0,24014000000.0,21919000000.0
EBITDA,50285000000.0,58180000000.0,48060000000.0,44434000000.0,39705000000.0
EBIT,40118000000.0,48982000000.0,34999000000.0,33231000000.0,31971000000.0
Net Interest Income,-48000000.0,104000000.0,278000000.0,154000000.0,3000000.0
Interest Expense,778000000.0,736000000.0,698000000.0,615000000.0,594000000.0
Interest Income,730000000.0,840000000.0,976000000.0,769000000.0,597000000.0
Normalized Income,30578390000.0,38197200000.0,26949150000.0,27230495125.09198,25506660000.0
Net Income From Continuing And Discontinued Operation,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Total Expenses,44488000000.0,42998000000.0,39712000000.0,42118000000.0,38066000000.0
Total Operating Income As Reported,38398000000.0,38275000000.0,37961000000.0,34323000000.0,32000000000.0
Diluted Average Shares,7445000000.0,7460000000.0,7466000000.0,7461000000.0,7461000000.0
Basic Average Shares,7426000000.0,7431000000.0,7433000000.0,7432000000.0,7434000000.0
Diluted EPS,4.27,5.16,3.72,3.65,3.46
Basic EPS,4.28,5.18,3.73,3.66,3.47
Diluted NI Availto Com Stockholders,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Net Income Common Stockholders,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Net Income,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Net Income Including Noncontrolling Interests,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Net Income Continuous Operations,31778000000.0,38458000000.0,27747000000.0,27233000000.0,25824000000.0
Tax Provision,7562000000.0,9788000000.0,6554000000.0,5383000000.0,5553000000.0
Pretax Income,39340000000.0,48246000000.0,34301000000.0,32616000000.0,31377000000.0
Other Income Expense,990000000.0,9867000000.0,-3938000000.0,-1861000000.0,-626000000.0
Other Non Operating Income Expenses,-491000000.0,9541000000.0,-4923000000.0,-1864000000.0,-1013000000.0
Special Income Charges,-37000000.0,-59000000.0,-14000000.0,-45000000.0,-24000000.0
Write Off,37000000.0,59000000.0,14000000.0,45000000.0,24000000.0
Gain On Sale Of Security,1518000000.0,385000000.0,999000000.0,48000000.0,411000000.0
Net Non Operating Interest Income Expense,-48000000.0,104000000.0,278000000.0,154000000.0,3000000.0
Interest Expense Non Operating,778000000.0,736000000.0,698000000.0,615000000.0,594000000.0
Interest Income Non Operating,730000000.0,840000000.0,976000000.0,769000000.0,597000000.0
Operating Income,38398000000.0,38275000000.0,37961000000.0,34323000000.0,32000000000.0
Operating Expense,17660000000.0,17020000000.0,15669000000.0,18104000000.0,16147000000.0
Research And Development,8915000000.0,8504000000.0,8146000000.0,8829000000.0,8198000000.0
Selling General And Administration,8745000000.0,8516000000.0,7523000000.0,9275000000.0,7949000000.0
Selling And Marketing Expense,6814000000.0,6584000000.0,5717000000.0,7285000000.0,6212000000.0
General And Administrative Expense,1931000000.0,1932000000.0,1806000000.0,1990000000.0,1737000000.0
Other Gand A,1931000000.0,1932000000.0,1806000000.0,1990000000.0,1737000000.0
Gross Profit,56058000000.0,55295000000.0,53630000000.0,52427000000.0,48147000000.0
Cost Of Revenue,26828000000.0,25978000000.0,24043000000.0,24014000000.0,21919000000.0
Total Revenue,82886000000.0,81273000000.0,77673000000.0,76441000000.0,70066000000.0
Operating Revenue,82886000000.0,81273000000.0,77673000000.0,76441000000.0,70066000000.0

```
