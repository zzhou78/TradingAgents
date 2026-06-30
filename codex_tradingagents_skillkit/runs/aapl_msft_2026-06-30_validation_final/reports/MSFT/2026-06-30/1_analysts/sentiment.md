# Sentiment Analyst

## Tool Outputs Used

- social_evidence processing over StockTwits and Reddit: social:MSFT:2026-06-30:001.

## Social Evidence Processing Rules

| Source | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral split | Dominant themes | Confidence | Limitations |
|---|---:|---:|---|---|---|---|
| fetch_stocktwits_messages | 31 | 30 | 11 / 1 / 18 | retail-heavy ticker feed | medium | limited narrative depth |
| fetch_reddit_posts | 1 | 1 | 0 / 0 / 1 | retail-heavy ticker feed | medium | limited narrative depth |

Summary: 32 social items were reviewed and 31 were usable ticker-relevant items. The feed is constructive but noisy; it is retail color only and does not support broader market-participant inference.

## Evidence Gaps

Social evidence is short-horizon, retail-heavy, and not a substitute for filings, price evidence, or full article text.

## Memory Update

* Durable facts to retain: MSFT sentiment_analyst used social:MSFT:2026-06-30:001 for this 2026-06-30 validation run.
* Prior mistake to avoid: Do not override current evidence with template language.
* Open questions: Refresh evidence for any later trade date.
* Evidence references: social:MSFT:2026-06-30:001
* Staleness / expiry: Expires after 2026-06-30.
