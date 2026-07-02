# Codex Role Evidence Packet: MPL.AX

- Trade date: `2026-07-02`
- Instrument identity: `Medibank Private Limited`

These packets are evidence only. Codex must act each role independently using the named skill.

## Role: market

- Skill: `tradingagents-market-analyst`

### Tool: get_stock_data

- Status: `ok`

```text
# Stock data for MPL.AX from 2026-06-02 to 2026-07-02
# Total records: 22
# Data retrieved on: 2026-07-02 22:06:59

Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2026-06-02,4.7,4.71,4.6,4.69,5640132,0.0,0.0
2026-06-03,4.71,4.73,4.63,4.67,3902373,0.0,0.0
2026-06-04,4.7,4.72,4.65,4.72,6390186,0.0,0.0
2026-06-05,4.76,4.8,4.74,4.78,5833186,0.0,0.0
2026-06-09,4.8,4.87,4.79,4.84,5278657,0.0,0.0
2026-06-10,4.86,4.91,4.79,4.84,7158497,0.0,0.0
2026-06-11,4.88,4.96,4.84,4.96,5377249,0.0,0.0
2026-06-12,4.96,5.03,4.94,4.97,4950767,0.0,0.0
2026-06-15,4.97,4.98,4.82,4.84,5944915,0.0,0.0
2026-06-16,4.83,4.88,4.8,4.84,5155220,0.0,0.0
2026-06-17,4.85,4.87,4.79,4.85,6736931,0.0,0.0
2026-06-18,4.84,4.9,4.84,4.9,5921623,0.0,0.0
2026-06-19,4.9,4.91,4.84,4.85,14385950,0.0,0.0
2026-06-22,4.87,4.94,4.83,4.91,4124525,0.0,0.0
2026-06-23,4.91,4.93,4.85,4.9,5972738,0.0,0.0
2026-06-24,4.9,4.94,4.86,4.86,8071075,0.0,0.0
2026-06-25,4.88,5.01,4.86,4.99,8989030,0.0,0.0
2026-06-26,4.95,5.0,4.91,4.97,7929773,0.0,0.0
2026-06-29,4.98,5.05,4.96,4.97,5254465,0.0,0.0
2026-06-30,4.98,5.04,4.97,4.97,7699142,0.0,0.0
2026-07-01,4.92,4.98,4.91,4.92,6087507,0.0,0.0
2026-07-02,4.92,4.99,4.89,4.99,9936584,0.0,0.0

```

### Tool: get_verified_market_snapshot

- Status: `ok`

```text
## Verified market data snapshot for MPL.AX

- Requested analysis date: 2026-07-02
- Latest trading row used: 2026-07-02
- Rows after the requested analysis date are excluded before verification.

### Latest verified OHLCV row

| Field | Value |
|---|---:|
| Open | 4.92 |
| High | 4.99 |
| Low | 4.89 |
| Close | 4.99 |
| Volume | 9936584 |

### Verified technical indicators (latest row)

| Indicator | Value |
|---|---:|
| close_10_ema | 4.94 |
| close_50_sma | 4.77 |
| close_200_sma | 4.63 |
| rsi | 60.91 |
| boll | 4.89 |
| boll_ub | 5.04 |
| boll_lb | 4.74 |
| macd | 0.06 |
| macds | 0.06 |
| macdh | 0.00 |
| atr | 0.09 |

### Recent verified closes (last 30 rows)

| Date | Close |
|---|---:|
| 2026-05-21 | 4.85 |
| 2026-05-22 | 4.81 |
| 2026-05-25 | 4.84 |
| 2026-05-26 | 4.80 |
| 2026-05-27 | 4.87 |
| 2026-05-28 | 4.81 |
| 2026-05-29 | 4.80 |
| 2026-06-01 | 4.71 |
| 2026-06-02 | 4.69 |
| 2026-06-03 | 4.67 |
| 2026-06-04 | 4.72 |
| 2026-06-05 | 4.78 |
| 2026-06-09 | 4.84 |
| 2026-06-10 | 4.84 |
| 2026-06-11 | 4.96 |
| 2026-06-12 | 4.97 |
| 2026-06-15 | 4.84 |
| 2026-06-16 | 4.84 |
| 2026-06-17 | 4.85 |
| 2026-06-18 | 4.90 |
| 2026-06-19 | 4.85 |
| 2026-06-22 | 4.91 |
| 2026-06-23 | 4.90 |
| 2026-06-24 | 4.86 |
| 2026-06-25 | 4.99 |
| 2026-06-26 | 4.97 |
| 2026-06-29 | 4.97 |
| 2026-06-30 | 4.97 |
| 2026-07-01 | 4.92 |
| 2026-07-02 | 4.99 |

Use this snapshot as the source of truth for exact OHLCV, price-level, and indicator-value claims. If another tool output conflicts with it, flag the discrepancy rather than inventing a reconciled number. Do not claim historical validation, support/resistance bounces, or exact percentage moves unless directly supported by tool output with concrete dates and prices.
```

### Tool: get_indicators:close_50_sma

- Status: `ok`

```text
## close_50_sma values from 2026-06-02 to 2026-07-02:

2026-07-02: 4.770200004577637
2026-07-01: 4.764600009918213
2026-06-30: 4.759600009918213
2026-06-29: 4.753400011062622
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 4.747400016784668
2026-06-25: 4.741200017929077
2026-06-24: 4.734400024414063
2026-06-23: 4.728200025558472
2026-06-22: 4.720600023269653
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 4.712800025939941
2026-06-18: 4.7048000240325925
2026-06-17: 4.695200023651123
2026-06-16: 4.687000026702881
2026-06-15: 4.679000024795532
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 4.670400018692017
2026-06-11: 4.658200025558472
2026-06-10: 4.64660002708435
2026-06-09: 4.638000020980835
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 4.629800014495849
2026-06-04: 4.623800010681152
2026-06-03: 4.617400016784668
2026-06-02: 4.61020001411438


50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
```

### Tool: get_indicators:close_200_sma

- Status: `ok`

```text
## close_200_sma values from 2026-06-02 to 2026-07-02:

2026-07-02: 4.63002836227417
2026-07-01: 4.629021208286286
2026-06-30: 4.628265926837921
2026-06-29: 4.627358772754669
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 4.6264025545120235
2026-06-25: 4.625691652297974
2026-06-24: 4.624576559066773
2026-06-23: 4.62425562620163
2026-06-22: 4.62416718006134
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 4.623740410804748
2026-06-18: 4.623325316905976
2026-06-17: 4.6229485464096065
2026-06-16: 4.6226776146888735
2026-06-15: 4.622985279560089
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 4.622908508777618
2026-06-11: 4.622806446552277
2026-06-10: 4.622514111995697
2026-06-09: 4.623062047958374
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 4.623946363925934
2026-06-04: 4.625322897434234
2026-06-03: 4.626855268478393
2026-06-02: 4.62839736700058


200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
```

