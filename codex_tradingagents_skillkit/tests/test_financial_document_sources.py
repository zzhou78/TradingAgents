from __future__ import annotations

import importlib.util
import json
import sys
import types
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


def test_other_market_tickers_record_document_gap_without_sec_lookup():
    module = _load_module()

    packet = module.collect_financial_document_sources(
        "7203.T",
        "2026-06-27",
        http_get=lambda url, headers: (_ for _ in ()).throw(AssertionError(url)),
    )

    assert packet["status"] == "unavailable"
    assert packet["sources"][0]["source_type"] == "sec_filings"
    assert "No market-specific financial document collector exists" in packet["sources"][0]["reason"]


def test_asx_tickers_route_to_asx_announcement_collector_and_filter_trade_date():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "company/CBA/announcements" in url:
            return json.dumps(
                {
                    "data": [
                        {
                            "title": "Appendix 4E and 2026 Full Year Results",
                            "announcement_date": "2026-08-10",
                            "url": "https://asx.example/CBA-fy26.pdf",
                        },
                        {
                            "title": "2025 Annual Report",
                            "announcement_date": "2025-08-12",
                            "url": "https://asx.example/CBA-annual-report.pdf",
                        },
                        {
                            "title": "AGM Presentation",
                            "announcement_date": "2025-10-20",
                            "url": "https://asx.example/CBA-agm.pdf",
                        },
                    ]
                }
            )
        if url == "https://asx.example/CBA-annual-report.pdf":
            return (
                "Annual report revenue income NPAT EPS dividend per share operating cash flow "
                "cash debt CET1 segment NIM loan growth arrears impairment outlook dividend capex risks"
            )
        if url == "https://asx.example/CBA-agm.pdf":
            return "AGM presentation outlook dividend capital management"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("CBA.AX", "2026-06-27", http_get=fake_http_get)

    assert packet["status"] == "ok"
    assert packet["market"] == "ASX"
    assert packet["asx_code"] == "CBA"
    assert any("company/CBA/announcements" in url for url in requested_urls)
    assert not any("fy26" in url for url in requested_urls)
    sources = packet["sources"]
    assert [source["document_type"] for source in sources] == ["Annual Report", "AGM Presentation"]
    annual = sources[0]
    assert annual["announcement_date"] == "2025-08-12"
    assert annual["extraction_status"] == "available"
    assert annual["source_quality_tier"] == "tier_1_asx_lodged_pdf"
    assert annual["document_role"] == "annual_report"
    assert annual["metric_eligibility"] == "eligible_financial_document"
    assert annual["extracted_sections"]
    rendered = module.render_financial_document_packet(packet)
    assert "- Market: `ASX`" in rendered
    assert "Annual Report" in rendered
    assert "operating_cash_flow" in rendered


