# News Analyst Report - CBA.AX

## Tool Outputs Used
- news/article_cards.json with article evidence cards, including news:CBA.AX:2026-07-02:001.
- As-of filter: only evidence valid for trade date 2026-07-02 is used for impact judgment.

## Article Evidence Cards
| Evidence ID | Title | Source | Publication date | Full-text status | Direct company relevance | Event type | Likely effect | Reason | Confidence | Evidence gap |
|---|---|---|---|---|---|---|---|---|---|---|
| news:CBA.AX:2026-07-02:001 | 2025 Annual Report | ASX announcement | 2025-12-31 | full_text | context_only | earnings/context | positive | direct earnings-release or official company evidence | low | none for selected official item |
| news:CBA.AX:2026-07-02:002 | 2025 Sustainability Reporting (pages 68-93 of the Annual Report) | ASX announcement | 2025-12-31 | full_text | pending_codex_interpretation | earnings/context | excluded / low relevance | snippet, generic, duplicate, or low direct relevance | medium | not used for final impact label |
| news:CBA.AX:2026-07-02:003 | 2025 Annual Report | ASX announcement | 2025-12-31 | full_text | pending_codex_interpretation | earnings/context | excluded / low relevance | snippet, generic, duplicate, or low direct relevance | medium | not used for final impact label |

## News Impact Summary
Impact label: mixed-to-positive, supported by news:CBA.AX:2026-07-02:001. The strongest usable news card is `2025 Annual Report`. It is treated as direct company event context, while generic snippets, duplicate official pages, unrelated posts, and post-trade-date items are excluded from the final impact label.

## Evidence Gaps
- Some candidate articles are snippet-only or generic official navigation pages; they are not used as material impact evidence.
- Full article text is preferred; snippet-only records are capped at low confidence.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: news:CBA.AX:2026-07-02:001
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
