# Sentiment Analyst Report - MSFT

## Tool Outputs Used
- social_summary.json source-level records: social:MSFT:2026-07-06:001, social:MSFT:2026-07-06:002.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| 13 | 3 | 0 | 0 | 3 | low |

The usable sentiment signal is low-confidence retail reaction. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
| social:MSFT:2026-07-06:001 | fetch_stocktwits_messages | ticker_specific_retail_platform | 2 | 0 | 0/0/0 | low | no_usable_ticker_relevant_items |
| social:MSFT:2026-07-06:002 | fetch_reddit_posts | broad_social_discussion | 11 | 3 | 0/0/3 | low | none disclosed |

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
| none | none | neutral | none | unavailable | none | No genuinely reasoned social items were found. |

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
| social:MSFT:2026-07-06:item:0004 | fetch_reddit_posts | neutral | low | r/stocks — 4 recent posts mentioning MSFT (via RSS feed; scores/comments unavailable): |
| social:MSFT:2026-07-06:item:0009 | fetch_reddit_posts | neutral | low | [2026-07-02] Are hyperscalers like $AMZN, $MSFT and $GOOG screwed if the there is an oversupply of data centres? |
| social:MSFT:2026-07-06:item:0010 | fetch_reddit_posts | neutral | low | body excerpt: META and SpaceX is just showed us it has excess capacity. If a data centre oversupply is true, semi stocks will fucking crash and burn for sure. V |

## Excluded / Downgraded Evidence
- Low-information, meme, spam-like, cross-ticker, and post-trade-date items are excluded or downgraded by the evidence cards.
- Retail-only sources are capped at low confidence in this run; they cannot support institution-level conclusions.
- Reddit is optional and sparse for this run; its absence or low usability lowers confidence rather than blocking the workflow.

## Event Context vs Reaction Evidence
- News and filings describe event facts; sentiment cards describe participant reaction.
- Related posts share independence groups such as event:MSFT:2026-07-06:earnings-or-price-action. Research Manager must not count article facts and social reposts as separate fundamental evidence.

## Final Sentiment Interpretation
Final sentiment: Mixed / low confidence. The signal is company-specific only where cards are direct-company, otherwise it is broad retail color. It is not sourced from analyst or institution-level feeds and is too noisy to drive a Buy/Hold/Sell decision alone.

## Evidence Gaps
- No approved analyst-rating revision feed, options sentiment, or institutional survey source was available.
- Reddit coverage is optional and low confidence in this run.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: social:MSFT:2026-07-06:001, social:MSFT:2026-07-06:002
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