### Tool: get_indicators:rsi

- Status: `ok`

```text
## rsi values from 2026-06-02 to 2026-07-02:

2026-07-02: 60.91351135533532
2026-07-01: 55.88240429227793
2026-06-30: 61.09861277809121
2026-06-29: 61.09861277809121
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 61.09861277809121
2026-06-25: 62.981395256281914
2026-06-24: 54.52298787104618
2026-06-23: 58.33102254659971
2026-06-22: 59.292335457085166
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 55.17660573317181
2026-06-18: 59.85979871101309
2026-06-17: 56.425528024381485
2026-06-16: 55.72200912264326
2026-06-15: 55.72200912264324
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 68.0348619555362
2026-06-11: 67.52226015585349
2026-06-10: 60.45597158563199
2026-06-09: 60.45597158563199
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 56.362767411077165
2026-06-04: 51.722464176901106
2026-06-03: 47.393791884392805
2026-06-02: 49.02653628803792


RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.
```

### Tool: get_indicators:macd

- Status: `ok`

```text
## macd values from 2026-06-02 to 2026-07-02:

2026-07-02: 0.05844818447782707
2026-07-01: 0.056813950536044544
2026-06-30: 0.06102893067920245
2026-06-29: 0.06043020456427772
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 0.058787027529384694
2026-06-25: 0.05583465207714866
2026-06-24: 0.049217845320835174
2026-06-23: 0.053292824594128874
2026-06-22: 0.05364608821109229
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 0.052298517736398153
2026-06-18: 0.05592690715553861
2026-06-17: 0.054653640671611825
2026-06-16: 0.057324456097179954
2026-06-15: 0.060917734087130526
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 0.0646179873166739
2026-06-11: 0.055164631249028595
2026-06-10: 0.04331447325816118
2026-06-09: 0.03977750397753255
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 0.03468446312876594
2026-06-04: 0.033788474792021184
2026-06-03: 0.03826253276984559
2026-06-02: 0.04850739170901974


MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
```

### Tool: get_indicators:atr

- Status: `ok`

```text
## atr values from 2026-06-02 to 2026-07-02:

2026-07-02: 0.09163905137533022
2026-07-01: 0.09099590881708114
2026-06-30: 0.09261096552136606
2026-06-29: 0.09435025735674984
2026-06-28: N/A: Not a trading day (weekend or holiday)
2026-06-27: N/A: Not a trading day (weekend or holiday)
2026-06-26: 0.09468488080050826
2026-06-25: 0.09504524450917115
2026-06-24: 0.09081794828930495
2026-06-23: 0.09165010402647804
2026-06-22: 0.09254627174343368
2026-06-21: N/A: Not a trading day (weekend or holiday)
2026-06-20: N/A: Not a trading day (weekend or holiday)
2026-06-19: 0.09120366699182056
2026-06-18: 0.09360391678990682
2026-06-17: 0.09580421367986434
2026-06-16: 0.09701992829323432
2026-06-15: 0.09832915941532505
2026-06-14: N/A: Not a trading day (weekend or holiday)
2026-06-13: N/A: Not a trading day (weekend or holiday)
2026-06-12: 0.09358526033864933
2026-06-11: 0.09386103785793846
2026-06-10: 0.09146573307777987
2026-06-09: 0.08927079827152586
2026-06-08: N/A: Not a trading day (weekend or holiday)
2026-06-07: N/A: Not a trading day (weekend or holiday)
2026-06-06: N/A: Not a trading day (weekend or holiday)
2026-06-05: 0.08921473077312536
2026-06-04: 0.08992352540619555
2026-06-03: 0.09145612775865532
2026-06-02: 0.0907989141529697


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
<no Reddit posts found mentioning MPL.AX across r/wallstreetbets, r/stocks, r/investing in the past 7 days>
```

## Role: news

- Skill: `tradingagents-news-analyst`

### Tool: get_news

- Status: `ok`

```text
No news found for MPL.AX between 2026-06-25 and 2026-07-02
```

### Tool: get_global_news

- Status: `ok`

```text
No global news found between 2026-06-25 and 2026-07-02
```

### Tool: get_insider_transactions

- Status: `ok`

```text
# Insider Transactions data for MPL.AX
# Data retrieved on: 2026-07-02 22:07:11

,Shares,Value,URL,Text,Insider,Position,Transaction,Start Date,Ownership
0,25000,78420.0,,Purchase at price 3.14 per share.,Everingham (Peter Dobie),Independent Non-Executive Director,,2026-02-27,D
1,11448,35991.0,,Purchase at price 3.14 per share.,Hey (Jacqueline Cherie),Director (Non-Executive),,2026-02-27,D
2,22370,70682.0,,Purchase at price 3.16 per share.,McIntyre (Lisa Margaret),Director (Non-Executive),,2026-02-23,D
3,535832,,,,Koczkar (David),Chief Executive Officer,,2025-09-04,D
4,5900,19672.0,,Purchase at price 3.33 per share.,Weatherill (Jay Wilson),Independent Non-Executive Director,,2025-09-01,D
5,59129,,,,Milisavljevic (Milosh),Divisional Officer,,2025-06-30,D
6,40000,,,,Rogers (Mark),Chief Financial Officer,,2025-06-30,D
7,457907,,,,Koczkar (David),Chief Executive Officer,,2024-09-02,D
8,32750,87589.0,,Purchase at price 2.67 per share.,Fagg (Kathryn Joy),Independent Non-Executive Director,,2024-08-26,D
9,5100,13484.0,,Purchase at price 2.64 per share.,Weatherill (Jay Wilson),Independent Non-Executive Director,,2024-08-26,D
10,100000,268130.0,,Purchase at price 2.68 per share.,Wilkins (Michael J),Independent Non-Executive Chairman,,2024-08-26,D

```

## Role: fundamentals

- Skill: `tradingagents-fundamentals-analyst`

### Tool: get_fundamentals

- Status: `ok`

```text
# Company Fundamentals for MPL.AX
# Data retrieved on: 2026-07-02 22:07:11

Name: Medibank Private Limited
Sector: Financial Services
Industry: Insurance - Specialty
Market Cap: 13742475264
PE Ratio (TTM): 29.35294
Forward PE: 19.632528
Price to Book: 5.856807
EPS (TTM): 0.17
Forward EPS: 0.25417
Dividend Yield: 3.33
Beta: 0.055
52 Week High: 5.28
52 Week Low: 4.06
50 Day Average: 4.7744
200 Day Average: 4.67475
Revenue (TTM): 8770199552
Gross Profit: 1927200000
EBITDA: 722200000
Net Income: 463400000
Profit Margin: 0.05284
Operating Margin: 0.09843001
Return on Equity: 0.19996001
Return on Assets: 0.10399
Debt to Equity: 11.778
Current Ratio: 2.203
Book Value: 0.852
Free Cash Flow: 692750016
```

### Tool: get_balance_sheet

