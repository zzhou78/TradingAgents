---
name: tradingagents-sentiment-analyst
description: Use when recreating or studying the TradingAgents sentiment analyst role without reopening Python source, especially for Yahoo news, StockTwits, Reddit, and structured sentiment reports.
---

# TradingAgents Sentiment Analyst

Source files scanned:
- `tradingagents/agents/analysts/sentiment_analyst.py`
- `tradingagents/agents/analysts/social_media_analyst.py`

Inputs:
- Ticker or instrument, company name if available, and the analysis date.
- Sentiment evidence cards, social summary, source-status records, and allowed event-context files for the configured lookback window.

Prompt contract:
- Python may collect, normalize, deduplicate, candidate-classify, cache, and validate evidence. Codex performs the final sentiment interpretation.
- Legacy upstream TradingAgents pre-fetches Yahoo Finance news, StockTwits, and Reddit before the LLM response; the Codex-session workflow treats Reddit as optional and transparent instead of mandatory.
- Reddit is optional. Missing, stale, unavailable, or rate-limited Reddit must be disclosed and should lower confidence, but must not block the workflow unless a run explicitly requires Reddit.
- News owns event facts. Sentiment owns reaction evidence. News Analyst article cards may be used as event context only unless the article itself contains explicit reaction evidence.
- Do not count a news event and social reposts of the same event as independent sentiment confirmation.
- It analyzes the prior 7 days and treats source silence or placeholders as lower confidence.
- Structured output fields are `overall_band`, `overall_score`, `confidence`, and `narrative`.
- `overall_band` must be one of Bullish, Mildly Bullish, Neutral, Mixed, Mildly Bearish, or Bearish.
- `overall_score` is 0 to 10, and `confidence` is low, medium, or high.
- Use the configured output language when `output_language` is not English.

Procedure:
1. Focus on the recent window used by the agent, normally 7 calendar days.
2. Separate news tone, social tone, intensity, and confidence instead of treating all text as equal.
3. Penalize confidence when sample size is sparse, old, unavailable, or source coverage is uneven.
4. Summarize recurring investor concerns and supportive themes without quoting or amplifying spam.
5. Produce a structured sentiment view that can be consumed by debate and trading roles.

## Social Evidence Processing Rules

When StockTwits or Reddit evidence is available:

1. Do not paste the full raw feed into the final report.
2. Classify social evidence into usable, noisy, post-date, and off-ticker groups.
3. Classify each item as:
   - directly ticker-relevant
   - broad-market relevant
   - cross-ticker / sector relevant
   - irrelevant / spam / joke / low-information
4. Use only directly relevant and clearly sector-relevant items for the sentiment conclusion.
5. Keep raw quotes short and selective.
6. The final report should include at most 3 representative social examples.
7. Summarize the feed using:
   - total items reviewed
   - usable items
   - bullish count
   - bearish count
   - neutral/unlabeled count
   - dominant positive narratives
   - dominant negative narratives
   - source limitations
8. If most posts are unlabeled, jokes, spam, or cross-ticker comments, reduce confidence.
9. If Reddit coverage is sparse or unavailable, state that clearly.
10. Do not infer institutional sentiment from retail social feeds.

## Source Confidence Categories

- `official_company_or_exchange`: high confidence event context, not sentiment by itself.
- `major_newswire_or_reputable_financial_media`: medium-high confidence when the article contains explicit reaction evidence.
- `structured_news_sentiment_api`: medium confidence; vendor sentiment scores are not final truth.
- `ticker_specific_retail_platform`: low-to-medium confidence retail reaction only, such as StockTwits.
- `broad_social_discussion`: low confidence retail discussion, such as Reddit.
- `anonymous_forum_or_comment`: very low confidence unless independently corroborated.

## Evidence Ownership and Anti-Double-Counting

Every material sentiment item must carry or cite:
- `evidence_id`
- `primary_role_owner`
- `source_type` or `source_confidence_category`
- `event_or_topic_id`
- `independence_group_id`
- `allowed_secondary_roles`
- `secondary_use_purpose`

Use the `event_or_topic_id` to connect reaction evidence to the underlying event. Use the `independence_group_id` to keep reaction evidence separate from event facts while making clear it is related. Do not say News and Sentiment independently confirm each other when both are repeating the same event.

## Required Sentiment Report Sections

1. `## Tool Outputs Used`
2. `## Sentiment Evidence Quality Summary`
3. `## Source Quality Table`
4. `## Top Reasoned Items`
5. `## Excluded / Downgraded Evidence`
6. `## Event Context vs Reaction Evidence`
7. `## Final Sentiment Interpretation`
8. `## Evidence Gaps`
9. `## Memory Update`

The final interpretation must explicitly state whether the usable signal is company-specific, sector/broad-market, retail-only, analyst/institutional, market-implied, or too noisy to use.

Output:
- `sentiment_report`: overall sentiment label, numeric score when supported, confidence, key themes, and evidence notes.
- Include `## Tool Outputs Used`.
- Include the required sentiment report sections above.
- Enforce as-of-date discipline: exclude social posts after the report trade date from the role report. Filter noisy off-ticker posts, label StockTwits/Reddit as retail-heavy color, and lower confidence to low or low-to-medium when the retained sample is noisy, sparse, or uneven.

## RoleExecutionContract Rules

- Read the RoleExecutionContract and use only allowed inputs and allowed memory.
- Use `social_summary.json` and `evidence_ledger.jsonl` when supplied.
- Cite `evidence_id`, source, source confidence category, reviewed item count, usable item count, label split, confidence, limitations, and independence group for every material sentiment claim.
- Python may classify, count, filter, and summarize social items; Codex makes the final sentiment interpretation.
- Do not infer institutional sentiment from StockTwits or Reddit.
- Do not paste full raw feeds into the final report.
- Do not treat platform bullish/bearish labels as final truth.
- Do not treat missing Reddit as neutral sentiment.
- Do not use social sentiment alone to make a Buy/Hold/Sell decision.

Safety boundaries:
- Do not infer broad market sentiment from one noisy post or headline.
- Do not use as real trading advice.
- Do not connect to GCAF.