def test_asx_landing_page_source_is_discovery_only_and_emits_no_sector_metrics():
    module = _load_module()

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if "company/CBA/announcements" in url or "asx-research/1.0/companies/CBA/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/CBA" in url:
            return """
            <html><body>
            <a href="https://company.example/investors/results">2025 Annual Report 15 Aug 2025</a>
            </body></html>
            """
        if url == "https://company.example/investors/results":
            return """
            <html><body>
            <nav>Home Search Contact us Reports and presentations Downloads Read more</nav>
            <main>
            Archive of annual reports, results presentations, and shareholder services.
            Net interest margin 2.08% CET1 12.3% dividend 485 cents.
            </main>
            </body></html>
            """
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("CBA.AX", "2026-07-02", http_get=fake_http_get)

    source = packet["sources"][0]
    assert source["source_quality_tier"] in {
        "tier_4_company_ir_landing_page",
        "tier_5_navigation_or_archive_page",
    }
    assert source["document_role"] in {"landing_page", "archive_page"}
    assert source["metric_eligibility"] == "discovery_only"
    assert packet["metric_extraction_status"] == "no_eligible_financial_sources"
    assert not [
        section
        for section in source["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    ]


def test_asx_metric_extraction_ranks_later_financial_candidate_over_first_navigation_hit():
    module = _load_module()

    document_text = (
        "Annual report operating and financial review cash flow statement. "
        "Contents 1 Net interest margin 2 CET1 3 Loan growth 4 Financial statements. "
        + " ".join(f"archive item {index}" for index in range(60))
        + " Operating review. Net interest margin 2.05% increased by 9 bps on FY24."
    )

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if "companies/CBA/announcements" in url:
            return json.dumps(
                {
                    "data": [
                        {
                            "title": "2025 Annual Report",
                            "announcement_date": "2025-08-15",
                            "url": "https://asx.example/CBA-annual-report.pdf",
                        }
                    ]
                }
            )
        if url == "https://asx.example/CBA-annual-report.pdf":
            return document_text
        raise AssertionError(url)

    packet = module.collect_financial_document_sources(
        "CBA.AX",
        "2026-07-02",
        http_get=fake_http_get,
        excerpt_chars=180,
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["net_interest_margin"]["metric_value_status"] == "value_extracted"
    assert sections["net_interest_margin"]["clean_metric_value"] == "2.05"
    assert sections["net_interest_margin"]["source_quality_tier"] == "tier_1_asx_lodged_pdf"
    assert sections["net_interest_margin"]["document_role"] == "annual_report"
    assert sections["net_interest_margin"]["source_page"] == "1"
    assert sections["net_interest_margin"]["metric_label_value_distance_tokens"] <= 3
    assert sections["net_interest_margin"]["section_title"] == "management_discussion_analysis"


def test_asx_collector_supports_current_markit_company_announcements_schema():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "asx-research/1.0/companies/WOW/announcements" in url:
            return json.dumps(
                {
                    "data": {
                        "displayName": "WOOLWORTHS GROUP LIMITED",
                        "items": [
                            {
                                "headline": "2026 Annual Report",
                                "date": "2026-08-20T08:00:00.000Z",
                                "documentKey": "post-trade-date",
                                "announcementType": "PERIODIC REPORTS",
                            },
                            {
                                "headline": "2025 Annual Report",
                                "date": "2025-08-28T08:00:00.000Z",
                                "documentKey": "annual-report-key",
                                "announcementType": "PERIODIC REPORTS",
                            },
                        ],
                    }
                }
            )
        if "asx-research/1.0/file/annual-report-key" in url:
            return "Annual report revenue income NPAT operating cash flow cash debt segment sales outlook capex risks"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("WOW.AX", "2026-06-27", http_get=fake_http_get)

    assert packet["status"] == "ok"
    assert any("asx-research/1.0/companies/WOW/announcements" in url for url in requested_urls)
    assert any("asx-research/1.0/file/annual-report-key" in url for url in requested_urls)
    assert not any("post-trade-date" in url for url in requested_urls)
    assert packet["sources"][0]["title"] == "2025 Annual Report"
    assert packet["sources"][0]["url"].endswith("/file/annual-report-key")
    assert packet["sources"][0]["extraction_status"] == "available"
    assert packet["sources"][0]["extracted_sections"]


def test_asx_collector_tries_official_and_ir_fallback_pages_when_endpoint_fails():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "company/BHP/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/BHP" in url:
            return """
            <html><body>
            <a href="https://asx.example/BHP-annual-report.pdf">2025 Annual Report 15 Aug 2025</a>
            </body></html>
            """
        if url == "https://www.bhp.com/investors/results":
            return """
            <html><body>
            <a href="https://www.bhp.com/results/fy25-results-presentation.pdf">FY25 Results Presentation 19 Aug 2025</a>
            </body></html>
            """
        if url == "https://asx.example/BHP-annual-report.pdf":
            return "Annual report revenue income NPAT operating cash flow debt segment production outlook capex risks"
        if url == "https://www.bhp.com/results/fy25-results-presentation.pdf":
            return "FY25 results presentation production realised price capex commodity exposure outlook"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources(
        "BHP.AX",
        "2026-06-27",
        identity={"investor_relations_url": "https://www.bhp.com/investors/results"},
        http_get=fake_http_get,
    )

    assert packet["status"] == "ok"
    assert any("company/BHP/announcements" in url for url in requested_urls)
    assert any("markets/company/BHP" in url for url in requested_urls)
    assert "https://www.bhp.com/investors/results" in requested_urls
    titles = [source["title"] for source in packet["sources"]]
    assert "2025 Annual Report" in titles
    assert "FY25 Results Presentation" in titles
    assert all(source["source_type"] == "asx_fallback_document" for source in packet["sources"])


def test_asx_fallback_promotes_report_links_from_discovery_landing_pages():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "company/BHP/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/BHP" in url:
            return """
            <html><body>
            <a href="https://www.bhp.example/annual-report">Annual Report 2025</a>
            </body></html>
            """
        if url == "https://www.bhp.example/annual-report":
            return """
            <html><body>
            <h1>Annual Report 2025</h1>
            <a href="/careers">Careers</a>
            <a href="/downloads/report">Read the report</a>
            </body></html>
            """
        if url == "https://www.bhp.example/careers":
            raise AssertionError("navigation link should not be promoted as an annual report")
        if url == "https://www.bhp.example/downloads/report":
            return "Annual report operating and financial review production capex reserves resources commodity exposure"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("BHP.AX", "2026-06-27", http_get=fake_http_get)

    urls = [source["url"] for source in packet["sources"]]
    assert "https://www.bhp.example/annual-report" in urls
    assert "https://www.bhp.example/downloads/report" in urls
    report = next(source for source in packet["sources"] if source["url"] == "https://www.bhp.example/downloads/report")
    assert report["document_role"] == "annual_report"
    assert report["source_quality_tier"] == "tier_3_company_annual_report_pdf"
    assert report["metric_eligibility"] == "eligible_financial_document"
    assert any(section.get("section_type") == "sector_metric" for section in report["extracted_sections"])
    assert "https://www.bhp.example/careers" not in requested_urls


def test_csl_structured_online_annual_report_is_eligible_financial_source():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "company/CSL/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/CSL" in url:
            return """
            <html><body>
            <a href="https://investors.csl.com/annualreport/2025/">CSL 2025 Annual Report 19 Aug 2025</a>
            </body></html>
            """
        if url == "https://investors.csl.com/annualreport/2025/":
            return """
            <html><body>
            <h1>CSL 2025 Annual Report</h1>
            <section>Operating and Financial Review</section>
            <section>Financial Report</section>
            <section>Key Performance Data Summary</section>
            __TABLE_ROW__ page=8 table=1 row=0 title=key_performance_data | Metric | FY2025 US$m | FY2024 US$m | Change %
            __TABLE_ROW__ page=8 table=1 row=1 title=key_performance_data | Segment revenue | 15,558 | 14,800 | 5.1%
            Research and development investment was US$1.4bn.
            Plasma collections increased 3.0% and gross margin was 50.6%.
            Net debt was US$10.2bn. Guidance outlook expects revenue growth of 5%.
            </body></html>
            """
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("CSL.AX", "2026-07-02", http_get=fake_http_get)

    assert packet["metric_extraction_status"] == "metrics_extracted_from_authoritative_sources"
    report = next(source for source in packet["sources"] if source["url"] == "https://investors.csl.com/annualreport/2025/")
    assert report["document_role"] == "annual_report"
    assert report["source_quality_tier"] == "tier_3_structured_online_annual_report"
    assert report["metric_eligibility"] == "eligible_financial_document"
    segment_revenue = next(
        section
        for section in report["extracted_sections"]
        if section.get("section_type") == "sector_metric" and section.get("metric_name") == "segment_revenue"
    )
    assert segment_revenue["metric_value_status"] == "value_extracted"
    assert segment_revenue["row_label"] == "Segment revenue"
    assert segment_revenue["column_label"] == "FY2025 US$m"
    assert "https://investors.csl.com/annualreport/2025/" in requested_urls


def test_asx_fallback_prefilters_archive_pages_to_latest_primary_report_pdf():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "company/XYZ/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/XYZ" in url:
            return "<html><body>No report links here.</body></html>"
        if url == "https://www.xyz.example/investors/annual-reporting":
            return """
            <html><body>
            <a href="/reports/annual-report-2025.pdf">Annual Report 2025</a>
            <a href="/reports/annual-report-2025.zip">Annual Report 2025 ZIP</a>
            <a href="/reports/annual-report-2025.xml">Annual Report 2025 XML</a>
            <a href="/reports/annual-report-2024.pdf">Annual Report 2024</a>
            </body></html>
            """
        if url == "https://www.xyz.example/reports/annual-report-2025.pdf":
            return "Annual report revenue income NPAT operating cash flow cash debt segment sales outlook capex risks"
        if url in {
            "https://www.xyz.example/reports/annual-report-2025.zip",
            "https://www.xyz.example/reports/annual-report-2025.xml",
            "https://www.xyz.example/reports/annual-report-2024.pdf",
        }:
            raise AssertionError(f"archive variant should not be fetched: {url}")
        raise AssertionError(url)

    packet = module.collect_financial_document_sources(
        "XYZ.AX",
        "2026-06-27",
        identity={"investor_relations_url": "https://www.xyz.example/investors/annual-reporting"},
        http_get=fake_http_get,
    )

    urls = [source["url"] for source in packet["sources"]]
    assert "https://www.xyz.example/reports/annual-report-2025.pdf" in urls
    assert "https://www.xyz.example/reports/annual-report-2025.zip" not in requested_urls
    assert "https://www.xyz.example/reports/annual-report-2025.xml" not in requested_urls
    assert "https://www.xyz.example/reports/annual-report-2024.pdf" not in requested_urls


def test_asx_fallback_uses_known_official_ir_pages_and_infers_report_years():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "asx-research/1.0/companies/WOW/announcements" in url or "company/WOW/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/WOW" in url:
            return "<html><body>No annual report links on this page.</body></html>"
        if url.endswith("/content/dam/wwg/investors/reports/f25/f25/2936242.pdf"):
            return "Annual report revenue income NPAT operating cash flow cash debt segment sales outlook capex risks"
        if "woolworthsgroup.com.au" in url:
            return """
            <html><body>
            <button type="button" data-href="/content/dam/wwg/investors/reports/f25/f25/2936242.pdf">
            Appendix 4E and Annual Report
            </button>
            <button type="button" data-href="/content/dam/wwg/investors/asx-announcements/2026/3058199.pdf">
            Sales Announcement
            </button>
            </body></html>
            """
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("WOW.AX", "2026-06-27", http_get=fake_http_get)

    assert packet["status"] == "ok"
    assert any("woolworthsgroup.com.au" in url for url in requested_urls)
    assert any(url.endswith("/content/dam/wwg/investors/reports/f25/f25/2936242.pdf") for url in requested_urls)
    assert not any(url.endswith("3058199.pdf") for url in requested_urls)
    annual = packet["sources"][0]
    assert annual["document_type"] == "Annual Report"
    assert annual["announcement_date"] == "2025-12-31"
    assert annual["extraction_status"] == "available"
    sections = {section["section_name"]: section for section in annual["extracted_sections"]}
    assert sections["management_discussion_analysis"]["status"] == "available"
    assert "management discussion" in sections["management_discussion_analysis"]["supports_claims"]
    assert sections["cash_flow_statement"]["status"] == "available"
    assert "cash flow statement" in sections["cash_flow_statement"]["supports_claims"]


def test_asx_pdf_text_extraction_uses_optional_pypdf(monkeypatch):
    module = _load_module()
    asx = module._load_asx_collector()

    class FakePage:
        def extract_text(self) -> str:
            return "Annual report operating cash flow outlook segment risks"

    class FakePdfReader:
        def __init__(self, stream):
            self.stream = stream
            self.pages = [FakePage()]

    monkeypatch.setitem(sys.modules, "pypdf", types.SimpleNamespace(PdfReader=FakePdfReader))

    assert "operating cash flow" in asx._extract_pdf_text(b"%PDF fake fixture")


def test_asx_ir_fallback_urls_are_loaded_from_rules_file():
    module = _load_module()
    asx = module._load_asx_collector()

    urls = asx._load_known_asx_ir_urls()

    assert "BHP" in urls
    assert "https://www.bhp.com/investors/annual-reporting" in urls["BHP"]
    assert "WOW" in urls


def test_asx_pdf_text_extraction_includes_pdfplumber_tables(monkeypatch):
    module = _load_module()
    asx = module._load_asx_collector()

    class FakePage:
        def extract_text(self) -> str:
            return "Annual report financial statements"

        def extract_tables(self):
            return [[["Segment", "Revenue"], ["Australia Food", "50000"]]]

    class FakePdf:
        pages = [FakePage()]

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setitem(
        sys.modules,
        "pdfplumber",
        types.SimpleNamespace(open=lambda stream: FakePdf()),
    )

    text = asx._extract_pdf_text(b"%PDF fake fixture")

    assert "Annual report financial statements" in text
    assert "Segment | Revenue" in text
    assert "__TABLE_ROW__ page=1 table=1 row=1 title=pdfplumber_table_1" in text
    assert "Australia Food | 50000" in text


def test_asx_pdf_text_extraction_tries_pdfplumber_text_table_strategy(monkeypatch):
    module = _load_module()
    asx = module._load_asx_collector()

    class FakePage:
        def extract_text(self) -> str:
            return "Annual report financial statements"

        def extract_tables(self, table_settings=None):
            if table_settings and table_settings.get("vertical_strategy") == "text":
                return [[["Metric", "FY2025 $m", "FY2024 $m"], ["Inventories", "4,169", "4,187"]]]
            return []

    class FakePdf:
        pages = [FakePage()]

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setitem(
        sys.modules,
        "pdfplumber",
        types.SimpleNamespace(open=lambda stream: FakePdf()),
    )

    text = asx._extract_pdf_text(b"%PDF fake fixture")

    assert "__TABLE_ROW__ page=1 table=1 row=0 title=pdfplumber_text_table_1" in text
    assert "Metric | FY2025 $m | FY2024 $m" in text
    assert "Inventories | 4,169 | 4,187" in text


def test_asx_pdf_text_extraction_reconstructs_word_coordinate_rows(monkeypatch):
    module = _load_module()
    asx = module._load_asx_collector()

    class FakePage:
        def extract_text(self) -> str:
            return "Inventories 4,169 4,187 (18)"

        def extract_tables(self, table_settings=None):
            return []

        def extract_words(self):
            return [
                {"text": "Metric", "x0": 10, "x1": 40, "top": 10},
                {"text": "FY2025", "x0": 160, "x1": 200, "top": 10},
                {"text": "$m", "x0": 204, "x1": 220, "top": 10},
                {"text": "FY2024", "x0": 260, "x1": 300, "top": 10},
                {"text": "$m", "x0": 304, "x1": 320, "top": 10},
                {"text": "Variance", "x0": 360, "x1": 415, "top": 10},
                {"text": "$m", "x0": 419, "x1": 435, "top": 10},
                {"text": "Inventories", "x0": 10, "x1": 80, "top": 30},
                {"text": "4,169", "x0": 160, "x1": 198, "top": 30},
                {"text": "4,187", "x0": 260, "x1": 298, "top": 30},
                {"text": "(18)", "x0": 360, "x1": 388, "top": 30},
            ]

    class FakePdf:
        pages = [FakePage()]

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setitem(
        sys.modules,
        "pdfplumber",
        types.SimpleNamespace(open=lambda stream: FakePdf()),
    )

    text = asx._extract_pdf_text(b"%PDF fake fixture")
    result = asx._extract_metric_value_from_text(text, "inventory")

    assert "__TABLE_ROW__ page=1 table=1001 row=1 title=pdfplumber_words" in text
    assert "Inventories | 4,169 | 4,187 | (18)" in text
    assert result["metric_value_status"] == "value_extracted"
    assert result["row_label"] == "Inventories"
    assert result["column_label"] == "FY2025 $m"
    assert result["clean_metric_value"] == "4169"


def test_asx_pdf_text_extraction_crops_below_table_titles(monkeypatch):
    module = _load_module()
    asx = module._load_asx_collector()

    class FakeCroppedPage:
        def extract_tables(self, table_settings=None):
            if table_settings and table_settings.get("vertical_strategy") == "text":
                return [[["Metric", "FY2025 $m"], ["Inventories", "4,169"]]]
            return []

    class FakePage:
        width = 600
        height = 800

        def extract_text(self) -> str:
            return "Working capital"

        def extract_tables(self, table_settings=None):
            return []

        def extract_words(self):
            return [
                {"text": "Working", "x0": 10, "x1": 62, "top": 100},
                {"text": "capital", "x0": 66, "x1": 110, "top": 100},
            ]

        def crop(self, bbox):
            assert bbox[1] <= 100
            return FakeCroppedPage()

    class FakePdf:
        pages = [FakePage()]

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setitem(
        sys.modules,
        "pdfplumber",
        types.SimpleNamespace(open=lambda stream: FakePdf()),
    )

    text = asx._extract_pdf_text(b"%PDF fake fixture")

    assert "pdfplumber_crop_balance_sheet_text_table" in text
    assert "Inventories | 4,169" in text


def _asx_sector_packet(module, ticker: str, document_text: str):
    code = ticker.removesuffix(".AX")

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        if f"companies/{code}/announcements" in url:
            return json.dumps(
                {
                    "data": [
                        {
                            "title": "2025 Annual Report",
                            "announcement_date": "2025-08-15",
                            "url": f"https://asx.example/{code}-annual-report.pdf",
                        }
                    ]
                }
            )
        if url == f"https://asx.example/{code}-annual-report.pdf":
            return document_text
        raise AssertionError(url)

    return module.collect_financial_document_sources(ticker, "2026-07-02", http_get=fake_http_get)


def _sector_metric_statuses(packet: dict[str, object]) -> dict[str, str]:
    source = packet["sources"][0]
    return {
        section["metric_name"]: section["status"]
        for section in source["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }


def test_asx_miner_metrics_are_extracted_for_bhp():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "BHP.AX",
        "Annual report operating and financial review cash flow statement production realised price "
        "unit cost AISC capex reserves resources iron ore copper commodity exposure outlook",
    )

    statuses = _sector_metric_statuses(packet)

    assert packet["asx_sector"] == "miners"
    assert statuses["production"] == "available"
    assert statuses["realised_price"] == "available"
    assert statuses["unit_cost_aisc"] == "available"
    assert statuses["capex"] == "available"
    assert statuses["reserves_resources"] == "available"
    assert statuses["commodity_exposure"] == "available"


def test_asx_bank_metrics_are_extracted_for_cba():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "CBA.AX",
        "Annual report operating and financial review cash flow statement NIM CET1 loan growth "
        "arrears impairment dividend ROE outlook",
    )

    statuses = _sector_metric_statuses(packet)

    assert packet["asx_sector"] == "banks"
    assert statuses["net_interest_margin"] == "available"
    assert statuses["cet1"] == "available"
    assert statuses["loan_growth"] == "available"
    assert statuses["arrears"] == "available"
    assert statuses["impairment"] == "available"
    assert statuses["dividend"] == "available"
    assert statuses["roe"] == "available"


def test_metric_value_association_prefers_nearest_compatible_label():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Net interest margin 9 bps on FY24. Operating income increased 5% on FY24.",
        "net_interest_margin",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "9"
    assert result["value_unit"] == "bps"
    assert result["association_score"] >= 80


def test_metric_value_rejects_competing_label_value():
    module = _load_module()
    asx = module._load_asx_collector()

    nim = asx._extract_metric_value_from_text(
        "Net interest margin commentary remained stable. Operating income increased 5% on FY24.",
        "net_interest_margin",
    )
    cet1 = asx._extract_metric_value_from_text(
        "CET1 capital remained strong. Operating income increased 5% on FY24.",
        "cet1",
    )

    assert nim["metric_value_status"] in {"metric_mentioned_only", "direction_extracted"}
    assert nim["clean_metric_value"] == "unavailable"
    assert "competing" in nim["association_reason"].lower()
    assert cet1["clean_metric_value"] == "unavailable"


def test_dense_parser_rejects_metric_label_with_later_narrative_numbers():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "home lending flow in Australia. We continue to look for ways to provide value to our customers. "
        "CommBank Yello supported more than 360,000 customers across 75 offers in 2025.",
        "loan_growth",
    )

    assert result["clean_metric_value"] == "unavailable"
    assert result["metric_value_status"] != "value_extracted"


def test_metric_value_downgrades_table_of_contents_context():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Contents 1 Overview 2 Operating review 3 Guidance 4 Directors report 5 Financial statements",
        "guidance",
    )

    assert result["metric_value_status"] == "context_only"
    assert result["clean_metric_value"] == "unavailable"
    assert result["association_score"] < 50


def test_metric_mentioned_only_keeps_clean_metric_value_unavailable():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "The report discusses dividends and capital management priorities.",
        "dividends",
    )

    assert result["metric_value_status"] == "metric_mentioned_only"
    assert result["clean_metric_value"] == "unavailable"


