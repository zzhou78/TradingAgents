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


def test_10k_and_10q_sources_extract_named_financial_sections():
    module = _load_module()

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if url.endswith("/company_tickers.json"):
            return json.dumps({"0": {"cik_str": 789019, "ticker": "MSFT", "title": "MICROSOFT CORP"}})
        if url.endswith("/CIK0000789019.json"):
            return json.dumps(
                {
                    "filings": {
                        "recent": {
                            "accessionNumber": [
                                "0000789019-26-000200",
                                "0000789019-25-000100",
                            ],
                            "filingDate": ["2026-04-29", "2025-07-30"],
                            "form": ["10-Q", "10-K"],
                            "primaryDocument": ["msft-20260331.htm", "msft-20250630.htm"],
                            "primaryDocDescription": ["Quarterly report", "Annual report"],
                        }
                    }
                }
            )
        if "msft-20250630.htm" in url:
            return """
            <html><body>
            Item 1. Business Annual business overview cloud and AI platform.
            Segment Information Productivity, Intelligent Cloud, and More Personal Computing.
            Segment Revenue Productivity revenue, Intelligent Cloud revenue, and More Personal Computing revenue.
            Item 1A. Risk Factors Competition, regulation, and infrastructure risk.
            Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations.
            Liquidity and Capital Resources Cash, investments, and debt maturity discussion.
            Commitments and Contractual Obligations Data center leases and purchase obligations.
            Item 7A. Quantitative and Qualitative Disclosures About Market Risk.
            </body></html>
            """
        if "msft-20260331.htm" in url:
            return """
            <html><body>
            Item 2. Management's Discussion and Analysis of Financial Condition and Results of Operations.
            Revenue increased due to cloud services.
            Segment Information Intelligent Cloud revenue accelerated.
            Segment revenue, cost of revenue, operating expenses, and operating income were as follows.
            Productivity, Intelligent Cloud, and More Personal Computing table.
            Liquidity and Capital Resources Cash and short-term investments declined.
            Capital Expenditures Data center investment increased.
            Item 3. Quantitative and Qualitative Disclosures About Market Risk.
            </body></html>
            """
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("MSFT", "2026-06-27", http_get=fake_http_get)
    sources = {source["source_type"]: source for source in packet["sources"]}

    annual_sections = {section["section_type"]: section for section in sources["annual_report_10k"]["sections"]}
    quarterly_sections = {section["section_type"]: section for section in sources["quarterly_report_10q"]["sections"]}

    assert "business_overview" in annual_sections
    assert "risk_factors" in annual_sections
    assert "mda" in annual_sections
    assert "segment_information" in annual_sections
    assert "segment_product_revenue_tables" in annual_sections
    assert "liquidity_and_capital_resources" in annual_sections
    assert "commitments_capex_contractual_obligations" in annual_sections
    assert annual_sections["business_overview"]["section_name"] == "10-K business overview"
    assert annual_sections["business_overview"]["status"] == "available"
    assert annual_sections["business_overview"]["source_type"] == "annual_report_10k"
    assert annual_sections["business_overview"]["filing_date"] == "2025-07-30"
    assert annual_sections["business_overview"]["url"].endswith("/msft-20250630.htm")
    assert "revenue drivers" in annual_sections["business_overview"]["supports_claims"]
    assert "cloud and AI platform" in annual_sections["business_overview"]["excerpt"]
    assert annual_sections["segment_product_revenue_tables"]["section_name"] == "10-K segment/product revenue tables"
    assert "Productivity revenue" in annual_sections["segment_product_revenue_tables"]["excerpt"]
    assert "revenue" in annual_sections["income_statement"]["supports_claims"]
    assert annual_sections["income_statement"]["status"] == "unavailable"

    assert "mda" in quarterly_sections
    assert quarterly_sections["business_overview"]["status"] == "unavailable"
    assert "segment_information" in quarterly_sections
    assert "segment_product_revenue_tables" in quarterly_sections
    assert "liquidity_and_capital_resources" in quarterly_sections
    assert "commitments_capex_contractual_obligations" in quarterly_sections
    assert quarterly_sections["mda"]["section_name"] == "10-Q MD&A"
    assert "cloud services" in quarterly_sections["mda"]["excerpt"]
    assert "Segment revenue, cost of revenue" in quarterly_sections["segment_product_revenue_tables"]["excerpt"]
    assert quarterly_sections["cash_flow_statement"]["status"] == "unavailable"