- Status: `ok`

```text
# Balance Sheet data for MPL.AX (quarterly)
# Data retrieved on: 2026-07-02 22:07:11

,2025-06-30
Ordinary Shares Number,2754003240.0
Share Issued,2754003240.0
Total Debt,209000000.0
Tangible Book Value,1836000000.0
Invested Capital,2370900000.0
Net Tangible Assets,1836000000.0
Capital Lease Obligations,174000000.0
Common Stock Equity,2335900000.0
Total Capitalization,2335900000.0
Total Equity Gross Minority Interest,2336100000.0
Minority Interest,200000.0
Stockholders Equity,2335900000.0
Gains Losses Not Affecting Retained Earnings,27400000.0
Other Equity Adjustments,27400000.0
Retained Earnings,2223500000.0
Capital Stock,85000000.0
Common Stock,85000000.0
Total Liabilities Net Minority Interest,2364200000.0
Employee Benefits,117900000.0
Non Current Pension And Other Postretirement Benefit Plans,117900000.0
Long Term Debt And Capital Lease Obligation,144800000.0
Long Term Capital Lease Obligation,144800000.0
Long Term Provisions,14700000.0
Current Deferred Liabilities,34400000.0
Current Deferred Taxes Liabilities,34400000.0
Current Debt And Capital Lease Obligation,64200000.0
Current Capital Lease Obligation,29200000.0
Current Debt,35000000.0
Other Current Borrowings,35000000.0
Current Provisions,28400000.0
Payables And Accrued Expenses,205900000.0
Payables,205900000.0
Accounts Payable,205900000.0
Total Assets,4700300000.0
Investments And Advances,264300000.0
Long Term Equity Investment,39000000.0
Goodwill And Other Intangible Assets,499900000.0
Other Intangible Assets,157500000.0
Goodwill,342400000.0
Net PPE,194200000.0
Receivables,66400000.0
Accounts Receivable,66400000.0
Cash Cash Equivalents And Short Term Investments,873900000.0
Other Short Term Investments,225300000.0
Cash And Cash Equivalents,648600000.0

```