def test_table_row_value_preserves_row_column_period_context():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Net interest margin | FY25 | 2.05% | FY24 | 1.96%",
        "net_interest_margin",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "2.05"
    assert result["value_unit"] == "%"
    assert result["row_label"] == "Net interest margin"
    assert result["column_label"] == "FY25"
    assert result["period_reference"] == "FY25"
    assert result["comparison_reference"] == "FY24"


def test_multiline_table_header_preserves_units_for_inventory():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Metric | 29 June 2025 | 30 June 2024 | Change\n"
        " | $m | $m | $m\n"
        "Inventories | 4,169 | 4,187 | (18)",
        "inventory",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "4169"
    assert result["value_unit"] == "$m"
    assert result["column_label"] == "29 June 2025 $m"


def test_unitless_metric_value_is_suppressed():
    module = _load_module()
    asx = module._load_asx_collector()
    original_profile_for_metric = asx._profile_for_metric

    def fake_profile_for_metric(metric_name: str):
        if metric_name == "unitless_test_metric":
            return {
                "accepted_labels": ["test metric"],
                "accepted_units": ["%"],
                "accepted_value_patterns": [r"\b\d+(?:\.\d+)?\b"],
                "max_label_value_distance_tokens": 8,
                "direction_rules": {"supportive": ["increased"], "adverse": ["decreased"]},
            }
        return original_profile_for_metric(metric_name)

    asx._profile_for_metric = fake_profile_for_metric

    result = asx._extract_metric_value_from_text(
        "Test metric 17 increased from 16 in the prior period.",
        "unitless_test_metric",
    )

    assert result["association_score"] < 80
    assert result["clean_metric_value"] == "unavailable"
    assert result["metric_value_status"] != "value_extracted"
    assert "unit unit unavailable incompatible" in result["association_reason"]


