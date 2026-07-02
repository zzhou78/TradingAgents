from __future__ import annotations

import argparse
import re
from pathlib import Path


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _clean_value(value: str) -> str:
    return value.strip().strip("*` ").strip()


def _first_match(text: str, patterns: tuple[str, ...]) -> str:
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            return _clean_value(match.group(1))
    return ""


def _normalized_label(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().upper()


def _number(value: str) -> float | None:
    cleaned = value.replace(",", "").replace("$", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return None


def _field_values(report_dir: Path) -> dict[str, str]:
    manager = _read(report_dir / "2_research" / "manager.md")
    trader = _read(report_dir / "3_trading" / "trader.md")
    portfolio = _read(report_dir / "5_portfolio" / "decision.md")
    complete = _read(report_dir / "complete_report.md")
    return {
        "manager_recommendation": _first_match(
            manager,
            (
                r"\*\*Recommendation\*\*\s*:\s*([A-Za-z ]+)",
                r"\bRecommendation\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "complete_recommendation": _first_match(
            complete,
            (
                r"\*\*Recommendation\*\*\s*:\s*([A-Za-z ]+)",
                r"\bRecommendation\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "trader_action": _first_match(
            trader,
            (
                r"\*\*Action\*\*\s*:\s*([A-Za-z ]+)",
                r"\bAction\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "complete_action": _first_match(
            complete,
            (
                r"\*\*Action\*\*\s*:\s*([A-Za-z ]+)",
                r"\bAction\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "trader_final": _first_match(
            trader,
            (
                r"FINAL TRANSACTION PROPOSAL\s*:\s*\*\*([A-Za-z ]+)\*\*",
                r"FINAL TRANSACTION PROPOSAL\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "complete_final": _first_match(
            complete,
            (
                r"FINAL TRANSACTION PROPOSAL\s*:\s*\*\*([A-Za-z ]+)\*\*",
                r"FINAL TRANSACTION PROPOSAL\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "trader_reference_price": _first_match(
            trader,
            (
                r"\bReference price\s*:\s*\$?([0-9][0-9,.]*)",
                r"\breference price\s+\$?([0-9][0-9,.]*)",
            ),
        ),
        "complete_reference_price": _first_match(
            complete,
            (
                r"\bReference price\s*:\s*\$?([0-9][0-9,.]*)",
                r"\breference price\s+\$?([0-9][0-9,.]*)",
            ),
        ),
        "portfolio_rating": _first_match(
            portfolio,
            (
                r"\*\*Rating\*\*\s*:\s*([A-Za-z ]+)",
                r"\bRating\s*:\s*([A-Za-z ]+)",
            ),
        ),
        "complete_portfolio_rating": _first_match(
            complete,
            (
                r"\*\*Rating\*\*\s*:\s*([A-Za-z ]+)",
                r"\bRating\s*:\s*([A-Za-z ]+)",
            ),
        ),
    }


def _market_values(report_dir: Path) -> tuple[float | None, float | None]:
    market = _read(report_dir / "1_analysts" / "market.md")
    latest_close = _first_match(
        market,
        (
            r"\bLatest close\s*\|\s*\$?([0-9][0-9,.]*)",
            r"\bLatest close\s*[:|]\s*\$?([0-9][0-9,.]*)",
            r"\bClose\s*[:|]\s*\$?([0-9][0-9,.]*)",
        ),
    )
    sma_200 = _first_match(
        market,
        (
            r"\b200 SMA\s*\|\s*\$?([0-9][0-9,.]*)",
            r"\b200\s*SMA\s*[:|]\s*\$?([0-9][0-9,.]*)",
        ),
    )
    return _number(latest_close), _number(sma_200)


def _compare_label(
    errors: list[str],
    *,
    role_value: str,
    complete_value: str,
    message: str,
) -> None:
    if role_value and complete_value and _normalized_label(role_value) != _normalized_label(complete_value):
        errors.append(f"{message}: role={role_value}; complete_report={complete_value}")


def _market_language_errors(report_dir: Path) -> list[str]:
    latest_close, sma_200 = _market_values(report_dir)
    if latest_close is None or sma_200 is None:
        return []
    complete = _read(report_dir / "complete_report.md")
    if latest_close < sma_200 and re.search(
        r"above\s+(?:the\s+)?200\s*SMA|long-term support intact|200\s*SMA points to long-term support",
        complete,
        re.IGNORECASE,
    ):
        return ["market-regime language contradicts Market Analyst report: complete_report describes 200 SMA support while market report shows price below 200 SMA"]
    if latest_close > sma_200 and re.search(r"below\s+(?:the\s+)?200\s*SMA|long-term support is not intact", complete, re.IGNORECASE):
        return ["market-regime language contradicts Market Analyst report: complete_report describes price below 200 SMA while market report shows price above 200 SMA"]
    return []


def validate_report_dir(report_dir: Path) -> list[str]:
    values = _field_values(report_dir)
    errors: list[str] = []
    _compare_label(
        errors,
        role_value=values["manager_recommendation"],
        complete_value=values["complete_recommendation"],
        message="Research Manager recommendation mismatch",
    )
    _compare_label(
        errors,
        role_value=values["trader_action"],
        complete_value=values["complete_action"],
        message="Trader action mismatch",
    )
    _compare_label(
        errors,
        role_value=values["trader_final"],
        complete_value=values["complete_final"],
        message="FINAL TRANSACTION PROPOSAL mismatch",
    )
    _compare_label(
        errors,
        role_value=values["portfolio_rating"],
        complete_value=values["complete_portfolio_rating"],
        message="Portfolio Manager rating mismatch",
    )
    trader_reference_price = _number(values["trader_reference_price"])
    complete_reference_price = _number(values["complete_reference_price"])
    if (
        trader_reference_price is not None
        and complete_reference_price is not None
        and abs(trader_reference_price - complete_reference_price) > 0.005
    ):
        errors.append(
            "Trader reference price mismatch: "
            f"role={trader_reference_price:.2f}; complete_report={complete_reference_price:.2f}"
        )
    errors.extend(_market_language_errors(report_dir))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate complete_report.md against role outputs.")
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args(argv)

    errors = validate_report_dir(args.report_dir)
    if errors:
        print("Complete report role consistency validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Complete report role consistency validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
