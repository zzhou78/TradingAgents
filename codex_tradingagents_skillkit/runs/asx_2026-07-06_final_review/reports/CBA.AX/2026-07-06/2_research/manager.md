# Research Manager Report - CBA.AX

## Tool Outputs Used
- Analyst reports for market, sentiment, news, fundamentals, financial report, and industry/theme discovery.
- Debate reports from Bull and Bear researchers.

## Primary Rating Driver
Primary rating driver: mixed

Market technicals are treated as a confidence and timing modifier, not as the main investment-rating engine.

## Evidence Winner
Metric direction is not strong enough for a directional rating: 7 available / 0 gap-labelled; 1 supportive, 1 adverse, 0 mixed, 5 neutral, 0 context-only, 2 available / 0 gap-labelled core sections. supportive examples: dividend (supportive, financial:CBA.AX:2026-07-06:021); adverse examples: impairment (adverse, financial:CBA.AX:2026-07-06:020); mixed/neutral examples: net interest margin (neutral, financial:CBA.AX:2026-07-06:016); CET1 (neutral, financial:CBA.AX:2026-07-06:017). The Research Manager cannot upgrade or downgrade without clearer directional metric quality.

## Structured Evidence Matrix
| Role | Evidence ID | Direction | Materiality | Confidence | Tool output | Weight | Reason | Independence group ID |
|---|---|---|---|---|---|---:|---|---|
| Market Analyst | market:CBA.AX:2026-07-06:001 | mixed | high | medium | market snapshot | 0 | Hold is driven by mixed: Metric direction is not strong enough for a directional rating: 7 available / 0 gap-labelled; 1 supportive, 1 adverse, 0 mixed, 5 neutral, 0 context-only, 2 available / 0 gap-labelled core sections. supportive examples: dividend (supportive, financial:CBA.AX:2026-07-06:021); adverse examples: impairment (adverse, financial:CBA.AX:2026-07-06:020); mixed/neutral examples: net interest margin (neutral, financial:CBA.AX:2026-07-06:016); CET1 (neutral, financial:CBA.AX:2026-07-06:017). The Research Manager cannot upgrade or downgrade without clearer directional metric quality. Market setup is a confidence/timing modifier only: latest close 164.66 is above the 10 EMA (163.25), below the 50 SMA (165.15), and above the 200 SMA (164.47). Trend score +0 changes Trader timing and Research Manager confidence, but it is not the evidence winner. | market:CBA.AX:2026-07-06:trend |
| Financial Report Analyst | financial:CBA.AX:2026-07-06:001 | positive | high | medium | filing section extraction | +2 | ASX document and sector-metric records support financial review with gaps disclosed | event:CBA.AX:2026-07-06:financial-report |
| News Analyst | news:CBA.AX:2026-07-06:001 | positive | medium | medium | article evidence card | +1 | Direct company evidence, not repeated snippet-only headlines | event:CBA.AX:2026-07-06:earnings |
| Sentiment Analyst | social:CBA.AX:2026-07-06:001 | mixed | low | low | social summary | 0 | Retail-only reaction is noisy and not independent fundamental evidence | reaction:CBA.AX:2026-07-06:retail |
| Bear Researcher | fundamentals:CBA.AX:2026-07-06:001 | negative | medium | medium | fundamentals packet | -1 | Valuation/timing risk keeps action from becoming aggressive | risk:CBA.AX:2026-07-06:valuation-trend |

Score calculation / component weights: Sector metric direction mix (7 available / 0 gap-labelled; 1 supportive, 1 adverse, 0 mixed, 5 neutral, 0 context-only), +1 official financial-report sections (2 available / 0 gap-labelled core sections), +0 market setup as timing/confidence modifier (mixed: close is above 10 EMA, below 50 SMA, and above 200 SMA), -1 evidence-gap/source-depth cap, 0 retail sentiment = Hold driven by mixed.

## Role Evidence Weighting
- Financial report / sector metrics: primary evidence group for ASX where available; filing and fundamentals evidence is not counted again through Bull/Bear restatement.
- Market technicals: capped timing/confidence modifier.
- News: contextual event evidence unless a direct material event is identified.
- Sentiment: low-confidence retail reaction with zero standalone decision weight.

## Rating Rationale
**Recommendation**: Hold

Hold beats Overweight and Underweight because metric direction is mixed, neutral, or gap-limited; timing uncertainty is left to Trader. The earnings/news/social style of evidence is grouped by independence ID so repeated role mentions do not become separate support. Rating-vs-rating selection was explicitly considered; social sentiment alone has zero decision weight.

