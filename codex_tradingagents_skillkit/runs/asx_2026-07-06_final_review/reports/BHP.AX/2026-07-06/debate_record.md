# TradingAgents Debate Record

- Ticker: `BHP.AX`
- Trade date: `2026-07-06`
- Status: completed Codex-visible debate transcript assembled from role outputs

This file is assembled after Codex-session role reports are written. It preserves the completed debate turns and links to the full role files.

## Research Team Debate

### Bull Researcher Round 1 - Opening Case

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\2_research\bull_round_1.md`

## Tool Outputs Used
- Market Analyst: market:BHP.AX:2026-07-06:001 through market:BHP.AX:2026-07-06:004.
- Financial Report Analyst: financial:BHP.AX:2026-07-06:016, financial:BHP.AX:2026-07-06:003, financial:BHP.AX:2026-07-06:008.
- News Analyst: news:BHP.AX:2026-07-06:001.

## Strongest Bull Evidence
- The best bull case is available ASX filing sections and market evidence support a reviewable base case, supported by direct filing and earnings-release evidence: financial:BHP.AX:2026-07-06:016 and financial:BHP.AX:2026-07-06:008.
- Market evidence is not ignored: latest close 60.02 is below the 10 EMA, above the 50 SMA, and above the 200 SMA (market:BHP.AX:2026-07-06:001, market:BHP.AX:2026-07-06:004).
- News support comes from news:BHP.AX:2026-07-06:001; social evidence is not counted as independent high-confidence confirmation.

## Falsification Conditions
- Falsified if updated filing evidence contradicts the earnings/segment strength cited above.
- Falsified technically if price loses the 10 EMA at 60.17 and fails to recover, or if BHP.AX breaks materially below the 200 SMA at 50.05.
- Falsified if Research Manager finds the same event is double-counted across News and Sentiment.

## Response To Bear
Bear is right that valuation and trend quality matter. The bull answer is that direct financial evidence remains stronger than retail sentiment, so the risk should limit aggressiveness rather than erase the constructive case.

### Bear Researcher Round 1 - Rebuttal to Bull

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\2_research\bear_round_1.md`

## Tool Outputs Used
- Market Analyst moving-average and MACD evidence: market:BHP.AX:2026-07-06:001, market:BHP.AX:2026-07-06:003, market:BHP.AX:2026-07-06:004, market:BHP.AX:2026-07-06:006.
- Fundamentals and filings: fundamentals:BHP.AX:2026-07-06:001, financial:BHP.AX:2026-07-06:012.
- Sentiment source quality records: social:BHP.AX:2026-07-06:001, social:BHP.AX:2026-07-06:002.

## Strongest Bear Evidence
- The strongest bear case is source coverage gaps and technical confirmation risk limit conviction. The table-driven market evidence shows close 60.02, 50 SMA 59.92, 200 SMA 50.05, and MACD -0.22.
- Sentiment is low-confidence retail color, not institution-level confirmation; therefore bullish platform labels should not be over-weighted.
- Risk factors and valuation/timing evidence require a margin of safety rather than a pure growth extrapolation.

## Falsification Conditions
- Falsified if BHP.AX reclaims the key trend levels with MACD improving and filings continue to show durable growth.
- Falsified if Bear relies only on noisy social posts or generic risk text without evidence IDs.

## Response To Bull
Bull's strongest argument is direct earnings and segment evidence. Bear's answer is not that the company is weak; it is that market timing, valuation, and trend evidence limit the immediate reward/risk, especially where social evidence is low-quality.