def test_low_association_score_does_not_populate_clean_metric_value():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Selling and marketing expenses were 17.4% of revenue. Segment revenue discussion follows.",
        "segment_revenue",
    )

    assert result["association_score"] < 80
    assert result["clean_metric_value"] == "unavailable"


def test_cba_nim_and_cet1_do_not_capture_operating_income_percentage():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "CBA.AX",
        "Annual report operating and financial review cash flow statement. "
        "Net interest margin 9 bps on FY24. CET1 12.3% at period end. "
        "Operating income increased 5% on FY24.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["net_interest_margin"]["clean_metric_value"] == "9"
    assert sections["net_interest_margin"]["value_unit"] == "bps"
    assert sections["cet1"]["clean_metric_value"] == "12.3"
    assert sections["cet1"]["value_unit"] == "%"


def test_cba_highlights_row_is_not_suppressed_by_report_navigation_terms():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "CBA.AX",
        "2025 highlights Financial highlights $10,133m Statutory net profit "
        "$28,465m Operating income Net interest margin 2.08% 9bpts on FY24 "
        "12.3% Capital ratio CET1 (APRA, Level 2) Dividend per share, fully franked "
        "Flat on FY24 $4.85 Annual Report Financial Report Additional Information Contents.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["net_interest_margin"]["metric_value_status"] == "value_extracted"
    assert sections["net_interest_margin"]["clean_metric_value"] == "2.08"
    assert sections["net_interest_margin"]["value_unit"] == "%"
    assert sections["cet1"]["metric_value_status"] == "value_extracted"
    assert sections["cet1"]["clean_metric_value"] == "12.3"
    assert sections["cet1"]["value_unit"] == "%"


def test_cba_cet1_prefers_right_hand_capital_ratio_label_over_prior_dividend_label():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Dividend per share, fully franked 12.3% Capital ratio CET1 (APRA, Level 2) Flat on FY24.",
        "cet1",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "12.3"
    assert result["value_unit"] == "%"


