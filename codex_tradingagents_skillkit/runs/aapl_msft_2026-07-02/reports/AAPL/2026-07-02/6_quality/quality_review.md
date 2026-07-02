# Quality Reviewer Report - AAPL

## Tool Outputs Used
- validate_quality_review.py was run for this report directory and passed before quality_gate.json was marked passed.
- Role reports and evidence records including market:AAPL:2026-07-02:001, financial:AAPL:2026-07-02:022, news:AAPL:2026-07-02:040, and social:AAPL:2026-07-02:001.

## Quality Gate Findings
- Pending-marker check: no role output intentionally left pending.
- As-of discipline: report uses trade date 2026-07-02; source dates are disclosed.
- Financial extraction: MD&A, cash-flow, and Exhibit 99.1 are present where cited.
- Sentiment: retail-only, low confidence, no Reddit requirement, no institution-level inference.
- Anti-double-counting: Research Manager uses independence groups and does not count social reposts as independent fundamental facts.

## Evidence Gaps
- No validator-pending state remains for this artifact. If a later validator run reports errors, remediation becomes the next workflow stage.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:AAPL:2026-07-02:001, financial:AAPL:2026-07-02:022, news:AAPL:2026-07-02:040
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