### Research Manager Decision - Evidence Weighing

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\2_research\manager.md`

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Primary Rating Driver
Primary rating driver: mixed

Market technicals are treated as a confidence and timing modifier, not as the main investment-rating engine.

## Evidence Winner
Metric direction is not strong enough for a directional rating: 6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only, 2 available / 0 gap-labelled core sections. supportive examples: production (supportive, financial:BHP.AX:2026-07-06:031); adverse examples: none; mixed/neutral examples: realised price (neutral, financial:BHP.AX:2026-07-06:032); unit cost (neutral, financial:BHP.AX:2026-07-06:033). The Research Manager cannot upgrade or downgrade without clearer directional metric quality.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:BHP.AX:2026-07-06:001 | mixed | high | medium | market snapshot | 0 | Hold is driven by mixed: Metric direction is not strong enough for a directional rating: 6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only, 2 available / 0 gap-labelled core sections. supportive examples: production (supportive, financial:BHP.AX:2026-07-06:031); adverse examples: none; mixed/neutral examples: realised price (neutral, financial:BHP.AX:2026-07-06:032); unit cost (neutral, financial:BHP.AX:2026-07-06:033). The Research Manager cannot upgrade or downgrade without clearer directional metric quality. Market setup is a confidence/timing modifier only: latest close 60.02 is below the 10 EMA (60.17), above the 50 SMA (59.92), and above the 200 SMA (50.05). Trend score +0 changes Trader timing and Research Manager confidence, but it is not the evidence winner. | market:BHP.AX:2026-07-06:trend |
| Financial Report Analyst | financial:BHP.AX:2026-07-06:016 | positive | high | medium | filing section extraction | +2 | ASX document and sector-metric records support financial review with gaps disclosed | event:BHP.AX:2026-07-06:financial-report |
| News Analyst | news:BHP.AX:2026-07-06:001 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:BHP.AX:2026-07-06:earnings |
| Sentiment Analyst | social:BHP.AX:2026-07-06:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:BHP.AX:2026-07-06:retail |
| Bear Researcher | fundamentals:BHP.AX:2026-07-06:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:BHP.AX:2026-07-06:valuation-trend |

Score calculation / component weights: Sector metric direction mix (6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only), +1 official financial-report sections (2 available / 0 gap-labelled core sections), +0 market setup as timing/confidence modifier (mixed: close is below 10 EMA, above 50 SMA, and above 200 SMA), -1 evidence-gap/source-depth cap, 0 retail sentiment = Hold driven by mixed.

## Role Evidence Weighting
- Financial report / sector metrics: primary evidence group for ASX where available; filing and fundamentals evidence is not counted again through Bull/Bear restatement.
- Market technicals: capped timing/confidence modifier.
- News: contextual event evidence unless a direct material event is identified.
- Sentiment: low-confidence retail reaction with zero standalone decision weight.

## Rating Rationale
**Recommendation**: Hold

Hold beats Overweight and Underweight because metric direction is mixed, neutral, or gap-limited; timing uncertainty is left to Trader. The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Rating-vs-rating selection was explicitly considered; social sentiment alone has zero decision weight.

## Rating-vs-Rating Reasoning
1. Why not Buy / Overweight? Buy/Overweight is not selected because sector metric quality is not clearly supportive (6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only; 2 available / 0 gap-labelled core sections).
2. Why not Sell / Underweight? Sell/Underweight is not selected because the metric evidence is not clearly adverse enough to prove deterioration.
3. Which role evidence was decisive? Decisive role evidence is Financial Report Analyst / ASX sector metrics (financial:BHP.AX:2026-07-06:031) plus Fundamentals/Financial section context; Market Analyst (market:BHP.AX:2026-07-06:001, market:BHP.AX:2026-07-06:002, market:BHP.AX:2026-07-06:003, market:BHP.AX:2026-07-06:004) modifies timing; News (news:BHP.AX:2026-07-06:001) is contextual and Sentiment is low weight.
4. Which sector-specific financial metrics mattered? miners metric direction mix: 6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only. supportive examples: production (supportive, financial:BHP.AX:2026-07-06:031); adverse examples: none; mixed/neutral examples: realised price (neutral, financial:BHP.AX:2026-07-06:032); unit cost (neutral, financial:BHP.AX:2026-07-06:033). Highlighted metric: production is available / supportive via financial:BHP.AX:2026-07-06:031.
5. Which evidence gaps capped confidence? Confidence is capped by 0 unavailable sector metric/gap labels, 0 unavailable core financial sections, low-confidence retail sentiment from social:BHP.AX:2026-07-06:001, and medium-confidence extraction depth.
6. How market setup changed the final rating. Market setup is a confidence/timing modifier only: latest close 60.02 is below the 10 EMA (60.17), above the 50 SMA (59.92), and above the 200 SMA (50.05). Trend score +0 changes Trader timing and Research Manager confidence, but it is not the evidence winner.

## Sector Metric Direction Audit
Direction is based on the extracted phrase, supporting sentence, clean value, and comparison basis below, not metric presence alone. Navigation/page-list snippets are downgraded to low-confidence context-only evidence.

| metric_name | extracted_value_or_phrase | clean_metric_value | value_unit | value_context | metric_value_status | association_score | association_reason | table_mapping_confidence | table_mapping_reason | period_reference | comparison_reference | supporting_sentence | comparison_basis | direction | confidence | confidence_reason | evidence_id | table_title | row_label | column_label | cell_value | source_page | current_period_value | prior_period_value | variance_value | variance_percent | raw_row_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| production | production record 263 Mt ^1% on FY2024 Western Australia Iron Ore (WAIO) is the lowest-cost major iron ore producer globally 2 and has one of the lowest greenhouse gas (GHG) emissi | 263 | m | targeted plugin flattened table row/column association | value_extracted | 100 | targeted ticker plugin matched a configured row inside a configured section before generic scoring | 100 | accepted row label; header row available; accepted column label; unit m compatible; source page preserved | FY2025 % | not specified | production record 263 Mt ^1% on FY2024 Western Australia Iron Ore (WAIO) is the lowest-cost major iron ore producer globally 2 and has one of the lowest greenhouse gas (GHG) emission production intensities of benchmarked iron ore operations | current/prior period values parsed from flattened financial table text | supportive | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:BHP.AX:2026-07-06:031 | segment_product_performance | production | FY2025 % | 263 M | 19 | unavailable | unavailable | unavailable | 263 | production record 263 Mt ^1% on FY2024 Western Australia Iron Ore (WAIO) is the lowest-cost major iron ore producer globally 2 and has one of the lowest greenhouse gas (GHG) emission production intensities of benchmarked iron ore operations.3 WAIO set multiple records in FY2025, including for full-year production of 257 Mt (290 Mt on a 100 per cent basis) |
| realised_price | re 4,392 3,711 Underlying ROCE 17% 13% Total copper production (kt) 2,017 1,865 Average realised prices Copper (US$/lb) 4.25 3.98 Unit costs Escondida (US$/lb) 1.19 1.45 Spence (US | 4.25 | US$/lb | flattened average realised prices table row | value_extracted | 88 | BHP flattened realised-price table row has realised-price heading, commodity row label, unit, and current/prior values | 88 | realised-price heading plus commodity row, unit, and current/prior values | FY2025 | FY2024 | re 4,392 3,711 Underlying ROCE 17% 13% Total copper production (kt) 2,017 1,865 Average realised prices Copper (US$/lb) 4.25 3.98 Unit costs Escondida (US$/lb) 1.19 1.45 Spence (US$/lb) 2.07 2.13 Copper | current/prior average realised price table values | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:BHP.AX:2026-07-06:032 | Average realised prices | Copper | FY2025 US$/lb | 4.25 | 113 | 4.25 | 3.98 | unavailable | unavailable | Average realised prices Copper (US$/lb) 4.25 3.98 |
| unit_cost_aisc | Production for FY2026 is expected to increase to between 18 and 20 Mt (36 and 40 Mt on a 100 per cent basis), weighted to the second half, while unit costs are expected to decrease | 116 | US$/t | unit costs near US$116/t | value_extracted | 86 | label-value distance 7 tokens; unit US$/t compatible; competing labels nearby: guidance | 0 | no structured table mapping available | FY2026 | not specified | Production for FY2026 is expected to increase to between 18 and 20 Mt (36 and 40 Mt on a 100 per cent basis), weighted to the second half, while unit costs are expected to decrease with guidance between US$116/t and US$128/t as we push to | metric mentioned without explicit comparative baseline | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:BHP.AX:2026-07-06:033 | unavailable | unavailable | unavailable | unavailable | 20 | unavailable | unavailable | unavailable | unavailable | unavailable |
| capex | investing cash flows (13,350) (8,762) (13,065) Net financing cash flows (5,971) (11,669) (10,315) Net (decrease)/increase in cash and cash equivalents (629) 234 (4,679) Net operati | -13350 | $m | targeted plugin flattened table row/column association | value_extracted | 100 | targeted ticker plugin matched a configured row inside a configured section before generic scoring | 100 | accepted row label; header row available; accepted column label; preferred value type current_period_value; unit $m compatible; source page preserved | 2025 $M | 2024 $M | investing cash flows (13,350) (8,762) (13,065) Net financing cash flows (5,971) (11,669) (10,315) Net (decrease)/increase in cash and cash equivalents (629) 234 (4,679) Net operating cash inflows of US$18.7 billion decreased by US$2.0 billi | current/prior period values parsed from flattened financial table text | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:BHP.AX:2026-07-06:034 | cash_flow_statement | investing cash flows | 2025 $M | (13,350) | 31 | -13350 | -8762 | unavailable | unavailable | investing cash flows (13,350) (8,762) (13,065) Net financing cash flows (5,971) (11,669) (10,315) Net (decrease)/increase in cash and cash equivalents (629) 234 (4,679) Net operating cash inflows of US$18.7 billion decreased by US$2.0 billion. This is primaril |
| reserves_resources | Total reserves (2) (15) 13 Summarised financial information relating to each of the Group’s subsidiaries with non-controlling interests (NCI) that are significant to the Group is s | unavailable | unavailable | no high-confidence metric-value association | metric_mentioned_only | 35 | metric label present but no compatible value found; competing or rejected labels may be closer | 0 | no table row mapping available | unavailable | unavailable | Total reserves (2) (15) 13 Summarised financial information relating to each of the Group’s subsidiaries with non-controlling interests (NCI) that are significant to the Group is shown below: /nobreakspace 2025 2024 US$M Minera Escondida | dense table-like row requires parsed row/column mapping before value use | neutral | low | metric row appears present, but dense table values were not safely mapped to columns | financial:BHP.AX:2026-07-06:035 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |
| commodity_exposure | Examples of forward-looking statements contained in this Report include, without limitation, statements describing (i) our strategy, Our Values and how we define our success; (ii) | unavailable | unavailable | no high-confidence metric-value association | unavailable | 0 | metric label was not found in extracted text | 0 | no table row mapping available | unavailable | unavailable | Examples of forward-looking statements contained in this Report include, without limitation, statements describing (i) our strategy, Our Values and how we define our success; (ii) our expectations regarding future demand for certain commodi | portfolio composition narrative | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:BHP.AX:2026-07-06:036 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |

## Debate Outcome Scorecard
| Field | Outcome |
|---|---|
| Bull evidence quality | medium |
| Bear evidence quality | medium |
| Strongest Bull evidence ID | financial:BHP.AX:2026-07-06:016 |
| Strongest Bear evidence ID | fundamentals:BHP.AX:2026-07-06:001 |
| Which side directly answered the other side better? | Bear |
| Which side relied on weaker or duplicated evidence? | neither side dominated; duplicated News/Sentiment reaction was discounted by independence group |
| Which evidence gap matters most? | Confidence is capped by 0 unavailable sector metric/gap labels, 0 unavailable core financial sections, low-confidence retail sentiment from social:BHP.AX:2026-07-06:001, and medium-confidence extraction depth. |
| Debate winner | Balanced |
| Rating implication | Hold |
| Trader implication | HOLD |

## Debate Change Assessment
- Pre-debate analyst evidence rating: Hold.
- Changed by debate? No.
- Explanation: Pre-debate analyst evidence already supported Hold; Bull/Bear debate clarified evidence quality and independence groups rather than changing the rating.
- Scorecard ID: debate:BHP.AX:2026-07-06:outcome-scorecard

## Market Technicals as Confidence / Timing Modifier
Market setup is a confidence/timing modifier only: latest close 60.02 is below the 10 EMA (60.17), above the 50 SMA (59.92), and above the 200 SMA (50.05). Trend score +0 changes Trader timing and Research Manager confidence, but it is not the evidence winner.

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

## Risk Management Team Debate

### Aggressive Risk Analyst Round 1 - Opportunity Case

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\4_risk\aggressive_round_1.md`