def test_earnings_8k_follows_exhibit_991_and_distinguishes_cover_page():
    module = _load_module()

    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if url.endswith("/company_tickers.json"):
            return json.dumps({"0": {"cik_str": 789019, "ticker": "MSFT", "title": "MICROSOFT CORP"}})
        if url.endswith("/CIK0000789019.json"):
            return json.dumps(
                {
                    "filings": {
                        "recent": {
                            "accessionNumber": ["0000789019-26-000100"],
                            "filingDate": ["2026-04-29"],
                            "form": ["8-K"],
                            "primaryDocument": ["msft-20260429.htm"],
                            "primaryDocDescription": ["Current report"],
                        }
                    }
                }
            )
        if url.endswith("-index.html"):
            return '<html><a href="/Archives/edgar/data/789019/000078901926000100/ex991.htm">EX-99.1</a></html>'
        if "msft-20260429.htm" in url:
            return """
            <html><body>
            FORM 8-K cover page.
            Item 2.02. Results of Operations and Financial Condition.
            A press release is furnished as Exhibit 99.1.
            </body></html>
            """
        if "ex991.htm" in url:
            return """
            <html><body>
            Exhibit 99.1 Microsoft Cloud revenue increased and operating income expanded.
            Segment results include Productivity and Business Processes and Intelligent Cloud.
            </body></html>
            """
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("MSFT", "2026-06-27", http_get=fake_http_get)
    earnings = next(source for source in packet["sources"] if source["source_type"] == "earnings_release_8k")

    assert earnings["cover_page"]["status"] == "available"
    assert "FORM 8-K cover page" in earnings["cover_page"]["excerpt"]
    assert earnings["exhibit_99_1"]["status"] == "available"
    assert earnings["exhibit_99_1"]["url"].endswith("/ex991.htm")
    assert "Cloud revenue increased" in earnings["exhibit_99_1"]["excerpt"]
    assert "ex991.htm" in "\n".join(requested_urls)
    rendered = module.render_financial_document_packet(packet)
    assert "### 8-K Cover Page: earnings_release_8k" in rendered
    assert "### Exhibit 99.1: earnings_release_8k" in rendered
    assert "- Status: `available`" in rendered


def test_earnings_8k_records_unavailable_exhibit_991_when_missing():
    module = _load_module()

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if url.endswith("/company_tickers.json"):
            return json.dumps({"0": {"cik_str": 789019, "ticker": "MSFT", "title": "MICROSOFT CORP"}})
        if url.endswith("/CIK0000789019.json"):
            return json.dumps(
                {
                    "filings": {
                        "recent": {
                            "accessionNumber": ["0000789019-26-000100"],
                            "filingDate": ["2026-04-29"],
                            "form": ["8-K"],
                            "primaryDocument": ["msft-20260429.htm"],
                            "primaryDocDescription": ["Current report"],
                        }
                    }
                }
            )
        if url.endswith("-index.html"):
            return '<html><a href="/Archives/edgar/data/789019/000078901926000100/ex101.htm">EX-101</a></html>'
        if "msft-20260429.htm" in url:
            return "<html>Item 2.02 Results of Operations and Financial Condition. Exhibit 99.1 furnished.</html>"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("MSFT", "2026-06-27", http_get=fake_http_get)
    earnings = next(source for source in packet["sources"] if source["source_type"] == "earnings_release_8k")

    assert earnings["cover_page"]["status"] == "available"
    assert earnings["exhibit_99_1"]["status"] == "unavailable"
    assert earnings["exhibit_99_1"]["url"] == ""
    assert "No Exhibit 99.1 link found" in earnings["exhibit_99_1"]["reason"]
    rendered = module.render_financial_document_packet(packet)
    assert "### Exhibit 99.1: earnings_release_8k" in rendered
    assert "- Status: `unavailable`" in rendered


def test_missing_financial_sections_are_recorded_as_evidence_gaps():
    module = _load_module()

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if url.endswith("/company_tickers.json"):
            return json.dumps({"0": {"cik_str": 789019, "ticker": "MSFT", "title": "MICROSOFT CORP"}})
        if url.endswith("/CIK0000789019.json"):
            return json.dumps(
                {
                    "filings": {
                        "recent": {
                            "accessionNumber": ["0000789019-26-000200"],
                            "filingDate": ["2026-04-29"],
                            "form": ["10-Q"],
                            "primaryDocument": ["msft-20260331.htm"],
                            "primaryDocDescription": ["Quarterly report"],
                        }
                    }
                }
            )
        if "msft-20260331.htm" in url:
            return "<html><body>Item 2. Management's Discussion and Analysis Revenue increased. Item 3.</body></html>"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("MSFT", "2026-06-27", http_get=fake_http_get)
    quarterly = next(source for source in packet["sources"] if source["source_type"] == "quarterly_report_10q")
    sections = {section["section_type"]: section for section in quarterly["sections"]}

    for section_type in [
        "commitments_capex_contractual_obligations",
        "segment_product_revenue_tables",
        "income_statement",
        "balance_sheet",
        "cash_flow_statement",
    ]:
        assert sections[section_type]["status"] == "unavailable"
        assert sections[section_type]["unavailable_reason"]
