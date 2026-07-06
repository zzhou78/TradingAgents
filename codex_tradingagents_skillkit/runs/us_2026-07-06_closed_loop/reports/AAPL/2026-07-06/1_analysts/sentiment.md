# Sentiment Analyst Report - AAPL

## Tool Outputs Used
- social_summary.json source-level records: social:AAPL:2026-07-06:001, social:AAPL:2026-07-06:002.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| 38 | 31 | 9 | 1 | 21 | low |

The usable sentiment signal is mixed retail-only reaction. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
| social:AAPL:2026-07-06:001 | fetch_stocktwits_messages | ticker_specific_retail_platform | 31 | 30 | 9/1/20 | medium | none disclosed |
| social:AAPL:2026-07-06:002 | fetch_reddit_posts | broad_social_discussion | 7 | 1 | 0/0/1 | low | none disclosed |

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
| social:AAPL:2026-07-06:item:0020 | fetch_stocktwits_messages | neutral | high | direct_company | reaction:AAPL:2026-07-06:valuation | [2026-07-06T05:18:46Z · @HeroicJobCreator · no-label] $AAPL $DJT $SPCX $SPY $TQQQ recap because you’re too slow to follow along.   You post democrats want to re |
| social:AAPL:2026-07-06:item:0013 | fetch_stocktwits_messages | bullish | medium | direct_company | reaction:AAPL:2026-07-06:earnings | [2026-07-06T09:46:40Z · @CapitaLit · no-label] NVDA, AAPL Stocks In Focus: Foxconn Beats Q2 Revenue Estimates But Sounds Caution On Geopolitics     $NVDA $AAPL |
| social:AAPL:2026-07-06:item:0019 | fetch_stocktwits_messages | bullish | medium | direct_company | reaction:AAPL:2026-07-06:earnings | [2026-07-06T05:44:02Z · @StocktwitsNews · no-label] NVDA, AAPL Stocks In Focus: Foxconn Beats Q2 Revenue Estimates But Sounds Caution On Geopolitics   $NVDA $AA |

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
| social:AAPL:2026-07-06:item:0002 | fetch_stocktwits_messages | neutral | low | [2026-07-06T11:03:06Z · @Olivia_Strickland · no-label] $AAPL up 4% premarket to 306.20 off yesterday&#39;s 308.63 close, only 177k shares traded so far. big gap |
| social:AAPL:2026-07-06:item:0003 | fetch_stocktwits_messages | neutral | low | [2026-07-06T10:34:24Z · @AAADios · no-label] $AAPL   Market is soaring, except 🍎  News looks solid. |
| social:AAPL:2026-07-06:item:0004 | fetch_stocktwits_messages | neutral | low | [2026-07-06T10:33:24Z · @sethmarcus · no-label] S&amp;P 500 Cycle Composite 2026    If tracking from here,  S&amp;P 500 still has legs to make higher-high into |

## Excluded / Downgraded Evidence
- Low-information, meme, spam-like, cross-ticker, and post-trade-date items are excluded or downgraded by the evidence cards.
- Retail-only sources are capped at low confidence in this run; they cannot support institution-level conclusions.
- Reddit is optional and sparse for this run; its absence or low usability lowers confidence rather than blocking the workflow.

## Event Context vs Reaction Evidence
- News and filings describe event facts; sentiment cards describe participant reaction.
- Related posts share independence groups such as event:AAPL:2026-07-06:earnings-or-price-action. Research Manager must not count article facts and social reposts as separate fundamental evidence.

## Final Sentiment Interpretation
Final sentiment: Mixed / low confidence. The signal is company-specific only where cards are direct-company, otherwise it is broad retail color. It is not sourced from analyst or institution-level feeds and is too noisy to drive a Buy/Hold/Sell decision alone.

## Evidence Gaps
- No approved analyst-rating revision feed, options sentiment, or institutional survey source was available.
- Reddit coverage is optional and low confidence in this run.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: social:AAPL:2026-07-06:001, social:AAPL:2026-07-06:002
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