## Tool Outputs Used
- Bull case evidence: financial:BHP.AX:2026-07-06:016, financial:BHP.AX:2026-07-06:008, news:BHP.AX:2026-07-06:001.
- Market reference: market:BHP.AX:2026-07-06:001.

## Opportunity Case
- Upside driver: available ASX filing sections and market evidence support a reviewable base case, supported by financial:BHP.AX:2026-07-06:016 and financial:BHP.AX:2026-07-06:008.
- If price confirms above 60.70, the paper-study setup would have stronger momentum support.

## Failure Points
- Failure point: break below 59.35 or deterioration below the 200 SMA at 50.05.
- Failure point: earnings or segment evidence no longer supports the bull thesis.

## Response To Prior Risk Arguments
The aggressive view accepts that social evidence is low confidence and does not use it as independent confirmation.

### Conservative Risk Analyst Round 1 - Response to Aggressive

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\4_risk\conservative_round_1.md`

## Tool Outputs Used
- Bear case evidence: market:BHP.AX:2026-07-06:006, fundamentals:BHP.AX:2026-07-06:001, financial:BHP.AX:2026-07-06:012.
- Financial extraction gaps: commitments/capex sections where unavailable.

## Downside Case
- Downside driver: source coverage gaps and technical confirmation risk limit conviction, supported by market and risk-factor evidence.
- If price loses 59.35, the risk case becomes more important for portfolio sizing.

## Unsupported Upside Challenges
- Unsupported upside challenge: retail bullish labels and low-reasoning posts cannot justify high confidence.
- Unsupported upside challenge: capex/commitment detail is gap-labelled if not extracted, so claims in that area must stay cautious.

## Response To Aggressive
Aggressive has a valid upside case, but it needs trend confirmation and cannot lean on duplicated news/social evidence.

### Neutral Risk Analyst Round 1 - Weighing

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\4_risk\neutral_round_1.md`

