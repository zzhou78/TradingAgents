from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
MODULE_PATH = BUNDLE / "scripts" / "financial_document_sources.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("financial_document_sources", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sec_sources_are_filtered_to_trade_date_and_include_excerpts():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if url.endswith("/company_tickers.json"):
            return json.dumps(
                {
                    "0": {
                        "cik_str": 789019,
                        "ticker": "MSFT",
                        "title": "MICROSOFT CORP",
                    }
                }
            )
        if url.endswith("/CIK0000789019.json"):
            return json.dumps(
                {
                    "filings": {
                        "recent": {
                            "accessionNumber": [
                                "0000789019-26-000999",
                                "0000789019-26-000123",
                                "0000789019-26-000122",
                                "0000789019-25-000101",
                            ],
                            "filingDate": [
                                "2026-07-01",
                                "2026-04-24",
                                "2026-04-23",
                                "2025-07-30",
                            ],
                            "form": ["10-Q", "8-K", "10-Q", "10-K"],
                            "primaryDocument": [
                                "msft-20260701.htm",
                                "msft-20260424.htm",
                                "msft-20260331.htm",
                                "msft-20250630.htm",
                            ],
                            "primaryDocDescription": [
                                "Quarterly report after the trade date",
                                "Earnings release exhibit",
                                "Quarterly report",
                                "Annual report",
                            ],
                        }
                    }
                }
            )
        if "msft-20260331.htm" in url:
            return "<html><body>Quarterly report revenue increased and operating margin expanded.</body></html>"
        if "msft-20250630.htm" in url:
            return "<html><body>Annual report risk factors discuss cloud demand and AI infrastructure.</body></html>"
        if "msft-20260424.htm" in url:
            return "<html><body>Earnings release reported cloud growth and guidance commentary.</body></html>"
        raise AssertionError(f"unexpected URL: {url}")

    packet = module.collect_financial_document_sources(
        "MSFT",
        "2026-06-27",
        http_get=fake_http_get,
        excerpt_chars=120,
    )

    assert packet["status"] == "ok"
    assert packet["cik"] == "0000789019"
    assert requested_urls[0].endswith("/company_tickers.json")
    assert not any("20260701" in url for url in requested_urls)

    sources = {source["source_type"]: source for source in packet["sources"]}
    assert sources["annual_report_10k"]["filing_date"] == "2025-07-30"
    assert sources["quarterly_report_10q"]["filing_date"] == "2026-04-23"
    assert sources["earnings_release_8k"]["filing_date"] == "2026-04-24"
    assert sources["investor_presentation"]["status"] == "unavailable"
    assert "https://www.sec.gov/Archives/edgar/data/789019/" in sources["quarterly_report_10q"]["url"]
    assert "cloud growth" in sources["earnings_release_8k"]["excerpt"]
    assert "2026-07-01" not in module.render_financial_document_packet(packet)


def test_non_us_tickers_record_document_gap_without_sec_lookup():
    module = _load_module()

    packet = module.collect_financial_document_sources(
        "CBA.AX",
        "2026-06-27",
        http_get=lambda url, headers: (_ for _ in ()).throw(AssertionError(url)),
    )

    assert packet["status"] == "unavailable"
    assert packet["sources"][0]["source_type"] == "sec_filings"
    assert "not a plain US exchange ticker" in packet["sources"][0]["reason"]


def test_generic_8k_is_not_mislabeled_as_earnings_release():
    module = _load_module()

    submissions = {
        "filings": {
            "recent": {
                "accessionNumber": [
                    "0000789019-26-000200",
                    "0000789019-26-000100",
                ],
                "filingDate": ["2026-06-05", "2026-04-24"],
                "form": ["8-K", "8-K"],
                "primaryDocument": ["governance.htm", "earnings.htm"],
                "primaryDocDescription": ["Current report", "Current report"],
            }
        }
    }

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if url.endswith("/company_tickers.json"):
            return json.dumps({"0": {"cik_str": 789019, "ticker": "MSFT", "title": "MICROSOFT CORP"}})
        if url.endswith("/CIK0000789019.json"):
            return json.dumps(submissions)
        if "governance.htm" in url:
            return "<html>Item 5.02 Director departure and board update.</html>"
        if "earnings.htm" in url:
            return "<html>Item 2.02 Results of Operations and Financial Condition. Revenue grew.</html>"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources(
        "MSFT",
        "2026-06-27",
        http_get=fake_http_get,
    )

    earnings = next(source for source in packet["sources"] if source["source_type"] == "earnings_release_8k")
    assert earnings["status"] == "available"
    assert earnings["filing_date"] == "2026-04-24"
    assert "earnings.htm" in earnings["url"]