def test_asx_ticker_plugins_load_cba_and_wow_without_runtime_metric_values():
    module = _load_module()
    asx = module._load_asx_collector()

    cba_plugin = asx._load_ticker_plugin("CBA.AX")
    wow_plugin = asx._load_ticker_plugin("WOW.AX")

    assert cba_plugin["ticker"] == "CBA.AX"
    assert wow_plugin["ticker"] == "WOW.AX"
    assert "financial highlights" in cba_plugin["preferred_sections"]
    assert "cash-flow statement" in wow_plugin["preferred_sections"]
    assert "net_interest_margin" in cba_plugin["metrics"]
    assert "capex" in wow_plugin["metrics"]

    def assert_no_runtime_values(value):
        if isinstance(value, dict):
            forbidden = {"clean_metric_value", "final_metric_value", "hard_coded_value", "expected_value"}
            assert not forbidden.intersection(value)
            for child in value.values():
                assert_no_runtime_values(child)
        elif isinstance(value, list):
            for child in value:
                assert_no_runtime_values(child)

    assert_no_runtime_values(cba_plugin)
    assert_no_runtime_values(wow_plugin)


def test_cba_plugin_rejects_nim_and_cet1_false_positives_with_plugin_context():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")

    nim = asx._extract_metric_value_from_text(
        "Financial highlights $28,465m Operating income increased 5% on FY24. "
        "Net interest margin commentary follows without a disclosed value.",
        "net_interest_margin",
        ticker_plugin=plugin,
    )
    cet1 = asx._extract_metric_value_from_text(
        "Tier 1 coverage ratio was 2% in an operational risk table. "
        "Capital ratio disclosures are discussed later.",
        "cet1",
        ticker_plugin=plugin,
    )

    assert nim["metric_value_status"] != "value_extracted"
    assert nim["clean_metric_value"] == "unavailable"
    assert cet1["metric_value_status"] != "value_extracted"
    assert cet1["clean_metric_value"] == "unavailable"


def test_cba_plugin_extracts_roe_from_key_ratio_style_text():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")

    result = asx._extract_metric_value_from_text(
        "Key ratios Cash NPAT $10,252m Return on average equity 13.9% and dividend payout ratio 79%.",
        "roe",
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "13.9"
    assert result["value_unit"] == "%"


def test_cba_plugin_value_validation_rejects_implausible_nim_percentage():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")

    result = asx._extract_metric_value_from_text(
        "Financial highlights Net interest margin 85% due to a malformed table extraction.",
        "net_interest_margin",
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_cba_plugin_direct_value_patterns_are_promoted_to_active_value_patterns():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")

    profile = asx._profile_for_metric("net_interest_margin", plugin)

    assert any("Net interest margin" in pattern for pattern in profile["accepted_value_patterns"])


def test_cba_nim_rejects_operating_income_percentage_before_metric_label():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Operating income increased 5% on FY24. Net interest margin commentary follows without a disclosed value.",
        "net_interest_margin",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_cba_nim_prefers_closest_financial_highlight_value_over_prior_growth_percent():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Statutory NPAT $10,133m 7% on FY24 Cash NPAT $10,252m 4% on FY24 "
        "Net interest margin 2.08% 9bpts on FY24 Loan loss rate 7bpts 2bpts on FY24.",
        "net_interest_margin",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "2.08"
    assert result["value_unit"] == "%"


def test_cba_nim_demotes_unmapped_pdf_table_artifact_below_clean_text_block():
    module = _load_module()
    asx = module._load_asx_collector()
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=3\n"
        "__TABLE_ROW__ page=3 table=1 row=0 title=pdfplumber_table_1 | "
        "2 2025 highlights Financial highlights $10,133m $10,252m Statutory net profit "
        "Cash NPAT after tax (NPAT) 4% on FY24 7% on FY24 $28,465m 2.08% "
        "Operating income Net interest margin | 5% on FY24\n"
        "Financial highlights $10,133m Statutory net profit after tax (NPAT) "
        "7% on FY24 $4.85 Dividend per share, fully franked 12.3% Capital ratio CET1 "
        "(APRA, Level 2) Flat on FY24 2.08% Net interest margin 9bpts on FY24 "
        "$28,465m Operating income 5% on FY24."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "net_interest_margin",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
        },
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "2.08"
    assert result["candidate_origin"] == "text_block"


def test_cba_cet1_rejects_unrelated_coverage_or_tier_one_percentages():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Tier 1 coverage ratio was 2% in the operational risk note. Capital ratio disclosures are discussed later.",
        "cet1",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_cba_loan_growth_rejects_home_lending_mix_without_growth_context():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Home lending represented 85% of the Australian lending portfolio mix.",
        "loan_growth",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_cba_arrears_rejects_climate_or_financed_emissions_context():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Climate financed emissions sector table: arrears exposure represented 85% of home lending emissions.",
        "arrears",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"

    result = asx._extract_metric_value_from_text(
        "RE100 renewable electricity % of global operations FY30: 100% 99.9% (Group) "
        "Pending certification in arrears Pending certification in arrears.",
        "arrears",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_cba_targeted_extractor_recovers_arrears_credit_quality_row():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=17\n"
        "Credit quality and arrears. 90+ days arrears by portfolio. "
        "Home loan and personal | 1.50 | 1.51. "
        "Business troublesome loans | 0.70 | 0.75."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "arrears",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
            "ticker_plugin": "CBA.AX",
        },
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "1.50"
    assert result["value_unit"] == "%"
    assert result["row_label"] == "Home loan and personal"
    assert result["column_label"] == "current_period_value"
    assert result["source_page"] == "17"
    assert result["candidate_origin"] == "targeted_plugin"


def test_cba_arrears_rejects_unmapped_pdf_word_table_artifact():
    module = _load_module()
    asx = module._load_asx_collector()
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=17\n"
        "__TABLE_ROW__ page=17 table=1001 row=25 title=pdfplumber_words | 19 | SUSTAINABILITY\n"
        "__TABLE_ROW__ page=17 table=1001 row=26 title=pdfplumber_words | FY25 | FY24 % change\n"
        "__TABLE_ROW__ page=17 table=1001 row=28 title=pdfplumber_words | 2.08 | 4% | certification in arrears"
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "arrears",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
        },
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_cba_impairment_table_prefers_current_expense_not_variance_percent():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Metric | FY2025 $m | FY2024 $m | Change %\n"
        "Loan impairment expense | 802 | 851 | (5.8%)",
        "impairment",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "802"
    assert result["value_unit"] == "$m"
    assert result["column_label"] == "FY2025 $m"


def test_cba_targeted_extractor_recovers_flattened_impairment_financial_summary():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=18\n"
        "Five-year financial summary 30 Jun 25 30 Jun 24 % change $M $M. "
        "Cash NPAT 10,252 9,836 4.2%. "
        "Loan impairment expense 802 851 (5.8%). "
        "Return on equity 13.9% 13.5%."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "impairment",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
            "ticker_plugin": "CBA.AX",
        },
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "802"
    assert result["value_unit"] == "$m"
    assert result["row_label"] == "Loan impairment expense"
    assert result["column_label"] in {"30 Jun 25 $M", "current_period_value"}
    assert result["current_period_value"] == "802"
    assert result["prior_period_value"] == "851"
    assert result["variance_percent"] == "-5.8"
    assert result["source_page"] == "18"
    assert result["candidate_origin"] == "targeted_plugin"