## Tool Outputs Used
- Aggressive and Conservative risk rounds.
- Market, financial, and sentiment evidence: market:BHP.AX:2026-07-06:001, financial:BHP.AX:2026-07-06:016, social:BHP.AX:2026-07-06:001.

## Risk Argument Quality
- Aggressive evidence quality: medium, because it uses direct financial and news evidence but requires confirmation.
- Conservative evidence quality: medium, because it uses market trend and valuation/timing risk with clear falsification levels.
- Sentiment evidence quality: low; retail-only, noisy, and not decision-grade alone.

## Stronger Risk Side
Stronger risk side: Neutral Risk was stronger because evidence remains mixed and no directional setup is complete. The concrete opportunity is miners metric direction mix: 6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only. supportive examples: production (supportive, financial:BHP.AX:2026-07-06:031); adverse examples: none; mixed/neutral examples: realised price (neutral, financial:BHP.AX:2026-07-06:032); unit cost (neutral, financial:BHP.AX:2026-07-06:033). Highlighted metric: production is available / supportive via financial:BHP.AX:2026-07-06:031. This is the strongest concrete opportunity because it is tied to Financial Report Analyst evidence financial:BHP.AX:2026-07-06:031 rather than generic sector language. The concrete risk is Confidence is capped by 0 unavailable sector metric/gap labels, 0 unavailable core financial sections, low-confidence retail sentiment from social:BHP.AX:2026-07-06:001, and medium-confidence extraction depth. Market timing risk is explicit at close 60.02 versus confirmation 60.70 and invalidation/caution 59.35.

