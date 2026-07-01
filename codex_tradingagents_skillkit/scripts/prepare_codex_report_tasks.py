from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

TASKS = {
    "market_analyst_task.md": {
        "skill": "tradingagents-market-analyst",
        "output_key": "market_report",
        "instruction": "Write the Market Analyst report from the market evidence only.",
    },
    "sentiment_analyst_task.md": {
        "skill": "tradingagents-sentiment-analyst",
        "output_key": "sentiment_report",
        "instruction": "Write the Sentiment Analyst report from the social evidence only; summarize social evidence instead of dumping raw feeds.",
    },
    "news_analyst_task.md": {
        "skill": "tradingagents-news-analyst",
        "output_key": "news_report",
        "instruction": "Codex must write the News Analyst report. Do not let Python classify likely effect; reason item by item. Treat political-trading or celebrity-trading headlines as low relevance unless they directly affect company fundamentals, regulation, price action, or sentiment.",
    },
    "fundamentals_analyst_task.md": {
        "skill": "tradingagents-fundamentals-analyst",
        "output_key": "fundamentals_report",
        "instruction": "Write the Fundamentals Analyst report from fundamentals evidence only.",
    },
    "financial_report_task.md": {
        "skill": "tradingagents-financial-report-analyst",
        "output_key": "financial_report",
        "instruction": "Read the structured fundamentals packet plus market-aware financial document packet: section-level 10-K/10-Q records and 8-K Exhibit 99.1 for US tickers; ASX announcements, annual reports, Appendix 4E/4D, results presentations, and investor materials for ASX tickers. Write financial_report.md with a claim-source table and cite the source section supporting each substantive claim. Python must not classify themes or financial-report conclusions. If a needed section or exhibit is unavailable, state the evidence gap.",
    },
    "industry_theme_discovery_task.md": {
        "skill": "tradingagents-industry-theme-discovery-analyst",
        "output_key": "industry_theme_report",
        "instruction": "Discover current industry themes and subthemes from the evidence, current online research packet, filings, and investor materials when available. Do not force-fit a preconfigured taxonomy. Python must not classify themes or financial-report conclusions. If online sources or filings are unavailable, state the evidence gap.",
    },
    "bull_researcher_round_1_task.md": {
        "skill": "tradingagents-bull-researcher",
        "output_key": "bull_researcher_round_1",
        "instruction": "Write the strongest evidence-backed Bull case. Cite the strongest supporting evidence, identify falsification conditions, and directly answer Bear's strongest available argument when prior Bear output exists.",
    },
    "bear_researcher_round_1_task.md": {
        "skill": "tradingagents-bear-researcher",
        "output_key": "bear_researcher_round_1",
        "instruction": "Write the strongest evidence-backed Bear case. Cite the strongest negative evidence, identify falsification conditions, and directly answer Bull's strongest argument.",
    },
    "research_manager_task.md": {
        "skill": "tradingagents-research-manager",
        "output_key": "research_manager",
        "instruction": "Weigh the completed analyst reports, Financial Report Analyst report, Industry / Theme Discovery Analyst report, and Bull/Bear debate; do not rely on Python-generated investment reasoning.",
    },
    "trader_task.md": {
        "skill": "tradingagents-trader",
        "output_key": "trader",
        "instruction": "Translate the Research Manager plan into a paper Trader Proposal with a matching FINAL TRANSACTION PROPOSAL line. For Buy or Sell, include a labelled Paper-study price framework with reference price or entry zone, invalidation level, and first confirmation or target level.",
    },
    "aggressive_risk_round_1_task.md": {
        "skill": "tradingagents-aggressive-risk-analyst",
        "output_key": "aggressive_risk_round_1",
        "instruction": "Write the aggressive risk view, focused on opportunity asymmetry and catalysts, while acknowledging concrete failure points.",
    },
    "conservative_risk_round_1_task.md": {
        "skill": "tradingagents-conservative-risk-analyst",
        "output_key": "conservative_risk_round_1",
        "instruction": "Write the conservative risk view, focused on downside, drawdown, valuation, liquidity, and evidence gaps; directly challenge unsupported upside assumptions.",
    },
    "neutral_risk_round_1_task.md": {
        "skill": "tradingagents-neutral-risk-analyst",
        "output_key": "neutral_risk_round_1",
        "instruction": "Compare the aggressive and conservative risk arguments by evidence quality. Do not force a compromise when the evidence is one-sided.",
    },
    "portfolio_manager_task.md": {
        "skill": "tradingagents-portfolio-manager",
        "output_key": "portfolio_manager",
        "instruction": "Synthesize the trader proposal and risk debate into the final paper portfolio decision.",
    },
    "complete_report_task.md": {
        "skill": "tradingagents-run-persistence",
        "output_key": "complete_report",
        "instruction": "Assemble complete_report.md from Codex-written role reports and run the hard contract validator.",
    },
    "quality_reviewer_task.md": {
        "skill": "tradingagents-quality-reviewer",
        "output_key": "quality_review",
        "instruction": "Review complete_report.md, role reports, evidence summary, and structured evidence files; write quality_review.md and quality_gate.json. Flag political-trading or celebrity-trading news that is treated as material without a direct company impact path. Do not pass review-grade completion when all news article cards are snippet-only, extracted MD&A is unavailable, an earnings 8-K has only cover-page evidence without Exhibit 99.1 or equivalent, or no cash-flow statement section is extracted.",
    },
}