def test_cba_targeted_impairment_does_not_treat_table_heading_dates_as_values():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=130\n"
        "Loan impairment expense and provisions for impairment Group Bank "
        "30 Jun 25 30 Jun 24 30 Jun 23 30 Jun 25 30 Jun 24 $M $M $M $M $M "
        "Loan impairment expense Net collective provision funding 456 559 795 445 513 "
        "Net new and increased individual provisioning 439 397."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "impairment",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
            "ticker_plugin": "CBA.AX",
        },
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"
    assert result["metric_diagnostics"]["failure_type"] in {"row_column_mapping_missing", "target_row_not_found"}


def test_cba_targeted_extractor_prefers_financial_summary_roe_over_rejected_context():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("CBA.AX")
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=18\n"
        "Five-year financial summary 30 Jun 25 30 Jun 24 % %. "
        "Return on equity 13.9% 13.5%.\n"
        f"{asx.PDF_PAGE_MARKER} page=96\n"
        "Remuneration peer comparison market capitalisation MFI share table. "
        "Cash NPAT and ROE 99% are discussed in executive pay benchmarking."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "roe",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
            "ticker_plugin": "CBA.AX",
        },
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "13.9"
    assert result["value_unit"] == "%"
    assert result["source_page"] == "18"
    assert result["candidate_origin"] == "targeted_plugin"
    assert "remuneration" not in result["supporting_sentence"].lower()


def test_cba_impairment_rejects_word_table_with_paragraph_column_fragment():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "__TABLE_ROW__ page=17 table=1001 row=11 title=pdfplumber_words | "
        "FY24 $9,836m | ongoing financial performance. Statutory NPAT includes non-cash items. | "
        "Loan impairment expense decreased 9% reflecting our robust credit origination and\n"
        "__TABLE_ROW__ page=17 table=1001 row=37 title=pdfplumber_words | "
        "Loan impairment expense | (726) | (802) | 9%",
        "impairment",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_bhp_production_value_before_right_hand_production_label_is_accepted():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "FY2025 at a glance 2Mt record annual copper production, including highest copper production in 17 years.",
        "production",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "2"
    assert result["value_unit"] == "mt"


def test_bhp_realised_price_dense_text_without_row_column_proof_is_rejected():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Includes the fair value of contingent payments based on 35% revenue share, "
        "subject to average realised prices achieved by the Assets exceeding thresholds "
        "of US$159/tonne in the 12 month period.",
        "realised_price",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"
    assert result["row_label"] in {"", "unavailable"}
    assert result["column_label"] in {"", "unavailable"}


def test_bhp_realised_price_requires_structured_table_row_and_column_mapping():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Metric | FY2025 | FY2024\n"
        "Average realised price (US$/t) | 103 | 98\n"
        "Production (Mt) | 257 | 260",
        "realised_price",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "103"
    assert result["value_unit"] == "US$/t"
    assert result["row_label"] == "Average realised price (US$/t)"
    assert result["column_label"] == "FY2025"
    assert result["table_mapping_confidence"] >= 80


def test_bhp_unit_cost_prefers_dollar_per_tonne_guidance_over_basis_percentage():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Production for FY2026 is expected to increase to between 18 and 20 Mt "
        "(36 and 40 Mt on a 100 per cent basis), while unit costs are expected "
        "to decrease with guidance between US$116/t and US$128/t.",
        "unit_cost_aisc",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "116"
    assert result["value_unit"] == "US$/t"


def test_bhp_broken_production_table_row_without_preferred_column_is_rejected():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_table_metric_value(
        "__TABLE_ROW__ page=22 table=1 row=11 title=pdfplumber_text_table_1 "
        "| gold production of 99 | ktoz (91 kt | oz FY2024). Hy | drofloat techn | ology | "
        "Environmental Im | pact State | ment (FEIS)",
        "production",
        asx._profile_for_metric("production"),
    )

    assert result == {}


def test_bhp_commodity_exposure_does_not_capture_production_decline_percentage():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_table_metric_value(
        "__TABLE_ROW__ page=22 table=1 row=0 title=pdfplumber_text_table_1 "
        "| header | 5 per cent), loca pper and zinc m | decreased 17 p | er cent to 119 | kt reflecting\n"
        "__TABLE_ROW__ page=22 table=1 row=53 title=pdfplumber_text_table_1 "
        "| At Antamina, copper p | roduction | decreased 17 p | er cent to 119 | kt reflecting",
        "commodity_exposure",
        asx._profile_for_metric("commodity_exposure"),
    )

    assert result == {}


def test_health_insurer_operating_profit_metric_profile_extracts_margin():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "MPL.AX",
        "Annual report operating and financial review. Operating profit margin increased 2.1% "
        "as premium revenue and resident policyholder growth improved.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["operating_profit_or_margin"]["metric_value_status"] == "value_extracted"
    assert sections["operating_profit_or_margin"]["clean_metric_value"] == "2.1"
    assert sections["operating_profit_or_margin"]["value_unit"] == "%"


def test_retailer_comparable_sales_metric_profile_extracts_growth():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "WOW.AX",
        "Annual report operating and financial review. Comparable sales increased 3.7% "
        "while total sales growth remained positive.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["comparable_sales_if_available"]["metric_value_status"] == "value_extracted"
    assert sections["comparable_sales_if_available"]["clean_metric_value"] == "3.7"
    assert sections["comparable_sales_if_available"]["value_unit"] == "%"


def test_csl_segment_revenue_and_guidance_reject_unrelated_percentages_and_toc_numbers():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "CSL.AX",
        "Contents 1 Overview 2 Segment revenue 3 Guidance 4 Financial statements. "
        "Selling and marketing expenses were 17.4% of revenue. "
        "Segment revenue by division is discussed in the operating review. "
        "Guidance outlook is subject to currency and regulatory conditions.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["segment_revenue"]["clean_metric_value"] == "unavailable"
    assert sections["segment_revenue"]["metric_value_status"] != "value_extracted"
    assert sections["guidance"]["clean_metric_value"] == "unavailable"
    assert sections["guidance"]["metric_value_status"] in {"metric_mentioned_only", "context_only"}


def test_csl_segment_revenue_dense_row_requires_structured_table_mapping():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "segment revenue 11,158 10,608 2,166 2,128 2,234 2,064 15,558 14,800 "
        "Segment gross profit 5,641 5,275 1,257 1,318 1,545 1,413 8,443 8,006 "
        "Segment gross profit % 50.6% 49.7% 58.0% 61.9%",
        "segment_revenue",
    )

    assert result["metric_value_status"] == "table_row_unparsed"
    assert result["clean_metric_value"] == "unavailable"
    assert result["association_score"] < 80


def test_csl_guidance_rejects_business_outlook_segment_revenue_heading():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "CSL's Businesses and Outlook US$11,158m CSL Behring revenue 16 Performance. "
        "The FY2025 financial year was dynamic for the vaccine market.",
        "guidance",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_wow_dividends_reject_footnote_marker_and_ebit_margin_is_preserved():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "WOW.AX",
        "Annual report operating and financial review cash flow statement. "
        "Dividend 1 cents footnote marker for prior period table note. "
        "EBIT margin decreasing by a normalised 82 bps to 5.4%.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["dividends"]["clean_metric_value"] == "unavailable"
    assert sections["dividends"]["metric_value_status"] != "value_extracted"
    assert sections["ebit_margin"]["clean_metric_value"] == "82"
    assert sections["ebit_margin"]["value_unit"] == "bps"
    assert sections["ebit_margin"]["direction"] == "adverse"