## Rating-vs-Rating Reasoning
1. Why not Buy / Overweight? Buy/Overweight is not selected because sector metric quality is not clearly supportive (7 available / 0 gap-labelled; 1 supportive, 1 adverse, 0 mixed, 5 neutral, 0 context-only; 2 available / 0 gap-labelled core sections).
2. Why not Sell / Underweight? Sell/Underweight is not selected because the metric evidence is not clearly adverse enough to prove deterioration.
3. Which role evidence was decisive? Decisive role evidence is Financial Report Analyst / ASX sector metrics (financial:CBA.AX:2026-07-06:021) plus Fundamentals/Financial section context; Market Analyst (market:CBA.AX:2026-07-06:001, market:CBA.AX:2026-07-06:002, market:CBA.AX:2026-07-06:003, market:CBA.AX:2026-07-06:004) modifies timing; News (news:CBA.AX:2026-07-06:001) is contextual and Sentiment is low weight.
4. Which sector-specific financial metrics mattered? banks metric direction mix: 7 available / 0 gap-labelled; 1 supportive, 1 adverse, 0 mixed, 5 neutral, 0 context-only. supportive examples: dividend (supportive, financial:CBA.AX:2026-07-06:021); adverse examples: impairment (adverse, financial:CBA.AX:2026-07-06:020); mixed/neutral examples: net interest margin (neutral, financial:CBA.AX:2026-07-06:016); CET1 (neutral, financial:CBA.AX:2026-07-06:017). Highlighted metric: dividend is available / supportive via financial:CBA.AX:2026-07-06:021.
5. Which evidence gaps capped confidence? Confidence is capped by 0 unavailable sector metric/gap labels, 0 unavailable core financial sections, low-confidence retail sentiment from social:CBA.AX:2026-07-06:001, and medium-confidence extraction depth.
6. How market setup changed the final rating. Market setup is a confidence/timing modifier only: latest close 164.66 is above the 10 EMA (163.25), below the 50 SMA (165.15), and above the 200 SMA (164.47). Trend score +0 changes Trader timing and Research Manager confidence, but it is not the evidence winner.

## Sector Metric Direction Audit
Direction is based on the extracted phrase, supporting sentence, clean value, and comparison basis below, not metric presence alone. Navigation/page-list snippets are downgraded to low-confidence context-only evidence.