GENERAL_EXPERT_WORKFLOW = """## Required Tool-Using Expert Workflow

1. Identify the role's evidence gap before writing conclusions.
2. Use the available tool outputs in the allowed input files first.
3. If a repeatable calculation, extraction, scoring, comparison, or validation is needed, use or request a Python tool instead of hand-waving.
4. Cite tool outputs and source files for every material claim.
5. State uncertainty and evidence gaps; do not replace missing evidence with assumptions or memory.
6. Include a `## Tool Outputs Used` section listing the concrete tools, source files, or upstream role outputs used.
7. Include an `## Evidence Gaps` section when source coverage is sparse, failed, or snippet-only.
"""

ROLE_EXPERT_REQUIREMENTS = {
    "tradingagents-market-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Quantitative Regime / Tool Outputs`

Use verified market snapshots, OHLCV data, moving averages, RSI, MACD, ATR, volume, and trend/regime evidence. Do not make template claims that conflict with actual indicator values.""",
    "tradingagents-sentiment-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- Social evidence processing table from the Sentiment Analyst skill.

Summarize social evidence only; do not paste full raw feeds or infer institutional sentiment from retail feeds.""",
    "tradingagents-news-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Article Evidence Cards`

For each material article card include: title, source, publication date, full-text status, direct company relevance, event type, key facts, novelty, materiality, likely effect, reason, confidence, and evidence gap. Keywords may support candidate discovery, not final impact judgment.""",
    "tradingagents-fundamentals-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Financial Statement Evidence`
- `## Sector-Specific Metrics`

Use sector-specific metrics where available; otherwise state the evidence gap instead of forcing a generic ratio template.""",
    "tradingagents-financial-report-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Claim-Source Table`

Every major claim must cite a source section or exhibit. Mark missing capex, guidance, segment, income statement, balance sheet, or cash-flow detail as an evidence gap.""",
    "tradingagents-research-manager": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Structured Evidence Matrix`

The matrix must compare Bull, Bear, market, sentiment, news, fundamentals, financial-report, and industry/theme evidence, including weight, confidence, and evidence gaps. Explain why Sell vs Hold vs Underweight wins when relevant.""",
    "tradingagents-bull-researcher": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Strongest Bull Evidence`
- `## Falsification Conditions`
- `## Response To Bear`

The Bull case must cite strongest evidence, avoid generic optimism, and define what would disprove the thesis.""",
    "tradingagents-bear-researcher": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Strongest Bear Evidence`
- `## Falsification Conditions`
- `## Response To Bull`

The Bear case must cite strongest evidence, avoid generic pessimism, and directly answer Bull's strongest argument.""",
    "tradingagents-trader": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Action Consistency Check`
- `## Paper-study price framework`
- `FINAL TRANSACTION PROPOSAL`

The final transaction proposal must match the reasoning and cite the Research Manager and market evidence used.""",
    "tradingagents-aggressive-risk-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Opportunity Case`
- `## Failure Points`

The aggressive case must identify upside asymmetry and concrete failure points.""",
    "tradingagents-conservative-risk-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Downside Case`
- `## Unsupported Upside Challenges`

The conservative case must challenge unsupported upside assumptions with evidence.""",
    "tradingagents-neutral-risk-analyst": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Risk Argument Quality`
- `## Stronger Risk Side`

The neutral case must compare argument quality and avoid forced compromise.""",
    "tradingagents-portfolio-manager": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Risk debate impact`
- `## Final Portfolio Decision`

The Portfolio Manager must state how the risk debate changed or confirmed the Trader proposal.""",
    "tradingagents-quality-reviewer": """Role-specific required sections:
- `## Tool Outputs Used`
- `## Quality Gate Findings`

Reject generic role text unsupported by tool outputs. ASX reports are not complete when ASX source collection fails; quality_gate.json must be failed until official ASX or investor-relations evidence is available or the gap is explicitly unresolved. For US reports, fail review-grade completion when structured evidence is only shallow: all news cards are snippet-only, extracted MD&A is unavailable, an earnings-related 8-K has no Exhibit 99.1 or equivalent earnings-release exhibit, or cash-flow statement sections are unavailable.""",
}

DEFAULT_OUTPUTS = {
    "financial_report": ("1_analysts", "financial_report.md"),
    "industry_theme_report": ("1_analysts", "industry_theme.md"),
    "quality_review": ("6_quality", "quality_review.md"),
    "quality_gate": ("6_quality", "quality_gate.json"),
}


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _workflow_paths(output_dir: Path) -> list[Path]:
    return sorted((output_dir / "evidence").glob("*/*/workflow_state.json"))


def _relative_or_absolute(path: str, base: Path) -> str:
    try:
        return str(Path(path).resolve().relative_to(base.resolve()))
    except ValueError:
        return str(Path(path))


def _evidence_brief(evidence: dict[str, Any]) -> str:
    identity = evidence.get("identity", {})
    roles = evidence.get("roles", {})
    role_lines = []
    for role, payload in sorted(roles.items()):
        tools = payload.get("tool_calls", {})
        role_lines.append(f"- {role}: {', '.join(sorted(tools)) or 'no tool calls recorded'}")
    return "\n".join(
        [
            f"- Company: {identity.get('company_name', evidence.get('ticker', 'N/A'))}",
            f"- Sector: {identity.get('sector', 'N/A')}",
            f"- Industry: {identity.get('industry', 'N/A')}",
            f"- Evidence roles: {len(roles)}",
            *role_lines,
        ]
    )


def _role_execution_contract_block(stage: dict[str, Any] | None) -> str:
    if not stage or "role_execution_contract" not in stage:
        return ""
    contract = json.dumps(stage["role_execution_contract"], indent=2)
    return f"""## RoleExecutionContract

```json
{contract}
```
"""


def _news_boundary_block(task: dict[str, str]) -> str:
    if task["skill"] != "tradingagents-news-analyst":
        return ""
    return """## News Analyst Evidence Boundaries

- Python candidate fields are not final investment judgments.
- Do not assign final impact labels without citing article evidence IDs.
- Snippet-only evidence cannot support high-confidence impact labels.
"""


def _financial_boundary_block(task: dict[str, str]) -> str:
    if task["skill"] != "tradingagents-financial-report-analyst":
        return ""
    return """## Financial Report Evidence Boundaries

- Python section records are not final financial judgments.
- Do not make major financial claims without section evidence IDs or explicit evidence gaps.
- Treat 8-K cover pages as source-routing evidence unless the cover page itself contains the cited fact.
- Prefer Exhibit 99.1 for earnings-release claims when available.
"""


def _market_boundary_block(task: dict[str, str]) -> str:
    if task["skill"] != "tradingagents-market-analyst":
        return ""
    return """## Market Analyst Evidence Boundaries

- Python metric observations are not final technical judgments.
- Do not make price-versus-moving-average claims without metric evidence IDs.
- Latest close, 10 EMA, 50 SMA, 200 SMA, RSI, MACD, ATR, and volume claims must match metric evidence.
- If metric evidence is missing, state the evidence gap instead of using template language.
"""


def _task_text(
    *,
    workflow: dict[str, Any],
    evidence: dict[str, Any],
    task_name: str,
    task: dict[str, str],
    repo_root: Path,
) -> str:
    output_path = _output_path_for(workflow, task["output_key"])
    evidence_path = workflow["evidence_path"]
    stage = _stage_for_output(workflow, output_path)
    allowed_input_files = stage.get("allowed_inputs", [evidence_path]) if stage else [evidence_path]
    forbidden_input_files = stage.get("forbidden_inputs", []) if stage else []
    allowed_memory_files = stage.get("allowed_memory_files", []) if stage else []
    forbidden_memory_roots = stage.get("forbidden_memory_roots", []) if stage else []
    memory_update_path = stage.get("memory_update_path", "") if stage else ""
    role_requirements = ROLE_EXPERT_REQUIREMENTS.get(task["skill"], "Role-specific required sections:\n- `## Tool Outputs Used`")
    role_execution_contract = _role_execution_contract_block(stage)
    news_boundary = _news_boundary_block(task)
    financial_boundary = _financial_boundary_block(task)
    market_boundary = _market_boundary_block(task)
    return f"""# Codex Report Task: {workflow['ticker']} {task_name.removesuffix('_task.md').replace('_', ' ').title()}

Ticker: `{workflow['ticker']}`
Trade date: `{workflow['trade_date']}`
Skill to use: `{task['skill']}`
Evidence file: `{_relative_or_absolute(evidence_path, repo_root)}`
Output file: `{_relative_or_absolute(output_path, repo_root)}`
Memory update file: `{_relative_or_absolute(memory_update_path, repo_root) if memory_update_path else ''}`

## Allowed Input Files

{_bullet_paths(allowed_input_files, repo_root)}

## Forbidden Input Files

{_bullet_paths(forbidden_input_files, repo_root) if forbidden_input_files else '- None declared.'}

## Allowed Memory Files

{_bullet_paths(allowed_memory_files, repo_root) if allowed_memory_files else '- None declared.'}

## Forbidden Memory Roots

{_bullet_paths(forbidden_memory_roots, repo_root) if forbidden_memory_roots else '- None declared.'}

## Instruction

{task['instruction']}

{GENERAL_EXPERT_WORKFLOW}

{role_requirements}

{role_execution_contract}

{news_boundary}

{financial_boundary}

{market_boundary}

## Evidence Brief

{_evidence_brief(evidence)}

## Boundaries

- Python prepared this task file only; it did not write investment reasoning.
- Codex must write the actual report output using the named skill.
- Read only the allowed input files.
- Read only the allowed memory files.
- Do not inspect other role memory.
- At the end, write a memory update for this role only.
- Memory must not override current evidence; if memory conflicts with current evidence, state the conflict explicitly.
- Python must not classify themes or financial-report conclusions.
- Keep raw feeds in evidence files unless the relevant skill explicitly asks for short representative examples.
- If online sources or filings are unavailable, state the evidence gap.
- Do not use as real trading advice.
- Do not connect to GCAF.

## Required Memory Update Footer

Every role output must end with:

```markdown
## Memory Update

* Durable facts to retain:
* Prior mistake to avoid:
* Open questions:
* Evidence references:
* Staleness / expiry:
```
"""


def _output_path_for(workflow: dict[str, Any], output_key: str) -> str:
    report_paths = workflow.get("report_paths", {})
    if output_key in report_paths:
        return str(report_paths[output_key])
    report_dir = Path(workflow.get("report_dir") or Path(report_paths["complete_report"]).parent)
    if output_key in DEFAULT_OUTPUTS:
        folder, filename = DEFAULT_OUTPUTS[output_key]
        return str(report_dir / folder / filename)
    return str(report_dir / "tasks" / f"{output_key}.md")


def _stage_for_output(workflow: dict[str, Any], output_path: str) -> dict[str, Any] | None:
    resolved = str(Path(output_path))
    for stage in workflow.get("stages", []):
        if str(Path(stage.get("output_path", ""))) == resolved:
            return stage
    return None


def _bullet_paths(paths: list[str], repo_root: Path) -> str:
    return "\n".join(f"- `{_relative_or_absolute(path, repo_root)}`" for path in paths)


def prepare_tasks_for_workflow(workflow_path: Path, repo_root: Path) -> dict[str, Any]:
    workflow = _read_json(workflow_path)
    evidence = _read_json(Path(workflow["evidence_path"]))
    report_dir = Path(workflow.get("report_dir") or Path(workflow["report_paths"]["complete_report"]).parent)
    task_dir = report_dir / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)

    task_entries: dict[str, dict[str, str]] = {}
    for task_name, task in TASKS.items():
        task_path = task_dir / task_name
        output_path = _output_path_for(workflow, task["output_key"])
        stage = _stage_for_output(workflow, output_path)
        workflow_output_paths = {
            prior_stage.get("output_path", "")
            for prior_stage in workflow.get("stages", [])
            if prior_stage.get("output_path")
        }
        task_path.write_text(
            _task_text(
                workflow=workflow,
                evidence=evidence,
                task_name=task_name,
                task=task,
                repo_root=repo_root,
            ),
            encoding="utf-8",
        )
        task_entries[task_name] = {
            "stage": stage.get("stage", "") if stage else "",
            "skill": task["skill"],
            "output_key": task["output_key"],
            "path": _relative_or_absolute(str(task_path), repo_root),
            "output_path": _relative_or_absolute(output_path, repo_root),
            "dependency_inputs": [
                _relative_or_absolute(path, repo_root)
                for path in (
                    stage.get("allowed_inputs", [])
                    if stage
                    else []
                )
                if path in workflow_output_paths
            ],
            "allowed_input_files": [
                _relative_or_absolute(path, repo_root)
                for path in (_stage_for_output(workflow, _output_path_for(workflow, task["output_key"])) or {}).get(
                    "allowed_inputs", []
                )
            ],
            "forbidden_input_files": [
                _relative_or_absolute(path, repo_root)
                for path in (_stage_for_output(workflow, _output_path_for(workflow, task["output_key"])) or {}).get(
                    "forbidden_inputs", []
                )
            ],
            "allowed_memory_files": [
                _relative_or_absolute(path, repo_root)
                for path in (_stage_for_output(workflow, _output_path_for(workflow, task["output_key"])) or {}).get(
                    "allowed_memory_files", []
                )
            ],
            "completion_gate": stage.get("completion_gate", "") if stage else "",
            "required_output_sections": (
                stage.get("role_execution_contract", {}).get("required_output_sections", []) if stage else []
            ),
            "quality_gate": stage.get("role_execution_contract", {}).get("quality_gate", "") if stage else "",
        }

    manifest = {
        "ticker": workflow["ticker"],
        "trade_date": workflow["trade_date"],
        "evidence_path": _relative_or_absolute(workflow["evidence_path"], repo_root),
        "tasks": task_entries,
        "contract": "Task prompts only. Codex role execution writes reports.",
    }
    (task_dir / "task_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def prepare_tasks(output_dir: Path, repo_root: Path) -> list[dict[str, Any]]:
    paths = _workflow_paths(output_dir)
    if not paths:
        raise FileNotFoundError(f"No workflow_state.json files found under {output_dir}")
    return [prepare_tasks_for_workflow(path, repo_root) for path in paths]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare Codex role task prompts from collected TradingAgents evidence.")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)

    repo_root = Path.cwd()
    try:
        manifests = prepare_tasks(args.output_dir, repo_root)
    except Exception as exc:
        print(str(exc))
        return 1
    for manifest in manifests:
        print(f"{manifest['ticker']}: prepared Codex report tasks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