def test_wow_capex_extracts_cash_flow_purchase_of_ppe_row():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Consolidated statement of cash flows. Investing activities.\n"
        "Metric | F25 $m | F24 $m\n"
        "Payments for property, plant and equipment | (1,890) | (1,732)\n"
        "Proceeds from disposal of property, plant and equipment | 33 | 28",
        "capex",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "-1890"
    assert result["value_unit"] == "$m"
    assert result["row_label"] == "Payments for property, plant and equipment"
    assert result["column_label"] == "F25 $m"
    assert result["table_mapping_confidence"] >= 80


def test_wow_plugin_extracts_capex_from_cash_flow_investing_ppe_context():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("WOW.AX")

    result = asx._extract_metric_value_from_text(
        "Consolidated cash-flow statement. Investing activities.\n"
        "Metric | F25 $m | F24 $m\n"
        "Purchase of property, plant and equipment | (1,890) | (1,732)",
        "capex",
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "-1890"
    assert result["value_unit"] == "$m"
    assert result["row_label"] == "Purchase of property, plant and equipment"
    assert result["column_label"] == "F25 $m"
    assert result["source_page"] == "unavailable"


def test_wow_targeted_extractor_recovers_flattened_cash_flow_capex_row():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("WOW.AX")
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=115\n"
        "Consolidated statement of cash flows 2025 2024 52 WEEKS 53 WEEKS NOTE $M $M. "
        "Cash flows from operating activities Receipts from customers 73,210 70,110. "
        "Cash flows from investing activities Payments for property, plant and equipment (1,890) (1,732). "
        "Proceeds from disposal of property, plant and equipment 33 28."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "capex",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
            "ticker_plugin": "WOW.AX",
        },
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "-1890"
    assert result["value_unit"] == "$m"
    assert result["row_label"] == "Payments for property, plant and equipment"
    assert result["column_label"] in {"2025 $M", "current_period_value"}
    assert result["current_period_value"] == "-1890"
    assert result["prior_period_value"] == "-1732"
    assert result["source_page"] == "115"
    assert result["candidate_origin"] == "targeted_plugin"


def test_wow_targeted_capex_unresolved_records_search_diagnostics():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("WOW.AX")
    document_structure = asx._build_document_structure(
        f"{asx.PDF_PAGE_MARKER} page=115\n"
        "Consolidated statement of cash flows 2025 2024 $M $M. "
        "Cash flows from investing activities Proceeds from disposal of businesses 33 28."
    )

    result = asx._extract_metric_value_from_document(
        document_structure,
        "capex",
        {
            "source_quality_tier": "tier_3_company_annual_report_pdf",
            "document_role": "annual_report",
            "extraction_status": "available",
            "metric_eligibility": "eligible_financial_document",
            "ticker_plugin": "WOW.AX",
        },
        ticker_plugin=plugin,
    )

    diagnostics = result["metric_diagnostics"]
    assert result["metric_value_status"] != "value_extracted"
    assert diagnostics["plugin_used"] is True
    assert diagnostics["targeted_search_attempted"] is True
    assert diagnostics["failure_type"] == "target_row_not_found"
    assert "cash flow statement" in diagnostics["target_sections"]
    assert diagnostics["candidate_sections_seen"]


def test_wow_capex_rejects_segment_revenue_table_without_capex_row():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Segment performance table capital expenditure mentioned in narrative. "
        "Segment | Sales $m | EBIT $m | Margin %\n"
        "Australian Food | 51,000 | 2,753 | 5.4%",
        "capex",
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_wow_plugin_rejects_segment_revenue_table_as_capex_evidence():
    module = _load_module()
    asx = module._load_asx_collector()
    plugin = asx._load_ticker_plugin("WOW.AX")

    result = asx._extract_metric_value_from_text(
        "Segment revenue table capital investment mentioned in narrative. "
        "Segment | Sales $m | EBIT $m | Margin %\n"
        "Australian Food | 51,000 | 2,753 | 5.4%",
        "capex",
        ticker_plugin=plugin,
    )

    assert result["metric_value_status"] != "value_extracted"
    assert result["clean_metric_value"] == "unavailable"


def test_wow_plugin_allows_f25_full_year_csv_data_pack_discovery():
    module = _load_module()
    requested_urls: list[str] = []

    def fake_http_get(url: str, headers: dict[str, str]) -> str:
        requested_urls.append(url)
        if "companies/WOW/announcements" in url:
            raise RuntimeError("ASX endpoint unavailable")
        if "markets/company/WOW" in url:
            return """
            <html><body>
            <a href="https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/2936242.pdf">
            F25 Annual Report 27 Aug 2025</a>
            <a href="https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/full-year-data-pack.csv">
            F25 Full Year CSV Data Pack 27 Aug 2025</a>
            </body></html>
            """
        if url.endswith("2936242.pdf"):
            return "Annual report operating and financial review cash flow statement total sales capex dividends inventory"
        if url.endswith("full-year-data-pack.csv"):
            return "Metric,F25 $m,F24 $m\nPurchase of property plant and equipment,(1890),(1732)"
        raise AssertionError(url)

    packet = module.collect_financial_document_sources("WOW.AX", "2026-07-02", http_get=fake_http_get)
    urls = {source.get("url") for source in packet["sources"]}
    csv_source = next(
        source for source in packet["sources"] if str(source.get("url", "")).endswith("full-year-data-pack.csv")
    )
    capex = next(
        section
        for source in packet["sources"]
        for section in source.get("extracted_sections", [])
        if section.get("section_type") == "sector_metric" and section.get("metric_name") == "capex"
    )

    assert "https://www.woolworthsgroup.com.au/content/dam/wwg/investors/reports/f25/f25/full-year-data-pack.csv" in urls
    assert csv_source["document_structure"]["table_count"] >= 1
    assert capex["metric_value_status"] == "value_extracted"
    assert capex["clean_metric_value"] == "-1890"
    assert capex["row_label"] == "Purchase of property plant and equipment"
    assert capex["column_label"] == "F25 $m"
    assert capex["source_page"] == "1"
    assert capex["candidate_score"] >= 80
    assert capex["ticker_plugin"] == "WOW.AX"
    assert any("markets/company/WOW" in url for url in requested_urls)


def test_mpl_claims_ratio_and_capital_adequacy_preserve_context():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "MPL.AX",
        "Annual report operating and financial review cash flow statement. "
        "Claims ratio increased 3.3% compared with the prior period. "
        "Capital adequacy included a $250m capital buffer above regulatory requirements.",
    )
    sections = {
        section["metric_name"]: section
        for section in packet["sources"][0]["extracted_sections"]
        if section.get("section_type") == "sector_metric"
    }

    assert sections["claims_ratio"]["clean_metric_value"] == "3.3"
    assert sections["claims_ratio"]["direction"] == "adverse"
    assert sections["capital_adequacy"]["clean_metric_value"] == "250"
    assert sections["capital_adequacy"]["value_unit"] == "$m"
    assert "capital buffer" in sections["capital_adequacy"]["supporting_sentence"].lower()


