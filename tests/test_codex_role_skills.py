from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".codex" / "skills"

EXPECTED_ROLE_SKILLS = [
    "tradingagents-market-analyst",
    "tradingagents-sentiment-analyst",
    "tradingagents-news-analyst",
    "tradingagents-fundamentals-analyst",
    "tradingagents-financial-report-analyst",
    "tradingagents-industry-theme-discovery-analyst",
    "tradingagents-bull-researcher",
    "tradingagents-bear-researcher",
    "tradingagents-research-manager",
    "tradingagents-trader",
    "tradingagents-aggressive-risk-analyst",
    "tradingagents-conservative-risk-analyst",
    "tradingagents-neutral-risk-analyst",
    "tradingagents-portfolio-manager",
]


def _frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n")
    _, raw, _ = text.split("---\n", 2)
    parsed = {}
    for line in raw.splitlines():
        key, value = line.split(":", 1)
        parsed[key.strip()] = value.strip().strip('"')
    return parsed


def test_all_tradingagents_role_skills_exist():
    missing = [
        name
        for name in EXPECTED_ROLE_SKILLS
        if not (SKILLS_ROOT / name / "SKILL.md").exists()
    ]
    assert missing == []


def test_role_skills_are_self_contained_and_discoverable():
    for name in EXPECTED_ROLE_SKILLS:
        skill_path = SKILLS_ROOT / name / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        fm = _frontmatter(text)

        assert fm["name"] == name
        assert fm["description"].startswith("Use when")
        assert len(fm["description"]) <= 500
        assert "TODO" not in text

        for required in [
            "Source files scanned:",
            "Inputs:",
            "Procedure:",
            "Output:",
            "Safety boundaries:",
        ]:
            assert required in text, f"{required} missing from {name}"

        assert "Do not use as real trading advice." in text
        assert "Do not connect to GCAF." in text


def test_trader_skill_keeps_safety_boundary_out_of_action_rationale():
    text = (SKILLS_ROOT / "tradingagents-trader" / "SKILL.md").read_text(encoding="utf-8")

    assert "Safety boundaries must not change the Buy / Hold / Sell action." in text
    assert "Do not cite paper-study status as a reason to avoid Buy or Sell." in text
    assert "The action rationale must come from market evidence, research manager input, and risk evidence." in text