| metric_name | extracted_value_or_phrase | clean_metric_value | value_unit | value_context | metric_value_status | association_score | association_reason | table_mapping_confidence | table_mapping_reason | period_reference | comparison_reference | supporting_sentence | comparison_basis | direction | confidence | confidence_reason | evidence_id | table_title | row_label | column_label | cell_value | source_page | current_period_value | prior_period_value | variance_value | variance_percent | raw_row_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| net_interest_margin | Statutory NPAT $10,133m 7% on FY24 Cash NPAT $10,252m 4% on FY24 Net interest margin 2.08% 9bpts on FY24 Loan loss rate 7bpts 2bpts on FY24 26 Highlights Sustainable shareholder re | 2.08 | % | Net interest margin near 2.08% | value_extracted | 100 | label-value distance 0 tokens; unit % compatible; competing labels nearby: margins, impairment | 0 | no structured table mapping available | FY2024 | not specified | Statutory NPAT $10,133m 7% on FY24 Cash NPAT $10,252m 4% on FY24 Net interest margin 2.08% 9bpts on FY24 Loan loss rate 7bpts 2bpts on FY24 26 Highlights Sustainable shareholder returns Delivering strong and sustainable fully franked | metric mentioned without explicit comparative baseline | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:CBA.AX:2026-07-06:016 | unavailable | unavailable | unavailable | unavailable | 15 | unavailable | unavailable | unavailable | unavailable | unavailable |
| cet1 | Financial highlights $10,133m Statutory net profit after tax (NPAT) 7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Level 2) Flat on FY24 2.08% N | 12.3 | % | Capital ratio CET1 near 12.3% | value_extracted | 100 | label-value distance 0 tokens; unit % compatible; competing labels nearby: dividend, dividends, capital_adequacy | 0 | no structured table mapping available | FY2024 | not specified | Financial highlights $10,133m Statutory net profit after tax (NPAT) 7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Level 2) Flat on FY24 2.08% Net interest margin 9bpts on FY24 $28,465m Operating income | metric mentioned without explicit comparative baseline | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:CBA.AX:2026-07-06:017 | unavailable | unavailable | unavailable | unavailable | 3 | unavailable | unavailable | unavailable | unavailable | unavailable |
| loan_growth | Home lending grew above market at 7%, while business and rural lending grew 2% above a relatively flat | 7 | % | Home lending near 7% | value_extracted | 92 | label-value distance 4 tokens; unit % compatible | 0 | no structured table mapping available | not specified | not specified | Home lending grew above market at 7%, while business and rural lending grew 2% above a relatively flat | metric mentioned without explicit comparative baseline | neutral | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:CBA.AX:2026-07-06:018 | unavailable | unavailable | unavailable | unavailable | 18 | unavailable | unavailable | unavailable | unavailable | unavailable |
| arrears | Home loan and personal / 1.50 / 1.51 __TABLE_ROW__ page=17 table=1001 row=48 title=pdfplumber_words / Operating expenses / Operating expenses increased 6% driven by higher staff, i | 6 | % | arrears near 6% | value_extracted | 87 | label-value distance 9 tokens; unit % compatible | 0 | no structured table mapping available | not specified | not specified | Home loan and personal / 1.50 / 1.51 __TABLE_ROW__ page=17 table=1001 row=48 title=pdfplumber_words / Operating expenses / Operating expenses increased 6% driven by higher staff, information technology costs and / loan arrears increased as | period-over-period wording in extracted filing/report phrase | neutral | low | metric row appears present, but dense table values were not safely mapped to columns | financial:CBA.AX:2026-07-06:019 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |
| impairment | loan impairment expense ¹ 726 802 1,108 674 715 1 The year ended 30 June 2024 includes a benefit of $30 million and $18 million for the Group and the Bank, respectively, in relatio | 726 | $m | targeted plugin flattened table row/column association | value_extracted | 100 | targeted ticker plugin matched a configured row inside a configured section before generic scoring | 100 | accepted row label; header row available; accepted column label; preferred value type current_period_value; unit $m compatible; source page preserved | 30 Jun 25 $M | 30 Jun 24 $M | loan impairment expense ¹ 726 802 1,108 674 715 1 The year ended 30 June 2024 includes a benefit of $30 million and $18 million for the Group and the Bank, respectively, in relation to credit exposures reclassified to assets held for sale. | current/prior period values parsed from flattened financial table text | adverse | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:CBA.AX:2026-07-06:020 | material_risks | loan impairment expense | 30 Jun 25 $M | 726 | 130 | 726 | 802 | unavailable | unavailable | loan impairment expense ¹ 726 802 1,108 674 715 1 The year ended 30 June 2024 includes a benefit of $30 million and $18 million for the Group and the Bank, respectively, in relation to credit exposures reclassified to assets held for sale. Movement in provisio |
| dividend | Financial highlights $10,133m Statutory net profit after tax (NPAT) 7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Level 2) Flat on FY24 2.08% N | 4.85 | $ | Dividend near $4.85 | value_extracted | 100 | label-value distance 0 tokens; unit $ compatible; competing labels nearby: dividends, dividends, capital_adequacy | 0 | no structured table mapping available | FY2024 | not specified | Financial highlights $10,133m Statutory net profit after tax (NPAT) 7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Level 2) Flat on FY24 2.08% Net interest margin 9bpts on FY24 $28,465m Operating income | period-over-period wording in extracted filing/report phrase | supportive | medium | source extractor confidence is medium and direction is based on supporting sentence/comparison basis | financial:CBA.AX:2026-07-06:021 | unavailable | unavailable | unavailable | unavailable | 3 | unavailable | unavailable | unavailable | unavailable | unavailable |
| roe | Return on equity – cash basis Based on net profit after tax (“cash basis”) divided by average shareholders’ | unavailable | unavailable | no high-confidence metric-value association | metric_mentioned_only | 35 | metric label present but no compatible value found; competing or rejected labels may be closer | 0 | no table row mapping available | unavailable | unavailable | Return on equity – cash basis Based on net profit after tax (“cash basis”) divided by average shareholders’ | metric mentioned without explicit comparative baseline | neutral | low | metric mention lacks a clean value and explicit comparison baseline | financial:CBA.AX:2026-07-06:022 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |

## Debate Outcome Scorecard
| Field | Outcome |
|---|---|
| Bull evidence quality | medium |
| Bear evidence quality | medium |
| Strongest Bull evidence ID | financial:CBA.AX:2026-07-06:001 |
| Strongest Bear evidence ID | fundamentals:CBA.AX:2026-07-06:001 |
| Which side directly answered the other side better? | Bear |
| Which side relied on weaker or duplicated evidence? | neither side dominated; duplicated News/Sentiment reaction was discounted by independence group |
| Which evidence gap matters most? | Confidence is capped by 0 unavailable sector metric/gap labels, 0 unavailable core financial sections, low-confidence retail sentiment from social:CBA.AX:2026-07-06:001, and medium-confidence extraction depth. |
| Debate winner | Balanced |
| Rating implication | Hold |
| Trader implication | HOLD |

## Debate Change Assessment
- Pre-debate analyst evidence rating: Hold.
- Changed by debate? No.
- Explanation: Pre-debate analyst evidence already supported Hold; Bull/Bear debate clarified evidence quality and independence groups rather than changing the rating.
- Scorecard ID: debate:CBA.AX:2026-07-06:outcome-scorecard

## Market Technicals as Confidence / Timing Modifier
Market setup is a confidence/timing modifier only: latest close 164.66 is above the 10 EMA (163.25), below the 50 SMA (165.15), and above the 200 SMA (164.47). Trend score +0 changes Trader timing and Research Manager confidence, but it is not the evidence winner.

## Evidence Gaps
- No final investment judgment is made by Python. This recommendation is Codex interpretation of collected evidence.
- Social reaction is low confidence and cannot independently drive the rating.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:CBA.AX:2026-07-06:001, financial:CBA.AX:2026-07-06:001, news:CBA.AX:2026-07-06:001
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
