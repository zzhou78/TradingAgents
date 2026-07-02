# Sentiment Analyst Report - MSFT

## Tool Outputs Used
- social_summary.json source-level records: social:MSFT:2026-07-02:001, social:MSFT:2026-07-02:002.
- social_cards.json item-level reaction cards; event context from News Analyst is used only as context, not independent sentiment support.

## Sentiment Evidence Quality Summary
| Items reviewed | Usable ticker-relevant items | Bullish | Bearish | Neutral/unlabeled | Interpretation confidence |
|---:|---:|---:|---:|---:|---|
| 32 | 29 | 8 | 5 | 16 | low |

The usable sentiment signal is mixed retail-only reaction. It is retail-only because the usable sources are StockTwits and optional Reddit/broad social. Platform labels are not treated as final sentiment, and missing or sparse Reddit coverage is not treated as neutral sentiment.

## Source Quality Table
| Evidence ID | Source | Source confidence category | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral | Confidence | Limitations |
|---|---|---|---:|---:|---|---|---|
| social:MSFT:2026-07-02:001 | fetch_stocktwits_messages | ticker_specific_retail_platform | 31 | 29 | 8/5/16 | medium | none disclosed |
| social:MSFT:2026-07-02:002 | fetch_reddit_posts | broad_social_discussion | 1 | 0 | 0/0/0 | low | no_usable_ticker_relevant_items |

## Top Reasoned Items
| Evidence ID | Source | Candidate label | Reasoning quality | Relevance | Independence group | Short excerpt |
|---|---|---|---|---|---|---|
| social:MSFT:2026-07-02:item:0015 | fetch_stocktwits_messages | neutral | high | direct_company | reaction:MSFT:2026-07-02:earnings | [2026-07-02T20:29:56Z · @EddieHayes · no-label] $MSFT    15 years of compounding in one snapshot:    Then:  • Stock: $47.44  • Revenue: $22.96B  • FCF: $10.55B |
| social:MSFT:2026-07-02:item:0031 | fetch_stocktwits_messages | neutral | high | direct_company | reaction:MSFT:2026-07-02:earnings | [2026-07-02T20:04:39Z · @FibonacciTrader_ · no-label] $MSFT - a 15-year compounding snapshot that tells the real story behind price action.    Back then:  • ~$4 |
| social:MSFT:2026-07-02:item:0022 | fetch_stocktwits_messages | bearish | medium | direct_company | reaction:MSFT:2026-07-02:valuation | [2026-07-02T20:13:41Z · @MountCapital · Bearish] $MSFT nope. it means he will increase capex  to waste more. He is famous for that |

## Representative Low-Quality Retail Items
| Evidence ID | Source | Candidate label | Reasoning quality | Short excerpt |
|---|---|---|---|---|
| social:MSFT:2026-07-02:item:0002 | fetch_stocktwits_messages | bullish | low | [2026-07-02T21:35:40Z · @NetflixUser · Bullish] $MSFT bought calls at close for next week! |
| social:MSFT:2026-07-02:item:0004 | fetch_stocktwits_messages | neutral | low | [2026-07-02T21:27:35Z · @AStrokeOfLuck · no-label] $MSFT |
| social:MSFT:2026-07-02:item:0005 | fetch_stocktwits_messages | bullish | low | [2026-07-02T21:22:15Z · @ShowMeThaMonay · Bullish] $MSFT Atleast $400 next week. |

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
