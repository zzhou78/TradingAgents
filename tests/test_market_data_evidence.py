from __future__ import annotations

from codex_tradingagents_skillkit.scripts.market_data_evidence import build_market_data_evidence


def test_build_market_data_evidence_extracts_metrics_relations_and_ledger():
    tool_calls = {
        "get_verified_market_snapshot": {
            "status": "ok",
            "output": (
                "Latest close: 372.97\n"
                "10 EMA: 377.15\n"
                "50 SMA: 410.52\n"
                "200 SMA: 446.27\n"
                "RSI: 41.26\n"
                "MACD: -5.1\n"
                "ATR: 8.2\n"
                "Volume: 123456"
            ),
        },
        "get_indicators:atr": {
            "status": "error",
            "error": "indicator unavailable",
        },
    }

    result = build_market_data_evidence(
        ticker="MSFT",
        trade_date="2026-06-29",
        tool_calls=tool_calls,
        structured_output_path="runs/x/market/quantitative_observations.json",
        retrieval_time="2026-06-29T09:30:00+10:00",
    )

    observations = result["metric_observations"]
    ledger = result["ledger_entries"]
    by_metric = {observation["metric_name"]: observation for observation in observations}

    assert by_metric["latest_close"]["value"] == 372.97
    assert by_metric["sma_200"]["value"] == 446.27
    assert by_metric["latest_close_vs_sma_200"]["relation"] == "below"
    assert by_metric["latest_close_vs_sma_200"]["supports_claims"] == [
        "price relative to 200 SMA",
        "long-term trend support/resistance",
    ]
    assert by_metric["get_indicators:atr"]["status"] == "unavailable"
    assert by_metric["get_indicators:atr"]["confidence"] == "low"
    assert by_metric["latest_close"]["final_market_judgment"] == "pending_codex_interpretation"

    assert len(ledger) == len(observations)
    assert ledger[0]["role"] == "market_analyst"
    assert ledger[0]["tool_name"] == "market_data_evidence"
    assert ledger[0]["structured_output_path"].endswith("quantitative_observations.json")


def test_build_market_data_evidence_extracts_verified_snapshot_markdown_tables():
    result = build_market_data_evidence(
        ticker="AAPL",
        trade_date="2026-06-30",
        tool_calls={
            "get_verified_market_snapshot": {
                "status": "ok",
                "output": (
                    "## Verified market data snapshot for AAPL\n\n"
                    "- Requested analysis date: 2026-06-30\n"
                    "- Latest trading row used: 2026-06-29\n\n"
                    "### Latest verified OHLCV row\n\n"
                    "| Field | Value |\n|---|---:|\n"
                    "| Close | 281.74 |\n"
                    "| Volume | 66368400 |\n\n"
                    "### Verified technical indicators (latest row)\n\n"
                    "| Indicator | Value |\n|---|---:|\n"
                    "| close_10_ema | 289.33 |\n"
                    "| close_50_sma | 291.78 |\n"
                    "| close_200_sma | 269.35 |\n"
                    "| rsi | 39.91 |\n"
                    "| macd | -2.90 |\n"
                    "| atr | 8.18 |\n"
                ),
            }
        },
        structured_output_path="runs/x/market/quantitative_observations.json",
        retrieval_time="2026-06-30T09:30:00+10:00",
    )

    by_metric = {observation["metric_name"]: observation for observation in result["metric_observations"]}

    assert by_metric["latest_close"]["value"] == 281.74
    assert by_metric["latest_close"]["source_date"] == "2026-06-29"
    assert by_metric["ema_10"]["value"] == 289.33
    assert by_metric["sma_200"]["value"] == 269.35
    assert by_metric["latest_close_vs_sma_200"]["relation"] == "above"
    assert by_metric["latest_close_vs_sma_200"]["source_date"] == "2026-06-29"
