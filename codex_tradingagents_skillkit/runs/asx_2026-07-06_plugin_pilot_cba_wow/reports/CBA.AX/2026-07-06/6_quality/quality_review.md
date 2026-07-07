# Quality Reviewer Report - CBA.AX

## Tool Outputs Used
- validate_quality_review.py was run for this report directory and passed before quality_gate.json was marked passed.
- evidence_reasoning_auditor.py was run before review-ready status: pass_with_warnings (0 critical findings, 3 warnings).
- Role reports and evidence records including market:CBA.AX:2026-07-06:001, financial:CBA.AX:2026-07-06:001, news:CBA.AX:2026-07-06:001, and social:CBA.AX:2026-07-06:001.

## Quality Gate Findings
- Pending-marker check: no role output intentionally left pending.
- As-of discipline: report uses trade date 2026-07-06; source dates are disclosed.
- ASX extraction: official-source collection succeeded or explicit gaps are disclosed; sector metrics are available or gap-labelled.
- Sentiment: retail-only, low confidence, no Reddit requirement, no institution-level inference.
- Anti-double-counting: Research Manager uses independence groups and does not count social reposts as independent fundamental facts.

## Evidence Gaps
- No validator-pending state remains for this artifact. If a later validator run reports errors, remediation becomes the next workflow stage.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:CBA.AX:2026-07-06:001, financial:CBA.AX:2026-07-06:001, news:CBA.AX:2026-07-06:001
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.

## Run-Level Warnings
- debate winner is always Balanced across a multi-ticker run

