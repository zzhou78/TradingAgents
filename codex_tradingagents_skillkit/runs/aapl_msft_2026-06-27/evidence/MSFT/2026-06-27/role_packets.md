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
# Data retrieved on: 2026-06-29 06:54:03

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
2026-06-26: 446.2722737121582
2026-06-25: 446.883790435791
2026-06-24: 447.594963684082
2026-06-23: 448.22708770751956
2026-06-22: 448.88125350952146
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 449.555401763916
2026-06-17: 450.1681071472168
2026-06-16: 450.7910632324219
2026-06-15: 451.35407653808596
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 451.8730308532715
2026-06-11: 452.4137333679199
2026-06-10: 452.9674659729004
2026-06-09: 453.50085525512696
2026-06-08: 453.98913818359375
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 454.4390010070801
2026-06-04: 454.88430313110354
2026-06-03: 455.3090647888184
2026-06-02: 455.75260498046873
2026-06-01: 456.13775329589845
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 456.41742752075197
2026-05-28: 456.7914582824707


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 40.48241450632475
2026-06-25: 28.7629288320608
2026-06-24: 32.48810369458887
2026-06-23: 35.3418191707639
2026-06-22: 30.958966947498133
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 34.982445722221506
2026-06-17: 34.662087384830656
2026-06-16: 40.27273126689767
2026-06-15: 42.831460041731475
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 37.195465375134724
2026-06-11: 36.93946989760487
2026-06-10: 39.56781082933335
2026-06-09: 41.95688626813507
2026-06-08: 45.466701181617495
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 47.65765705019186
2026-06-04: 53.14708757566906
2026-06-03: 52.83233730212237
2026-06-02: 60.224303044666215
2026-06-01: 73.323671885172
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 70.09099947692911
2026-05-28: 59.880834878109724


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: -13.754531420475189
2026-06-25: -14.108447858444322
2026-06-24: -12.30434046985215
2026-06-23: -11.108635311464752
2026-06-22: -10.284319877927885
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: -8.410602904903953
2026-06-17: -7.124649677593425
2026-06-16: -5.329784557379412
2026-06-15: -4.4804853794148585
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: -3.9350842755270037
2026-06-11: -2.26331456119334
2026-06-10: -0.05588089909355176
2026-06-09: 2.04765745221772
2026-06-08: 4.086751338785234
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 5.781788883536592
2026-06-04: 7.35920842266205
2026-06-03: 8.106838031083214
2026-06-02: 9.015457671714842
2026-06-01: 8.621652686242783
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 6.037682063014074
2026-05-28: 3.6984658768868144


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-05-28 to 2026-06-27:

2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 13.204891181723736
2026-06-25: 12.391421366525803
2026-06-24: 12.093839991024183
2026-06-23: 11.939519520832533
2026-06-22: 12.097943723757153
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: N/A: Not a trading day (weekend or holiday)
2026-06-18: 11.908554967231266
2026-06-17: 12.202290246411316
2026-06-16: 11.870929553977815
2026-06-15: 12.086385110113133
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 12.169183213535296
2026-06-11: 12.37681259759931
2026-06-10: 12.301183924217526
2026-06-09: 12.64127461971022
2026-06-08: 12.57521882122639
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 12.881004414896449
2026-06-04: 12.71261957571781
2026-06-03: 12.941283371205719
2026-06-02: 12.6244592029451
2026-06-01: 12.050187115641604
2026-05-31: N/A: Not a trading day (weekend or holiday)
2026-05-30: N/A: Not a trading day (weekend or holiday)
2026-05-29: 11.740200194549127
2026-05-28: 10.847908183522856


ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.
```

## Role: social

- Skill: `tradingagents-sentiment-analyst`

### Tool: fetch_stocktwits_messages

- Status: `ok`

```text
Bullish: 8 (27%) · Bearish: 3 (10%) · Unlabeled: 19 · Total: 30 most-recent messages

