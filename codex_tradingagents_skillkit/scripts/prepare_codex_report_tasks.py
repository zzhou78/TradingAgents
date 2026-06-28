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
        "instruction": "Read the structured fundamentals packet plus section-level 10-K/10-Q records, 8-K cover pages, Exhibit 99.1 earnings releases, investor materials, and management commentary. Write financial_report.md with a claim-source table and cite the source section supporting each substantive claim. Python must not classify themes or financial-report conclusions. If a needed section or exhibit is unavailable, state the evidence gap.",
    },
    "industry_theme_discovery_task.md": {
        "skill": "tradingagents-industry-theme-discovery-analyst",
        "output_key": "industry_theme_report",
        "instruction": "Discover current industry themes and subthemes from the evidence, current online research packet, filings, and investor materials when available. Do not force-fit a preconfigured taxonomy. Python must not classify themes or financial-report conclusions. If online sources or filings are unavailable, state the evidence gap.",
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
        "instruction": "Review complete_report.md, role reports, and evidence summary; write quality_review.md and quality_gate.json. Flag political-trading or celebrity-trading news that is treated as material without a direct company impact path.",
    },
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
    return f"""# Codex Report Task: {workflow['ticker']} {task_name.removesuffix('_task.md').replace('_', ' ').title()}

Ticker: `{workflow['ticker']}`
Trade date: `{workflow['trade_date']}`
Skill to use: `{task['skill']}`
Evidence file: `{_relative_or_absolute(evidence_path, repo_root)}`
Output file: `{_relative_or_absolute(output_path, repo_root)}`

## Instruction

{task['instruction']}

## Evidence Brief

{_evidence_brief(evidence)}

## Boundaries

- Python prepared this task file only; it did not write investment reasoning.
- Codex must write the actual report output using the named skill.
- Python must not classify themes or financial-report conclusions.
- Keep raw feeds in evidence files unless the relevant skill explicitly asks for short representative examples.
- If online sources or filings are unavailable, state the evidence gap.
- Do not use as real trading advice.
- Do not connect to GCAF.
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


def prepare_tasks_for_workflow(workflow_path: Path, repo_root: Path) -> dict[str, Any]:
    workflow = _read_json(workflow_path)
    evidence = _read_json(Path(workflow["evidence_path"]))
    report_dir = Path(workflow.get("report_dir") or Path(workflow["report_paths"]["complete_report"]).parent)
    task_dir = report_dir / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)

    task_entries: dict[str, dict[str, str]] = {}
    for task_name, task in TASKS.items():
        task_path = task_dir / task_name
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
            "skill": task["skill"],
            "output_key": task["output_key"],
            "path": _relative_or_absolute(str(task_path), repo_root),
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