## Evidence Gaps
- No options-implied risk, borrow/short-interest feed, or intraday volatility surface was available.

### Portfolio Manager Synthesis

- Full output: `codex_tradingagents_skillkit\runs\asx_2026-07-06_final_review\reports\BHP.AX\2026-07-06\5_portfolio\decision.md`

## Tool Outputs Used
- Research Manager: Hold.
- Trader action: HOLD at reference price 60.02.
- Risk debate outputs and evidence: market:BHP.AX:2026-07-06:001, financial:BHP.AX:2026-07-06:016, news:BHP.AX:2026-07-06:001.

## Risk debate impact
The risk debate tempers position implementation through concrete evidence, not a generic sizing phrase. Strongest concrete opportunity: miners metric direction mix: 6 available / 0 gap-labelled; 1 supportive, 0 adverse, 0 mixed, 5 neutral, 0 context-only. supportive examples: production (supportive, financial:BHP.AX:2026-07-06:031); adverse examples: none; mixed/neutral examples: realised price (neutral, financial:BHP.AX:2026-07-06:032); unit cost (neutral, financial:BHP.AX:2026-07-06:033). Highlighted metric: production is available / supportive via financial:BHP.AX:2026-07-06:031. This is the strongest concrete opportunity because it is tied to Financial Report Analyst evidence financial:BHP.AX:2026-07-06:031 rather than generic sector language. Strongest concrete risk: Confidence is capped by 0 unavailable sector metric/gap labels, 0 unavailable core financial sections, low-confidence retail sentiment from social:BHP.AX:2026-07-06:001, and medium-confidence extraction depth. Market timing risk is explicit at close 60.02 versus confirmation 60.70 and invalidation/caution 59.35. Stronger risk side: Neutral Risk was stronger because evidence remains mixed and no directional setup is complete.

## Final Portfolio Decision
**Rating**: Hold

Research decision: Hold. Trader action: HOLD. Portfolio decision: maintain Hold paper-study stance while preserving rating/action tension. Rating and action are aligned by current setup quality. No real trade execution or broker/order tooling is used.

## Rating-Action Tension
- Research Manager rating: Hold
- Trader action: HOLD
- Portfolio stance: Hold
- Interpretation: research evidence and trade timing are separate decisions; the portfolio stance reflects research quality and risk debate, not just the immediate Trader action.

## Evidence Gaps
- Portfolio sizing, tax constraints, mandate constraints, and liquidity limits are not modeled.

## Transcript Integrity

- Pending debate outputs: `0`
- The complete report should cite these same role outputs rather than treating this file as a separate evidence source.
