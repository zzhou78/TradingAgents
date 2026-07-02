from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
QUALITY_VALIDATOR = BUNDLE / "scripts" / "validate_quality_review.py"


def _load_quality_validator():
    spec = importlib.util.spec_from_file_location("validate_quality_review", QUALITY_VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sentiment_report_cannot_rely_only_on_raw_platform_counts(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    analyst_dir = report_dir / "1_analysts"
    analyst_dir.mkdir(parents=True)
    (analyst_dir / "sentiment.md").write_text(
        "# Sentiment\n\n"
        "## Tool Outputs Used\n\n- social_evidence_processing\n\n"
        "## Social Evidence Processing Rules\n\n"
        "| Source | Items reviewed | Usable ticker-relevant items | Bullish / bearish / neutral split | Confidence |\n"
        "|---|---:|---:|---|---|\n"
        "| StockTwits | 10 | 10 | 9 / 0 / 1 | high |\n\n"
        "Final sentiment is bullish because 90% of platform labels are bullish.\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert any("sentiment conclusion is based only on raw social counts" in error for error in errors)


def test_social_card_quality_blocks_medium_confidence_when_items_are_low_quality(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    evidence_dir = tmp_path / "evidence" / "MSFT" / "2026-06-30"
    (report_dir / "1_analysts").mkdir(parents=True)
    (evidence_dir / "social").mkdir(parents=True)
    (evidence_dir / "social" / "social_cards.json").write_text(
        json.dumps(
            [
                {
                    "evidence_id": "social:MSFT:2026-06-30:item:0001",
                    "ticker_relevance": "direct_company",
                    "reasoning_quality": "low",
                    "meme_or_joke": True,
                    "platform_label": "bullish",
                    "as_of_validity": {"valid_for_trade_date": True},
                }
            ]
        ),
        encoding="utf-8",
    )
    (evidence_dir / "social" / "social_summary.json").write_text(
        json.dumps(
            {
                "sources": [
                    {
                        "source": "fetch_stocktwits_messages",
                        "usable_ticker_relevant_items": 1,
                        "confidence": "medium",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "MSFT", "trade_date": "2026-06-30"}), encoding="utf-8")

    errors = validator.validate_report_dir(report_dir, evidence_path)

    assert any("sentiment source confidence is unsupported by social item quality" in error for error in errors)


def test_top_reasoned_items_cannot_include_low_reasoning_quality(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir = tmp_path / "reports" / "MSFT" / "2026-07-02"
    analyst_dir = report_dir / "1_analysts"
    analyst_dir.mkdir(parents=True)
    (analyst_dir / "sentiment.md").write_text(
        "# Sentiment\n\n"
        "## Tool Outputs Used\n\n- social_evidence_processing\n\n"
        "## Top Reasoned Items\n"
        "| Evidence ID | Source | Candidate label | Reasoning quality | Relevance |\n"
        "|---|---|---|---|---|\n"
        "| social:MSFT:2026-07-02:item:0001 | stocktwits | bullish | low | direct_company |\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert any("Top Reasoned Items cannot include low reasoning-quality" in error for error in errors)


def test_quality_review_cannot_say_validator_pending_when_gate_passed(tmp_path: Path):
    validator = _load_quality_validator()
    run_dir = tmp_path / "run"
    report_dir = run_dir / "reports" / "MSFT" / "2026-07-02"
    quality_dir = report_dir / "6_quality"
    quality_dir.mkdir(parents=True)
    (run_dir / "closed_loop_status.json").write_text(
        json.dumps({"status": "review_ready_paper_study"}),
        encoding="utf-8",
    )
    (quality_dir / "quality_gate.json").write_text(
        json.dumps(
            {
                "passed": True,
                "status": "workflow_complete",
                "issues": [],
                "closed_loop_status_path": str(run_dir / "closed_loop_status.json"),
            }
        ),
        encoding="utf-8",
    )
    (quality_dir / "quality_review.md").write_text(
        "# Quality Review\n\n## Evidence Gaps\n\n- Validator must still be run after file generation.\n",
        encoding="utf-8",
    )

    errors = validator.validate_report_dir(report_dir)

    assert any("quality_review.md says validator is pending" in error for error in errors)
