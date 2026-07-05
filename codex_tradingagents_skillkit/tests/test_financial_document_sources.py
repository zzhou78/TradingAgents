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
    assert annual["extracted_sections"]
    rendered = module.render_financial_document_packet(packet)
    assert "- Market: `ASX`" in rendered
    assert "Annual Report" in rendered
    assert "operating_cash_flow" in rendered


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
    assert "Australia Food | 50000" in text


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
    assert result["current_period_value"] == "4169"
    assert result["prior_period_value"] == "4187"
    assert result["variance_value"] == "-18"


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
