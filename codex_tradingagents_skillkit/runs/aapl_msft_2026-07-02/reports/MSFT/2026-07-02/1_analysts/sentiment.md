# Sentiment Analyst Report - MSFT

## Tool Outputs Used
- social_summary.json source-level records: social:MSFT:2026-07-02:001, social:MSFT:2026-07-02:002.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| 44 | 34 | 8 | 5 | 21 | low |

The usable sentiment signal is mixed retail-only reaction. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
| social:MSFT:2026-07-02:001 | fetch_stocktwits_messages | ticker_specific_retail_platform | 31 | 29 | 8/5/16 | medium | none disclosed |
| social:MSFT:2026-07-02:002 | fetch_reddit_posts | broad_social_discussion | 13 | 5 | 0/0/5 | low | none disclosed |

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
| social:MSFT:2026-07-02:item:0034 | fetch_reddit_posts | neutral | high | direct_company | reaction:MSFT:2026-07-02:earnings | body excerpt: MSFT earnings less than a month out. Prediction that it will run up to 462 just before earnings. Microsoft will post record earnings for another q |
| social:MSFT:2026-07-02:item:0004 | fetch_stocktwits_messages | neutral | medium | direct_company | reaction:MSFT:2026-07-02:none | [2026-07-02T13:45:23Z · @machumble · no-label] $SNDK because now funds go to $MSFT $META so $SPY goes up with them and doesnt need $SOXX anymore |
| social:MSFT:2026-07-02:item:0006 | fetch_stocktwits_messages | bullish | medium | direct_company | reaction:MSFT:2026-07-02:valuation | [2026-07-02T13:44:55Z · @duyonthego · Bullish] $META sells the news but imagine a direct competitor to $AMZN AWS, $GOOGL Cloud, $MSFT Azure |

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
| social:MSFT:2026-07-02:item:0002 | fetch_stocktwits_messages | bullish | low | [2026-07-02T13:51:36Z · @CRNA24 · Bullish] $MSFT feels like buying &lt;$400 is one of those opportunities you just have to take. Everyone knows this will be bac |
| social:MSFT:2026-07-02:item:0003 | fetch_stocktwits_messages | neutral | low | [2026-07-02T13:48:27Z · @AIWealthCircle · no-label] Microsoft $MSFT just dropped something that feels bigger than a product update.    Microsoft Frontier Compan |
| social:MSFT:2026-07-02:item:0005 | fetch_stocktwits_messages | neutral | low | [2026-07-02T13:45:05Z · @SeNSF · no-label] $MSFT Bulls in Control Above 388 Breakout. Bears in Control Below 381 Breakdown. Play the Break/Retest or Reversal/Re |

## Excluded / Downgraded Evidence
- Low-information, meme, spam-like, cross-ticker, and post-trade-date items are excluded or downgraded by the evidence cards.
- Retail-only sources are capped at low confidence in this run; they cannot support institution-level conclusions.
- Reddit is optional and sparse for this run; its absence or low usability lowers confidence rather than blocking the workflow.

## Event Context vs Reaction Evidence
- News and filings describe event facts; sentiment cards describe participant reaction.
- Related posts share independence groups such as event:MSFT:2026-07-02:earnings-or-price-action. Research Manager must not count article facts and social reposts as separate fundamental evidence.

## Final Sentiment Interpretation
Final sentiment: Mixed / low confidence. The signal is company-specific only where cards are direct-company, otherwise it is broad retail color. It is not sourced from analyst or institution-level feeds and is too noisy to drive a Buy/Hold/Sell decision alone.

## Evidence Gaps
- No approved analyst-rating revision feed, options sentiment, or institutional survey source was available.
- Reddit coverage is optional and low confidence in this run.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: social:MSFT:2026-07-02:001, social:MSFT:2026-07-02:002
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