### Tool: get_cashflow

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'MPL.AX' from any configured vendor (no cash flow data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

### Tool: get_income_statement

- Status: `ok`

```text
NO_DATA_AVAILABLE: No usable market data for 'MPL.AX' from any configured vendor (no income statement data). The symbol may be invalid, delisted, not covered, or the vendor returned stale data. Do not estimate or fabricate values — report that data is unavailable for this symbol.
```

## Role: financial_report

- Skill: `tradingagents-financial-report-analyst`

### Tool: collect_financial_document_sources

- Status: `ok`

```text
## Financial Document Source Packet: MPL.AX

- Trade date: `2026-07-02`
- Collection status: `ok`
- Market: `ASX`
- ASX code: `MPL`
- As-of rule: Only ASX announcements with announcement/lodgement date <= trade_date are included.

| Source | Status | Filing date | Form | URL / reason |
|---|---:|---:|---:|---|
| asx_fallback_document | available | 2025-12-31 | Annual Report | https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf |

### Section: asx_fallback_document / section

- Section name: revenue_income_npat
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: revenue, income, NPAT

```text
income 73 Consolidated statement of financial position 74 Consolidated statement of changes in equity 75 Consolidated statement of cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Shareholder information 120 Financial calendar 121 Corporate directory 121 This report and the Corporate Governance Statement is part of our suite of reporting for the 2025 financial year. You can find more information about our performance in our Full Year Results Investor Presentation and Sustainability Summary. Our cover features Cath and her family playing The Family Roast – a card game we developed to encourage more meaningful conversations as part of our commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our shareholders. Medibank remains a resilient business with a strong capital position and the Board determined shareholders would
```

### Section: asx_fallback_document / section

- Section name: eps_dps
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: EPS, DPS, dividends

```text
Earnings per share (EPS) (cents) 18.2 17.9 1.7% Normalisation for investment returns (10.1) 0.3 n.m. Normalisation for COVID-19 reserve movements 128.0 7 7.6 64.9% Underlying NPAT2 618.7 570.4 8.5% Underlying EPS (cents)2 22.5 20.7 8.5% Dividend per share (cents) 18.0 16.6 8.4% Dividend payout ratio2 80.1% 80.1% - 1. Health Insurance operating profit excludes the impacts of COVID-19. 2. Underlying NPAT is statutory NPAT normalised for growth asset returns to historical long-term expectations, credit spread movements, movement in COVID-19 reserve and one-off items. Dividend payout ratio based on underlying NPAT. Annual Report 2025 25 26 Medibank Operating and financial review Unless otherwise stated, discussion of performance in this section of the report is on a management basis, which is consistent with how performance is assessed internally. This includes reporting the impacts of COVID-19 outside of Group operating profit. Group Medibank’s financial results for the 12 months ended 30 June 2025 demonstrates our disciplined approach to managing the business, highlights the benefit of continuing revenue diversification and includes investment for future growth. Group operating profit was up 8.9% to $762.4 million, with solid growth in resident Health Insurance, an important contribution from non-resident Health Insurance and continued strong momentum in Medibank Health. Profit before tax and COVID-19 impacts increased 10.8% to $911.6 million with a $25.6 million increase in net investment income to $207.8 million and cybercrime costs and other income and expenses broadly in line with last year. The non-recurring cybercrime costs of $39.7 million include further IT security uplift costs of approximately $24 million and legal and other costs related to regulatory investigations and litigation associated with the 2022 cybercrime event. In 2026, we expect these costs to be around $35 million (excludes the impact of any potential findings or outcomes from regulatory investigations or litigation) and the IT security uplift program to be largely embedded. In 2027, costs are expected to be largely related to ongoing regulatory investigations and litigation. Reported net profit after tax (NPAT) attributable to Medibank shareholders increased $8.3 million to $500.8 million. However, this has been significantly impacted by the adoption of AASB 17 Insurance Contracts (AASB 17), which decreased statutory NPAT by $128.0 million and $77.6 million in 2025 and 2024 respectively, due to the timing and value of COVID-19 claims savings and customer give backs. Underlying NPAT, which adjusts statutory NPAT for movement in the COVID-19 equity reserve and the normalisation of investment returns, increased 8.5% to $618.7 million. Reported earnings per share (EPS) was 1.7% higher at 18.2 cents per share, while underlying EPS was up 8.5% to 22.5 cents per share. The key reasons for the movements in the Health Insurance and Medibank Health results, as well as net investment income, are outlined in this report. Health Insurance financial performance Year ended 30 June ($m) 2025 2024 Change Premium revenue 8,211.0 7,903.0 3.9% Net claims expense (including risk equalisation) (6,814.6) (6,595.8) 3.3% Gross profit 1,396.4 1,307. 2 6.8% Management expenses (654.9) (614.9) 6.5% Operating profit1 741.5 692.3 7.1% Gross margin 17.0% 16.5% 50bps Management expense ratio 8.0% 7.8% 20bps Operating margin 9.0% 8.8% 20bps 1. Health Insurance operating profit excludes the impacts of COVID-19. Our Health Insurance business has remained resilient despite a challenging economic environment, with continued benefits arising from our disciplined approach to growth and claims management during COVID-19. Gross margin of 17.0% was 50 basis points higher with a significantly improved risk equalisation outcome compared to 2024, as well as a 20 basis point benefit from the strong growth in higher margin non-resident policies. We have continued to balance disciplined cost management as we invest in growth resulting in our management expense ratio increasing 20 basis points to 8.0%, with a 20 basis point increase in operating margin to 9.0% and operating profit up 7.1% to $741.5 million. Industry and customer growth The resident health insurance market has remained buoyant with policyholder growth1 in the 12 months to 30 June 2025 expected to be only modestly lower than the 2.3% growth in the 12 months to 31 March 2025, with ongoing strong growth in the 25 to 30-year-old cohort. However, cost-of-living pressures continue to impact the industry with switching rates increasing and a higher share of industry joins through aggregator platforms. Our reported resident policyholders increased by 27,900 or 1.4% which is double the growth rate of the prior 12-month period. The Medibank and ahm brands grew 0.3% and 4.3% respectively, with momentum improving in the second half of 2025. 1. Industry average, resident policyholders, APRA quarterly private health insurance statistics to Mar 25 with estimate for Jun 25 quarter. Annual Report 2025 27 The resident acquisition rate increased 50 basis points to 11.5%, with the Medibank brand improving 40 basis points to 9.3% and the ahm brand up 50 basis points to 18.6%. The improvement in the Medibank brand includes the benefit from investing in our differentiation strategy and additional marketing spend during the second half of 2025. The ahm brand proposition continues to resonate with consumers with the percentage of sales through direct channels remaining stable despite the increasing role of aggregators in the industry. Retention improved by 20 basis points to 10.1% with a 30 basis point improvement across both brands despite higher industry switching rates. This was supported by additional investment in product benefits and Live Better rewards program in the Medibank brand and ahm’s enhanced customer experience. Our key areas of focus for policyholder growth in 2026 include further improving retention,
```

### Section: asx_fallback_document / section

- Section name: management_discussion_analysis
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: management discussion, MD&A, outlook

```text
Operating and financial review 25 Directors 34 Executive leadership team 37 Corporate governance 39 Risk management 41 Directors’ report 47 Remuneration report 50 Financial report 72 Consolidated statement of comprehensive income 73 Consolidated statement of financial position 74 Consolidated statement of changes in equity 75 Consolidated statement of cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Shareholder information 120 Financial calendar 121 Corporate directory 121 This report and the Corporate Governance Statement is part of our suite of reporting for the 2025 financial year. You can find more information about our performance in our Full Year Results Investor Presentation and Sustainability Summary. Our cover features Cath and her family playing The Family Roast – a card game we developed to encourage more meaningful conversations as part of our commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and
```

### Section: asx_fallback_document / section

- Section name: cash_flow_statement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: cash flow statement, operating cash flow

```text
Consolidated statement of cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Shareholder information 120 Financial calendar 121 Corporate directory 121 This report and the Corporate Governance Statement is part of our suite of reporting for the 2025 financial year. You can find more information about our performance in our Full Year Results Investor Presentation and Sustainability Summary. Our cover features Cath and her family playing The Family Roast – a card game we developed to encourage more meaningful conversations as part of our commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our shareholders. Medibank remains a resilient business with a strong capital position and the Board determined shareholders would receive a fully franked final ordinary dividend of 10.2 cents per share, bringing the total FY25 fully
```

### Section: asx_fallback_document / section

- Section name: operating_cash_flow
- Status: `unavailable`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: operating cash flow
- Unavailable reason: operating_cash_flow was not identified in extracted ASX document text.

### Section: asx_fallback_document / section

- Section name: free_cash_flow_or_cash_movement
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: free cash flow, cash movement

```text
net cash flow from operating activities 15. Income tax 16. Group structure 17. Related party transactions 18. Share-based payments 19. Auditor’s remuneration 20. Other Other Consolidated entity disclosure statement 110 Signed reports Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Annual Report 2025 73 Consolidated statement of comprehensive income For the financial year ended 30 June 2025 Note 2025 $m 2024 $m Insurance revenue 2(b) 4(a) 8,011.7 7,623.1 Insurance service expenses Incurred claims 4(a) (6,654.7) (6, 289.3) Other insurance service expenses 3 (656.6) (619.5) (7,311.3) (6,908.8) Insurance service result 700.4 714.3 Other operating revenue 2(b) 334.7 222.8 Other expenses 3 (503.1) (400.5) Share of net profit/(loss) from equity accounted investments 16(c) (11.0) (7.1) Profit before net investment income and income tax 521.0 529.5 Net investment income 6(a) 207.8 182.2 Profit for the year before income tax 728.8 711.7 Income tax expense 15(a) (219.5) (215.3) Profit for the year 509.3 496.4 Total comprehensive income for the year, net of tax 509.3 496.4 Profit and total comprehensive income for the year attributable to: Equity holders of the parent entity 500.8 492.5 Non-controlling interests 8.5 3.9 509.3 496.4 Note cents cents Earnings per share attributable to ordinary equity holders of the parent entity – basic and diluted 5(b) 18.2 17.9 The above statement should be read in conjunction with the accompanying notes. 74 Medibank Consolidated statement of financial position As at 30 June 2025 Note 2025 $m 2024 $m Current assets Cash and cash equivalents 6 648.6 691.0 Trade and other receivables 66.4 39.5 Financial assets at fair value 6(b) 3,062.5 3,048.2 Other assets 34.1 27.6 Total current assets 3,811.6 3,806.3 Non-current assets Property, plant and equipment 9 194.2 205.0 Intangible assets 10 499.9 467.0 Deferred tax assets 15(c) 146.5 142.1 Equity accounted investments 16(c) 39.0 58.7 Other assets 9.1 6.3 Total non-current assets 888.7 879.1 Total assets 4,700.3 4,685.4 Current liabilities Trade and other payables 170.5 145.4 Lease liabilities 13(a) 29. 2 31.7 Borrowings 7(c) 35.0 34.9 Insurance contract liabilities 4(a) 1,606.1 1,636.1 Tax liability 34.4 48.7 Provisions and employee entitlements 11 128.6 118.0 Total current liabilities 2,003.8 2,014.8 Non-current liabilities Trade and other payables 35.4 18.4 Lease liabilities 13(a) 144.8 151.7 Insurance contract liabilities 4(a) 147.8 165.8 Provisions and employee entitlements 11 32.4 29.6 Total non-current liabilities 360.4 365.5 Total liabilities 2,364.2 2,380.3 Net assets 2,336.1 2,305.1 Equity Contributed equity 8(a) 85.0 85.0 Reserves 8(b) 27.4 152.3 Retained earnings 2,223.5 2,068.4 Total equity (attributable to equity holders of the parent entity) 2,335.9 2,305.7 Non-controlling interests 0.2 (0.6) Total equity 2,336.1 2,305.1 The above statement should be read in conjunction with the accompanying notes. Annual Report 2025 75 Consolidated statement of changes in equity For the financial year ended 30 June 2025 Total equity (attributable to equity holders of the parent entity) Non- controlling interests $m Total equity $mNote Contributed equity $m Reserves $m Retained earnings $m Total $m Balance at 1 July 2023 85.0 233.5 1,925.2 2,243.7 - 2,243.7 Profit for the year - - 492.5 492.5 3.9 496.4 Other comprehensive income - - - - - - Total comprehensive income for the year - - 492.5 492.5 3.9 496.4 Dividends paid 5(a)(i) - - (426.9) (426.9) (2.9) (429.8) Movement in COVID-19 reserve, net of tax 8(b)(i) - (7 7.6) 7 7.6 - - - Non-controlling interest from acquisition of subsidiary - - - - (1.3) (1.3) Other movements in non-controlling interests - - - - (0.3) (0.3) Acquisition and settlement of share-based payment, net of tax - (6.9) - (6.9) - (6.9) Share-based payment transactions - 3.3 - 3.3 - 3.3 Balance at 30 June 2024 85.0 152.3 2,068.4 2,305.7 (0.6) 2,305.1 Profit for the year - - 500.8 500.8 8.5 509.3 Other comprehensive income - - - - - - Total comprehensive income for the year - - 500.8 500.8 8.5 509.3 Dividends paid 5(a)(i) - - (473.7) (473.7) (6.9) (480.6) Movement in COVID-19 reserve, net of tax 8(b)(i) - (128.0) 128.0 - - - Other movements in non-controlling interests - - - - (0.8) (0.8) Acquisition and settlement of share-based payment, net of tax - (5.4) - (5.4) - (5.4) Share-based payment transactions - 8.5 - 8.5 - 8.5 Balance at 30 June 2025 85.0 27.4 2,223.5 2,335.9 0.2 2,336.1 The above statement should be read in conjunction with the accompanying notes. 76 Medibank Consolidated statement of cash flows For the financial year ended 30 June 2025 Note 2025 $m 2024 $m Cash flows from operating activities Premium receipts 8,004.4 7,910.3 Medibank Health receipts 357.5 246.5 Payments for claims and levies (6,660.6) (6,271.0) Payments to suppliers and employees (1,079.6) (885.1) Income taxes paid (240.8) (132.2) Net cash inflow from operating activities 14 380.9 868.5 Cash flows from investing activities Interest received 133.2 119.9 Trust distributions received 12.3 11.6 Investment management expenses (5.7) (4.8) Net sales/(purchases) of financial assets 50.4 (127.2) Purchase of equity accounted investments 16(c) (7.0) (15.5) Payments for the purchase of businesses, net of cash acquired 16(b) 1.6 (37. 2) Loans to equity accounted investments 17(a) (4.5) - Purchase of plant and equipment (11.2) (7.0) Purchase of intangible assets (58.6) (50.6) Net cash inflow/(outflow) from investing activities 110.5 (110.8) Cash flows from financing activities Purchase of shares to settle share-based payment (6.4) (7.5) Lease principal and interest payments 13 (46.8) (48.7) Borrowings repayments 7(c) - (1.3) Dividends paid to non-controlling interests (6.9) (2.9) Dividends paid to equity holders of the parent entity 5(a)(i) (473.7) (426.9) Net cash outflow from financing activities (533.8) (487.3) Net increase/(decrease) in cash and cash equivalents (42.4) 270.4 Cash and
```

### Section: asx_fallback_document / section

- Section name: cash_debt_gearing
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: cash, debt, gearing, capital

```text
cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Shareholder information 120 Financial calendar 121 Corporate directory 121 This report and the Corporate Governance Statement is part of our suite of reporting for the 2025 financial year. You can find more information about our performance in our Full Year Results Investor Presentation and Sustainability Summary. Our cover features Cath and her family playing The Family Roast – a card game we developed to encourage more meaningful conversations as part of our commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our shareholders. Medibank remains a resilient business with a strong capital position and the Board determined shareholders would receive a fully franked final ordinary dividend of 10.2 cents per share, bringing the total FY25 fully franked ordinary dividend to
```

### Section: asx_fallback_document / section

- Section name: segment_product_performance
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: segment performance, sector metrics

```text
segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our shareholders. Medibank remains a resilient business with a strong capital position and the Board determined shareholders would receive a fully franked final ordinary dividend of 10.2 cents per share, bringing the total FY25 fully franked ordinary dividend to 18.0 cents per share, up 8.4% on FY24. The Board continued to play an active role in the oversight of the Medibank Group. Throughout the year we maintained our focus on performance, working alongside the executive team on the company’s strategy and its 2030 vision. A feature of our strategy is our growing focus on wellbeing and on primary care, which also centres on system change as we look to support GPs, nurses and allied health professionals within multidisciplinary teams to deliver proactive and coordinated care in the community, and also to champion a focus on prevention. We are proud of Medibank’s growing role in driving change across the health system – not only for the benefit of our customers and patients, but also for the wider community. The Board has seen personalised care models in action, with on-site tours of the Amplar Health Home Hospital service in Adelaide and Adeney Private Hospital in Melbourne. As well, directors continued to participate in regular customer connection sessions and visits to retail stores. At the same time, we have deepened our relationships with industry stakeholders and community partners. This includes providing targeted funding and collaborative support to help our hospital partners innovate and drive lasting change across the health system. During the year the Board supervised key risk and regulatory initiatives designed to enhance Medibank’s resilience. This included adopting the Australian Prudential Regulation Authority’s new operational risk management standard, implementing the Financial Accountability Regime and overseeing an update to our risk culture framework. Board succession planning and capability development are essential for leadership continuity, strong governance and the ability to take on future opportunities and challenges. To support this focus, the Board participated in a wide- ranging program of professional development and business immersion activities throughout the year. 4 Medibank We remain committed to advancing diversity and inclusion across the business. We aim to maintain at least 40% female representation in the Group and senior executive population and on our Board. While we narrowly missed our objective for the Board in FY25, we exceeded the target across the Group and senior executive team. At our Annual General Meeting in November, we will farewell long standing directors, Linda Nicholls AO and David Fagan, who will retire at the conclusion of that meeting. The Board is recommending shareholders vote for the election of Jacqueline Hey and Dr Lisa McIntyre, two highly credentialed and experienced directors who bring a wealth of experience across the financial services, technology and health sectors. We continue to address our environmental, social and governance commitments, including preparing for new sustainability reporting requirements next year. In FY25 we achieved the target for net zero emissions for our Scope 1 and 2 operations that we set in FY21. Given the changes in our business since this target was set, we have now developed an updated baseline for greenhouse gas emissions and are reassessing our targets and pathway to account for this. The 2025 financial year was another successful year for Medibank. I extend my sincere thanks to my fellow directors for their contribution during the year, and on behalf of the Board, acknowledge the leadership of David Koczkar and the executive team. Most importantly, I thank the entire Medibank team for their steadfast commitment to our shared purpose of Better Health for Better Lives. “ We are proud of Medibank’s growing role in driving change across the health system – not only for the benefit of our customers and patients, but also for the wider community.” “ The Board continued to play an active role in the oversight of the Medibank Group.” Annual Report 2025 5 CEO's message David Koczkar We are delivering where it counts most for our customers – improving value, supporting more of their health needs and driving the health transition our country needs. Over the past few years, we have invested in our people, our products and services and continued to strengthen our foundations. And we are seeing the results of this, in the growth of our business and the progress we have made towards our vision to deliver the best health and wellbeing for Australia. We have made substantial changes to the way we work to make a greater impact for our customers and patients. Through our work. Reinvented program we have focused on empowering our people
```

### Section: asx_fallback_document / section

- Section name: management_commentary_outlook
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: outlook, management commentary

```text
outlook Resident health insurance Industry growth: anticipate moderating industry growth relative to FY25 Policyholder growth: aim to grow market share in a disciplined way, including further volume growth in the Medibank brand Claims: expect claims per policy unit growth of 2.6%-2.9% Non-resident health insurance Gross profit: aim to maintain solid gross profit growth Medibank Health Medibank Health: expect low double- digit organic operating profit growth M&A: based on the strong asset pipeline, we aim to invest towards the top end of the $150m-$250m FY24-FY26 M&A target where this creates long-term value Annual Report 2025 7 Our stakeholders Customers Employees Shareholders Health providers and patients Community 8 Medibank Delivering value to stakeholders through our strategy The material issues they care most about Affordable, innovative and personalised health and wellbeing programs and services Meet our 2030 vision of the healthiest workplace through our work. Reinvented program Support healthy communities Work together to build a stronger and more sustainable health system Responsible decision making centred on customers and patients Environmental health and climate change Responsible use and protection of customer data Our strategy – growing as a health company Deliver leading experiences Create personalised and connected customer experiences Empower our people and reinvent work Collaborate with our communities and partners to make a difference Continue to strengthen trust and reputation Differentiate our insurance business Deliver more value, choice, and control for customers Provide holistic health solutions to customers including resident, non-resident and corporate customers Strengthen our dual brands and provider networks Lead change with partners to deliver affordable healthcare Expand in health Accelerate growth in prevention, primary and virtual care and personalised care models Scale and connect our existing health businesses Deliver more health services to Medibank and ahm customers Accelerate Australia’s health transition Continue to strengthen our foundations Embed a purpose-led risk culture and approach to risk management focused on customer centricity and health Support business growth by continuing to modernise our technology platforms, leveraging cloud, AI and automation to deliver scalability, efficiency and agility How we’re delivering value Better Health for Better Lives Deepening relationships with customers • Deliver exceptional customer experience • Personalised service via community hubs • Technology and AI enablement • Strong risk management and governance Delivering more value, choice and control • Differentiated products and services • Empower customers to manage their health • Greater options for when and where customers receive care Supporting whole of health needs • Proactive and personalised • Platform connecting consumer needs with health services • Tailored across the customer lifecycle Driving change in the health system • Focus on better ways of providing care • Investments catalyse change • Partnerships foster innovation and drive wide uptake • Advocate for reform to sustain the system Annual Report 2025 9 Deliver leading experiences Deliver leading experiences We’re enabling our people to do more of what matters for our customers and help make a difference to our community Our strategy > Create personalised and connected customer experiences > Empower our people and reinvent work > Collaborate with our communities to make a difference > Continue to strengthen trust and reputation 4.2m total health insurance customers as at 30 June 2025 46% service enquiries resolved through messaging 10k+ people received help through our Live Better vans 111 regional towns visited 10 Medibank Need to know • Customer advocacy is at a 3-year high as we established more autonomous teams • Experimented with new ways of working including expanding our 4-day work week trial to 500 employees after participants were shown to be happier, healthier and more efficient • Supported community-led initiatives including parkrun Australia and 36 Months 20% increase in unique users of My Medibank app Transforming customer support with a local touch We want every customer and patient to have a brilliant experience when they contact us. So, we’re transforming how we work to deliver more personalised experiences, backed by local knowledge, simple processes and intelligent tools. Customer advocacy increased significantly across both Medibank and ahm this year and the Group is now at a 3-year high. Following a successful pilot, this year we reorganised our customer support teams across Medibank and our Amplar Home Health teams into geographically located hubs so that customers are supported by team members who live and work locally. ahm also simplified its customer service approach so team members could better resolve queries themselves and take ownership of any follow-up required. Not only do customers love these new approaches, but our employee engagement score was one of the highest we've seen, and our attrition rate has halved. This customer-first approach has transformed how teams work and how customer support is delivered. To further embed a customer-first mindset throughout our business, we trained more than 65 senior leaders across Medibank and ahm to support customers directly in our messaging and phone channels. This creates a strong connection with both the customer support teams and the customer experience, enabling our leaders to identify and champion areas for continuous improvement. With more customers using our digital channels, we improved functionality and removed friction points making it easier for customers to self-serve with confidence. This included adding new search functionality to our My Medibank app and website, a new hospital eligibility check feature and reinventing our retail product comparison experience. Additionally, ahm introduced its first digital
```

### Section: asx_fallback_document / section

- Section name: dividends_capital_management
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: dividends, capital management

```text
dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our shareholders. Medibank remains a resilient business with a strong capital position and the Board determined shareholders would receive a fully franked final ordinary dividend of 10.2 cents per share, bringing the total FY25 fully franked ordinary dividend to 18.0 cents per share, up 8.4% on FY24. The Board continued to play an active role in the oversight of the Medibank Group. Throughout the year we maintained our focus on performance, working alongside the executive team on the company’s strategy and its 2030 vision. A feature of our strategy is our growing focus on wellbeing and on primary care, which also centres on system change as we look to support GPs, nurses and allied health professionals within multidisciplinary teams to deliver proactive and coordinated care in the community, and also to champion a focus on prevention. We are proud of Medibank’s growing role in driving change across the health system – not only for the benefit of our customers and patients, but also for the wider community. The Board has seen personalised care models in action, with on-site tours of the Amplar Health Home Hospital service in Adelaide and Adeney Private Hospital in Melbourne. As well, directors continued to participate in regular customer connection sessions and visits to retail stores. At the same time, we have deepened our relationships with industry stakeholders and community partners. This includes providing targeted funding and collaborative support to help our hospital partners innovate and drive lasting change across the health system. During the year the Board supervised key risk and regulatory initiatives designed to enhance Medibank’s resilience. This included adopting the Australian Prudential Regulation Authority’s new operational risk management standard, implementing the Financial Accountability Regime and overseeing an update to our risk culture framework. Board succession planning and capability development are essential for leadership continuity, strong governance and the ability to take on future opportunities and challenges. To support this focus, the Board participated in a wide- ranging program of professional development and business immersion activities throughout the year. 4 Medibank We remain committed to advancing diversity and inclusion across the business. We aim to maintain at least 40% female representation in the Group and senior executive population and on our Board. While we narrowly missed our objective for the Board in FY25, we exceeded the target across the Group and senior executive team. At our Annual General Meeting in November, we will farewell long standing directors, Linda Nicholls AO and David Fagan, who will retire at the conclusion of that meeting. The Board is recommending shareholders vote for the election of Jacqueline Hey and Dr Lisa McIntyre, two highly credentialed and experienced directors who bring a wealth of experience across the financial services, technology and health sectors. We continue to address our environmental, social and governance commitments, including preparing for new sustainability reporting requirements next year. In FY25 we achieved the target for net zero emissions for our Scope 1 and 2 operations that we set in FY21. Given the changes in our business since this target was set, we have now developed an updated baseline for greenhouse gas emissions and are reassessing our targets and pathway to account for this. The 2025 financial year was another successful year for Medibank. I extend my sincere thanks to my fellow directors for their contribution during the year, and on behalf of the Board, acknowledge the leadership of David Koczkar and the executive team. Most importantly, I thank the entire Medibank team for their steadfast commitment to our shared purpose of Better Health for Better Lives. “ We are proud of Medibank’s growing role in driving change across the health system – not only for the benefit of our customers and patients, but also for the wider community.” “ The Board continued to play an active role in the oversight of the Medibank Group.” Annual Report 2025 5 CEO's message David Koczkar We are delivering where it counts most for our customers – improving value, supporting more of their health needs and driving the health transition our country needs. Over the past few years, we have invested in our people, our products and services and continued to strengthen our foundations. And we are seeing the results of this, in the growth of our business and the progress we have made towards our vision to deliver the best health and wellbeing for Australia. We have made substantial changes to the way we work to make a greater impact for our customers
```

### Section: asx_fallback_document / section

- Section name: capex_commitments
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: capex, commitments

```text
commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our shareholders. Medibank remains a resilient business with a strong capital position and the Board determined shareholders would receive a fully franked final ordinary dividend of 10.2 cents per share, bringing the total FY25 fully franked ordinary dividend to 18.0 cents per share, up 8.4% on FY24. The Board continued to play an active role in the oversight of the Medibank Group. Throughout the year we maintained our focus on performance, working alongside the executive team on the company’s strategy and its 2030 vision. A feature of our strategy is our growing focus on wellbeing and on primary care, which also centres on system change as we look to support GPs, nurses and allied health professionals within multidisciplinary teams to deliver proactive and coordinated care in the community, and also to champion a focus on prevention. We are proud of Medibank’s growing role in driving change across the health system – not
```

### Section: asx_fallback_document / section

- Section name: material_risks
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: risks

```text
Risk management 41 Directors’ report 47 Remuneration report 50 Financial report 72 Consolidated statement of comprehensive income 73 Consolidated statement of financial position 74 Consolidated statement of changes in equity 75 Consolidated statement of cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Shareholder information 120 Financial calendar 121 Corporate directory 121 This report and the Corporate Governance Statement is part of our suite of reporting for the 2025 financial year. You can find more information about our performance in our Full Year Results Investor Presentation and Sustainability Summary. Our cover features Cath and her family playing The Family Roast – a card game we developed to encourage more meaningful conversations as part of our commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both the resident and non- resident health insurance businesses with Medibank's Health Insurance operating profit up 7.1% to $741.5 million. In Medibank Health, segment profit was up 27% to $76.7 million. The increasing contribution of this business, now at around 10% of earnings, is delivering benefits for both our customers and the community, as well as further diversifying our business for the long-term benefit of our
```

### Section: asx_fallback_document / section

- Section name: one_off_items
- Status: `available`
- Source type: `asx_fallback_document`
- Filing date: `2025-12-31`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf
- Supports claims: one-off items

```text
one-off support in recent years. We are a leading health company and we take our role seriously to support the needs of our customers and the community, now and into the future. Our focus is clear – making healthcare more accessible, more affordable and more personalised. And it is what continues to inspire us for the work that lies ahead. I’d like to thank Mike Wilkins and the Board for their support this year and express my gratitude to our amazing team. Their dedication to our purpose and determination to shape the future of health enables us to keep building a stronger, more sustainable health system for Australia. Together, we’re not just adapting to change – we’re driving it. And that’s something we can all be proud of. “ We have invested in our people, our products and services and continued to strengthen our foundations. And we are seeing the results of this” FY26 outlook Resident health insurance Industry growth: anticipate moderating industry growth relative to FY25 Policyholder growth: aim to grow market share in a disciplined way, including further volume growth in the Medibank brand Claims: expect claims per policy unit growth of 2.6%-2.9% Non-resident health insurance Gross profit: aim to maintain solid gross profit growth Medibank Health Medibank Health: expect low double- digit organic operating profit growth M&A: based on the strong asset pipeline, we aim to invest towards the top end of the $150m-$250m FY24-FY26 M&A target where this creates long-term value Annual Report 2025 7 Our stakeholders Customers Employees Shareholders Health providers and patients Community 8 Medibank Delivering value to stakeholders through our strategy The material issues they care most about Affordable, innovative and personalised health and wellbeing programs and services Meet our 2030 vision of the healthiest workplace through our work. Reinvented program Support healthy communities Work together to build a stronger and more sustainable health system Responsible decision making centred on customers and patients Environmental health and climate change Responsible use and protection of customer data Our strategy – growing as a health company Deliver leading experiences Create personalised and connected customer experiences Empower our people and reinvent work Collaborate with our communities and partners to make a difference Continue to strengthen trust and reputation Differentiate our insurance business Deliver more value, choice, and control for customers Provide holistic health solutions to customers including resident, non-resident and corporate customers Strengthen our dual brands and provider networks Lead change with partners to deliver affordable healthcare Expand in health Accelerate growth in prevention, primary and virtual care and personalised care models Scale and connect our existing health businesses Deliver more health services to Medibank and ahm customers Accelerate Australia’s health transition Continue to strengthen our foundations Embed a purpose-led risk culture and approach to risk management focused on customer centricity and health Support business growth by continuing to modernise our technology platforms, leveraging cloud, AI and automation to deliver scalability, efficiency and agility How we’re delivering value Better Health for Better Lives Deepening relationships with customers • Deliver exceptional customer experience • Personalised service via community hubs • Technology and AI enablement • Strong risk management and governance Delivering more value, choice and control • Differentiated products and services • Empower customers to manage their health • Greater options for when and where customers receive care Supporting whole of health needs • Proactive and personalised • Platform connecting consumer needs with health services • Tailored across the customer lifecycle Driving change in the health system • Focus on better ways of providing care • Investments catalyse change • Partnerships foster innovation and drive wide uptake • Advocate for reform to sustain the system Annual Report 2025 9 Deliver leading experiences Deliver leading experiences We’re enabling our people to do more of what matters for our customers and help make a difference to our community Our strategy > Create personalised and connected customer experiences > Empower our people and reinvent work > Collaborate with our communities to make a difference > Continue to strengthen trust and reputation 4.2m total health insurance customers as at 30 June 2025 46% service enquiries resolved through messaging 10k+ people received help through our Live Better vans 111 regional towns visited 10 Medibank Need to know • Customer advocacy is at a 3-year high as we established more autonomous teams • Experimented with new ways of working including expanding our 4-day work week trial to 500 employees after participants were shown to be happier, healthier and more efficient • Supported community-led initiatives including parkrun Australia and 36 Months 20% increase in unique users of My Medibank app Transforming customer support with a local touch We want every customer and patient to have a brilliant experience when they contact us. So, we’re transforming how we work to deliver more personalised experiences, backed by local knowledge, simple processes and intelligent tools. Customer advocacy increased significantly across both Medibank and ahm this year and the Group is now at a 3-year high. Following a successful pilot, this year we reorganised our customer support teams across Medibank and our Amplar Home Health teams into geographically located hubs so that customers are supported by team members who live and work locally. ahm also simplified its customer service approach so team members could better resolve queries themselves and take ownership of any follow-up required. Not only do customers love these new approaches, but our employee engagement score was one of the highest we've seen, and our
```

### Excerpt: asx_fallback_document

- Filing date: `N/A`
- URL: https://www.medibank.com.au/content/dam/retail/about-assets/pdfs/investor-centre/annual-reports/Medibank_AnnualReport2025.pdf

```text
Annual Report 2025 Contents Medibank Group – our story 1 2025 highlights 2 Chair’s message 4 CEO’s message 6 Delivering value to stakeholders through our strategy 8 Deliver leading experiences 10 Differentiate our insurance business 14 Expand in health 18 Continue to strengthen our foundations 22 Sustainability at Medibank 24 Operating and financial review 25 Directors 34 Executive leadership team 37 Corporate governance 39 Risk management 41 Directors’ report 47 Remuneration report 50 Financial report 72 Consolidated statement of comprehensive income 73 Consolidated statement of financial position 74 Consolidated statement of changes in equity 75 Consolidated statement of cash flows 76 Notes to the consolidated financial statements 77 Consolidated entity disclosure statement 110 Directors’ declaration 112 Auditor’s independence declaration 113 Independent auditor’s report 114 Shareholder information 120 Financial calendar 121 Corporate directory 121 This report and the Corporate Governance Statement is part of our suite of reporting for the 2025 financial year. You can find more information about our performance in our Full Year Results Investor Presentation and Sustainability Summary. Our cover features Cath and her family playing The Family Roast – a card game we developed to encourage more meaningful conversations as part of our commitment to improve mental health in Australia. Annual Report 2025 Corporate Governance Statement 2025 Sustainability Summary 2025 Full year results 2025 Unless otherwise stated, references to a year are to the financial year ending 30 June in that year. References to COVID are to COVID-19. References to Net Zero and Net Zero pathway are based on business-as-usual operations of Medibank Private Limited and its wholly owned subsidiaries in 2021, and do not include Myhealth or any future partnership and investment activity or its investment portfolio. Employee data referenced in pages 2 to 24 only relates to employees of Medibank Private Limited or its wholly owned subsidiaries. Medibank Group – our story As one of Australia’s leading health companies, we want people to experience their best health and wellbeing, so they can live better lives. We support more than 4.2 million customers with health cover through our Medibank and ahm brands, and our Amplar Health network delivers care to millions of people across the country through prevention programs and primary care, virtual health, home and community-based care. Our focus is on giving people greater choice, easier access, and better value from the health system. That’s why we’re working closely with health providers and governments to reimagine how care is delivered and investing to develop more personalised models of care. We’re accelerating the health transition in Australia, so that all of us can continue to access the care we need. Purpose Better Health for Better Lives Vision The best health and wellbeing for Australia Values Customer obsessed Show heart Brilliance together Break boundaries Our businesses Supports the health and wellbeing of customers with a range of personalised health programs, services and products in addition to health cover Offers straightforward health cover and multi-category insurance options, focused on cutting out the complexity and making things simple and affordable Other insurance – Travel, pet, life, home and car insurance that deliver more value for our customers and support their quality of life Delivers innovative healthcare at scale across Australia through virtual health, primary care, hospital and homecare Incorporates: Amplar Health Home Hospital Pinnacle Health Group Medinet Australia Our health investments Primary care Myhealth Medical Group Short stay hospitals and no gap hospitals Adeney Private Hospital (Vic) The Orthopaedic Institute at Macquarie University Hospital (NSW) East Sydney Private Hospital (NSW) Integrated Mental Health (iMH) hospitals – Sydney, Canberra, Brisbane Western Hospital (SA) Sustainability focus areas Customer health Employee health Sustainable health system Environmental health Ethical and responsible business and leadership in health Annual Report 2025 1 2025 highlights Customer 4.2m total health insurance customers $1.71b total COVID financial support since 2020 $6.6b total claims paid Medibank journey NPS 12.9 (+2.3) average ahm service NPS 48.0 (+2.0) average customer advocacy +27.9k (+1.4%) net resident policyholder growth +10.5k (+3.1%) net non-resident policy unit growth Healthcare 52% of Medibank policyholders engaged with health and wellbeing services 931k (+13%) Live Better rewards participants $50m investment in mental health over next 5 years 177k hospital bed days saved through homecare programs delivered by Amplar Health 4.3m health interactions delivered by Amplar Health network 2 Medibank People & community 8.1 ⁄ 10 employee engagement $2.8m community investment Place to work +38 Products and services +39 employee advocacy (eNPS) 3,956 employees including 964 health professionals Financial $618.7m (+8.5%) Group underlying net profit after tax 10.2 cps final ordinary dividend fully franked 26.5% resident policyholder market share $76.7m (+27.0%) Medibank Health segment profit $741.5m (+7.1%) Health Insurance operating profit c. $10m in productivity savings $207.8m (+14.1%) net investment income All data is presented on a statutory basis as at 30 June 2025. Some figures are subject to rounding. Annual Report 2025 3 Chair’s message Mike Wilkins AO Medibank’s commitment to our customers has been demonstrated in the strength of our performance this year. Importantly, Medibank’s leadership in further driving Australia’s health transition is supporting system change while positioning the company for sustainable long-term growth. The Australian health insurance market remained buoyant with customer numbers at record levels despite the ongoing impact of cost-of-living pressures on many households. We saw continued growth in both
```

```
