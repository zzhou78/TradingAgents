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


def _write_fixture(tmp_path: Path, article_cards: list[dict[str, object]]) -> tuple[Path, Path]:
    report_dir = tmp_path / "reports" / "MSFT" / "2026-06-30"
    evidence_dir = tmp_path / "evidence" / "MSFT" / "2026-06-30"
    (report_dir / "1_analysts").mkdir(parents=True)
    (evidence_dir / "news").mkdir(parents=True)
    (report_dir / "1_analysts" / "news.md").write_text(
        "## Tool Outputs Used\n\n"
        "## Article Evidence Cards\n\n"
        "## News Impact Summary\n\n"
        "Neutral impact from news:MSFT:2026-06-30:001.\n",
        encoding="utf-8",
    )
    (evidence_dir / "news" / "source_attempts.json").write_text(
        json.dumps(
            [
                {
                    "adapter": "company_ir_adapter",
                    "status": "available",
                    "items_found": 1,
                    "limitations": [],
                    "fallback_used": False,
                }
            ]
        ),
        encoding="utf-8",
    )
    (evidence_dir / "news" / "article_cards.json").write_text(json.dumps(article_cards), encoding="utf-8")
    evidence_path = evidence_dir / "evidence.json"
    evidence_path.write_text(json.dumps({"ticker": "MSFT", "trade_date": "2026-06-30"}), encoding="utf-8")
    return report_dir, evidence_path


def test_quality_gate_rejects_error_page_as_verified_full_text(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir, evidence_path = _write_fixture(
        tmp_path,
        [
            {
                "evidence_id": "news:MSFT:2026-06-30:001",
                "text_status": "error_page",
                "full_text_status": "full_text",
                "content_quality_score": 8,
                "confidence": "medium",
                "as_of_validity": {"valid_for_trade_date": True},
            }
        ],
    )

    errors = validator.validate_report_dir(report_dir, evidence_path)

    assert any("weak or blocked news article is treated as full text" in error for error in errors)


def test_quality_gate_rejects_post_trade_article_as_valid(tmp_path: Path):
    validator = _load_quality_validator()
    report_dir, evidence_path = _write_fixture(
        tmp_path,
        [
            {
                "evidence_id": "news:MSFT:2026-06-30:001",
                "text_status": "full_text_verified",
                "full_text_status": "full_text",
                "content_quality_score": 90,
                "confidence": "medium",
                "as_of_validity": {"valid_for_trade_date": False},
                "limitations": [],
            }
        ],
    )

    errors = validator.validate_report_dir(report_dir, evidence_path)

    assert any("post-trade-date news article cannot support review-grade evidence" in error for error in errors)
