# Sentiment Analyst Report - AAPL

## Tool Outputs Used
- social_summary.json source-level records: social:AAPL:2026-07-02:001, social:AAPL:2026-07-02:002.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| 32 | 30 | 7 | 2 | 21 | low |

The usable sentiment signal is mixed retail-only reaction. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
| social:AAPL:2026-07-02:001 | fetch_stocktwits_messages | ticker_specific_retail_platform | 31 | 30 | 7/2/21 | low | none disclosed |
| social:AAPL:2026-07-02:002 | fetch_reddit_posts | broad_social_discussion | 1 | 0 | 0/0/0 | low | no_usable_ticker_relevant_items |

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
| social:AAPL:2026-07-02:item:0016 | fetch_stocktwits_messages | neutral | medium | direct_company | reaction:AAPL:2026-07-02:ai_capex | [2026-07-02T13:48:37Z · @AlphaFrontier · no-label] $AAPL China shipments are still soft. Edgewater says they’ve been down Y/Y for 8 straight weeks through end o |

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
| social:AAPL:2026-07-02:item:0002 | fetch_stocktwits_messages | neutral | low | [2026-07-02T14:00:22Z · @erob_trades_official · no-label] $AAPL what’s the news? |
| social:AAPL:2026-07-02:item:0003 | fetch_stocktwits_messages | neutral | low | [2026-07-02T14:00:19Z · @ASM · no-label] The greatest $AAPL open ive ever seen OMG wow    $SPY $QQQ |
| social:AAPL:2026-07-02:item:0004 | fetch_stocktwits_messages | bullish | low | [2026-07-02T13:58:14Z · @str8upcashhomie · Bullish] $AAPL |

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