def test_wow_ebit_margin_prefers_82_bps_change_over_later_percentage():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "EBIT margin decreasing by a normalised 82 bps to 5.4%. "
        "In H2, EBIT declined by a normalised 8.1% with an EBIT margin of 5.5%.",
        "ebit_margin",
    )

    assert result["clean_metric_value"] == "82"
    assert result["value_unit"] == "bps"
    assert result["direction"] == "adverse"


def test_wow_ebit_margin_prefers_margin_bps_over_ebit_decline_percentage():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Australian Food F25 EBIT of $2,753 million declined by a normalised 10.5% "
        "with the EBIT margin decreasing by a normalised 82 bps to 5.4%.",
        "ebit_margin",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "82"
    assert result["value_unit"] == "bps"
    assert result["direction"] == "adverse"


def test_dense_working_capital_inventory_row_is_not_nearest_number_extracted():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Inventories 4,169 4,187 (18) Trade payables (6,016) (5,815) (201) "
        "Net investment in inventory increased by 44 $m compared with FY24.",
        "inventory",
    )

    assert result["metric_value_status"] == "table_row_unparsed"
    assert result["clean_metric_value"] == "unavailable"
    assert result["association_score"] < 80
    assert "dense" in result["association_reason"].lower()


def test_pipe_table_inventory_row_preserves_row_column_period_context():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "Metric | FY2025 $m | FY2024 $m | Variance $m\n"
        "Inventories | 4,169 | 4,187 | (18)\n"
        "Trade payables | (6,016) | (5,815) | (201)",
        "inventory",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "4169"
    assert result["value_unit"] == "$m"
    assert result["row_label"] == "Inventories"
    assert result["column_label"] == "FY2025 $m"
    assert result["cell_value"] == "4,169"
    assert result["current_period_value"] == "4169"
    assert result["prior_period_value"] == "4187"
    assert result["variance_value"] == "-18"
    assert result["table_mapping_confidence"] >= 80


def test_structured_table_inventory_prefers_cell_mapping_over_later_nearby_value():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "__TABLE_ROW__ page=12 table=2 row=0 title=working_capital | Metric | FY2025 $m | FY2024 $m | Variance $m\n"
        "__TABLE_ROW__ page=12 table=2 row=1 title=working_capital | Inventories | 4,169 | 4,187 | (18)\n"
        "__TABLE_ROW__ page=12 table=2 row=2 title=working_capital | Trade payables | (6,016) | (5,815) | (201)\n"
        "Net investment in inventory increased by 44 $m compared with FY24.",
        "inventory",
    )

    assert result["metric_value_status"] == "value_extracted"
    assert result["clean_metric_value"] == "4169"
    assert result["cell_value"] == "4,169"
    assert result["table_title"] == "working_capital"
    assert result["source_page"] == "12"
    assert result["row_label"] == "Inventories"
    assert result["column_label"] == "FY2025 $m"
    assert result["table_mapping_confidence"] >= 80
    assert "44" not in result["value_context"]


def test_asx_packet_records_table_extraction_diagnostics():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "WOW.AX",
        "__TABLE_ROW__ page=12 table=2 row=0 title=working_capital | Metric | FY2025 $m | FY2024 $m\n"
        "__TABLE_ROW__ page=12 table=2 row=1 title=working_capital | Inventories | 4,169 | 4,187\n"
        "Annual report operating and financial review cash flow statement inventory.",
    )

    diagnostics = packet["sources"][0]["table_extraction_diagnostics"]

    assert diagnostics["table_rows_detected"] == 2
    assert diagnostics["table_rows_by_strategy"]["pdfplumber_default"] == 2
    assert diagnostics["metric_like_table_rows"]


def test_mpl_claims_ratio_prefers_claims_expense_change_over_later_percentages():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "claims expense (including risk equalisation) (6,814.6) (6,595.8) 3.3% "
        "Gross profit 1,396.4 1,307.2 6.8% Management expenses 6.5%",
        "claims_ratio",
    )

    assert result["clean_metric_value"] == "3.3"
    assert result["value_unit"] == "%"
    assert result["direction"] == "adverse"


def test_mpl_claims_ratio_prefers_primary_row_over_later_non_resident_sentence():
    module = _load_module()
    asx = module._load_asx_collector()

    result = asx._extract_metric_value_from_text(
        "claims expense (including risk equalisation) (6,814.6) (6,595.8) 3.3% "
        "Gross profit 1,396.4 1,307.2 6.8%. "
        "Non-resident net claims expense increased by 8.8% to $190.6 million.",
        "claims_ratio",
    )

    assert result["clean_metric_value"] == "3.3"
    assert result["value_unit"] == "%"
    assert "8.8" not in result["value_context"]


def test_asx_healthcare_metrics_are_extracted_for_csl():
    module = _load_module()
    packet = _asx_sector_packet(
        module,
        "CSL.AX",
        "Annual report operating and financial review cash flow statement segment revenue R&D "
        "plasma collections margin net debt guidance outlook",
    )

    statuses = _sector_metric_statuses(packet)

    assert packet["asx_sector"] == "healthcare"
    assert statuses["segment_revenue"] == "available"
    assert statuses["r_and_d"] == "available"
    assert statuses["plasma_collections"] == "available"
    assert statuses["margins"] == "available"
    assert statuses["debt"] == "available"
    assert statuses["guidance"] == "available"


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


def test_us_filing_sections_handle_sec_heading_variants():
    module = _load_module()

    raw = """
    <html><body>
    Item 7. Management&rsquo;s Discussion and Analysis of Financial Condition and Results of Operations.
    Revenue increased because cloud demand improved.
    LIQUIDITY AND CAPITAL RESOURCES Cash and investments were sufficient.
    Item 7A. Quantitative and Qualitative Disclosures About Market Risk.
    CASH FLOWS S TATEMENTS
    (In millions) Operations Net income 101,832 Depreciation and amortization 34,710
    Financing activities Dividends and share repurchases.
    Notes to Financial Statements
    </body></html>
    """

    sections = module._extract_filing_sections(
        form="10-K",
        raw=raw,
        limit=1000,
        source_type="annual_report_10k",
        filing_date="2025-07-30",
        url="https://sec.example/msft-10k.htm",
    )
    by_type = {section["section_type"]: section for section in sections}

    assert by_type["mda"]["status"] == "available"
    assert "cloud demand improved" in by_type["mda"]["excerpt"]
    assert by_type["cash_flow_statement"]["status"] == "available"
    assert "Operations Net income" in by_type["cash_flow_statement"]["excerpt"]


def test_earnings_8k_finds_exhibit_991_from_table_row_description():
    module = _load_module()

    index_html = """
    <html><body>
    <table>
      <tr>
        <td><a href="/ixviewer/doc/action/doc/exhibit991.htm">Document</a></td>
        <td>EX-99.1</td>
        <td>Earnings Release</td>
      </tr>
    </table>
    </body></html>
    """

    url = module._find_exhibit_99_1_url(index_html, "0000789019", "0000789019-26-000100")

    assert url == "https://www.sec.gov/ixviewer/doc/action/doc/exhibit991.htm"


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
