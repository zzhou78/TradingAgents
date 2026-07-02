# Sentiment Analyst Report - AAPL

## Tool Outputs Used
- social_summary.json source-level records: social:AAPL:2026-07-02:001, social:AAPL:2026-07-02:002.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| 42 | 30 | 8 | 2 | 20 | low |

The usable sentiment signal is mixed retail-only reaction. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
| social:AAPL:2026-07-02:001 | fetch_stocktwits_messages | ticker_specific_retail_platform | 31 | 29 | 8/2/19 | medium | none disclosed |
| social:AAPL:2026-07-02:002 | fetch_reddit_posts | broad_social_discussion | 11 | 1 | 0/0/1 | low | none disclosed |

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
| social:AAPL:2026-07-02:item:0010 | fetch_stocktwits_messages | neutral | medium | direct_company | reaction:AAPL:2026-07-02:product | [2026-07-02T21:00:34Z · @jujets · no-label] $AAPL the youth of the world Love the I Phone!! Families will continue and grow in the Apple ECO ! Great Products an |
| social:AAPL:2026-07-02:item:0012 | fetch_stocktwits_messages | neutral | medium | direct_company | reaction:AAPL:2026-07-02:earnings | [2026-07-02T20:56:30Z · @thebig2na · no-label] $AAPL long on Apple until 15 minutes before earnings release, not gambling… |
| social:AAPL:2026-07-02:item:0019 | fetch_stocktwits_messages | bullish | medium | direct_company | reaction:AAPL:2026-07-02:valuation | [2026-07-02T20:51:01Z · @thebig2na · no-label] $AAPL told you about the iPhone Fold and the absolutely crazy interest, people(including myself) will absolutely |

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
| social:AAPL:2026-07-02:item:0002 | fetch_stocktwits_messages | neutral | low | [2026-07-02T21:36:31Z · @Judy11 · no-label] $AAPL should have bought at 279. Not here. No thanks |
| social:AAPL:2026-07-02:item:0004 | fetch_stocktwits_messages | neutral | low | [2026-07-02T21:25:16Z · @cubie · no-label] @Jeremymartin007 @simon58 @judgeyoung2 @jenbunn @ribbey @EBE_day @TraderRapp @Godreal1 @tonyctl @zuby34   thats was b |
| social:AAPL:2026-07-02:item:0005 | fetch_stocktwits_messages | neutral | low | [2026-07-02T21:24:14Z · @DarkFlowSignals · no-label] $AAPL Soft jobs print rotated money out of tech and into safety today, but the tape steadied into the close |

## Excluded / Downgraded Evidence
- Low-information, meme, spam-like, cross-ticker, and post-trade-date items are excluded or downgraded by the evidence cards.
- Retail-only sources are capped at low confidence in this run; they cannot support institution-level conclusions.
- Reddit is optional and sparse for this run; its absence or low usability lowers confidence rather than blocking the workflow.

## Event Context vs Reaction Evidence
- News and filings describe event facts; sentiment cards describe participant reaction.
- Related posts share independence groups such as event:AAPL:2026-07-02:earnings-or-price-action. Research Manager must not count article facts and social reposts as separate fundamental evidence.

## Final Sentiment Interpretation
Final sentiment: Mixed / low confidence. The signal is company-specific only where cards are direct-company, otherwise it is broad retail color. It is not sourced from analyst or institution-level feeds and is too noisy to drive a Buy/Hold/Sell decision alone.

## Evidence Gaps
- No approved analyst-rating revision feed, options sentiment, or institutional survey source was available.
- Reddit coverage is optional and low confidence in this run.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: social:AAPL:2026-07-02:001, social:AAPL:2026-07-02:002
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