[2026-06-28T20:24:09Z · @Zamto · no-label] $MSFT will it be bearish because of Trump on monday
[2026-06-28T20:21:42Z · @MakeIGVGreatAgain · Bullish] $MSFT
[2026-06-28T20:17:27Z · @MarketMaestro1 · no-label] You need to pay close attention when these stocks reach these price levels:    1. $DRAM (DRAM) → Must buy under $80  2. $SPCX (SpaceX) → Must buy $135-$155  3. $NVDA (NVIDIA) → Must buy under $195  4. $MSFT (Microsoft) → Must buy under $350  5. $GOOG (Gooqle) →Must buy under $340…
[2026-06-28T20:12:44Z · @Nasdaq_Frontier · no-label] These are 5 high quality no brainers available in the market:    - $AMZN    - $META    - $MSFT    - $MA    - $BABA    Do you have better Risk/Reward 5?
[2026-06-28T20:10:16Z · @Unknown333 · Bullish] $MSFT latest news  gonna hit 450 eow , for sure 💯 very latest news is on the way you guys will see
[2026-06-28T20:10:07Z · @HitstheGreen · Bullish] $MSFT Financial Strength, Profitability, Growth, Valuation, and Momentum. GLTA long $MSFT
[2026-06-28T20:08:27Z · @RockyTSTH · no-label] OPTION WATCHLIST 6/28/2026    $ASTS- Stock down 50% from all time highs. Seeing some buyers coming in . looking for $80 plus if $70 holds. Stock seeing some call buyers coming in. high watch    $MSFT- Michael burry going long on the stock last week. Stock bouncing $20 from lows. …
[2026-06-28T20:04:01Z · @kcphaeton · no-label] $GOOG $META $MSFT $ORCL $QQQ @howardlindzon sometimes it’s good to have a breather and a pull back in order to allow folks to enter the market at a lower rate. Love buying stuff on sale. ￼
[2026-06-28T20:00:01Z · @NetflixUser · Bearish] $MSFT exactly. Same pattern as previous pops &gt; 2%
[2026-06-28T19:51:27Z · @Tesla5000 · no-label] $NFLX $MSFT   Microsoft has a rare opportunity to acquire Netflix if the company is trading significantly below its intrinsic value. Netflix’s global streaming platform, premium content, and hundreds of millions of subscribers would complement Microsoft’s strengths in artificial …
[2026-06-28T19:35:53Z · @TechTraderr1r · no-label] $MSFT is holding strong at $372.97 despite the broader sector noise. Institutional accumulation is clear—they are betting on Azure’s dominance in the AI era.
[2026-06-28T19:23:47Z · @ironmantrader777 · Bearish] $MSFT bull trap friday
[2026-06-28T19:12:27Z · @DocOctagon · Bullish] $MSFT $AAPL $MU People that keep bringing up China memory chips are either morons who haven&#39;t done any research or bears trying to push a narrative. China DRAM chips have significantly more power draw than Micron&#39;s chips which increases data center total cost of ownership…
[2026-06-28T19:06:17Z · @ba1980 · Bullish] $MSFT currently 375.54 on hyper.
[2026-06-28T18:52:46Z · @TheProphetOfProfit · no-label] $MSFT Buyers finally stepped in late last week at multi-year uptrend support on the weekly. Leaps look rather appetizing at this support.
[2026-06-28T18:45:13Z · @Unknown333 · no-label] $MSFT hit 400 monday
[2026-06-28T18:44:25Z · @holdingbags · no-label] $MSFT best case is for an undercut and go. Nice way to buy up the weekly, but still under the up trend line (UTL) and pivot.
[2026-06-28T18:35:37Z · @AshHydrogen · no-label] $PLTR replacing $MSFT at $DELL
[2026-06-28T18:33:40Z · @Mercy_forever · no-label] $NVDA $SPY $AMZN $MSFT $GOOGL This is huge.. Nvidia’s partnership with Firmus Technologies marks a strategic move to solidify its influence in the global AI infrastructure market. By supplying 170,000 advanced GPUs for a new Indonesian data center, Nvidia secures significant, lon…
[2026-06-28T18:28:33Z · @SkeletonEarFace · no-label] $MSFT on the way to 600 and every bear will be smoked
[2026-06-28T18:10:15Z · @TheHomelander · Bullish] $MSFT if $AAPL get their way with Chinese memory chips, the DRAM bubble pops and hyperscalers regain leadership.  You don’t think Trump or Lutnik will go for it? $MU price hikes showing up in inflation data. What do you think they want more? American company leadership or a rate …
[2026-06-28T18:07:10Z · @TheHomelander · no-label] $MSFT bear coping at its finest
[2026-06-28T18:06:20Z · @NetflixUser · Bearish] $MSFT I’ll say this again to warn - this will not close above $400 again in 2026
[2026-06-28T17:53:48Z · @StackRadar1 · no-label] $MSFT week of June 29
[2026-06-28T17:50:38Z · @ryanmcraver · no-label] Cash flow the majors shows the impact of AI investments $GOOG $META $ORCL $AMZN $MSFT
[2026-06-28T17:48:58Z · @MilhouseVanhouten · Bullish] $MSFT you have to be absolutely completely insane or just new and inexperienced to see this in a 6 month period, attached to Microsoft and not put every dime you own into it as soon as you can.
[2026-06-28T17:46:11Z · @Mercy_forever · Bullish] $ORCL (No position )But Holly crap down 100 point since JUN 01  A 40%  decline 🤯And I thought it’s trading at huge PE BUT NO it’s 25 PE with 13.63 forward LIKE WTF is  going on with this POS market or the FUCKERY that big HF and INSTITUTION try to pull or do Just effing insane $S…
[2026-06-28T17:44:42Z · @jontanaj · no-label] $MSFT https://youtu.be/HOKO-_iTaH8?is=AOQClzqe4rfh-L88
[2026-06-28T17:41:13Z · @SwingTraderPro1 · no-label] Out of ~70 mega-cap stocks ($200B+), leadership and laggards are starting to diverge in a big way.    Worst performers over the last 12 months:    $NFLX -43.5%  $ORCL -30.2%  $MSFT -25%  $META -24.2%  $PLTR -21.7%    These aren’t small caps or speculative names-these are core ind…
[2026-06-28T17:41:01Z · @Rdg57 · no-label] $MSFT $400 by Friday?
```

### Tool: fetch_reddit_posts

- Status: `ok`

```text
r/wallstreetbets — 5 recent posts mentioning MSFT (via RSS feed; scores/comments unavailable):
  [2026-06-28] MSFT - Bearish Cup & Handle Pattern - Next $342.
    body excerpt: MSFT - Bearish Cup & Handle Pattern - Next $342. Any thesis? https://preview.redd.it/22jnhtkcu2ah1.png?width=1210&format=png&auto=webp&s=ca2375942c616847795880875b7f546bf0db7cf1
  [2026-06-27] Microslop is on sale
    body excerpt: So Microsoft just had its worst month since the dot-com bubble and the bear case is they're spending TOO MUCH on AI. You're telling me Microsoft is shoveling billions into the biggest technological revolution in 25 years? Just like every ot…
  [2026-06-27] MSFT leaps and some long dated
    body excerpt: Will probably roll out the leaps
  [2026-06-27] MU $2000 is no longer a meme
    body excerpt: MU just dropped numbers that broke the old memory playbook. Q3 did $41.46B in revenue, up from $9.3B a year ago, EPS $25.11 when the street was looking for like $20. The part that actually got me was the margin, 85%, nobody had that modeled…
  [2026-06-26] 2x life savings in MSFT
    body excerpt: Brain smoother than Satya Nutella’s forehead

r/stocks: <no posts found mentioning MSFT in the past 7 days>

r/investing: <no posts found mentioning MSFT in the past 7 days>
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
# Data retrieved on: 2026-06-29 06:54:17

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
# Data retrieved on: 2026-06-29 06:54:17

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
# Data retrieved on: 2026-06-29 06:54:17

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
# Data retrieved on: 2026-06-29 06:54:18

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
# Data retrieved on: 2026-06-29 06:54:18

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

## Role: financial_report

- Skill: `tradingagents-financial-report-analyst`

### Tool: collect_financial_document_sources

- Status: `ok`

