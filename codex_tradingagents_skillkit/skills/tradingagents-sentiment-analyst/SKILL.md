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
- Prefetched Yahoo Finance news, StockTwits, Reddit, or equivalent sentiment data for the configured lookback window.

Prompt contract:
- The role pre-fetches Yahoo Finance news, StockTwits, and Reddit before the LLM response; do not invent missing social posts.
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

Output:
- `sentiment_report`: overall sentiment label, numeric score when supported, confidence, key themes, and evidence notes.
- Enforce as-of-date discipline: exclude social posts after the report trade date from the role report. Filter noisy off-ticker posts, label StockTwits/Reddit as retail-heavy color, and lower confidence to low or low-to-medium when the retained sample is noisy, sparse, or uneven.

Safety boundaries:
- Do not infer broad market sentiment from one noisy post or headline.
- Do not use as real trading advice.
- Do not connect to GCAF.
