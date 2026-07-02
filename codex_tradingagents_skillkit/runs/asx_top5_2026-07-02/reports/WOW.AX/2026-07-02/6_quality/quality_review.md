# Quality Reviewer Report - WOW.AX

## Tool Outputs Used
- validate_quality_review.py planned check for report directory.
- Role reports and evidence records including market:WOW.AX:2026-07-02:001, financial:WOW.AX:2026-07-02:001, news:WOW.AX:2026-07-02:003, and social:WOW.AX:2026-07-02:001.

## Quality Gate Findings
- Pending-marker check: no role output intentionally left pending.
- As-of discipline: report uses trade date 2026-07-02; source dates are disclosed.
- Financial extraction: MD&A, cash-flow, and Exhibit 99.1 are present where cited.
- Sentiment: retail-only, low confidence, no Reddit requirement, no institution-level inference.
- Anti-double-counting: Research Manager uses independence groups and does not count social reposts as independent fundamental facts.

## Evidence Gaps
- Validator must still be run after file generation; if it reports errors, remediation remains the next workflow stage.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:WOW.AX:2026-07-02:001, financial:WOW.AX:2026-07-02:001, news:WOW.AX:2026-07-02:003
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