```text
## Financial Document Source Packet: MSFT

- Trade date: `2026-06-27`
- Collection status: `ok`
- SEC company name: MICROSOFT CORP
- SEC CIK: `0000789019`
- As-of rule: Only filings with filingDate <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| annual_report_10k | available | 2025-07-30 | 10-K | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm |
| quarterly_report_10q | available | 2026-04-29 | 10-Q | https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm |
| earnings_release_8k | available | 2026-04-29 | 8-K | https://www.sec.gov/Archives/edgar/data/789019/000119312526191457/msft-20260429.htm |
| investor_presentation | unavailable |  |  | No investor presentation source was discovered from the SEC submissions feed. |

### Section: annual_report_10k / business_overview

- Source section: 10-K business
- Filing date: `2025-07-30`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

```text
Item 1. Business 3 Information about our Executive Officers 14
```

### Section: annual_report_10k / risk_factors

- Source section: 10-K risk factors
- Filing date: `2025-07-30`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

```text
Item 1A. Risk Factors 16
```

### Section: annual_report_10k / segment_information

- Source section: 10-K segment information
- Filing date: `2025-07-30`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

```text
Segment Information and Geographic Data of the Notes to Financial Statements (Part II, Item 8 of this Form 10-K). Our reportable segments are described below. Productivity and Business Processes Our Productivity and Business Processes segment consists of products and services in our portfolio of productivity, communication, and information services, spanning a variety of devices and platforms. This segment primarily comprises: • Microsoft 365 Commercial products and cloud services, including Microsoft 365 Commercial cloud, comprising Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot; and Microsoft 365 Commercial products, comprising Windows Commercial on-premises and Office licensed on-premises. • Microsoft 365 Consumer products and cloud services, including Microsoft 365 Consumer subscriptions, Office licensed on-premises, and other consumer services. • LinkedIn, including Talent Solutions, Marketing Solutions, Premium Subscriptions, and Sales Solutions. • Dynamics products and cloud services, including Dynamics 365, comprising a set of intelligent, cloud-based applications across ERP, CRM, Power Apps, and Power Automate; and on-premises ERP and CRM applications. Microsoft 365 Commercial Products and Cloud Services Microsoft 365 Commercial is an AI-powered business and productivity solutions platform that brings together Office, Windows, Microsoft 365 Copilot, and Enterprise Mobility + Security to help organizations empower their employees. Growth depends on our ability to reach new users in new markets such as frontline workers, small and medium businesses, and growth markets, as well as add AI-enabled tools, features, and agentic scenarios to our core product and service offerings across communication, collaboration, analytics, security, compliance, and other AI business productivity categories. Microsoft 365 Commercial revenue is mainly affected by a combination of continued installed base growth and average revenue per user expansion, as well as the continued shift from Office licensed on-premises to Microsoft 365. Microsoft 365 Consumer Products and Cloud Services Microsoft 365 Consumer is designed to increase personal productivity and creativity through a range of products and services. Growth depends on our ability to reach new users, add value to our core product set with new features including AI tools, and continue to expand our product and service offerings into new markets. Microsoft 365 Consumer cloud revenue and Office Consumer products revenue is mainly affected by the percentage of customers that buy Office with their new devices and the continued shift from Office licensed on-premises to Microsoft 365 Consumer subscriptions. Microsoft 365 Consumer cloud revenue is also affected by the demand for communication and storage through Outlook.com and OneDrive, which is largely driven by subscriptions and advertising. 5 PART I Item 1 LinkedIn LinkedIn connects the world’s professionals to make them more productive and successful and transforms the way companies hire, market, sell, and learn. In addition to LinkedIn’s free services, LinkedIn offers monetized solutions designed to offer AI-enabled insights and productivity: Talent Solutions, Marketing Solutions, Premium Subscriptions, and Sales Solutions. Growth will depend on our ability to increase LinkedIn member engagement on the platform and our ability to continue offering insight and AI-enabled services that provide value for our members and customers. LinkedIn revenue is mainly affected by demand from enterprises and professionals for subscriptions to Talent Solutions, Sales Solutions, and Premium Subscriptions offerings, as well as member engagement and the quality of the sponsored content delivered to those members to drive Marketing Solutions. Dynamics Products and Cloud Services Dynamics provides cloud-based and on-premises business solutions for financial management, enterprise resource planning (“ERP”), customer relationship management (“CRM”), and supply chain management, as well as agentic AI and other low code application development platforms, for small and medium businesses, large organizations, and divisions of global enterprises. Dynamics revenue is driven by the number of users licensed and applications consumed, expansion of average revenue per user, and the continued shift to Dynamics 365, a unified set of cloud-based intelligent business applications, including our low code development platforms, such as Power Apps and Power Automate. Competition Competitors to Office include software and global application vendors, web-based and mobile application companies, AI-first application companies, as well as local application developers. We compete by providing secure, integrated industry-specific, and easy-to-use productivity and collaboration tools and services that create comprehensive solutions and work well with technologies our customers already have both on-premises or in the cloud. Windows faces competition from various software products and from alternative platforms and devices. Microsoft Defender for Endpoint competes with endpoint security solution providers. Our Enterprise Mobility + Security offerings compete with products from a range of competitors including identity vendors, security solution vendors, and numerous other security point solution vendors. LinkedIn faces competition from online professional networks; recruiting, talent management, and human resource services companies; job boards; companies that provide learning and development products and services; online and offline outlets that generate revenue from advertisers and marketers; and online and offline outlets for companies with lead generation and customer intelligence and insights. Dynamics competes with cloud-based and on-premises business
```

### Section: annual_report_10k / liquidity_and_capital_resources

- Source section: 10-K liquidity and capital resources
- Filing date: `2025-07-30`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

```text
LIQUIDITY AND CAPITAL RESOURCES We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities and cash commitments for investing and financing activities, such as dividends, share repurchases, debt maturities, material
```

### Section: annual_report_10k / commitments_capex_contractual_obligations

- Source section: 10-K commitments / capex / contractual obligations
- Filing date: `2025-07-30`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

```text
capital expenditures, and the transition tax related to the Tax Cuts and Jobs Act (“TCJA”), for at least the next 12 months and thereafter for the foreseeable future. Cash, Cash Equivalents, and Investments Cash, cash equivalents, and short-term investments totaled $94.6 billion and $75.5 billion as of June 30, 2025 and 2024, respectively. Equity and other investments were $15.4 billion and $14.6 billion as of June 30, 2025 and 2024, respectively. Our short-term investments are primarily intended to facilitate liquidity and capital preservation. They consist predominantly of highly liquid investment-grade fixed-income securities, diversified among industries and individual issuers. The investments are predominantly U.S. dollar-denominated securities, but also include foreign currency-denominated securities to diversify risk. Our fixed-income investments are exposed to interest rate risk and credit risk. The credit risk and average maturity of our fixed-income portfolio are managed to achieve economic returns that correlate to certain fixed-income indices. The settlement risk related to these investments is insignificant given that the short-term investments held are primarily highly liquid investment-grade fixed-income securities. Valuation In general, and where applicable, we use quoted prices in active markets for identical assets or liabilities to determine the fair value of our financial instruments. This pricing methodology applies to our Level 1 investments, such as U.S. government securities, common and preferred stock, and mutual funds. If quoted prices in active markets for identical assets or liabilities are not available to determine fair value, then we use quoted prices for similar assets and liabilities or inputs other than the quoted prices that are observable either directly or indirectly. This pricing methodology applies to our Level 2 investments, such as commercial paper, certificates of deposit, U.S. agency securities, foreign government bonds, mortgage- and asset-backed securities, corporate notes and bonds, and municipal securities. Level 3 investments are valued using internally-developed models with unobservable inputs. Assets and liabilities measured at fair value on a recurring basis using unobservable inputs are an immaterial portion of our portfolio. A majority of our investments are priced by pricing vendors and are generally Level 1 or Level 2 investments as these vendors either provide a quoted market price in an active market or use observable inputs for their pricing without applying significant adjustments. Broker pricing is used mainly when a quoted price is not available, the investment is not priced by our pricing vendors, or when a broker price is more reflective of fair values in the market in which the investment trades. Our broker-priced investments are generally classified as Level 2 investments because the broker prices these investments based on similar assets without applying significant adjustments. In addition, all our broker-priced investments have a sufficient level of trading volume to demonstrate that the fair values used are appropriate for these investments. Our fair value processes include controls that are designed to ensure appropriate fair values are recorded. These controls include model validation, review of key model inputs, analysis of period-over-period fluctuations, and independent recalculation of prices where appropriate. Cash Flows Cash from operations increased $17.6 billion to $136.2 billion for fiscal year 2025, primarily due to an increase in cash received from customers, offset in part by an increase in cash paid to suppliers and employees and cash used to pay income taxes. Cash used in financing increased $13.9 billion to $51.7 billion for fiscal year 2025, primarily due to a $9.5 billion increase in cash used for repayments of debt, net of proceeds. Cash used in investing decreased $24.4 billion to $72.6 billion for fiscal year 2025, primarily due to a $63.2 billion decrease in cash used for acquisitions of companies, net of cash acquired and divestitures, and purchases of intangible and other assets, offset in part by a $22.3 billion increase in cash used in net investment purchases, sales, and maturities, and a $20.1 billion increase in additions to property and equipment. 43 PART II Item 7 Debt Proceeds We issue debt to take advantage of favorable pricing and liquidity in the debt markets, reflecting our credit rating. The proceeds of these issuances were or will be used for general corporate purposes, which may include, among other things, funding for working capital,
```

### Excerpt: annual_report_10k

- Filing date: `2025-07-30`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

```text
10-K UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 FORM 10-K ☒ ANNUAL REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934 For the Fiscal Year Ended June 30 , 2025 OR ☐ TRANSITION REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934 For the Transition Period From to Commission File Number 001-37845 MICROSOFT CORPORATION Washington 91-1144442 (STATE OF INCORPORATION) (I.R.S. ID) ONE MICROSOFT WAY , REDMOND , Washington 98052-6399 ( 425 ) 882-8080 www.microsoft.com/investor Securities registered pursuant to Section 12(b) of the Act: Title of each class Trading Symbol Name of exchange on which registered Common stock, $ 0.00000625 par value per share MSFT Nasdaq 3.125% Notes due 2028 MSFT Nasdaq 2.625% Notes due 2033 MSFT Nasdaq Securities registered pursuant to Section 12(g) of the Act: N one Indicate by check mark if the registrant is a well-known seasoned issuer, as defined in Rule 405 of the Securities Act. Yes ☒ No ☐ Indicate by check mark if the registrant is not required to file reports pursuant to Section 13 or Section 15(d) of the Act. Yes ☐ No ☒ Indicate by check mark whether the registrant (1) has filed all reports required to be filed by Section 13 or 15(d) of the Securities Exchange Act of 1934 during the preceding 12 months (or for such shorter period that the registrant was required to file such reports), and (2) has been subject to such filing requirements for the past 90 days. Yes ☒ No ☐ Indicate by check mark whether the registrant has submitted electronically every Interactive Data File required to be submitted pursuant to Rule 405 of Regulation S-T (§232.405 of this chapter) during the preceding 12 months (or for such shorter period that the registrant was required to submit such files). Yes ☒ No ☐ Indicate by check mark whether the registrant is a large accelerated filer, an accelerated filer, a non-accelerated filer, a smaller reporting company, or an emerging growth company. See the definitions of “large accelerated filer,” “accelerated filer,” “smaller reporting company,” and “emerging growth company” in Rule 12b-2 of the Exchange Act. Large Accelerated Filer ☒ Accelerated Filer ☐ Non-accelerated Filer ☐ Smaller Reporting Company ☐ Emerging Growth Company ☐ If an emerging growth company, indicate by check mark if the registrant has elected not to use the extended transition period for complying with any new or revised financial accounting standards provided pursuant to Section 13(a) of the Exchange Act. ☐ Indicate by check mark whether the registrant has filed a report on and attestation to its management’s assessment of the effectiveness of its internal control over financial reporting under Section 404(b) of the Sarbanes-Oxley Act (15 U.S.C. 7262(b)) by the registered public accounting firm that prepared or issued its audit report. ☒ If securities are registered pursuant to Section 12(b) of the Act, indicate by check mark whether the financial statements of the registrant included in the filing reflect the correction of an error to previously issued financial statements. ☐ Indicate by check mark whether any of those error corrections are restatements that required a recovery analysis of incentive-based compensation received by any of the registrant’s executive officers during the relevant recovery period pursuant to §240.10D-1(b). ☐ Indicate by check mark whether the registrant is a shell company (as defined in Rule 12b-2 of the Act). Yes ☐ No ☒ As of December 31, 2024, the aggregate market value of the registrant’s common stock held by non-affiliates of the registrant was $ 3.1 trillion based on the closing sale price as reported on the NASDAQ National Market System. As of July 24, 2025, there were 7,433,166,379 shares of common stock outstanding. DOCUMENTS INCORPORATED BY REFERENCE Portions of the definitive Proxy Statement to be delivered to shareholders in connection with the Annual Meeting of Shareholders to be held on December 5, 2025 are incorporated by reference into Part III. MICROSOFT CORPORATION FORM 10-K For the Fiscal Year Ended June 30, 2025 INDEX Page PART I Item 1. Business 3 Information about our Executive Officers 14 Item 1A. Risk Factors 16 Item 1B. Unresolved Staff Comments 30 Item 1C. Cybersecurity 30 Item 2. Properties 32 Item 3. Legal Proceedings 32 Item 4. Mine Safety Disclosures 32 PART II Item 5. Market for Registrant’s Common Equity, Related Stockholder Matters, and Issuer Purchases of Equity Securities 33 Item 6. [Reserved] 34 Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations 35 Item 7A. Quantitative and Qualitative Disclosures About Market Risk 49 Item 8. Financial Statements and Supplementary Data 50 Item 9. Changes in and Disagreements with Accountants on Accounting and Financial Disclosure 89 Item 9A. Controls and Procedures 89 Report of Management on Internal Control over Financial Reporting 89 Report of Independent Registered Public Accounting Firm 90 Item 9B. Other Information 91 Item 9C. Disclosure Regarding Foreign Jurisdictions that Prevent Inspections 91 PART III Item 10. Directors, Executive Officers, and Corporate Governance 91 Item 11. Executive Compensation 91 Item 12. Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters 91 Item 13. Certain Relationships and Related Transactions, and Director Independence 91 Item 14. Principal Accountant Fees and Services 92 PART IV Item 15. Exhibit and Financial Statement Schedules 93 Item 16. Form 10-K Summary 100 Signatures 101 2 PART I Item 1 Note About Forward-Looking Statements This report includes estimates, projections, statements relating to our business plans, objectives, and expected operating results that are “forward-looking statements” within the meaning of the Private Securities Litigation Reform Act of 1995, Section 27A of the Securities Act of 1933, and Section 21E of the Securities Exchange Act of 1934.
```

### Section: quarterly_report_10q / risk_factors

- Source section: 10-Q risk factors
- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm

```text
Item 1A. Risk Factors 49
```

### Section: quarterly_report_10q / segment_information

- Source section: 10-Q segment information
- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm

```text
SEGMENT INFORMATION AND GEOGRAPHIC DATA In its operation of the business, management, including our chief operating decision maker (“CODM”), who is also our Chief Executive Officer , reviews certain financial information, including segmented internal profit and loss statements. The primary profitability measure used by the CODM to review segment operating results is operating income. The CODM uses operating income to allocate resources during our annual planning process and throughout the year, as well as to assess the performance of our segments, primarily by monitoring actual results compared to prior periods and expected results. During the periods presented, we reported our financial performance based on the following segments : Productivity and Business Processes, Intelligent Cloud, and More Personal Computing. 26 PART I Item 1 Our reportable segments are described below. Productivity and Business Processes Our Productivity and Business Processes segment consists of products and services in our portfolio of productivity, communication, and information services, spanning a variety of devices and platforms. This segment primarily comprises: • Microsoft 365 Commercial products and cloud services, including Microsoft 365 Commercial cloud, comprising Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot; and Microsoft 365 Commercial products, comprising Windows Commercial on-premises and Office licensed on-premises. • Microsoft 365 Consumer products and cloud services, including Microsoft 365 Consumer subscriptions, Office licensed on-premises, and other consumer services. • LinkedIn, including Talent Solutions, Marketing Solutions, Premium Subscriptions, and Sales Solutions. • Dynamics products and cloud services, including Dynamics 365, comprising a set of intelligent, cloud-based applications across ERP, CRM, Power Apps, and Power Automate; and on-premises ERP and CRM applications. Intelligent Cloud Our Intelligent Cloud segment consists of our public, private, and hybrid server products and cloud services that power modern business and developers. This segment primarily comprises: • Server products and cloud services, including Azure and other cloud services, comprising cloud and AI consumption-based services, GitHub cloud services, Nuance Healthcare cloud services, virtual desktop offerings, and other cloud services; and Server products, comprising SQL Server, Windows Server, Visual Studio, System Center, related Client Access Licenses, and other on-premises offerings. • Enterprise and partner services, including Enterprise Support Services, Industry Solutions, Nuance professional services, Microsoft Partner Network, and Learning Experience. More Personal Computing Our More Personal Computing segment consists of products and services that put customers at the center of the experience with our technology. This segment primarily comprises: • Windows and Devices, including Windows OEM licensing (Windows Pro and non-Pro licenses sold through the OEM channel) and Devices, comprising Surface and PC accessories. • Gaming, including Xbox hardware and Xbox content and services, comprising first- and third-party content (including games and in-game content), Xbox Game Pass and other subscriptions, Xbox Cloud Gaming, advertising, and other cloud services. • Search advertising (formerly Search and news advertising), comprising Bing, Copilot, Microsoft News, Microsoft Edge, and third-party affiliates. Revenue and costs are generally directly attributed to our segments. However, due to the integrated structure of our business, certain revenue recognized and costs incurred by one segment may benefit other segments. Revenue from certain contracts is allocated among the segments based on the relative value of the underlying products and services, which can include allocation based on actual prices charged, prices when sold separately, or estimated costs plus a profit margin. Cost of revenue is allocated in certain cases based on a relative revenue methodology. Operating expenses that are allocated primarily include those relating to our investments in AI infrastructure and training, as well as marketing of products and services, from which multiple segments benefit and are generally allocated based on relative gross margin. 27 PART I Item 1 In addition, certain costs are incurred at a corporate level and allocated to our segments. These allocated costs generally include legal, including settlements and fines, information technology, human resources, finance, excise taxes, field selling, shared facilities services, customer service and support, and severance incurred as part of a corporate program. Each allocation is measured differently based on the specific facts and circumstances of the costs being allocated and is generally based on relative gross margin or relative headcount. Segment revenue, cost of revenue, operating expenses, and operating income were as follows during the periods presented: (In millions) Three Months Ended March 31, Nine Months Ended March 31, 2026 2025 2026 2025 Productivity and Business Processes Revenue $ 35,013 $ 29,944 $ 102,149 $ 87,698 Cost of revenue 6,197 5,517 18,028 16,380 Operating expenses 7,843 7,048 22,142 20,538 Operating income $ 20,973 $ 17,379 $ 61,979 $ 50,780 Intelligent Cloud Revenue $ 34,681 $ 26,751 $ 98,485 $ 76,387 Cost of revenue 15,120 10,307 41,000 28,326 Operating expenses 5,808 5,349 16,468 15,612 Operating income $ 13,753 $ 11,095 $ 41,017 $ 32,449 More Personal Computing Revenue $ 13,192 $ 13,371 $ 41,198 $ 41,198 Cost of revenue 5,511 6,095 17,821 19,111 Operating expenses 4,009 3,750 11,739 11,111 Operating income $ 3,672 $ 3,526 $ 11,638 $ 10,976 Total Revenue $ 82,886 $ 70,066 $ 241,832 $ 205,283 Cost of revenue 26,828 21,919 76,849 63,817 Operating expenses
```

### Section: quarterly_report_10q / liquidity_and_capital_resources

- Source section: 10-Q liquidity and capital resources
- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm

```text
LIQUIDITY AND CAPITAL RESOURCES We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities and cash commitments for investing and financing activities, such as dividends, share repurchases, debt maturities, and material
```

### Section: quarterly_report_10q / commitments_capex_contractual_obligations

- Source section: 10-Q commitments / capex / contractual obligations
- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm

```text
capital expenditures, for at least the next 12 months and thereafter for the foreseeable future. Cash, Cash Equivalents, and Investments Cash, cash equivalents, and short-term investments totaled $78.3 billion and $94.6 billion as of March 31, 2026 and June 30, 2025, respectively. Equity and other investments were $33.7 billion and $15.4 billion as of March 31, 2026 and June 30, 2025, respectively. Our short-term investments are primarily intended to facilitate liquidity and capital preservation. They consist predominantly of highly liquid investment-grade fixed-income securities, diversified among industries and individual issuers. The investments are predominantly U.S. dollar-denominated securities, but also include foreign currency-denominated securities to diversify risk. Our fixed-income investments are exposed to interest rate risk and credit risk. The credit risk and average maturity of our fixed-income portfolio are managed to achieve economic returns that correlate to certain fixed-income indices. The settlement risk related to these investments is insignificant given that the short-term investments held are primarily highly liquid investment-grade fixed-income securities. Valuation In general, and where applicable, we use quoted prices in active markets for identical assets or liabilities to determine the fair value of our financial instruments. This pricing methodology applies to our Level 1 investments, such as U.S. government securities, common and preferred stock, and mutual funds. If quoted prices in active markets for identical assets or liabilities are not available to determine fair value, then we use quoted prices for similar assets and liabilities or inputs other than the quoted prices that are observable either directly or indirectly. This pricing methodology applies to our Level 2 investments, such as commercial paper, certificates of deposit, U.S. agency securities, foreign government bonds, mortgage- and asset-backed securities, corporate notes and bonds, and municipal securities. Level 3 investments are valued using internally-developed models with unobservable inputs. Assets and liabilities measured at fair value on a recurring basis using unobservable inputs are an immaterial portion of our portfolio. 43 PART I Item 2 A majority of our investments are priced by pricing vendors and are generally Level 1 or Level 2 investments as these vendors either provide a quoted market price in an active market or use observable inputs for their pricing without applying significant adjustments. Broker pricing is used mainly when a quoted price is not available, the investment is not priced by our pricing vendors, or when a broker price is more reflective of fair values in the market in which the investment trades. Our broker-priced investments are generally classified as Level 2 investments because the broker prices these investments based on similar assets without applying significant adjustments. In addition, all our broker-priced investments have a sufficient level of trading volume to demonstrate that the fair values used are appropriate for these investments. Our fair value processes include controls that are designed to ensure appropriate fair values are recorded. These controls include model validation, review of key model inputs, analysis of period-over-period fluctuations, and independent recalculation of prices where appropriate. Cash Flows Cash from operations increased $34.0 billion to $127.5 billion for the nine months ended March 31, 2026, primarily due to an increase in cash received from customers and a decrease in cash used to pay income taxes, offset in part by an increase in cash paid to suppliers. Cash used in financing decreased $88 million to $40.8 billion for the nine months ended March 31, 2026, primarily due to a $6.0 billion decrease in cash used for repayments of debt, offset in part by a $3.8 billion increase in common stock repurchases and a $1.8 billion increase in dividends paid. Cash used in investing increased $42.6 billion to $84.7 billion for the nine months ended March 31, 2026, primarily due to a $32.7 billion increase in additions to property and equipment, a $9.1 billion increase in other investing primarily to facilitate the purchase of components, and a $3.8 billion decrease in cash from net investment purchases, sales, and maturities. Debt Proceeds We issue debt to take advantage of favorable pricing and liquidity in the debt markets, reflecting our credit rating. The proceeds of these issuances were or will be used for general corporate purposes, which may include, among other things, funding for working capital,
```

### Excerpt: quarterly_report_10q

- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm

```text
10-Q UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 FORM 10- Q ☒ QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934 For the Quarterly Period Ended March 31, 2026 OR ☐ TRANSITION REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934 For the Transition Period From to Commission File Number 001-37845 MICROSOFT CORPORATION Washington 91-1144442 (STATE OF INCORPORATION) (I.R.S. ID) ONE MICROSOFT WAY , REDMOND , Washington 98052-6399 ( 425 ) 882-8080 www.microsoft.com/investor Securities registered pursuant to Section 12(b) of the Act: Title of each class Trading Symbol Name of exchange on which registered Common stock, $0.00000625 par value per share MSFT Nasdaq 3.125% Notes due 2028 MSFT Nasdaq 2.625% Notes due 2033 MSFT Nasdaq Indicate by check mark whether the registrant (1) has filed all reports required to be filed by Section 13 or 15(d) of the Securities Exchange Act of 1934 during the preceding 12 months (or for such shorter period that the registrant was required to file such reports), and (2) has been subject to such filing requirements for the past 90 days. Yes ☒ No ☐ Indicate by check mark whether the registrant has submitted electronically every Interactive Data File required to be submitted pursuant to Rule 405 of Regulation S-T (§232.405 of this chapter) during the preceding 12 months (or for such shorter period that the registrant was required to submit such files). Yes ☒ No ☐ Indicate by check mark whether the registrant is a large accelerated filer, an accelerated filer, a non-accelerated filer, a smaller reporting company, or an emerging growth company. See the definitions of “large accelerated filer,” “accelerated filer,” “smaller reporting company,” and “emerging growth company” in Rule 12b-2 of the Exchange Act. Large Accelerated Filer ☒ Accelerated Filer ☐ Non-accelerated Filer ☐ Smaller Reporting Company ☐ Emerging Growth Company ☐ If an emerging growth company, indicate by check mark if the registrant has elected not to use the extended transition period for complying with any new or revised financial accounting standards provided pursuant to Section 13(a) of the Exchange Act. ☐ Indicate by check mark whether the registrant is a shell company (as defined in Rule 12b-2 of the Exchange Act). Yes ☐ No ☒ Indicate the number of shares outstanding of each of the issuer’s classes of common stock, as of the latest practicable date. Class Outstanding as of April 23, 2026 Common Stock, $ 0.00000625 par value per share 7,428,434,704 shares MICROSOFT CORPORATION FORM 10-Q For the Quarter Ended March 31, 2026 INDEX Page PART I. FINANCIAL INFORMATION Item 1. Financial Statements a) Income Statements for the Three and Nine Months Ended March 31, 2026 and 2025 3 b) Comprehensive Income Statements for the Three and Nine Months Ended March 31, 2026 and 2025 4 c) Balance Sheets as of March 31, 2026 and June 30, 2025 5 d) Cash Flows Statements for the Three and Nine Months Ended March 31, 2026 and 2025 6 e) Stockholders’ Equity Statements for the Three and Nine Months Ended March 31, 2026 and 2025 7 f) Notes to Financial Statements 8 g) Report of Independent Registered Public Accounting Firm 30 Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations 31 Item 3. Quantitative and Qualitative Disclosures About Market Risk 48 Item 4. Controls and Procedures 48 PART II. OTHER INFORMATION Item 1. Legal Proceedings 49 Item 1A. Risk Factors 49 Item 2. Unregistered Sales of Equity Securities and Use of Proceeds 65 Item 5. Other Information 66 Item 6. Exhibits 67 SIGNATURE 68 2 PART I Item 1 PART I. FINANCI AL INFORMATION ITEM 1. FINA NCIAL STATEMENTS INCOME STA TEMENTS (In millions, except per share amounts) (Unaudited) Three Months Ended March 31, Nine Months Ended March 31, 2026 2025 2026 2025 Revenue: Product $ 15,089 $ 15,319 $ 47,462 $ 46,810 Service and other 67,797 54,747 194,370 158,473 Total revenue 82,886 70,066 241,832 205,283 Cost of revenue: Product 2,733 3,037 9,160 10,187 Service and other 24,095 18,882 67,689 53,630 Total cost of revenue 26,828 21,919 76,849 63,817 Gross margin 56,058 48,147 164,983 141,466 Research and development 8,915 8,198 25,565 23,659 Sales and marketing 6,814 6,212 19,115 18,369 General and administrative 1,931 1,737 5,669 5,233 Operating income 38,398 32,000 114,634 94,205 Other income (expense), net 942 ( 623 ) 7,253 ( 3,194 ) Income before income taxes 39,340 31,377 121,887 91,011 Provision for income taxes 7,562 5,553 23,904 16,412 Net income $ 31,778 $ 25,824 $ 97,983 $ 74,599 Earnings per share: Basic $ 4.28 $ 3.47 $ 13.19 $ 10.03 Diluted $ 4.27 $ 3.46 $ 13.14 $ 9.99 Weighted average shares outstanding: Basic 7,426 7,434 7,430 7,434 Diluted 7,445 7,461 7,457 7,466 Refer to accompanying notes. 3 PART I Item 1 COMPREHENSIVE IN COME STATEMENTS (In millions) (Unaudited) Three Months Ended March 31, Nine Months Ended March 31, 2026 2025 2026 2025 Net income $ 31,778 $ 25,824 $ 97,983 $ 74,599 Other comprehensive income (loss), net of tax: Net change related to derivatives 0 ( 20 ) ( 6 ) 4 Net change related to investments ( 239 ) 450 287 1,130 Translation adjustments and other ( 287 ) 353 ( 162 ) ( 377 ) Other comprehensive income (loss) ( 526 ) 783 119 757 Comprehensive income $ 31,252 $ 26,607 $ 98,102 $ 75,356 Refer to accompanying notes. 4 PART I Item 1 BALANCE SHEETS (In millions) (Unaudited) March 31, 2026 June 30, 2025 Assets Current assets: Cash and cash equivalents $ 32,105 $ 30,242 Short-term investments 46,167 64,323 Total cash, cash equivalents, and short-term investments 78,272 94,565 Accounts receivable, net of allowance for doubtful accounts of $ 794 and $ 944 60,041 69,905 Inventories 1,219 938 Other current assets 35,797 25,723 Total current assets 175,329 191,131 Property and equipment, net of accumulated depreciation of $ 111,723 and $ 93,653 283,228 204,966 Operating lease right-of-use assets 24,403 24,823 Equity
```

### 8-K Cover Page: earnings_release_8k

- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191457/msft-20260429.htm

```text
8-K UNITED STATES SECURITIES AND EXCHANGE COMMISSION WASHINGTON, D.C. 20549 FORM 8-K CURRENT REPORT PURSUANT TO SECTION 13 OR 15(D) OF THE SECURITIES EXCHANGE ACT OF 1934 Date of Report (Date of earliest event reported) April 29, 2026 Microsoft Corporation Washington 001-37845 91-1144442 (State or Other Jurisdiction of Incorporation) (Commission File Number) (IRS Employer Identification No.) One Microsoft Way , Redmond , Washington 98052-6399 ( 425 ) 882-8080 www.microsoft.com/investor Check the appropriate box below if the Form 8-K filing is intended to simultaneously satisfy the filing obligation of the registrant under any of the following provisions (see General Instruction A.2. below):  Written communications pursuant to Rule 425 under the Securities Act (17 CFR 230.425)  Soliciting material pursuant to Rule 14a-12 under the Exchange Act (17 CFR 240.14a-12)  Pre-commencement communications pursuant to Rule 14d-2(b) under the Exchange Act (17 CFR 240.14d-2(b))  Pre-commencement communications pursuant to Rule 13e-4(c) under the Exchange Act (17 CFR 240.13e-4(c)) Securities registered pursuant to Section 12(b) of the Act: Title of each class Trading Symbol Name of exchange on which registered Common stock, $0.00000625 par value per share MSFT Nasdaq 3.125% Notes due 2028 MSFT Nasdaq 2.625% Notes due 2033 MSFT Nasdaq Indicate by check mark whether the registrant is an emerging growth company as defined in Rule 405 of the Securities Act of 1933 (§230.405 of this chapter) or Rule 12b-2 of the Securities Exchange Act of 1934 (§240.12b-2 of this chapter). Emerging growth company ¨ If an emerging growth company, indicate by check mark if the registrant has elected not to use the extended transition period for complying with any new or revised financial accounting standards provided pursuant to Section 13(a) of the Exchange Act. ¨ Item 2.02. Results of Operations and Financial Condition On April 29, 2026, Microsoft Corporation issued a press release announcing its financial results for the fiscal quarter ended March 31, 2026. A copy of the press release is furnished as Exhibit 99.1 to this report. In accordance with General Instruction B.2 of Form 8-K, the information in this Current Report on Form 8-K, including Exhibit 99.1, shall not be deemed to be “filed” for purposes of Section 18 of the Securities Exchange Act of 1934, as amended (the “Exchange Act”), or otherwise subject to the liability of that section, and shall not be incorporated by reference into any registration statement or other document filed under the Securities Act of 1933, as amended, or the Exchange Act, except as shall be expressly set forth by specific reference in such filing. Item 9.01. Financial Statements and Exhibits (d) Exhibits: 99.1 Press release, dated April 29, 2026, issued by Microsoft Corporation 104 Cover Page Interactive Data File (embedded within the Inline XBRL document) SIGNATURE Pursuant to the requirements of the Securities Exchange Act of 1934, the registrant has duly caused this report to be signed on its behalf by the undersigned hereunto duly authorized. MICROSOFT CORPORATION Date: April 29, 2026 /s/ A LICE L . J OLLA Alice L. Jolla Corporate Vice President and Chief Accounting Officer
```

### Excerpt: earnings_release_8k

- Filing date: `2026-04-29`
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191457/msft-20260429.htm

```text
8-K UNITED STATES SECURITIES AND EXCHANGE COMMISSION WASHINGTON, D.C. 20549 FORM 8-K CURRENT REPORT PURSUANT TO SECTION 13 OR 15(D) OF THE SECURITIES EXCHANGE ACT OF 1934 Date of Report (Date of earliest event reported) April 29, 2026 Microsoft Corporation Washington 001-37845 91-1144442 (State or Other Jurisdiction of Incorporation) (Commission File Number) (IRS Employer Identification No.) One Microsoft Way , Redmond , Washington 98052-6399 ( 425 ) 882-8080 www.microsoft.com/investor Check the appropriate box below if the Form 8-K filing is intended to simultaneously satisfy the filing obligation of the registrant under any of the following provisions (see General Instruction A.2. below):  Written communications pursuant to Rule 425 under the Securities Act (17 CFR 230.425)  Soliciting material pursuant to Rule 14a-12 under the Exchange Act (17 CFR 240.14a-12)  Pre-commencement communications pursuant to Rule 14d-2(b) under the Exchange Act (17 CFR 240.14d-2(b))  Pre-commencement communications pursuant to Rule 13e-4(c) under the Exchange Act (17 CFR 240.13e-4(c)) Securities registered pursuant to Section 12(b) of the Act: Title of each class Trading Symbol Name of exchange on which registered Common stock, $0.00000625 par value per share MSFT Nasdaq 3.125% Notes due 2028 MSFT Nasdaq 2.625% Notes due 2033 MSFT Nasdaq Indicate by check mark whether the registrant is an emerging growth company as defined in Rule 405 of the Securities Act of 1933 (§230.405 of this chapter) or Rule 12b-2 of the Securities Exchange Act of 1934 (§240.12b-2 of this chapter). Emerging growth company ¨ If an emerging growth company, indicate by check mark if the registrant has elected not to use the extended transition period for complying with any new or revised financial accounting standards provided pursuant to Section 13(a) of the Exchange Act. ¨ Item 2.02. Results of Operations and Financial Condition On April 29, 2026, Microsoft Corporation issued a press release announcing its financial results for the fiscal quarter ended March 31, 2026. A copy of the press release is furnished as Exhibit 99.1 to this report. In accordance with General Instruction B.2 of Form 8-K, the information in this Current Report on Form 8-K, including Exhibit 99.1, shall not be deemed to be “filed” for purposes of Section 18 of the Securities Exchange Act of 1934, as amended (the “Exchange Act”), or otherwise subject to the liability of that section, and shall not be incorporated by reference into any registration statement or other document filed under the Securities Act of 1933, as amended, or the Exchange Act, except as shall be expressly set forth by specific reference in such filing. Item 9.01. Financial Statements and Exhibits (d) Exhibits: 99.1 Press release, dated April 29, 2026, issued by Microsoft Corporation 104 Cover Page Interactive Data File (embedded within the Inline XBRL document) SIGNATURE Pursuant to the requirements of the Securities Exchange Act of 1934, the registrant has duly caused this report to be signed on its behalf by the undersigned hereunto duly authorized. MICROSOFT CORPORATION Date: April 29, 2026 /s/ A LICE L . J OLLA Alice L. Jolla Corporate Vice President and Chief Accounting Officer
```

```
