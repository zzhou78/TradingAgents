from __future__ import annotations

import csv
import html
import io
import json
import re
import sys
import urllib.request
from collections.abc import Callable
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

ASX_MARKIT_API_BASE = "https://asx.api.markitdigital.com/asx-research/1.0"
ASX_MARKIT_ANNOUNCEMENTS_URL = ASX_MARKIT_API_BASE + "/companies/{code}/announcements"
ASX_ANNOUNCEMENTS_URL = "https://www.asx.com.au/asx/1/company/{code}/announcements?count=100"
ASX_COMPANY_PAGE_URL = "https://www.asx.com.au/markets/company/{code}"
DEFAULT_ASX_USER_AGENT = "CodexTradingAgents/0.1 ASX document research"
REPO_ROOT = Path(__file__).resolve().parents[2]
ASX_IR_RULES_PATH = REPO_ROOT / "data" / "rules" / "asx_investor_relations_urls.yaml"
ASX_METRIC_PROFILE_PATH = Path(__file__).resolve().parents[1] / "data" / "rules" / "asx_sector_metric_extraction_profiles.yaml"
ASX_TICKER_PLUGIN_DIR = Path(__file__).resolve().parents[1] / "data" / "rules" / "asx_ingestion" / "tickers"
CODEX_BUNDLED_PYTHON_PACKAGES = (
    Path.home()
    / ".cache"
    / "codex-runtimes"
    / "codex-primary-runtime"
    / "dependencies"
    / "python"
    / "Lib"
    / "site-packages"
)

ASX_SECTOR_BY_CODE = {
    "BHP": "miners",
    "CBA": "banks",
    "CSL": "healthcare",
    "MPL": "health_insurers",
    "WOW": "retailers",
}

ASX_SECTOR_METRIC_PATTERNS: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "banks": [
        ("net_interest_margin", "NIM", r"\bNIM\b|net interest margin", ["NIM", "margin quality"]),
        ("cet1", "CET1", r"\bCET1\b|common equity tier 1", ["CET1", "capital adequacy"]),
        ("loan_growth", "Loan growth", r"loan growth|home lending|business lending|gross loans", ["loan growth"]),
        ("arrears", "Arrears", r"arrears|delinquen", ["arrears", "credit quality"]),
        ("impairment", "Impairment", r"impairment|loan loss|credit loss", ["impairment", "credit quality"]),
        ("dividend", "Dividend", r"dividend|DPS|dividend per share", ["dividend"]),
        ("roe", "ROE", r"\bROE\b|return on equity", ["ROE", "profitability"]),
    ],
    "miners": [
        ("production", "Production", r"production|produced|shipments?", ["production"]),
        ("realised_price", "Realised price", r"realised price|realized price|average realised", ["realised price"]),
        ("unit_cost_aisc", "Unit cost / AISC", r"unit cost|AISC|all-in sustaining cost|cash cost", ["unit cost", "AISC"]),
        ("capex", "Capex", r"capex|capital expenditure", ["capex"]),
        ("reserves_resources", "Reserves/resources", r"reserves?|resources?", ["reserves", "resources"]),
        ("commodity_exposure", "Commodity exposure", r"iron ore|copper|coal|potash|nickel|commodity", ["commodity exposure"]),
    ],
    "healthcare": [
        ("segment_revenue", "Segment revenue", r"segment revenue|revenue by segment|segment sales", ["segment revenue"]),
        ("r_and_d", "R&D", r"R&D|research and development", ["R&D"]),
        ("plasma_collections", "Plasma collections", r"plasma collection|plasma collections|plasma volume", ["plasma collections"]),
        ("margins", "Margins", r"margin|gross margin|EBIT margin", ["margins"]),
        ("debt", "Debt", r"net debt|borrowings|debt", ["debt", "liquidity"]),
        ("guidance", "Guidance", r"guidance|outlook|expects?|forecast", ["guidance", "outlook"]),
    ],
    "health_insurers": [
        ("premium_growth", "Premium growth", r"premium growth|premiums?", ["premium growth"]),
        ("claims_ratio", "Claims ratio", r"claims ratio|claims expense|benefits paid", ["claims ratio"]),
        ("membership", "Membership", r"membership|policyholders?|members", ["membership"]),
        ("capital_adequacy", "Capital adequacy", r"capital adequacy|capital ratio|regulatory capital", ["capital adequacy"]),
        (
            "operating_profit_or_margin",
            "Operating profit / margin",
            r"operating profit(?: margin)?|operating margin|organic operating profit growth",
            ["operating profit", "operating margin"],
        ),
    ],
    "retailers": [
        ("sales_growth", "Sales growth", r"sales growth|comparable sales|same[- ]store sales|total sales", ["sales growth"]),
        (
            "comparable_sales_if_available",
            "Comparable sales",
            r"comparable sales|same[- ]store sales|like[- ]for[- ]like sales",
            ["comparable sales"],
        ),
        ("ebit_margin", "EBIT margin", r"EBIT margin|operating margin", ["EBIT margin"]),
        ("inventory", "Inventory", r"inventor(?:y|ies)|stock loss|shrink", ["inventory"]),
        ("capex", "Capex", r"capex|capital expenditure", ["capex"]),
        ("dividends", "Dividends", r"dividend|DPS|dividend per share", ["dividends"]),
    ],
}

ASX_METRIC_VALUE_STATUSES = {
    "value_extracted",
    "portfolio_mix_narrative",
    "guidance_narrative",
    "direction_extracted",
    "metric_mentioned_only",
    "context_only",
    "table_row_unparsed",
    "unavailable",
}

DENSE_TABLE_ROW_LABELS = [
    "inventories",
    "inventory",
    "trade payables",
    "receivables",
    "trade receivables",
    "net investment in inventory",
    "cash",
    "borrowings",
    "debt",
    "assets",
    "liabilities",
    "claims expense",
    "gross profit",
    "management expenses",
    "operating profit",
    "sales",
    "ebit",
    "revenue",
]

STRUCTURED_TABLE_REQUIRED_METRICS = {
    "inventory",
    "debt",
    "capital_adequacy",
    "impairment",
    "segment_revenue",
    "production",
    "realised_price",
    "commodity_exposure",
    "reserves_resources",
    "capex",
    "membership",
}
STRICT_STRUCTURED_VALUE_METRICS = {
    "capex",
    "commodity_exposure",
    "impairment",
    "realised_price",
    "reserves_resources",
    "segment_revenue",
}
TABLE_ROW_MARKER = "__TABLE_ROW__"
PRICE_DENOMINATOR_PATTERN = r"(?:t|tonne|wmt|dmt|lb|oz|boe|kg)"
BHP_REALISED_PRICE_CONTEXT_TERMS = (
    "realised price",
    "realised prices",
    "realized price",
    "realized prices",
    "average realised price",
    "average realised prices",
    "average realized price",
    "average realized prices",
    "price received",
    "realised pricing",
    "realized pricing",
)
BHP_COMMODITY_ROW_LABELS = (
    "iron ore",
    "copper",
    "steelmaking coal",
    "coal",
    "potash",
    "nickel",
    "petroleum",
    "energy coal",
    "metallurgical coal",
)
CSL_SEGMENTS = ("CSL Behring", "CSL Seqirus", "CSL Vifor")
CSL_DEBT_CURRENT_TOTAL_LABELS = (
    "current interest-bearing liabilities and borrowings",
    "current interest bearing liabilities and borrowings",
    "total current interest-bearing liabilities and borrowings",
    "total current interest bearing liabilities and borrowings",
    "current borrowings",
    "total current borrowings",
)
CSL_DEBT_NON_CURRENT_TOTAL_LABELS = (
    "non-current interest-bearing liabilities and borrowings",
    "non current interest bearing liabilities and borrowings",
    "noncurrent interest bearing liabilities and borrowings",
    "total non-current interest-bearing liabilities and borrowings",
    "total non current interest bearing liabilities and borrowings",
    "total noncurrent interest bearing liabilities and borrowings",
    "non-current borrowings",
    "non current borrowings",
    "total non-current borrowings",
    "total non current borrowings",
)
CSL_DEBT_DIRECT_TOTAL_LABELS = (
    "net debt",
    "total debt",
    "total borrowings",
    "borrowings",
    "interest-bearing liabilities and borrowings",
    "interest bearing liabilities and borrowings",
    "interest-bearing liabilities",
    "interest bearing liabilities",
)
VALUE_BEARING_STATUSES = {"value_extracted", "segment_growth", "profitability_metric"}
PDFPLUMBER_WORD_TABLE_INDEX = 1001
PDF_WORD_ROW_TOLERANCE = 3.0
PDF_WORD_COLUMN_GAP = 18.0
PDF_TABLE_TITLE_CROP_HEIGHT = 320
PDFPLUMBER_MAX_TABLE_PAGES = 60
PDF_PAGE_MARKER = "__PDF_PAGE__"
DOCUMENT_TEXT_BLOCK_CHARS = 900
MAX_STRUCTURED_ONLINE_REPORT_CHILD_PAGES = 12

SOURCE_QUALITY_TIERS = {
    "tier_1_asx_lodged_pdf",
    "tier_2_company_results_pdf",
    "tier_3_company_annual_report_pdf",
    "tier_3_structured_online_annual_report",
    "tier_4_company_ir_landing_page",
    "tier_5_navigation_or_archive_page",
}
ELIGIBLE_SOURCE_QUALITY_TIERS = {
    "tier_1_asx_lodged_pdf",
    "tier_2_company_results_pdf",
    "tier_3_company_annual_report_pdf",
    "tier_3_structured_online_annual_report",
}
SOURCE_QUALITY_RANK = {
    "tier_1_asx_lodged_pdf": 1,
    "tier_2_company_results_pdf": 2,
    "tier_3_company_annual_report_pdf": 3,
    "tier_3_structured_online_annual_report": 3,
    "tier_4_company_ir_landing_page": 4,
    "tier_5_navigation_or_archive_page": 5,
}
DOCUMENT_ROLE_RANK = {
    "appendix_4e": 1,
    "financial_report_pdf": 2,
    "annual_report": 3,
    "results_presentation": 4,
    "investor_presentation": 5,
    "unknown": 8,
    "landing_page": 9,
    "archive_page": 10,
}
FINANCIAL_DOCUMENT_ROLES = {
    "annual_report",
    "appendix_4e",
    "results_presentation",
    "financial_report_pdf",
    "investor_presentation",
}

PDFPLUMBER_TABLE_STRATEGIES: list[tuple[str, dict[str, Any] | None]] = [
    ("default", None),
    ("lines", {"vertical_strategy": "lines", "horizontal_strategy": "lines"}),
    (
        "text",
        {
            "vertical_strategy": "text",
            "horizontal_strategy": "text",
            "snap_tolerance": 4,
            "join_tolerance": 4,
            "intersection_tolerance": 6,
            "text_tolerance": 3,
        },
    ),
]

HttpGet = Callable[[str, dict[str, str]], str]

DOCUMENT_PATTERNS: list[tuple[str, str]] = [
    ("Annual Report", r"\bannual report\b"),
    ("Appendix 4E / Preliminary Final Report", r"\bappendix 4e\b|preliminary final report"),
    ("Full Year Results", r"\bfull year results?\b|fy\d{2,4} results"),
    ("Half Year Report", r"\bhalf year report\b|half-year report"),
    ("Appendix 4D", r"\bappendix 4d\b"),
    ("Quarterly Activities Report", r"\bquarterly activities report\b"),
    ("Appendix 4C", r"\bappendix 4c\b"),
    ("Appendix 5B", r"\bappendix 5b\b"),
    ("Cash Flow Statement", r"\bstatement of cash flows\b|\bcash flows?\b"),
    ("Results Presentation", r"\bresults presentation\b"),
    ("Investor Presentation", r"\binvestor presentation\b"),
    ("AGM Presentation", r"\bagm presentation\b|annual general meeting presentation"),
    ("Sustainability Report", r"\bsustainability report\b"),
]

SECTION_PATTERNS: list[tuple[str, str, list[str]]] = [
    ("revenue_income_npat", r"\b(revenue|income|npat|profit after tax)\b", ["revenue", "income", "NPAT"]),
    ("eps_dps", r"\b(eps|earnings per share|dps|dividend per share)\b", ["EPS", "DPS", "dividends"]),
    (
        "management_discussion_analysis",
        r"\b(management discussion|operating and financial review|operating review|financial review|outlook)\b",
        ["management discussion", "MD&A", "outlook"],
    ),
    (
        "cash_flow_statement",
        r"\b(consolidated statements? of cash flows|statements? of cash flows|cash flow statement|cash flows|operating cash flow|net cash)\b",
        ["cash flow statement", "operating cash flow"],
    ),
    ("operating_cash_flow", r"\boperating cash flow\b", ["operating cash flow"]),
    ("free_cash_flow_or_cash_movement", r"\bfree cash flow\b|cash movement|net cash", ["free cash flow", "cash movement"]),
    ("cash_debt_gearing", r"\b(cash|debt|gearing|cet1|capital ratio)\b", ["cash", "debt", "gearing", "capital"]),
    ("segment_product_performance", r"\b(segment|production|realised price|nim|loan growth|arr|premium)\b", ["segment performance", "sector metrics"]),
    ("management_commentary_outlook", r"\b(outlook|guidance|commentary|expects?|forecast)\b", ["outlook", "management commentary"]),
    ("dividends_capital_management", r"\b(dividend|buy-back|buyback|capital management)\b", ["dividends", "capital management"]),
    ("capex_commitments", r"\b(capex|capital expenditure|commitments?)\b", ["capex", "commitments"]),
    ("material_risks", r"\b(risk|uncertain|impairment|arrears|claims ratio)\b", ["risks"]),
    ("one_off_items", r"\b(one-off|significant item|non-recurring|impairment)\b", ["one-off items"]),
    (
        "financial_statement_tables",
        r"\b(revenue\s+.*npat|assets\s+.*liabilities|cash flows?\s+from operating|operating cash flow)\b",
        ["financial statement table", "income statement", "balance sheet", "cash flow statement"],
    ),
    (
        "segment_product_tables",
        r"\b(segment\s+.*revenue|production\s+.*unit cost|product\s+.*sales|membership\s+.*premium)\b",
        ["segment table", "product table", "sector metrics"],
    ),
]


def _headers() -> dict[str, str]:
    return {
        "User-Agent": DEFAULT_ASX_USER_AGENT,
        "Accept": "application/json,text/html,application/pdf;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
    }


def _default_http_get(url: str, headers: dict[str, str]) -> str:
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:  # noqa: S310 - fixed ASX/user supplied IR URLs.
        body = response.read()
        content_type = str(response.headers.get("Content-Type", ""))
    if body.startswith(b"%PDF") or "pdf" in content_type.lower():
        text = _extract_pdf_text(body)
        if text.strip():
            return text
    return body.decode("utf-8", errors="replace")


def _extract_pdf_text(body: bytes) -> str:
    pypdf_text = _extract_pdf_text_with_pypdf(body)
    pdfplumber_rows = _extract_pdf_text_with_pdfplumber(body, include_page_text=not bool(pypdf_text.strip()))
    if pypdf_text and pdfplumber_rows:
        return f"{pypdf_text}\n{pdfplumber_rows}".strip()
    if pypdf_text:
        return pypdf_text
    if pdfplumber_rows:
        return pdfplumber_rows
    return ""


def _extract_pdf_text_with_pypdf(body: bytes) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    try:
        reader = PdfReader(io.BytesIO(body))
    except Exception:
        return ""
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            continue
        if text:
            pages.append(f"{PDF_PAGE_MARKER} page={page_number}\n{text}")
    return "\n".join(page for page in pages if page).strip()


def _extract_pdf_text_with_pdfplumber(body: bytes, *, include_page_text: bool = True) -> str:
    try:
        import pdfplumber
    except ImportError:
        if CODEX_BUNDLED_PYTHON_PACKAGES.exists():
            sys.path.append(str(CODEX_BUNDLED_PYTHON_PACKAGES))
            try:
                import pdfplumber
            except ImportError:
                return ""
        else:
            return ""
    parts: list[str] = []
    try:
        with pdfplumber.open(io.BytesIO(body)) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                if include_page_text:
                    try:
                        text = page.extract_text() or ""
                    except Exception:
                        text = ""
                    if text:
                        parts.append(f"{PDF_PAGE_MARKER} page={page_number}")
                        parts.append(text)
                if page_number > PDFPLUMBER_MAX_TABLE_PAGES:
                    if not include_page_text:
                        break
                    continue
                parts.extend(_extract_pdfplumber_table_rows(page, page_number))
                parts.extend(_extract_pdfplumber_word_table_rows(page, page_number))
    except Exception:
        return ""
    return "\n".join(part for part in parts if part).strip()


def _extract_pdfplumber_table_rows(page: Any, page_number: int) -> list[str]:
    rows: list[str] = []
    seen_rows: set[tuple[str, ...]] = set()
    next_table_index = 1
    for strategy_name, settings in PDFPLUMBER_TABLE_STRATEGIES:
        try:
            if settings is None:
                tables = page.extract_tables() or []
            else:
                tables = page.extract_tables(table_settings=settings) or []
        except TypeError:
            if settings is not None:
                continue
            try:
                tables = page.extract_tables() or []
            except Exception:
                tables = []
        except Exception:
            tables = []
        for table in tables:
            table_title = "pdfplumber_table" if strategy_name == "default" else f"pdfplumber_{strategy_name}_table"
            emitted_any = False
            for row_index, row in enumerate(table or []):
                cells = _normalize_pdf_table_cells(row or [])
                if not _cells_look_table_like(cells):
                    continue
                row_key = tuple(cell.lower() for cell in cells)
                if row_key in seen_rows:
                    continue
                seen_rows.add(row_key)
                emitted_any = True
                rows.append(
                    _format_structured_table_row(
                        cells,
                        page_number,
                        next_table_index,
                        row_index,
                        f"{table_title}_{next_table_index}",
                    )
                )
            if emitted_any:
                next_table_index += 1
    rows.extend(_extract_pdfplumber_cropped_table_rows(page, page_number, seen_rows, next_table_index))
    return rows


def _extract_pdfplumber_cropped_table_rows(
    page: Any,
    page_number: int,
    seen_rows: set[tuple[str, ...]],
    start_table_index: int,
) -> list[str]:
    rows: list[str] = []
    next_table_index = start_table_index
    for title, top in _pdf_table_title_regions(page):
        try:
            height = float(getattr(page, "height", top + PDF_TABLE_TITLE_CROP_HEIGHT))
            width = float(getattr(page, "width", 10_000))
            cropped = page.crop((0, max(0.0, top - 8.0), width, min(height, top + PDF_TABLE_TITLE_CROP_HEIGHT)))
        except Exception:
            continue
        for strategy_name, settings in PDFPLUMBER_TABLE_STRATEGIES:
            try:
                if settings is None:
                    tables = cropped.extract_tables() or []
                else:
                    tables = cropped.extract_tables(table_settings=settings) or []
            except TypeError:
                if settings is not None:
                    continue
                try:
                    tables = cropped.extract_tables() or []
                except Exception:
                    tables = []
            except Exception:
                tables = []
            for table in tables:
                emitted_any = False
                for row_index, row in enumerate(table or []):
                    cells = _normalize_pdf_table_cells(row or [])
                    if not _cells_look_table_like(cells):
                        continue
                    row_key = tuple(cell.lower() for cell in cells)
                    if row_key in seen_rows:
                        continue
                    seen_rows.add(row_key)
                    emitted_any = True
                    rows.append(
                        _format_structured_table_row(
                            cells,
                            page_number,
                            next_table_index,
                            row_index,
                            f"pdfplumber_crop_{title}_{strategy_name}_table_{next_table_index}",
                        )
                    )
                if emitted_any:
                    next_table_index += 1
    return rows


def _pdf_table_title_regions(page: Any) -> list[tuple[str, float]]:
    try:
        words = page.extract_words() or []
    except Exception:
        return []
    rows = _cluster_pdf_words_by_row(words)
    title_patterns = [
        ("balance_sheet", r"\b(statement of financial position|balance sheet|working capital)\b"),
        ("cash_flow", r"\b(statement of cash flows|cash flow)\b"),
        ("income_statement", r"\b(income statement|statement of comprehensive income|profit or loss)\b"),
        ("segment", r"\b(segment information|segment revenue|operating segments)\b"),
        ("metrics", r"\b(key metrics|operating metrics|financial metrics)\b"),
    ]
    regions: list[tuple[str, float]] = []
    seen: set[tuple[str, int]] = set()
    for row_words in rows:
        line = _clean_text(" ".join(str(word.get("text") or "") for word in row_words))
        top = min(float(word.get("top") or word.get("doctop") or 0) for word in row_words)
        for title, pattern in title_patterns:
            if not re.search(pattern, line, re.IGNORECASE):
                continue
            key = (title, int(top // 10))
            if key in seen:
                continue
            seen.add(key)
            regions.append((title, top))
    return regions


def _normalize_pdf_table_cells(row: list[Any]) -> list[str]:
    return [_clean_text(str(cell or "").replace("\n", " ")) for cell in row]


def _cells_look_table_like(cells: list[str]) -> bool:
    non_empty = [cell for cell in cells if cell]
    if len(non_empty) < 2:
        return False
    numeric_cells = sum(1 for cell in non_empty if _cell_has_number(cell))
    header_cells = sum(1 for cell in non_empty if _looks_like_period_or_metric_header(cell))
    return numeric_cells >= 1 or header_cells >= 2


def _cell_has_number(cell: str) -> bool:
    return bool(re.search(r"\(?-?(?:US\$|A\$|\$)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)?", cell, re.IGNORECASE))


def _looks_like_period_or_metric_header(cell: str) -> bool:
    return bool(
        re.search(
            r"\b(?:metric|segment|fy\d{2,4}|20\d{2}|variance|change|current|prior|revenue|margin|inventory|claims|dividend|cet1|nim)\b|[$%]",
            cell,
            re.IGNORECASE,
        )
    )


def _extract_pdfplumber_word_table_rows(page: Any, page_number: int) -> list[str]:
    try:
        words = page.extract_words() or []
    except Exception:
        return []
    row_clusters = _cluster_pdf_words_by_row(words)
    structured_rows: list[str] = []
    for row_index, row_words in enumerate(row_clusters):
        cells = _cells_from_pdf_word_row(row_words)
        if _cells_look_table_like(cells):
            structured_rows.append(
                _format_structured_table_row(
                    cells,
                    page_number,
                    PDFPLUMBER_WORD_TABLE_INDEX,
                    row_index,
                    "pdfplumber_words",
                )
            )
    return structured_rows


def _cluster_pdf_words_by_row(words: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    normalized_words = [word for word in words if str(word.get("text") or "").strip()]
    sorted_words = sorted(
        normalized_words,
        key=lambda word: (float(word.get("top") or word.get("doctop") or 0), float(word.get("x0") or 0)),
    )
    rows: list[list[dict[str, Any]]] = []
    row_tops: list[float] = []
    for word in sorted_words:
        top = float(word.get("top") or word.get("doctop") or 0)
        matched_index = next((index for index, row_top in enumerate(row_tops) if abs(top - row_top) <= PDF_WORD_ROW_TOLERANCE), None)
        if matched_index is None:
            rows.append([word])
            row_tops.append(top)
        else:
            rows[matched_index].append(word)
            row_tops[matched_index] = (row_tops[matched_index] + top) / 2
    return [sorted(row, key=lambda word: float(word.get("x0") or 0)) for row in rows]


def _cells_from_pdf_word_row(words: list[dict[str, Any]]) -> list[str]:
    cells: list[list[str]] = []
    current_cell: list[str] = []
    previous_x1: float | None = None
    for word in sorted(words, key=lambda item: float(item.get("x0") or 0)):
        text = str(word.get("text") or "").strip()
        if not text:
            continue
        x0 = float(word.get("x0") or 0)
        x1 = float(word.get("x1") or x0)
        if previous_x1 is not None and x0 - previous_x1 > PDF_WORD_COLUMN_GAP and current_cell:
            cells.append(current_cell)
            current_cell = []
        current_cell.append(text)
        previous_x1 = x1
    if current_cell:
        cells.append(current_cell)
    return [_clean_text(" ".join(cell)) for cell in cells if any(part.strip() for part in cell)]


def _format_structured_table_row(cells: list[str], page_number: int, table_index: int, row_index: int, table_title: str) -> str:
    escaped_title = re.sub(r"\s+", "_", table_title.strip() or f"pdfplumber_table_{table_index}")
    return (
        f"{TABLE_ROW_MARKER} page={page_number} table={table_index} row={row_index} title={escaped_title} | "
        + " | ".join(cells)
    )


def _csv_document_to_structured_table_text(raw_document: str, *, table_title: str = "csv_data_pack") -> str:
    rows: list[str] = []
    for row_index, row in enumerate(csv.reader(io.StringIO(raw_document))):
        cells = [_clean_text(cell) for cell in row]
        if len([cell for cell in cells if cell]) < 2:
            continue
        rows.append(_format_structured_table_row(cells, 1, 1, row_index, table_title))
    return "\n".join(rows)


def _structured_online_report_child_urls(
    raw_document: str,
    base_url: str,
    ticker_plugin: dict[str, Any] | None = None,
    *,
    page_url: str = "",
) -> list[str]:
    parsed_base = urlparse(base_url)
    if parsed_base.scheme not in {"http", "https"} or not parsed_base.netloc:
        return []
    join_base = page_url or base_url
    base_path = parsed_base.path or "/"
    if not base_path.endswith("/"):
        base_path = base_path.rsplit("/", 1)[0] + "/"
    section_terms = [
        "operating and financial review",
        "financial report",
        "key performance data",
        "outlook",
        "guidance",
        "csl behring",
        "csl seqirus",
        "csl vifor",
        "plasma",
        "debt",
        "borrowings",
        "liquidity",
        "balance sheet",
        "statement of financial position",
        "financial statements",
        "notes to the financial statements",
        "cash and cash equivalents",
        "table of contents",
        "toc",
    ]
    if ticker_plugin:
        section_terms.extend(str(term) for term in ticker_plugin.get("preferred_sections", []) or [])
        for metric_profile in (ticker_plugin.get("metrics") or {}).values():
            if isinstance(metric_profile, dict):
                section_terms.extend(str(term) for term in metric_profile.get("target_sections", []) or [])
    urls: list[str] = []
    base_without_fragment = base_url.split("#", 1)[0].rstrip("/")
    for anchor in re.finditer(r"(?is)<a\b(?P<attrs>[^>]*)>(?P<label>.*?)</a>", raw_document):
        attrs = anchor.group("attrs")
        href_match = re.search(r"href=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        if not href_match:
            continue
        href = href_match.group(1).strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        child_url = urljoin(join_base, href).split("#", 1)[0]
        parsed_child = urlparse(child_url)
        if parsed_child.scheme not in {"http", "https"} or parsed_child.netloc != parsed_base.netloc:
            continue
        if child_url.rstrip("/") == base_without_fragment:
            continue
        child_path = parsed_child.path or "/"
        if not child_path.startswith(base_path):
            continue
        if _is_pdf_like_url(child_url) or _is_csv_like_url(child_url) or re.search(
            r"\.(?:zip|xml|xlsx?|json|png|jpe?g|svg)(?:[?#].*)?$",
            child_url,
            re.IGNORECASE,
        ):
            continue
        label_text = _clean_text(anchor.group("label"))
        searchable = f"{label_text} {href.replace('-', ' ').replace('_', ' ')}".lower()
        if section_terms and not any(term.lower() in searchable for term in section_terms):
            continue
        if child_url not in urls:
            urls.append(child_url)
        if len(urls) >= MAX_STRUCTURED_ONLINE_REPORT_CHILD_PAGES:
            break
    return urls


def _expand_structured_online_annual_report(
    raw_document: str,
    url: str,
    title: str,
    http_get: HttpGet,
    headers: dict[str, str],
    ticker_plugin: dict[str, Any] | None,
) -> tuple[str, list[str]]:
    if not _looks_like_structured_online_annual_report(raw_document, url, title):
        return raw_document, []
    parts = [raw_document]
    fetched_urls: list[str] = []
    queued_urls = _structured_online_report_child_urls(raw_document, url, ticker_plugin)
    seen_urls = set(queued_urls)
    while queued_urls and len(fetched_urls) < MAX_STRUCTURED_ONLINE_REPORT_CHILD_PAGES:
        child_url = queued_urls.pop(0)
        try:
            child_document = http_get(child_url, headers)
        except Exception:  # noqa: BLE001 - keep the parent structured report usable if a child section fails.
            continue
        if not child_document or not _is_html_like_document(child_document) or _is_pdf_like_url(child_url):
            continue
        fetched_urls.append(child_url)
        parts.append(f"<h2>Linked report page {html.escape(child_url)}</h2>\n{child_document}")
        page_match = re.search(r"/(\d+)/?$", urlparse(child_url).path)
        if page_match:
            adjacent_url = urljoin(child_url, f"../{int(page_match.group(1)) + 1}/")
            if adjacent_url not in seen_urls and len(fetched_urls) + len(queued_urls) < MAX_STRUCTURED_ONLINE_REPORT_CHILD_PAGES:
                seen_urls.add(adjacent_url)
                queued_urls.append(adjacent_url)
        for nested_url in _structured_online_report_child_urls(
            child_document,
            url,
            ticker_plugin,
            page_url=child_url,
        ):
            if nested_url in seen_urls:
                continue
            seen_urls.add(nested_url)
            queued_urls.append(nested_url)
    return "\n".join(parts), fetched_urls


def _extract_structured_online_annual_report_sections(raw_document: str) -> str:
    if not _is_html_like_document(raw_document):
        return raw_document
    sections: list[str] = []
    for heading in re.finditer(r"(?is)<h([1-6])\b([^>]*)>(.*?)</h\1>", raw_document):
        attrs = heading.group(2)
        heading_text = _clean_text(heading.group(3))
        anchor = ""
        anchor_match = re.search(r"\bid=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        if anchor_match:
            anchor = anchor_match.group(1)
        if heading_text:
            sections.append(_clean_text(f"Section {anchor} {heading_text}"))
    for anchor_match in re.finditer(r"(?is)<a\b([^>]*)>(.*?)</a>", raw_document):
        attrs = anchor_match.group(1)
        label = _clean_text(anchor_match.group(2))
        href_match = re.search(r"\bhref=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        href = href_match.group(1) if href_match else ""
        if label and href:
            sections.append(_clean_text(f"Anchor {label} {href}"))
    table_index = 1
    for table_match in re.finditer(r"(?is)<table\b[^>]*>(.*?)</table>", raw_document):
        table_html = table_match.group(1)
        caption_match = re.search(r"(?is)<caption\b[^>]*>(.*?)</caption>", table_html)
        title = _clean_text(caption_match.group(1)) if caption_match else f"online_annual_report_table_{table_index}"
        for row_index, row_match in enumerate(re.finditer(r"(?is)<tr\b[^>]*>(.*?)</tr>", table_html)):
            cells = [
                _clean_text(cell)
                for cell in re.findall(r"(?is)<t[dh]\b[^>]*>(.*?)</t[dh]>", row_match.group(1))
            ]
            if len([cell for cell in cells if cell]) >= 2:
                sections.append(_format_structured_table_row(cells, 1, table_index, row_index, title))
        table_index += 1
    for card_match in re.finditer(
        r"(?is)<(?P<tag>div|section|article|li)\b(?P<attrs>[^>]*(?:metric|tile|card|stat|kpi)[^>]*)>(?P<body>.*?)</(?P=tag)>",
        raw_document,
    ):
        card_text = _clean_text(card_match.group("body"))
        if card_text and re.search(r"\d", card_text):
            sections.append(card_text)
    for raw_line in raw_document.splitlines():
        line = raw_line.strip()
        if line.startswith(TABLE_ROW_MARKER):
            sections.append(line)
    for json_match in re.finditer(
        r"(?is)<script\b[^>]+type=['\"]application/ld\+json['\"][^>]*>(.*?)</script>",
        raw_document,
    ):
        structured_text = _clean_text(json_match.group(1))
        if structured_text:
            sections.append(f"Embedded structured data {structured_text}")
    for meta_match in re.finditer(r"(?is)<meta\b[^>]+>", raw_document):
        tag = meta_match.group(0)
        if not re.search(r"\b(?:name|property)=['\"](?:description|og:description|twitter:description)['\"]", tag, re.IGNORECASE):
            continue
        content_match = re.search(r"\bcontent=['\"]([^'\"]+)['\"]", tag, re.IGNORECASE)
        if not content_match:
            continue
        meta_text = _clean_text(html.unescape(content_match.group(1)))
        if meta_text:
            sections.append(f"Page metadata {meta_text}")
    raw_without_table_markers = "\n".join(
        raw_line for raw_line in raw_document.splitlines() if not raw_line.strip().startswith(TABLE_ROW_MARKER)
    )
    clean_document = _clean_text(raw_without_table_markers)
    if clean_document:
        sections.append(clean_document)
    return "\n".join(section for section in sections if section)


def _document_text_for_structure(raw_document: str, url: str, title: str = "") -> str:
    if _is_csv_like_url(url):
        table_text = _csv_document_to_structured_table_text(raw_document, table_title=title or "csv_data_pack")
        return f"{raw_document}\n{table_text}" if table_text else raw_document
    if _is_html_like_document(raw_document) and not _is_pdf_like_url(url):
        return _extract_structured_online_annual_report_sections(raw_document)
    return raw_document


def normalize_asx_code(ticker: str) -> str:
    symbol = ticker.upper().strip()
    return symbol[:-3] if symbol.endswith(".AX") else symbol


def is_asx_ticker(ticker: str, identity: dict[str, Any] | None = None) -> bool:
    symbol = ticker.upper().strip()
    if symbol.endswith(".AX"):
        return True
    identity = identity or {}
    market = str(identity.get("market") or identity.get("exchange") or "").upper()
    return market in {"ASX", "XASX", "AU"}


def _parse_date(value: str) -> datetime:
    value = value.strip()
    if re.match(r"\d{4}-\d{2}-\d{2}", value):
        value = value[:10]
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d %b %Y"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise ValueError(value)


def _clean_text(raw: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _excerpt(text: str, limit: int) -> str:
    text = _clean_text(text)
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].strip()


def _classify_document(title: str) -> str | None:
    for document_type, pattern in DOCUMENT_PATTERNS:
        if re.search(pattern, title, re.IGNORECASE):
            return document_type
    return None


def _classify_document_with_plugin(title: str, url: str = "", ticker_plugin: dict[str, Any] | None = None) -> str | None:
    haystack = f"{title} {url}"
    for hint in _plugin_list(_plugin_source_hints(ticker_plugin), "document_type_hints"):
        if not isinstance(hint, dict):
            continue
        pattern = str(hint.get("pattern") or "")
        document_type = str(hint.get("document_type") or "")
        if pattern and document_type and re.search(pattern, haystack, re.IGNORECASE):
            return document_type
    return _classify_document(title)


def _is_pdf_like_url(url: str) -> bool:
    lower = url.lower()
    return lower.endswith(".pdf") or ".pdf?" in lower or "/file/" in lower


def _is_csv_like_url(url: str) -> bool:
    lower = url.lower()
    return lower.endswith(".csv") or ".csv?" in lower


def _is_html_like_document(raw_document: str) -> bool:
    return bool(re.search(r"(?is)<\s*(?:html|body|main|nav|a|button|script|style)\b", raw_document))


def _looks_like_archive_or_navigation(raw_document: str, url: str, title: str) -> bool:
    lower = _clean_text(f"{title} {url} {raw_document[:5000]}").lower()
    archive_terms = sum(
        1
        for term in [
            "archive",
            "reports and presentations",
            "annual reports",
            "shareholder services",
            "downloads",
            "asx announcements",
            "investor centre",
            "investor center",
        ]
        if term in lower
    )
    if _is_navigation_or_toc(lower):
        return True
    return archive_terms >= 2 and _is_html_like_document(raw_document)


def _looks_like_structured_online_annual_report(raw_document: str, url: str, title: str) -> bool:
    if not raw_document or not _is_html_like_document(raw_document) or _is_pdf_like_url(url):
        return False
    lower = _clean_text(f"{title} {url} {raw_document[:30000]}").lower()
    has_annual_report_identity = bool(
        re.search(r"\bannual\s+report\b|annualreport/\d{4}|annual-report-\d{4}|annual-reporting", lower)
    )
    if not has_annual_report_identity:
        return False
    section_hits = sum(
        1
        for term in [
            "operating and financial review",
            "financial report",
            "key performance data summary",
            "directors' report",
            "directors report",
            "shareholder information",
            "performance year in review",
        ]
        if term in lower
    )
    financial_metric_hits = sum(
        1
        for term in [
            "revenue",
            "cashflow",
            "cash flow",
            "net debt",
            "gross margin",
            "research and development",
            "plasma collections",
            "guidance",
            "outlook",
        ]
        if term in lower
    )
    return section_hits >= 2 and financial_metric_hits >= 2


def _document_role(document_type: str | None, *, raw_document: str = "", url: str = "", title: str = "") -> str:
    if raw_document and _is_html_like_document(raw_document) and not _is_pdf_like_url(url):
        if _looks_like_structured_online_annual_report(raw_document, url, title):
            return "annual_report"
        return "archive_page" if _looks_like_archive_or_navigation(raw_document, url, title) else "landing_page"
    normalized = (document_type or "").lower()
    if "annual report" in normalized:
        return "annual_report"
    if "appendix 4e" in normalized or "preliminary final" in normalized:
        return "appendix_4e"
    if "results" in normalized and "presentation" in normalized:
        return "results_presentation"
    if "investor presentation" in normalized or "agm presentation" in normalized:
        return "investor_presentation"
    if any(term in normalized for term in ["half year", "appendix 4d", "quarterly", "cash flow", "full year results"]):
        return "financial_report_pdf"
    if "sustainability" in normalized:
        return "investor_presentation"
    return "unknown"


def _source_quality_tier(
    *,
    source_type: str,
    document_role: str,
    url: str,
    fallback_page_url: str = "",
    raw_document: str = "",
    title: str = "",
) -> str:
    if _looks_like_structured_online_annual_report(raw_document, url, title):
        return "tier_3_structured_online_annual_report"
    if document_role == "archive_page" or _looks_like_archive_or_navigation(raw_document, url, title):
        return "tier_5_navigation_or_archive_page"
    if document_role == "landing_page":
        return "tier_4_company_ir_landing_page"
    if raw_document and _is_html_like_document(raw_document) and not _is_pdf_like_url(url):
        return "tier_4_company_ir_landing_page"
    lower_url = url.lower()
    lower_fallback_page = fallback_page_url.lower()
    asx_lodged = (
        source_type == "asx_announcement"
        or "asx-research/1.0/file/" in lower_url
        or "asx.com.au" in lower_url
        or "asx.com.au/markets/company" in lower_fallback_page
        or (source_type == "asx_fallback_document" and "asx" in lower_url)
    )
    if asx_lodged and document_role in FINANCIAL_DOCUMENT_ROLES:
        return "tier_1_asx_lodged_pdf"
    if document_role == "annual_report":
        return "tier_3_company_annual_report_pdf"
    if document_role in {"appendix_4e", "results_presentation", "financial_report_pdf", "investor_presentation"}:
        return "tier_2_company_results_pdf"
    return "tier_4_company_ir_landing_page" if not _is_pdf_like_url(url) else "tier_2_company_results_pdf"


def _metric_eligibility(source_quality_tier: str, document_role: str, extraction_status: str) -> str:
    if (
        source_quality_tier in ELIGIBLE_SOURCE_QUALITY_TIERS
        and document_role in FINANCIAL_DOCUMENT_ROLES
        and extraction_status == "available"
    ):
        return "eligible_financial_document"
    if source_quality_tier in {"tier_4_company_ir_landing_page", "tier_5_navigation_or_archive_page"}:
        return "discovery_only"
    return "not_eligible"


def _announcement_rows(payload: str) -> list[dict[str, Any]]:
    data = json.loads(payload)
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    for key in ("data", "announcements", "items", "results"):
        rows = data.get(key) if isinstance(data, dict) else None
        if isinstance(rows, list):
            return [row for row in rows if isinstance(row, dict)]
        if isinstance(rows, dict):
            for nested_key in ("items", "announcements", "results"):
                nested_rows = rows.get(nested_key)
                if isinstance(nested_rows, list):
                    return [row for row in nested_rows if isinstance(row, dict)]
    return []


def _field(row: dict[str, Any], *names: str) -> str:
    for name in names:
        value = row.get(name)
        if value not in (None, ""):
            return str(value)
    return ""


def _document_url(row: dict[str, Any]) -> str:
    url = _field(row, "url", "document_url", "pdf_url", "file_url", "documentReleaseUrl", "downloadUrl")
    if url:
        return url
    document_key = _field(row, "documentKey", "document_key", "fileKey", "file_key")
    if document_key:
        return f"{ASX_MARKIT_API_BASE}/file/{document_key}"
    return ""


def _announcement_endpoint_urls(asx_code: str) -> list[str]:
    return [
        ASX_MARKIT_ANNOUNCEMENTS_URL.format(code=asx_code),
        ASX_ANNOUNCEMENTS_URL.format(code=asx_code),
    ]


def _date_from_text(text: str) -> str:
    iso = re.search(r"\b\d{4}-\d{2}-\d{2}\b", text)
    if iso:
        return iso.group(0)
    dated = re.search(r"\b\d{1,2}\s+[A-Z][a-z]{2,8}\s+\d{4}\b", text)
    if dated:
        return dated.group(0)
    year = re.search(r"\b(20\d{2})\b", text)
    if year:
        return f"{year.group(1)}-12-31"
    fiscal_year = re.search(r"\bF(?:Y)?(\d{2})\b", text, re.IGNORECASE)
    if fiscal_year:
        return f"20{fiscal_year.group(1)}-12-31"
    return ""


def _title_without_date(text: str) -> str:
    date_text = _date_from_text(text)
    if date_text:
        text = text.replace(date_text, " ")
    return re.sub(r"\s+", " ", text).strip()


def _fallback_row_title(*candidates: str) -> str:
    cleaned_candidates = [_clean_text(candidate) for candidate in candidates if _clean_text(candidate)]
    for candidate in cleaned_candidates:
        if _classify_document(candidate):
            title = _title_without_date(candidate)
            if title:
                return title
    for candidate in cleaned_candidates:
        title = _title_without_date(candidate)
        if title:
            return title
    return ""


def _can_inherit_report_context(clean_label: str, title: str, href: str) -> bool:
    label_title = f"{clean_label} {title}".lower()
    href_context = href.replace("-", " ").replace("_", " ").lower()
    has_report_action = bool(re.search(r"\b(?:read|view|open|download|get)\b.*\breport\b|\breport\b", label_title))
    inherited_report_asset = bool(
        re.search(r"\b(?:pdf|download|full\s+report|annual\s+report)\b", label_title)
        and re.search(r"(?:\.pdf(?:[?#].*)?$|/download|/downloads|/documents?|/reports?|annual\s+report)", href_context)
    )
    has_document_url_cue = bool(
        re.search(
            r"(?:\.pdf(?:[?#].*)?$|/download|/downloads|/content/dam|/documents?|/reports?|annual\s+report)",
            href_context,
            re.IGNORECASE,
        )
    )
    return (has_report_action or inherited_report_asset) and has_document_url_cue


def _fallback_page_self_row(page_html: str, page_url: str) -> dict[str, Any] | None:
    clean = _clean_text(page_html)
    document_type = _classify_document(f"{page_url.replace('-', ' ').replace('_', ' ')} {clean[:1000]}")
    if not document_type and not _looks_like_structured_online_annual_report(page_html, page_url, clean[:120]):
        return None
    date_text = _date_from_text(f"{page_url} {clean[:3000]}")
    if not date_text:
        return None
    return {
        "title": _fallback_row_title(clean[:240], page_url),
        "announcement_date": date_text,
        "url": page_url,
        "fallback_page_url": page_url,
    }


def _fallback_rows(
    page_html: str,
    page_url: str,
    *,
    inherited_title: str = "",
    inherited_date: str = "",
    ticker_plugin: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    inherited_title = _clean_text(inherited_title)
    inherited_date = _date_from_text(inherited_date) if inherited_date else ""
    for anchor in re.finditer(r"(?is)<a\b(?P<attrs>[^>]*)>(?P<label>.*?)</a>", page_html):
        attrs = anchor.group("attrs")
        href_match = re.search(r"href=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        if not href_match:
            continue
        href = href_match.group(1)
        title_match = re.search(r"title=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        title = _clean_text(title_match.group(1)) if title_match else ""
        clean_label = _clean_text(anchor.group("label"))
        direct_searchable_text = f"{clean_label} {title} {href.replace('-', ' ').replace('_', ' ')} {page_url}"
        searchable_text = direct_searchable_text
        if not _classify_document_with_plugin(searchable_text, href, ticker_plugin):
            if not inherited_title or not _can_inherit_report_context(clean_label, title, href):
                continue
            searchable_text = f"{direct_searchable_text} {inherited_title}"
        date_text = _date_from_text(searchable_text) or inherited_date
        if not date_text:
            continue
        rows.append(
            {
                "title": _fallback_row_title(title, clean_label, inherited_title, searchable_text),
                "announcement_date": date_text,
                "url": urljoin(page_url, href),
                "fallback_page_url": page_url,
            }
        )
    for href, label in re.findall(
        r"(?is)<button\b[^>]+data-href=['\"]([^'\"]+)['\"][^>]*>(.*?)</button>",
        page_html,
    ):
        clean_label = _clean_text(label)
        direct_searchable_text = f"{clean_label} {href.replace('-', ' ').replace('_', ' ')}"
        searchable_text = direct_searchable_text
        if not _classify_document_with_plugin(searchable_text, href, ticker_plugin):
            if not inherited_title or not _can_inherit_report_context(clean_label, "", href):
                continue
            searchable_text = f"{direct_searchable_text} {inherited_title}"
        date_text = _date_from_text(searchable_text) or inherited_date
        if not date_text:
            continue
        rows.append(
            {
                "title": _fallback_row_title(clean_label, inherited_title, searchable_text),
                "announcement_date": date_text,
                "url": urljoin(page_url, href),
                "fallback_page_url": page_url,
            }
        )
    return rows


def _fallback_row_sort_key(
    row: dict[str, Any],
    ticker_plugin: dict[str, Any] | None = None,
) -> tuple[datetime, int, int, str]:
    date_text = str(row.get("announcement_date") or "")
    try:
        parsed_date = _parse_date(date_text)
    except ValueError:
        parsed_date = datetime.min
    url = str(row.get("url") or "")
    title = str(row.get("title") or "")
    document_type = _classify_document_with_plugin(
        f"{title} {url.replace('-', ' ').replace('_', ' ')}",
        url,
        ticker_plugin,
    )
    role = _document_role(document_type, url=url, title=title)
    if _is_pdf_like_url(url):
        asset_rank = 0
    elif re.search(r"/(?:download|downloads|content/dam|documents?)/", url.lower()):
        asset_rank = 1
    else:
        asset_rank = 2
    return (parsed_date, -asset_rank, -DOCUMENT_ROLE_RANK.get(role, 99), url)


def _allowed_by_plugin_asset_pattern(row: dict[str, Any], ticker_plugin: dict[str, Any] | None) -> bool:
    haystack = f"{row.get('title', '')} {row.get('url', '')}".lower()
    for pattern in _plugin_list(_plugin_source_hints(ticker_plugin), "allow_asset_patterns"):
        if re.search(str(pattern), haystack, re.IGNORECASE):
            return True
    return False


def _allowed_fallback_document_asset(row: dict[str, Any], ticker_plugin: dict[str, Any] | None = None) -> bool:
    haystack = f"{row.get('title', '')} {row.get('url', '')}".lower()
    if _allowed_by_plugin_asset_pattern(row, ticker_plugin):
        return True
    if re.search(r"\.(?:zip|xml|xhtml|xlsx?|csv)(?:[?#].*)?$", haystack):
        return False
    excluded_report_terms = [
        "economic contribution",
        "economiccontribution",
        "climate transition",
        "climatetransition",
        "sustainability report",
        "reportextract",
        "report extract",
    ]
    return not any(term in haystack for term in excluded_report_terms)


def _prefilter_fallback_rows(
    rows: list[dict[str, Any]],
    ticker_plugin: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    seen_roles: set[str] = set()
    sorted_rows = sorted(
        [row for row in rows if _allowed_fallback_document_asset(row, ticker_plugin)],
        key=lambda row: _fallback_row_sort_key(row, ticker_plugin),
        reverse=True,
    )
    for row in sorted_rows:
        url = str(row.get("url") or "")
        title = str(row.get("title") or "")
        document_type = _classify_document_with_plugin(
            f"{title} {url.replace('-', ' ').replace('_', ' ')}",
            url,
            ticker_plugin,
        )
        role = _document_role(document_type, url=url, title=title)
        role_key = role if role in FINANCIAL_DOCUMENT_ROLES else document_type or url
        if role_key in FINANCIAL_DOCUMENT_ROLES and role_key in seen_roles:
            continue
        if role_key in FINANCIAL_DOCUMENT_ROLES:
            seen_roles.add(role_key)
        selected.append(row)
    return selected


def _fallback_page_urls(
    asx_code: str,
    identity: dict[str, Any] | None,
    ticker_plugin: dict[str, Any] | None = None,
) -> list[str]:
    urls = [ASX_COMPANY_PAGE_URL.format(code=asx_code)]
    identity = identity or {}
    for key in ("investor_relations_url", "investorRelationsUrl", "ir_url", "investors_url"):
        url = identity.get(key)
        if url:
            urls.append(str(url))
    hints = _plugin_source_hints(ticker_plugin)
    urls.extend(str(url) for url in _plugin_list(hints, "fallback_page_urls") if url)
    urls.extend(str(url) for url in _plugin_list(hints, "official_urls") if url)
    urls.extend(_load_known_asx_ir_urls().get(asx_code, []))
    return list(dict.fromkeys(urls))


def _parse_simple_ir_yaml(raw: str) -> dict[str, list[str]]:
    parsed: dict[str, list[str]] = {}
    current = ""
    for raw_line in raw.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not raw_line.startswith((" ", "\t")) and line.endswith(":"):
            current = line[:-1].strip().upper()
            parsed.setdefault(current, [])
            continue
        if current and line.startswith("- "):
            parsed.setdefault(current, []).append(line[2:].strip())
    return {key: [url for url in urls if url] for key, urls in parsed.items()}


def _load_known_asx_ir_urls(path: Path = ASX_IR_RULES_PATH) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    raw = path.read_text(encoding="utf-8")
    try:
        import yaml
    except ImportError:
        return _parse_simple_ir_yaml(raw)
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        return {}
    parsed: dict[str, list[str]] = {}
    for key, value in data.items():
        if isinstance(value, list):
            parsed[str(key).upper()] = [str(url) for url in value if url]
    return parsed


def _load_metric_profiles(path: Path = ASX_METRIC_PROFILE_PATH) -> dict[str, dict[str, dict[str, Any]]]:
    if not path.exists():
        return {}
    raw = path.read_text(encoding="utf-8")
    try:
        import yaml
    except ImportError:
        return {}
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        return {}
    profiles: dict[str, dict[str, dict[str, Any]]] = {}
    for sector, sector_profiles in data.items():
        if not isinstance(sector_profiles, dict):
            continue
        profiles[str(sector)] = {
            str(metric_name): profile
            for metric_name, profile in sector_profiles.items()
            if isinstance(profile, dict)
        }
    return profiles


def _ticker_plugin_path(ticker: str, plugin_dir: Path = ASX_TICKER_PLUGIN_DIR) -> Path:
    symbol = ticker.upper().strip()
    if not symbol.endswith(".AX"):
        symbol = f"{normalize_asx_code(symbol)}.AX"
    return plugin_dir / f"{symbol}.yaml"


def _load_ticker_plugin(ticker: str, plugin_dir: Path = ASX_TICKER_PLUGIN_DIR) -> dict[str, Any]:
    path = _ticker_plugin_path(ticker, plugin_dir)
    if not path.exists():
        return {}
    try:
        import yaml
    except ImportError:
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        return {}
    plugin = deepcopy(data)
    plugin.setdefault("ticker", _ticker_plugin_path(ticker, plugin_dir).stem)
    plugin["_plugin_path"] = str(path)
    return plugin


def _plugin_source_hints(ticker_plugin: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(ticker_plugin, dict):
        return {}
    hints = ticker_plugin.get("source_hints") or {}
    return hints if isinstance(hints, dict) else {}


def _plugin_list(container: dict[str, Any], key: str) -> list[Any]:
    value = container.get(key)
    return value if isinstance(value, list) else []


def _plugin_metric_profile(ticker_plugin: dict[str, Any] | None, metric_name: str) -> dict[str, Any]:
    if not isinstance(ticker_plugin, dict):
        return {}
    metrics = ticker_plugin.get("metrics") or {}
    if not isinstance(metrics, dict):
        return {}
    profile = metrics.get(metric_name) or {}
    return profile if isinstance(profile, dict) else {}


def _merge_unique_list(left: list[Any], right: list[Any]) -> list[Any]:
    merged: list[Any] = []
    seen: set[str] = set()
    for item in [*left, *right]:
        key = str(item)
        if key in seen:
            continue
        seen.add(key)
        merged.append(item)
    return merged


def _merge_metric_profile(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    if not overlay:
        return base
    merged = deepcopy(base)
    list_keys = {
        "accepted_labels",
        "accepted_row_labels",
        "accepted_column_labels",
        "accepted_units",
        "accepted_value_patterns",
        "accepted_statuses",
        "direct_value_patterns",
        "preferred_value_type",
        "required_nearby_terms",
        "rejected_nearby_terms",
        "hard_rejected_nearby_terms",
        "rejected_column_labels",
        "preferred_sections",
        "preferred_tables",
        "target_sections",
        "target_rows",
        "reject_sections",
        "reject_contexts",
        "validation_rules",
    }
    for key, value in overlay.items():
        if key in {"fixture_snippets", "expected_outputs"}:
            continue
        if key == "direct_value_patterns" and isinstance(value, list):
            merged["direct_value_patterns"] = _merge_unique_list(list(merged.get("direct_value_patterns") or []), value)
            merged["accepted_value_patterns"] = _merge_unique_list(list(merged.get("accepted_value_patterns") or []), value)
            continue
        if key in list_keys and isinstance(value, list):
            merged[key] = _merge_unique_list(list(merged.get(key) or []), value)
        elif isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = {**merged[key], **value}
        else:
            merged[key] = deepcopy(value)
    return merged


def _metric_profiles_for_sector(sector: str) -> dict[str, dict[str, Any]]:
    return _load_metric_profiles().get(sector, {})


def _sector_for_asx_code(asx_code: str) -> str:
    return ASX_SECTOR_BY_CODE.get(asx_code.upper(), "general")


def _section_unavailable(
    *,
    section_name: str,
    source: dict[str, Any],
    supports_claims: list[str],
    reason: str,
    section_type: str | None = None,
) -> dict[str, Any]:
    return {
        "section_name": section_name,
        "section_type": section_type or section_name,
        "status": "unavailable",
        "source_type": source["source_type"],
        "filing_date": source["announcement_date"],
        "url": source.get("url", ""),
        "excerpt": "",
        "supports_claims": supports_claims,
        "unavailable_reason": reason,
        "evidence_gap": reason,
    }


def _token_count_between(left: str, right: str) -> int:
    return len(re.findall(r"\w+", left + " " + right))


def _sentences(text: str) -> list[str]:
    clean = _clean_text(text)
    pieces = re.split(r"(?<=[.!?])\s+|\n+", clean)
    return [piece.strip() for piece in pieces if piece.strip()]


def _is_navigation_or_toc(text: str) -> bool:
    lower = text.lower()
    toc_hits = sum(1 for term in ["contents", "table of contents", "directors report", "financial statements"] if term in lower)
    nav_hits = sum(
        1
        for term in [
            "home",
            "search",
            "contact us",
            "reports and presentations",
            "shareholder services",
            "downloads",
            "read more",
        ]
        if term in lower
    )
    numbered_sections = len(re.findall(r"\b\d{1,2}\s+[A-Z][A-Za-z /&-]{3,30}", text))
    return (toc_hits >= 1 and numbered_sections >= 3) or nav_hits >= 4


def _profile_for_metric(metric_name: str, ticker_plugin: dict[str, Any] | None = None) -> dict[str, Any]:
    plugin_profile = _plugin_metric_profile(ticker_plugin, metric_name)
    for sector_profiles in _load_metric_profiles().values():
        profile = sector_profiles.get(metric_name)
        if profile:
            return _merge_metric_profile(profile, plugin_profile)
    for specs in ASX_SECTOR_METRIC_PATTERNS.values():
        for name, label, pattern, _supports_claims in specs:
            if name == metric_name:
                return _merge_metric_profile(
                    {
                    "accepted_labels": [label, name.replace("_", " ")],
                    "accepted_units": ["%", "bps", "$m", "$bn", "m", "bn", "cents"],
                    "accepted_value_patterns": [
                        r"\b(?:US\$|A\$|\$)?\d+(?:\.\d+)?\s*(?:bn|m|bps|%|per cent|cents|mt|kt|moz)\b"
                    ],
                    "required_nearby_terms": [],
                    "rejected_nearby_terms": [],
                    "max_label_value_distance_tokens": 10,
                    "direction_rules": {"supportive": ["increased", "higher"], "adverse": ["decreased", "lower"]},
                    "legacy_pattern": pattern,
                    },
                    plugin_profile,
                )
    return {}


def _profile_for_metric_context(metric_name: str, ticker_plugin: dict[str, Any] | None = None) -> dict[str, Any]:
    try:
        return _profile_for_metric(metric_name, ticker_plugin)
    except TypeError:
        if ticker_plugin:
            raise
        return _profile_for_metric(metric_name)


def _label_regex(label: str) -> str:
    if label.upper() == label and len(label) <= 5:
        return rf"\b{re.escape(label)}\b"
    if label.strip().lower() == "cash":
        return r"\bcash\b"
    return re.escape(label).replace(r"\ ", r"\s+")


def _label_matches(text: str, profile: dict[str, Any]) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    for label in profile.get("accepted_labels", []) or []:
        matches.extend(re.finditer(_label_regex(str(label)), text, re.IGNORECASE))
    return sorted(matches, key=lambda match: match.start())


def _value_matches(text: str, profile: dict[str, Any]) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    for pattern in profile.get("accepted_value_patterns", []) or []:
        matches.extend(re.finditer(str(pattern), text, re.IGNORECASE))
    generic_pattern = (
        r"(?:US\$|A\$|\$)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\s*"
        r"(?:bps|bpts|%|per cent|cents|cps|bn|m|billion|million|mt|kt|moz|mmboe|boe|centres|/(?:t|tonne|lb|oz|boe))"
    )
    for match in re.finditer(generic_pattern, text, re.IGNORECASE):
        _clean_value, unit = _clean_value_and_unit(match.group(0))
        if _unit_compatible(unit, profile) and all(match.span() != existing.span() for existing in matches):
            matches.append(match)
    return sorted(matches, key=lambda match: match.start())


def _profile_terms(profile: dict[str, Any], key: str) -> list[str]:
    return [str(term).strip().lower() for term in profile.get(key, []) or [] if str(term).strip()]


def _term_present(term: str, text: str) -> bool:
    if not term:
        return True
    normalized_text = text.replace("_", " ")
    if re.fullmatch(r"[\w ]+", term):
        return bool(re.search(rf"\b{re.escape(term)}\b", normalized_text, re.IGNORECASE))
    return term.lower() in normalized_text.lower()


def _required_terms_present(text: str, profile: dict[str, Any]) -> bool:
    required = _profile_terms(profile, "required_nearby_terms")
    if not required:
        return True
    return any(_term_present(term, text) for term in required)


def _rejected_terms_present(text: str, profile: dict[str, Any]) -> list[str]:
    return [term for term in _profile_terms(profile, "rejected_nearby_terms") if _term_present(term, text)]


def _hard_rejected_terms_present(text: str, profile: dict[str, Any]) -> list[str]:
    return [term for term in _profile_terms(profile, "hard_rejected_nearby_terms") if _term_present(term, text)]


def _hard_rejected_for_candidate(text: str, window: str, profile: dict[str, Any]) -> list[str]:
    scope = str(profile.get("hard_reject_scope") or "nearby").lower()
    haystack = text if scope == "candidate_text" else window
    return _hard_rejected_terms_present(haystack, profile)


def _clean_value_and_unit(raw: str) -> tuple[str, str]:
    value_match = re.search(r"(?P<negative>\()?(?:US\$|A\$|\$)?(?P<value>(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)", raw, re.IGNORECASE)
    if value_match:
        clean_value = value_match.group("value").replace(",", "")
        if value_match.group("negative"):
            clean_value = f"-{clean_value}"
    else:
        clean_value = "unavailable"
    lower = raw.lower().replace(" ", "")
    if "bpts" in lower or "bps" in lower:
        unit = "bps"
    elif "percent" in lower or "percent" in lower.replace("per", "per ") or "%" in raw or "per cent" in raw.lower():
        unit = "per cent" if "per cent" in raw.lower() else "%"
    elif re.search(r"(?:usc|uscent|uscents|us cents)/?lb", lower):
        unit = "USc/lb"
    elif re.search(r"(?:^|[^a-z])c/lb|cents/lb|centsperlb|centsperpound", lower):
        unit = "c/lb" if "c/lb" in lower else "cents/lb"
    elif "cents" in lower or "cps" in lower:
        unit = "cents" if "cents" in lower else "cps"
    elif ("us$" in lower or "a$" in lower) and re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower):
        denominator = re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower)
        suffix = denominator.group(0).replace("tonne", "t") if denominator else "/t"
        unit = f"US${suffix}"
    elif "$" in raw and re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower):
        denominator = re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower)
        suffix = denominator.group(0).replace("tonne", "t") if denominator else "/t"
        unit = f"${suffix}"
    elif "us$" in lower and ("bn" in lower or "billion" in lower):
        unit = "US$bn"
    elif "us$" in lower and ("m" in lower or "million" in lower):
        unit = "US$m"
    elif ("a$" in lower or "$" in raw) and ("bn" in lower or "billion" in lower):
        unit = "$bn"
    elif ("a$" in lower or "$" in raw) and ("m" in lower or "million" in lower):
        unit = "$m"
    elif "us$" in lower or "a$" in lower or "$" in raw:
        unit = "$"
    elif lower.endswith("bn") or lower.endswith("billion"):
        unit = "bn"
    elif lower.endswith("m") or lower.endswith("million"):
        unit = "m"
    elif lower.endswith("mt"):
        unit = "mt"
    elif lower.endswith("kt"):
        unit = "kt"
    elif lower.endswith("moz"):
        unit = "moz"
    elif lower.endswith("mmboe"):
        unit = "mmboe"
    elif lower.endswith("boe"):
        unit = "boe"
    elif lower.endswith("centres"):
        unit = "centres"
    else:
        unit = "unit unavailable"
    return clean_value, unit


def _numeric_value_spans(text: str) -> list[re.Match[str]]:
    pattern = rf"\(?-?(?:US\$|A\$|\$)?(?:\d{{1,3}}(?:,\d{{3}})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|USc/lb|c/lb|US cents/lb|cents/lb|cents|cps|bn|m|billion|million|mt|kt|moz|mmboe|boe|centres|/{PRICE_DENOMINATOR_PATTERN})?"
    return [match for match in re.finditer(pattern, text, re.IGNORECASE) if re.search(r"\d", match.group(0))]


def _dense_table_row_signal(text: str) -> bool:
    clean = _clean_text(text)
    lower = clean.lower()
    numeric_count = len(_numeric_value_spans(clean))
    label_hits = sum(1 for label in DENSE_TABLE_ROW_LABELS if re.search(rf"\b{re.escape(label)}\b", lower))
    variance_style = bool(re.search(r"\([\d,]+(?:\.\d+)?\)", clean)) or len(re.findall(r"\bFY\d{2,4}\b|\b20\d{2}\b", clean, re.IGNORECASE)) >= 2
    repeated_row_values = bool(re.search(r"\b[A-Za-z][A-Za-z /&-]{2,}\s+\(?[\d,]+(?:\.\d+)?\)?\s+\(?[\d,]+(?:\.\d+)?\)?\s+\(?-?[\d,]+(?:\.\d+)?\)?", clean))
    return numeric_count > 4 and label_hits >= 2 and (variance_style or repeated_row_values)


def _first_metric_support_sentence(clean: str, profile: dict[str, Any]) -> str:
    support_sentence = clean[:240]
    for sentence in _sentences(clean):
        if _label_matches(sentence, profile):
            return sentence[:240]
    return support_sentence


def _table_row_unparsed_result(base: dict[str, Any], clean: str, profile: dict[str, Any]) -> dict[str, Any]:
    support_sentence = _first_metric_support_sentence(clean, profile)
    direction = _direction_from_profile(support_sentence, profile)
    return {
        **base,
        "metric_value_status": "table_row_unparsed",
        "association_score": 45,
        "association_reason": "dense table-like row contains multiple numeric values and financial row labels; clean value withheld until row/column mapping is parsed",
        "supporting_sentence": support_sentence,
        "comparison_basis": "dense table-like row requires parsed row/column mapping before value use",
        "direction": direction if direction != "neutral" else "neutral",
        "confidence": "low",
        "confidence_reason": "metric row appears present, but value association is unsafe without row/column mapping",
    }


def _numeric_cell_value(cell: str, inferred_unit: str) -> tuple[str, str] | None:
    if re.fullmatch(r"FY?\d{2,4}", cell.strip(), re.IGNORECASE):
        return None
    value_match = re.search(
        rf"\(?-?(?:US\$|A\$|\$)?(?:\d{{1,3}}(?:,\d{{3}})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|USc/lb|c/lb|US cents/lb|cents/lb|cents|cps|bn|m|mt|kt|moz|mmboe|boe|centres|/{PRICE_DENOMINATOR_PATTERN})?",
        cell,
        re.IGNORECASE,
    )
    if not value_match:
        return None
    clean_value, unit = _clean_value_and_unit(value_match.group(0))
    if unit == "unit unavailable":
        unit = inferred_unit
    if unit == "unit unavailable":
        return None
    return clean_value, unit


def _unit_from_column_label(label: str, fallback: str = "unit unavailable") -> str:
    lower = label.lower()
    if re.search(r"(?:usc|us cents)\s*/\s*lb", lower):
        return "USc/lb"
    if re.search(r"\bc\s*/\s*lb\b", lower):
        return "c/lb"
    if re.search(r"cents\s*/\s*lb", lower):
        return "cents/lb"
    if "us$/" in lower and re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower):
        denominator = re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower)
        return f"US${denominator.group(0).replace('tonne', 't')}" if denominator else "US$/t"
    if "$/" in lower or re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower):
        denominator = re.search(rf"/{PRICE_DENOMINATOR_PATTERN}\b", lower)
        return f"${denominator.group(0).replace('tonne', 't')}" if denominator else "$/t"
    if "us$m" in lower:
        return "US$m"
    if "us$bn" in lower:
        return "US$bn"
    if "$m" in lower or "a$m" in lower:
        return "$m"
    if "$bn" in lower or "a$bn" in lower:
        return "$bn"
    if "bps" in lower or "bpts" in lower:
        return "bps"
    if "%" in lower or "per cent" in lower:
        return "%"
    if "cents" in lower:
        return "cents"
    if "centres" in lower:
        return "centres"
    return fallback


def _parse_structured_table_line(line: str) -> tuple[dict[str, str], list[str]]:
    row = line.strip()
    metadata: dict[str, str] = {
        "source_page": "unavailable",
        "table_title": "unavailable",
        "table_index": "unavailable",
        "row_index": "unavailable",
    }
    if row.startswith(TABLE_ROW_MARKER):
        prefix, _separator, cell_text = row.partition("|")
        for key, value in re.findall(r"\b(page|table|row|title)=([^\s|]+)", prefix):
            if key == "page":
                metadata["source_page"] = value
            elif key == "title":
                metadata["table_title"] = value
            elif key == "table":
                metadata["table_index"] = value
            elif key == "row":
                metadata["row_index"] = value
        row = cell_text
    cells = [_clean_text(cell) for cell in row.split("|")]
    return metadata, cells


def _section_title_for_text(text: str) -> str:
    clean = _clean_text(text)
    for section_name, pattern, _supports_claims in SECTION_PATTERNS:
        if re.search(pattern, clean, re.IGNORECASE):
            return section_name
    if _is_navigation_or_toc(clean):
        return "navigation_or_table_of_contents"
    return "unclassified_text"


def _text_blocks_from_page_text(text: str) -> list[dict[str, str]]:
    sentences = _sentences(text)
    if not sentences and text.strip():
        sentences = [_clean_text(text)]
    blocks: list[dict[str, str]] = []
    current: list[str] = []
    current_length = 0
    carried_section_title = ""
    for sentence in sentences:
        if current and current_length + len(sentence) > DOCUMENT_TEXT_BLOCK_CHARS:
            block_text = _clean_text(" ".join(current))
            section_title = _section_title_for_text(block_text)
            if section_title == "unclassified_text" and carried_section_title:
                section_title = carried_section_title
            blocks.append({"section_title": section_title, "text": block_text})
            current = []
            current_length = 0
        current.append(sentence)
        current_length += len(sentence) + 1
        sentence_title = _section_title_for_text(sentence)
        if sentence_title not in {"unclassified_text", "navigation_or_table_of_contents"}:
            carried_section_title = sentence_title
    if current:
        block_text = _clean_text(" ".join(current))
        section_title = _section_title_for_text(block_text)
        if section_title == "unclassified_text" and carried_section_title:
            section_title = carried_section_title
        blocks.append({"section_title": section_title, "text": block_text})
    return blocks


def _new_structured_page(page_number: str) -> dict[str, Any]:
    return {"page_number": page_number, "text_blocks": [], "tables": []}


def _build_document_structure(text: str) -> dict[str, Any]:
    pages_by_number: dict[str, dict[str, Any]] = {}
    table_lookup: dict[tuple[str, str, str], dict[str, Any]] = {}
    current_page = "1"
    text_lines_by_page: dict[str, list[str]] = {"1": []}

    def page_for(page_number: str) -> dict[str, Any]:
        page = pages_by_number.get(page_number)
        if page is None:
            page = _new_structured_page(page_number)
            pages_by_number[page_number] = page
        text_lines_by_page.setdefault(page_number, [])
        return page

    page_for(current_page)
    for raw_line in text.splitlines() or [text]:
        line = raw_line.strip()
        if not line:
            continue
        page_marker = re.match(rf"^{re.escape(PDF_PAGE_MARKER)}\s+page=(?P<page>\d+)", line)
        if page_marker:
            current_page = page_marker.group("page")
            page_for(current_page)
            continue
        if line.startswith(TABLE_ROW_MARKER):
            metadata, cells = _parse_structured_table_line(line)
            page_number = metadata.get("source_page", "unavailable")
            if page_number == "unavailable":
                page_number = current_page
                metadata["source_page"] = page_number
            page = page_for(page_number)
            table_key = (
                page_number,
                metadata.get("table_index", "unavailable"),
                metadata.get("table_title", "unavailable"),
            )
            table = table_lookup.get(table_key)
            if table is None:
                table = {
                    "source_page": page_number,
                    "table_index": metadata.get("table_index", "unavailable"),
                    "table_title": metadata.get("table_title", "unavailable"),
                    "section_title": _section_title_for_text(metadata.get("table_title", "")),
                    "rows": [],
                }
                table_lookup[table_key] = table
                page["tables"].append(table)
            table["rows"].append(
                {
                    "row_index": metadata.get("row_index", "unavailable"),
                    "cells": cells,
                    "raw_row_text": " | ".join(cells),
                }
            )
            continue
        text_lines_by_page.setdefault(current_page, []).append(line)

    for page_number, lines in text_lines_by_page.items():
        if not lines:
            continue
        page = page_for(page_number)
        page["text_blocks"].extend(_text_blocks_from_page_text("\n".join(lines)))

    ordered_pages = sorted(
        pages_by_number.values(),
        key=lambda page: int(page["page_number"]) if str(page["page_number"]).isdigit() else 10_000,
    )
    return {
        "pages": ordered_pages,
        "page_count": len(ordered_pages),
        "table_count": len(table_lookup),
        "text_block_count": sum(len(page.get("text_blocks", [])) for page in ordered_pages),
    }


def _table_text_from_structured_table(table: dict[str, Any]) -> str:
    page_number = str(table.get("source_page") or "unavailable")
    table_index = str(table.get("table_index") or "unavailable")
    table_title = str(table.get("table_title") or "unavailable")
    rows = []
    for row in table.get("rows", []):
        cells = [str(cell) for cell in row.get("cells", [])]
        row_index = int(str(row.get("row_index") or "0")) if str(row.get("row_index") or "0").isdigit() else 0
        table_index_int = int(table_index) if table_index.isdigit() else 0
        rows.append(_format_structured_table_row(cells, int(page_number) if page_number.isdigit() else 0, table_index_int, row_index, table_title))
    return "\n".join(rows)


def _table_key(metadata: dict[str, str]) -> tuple[str, str]:
    return (metadata.get("source_page", "unavailable"), metadata.get("table_index", "unavailable"))


def _header_continuation_row(cells: list[str]) -> bool:
    if not cells:
        return False
    first_cell = cells[0].strip().lower()
    non_empty = [cell for cell in cells if cell.strip()]
    if first_cell and any(label in first_cell for label in DENSE_TABLE_ROW_LABELS):
        return False
    unit_cells = sum(
        1
        for cell in cells
        if re.search(rf"\b(?:\$m|\$bn|bps|bpts|%|cents|mt|kt|moz|/{PRICE_DENOMINATOR_PATTERN})\b|[$%]", cell, re.IGNORECASE)
    )
    period_cells = sum(1 for cell in cells if re.search(r"\b(?:FY)?20\d{2}\b|\bFY\d{2}\b|current|prior|variance|change", cell, re.IGNORECASE))
    return bool(unit_cells or period_cells) and (not first_cell or len(non_empty) >= 2)


def _merge_table_header_rows(existing: list[str], continuation: list[str]) -> list[str]:
    width = max(len(existing), len(continuation))
    merged: list[str] = []
    for index in range(width):
        left = existing[index] if index < len(existing) else ""
        right = continuation[index] if index < len(continuation) else ""
        if not left:
            merged.append(right)
        elif not right or right.lower() in left.lower():
            merged.append(left)
        else:
            merged.append(_clean_text(f"{left} {right}"))
    return merged


def _profile_row_labels(profile: dict[str, Any]) -> list[str]:
    row_labels = profile.get("accepted_row_labels") or profile.get("accepted_labels") or []
    return [str(label) for label in row_labels if str(label).strip()]


def _profile_contextual_row_labels(profile: dict[str, Any]) -> list[str]:
    return [str(label) for label in profile.get("contextual_row_labels", []) or [] if str(label).strip()]


def _row_label_matches(row_label: str, profile: dict[str, Any]) -> bool:
    row_profile = {**profile, "accepted_labels": _profile_row_labels(profile)}
    return bool(_label_matches(row_label, row_profile))


def _contextual_row_label_matches(row_label: str, profile: dict[str, Any]) -> bool:
    labels = _profile_contextual_row_labels(profile)
    if not labels:
        return False
    row_profile = {**profile, "accepted_labels": labels}
    return bool(_label_matches(row_label, row_profile))


def _realised_price_context_present(text: str) -> bool:
    lower = _clean_text(text.replace("_", " ")).lower()
    return any(term in lower for term in BHP_REALISED_PRICE_CONTEXT_TERMS)


def _contextual_row_allowed(metric_name: str, row_label: str, context: str, profile: dict[str, Any]) -> bool:
    if metric_name != "realised_price":
        return False
    if not _realised_price_context_present(context):
        return False
    if _contextual_row_label_matches(row_label, profile):
        return True
    return row_label.strip().lower() in BHP_COMMODITY_ROW_LABELS


def _commodity_exposure_numeric_table_allowed(
    *,
    row_label: str,
    column_label: str,
    unit: str,
    metadata: dict[str, str],
    row_context: str,
) -> bool:
    context = _clean_text(
        " ".join(
            [
                row_label,
                column_label,
                metadata.get("table_title", ""),
                row_context,
            ]
        ).replace("_", " ")
    ).lower()
    has_commodity_row = any(commodity in row_label.lower() for commodity in BHP_COMMODITY_ROW_LABELS)
    explicit_mix_context = any(
        term in context
        for term in (
            "revenue by commodity",
            "ebitda by commodity",
            "production by commodity",
            "commodity mix",
            "commodity exposure",
            "commodity portfolio",
            "portfolio mix",
        )
    )
    return has_commodity_row and explicit_mix_context


def _column_label_allowed(column_label: str, profile: dict[str, Any]) -> bool:
    lower = column_label.lower()
    if re.fullmatch(r"\s*notes?\s*", lower):
        return False
    if _looks_like_paragraph_fragment(column_label):
        return False
    normalized = re.sub(r"\bfy(\d{2})\b", lambda match: f"fy20{match.group(1)} 20{match.group(1)}", lower)
    rejected = [str(label).lower() for label in profile.get("rejected_column_labels", []) or []]
    if any(label and (label in lower or label in normalized) for label in rejected):
        return False
    accepted = [str(label).lower() for label in profile.get("accepted_column_labels", []) or []]
    return not accepted or any(label and (label in lower or label in normalized) for label in accepted)


def _looks_like_paragraph_fragment(label: str) -> bool:
    clean = _clean_text(label)
    words = re.findall(r"\w+", clean)
    if len(clean) > 110 or len(words) > 14:
        return True
    lower = clean.lower()
    paragraph_terms = [
        "reflecting",
        "due to",
        "geopolitical",
        "tensions",
        "performance",
        "practices",
        "outlook",
        "originatio",
        "financial report",
    ]
    return len(words) > 7 and any(term in lower for term in paragraph_terms)


def _value_type_from_column_label(column_label: str, index: int) -> str:
    lower = column_label.lower()
    if any(term in lower for term in ["variance %", "variance_percent", "change %", "% change"]):
        return "variance_percent"
    if any(term in lower for term in ["variance", "change"]):
        return "variance_value"
    if re.search(r"\bfy?25\b|\b2025\b", lower) or "current" in lower:
        return "current_period_value"
    if re.search(r"\bfy?24\b|\b2024\b", lower) or "prior" in lower:
        return "prior_period_value"
    if "%" in lower:
        return "variance_percent"
    if index == 1:
        return "current_period_value"
    if index == 2:
        return "prior_period_value"
    if index == 3:
        return "variance_value"
    return "cell_value"


def _preferred_value_types(profile: dict[str, Any]) -> list[str]:
    preferred = profile.get("preferred_value_type") or ["current_period_value", "variance_percent", "variance_value"]
    return [str(item) for item in preferred if str(item).strip()]


def _table_mapping_score(
    *,
    row_label: str,
    column_label: str,
    value_type: str,
    unit: str,
    profile: dict[str, Any],
    has_header: bool,
    metadata: dict[str, str],
) -> tuple[int, str]:
    score = 30
    reasons = []
    if _row_label_matches(row_label, profile):
        score += 30
        reasons.append("accepted row label")
    if has_header:
        score += 15
        reasons.append("header row available")
    if _column_label_allowed(column_label, profile):
        score += 10
        reasons.append("accepted column label")
    else:
        score -= 30
        reasons.append("rejected column label")
    if value_type in _preferred_value_types(profile):
        score += 10
        reasons.append(f"preferred value type {value_type}")
    if _unit_compatible(unit, profile):
        score += 10
        reasons.append(f"unit {unit} compatible")
    else:
        score -= 20
        reasons.append(f"unit {unit} incompatible")
    if metadata.get("source_page", "unavailable") != "unavailable":
        score += 5
        reasons.append("source page preserved")
    return max(0, min(100, score)), "; ".join(reasons)


def _profile_string_list(profile: dict[str, Any], key: str) -> list[str]:
    return [str(term).strip() for term in profile.get(key, []) or [] if str(term).strip()]


def _target_rows_for_profile(profile: dict[str, Any]) -> list[str]:
    target_rows = _profile_string_list(profile, "target_rows")
    if target_rows:
        return target_rows
    return _profile_string_list(profile, "accepted_row_labels")


def _target_sections_for_profile(profile: dict[str, Any]) -> list[str]:
    return _merge_unique_list(
        _profile_string_list(profile, "target_sections"),
        _profile_string_list(profile, "preferred_sections"),
    )


def _term_hits(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if _term_present(term.lower(), text.lower())]


def _targeted_search_enabled(ticker_plugin: dict[str, Any] | None, profile: dict[str, Any]) -> bool:
    return bool(ticker_plugin and (_profile_string_list(profile, "target_rows") or _profile_string_list(profile, "target_sections")))


def _new_metric_diagnostics(
    *,
    ticker_plugin: dict[str, Any] | None,
    profile: dict[str, Any],
    targeted_search_attempted: bool,
) -> dict[str, Any]:
    return {
        "plugin_used": bool(ticker_plugin),
        "plugin_path": str((ticker_plugin or {}).get("_plugin_path") or "unavailable"),
        "targeted_search_attempted": targeted_search_attempted,
        "target_sections": _target_sections_for_profile(profile),
        "target_rows": _target_rows_for_profile(profile),
        "candidate_sections_seen": [],
        "candidate_rows_seen": [],
        "best_rejected_candidate": "unavailable",
        "best_rejected_source_page": "unavailable",
        "rejection_reason": "unavailable",
        "failure_type": "metric_not_present",
    }


def _record_diagnostic_seen(diagnostics: dict[str, Any], key: str, value: str) -> None:
    if not value or value == "unavailable":
        return
    values = diagnostics.setdefault(key, [])
    if value not in values:
        values.append(value)


def _set_diagnostic_rejection(
    diagnostics: dict[str, Any],
    *,
    candidate: str,
    source_page: str,
    reason: str,
    failure_type: str,
) -> None:
    if diagnostics.get("best_rejected_candidate") == "unavailable":
        diagnostics["best_rejected_candidate"] = candidate[:240]
        diagnostics["best_rejected_source_page"] = source_page
        diagnostics["rejection_reason"] = reason
        diagnostics["failure_type"] = failure_type


def _normalize_unit_for_comparison(unit: str) -> str:
    normalized = unit.strip().lower().replace(" ", "")
    normalized = normalized.replace("tonne", "t")
    if normalized in {"usc/lb", "uscents/lb", "uscent/lb"}:
        return "usc/lb"
    if normalized in {"uscentsperlb", "uscentperlb", "uscperlb"}:
        return "usc/lb"
    if normalized in {"uscents/lb", "usc/lb"}:
        return "usc/lb"
    if normalized in {"cents/lb", "centsperlb"}:
        return "cents/lb"
    if normalized == "clb":
        return "c/lb"
    return normalized


def _unit_compatible(unit: str, profile: dict[str, Any]) -> bool:
    accepted = {_normalize_unit_for_comparison(str(item)) for item in profile.get("accepted_units", []) or []}
    if not accepted:
        return True
    normalized = _normalize_unit_for_comparison(unit)
    if normalized in accepted:
        return True
    if normalized == "per cent" and "%" in accepted:
        return True
    return normalized in {"$m", "$bn"} and any(item in accepted for item in {normalized, f"a{normalized}", normalized[1:]})


def _value_validation_failure(clean_value: str, unit: str, profile: dict[str, Any]) -> str:
    validation = profile.get("value_validation") or {}
    if not isinstance(validation, dict):
        return ""
    try:
        numeric_value = float(str(clean_value).replace(",", ""))
    except ValueError:
        return ""
    normalized_unit = unit.lower()
    for rule in validation.get("ranges", []) or []:
        if not isinstance(rule, dict):
            continue
        units = {str(item).lower() for item in rule.get("units", []) or []}
        if units and normalized_unit not in units:
            continue
        min_value = rule.get("min")
        max_value = rule.get("max")
        if min_value is not None and numeric_value < float(min_value):
            return f"value {clean_value}{unit} below plugin validation minimum {min_value}"
        if max_value is not None and numeric_value > float(max_value):
            return f"value {clean_value}{unit} above plugin validation maximum {max_value}"
    return ""


def _flattened_table_column_labels(text: str, metric_name: str, profile: dict[str, Any]) -> list[str]:
    lower = text.lower()
    money_unit = "$M" if re.search(r"\$\s*m|\$m|a\$m|\bus\$m\b", text, re.IGNORECASE) else ""
    percent_unit = "%" if "%" in text or metric_name in {"arrears", "roe"} else ""
    value_unit = money_unit or percent_unit
    if re.search(r"\b30\s+jun\s+25\b.*\b30\s+jun\s+24\b", lower):
        labels = ["30 Jun 25", "30 Jun 24"]
    elif re.search(r"\bfy\s?25\b.*\bfy\s?24\b|\bfy2025\b.*\bfy2024\b", lower):
        labels = ["FY2025", "FY2024"]
    elif re.search(r"\b2025\b.*\b2024\b", lower):
        labels = ["2025", "2024"]
    else:
        labels = ["current_period_value", "prior_period_value"]
    if value_unit and not labels[0].endswith(value_unit):
        labels = [f"{label} {value_unit}" if not label.endswith("_value") else label for label in labels]
    if re.search(r"%\s*change|change\s*%", lower):
        labels.append("% change")
    elif "variance" in lower:
        labels.append("variance")
    return labels


def _infer_flattened_unit(metric_name: str, raw_value: str, column_label: str, text: str, profile: dict[str, Any]) -> str:
    _clean_value, unit = _clean_value_and_unit(raw_value)
    if unit != "unit unavailable":
        return unit
    column_unit = _unit_from_column_label(column_label)
    if column_unit != "unit unavailable":
        return column_unit
    accepted = {str(item).lower() for item in profile.get("accepted_units", []) or []}
    lower = text.lower()
    if metric_name in {"arrears", "roe"} and "%" in accepted:
        return "%"
    if metric_name in {"impairment", "capex"} and any(unit_name in accepted for unit_name in {"$m", "a$m", "us$m"}):
        return "$m"
    if re.search(r"\$\s*m|\$m|a\$m|\bus\$m\b", lower) and any(unit_name in accepted for unit_name in {"$m", "a$m", "us$m"}):
        return "$m"
    return "unit unavailable"


def _slice_flattened_row(text: str, label_match: re.Match[str]) -> str:
    tail = text[label_match.start() :]
    sentence_end = re.search(r"(?:(?<=\d)|(?<=\))|(?<=%))\.\s+(?=[A-Z])", tail)
    if sentence_end:
        return tail[: sentence_end.start()].strip(" .")
    return tail[:260].strip(" .")


def _numeric_match_is_period_fragment(text: str, match: re.Match[str]) -> bool:
    raw = match.group(0).strip().strip("()")
    if not re.fullmatch(r"\d{2,4}", raw):
        return False
    before = text[max(0, match.start() - 12) : match.start()].lower()
    after = text[match.end() : match.end() + 12].lower()
    if re.search(r"\bjun\s*$", before) or re.match(r"\s*jun\b", after):
        return True
    return raw in {"23", "24", "25", "2023", "2024", "2025"} and (
        re.search(r"\b(?:fy|year|weeks?|period)\s*$", before) or re.match(r"\s*(?:fy|year|weeks?|period)\b", after)
    )


def _row_value_prefix_too_noisy(value_text: str, first_value_start: int) -> bool:
    prefix = _clean_text(value_text[:first_value_start])
    if not prefix:
        return False
    words = re.findall(r"[A-Za-z]+", prefix)
    return len(words) > 3


def _extract_metric_from_flattened_financial_table(
    text: str,
    metric_name: str,
    profile: dict[str, Any],
    source_context: dict[str, Any],
) -> dict[str, Any]:
    target_rows = _target_rows_for_profile(profile)
    if not target_rows:
        return {}
    last_rejection: dict[str, Any] = {}
    for row_label_pattern in target_rows:
        for match in re.finditer(_label_regex(row_label_pattern), text, re.IGNORECASE):
            row_text = _slice_flattened_row(text, match)
            row_label = _clean_text(text[match.start() : match.end()])
            value_text = row_text[match.end() - match.start() :]
            value_matches = [
                value_match
                for value_match in _numeric_value_spans(value_text)
                if not _numeric_match_is_period_fragment(value_text, value_match)
            ]
            if not value_matches:
                last_rejection = {
                    "metric_value_status": "unavailable",
                    "failure_type": "row_column_mapping_missing",
                    "rejection_reason": "target row was present but no numeric values were found after the row label",
                    "raw_row_text": row_text,
                }
                continue
            if _row_value_prefix_too_noisy(value_text, value_matches[0].start()):
                last_rejection = {
                    "metric_value_status": "unavailable",
                    "failure_type": "row_column_mapping_missing",
                    "rejection_reason": "target row label appeared in a heading or grouped table label rather than a value row",
                    "raw_row_text": row_text,
                }
                continue
            if metric_name == "debt" and not _debt_balance_sheet_context_present(row_text):
                last_rejection = {
                    "metric_value_status": "unavailable",
                    "failure_type": "value_rejected_by_profile",
                    "rejection_reason": "debt metric requires debt, borrowings, leverage, gearing, or cash plus debt context",
                    "raw_row_text": row_text,
                }
                continue
            column_labels = _flattened_table_column_labels(text, metric_name, profile)
            metadata = {"source_page": str(source_context.get("source_page") or "unavailable")}
            values: list[dict[str, str]] = []
            for index, value_match in enumerate(value_matches[: max(2, len(column_labels))], start=1):
                raw_value = value_match.group(0).strip()
                column_label = column_labels[index - 1] if index - 1 < len(column_labels) else f"value_{index}"
                inferred_unit = _infer_flattened_unit(metric_name, raw_value, column_label, text, profile)
                parsed = _numeric_cell_value(raw_value, inferred_unit)
                if not parsed:
                    continue
                clean_value, unit = parsed
                value_type = _value_type_from_column_label(column_label, index)
                if not _unit_compatible(unit, profile):
                    continue
                if metric_name == "commodity_exposure" and not _commodity_exposure_numeric_table_allowed(
                    row_label=row_label,
                    column_label=column_label,
                    unit=unit,
                    metadata={
                        "source_page": str(source_context.get("source_page") or "unavailable"),
                        "table_title": str(source_context.get("section_title") or source_context.get("table_title") or ""),
                    },
                    row_context=row_text,
                ):
                    continue
                validation_failure = _value_validation_failure(clean_value, unit, profile)
                if validation_failure:
                    last_rejection = {
                        "metric_value_status": "unavailable",
                        "failure_type": "value_rejected_by_profile",
                        "rejection_reason": validation_failure,
                        "raw_row_text": row_text,
                    }
                    continue
                if not _column_label_allowed(column_label, profile):
                    continue
                mapping_score, mapping_reason = _table_mapping_score(
                    row_label=row_label,
                    column_label=column_label,
                    value_type=value_type,
                    unit=unit,
                    profile=profile,
                    has_header=column_label not in {"current_period_value", "prior_period_value"},
                    metadata=metadata,
                )
                values.append(
                    {
                        "clean_value": clean_value,
                        "unit": unit,
                        "column_label": column_label,
                        "value_type": value_type,
                        "cell_value": raw_value,
                        "table_mapping_confidence": str(mapping_score),
                        "table_mapping_reason": mapping_reason,
                    }
                )
            if not values:
                last_rejection = {
                    "metric_value_status": "unavailable",
                    "failure_type": "row_column_mapping_missing",
                    "rejection_reason": "target row values were present but no value satisfied unit, column, and profile rules",
                    "raw_row_text": row_text,
                }
                continue
            preferred_types = _preferred_value_types(profile)
            preferred = next((item for value_type in preferred_types for item in values if item["value_type"] == value_type), values[0])
            value_fields = {item["value_type"]: item["clean_value"] for item in values}
            value_column_labels = {item["value_type"]: item["column_label"] for item in values}
            current_period_value = value_fields.get("current_period_value", "unavailable")
            prior_period_value = value_fields.get("prior_period_value", "unavailable")
            variance_value = value_fields.get("variance_value", "unavailable")
            variance_percent = value_fields.get("variance_percent", "unavailable")
            comparison_reference = (
                value_column_labels.get("prior_period_value", "not specified")
                if prior_period_value != "unavailable"
                else "not specified"
            )
            mapping_score = int(preferred["table_mapping_confidence"])
            return {
                "score": max(88, mapping_score),
                "clean_metric_value": preferred["clean_value"],
                "value_unit": preferred["unit"],
                "value_context": "targeted plugin flattened table row/column association",
                "metric_value_status": "value_extracted",
                "association_score": max(88, mapping_score),
                "association_reason": "targeted ticker plugin matched a configured row inside a configured section before generic scoring",
                "period_reference": preferred["column_label"],
                "comparison_reference": comparison_reference,
                "supporting_sentence": row_text,
                "comparison_basis": "current/prior period values parsed from flattened financial table text",
                "direction": _direction_from_profile(row_text, profile),
                "confidence": "medium",
                "confidence_reason": "clean value accepted because ticker plugin target row, section context, and row/column mapping were satisfied",
                "table_title": str(source_context.get("section_title") or "flattened_financial_table"),
                "row_label": row_label,
                "column_label": preferred["column_label"],
                "source_page": str(source_context.get("source_page") or "unavailable"),
                "cell_value": preferred["cell_value"],
                "table_mapping_confidence": max(88, mapping_score),
                "table_mapping_reason": preferred["table_mapping_reason"],
                "raw_row_text": row_text,
                "current_period_value": current_period_value,
                "prior_period_value": prior_period_value,
                "variance_value": variance_value,
                "variance_percent": variance_percent,
                "value_type": preferred["value_type"],
                "table_values": value_fields,
            }
    return last_rejection


def _target_context_matches(text: str, section_title: str, profile: dict[str, Any]) -> list[str]:
    haystack = _clean_text(f"{section_title} {text}".replace("_", " "))
    return _term_hits(haystack, _target_sections_for_profile(profile))


def _target_context_rejections(text: str, section_title: str, profile: dict[str, Any]) -> list[str]:
    haystack = _clean_text(f"{section_title} {text}".replace("_", " "))
    rejected = []
    for key in ("reject_sections", "reject_contexts", "rejected_nearby_terms", "hard_rejected_nearby_terms"):
        rejected.extend(_term_hits(haystack, _profile_string_list(profile, key)))
    return _merge_unique_list([], rejected)


def _extract_ticker_targeted_metric_value(
    *,
    document_structure: dict[str, Any],
    metric_name: str,
    ticker_plugin: dict[str, Any] | None,
    source: dict[str, Any],
    profile: dict[str, Any],
) -> dict[str, Any]:
    if not _targeted_search_enabled(ticker_plugin, profile):
        return {}
    diagnostics = _new_metric_diagnostics(
        ticker_plugin=ticker_plugin,
        profile=profile,
        targeted_search_attempted=True,
    )
    candidates: list[dict[str, Any]] = []
    target_rows = _target_rows_for_profile(profile)
    for page in document_structure.get("pages", []):
        page_number = str(page.get("page_number") or "unavailable")
        blocks: list[tuple[str, str]] = []
        for table in page.get("tables", []):
            table_text = _table_text_from_structured_table(table)
            blocks.append((str(table.get("section_title") or table.get("table_title") or "financial_statement_tables"), table_text))
        for block in page.get("text_blocks", []):
            blocks.append((str(block.get("section_title") or "unclassified_text"), str(block.get("text") or "")))
        for section_title, block_text in blocks:
            if not block_text:
                continue
            context_hits = _target_context_matches(block_text, section_title, profile)
            row_hits = _term_hits(block_text, target_rows)
            for context_hit in context_hits:
                _record_diagnostic_seen(diagnostics, "candidate_sections_seen", context_hit)
            for row_hit in row_hits:
                _record_diagnostic_seen(diagnostics, "candidate_rows_seen", row_hit)
            if not context_hits and not row_hits:
                continue
            rejections = _target_context_rejections(block_text, section_title, profile)
            if rejections:
                _set_diagnostic_rejection(
                    diagnostics,
                    candidate=block_text,
                    source_page=page_number,
                    reason=f"rejected targeted context: {', '.join(rejections)}",
                    failure_type="rejected_context",
                )
                continue
            if _target_sections_for_profile(profile) and not context_hits:
                _set_diagnostic_rejection(
                    diagnostics,
                    candidate=block_text,
                    source_page=page_number,
                    reason="target row appeared outside configured target sections",
                    failure_type="section_not_found",
                )
                continue
            if not row_hits:
                continue
            association = {}
            if TABLE_ROW_MARKER in block_text:
                association = _extract_table_metric_value(block_text, metric_name, profile)
            if not association:
                association = _extract_metric_from_flattened_financial_table(
                    block_text,
                    metric_name,
                    profile,
                    {"source_page": page_number, "section_title": section_title},
                )
            if not association:
                continue
            if association.get("metric_value_status") != "value_extracted":
                _set_diagnostic_rejection(
                    diagnostics,
                    candidate=str(association.get("raw_row_text") or block_text),
                    source_page=page_number,
                    reason=str(association.get("rejection_reason") or "target row could not be mapped"),
                    failure_type=str(association.get("failure_type") or "row_column_mapping_missing"),
                )
                continue
            candidate = _metric_candidate_from_association(
                association=association,
                source=source,
                page_number=page_number,
                section_title=section_title,
                candidate_text=block_text,
                candidate_origin="targeted_plugin",
                profile=profile,
            )
            if candidate:
                candidate["metric_diagnostics"] = {**diagnostics, "failure_type": "unavailable"}
                candidates.append(candidate)
    if candidates:
        return max(candidates, key=_metric_candidate_sort_key)
    if diagnostics["candidate_rows_seen"]:
        diagnostics["failure_type"] = diagnostics["failure_type"] if diagnostics["failure_type"] != "metric_not_present" else "row_column_mapping_missing"
    elif diagnostics["candidate_sections_seen"]:
        diagnostics["failure_type"] = "target_row_not_found"
    else:
        diagnostics["failure_type"] = "section_not_found"
    return {
        "metric_value_status": "unavailable",
        "clean_metric_value": "unavailable",
        "metric_diagnostics": diagnostics,
        "association_reason": "targeted ticker plugin search did not find a row/column-mapped metric value",
    }


def _direction_from_profile(text: str, profile: dict[str, Any]) -> str:
    lower = text.lower()
    rules = profile.get("direction_rules") or {}
    supportive = [str(item).lower() for item in rules.get("supportive", []) or []]
    adverse = [str(item).lower() for item in rules.get("adverse", []) or []]
    supportive_hit = any(term in lower for term in supportive)
    adverse_hit = any(term in lower for term in adverse)
    if supportive_hit and adverse_hit:
        return "mixed"
    if supportive_hit:
        return "supportive"
    if adverse_hit:
        return "adverse"
    return "neutral"


def _period_references(text: str) -> tuple[str, str]:
    periods = []
    for match in re.finditer(r"\b(?:FY)?20\d{2}\b|\bFY\d{2}\b", text, re.IGNORECASE):
        value = match.group(0).upper()
        if value.startswith("FY") and len(value) == 4:
            value = "FY20" + value[-2:]
        elif value.startswith("20"):
            value = "FY" + value
        if value not in periods:
            periods.append(value)
    return (periods[0] if periods else "not specified", periods[1] if len(periods) > 1 else "not specified")


def _fiscal_period_from_column_label(label: str) -> str:
    match = re.search(r"\b(?:FY)?20\d{2}\b|\bFY\d{2}\b", str(label), re.IGNORECASE)
    if not match:
        return "not specified"
    value = match.group(0).upper()
    if value.startswith("FY") and len(value) == 4:
        return "FY20" + value[-2:]
    if value.startswith("20"):
        return "FY" + value
    return value


def _competing_labels_near_value(text: str, metric_name: str, value_start: int) -> list[str]:
    competitors: list[tuple[int, str]] = []
    for sector_profiles in _load_metric_profiles().values():
        for other_metric, profile in sector_profiles.items():
            if other_metric == metric_name:
                continue
            for label_match in _label_matches(text, profile):
                distance = abs(value_start - label_match.end())
                if distance <= 80:
                    competitors.append((distance, other_metric))
    return [metric for _distance, metric in sorted(competitors)[:3]]


def _best_label_value_association(text: str, metric_name: str, profile: dict[str, Any]) -> dict[str, Any]:
    label_matches = _label_matches(text, profile)
    if not label_matches:
        return {}
    value_matches = _value_matches(text, profile)
    if not value_matches:
        return {}
    max_distance = int(profile.get("max_label_value_distance_tokens") or 10)
    best: dict[str, Any] = {}
    for label_match in label_matches:
        for value_match in value_matches:
            before = text[min(label_match.end(), value_match.end()) : max(label_match.start(), value_match.start())]
            token_distance = _token_count_between(before, "")
            if token_distance > max_distance:
                continue
            raw_value = value_match.group(0)
            clean_value, unit = _clean_value_and_unit(raw_value)
            if _value_validation_failure(clean_value, unit, profile):
                continue
            window_start = max(0, min(label_match.start(), value_match.start()) - 80)
            window_end = min(len(text), max(label_match.end(), value_match.end()) + 80)
            window = text[window_start:window_end]
            lower_window = window.lower()
            if _hard_rejected_for_candidate(text, lower_window, profile):
                continue
            if metric_name == "debt" and not _debt_balance_sheet_context_present(window):
                continue
            if not _required_terms_present(window, profile):
                continue
            between_start = min(label_match.end(), value_match.end())
            between_end = max(label_match.start(), value_match.start())
            lower_between = text[between_start:between_end].lower()
            score = 35
            score += max(0, 20 - token_distance * 2)
            score += 20 if _unit_compatible(unit, profile) else -25
            score += 15
            score += 10
            direction = _direction_from_profile(window, profile)
            if metric_name == "claims_ratio" and unit == "%":
                try:
                    if float(clean_value) > 0:
                        direction = "adverse"
                except ValueError:
                    pass
            if direction != "neutral":
                score += 5
            if metric_name in {"ebit_margin", "margins"} and unit == "bps":
                score += 10
            competing = _competing_labels_near_value(text, metric_name, value_match.start())
            if competing:
                stronger = False
                own_distance = min(
                    abs(value_match.start() - label_match.start()),
                    abs(value_match.start() - label_match.end()),
                )
                own_label_is_close_after_value = label_match.start() >= value_match.end() and token_distance <= 3
                for other_metric in competing:
                    if other_metric == "guidance" and metric_name != "guidance":
                        continue
                    if metric_name == "operating_profit_or_margin" and other_metric == "margins":
                        continue
                    if metric_name == "production" and other_metric == "commodity_exposure":
                        continue
                    other_profile = _profile_for_metric(other_metric)
                    own_label_is_close_before_value = label_match.end() <= value_match.start() and token_distance <= 2
                    for other_label in _label_matches(text, other_profile):
                        if own_label_is_close_after_value and other_label.end() <= value_match.start():
                            continue
                        if own_label_is_close_before_value and other_label.start() >= value_match.end():
                            continue
                        other_distance = min(
                            abs(value_match.start() - other_label.start()),
                            abs(value_match.start() - other_label.end()),
                        )
                        if other_distance < own_distance:
                            stronger = True
                if stronger:
                    score -= 35
            if token_distance <= 2:
                rejected_hits = _rejected_terms_present(lower_between, profile)
            else:
                rejected_hits = _rejected_terms_present(lower_window, profile)
            if rejected_hits:
                score -= 30
            if _is_navigation_or_toc(window):
                score -= 50
            if "footnote" in lower_window or re.search(r"\bnote\b", lower_window):
                score -= 30
            if unit in {"cents", "cps"} and re.search(r"\b1\s*cents?\s+per share\s+\$?m\b", lower_window, re.IGNORECASE):
                score -= 60
            reason_parts = [
                f"label-value distance {token_distance} tokens",
                f"unit {unit} {'compatible' if _unit_compatible(unit, profile) else 'incompatible'}",
            ]
            if competing:
                reason_parts.append(f"competing labels nearby: {', '.join(competing)}")
            if rejected_hits:
                reason_parts.append(f"rejected nearby terms: {', '.join(rejected_hits)}")
            if unit in {"cents", "cps"} and re.search(r"\b1\s*cents?\s+per share\s+\$?m\b", lower_window, re.IGNORECASE):
                reason_parts.append("dividend table header or footnote marker")
            candidate = {
                "score": max(0, min(100, score)),
                "clean_metric_value": clean_value,
                "value_unit": unit,
                "value_context": f"{text[label_match.start():label_match.end()]} near {raw_value}",
                "supporting_sentence": text.strip(),
                "association_reason": "; ".join(reason_parts),
                "direction": direction,
                "period_reference": _period_references(text)[0],
                "comparison_reference": _period_references(text)[1],
                "label_start": label_match.start(),
                "value_start": value_match.start(),
                "label_value_distance_tokens": token_distance,
            }
            if not best:
                best = candidate
                continue
            candidate_high = candidate["score"] >= 80
            best_high = best["score"] >= 80
            if candidate_high and best_high:
                if metric_name in {"ebit_margin", "margins"}:
                    candidate_unit = str(candidate.get("value_unit") or "").lower()
                    best_unit = str(best.get("value_unit") or "").lower()
                    if candidate_unit == "bps" and best_unit != "bps":
                        best = candidate
                    continue
                candidate_distance = int(candidate.get("label_value_distance_tokens", 999))
                best_distance = int(best.get("label_value_distance_tokens", 999))
                if candidate_distance < best_distance:
                    best = candidate
                    continue
                if candidate_distance > best_distance:
                    continue
                if (candidate["label_start"], candidate["value_start"]) < (best["label_start"], best["value_start"]):
                    best = candidate
            elif candidate["score"] > best["score"]:
                best = candidate
    return best


def _normalize_debt_label(label: str) -> str:
    normalized = _clean_text(label).lower()
    normalized = re.sub(r"[\u2010-\u2015]", "-", normalized)
    normalized = normalized.replace("interest bearing", "interest-bearing")
    normalized = normalized.replace("non current", "non-current")
    normalized = normalized.replace("noncurrent", "non-current")
    return normalized


def _csl_debt_row_kind(row_label: str) -> str:
    label = _normalize_debt_label(row_label)
    if "cash and cash equivalents" in label:
        return "cash_only"
    if any(term in label for term in CSL_DEBT_NON_CURRENT_TOTAL_LABELS):
        return "non_current_total"
    if any(term in label for term in CSL_DEBT_CURRENT_TOTAL_LABELS):
        return "current_total"
    if "lease liabilities" in label:
        return "lease_liabilities"
    if any(term in label for term in CSL_DEBT_DIRECT_TOTAL_LABELS):
        return "direct_total"
    if "senior notes" in label or "bank and other borrowings" in label:
        return "debt_component"
    return ""


def _numeric_string_to_float(value: str) -> float | None:
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return None


def _format_numeric_total(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _csl_debt_values_from_cells(
    *,
    cells: list[str],
    header_cells: list[str],
    metadata: dict[str, str],
    profile: dict[str, Any],
    full_context: str,
) -> list[dict[str, str]]:
    values: list[dict[str, str]] = []
    row_label = cells[0] if cells else ""
    unit_context = " ".join([metadata.get("table_title", ""), *header_cells, *cells, full_context])
    fallback_unit = _unit_from_column_label(unit_context)
    for index, cell in enumerate(cells[1:], start=1):
        column_label = header_cells[index] if index < len(header_cells) and header_cells[index] else f"value_{index}"
        if re.fullmatch(r"\s*notes?\s*", column_label, re.IGNORECASE):
            continue
        inferred_unit = _unit_from_column_label(column_label)
        if inferred_unit == "unit unavailable":
            inferred_unit = fallback_unit
        if inferred_unit == "unit unavailable":
            inferred_unit = _unit_from_column_label(row_label)
        parsed = _numeric_cell_value(cell, inferred_unit)
        if not parsed:
            continue
        clean_value, unit = parsed
        if unit == "unit unavailable" and fallback_unit != "unit unavailable":
            unit = fallback_unit
        if not _unit_compatible(unit, profile):
            continue
        if _value_validation_failure(clean_value, unit, profile):
            continue
        value_type = _value_type_from_column_label(column_label, index)
        if value_type not in {"current_period_value", "prior_period_value"} and index == 1:
            value_type = "current_period_value"
        values.append(
            {
                "clean_value": clean_value,
                "unit": unit,
                "column_label": column_label,
                "value_type": value_type,
                "cell_value": cell,
            }
        )
    return values


def _csl_debt_first_value(
    rows: list[dict[str, str]],
    value_type: str = "current_period_value",
) -> dict[str, str] | None:
    return next((row for row in rows if row["value_type"] == value_type), rows[0] if rows else None)


def _csl_debt_total_association(
    *,
    current_row: dict[str, Any],
    non_current_row: dict[str, Any],
    table_title: str,
    source_page: str,
    profile: dict[str, Any],
) -> dict[str, Any]:
    current_value = _csl_debt_first_value(current_row["values"])
    non_current_value = _csl_debt_first_value(non_current_row["values"])
    if not current_value or not non_current_value:
        return {}
    current_number = _numeric_string_to_float(current_value["clean_value"])
    non_current_number = _numeric_string_to_float(non_current_value["clean_value"])
    if current_number is None or non_current_number is None:
        return {}
    unit = current_value["unit"] if current_value["unit"] == non_current_value["unit"] else current_value["unit"]
    total = current_number + non_current_number
    prior_total = "unavailable"
    current_prior = _csl_debt_first_value(current_row["values"], "prior_period_value")
    non_current_prior = _csl_debt_first_value(non_current_row["values"], "prior_period_value")
    if current_prior and non_current_prior:
        current_prior_number = _numeric_string_to_float(current_prior["clean_value"])
        non_current_prior_number = _numeric_string_to_float(non_current_prior["clean_value"])
        if current_prior_number is not None and non_current_prior_number is not None:
            prior_total = _format_numeric_total(current_prior_number + non_current_prior_number)
    row_label = "total interest-bearing liabilities and borrowings"
    mapping_score, mapping_reason = _table_mapping_score(
        row_label=row_label,
        column_label=current_value["column_label"],
        value_type="current_period_value",
        unit=unit,
        profile=profile,
        has_header=True,
        metadata={"source_page": source_page, "table_title": table_title},
    )
    score = max(92, mapping_score)
    current_total = _format_numeric_total(total)
    period_reference = _fiscal_period_from_column_label(current_value["column_label"])
    if period_reference == "not specified":
        period_reference = current_value["column_label"]
    comparison_reference = (
        _fiscal_period_from_column_label(current_prior["column_label"]) if current_prior else "not specified"
    )
    if current_prior and comparison_reference == "not specified":
        comparison_reference = current_prior["column_label"]
    normalized_column_label = (
        f"{period_reference} {unit}" if period_reference.startswith("FY") else current_value["column_label"]
    )
    return {
        "score": score,
        "clean_metric_value": current_total,
        "metric_value_status": "value_extracted",
        "association_score": score,
        "value_unit": unit,
        "value_context": "current and non-current interest-bearing liabilities and borrowings total",
        "supporting_sentence": f"{current_row['raw_row_text']} {non_current_row['raw_row_text']}",
        "association_reason": "CSL debt extracted by summing current and non-current interest-bearing liabilities and borrowings rows",
        "confidence": "medium",
        "confidence_reason": "clean value accepted because current and non-current borrowings rows prove total balance-sheet debt",
        "direction": "neutral",
        "period_reference": period_reference,
        "comparison_reference": comparison_reference,
        "table_title": table_title,
        "source_section": table_title,
        "row_label": row_label,
        "column_label": normalized_column_label,
        "cell_value": current_total,
        "source_page": source_page,
        "current_period_value": current_total,
        "prior_period_value": prior_total,
        "variance_value": "unavailable",
        "variance_percent": "unavailable",
        "raw_row_text": f"{current_row['raw_row_text']} | {non_current_row['raw_row_text']}",
        "table_values": {
            "current_interest_bearing_liabilities_and_borrowings": current_value["clean_value"],
            "non_current_interest_bearing_liabilities_and_borrowings": non_current_value["clean_value"],
            "current_period_value": current_total,
            "prior_period_value": prior_total,
        },
        "table_mapping_confidence": score,
        "table_mapping_reason": f"current and non-current borrowings rows mapped; {mapping_reason}",
        "value_type": "current_period_value",
    }


def _csl_direct_debt_association(
    *,
    row: dict[str, Any],
    table_title: str,
    source_page: str,
    profile: dict[str, Any],
    lease_warning: bool = False,
) -> dict[str, Any]:
    value = _csl_debt_first_value(row["values"])
    if not value:
        return {}
    row_label = row["row_label"]
    mapping_score, mapping_reason = _table_mapping_score(
        row_label=row_label,
        column_label=value["column_label"],
        value_type=value["value_type"],
        unit=value["unit"],
        profile=profile,
        has_header=True,
        metadata={"source_page": source_page, "table_title": table_title},
    )
    score = max(88, mapping_score)
    confidence_reason = "clean value accepted because CSL debt row has row/column proof"
    if lease_warning:
        confidence_reason += "; lease liabilities are balance-sheet debt evidence, not total debt"
    return {
        "score": score,
        "clean_metric_value": value["clean_value"],
        "metric_value_status": "value_extracted",
        "association_score": score,
        "value_unit": value["unit"],
        "value_context": "CSL balance-sheet debt row",
        "supporting_sentence": row["raw_row_text"],
        "association_reason": "CSL debt extracted from a borrowings, debt, or balance-sheet liabilities row",
        "confidence": "medium",
        "confidence_reason": confidence_reason,
        "direction": "neutral",
        "period_reference": value["column_label"],
        "comparison_reference": "not specified",
        "table_title": table_title,
        "source_section": table_title,
        "row_label": row_label,
        "column_label": value["column_label"],
        "cell_value": value["cell_value"],
        "source_page": source_page,
        "current_period_value": value["clean_value"],
        "prior_period_value": "unavailable",
        "variance_value": "unavailable",
        "variance_percent": "unavailable",
        "raw_row_text": row["raw_row_text"],
        "table_values": {value["value_type"]: value["clean_value"]},
        "table_mapping_confidence": score,
        "table_mapping_reason": mapping_reason,
        "value_type": value["value_type"],
        "metric_subtype": "lease_liabilities_balance_sheet_debt" if lease_warning else "",
    }


def _extract_csl_debt_or_balance_sheet_table(text: str, profile: dict[str, Any]) -> dict[str, Any]:
    if "|" not in text:
        return {}
    headers_by_table: dict[tuple[str, str], list[str]] = {}
    current_rows: dict[tuple[str, str], dict[str, Any]] = {}
    non_current_rows: dict[tuple[str, str], dict[str, Any]] = {}
    direct_candidates: list[dict[str, Any]] = []
    lease_candidates: list[dict[str, Any]] = []
    cash_only_seen = False
    split_pattern = r"\n|(?<=\d[%a-zA-Z])\s+(?=(?:__TABLE_ROW__\s+)?[A-Z][A-Za-z /&-]{2,}\s*\|)"
    for raw_row in re.split(split_pattern, text):
        row = raw_row.strip()
        if "|" not in row:
            continue
        metadata, cells = _parse_structured_table_line(row)
        if len(cells) < 2:
            continue
        key = _table_key(metadata)
        table_title = metadata.get("table_title", "unavailable").replace("_", " ")
        row_label = cells[0]
        row_kind = _csl_debt_row_kind(row_label)
        if not row_kind:
            if key in headers_by_table and _header_continuation_row(cells):
                headers_by_table[key] = _merge_table_header_rows(headers_by_table[key], cells)
            else:
                headers_by_table[key] = cells
            continue
        if row_kind == "cash_only":
            cash_only_seen = True
            continue
        values = _csl_debt_values_from_cells(
            cells=cells,
            header_cells=headers_by_table.get(key, []),
            metadata=metadata,
            profile=profile,
            full_context=text,
        )
        if not values:
            continue
        row_record = {
            "row_label": row_label,
            "values": values,
            "raw_row_text": " | ".join(cells),
            "table_title": table_title,
            "source_page": metadata.get("source_page", "unavailable"),
        }
        if row_kind == "current_total":
            current_rows[key] = row_record
        elif row_kind == "non_current_total":
            non_current_rows[key] = row_record
        elif row_kind == "direct_total":
            direct_candidates.append(row_record)
        elif row_kind == "lease_liabilities":
            lease_candidates.append(row_record)
    for key, current_row in current_rows.items():
        non_current_row = non_current_rows.get(key)
        if not non_current_row:
            continue
        table_title = current_row.get("table_title") or non_current_row.get("table_title") or "CSL debt table"
        source_page = current_row.get("source_page") or non_current_row.get("source_page") or "unavailable"
        association = _csl_debt_total_association(
            current_row=current_row,
            non_current_row=non_current_row,
            table_title=table_title,
            source_page=source_page,
            profile=profile,
        )
        if association:
            return association
    for row in direct_candidates:
        association = _csl_direct_debt_association(
            row=row,
            table_title=str(row.get("table_title") or "CSL debt table"),
            source_page=str(row.get("source_page") or "unavailable"),
            profile=profile,
        )
        if association:
            return association
    for row in lease_candidates:
        association = _csl_direct_debt_association(
            row=row,
            table_title=str(row.get("table_title") or "CSL debt table"),
            source_page=str(row.get("source_page") or "unavailable"),
            profile=profile,
            lease_warning=True,
        )
        if association:
            return association
    if cash_only_seen:
        return {
            "metric_value_status": "unavailable",
            "failure_type": "value_rejected_by_profile",
            "rejection_reason": "cash and cash equivalents alone is not debt or borrowings evidence",
            "raw_row_text": "cash and cash equivalents",
        }
    return {}


def _extract_table_metric_value(text: str, metric_name: str, profile: dict[str, Any]) -> dict[str, Any]:
    if "|" not in text:
        return {}
    if metric_name == "debt":
        csl_debt = _extract_csl_debt_or_balance_sheet_table(text, profile)
        if csl_debt:
            return csl_debt
    headers_by_table: dict[tuple[str, str], list[str]] = {}
    best: dict[str, Any] = {}
    for raw_row in re.split(r"\n|(?<=\d[%a-zA-Z])\s+(?=(?:__TABLE_ROW__\s+)?[A-Z][A-Za-z /&-]{2,}\s*\|)", text):
        row = raw_row.strip()
        if "|" not in row:
            continue
        metadata, cells = _parse_structured_table_line(row)
        if len(cells) < 3:
            continue
        key = _table_key(metadata)
        row_content = " | ".join(cells)
        if _rejected_terms_present(row_content, profile) or _hard_rejected_terms_present(row_content, profile):
            continue
        table_context = " ".join(
            [
                metadata.get("table_title", ""),
                row_content,
                " ".join(headers_by_table.get(key, [])),
            ]
        )
        row_matches_profile = _row_label_matches(cells[0], profile)
        row_matches_context = _contextual_row_allowed(metric_name, cells[0], table_context, profile)
        if row_matches_profile and metric_name == "realised_price" and not headers_by_table.get(key) and _realised_price_context_present(row_content):
            headers_by_table[key] = cells
            continue
        if not row_matches_profile and not row_matches_context:
            if key in headers_by_table and _header_continuation_row(cells):
                headers_by_table[key] = _merge_table_header_rows(headers_by_table[key], cells)
            else:
                headers_by_table[key] = cells
            continue
        row_label = cells[0]
        header_cells = headers_by_table.get(key, [])
        if metric_name in STRUCTURED_TABLE_REQUIRED_METRICS and not header_cells:
            continue
        row_context = " ".join([row_label, metadata.get("table_title", ""), *header_cells, *cells[1:]])
        if metric_name == "debt" and not _debt_balance_sheet_context_present(row_context):
            continue
        if not _required_terms_present(row_context, profile):
            continue
        values: list[dict[str, str]] = []
        row_unit_hint = next(
            (
                unit
                for unit in (_unit_from_column_label(cell) for cell in cells[1:])
                if unit != "unit unavailable"
            ),
            "unit unavailable",
        )
        for index, cell in enumerate(cells[1:], start=1):
            column_label = header_cells[index] if header_cells and index < len(header_cells) else cells[index - 1]
            inferred_unit = _unit_from_column_label(column_label)
            if inferred_unit == "unit unavailable":
                inferred_unit = _unit_from_column_label(" ".join([metadata.get("table_title", ""), *header_cells]))
            if inferred_unit == "unit unavailable":
                inferred_unit = row_unit_hint
            if inferred_unit == "unit unavailable":
                inferred_unit = _unit_from_column_label(row_label)
            parsed = _numeric_cell_value(cell, inferred_unit)
            if not parsed:
                continue
            clean_value, unit = parsed
            if unit != "unit unavailable" and not _unit_compatible(unit, profile):
                continue
            if metric_name == "commodity_exposure" and not _commodity_exposure_numeric_table_allowed(
                row_label=row_label,
                column_label=column_label,
                unit=unit,
                metadata=metadata,
                row_context=row_context,
            ):
                continue
            if _value_validation_failure(clean_value, unit, profile):
                continue
            value_type = _value_type_from_column_label(column_label, index)
            if not _column_label_allowed(column_label, profile):
                continue
            mapping_score, mapping_reason = _table_mapping_score(
                row_label=row_label,
                column_label=column_label,
                value_type=value_type,
                unit=unit,
                profile=profile,
                has_header=bool(header_cells),
                metadata=metadata,
            )
            values.append(
                {
                    "index": str(index),
                    "clean_value": clean_value,
                    "unit": unit,
                    "column_label": column_label,
                    "value_type": value_type,
                    "cell_value": cell,
                    "table_mapping_confidence": str(mapping_score),
                    "table_mapping_reason": mapping_reason,
                }
            )
        if not values:
            continue
        preferred_types = _preferred_value_types(profile)
        preferred = next((item for value_type in preferred_types for item in values if item["value_type"] == value_type), values[0])
        clean_value = preferred["clean_value"]
        unit = preferred["unit"]
        column_label = preferred["column_label"]
        value_type = preferred["value_type"]
        mapping_score = int(preferred["table_mapping_confidence"])
        value_fields = {item["value_type"]: item["clean_value"] for item in values}
        value_column_labels = {item["value_type"]: item["column_label"] for item in values}
        current_period_value = value_fields.get("current_period_value", "unavailable")
        prior_period_value = value_fields.get("prior_period_value", "unavailable")
        variance_value = value_fields.get("variance_value", "unavailable")
        variance_percent = value_fields.get("variance_percent", "unavailable")
        comparison_reference = value_column_labels.get("prior_period_value", "not specified") if prior_period_value != "unavailable" else "not specified"
        direction = _direction_from_profile(row, profile)
        if metric_name == "claims_ratio" and unit in {"%", "per cent"}:
            try:
                if float(clean_value) > 0:
                    direction = "adverse"
            except ValueError:
                pass
        score = max(0, min(100, mapping_score))
        candidate = {
            "score": score,
            "clean_metric_value": clean_value if score >= 80 else "unavailable",
            "metric_value_status": "value_extracted" if score >= 80 else "table_row_unparsed",
            "association_score": score,
            "value_unit": unit,
            "value_context": "table row/column label association",
            "supporting_sentence": row,
            "association_reason": "table row label matches accepted metric label and value is taken from parsed row/column structure",
            "confidence": "medium" if score >= 80 else "low",
            "confidence_reason": (
                "clean value accepted because row label, column label, and source table structure were mapped"
                if score >= 80
                else "clean value withheld because row/column mapping was below the clean extraction threshold"
            ),
            "direction": direction,
            "period_reference": column_label,
            "comparison_reference": comparison_reference,
            "table_title": metadata.get("table_title", "unavailable"),
            "row_label": row_label,
            "column_label": column_label,
            "cell_value": preferred["cell_value"],
            "source_page": metadata.get("source_page", "unavailable"),
            "current_period_value": current_period_value,
            "prior_period_value": prior_period_value,
            "variance_value": variance_value,
            "variance_percent": variance_percent,
            "raw_row_text": " | ".join(cells),
            "table_values": value_fields,
            "table_mapping_confidence": score,
            "table_mapping_reason": preferred["table_mapping_reason"],
            "value_type": value_type,
        }
        segment_name = _segment_name_in_text(" ".join([row_label, metadata.get("table_title", ""), row]))
        if metric_name == "segment_revenue" and segment_name:
            candidate["segment_name"] = segment_name
        if not best or score > int(best.get("table_mapping_confidence", 0)):
            best = candidate
    return best


def _extract_dense_metric_row_value(text: str, metric_name: str, profile: dict[str, Any]) -> dict[str, Any]:
    if metric_name in STRUCTURED_TABLE_REQUIRED_METRICS:
        return {}
    label_matches = _label_matches(text, profile)
    if not label_matches:
        return {}
    row_start = label_matches[0].start()
    next_label_start = len(text)
    lower_tail = text[label_matches[0].end() :].lower()
    for label in DENSE_TABLE_ROW_LABELS:
        match = re.search(rf"\b{re.escape(label)}\b", lower_tail)
        if match:
            absolute_start = label_matches[0].end() + match.start()
            if absolute_start > label_matches[0].end() and absolute_start < next_label_start:
                next_label_start = absolute_start
    row = text[row_start:next_label_start].strip()
    if _rejected_terms_present(row, profile) or _hard_rejected_terms_present(row, profile) or not _required_terms_present(row, profile):
        return {}
    if metric_name == "debt" and not _debt_balance_sheet_context_present(row):
        return {}
    first_sentence = re.split(r"(?<=[.!?])\s+", row, maxsplit=1)[0]
    immediate_window = row[:140]
    if not _numeric_value_spans(first_sentence) and len(_numeric_value_spans(immediate_window)) < 2:
        return {}
    value_matches = _numeric_value_spans(row)
    if len(value_matches) < 3:
        return {}
    parsed_values: list[tuple[str, str, str]] = []
    for match in value_matches:
        clean_value, unit = _clean_value_and_unit(match.group(0))
        parsed_values.append((clean_value, unit, match.group(0).strip()))
    preferred = parsed_values[0]
    column_label = "current_period_value"
    if metric_name == "claims_ratio":
        percent_values = [item for item in parsed_values if item[1] in {"%", "per cent"} or "%" in item[2]]
        if not percent_values:
            return {}
        preferred = percent_values[-1]
        column_label = "variance_percent"
    clean_value, unit, raw_value = preferred
    if unit != "unit unavailable" and not _unit_compatible(unit, profile):
        return {}
    if _value_validation_failure(clean_value, unit, profile):
        return {}
    direction = _direction_from_profile(row, profile)
    if metric_name == "claims_ratio" and unit in {"%", "per cent"}:
        try:
            if float(clean_value) > 0:
                direction = "adverse"
        except ValueError:
            pass
    return {
        "score": 88,
        "clean_metric_value": clean_value,
        "value_unit": unit,
        "value_context": "dense row parsed before next financial row label",
        "supporting_sentence": row,
        "association_reason": "dense row label matched accepted metric label and value was selected from the parsed metric row before the next row label",
        "direction": direction,
        "period_reference": column_label,
        "comparison_reference": "prior_period_value" if len(parsed_values) >= 2 else "not specified",
        "table_title": "unavailable",
        "row_label": row[:80],
        "column_label": column_label,
        "cell_value": raw_value,
        "source_page": "unavailable",
        "table_mapping_confidence": 88,
        "table_mapping_reason": "dense metric row isolated before next financial row label",
        "raw_row_text": row,
        "current_period_value": parsed_values[0][0] if len(parsed_values) >= 1 else "unavailable",
        "prior_period_value": parsed_values[1][0] if len(parsed_values) >= 2 else "unavailable",
        "variance_value": parsed_values[2][0] if len(parsed_values) >= 3 and "%" not in parsed_values[2][2] else "unavailable",
        "variance_percent": clean_value if column_label == "variance_percent" else "unavailable",
        "raw_value": raw_value,
    }


def _metric_label_present(text: str, profile: dict[str, Any]) -> bool:
    return bool(_label_matches(text, profile))


def _best_metric_context(clean: str, profile: dict[str, Any], fallback_length: int = 900) -> str:
    label_matches = _label_matches(clean, profile)
    if not label_matches:
        return clean[:fallback_length]
    label_match = label_matches[0]
    sentence_match = None
    for sentence in _sentences(clean):
        if _label_matches(sentence, profile):
            sentence_match = sentence
            break
    if sentence_match:
        return sentence_match
    window_start = max(0, label_match.start() - 220)
    window_end = min(len(clean), label_match.end() + fallback_length)
    return clean[window_start:window_end].strip()


def _accepted_status(profile: dict[str, Any], status: str) -> bool:
    return status in {str(item).strip() for item in profile.get("accepted_statuses", []) or []}


def _commodity_names_in_text(text: str) -> list[str]:
    lower = text.lower()
    names = []
    for commodity in (*BHP_COMMODITY_ROW_LABELS,):
        if commodity in lower and commodity not in names:
            names.append(commodity)
    return names


def _commodity_support_sentence(clean: str, profile: dict[str, Any]) -> str:
    context_terms = (
        "portfolio",
        "commodity mix",
        "commodity exposure",
        "commodity portfolio",
        "portfolio mix",
        "our businesses",
        "business overview",
        "asset portfolio",
        "operating assets",
        "principal activities",
        "commodities",
    )
    for sentence in _sentences(clean):
        lower = sentence.lower()
        if len(_commodity_names_in_text(sentence)) >= 2 and any(term in lower for term in context_terms):
            return sentence[:600]
    for sentence in _sentences(clean):
        if len(_commodity_names_in_text(sentence)) >= 2:
            return sentence[:600]
    return _first_metric_support_sentence(clean, profile)


def _segment_name_in_text(text: str) -> str:
    lower = text.lower().replace("_", " ")
    for segment in CSL_SEGMENTS:
        if segment.lower() in lower:
            return segment
    return ""


def _guidance_direction(text: str) -> str:
    lower = text.lower()
    positive = any(term in lower for term in ("growth", "increase", "improve", "strong", "higher", "positive"))
    negative = any(term in lower for term in ("decline", "decrease", "lower", "weaker", "negative", "soft"))
    if positive and negative:
        return "mixed"
    if positive:
        return "positive"
    if negative:
        return "negative"
    return "neutral"


def _debt_balance_sheet_context_present(text: str) -> bool:
    lower = _clean_text(text).lower()
    strong_terms = (
        "net debt",
        "borrowings",
        "total debt",
        "interest-bearing liabilities",
        "interest bearing liabilities",
        "lease liabilities",
        "leverage",
        "gearing",
        "net cash",
    )
    if any(term in lower for term in strong_terms):
        return True
    if "cash and cash equivalents" in lower:
        return any(term in lower for term in ("debt", "borrowings", "interest-bearing", "lease liabilities", "gearing", "leverage"))
    return False


def _narrative_context_present(metric_name: str, text: str, profile: dict[str, Any]) -> bool:
    lower = text.lower()
    if metric_name == "commodity_exposure" and _accepted_status(profile, "portfolio_mix_narrative"):
        commodities = _commodity_names_in_text(text)
        has_context = any(
            term in lower
            for term in (
                "portfolio",
                "commodity mix",
                "commodity exposure",
                "commodity portfolio",
                "portfolio mix",
                "our businesses",
                "business overview",
                "asset portfolio",
                "operating assets",
                "principal activities",
                "commodities",
            )
        )
        return len(commodities) >= 2 and has_context
    if metric_name == "guidance" and _accepted_status(profile, "guidance_narrative"):
        return any(term in lower for term in ("guidance", "outlook", "financial outlook")) and any(
            term in lower for term in ("expects", "expected", "forecast", "anticipates", "outlook", "subject to")
        )
    if metric_name == "plasma_collections" and _accepted_status(profile, "plasma_network_narrative"):
        return "plasma" in lower and any(
            term in lower
            for term in (
                "collection network",
                "plasma network",
                "donor centres",
                "donor centers",
                "collection centres",
                "collection centers",
                "plasma centres",
                "plasma centers",
                "plasma supply",
            )
        )
    return False


def _narrative_metric_association(
    *,
    metric_name: str,
    clean: str,
    profile: dict[str, Any],
    base: dict[str, Any],
) -> dict[str, Any]:
    if metric_name == "commodity_exposure" and _accepted_status(profile, "portfolio_mix_narrative"):
        commodities = _commodity_names_in_text(clean)
        lower = clean.lower()
        has_portfolio_context = any(
            term in lower
            for term in ("portfolio", "commodity mix", "commodity exposure", "commodity portfolio", "portfolio mix")
        )
        if len(commodities) >= 2 and has_portfolio_context:
            support_sentence = _commodity_support_sentence(clean, profile)
            return {
                **base,
                "metric_value_status": "portfolio_mix_narrative",
                "association_score": 90,
                "association_reason": "eligible section describes commodity portfolio mix but does not provide a numeric exposure value",
                "value_unit": "narrative",
                "value_context": "portfolio mix narrative; no numeric clean metric value assigned",
                "supporting_sentence": support_sentence,
                "comparison_basis": "portfolio composition narrative",
                "direction": "neutral",
                "confidence": "medium",
                "confidence_reason": "commodity exposure accepted only as portfolio_mix_narrative with commodity names and source context",
                "commodity_names": commodities,
                "commodity_names_identified": commodities,
            }
    if metric_name == "guidance" and _accepted_status(profile, "guidance_narrative"):
        lower = clean.lower()
        has_guidance_context = any(term in lower for term in ("guidance", "outlook", "financial outlook"))
        has_directional_guidance = any(
            term in lower
            for term in ("expects", "expected", "forecast", "anticipates", "targets", "outlook for")
        )
        if has_guidance_context and has_directional_guidance:
            support_sentence = _first_metric_support_sentence(clean, profile)
            return {
                **base,
                "metric_value_status": "guidance_narrative",
                "association_score": 82,
                "association_reason": "eligible outlook/guidance section provides directional guidance without a clean numeric value",
                "value_unit": "narrative",
                "value_context": "guidance narrative; no numeric clean metric value assigned",
                "supporting_sentence": support_sentence,
                "comparison_basis": "management outlook/guidance narrative",
                "direction": _direction_from_profile(support_sentence, profile),
                "confidence": "medium",
                "confidence_reason": "guidance accepted as narrative because the plugin permits non-numeric outlook evidence",
                "guidance_direction": _guidance_direction(support_sentence),
            }
    if metric_name == "plasma_collections" and _accepted_status(profile, "plasma_network_narrative"):
        if _narrative_context_present(metric_name, clean, profile):
            support_sentence = _first_metric_support_sentence(clean, profile)
            centre_match = re.search(r"\b(\d{1,4}(?:,\d{3})?)\s+(?:donor\s+)?(?:plasma\s+)?(?:collection\s+)?cent(?:re|er)s\b", support_sentence, re.IGNORECASE)
            return {
                **base,
                "metric_value_status": "plasma_network_narrative",
                "association_score": 84,
                "association_reason": "eligible CSL Plasma section describes plasma collection network evidence without a clean collection-volume value",
                "value_unit": "narrative",
                "value_context": "plasma network narrative; no numeric clean metric value assigned",
                "supporting_sentence": support_sentence,
                "comparison_basis": "plasma collection network narrative",
                "direction": "supportive"
                if re.search(r"\b(?:expanded|expansion|growth|increased|opened|added)\b", support_sentence, re.IGNORECASE)
                else "neutral",
                "confidence": "medium",
                "confidence_reason": "plasma collection network evidence is accepted as narrative because the CSL plugin permits network evidence",
                "centre_count": centre_match.group(1).replace(",", "") if centre_match else "unavailable",
            }
    return {}


def _csl_segment_revenue_card_association(clean: str, profile: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    if not _unit_compatible("US$m", profile) and not _unit_compatible("$m", profile):
        return {}
    money_pattern = r"(?P<value>(?:US\$|A\$|\$)?\s*(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\s*(?:m|bn|million|billion))"
    for segment in CSL_SEGMENTS:
        segment_pattern = re.escape(segment).replace(r"\ ", r"\s+")
        patterns = [
            rf"{money_pattern}\s+{segment_pattern}\s+(?:revenue|sales)\b",
            rf"{segment_pattern}\s+(?:revenue|sales)\s+{money_pattern}",
        ]
        for pattern in patterns:
            match = re.search(pattern, clean, re.IGNORECASE)
            if not match:
                continue
            raw_value = match.group("value")
            clean_value, unit = _clean_value_and_unit(raw_value)
            if clean_value == "unavailable" or not _unit_compatible(unit, profile):
                continue
            support_sentence = next((sentence for sentence in _sentences(clean) if match.group(0) in sentence), clean[:240])
            return {
                **base,
                "clean_metric_value": clean_value,
                "value_unit": unit,
                "value_context": f"{segment} revenue metric card",
                "metric_value_status": "value_extracted",
                "association_score": 88,
                "association_reason": "CSL segment revenue card pairs a segment label with an adjacent revenue value",
                "period_reference": _period_references(clean)[0],
                "comparison_reference": _period_references(clean)[1],
                "supporting_sentence": support_sentence[:240],
                "comparison_basis": "segment revenue card",
                "direction": "neutral",
                "confidence": "medium",
                "confidence_reason": "segment revenue accepted from segment-specific CSL metric card text",
                "segment_name": segment,
                "row_label": f"{segment} revenue",
                "cell_value": raw_value.strip(),
            }
    return {}


def _csl_profitability_metric_association(clean: str, profile: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    if not _accepted_status(profile, "profitability_metric"):
        return {}
    label_pattern = (
        r"(?P<label>NPATA|EBITDA?|EBITA|operating profit|underlying profit|"
        r"net profit after tax before amortisation)"
    )
    value_pattern = r"(?P<value>(?:US\$|A\$|\$)?\s*(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\s*(?:m|bn|million|billion|%))"
    patterns = [
        rf"{label_pattern}.{{0,120}}?{value_pattern}",
        rf"{value_pattern}.{{0,80}}?{label_pattern}",
    ]
    for pattern in patterns:
        match = re.search(pattern, clean, re.IGNORECASE)
        if not match:
            continue
        raw_value = match.group("value")
        clean_value, unit = _clean_value_and_unit(raw_value)
        if clean_value == "unavailable":
            continue
        label = _clean_text(match.group("label"))
        support_sentence = next((sentence for sentence in _sentences(clean) if match.group(0) in sentence), clean[:240])
        return {
            **base,
            "clean_metric_value": clean_value,
            "value_unit": unit,
            "value_context": f"{label} profitability metric",
            "metric_value_status": "profitability_metric",
            "association_score": 86,
            "association_reason": "CSL profitability measure is accepted as NPATA/EBIT-style evidence when no formal margin percentage is available",
            "period_reference": _period_references(clean)[0],
            "comparison_reference": _period_references(clean)[1],
            "supporting_sentence": support_sentence[:240],
            "comparison_basis": "profitability metric",
            "direction": _direction_from_profile(support_sentence, profile),
            "confidence": "medium",
            "confidence_reason": "profitability metric accepted as CSL margin substitute under ticker plugin rules",
            "row_label": label,
            "cell_value": raw_value.strip(),
        }
    return {}


def _bhp_flattened_realised_price_association(clean: str, profile: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    lower = clean.lower()
    if any(term in lower for term in ("contingent payments", "threshold", "thresholds", "revenue share", "pricing assumption")):
        return {}
    if not _realised_price_context_present(clean):
        return {}
    commodity_pattern = "|".join(re.escape(commodity) for commodity in sorted(BHP_COMMODITY_ROW_LABELS, key=len, reverse=True))
    unit_pattern = (
        r"US\$/wmt|US\$/dmt|US\$/t|US\$/tonne|US\$/lb|US\$/oz|US\$/boe|US\$/kg|"
        r"\$/wmt|\$/dmt|\$/t|\$/tonne|\$/lb|\$/oz|\$/boe|\$/kg|"
        r"USc/lb|c/lb|US cents/lb|cents/lb"
    )
    number_pattern = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?"
    patterns = [
        rf"(?P<title>average realised prices?|realised prices?|price received|realised pricing).{{0,260}}?"
        rf"(?P<row>{commodity_pattern})\s*\((?P<unit>{unit_pattern})\)\s+"
        rf"(?P<current>{number_pattern})\s+(?P<prior>{number_pattern})",
        rf"(?P<title>average realised prices?|realised prices?|price received|realised pricing)\s*"
        rf"\((?P<unit>{unit_pattern})\).{{0,180}}?(?P<row>{commodity_pattern})\s+"
        rf"(?P<current>{number_pattern})\s+(?P<prior>{number_pattern})",
    ]
    for pattern in patterns:
        match = re.search(pattern, clean, re.IGNORECASE)
        if not match:
            continue
        unit = _unit_from_column_label(match.group("unit"))
        current_value = match.group("current").replace(",", "")
        prior_value = match.group("prior").replace(",", "")
        if not _unit_compatible(unit, profile):
            continue
        if _value_validation_failure(current_value, unit, profile):
            continue
        row_label = _clean_text(match.group("row"))
        period_reference, comparison_reference = _period_references(clean)
        if period_reference == "not specified":
            period_reference = "FY2025"
        if comparison_reference == "not specified":
            comparison_reference = "FY2024"
        support_sentence = clean[max(0, match.start() - 80) : min(len(clean), match.end() + 80)].strip()
        return {
            **base,
            "clean_metric_value": current_value,
            "value_unit": unit,
            "value_context": "flattened average realised prices table row",
            "metric_value_status": "value_extracted",
            "association_score": 88,
            "association_reason": "BHP flattened realised-price table row has realised-price heading, commodity row label, unit, and current/prior values",
            "period_reference": period_reference,
            "comparison_reference": comparison_reference,
            "supporting_sentence": support_sentence,
            "comparison_basis": "current/prior average realised price table values",
            "direction": "neutral",
            "confidence": "medium",
            "confidence_reason": "clean value accepted from a BHP average realised prices row with row/column proof",
            "table_title": _clean_text(match.group("title")),
            "row_label": row_label,
            "column_label": f"{period_reference} {unit}",
            "cell_value": match.group("current"),
            "table_mapping_confidence": 88,
            "table_mapping_reason": "realised-price heading plus commodity row, unit, and current/prior values",
            "raw_row_text": _clean_text(match.group(0)),
            "current_period_value": current_value,
            "prior_period_value": prior_value,
        }
    return {}


def _csl_flattened_debt_balance_sheet_association(clean: str, profile: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    lower = clean.lower()
    if "interest-bearing liabilities and borrowings" not in lower and "interest bearing liabilities and borrowings" not in lower:
        return {}
    if "current liabilities" not in lower or "non-current liabilities" not in lower:
        return {}
    current_section_match = re.search(
        r"(?<!non-)current liabilities(?P<section>.*?)(?:non-current liabilities|total current liabilities|$)",
        clean,
        re.IGNORECASE,
    )
    non_current_section_match = re.search(
        r"non-current liabilities(?P<section>.*?)(?:total non-current liabilities|total liabilities|net assets|$)",
        clean,
        re.IGNORECASE,
    )
    if not current_section_match or not non_current_section_match:
        return {}
    row_pattern = re.compile(
        r"interest[- ]bearing liabilities and borrowings\s+(?:\d{1,3}\s+)?"
        r"(?P<current>\(?-?\d{1,3}(?:,\d{3})*(?:\.\d+)?\)?)\s+"
        r"(?P<prior>\(?-?\d{1,3}(?:,\d{3})*(?:\.\d+)?\)?)",
        re.IGNORECASE,
    )
    current_match = row_pattern.search(current_section_match.group("section"))
    non_current_match = row_pattern.search(non_current_section_match.group("section"))
    if not current_match or not non_current_match:
        return {}
    current_value = current_match.group("current").replace(",", "").strip("()")
    non_current_value = non_current_match.group("current").replace(",", "").strip("()")
    current_number = _numeric_string_to_float(current_value)
    non_current_number = _numeric_string_to_float(non_current_value)
    if current_number is None or non_current_number is None:
        return {}
    unit = _unit_from_column_label(clean)
    if unit == "unit unavailable":
        unit = "US$m" if "us$m" in lower or "us$ million" in lower else "$m"
    if not _unit_compatible(unit, profile):
        return {}
    total = _format_numeric_total(current_number + non_current_number)
    if _value_validation_failure(total, unit, profile):
        return {}
    current_prior = current_match.group("prior").replace(",", "").strip("()")
    non_current_prior = non_current_match.group("prior").replace(",", "").strip("()")
    prior_total = "unavailable"
    current_prior_number = _numeric_string_to_float(current_prior)
    non_current_prior_number = _numeric_string_to_float(non_current_prior)
    if current_prior_number is not None and non_current_prior_number is not None:
        prior_total = _format_numeric_total(current_prior_number + non_current_prior_number)
    period_reference = "FY2025"
    comparison_reference = "FY2024"
    source_page_match = re.search(r"(?:page\s+|/)(9[0-9]|1[01][0-9])(?:/|\b)", clean, re.IGNORECASE)
    source_page = source_page_match.group(1) if source_page_match else "unavailable"
    support_start = max(0, current_section_match.start() - 120)
    support_end = min(len(clean), non_current_section_match.end() + 120)
    supporting_sentence = _clean_text(clean[support_start:support_end])
    return {
        **base,
        "clean_metric_value": total,
        "value_unit": unit,
        "value_context": "flattened balance-sheet current and non-current interest-bearing liabilities total",
        "metric_value_status": "value_extracted",
        "association_score": 90,
        "association_reason": "CSL flattened balance-sheet text contains current and non-current interest-bearing liabilities and borrowings rows",
        "period_reference": period_reference,
        "comparison_reference": comparison_reference,
        "supporting_sentence": supporting_sentence[:600],
        "comparison_basis": "current and non-current balance-sheet liabilities summed",
        "direction": "neutral",
        "confidence": "medium",
        "confidence_reason": "clean value accepted because flattened balance-sheet text preserves both current and non-current borrowings rows",
        "table_title": "Consolidated Balance Sheet",
        "source_section": "Consolidated Balance Sheet",
        "row_label": "total interest-bearing liabilities and borrowings",
        "column_label": f"{period_reference} {unit}",
        "cell_value": total,
        "source_page": source_page,
        "table_mapping_confidence": 90,
        "table_mapping_reason": "flattened current/non-current borrowings rows mapped from balance-sheet text",
        "raw_row_text": _clean_text(f"{current_match.group(0)} | {non_current_match.group(0)}"),
        "current_period_value": total,
        "prior_period_value": prior_total,
        "table_values": {
            "current_interest_bearing_liabilities_and_borrowings": current_value,
            "non_current_interest_bearing_liabilities_and_borrowings": non_current_value,
            "current_period_value": total,
            "prior_period_value": prior_total,
        },
    }


def _segment_growth_association(clean: str, profile: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    if not _accepted_status(profile, "segment_growth"):
        return {}
    pattern = re.compile(
        r"\b(?P<segment>CSL\s+(?:Behring|Seqirus|Vifor))\b.{0,80}?\b(?:revenue|sales)\b"
        r".{0,80}?\b(?P<direction>increased|increase|grew|growth|decreased|declined|decline)\b"
        r".{0,40}?(?P<value>\d+(?:\.\d+)?)\s*%",
        re.IGNORECASE,
    )
    match = pattern.search(clean)
    if not match:
        return {}
    segment = _clean_text(match.group("segment"))
    clean_value = match.group("value")
    support_sentence = next((sentence for sentence in _sentences(clean) if match.group(0) in sentence), clean[:240])
    direction_word = match.group("direction").lower()
    direction = "supportive" if direction_word in {"increased", "increase", "grew", "growth"} else "adverse"
    return {
        **base,
        "clean_metric_value": clean_value,
        "value_unit": "%",
        "value_context": f"{segment} revenue growth",
        "metric_value_status": "segment_growth",
        "association_score": 86,
        "association_reason": "segment revenue growth percentage is accepted because current segment revenue value is unavailable",
        "period_reference": _period_references(clean)[0],
        "comparison_reference": _period_references(clean)[1],
        "supporting_sentence": support_sentence[:240],
        "comparison_basis": "segment revenue growth",
        "direction": direction,
        "confidence": "medium",
        "confidence_reason": "segment growth accepted as an alternate CSL segment evidence status",
        "segment_name": segment,
    }


def _special_status_for_value_candidate(metric_name: str, best: dict[str, Any], profile: dict[str, Any]) -> str:
    support = " ".join(
        str(best.get(field) or "")
        for field in ("supporting_sentence", "row_label", "column_label", "table_title", "value_context")
    )
    support_lower = support.lower()
    unit = str(best.get("value_unit") or "").lower()
    if metric_name == "segment_revenue" and _accepted_status(profile, "segment_growth"):
        if unit in {"%", "per cent"} and re.search(r"\b(?:growth|grew|increased|increase|declined|decreased|change)\b", support_lower):
            return "segment_growth"
    if metric_name == "margins" and _accepted_status(profile, "profitability_metric"):
        if re.search(
            r"\b(?:npata|ebit|ebita|operating profit|underlying profit|net profit after tax before amortisation)\b",
            support_lower,
        ) and "margin" not in support_lower:
            return "profitability_metric"
    return "value_extracted"


def _extract_metric_value_from_text(
    text: str,
    metric_name: str,
    *,
    ticker_plugin: dict[str, Any] | None = None,
) -> dict[str, Any]:
    profile = _profile_for_metric_context(metric_name, ticker_plugin)
    clean = _clean_text(text)
    base = {
        "clean_metric_value": "unavailable",
        "value_unit": "unavailable",
        "value_context": "no high-confidence metric-value association",
        "metric_value_status": "unavailable",
        "association_score": 0,
        "association_reason": "metric label was not found in extracted text",
        "period_reference": "unavailable",
        "comparison_reference": "unavailable",
        "supporting_sentence": "no supporting sentence extracted",
        "comparison_basis": "unavailable",
        "direction": "unavailable",
        "confidence": "low",
        "confidence_reason": "no supportable metric evidence found",
        "table_title": "unavailable",
        "row_label": "unavailable",
        "column_label": "unavailable",
        "source_page": "unavailable",
        "cell_value": "unavailable",
        "table_mapping_confidence": 0,
        "table_mapping_reason": "no table row mapping available",
        "raw_row_text": "unavailable",
        "current_period_value": "unavailable",
        "prior_period_value": "unavailable",
        "variance_value": "unavailable",
        "variance_percent": "unavailable",
    }
    if not profile:
        return base
    if metric_name == "realised_price":
        realised_price = _bhp_flattened_realised_price_association(clean, profile, base)
        if realised_price:
            return realised_price
    if metric_name == "debt":
        csl_debt = _csl_flattened_debt_balance_sheet_association(clean, profile, base)
        if csl_debt:
            return csl_debt
    if metric_name == "segment_revenue":
        segment_card = _csl_segment_revenue_card_association(clean, profile, base)
        if segment_card:
            return segment_card
        segment_growth = _segment_growth_association(clean, profile, base)
        if segment_growth:
            return segment_growth
    if metric_name == "margins":
        profitability_metric = _csl_profitability_metric_association(clean, profile, base)
        if profitability_metric:
            return profitability_metric
    early_narrative = _narrative_metric_association(metric_name=metric_name, clean=clean, profile=profile, base=base)
    if early_narrative and not _metric_label_present(clean, profile):
        return early_narrative
    label_present = _metric_label_present(clean, profile)
    if not label_present:
        return base
    navigation_context = _is_navigation_or_toc(clean)
    metric_context = _best_metric_context(clean, profile)
    metric_context_is_navigation = _is_navigation_or_toc(metric_context)
    best = _extract_table_metric_value(text, metric_name, profile)
    if best and best.get("metric_value_status") == "unavailable":
        best = {}
    if not best and metric_name not in STRICT_STRUCTURED_VALUE_METRICS:
        for sentence in _sentences(clean):
            if not _label_matches(sentence, profile):
                continue
            if _dense_table_row_signal(sentence):
                dense_candidate = _extract_dense_metric_row_value(sentence, metric_name, profile)
                if dense_candidate:
                    best = dense_candidate if not best or dense_candidate["score"] > best["score"] else best
                    continue
                return _table_row_unparsed_result(base, sentence, profile)
            candidate = _best_label_value_association(sentence, metric_name, profile)
            if not candidate:
                continue
            if not best:
                best = candidate
                continue
            candidate_high = candidate["score"] >= 80
            best_high = best["score"] >= 80
            if candidate_high and best_high:
                continue
            if candidate["score"] > best["score"]:
                best = candidate
    if not best and metric_name not in STRICT_STRUCTURED_VALUE_METRICS and _dense_table_row_signal(metric_context):
        best = _extract_dense_metric_row_value(metric_context, metric_name, profile)
    if not best and _dense_table_row_signal(metric_context):
        return _table_row_unparsed_result(base, metric_context, profile)
    if not best and navigation_context and metric_context_is_navigation:
        return {
            **base,
            "metric_value_status": "context_only",
            "association_reason": "navigation or table-of-contents context is not metric evidence",
            "supporting_sentence": metric_context[:240] or base["supporting_sentence"],
            "direction": "context_only",
            "confidence_reason": "downgraded because extracted text is navigation/table-of-contents context",
        }
    narrative = _narrative_metric_association(metric_name=metric_name, clean=clean, profile=profile, base=base)
    if not best and narrative:
        return narrative
    support_sentence = clean[:240]
    for sentence in _sentences(clean):
        if _label_matches(sentence, profile):
            support_sentence = sentence[:240]
            break
    direction = _direction_from_profile(support_sentence, profile)
    if not best:
        status = "direction_extracted" if direction != "neutral" else "metric_mentioned_only"
        confidence_reason = (
            "directional wording is present but no compatible clean metric value was attached"
            if status == "direction_extracted"
            else "metric label is present but no clean value or direction was extracted"
        )
        return {
            **base,
            "metric_value_status": status,
            "association_score": 45 if status == "direction_extracted" else 35,
            "association_reason": "metric label present but no compatible value found; competing or rejected labels may be closer",
            "supporting_sentence": support_sentence,
            "comparison_basis": "period-over-period wording in extracted filing/report phrase"
            if status == "direction_extracted"
            else "metric mentioned without explicit comparative baseline",
            "direction": direction,
            "confidence": "low",
            "confidence_reason": confidence_reason,
        }
    score = int(best["score"])
    has_table_mapping = "table_mapping_confidence" in best
    unit_missing_for_profile = (
        score >= 80
        and bool(profile.get("accepted_units"))
        and str(best.get("value_unit") or "").lower() in {"", "unavailable", "unit unavailable"}
    )
    status = (
        "value_extracted"
        if score >= 80 and not unit_missing_for_profile
        else (
            "table_row_unparsed"
            if has_table_mapping
            else ("direction_extracted" if best["direction"] != "neutral" or score >= 50 else "metric_mentioned_only")
        )
    )
    if status == "value_extracted":
        status = _special_status_for_value_candidate(metric_name, best, profile)
    if unit_missing_for_profile:
        status = "direction_extracted" if best["direction"] != "neutral" else "metric_mentioned_only"
    clean_value = best["clean_metric_value"] if status in VALUE_BEARING_STATUSES else "unavailable"
    confidence = "medium" if status in VALUE_BEARING_STATUSES else "low"
    confidence_reason = (
        "clean value accepted because metric label, compatible unit, and proximity met threshold"
        if status in VALUE_BEARING_STATUSES
        else (
            "clean value withheld because accepted metric units were not preserved in the source text"
            if unit_missing_for_profile
            else (
                "clean value withheld because table row mapping confidence is below accepted threshold"
                if status == "table_row_unparsed"
                else "clean value withheld because association score is below accepted threshold"
            )
        )
    )
    association_reason = best["association_reason"]
    if unit_missing_for_profile:
        association_reason = f"{association_reason}; accepted unit was unavailable so clean value was suppressed"
    lease_liabilities_warning = (
        metric_name == "debt"
        and status in VALUE_BEARING_STATUSES
        and re.search(
            r"\blease liabilities\b",
            " ".join(str(best.get(field) or "") for field in ("supporting_sentence", "row_label", "value_context")),
            re.IGNORECASE,
        )
    )
    if lease_liabilities_warning:
        association_reason = f"{association_reason}; lease liabilities are balance-sheet debt evidence, not total debt"
        confidence_reason = f"{confidence_reason}; lease liabilities are balance-sheet debt evidence, not total debt"
    return {
        **base,
        "metric_subtype": "lease_liabilities_balance_sheet_debt" if lease_liabilities_warning else base.get("metric_subtype", ""),
        "clean_metric_value": clean_value,
        "value_unit": best["value_unit"] if status in VALUE_BEARING_STATUSES else "unavailable",
        "value_context": best["value_context"] if status in VALUE_BEARING_STATUSES else "value association below acceptance threshold",
        "metric_value_status": status,
        "association_score": score,
        "association_reason": association_reason,
        "period_reference": best.get("period_reference", "not specified"),
        "comparison_reference": best.get("comparison_reference", "not specified"),
        "supporting_sentence": best["supporting_sentence"][:240],
        "comparison_basis": "period-over-period wording in extracted filing/report phrase"
        if best["direction"] != "neutral"
        else "metric mentioned without explicit comparative baseline",
        "direction": best["direction"],
        "confidence": confidence,
        "confidence_reason": confidence_reason,
        "table_title": best.get("table_title", "unavailable"),
        "row_label": best.get("row_label", "unavailable"),
        "column_label": best.get("column_label", "unavailable"),
        "source_page": best.get("source_page", "unavailable"),
        "cell_value": best.get("cell_value", "unavailable") if status in VALUE_BEARING_STATUSES else "unavailable",
        "table_mapping_confidence": best.get("table_mapping_confidence", 0),
        "table_mapping_reason": best.get("table_mapping_reason", "no structured table mapping available"),
        "raw_row_text": best.get("raw_row_text", "unavailable"),
        "current_period_value": best.get("current_period_value", "unavailable"),
        "prior_period_value": best.get("prior_period_value", "unavailable"),
        "variance_value": best.get("variance_value", "unavailable"),
        "variance_percent": best.get("variance_percent", "unavailable"),
        "segment_name": _segment_name_in_text(
            " ".join(str(best.get(field) or "") for field in ("supporting_sentence", "row_label", "table_title", "value_context"))
        ),
    }


def _metric_specs_for_sector(sector: str) -> list[tuple[str, str, list[str]]]:
    profile_specs = _metric_profiles_for_sector(sector)
    legacy_specs = ASX_SECTOR_METRIC_PATTERNS.get(sector, [])
    legacy_supports = {name: supports_claims for name, _label, _pattern, supports_claims in legacy_specs}
    specs: list[tuple[str, str, list[str]]] = []
    if profile_specs:
        for metric_name, profile in profile_specs.items():
            labels = [str(label) for label in profile.get("accepted_labels", []) or [metric_name]]
            metric_label = labels[0]
            supports_claims = legacy_supports.get(metric_name, [metric_label])
            specs.append((metric_name, metric_label, supports_claims))
        return specs
    return [(name, label, supports_claims) for name, label, _pattern, supports_claims in legacy_specs]


def _int_metric_field(value: Any) -> int:
    try:
        return int(float(str(value or "0")))
    except ValueError:
        return 0


def _metric_label_value_distance(association: dict[str, Any]) -> int:
    reason = str(association.get("association_reason") or "")
    match = re.search(r"label-value distance\s+(\d+)\s+tokens", reason, re.IGNORECASE)
    if match:
        return int(match.group(1))
    if association.get("metric_value_status") == "value_extracted" and association.get("row_label") not in {"", "unavailable"}:
        return 0
    return 999


def _competing_labels_from_association(association: dict[str, Any]) -> list[str]:
    reason = str(association.get("association_reason") or "")
    match = re.search(r"competing labels nearby:\s*([^;]+)", reason, re.IGNORECASE)
    if not match:
        return []
    return [label.strip() for label in match.group(1).split(",") if label.strip()]


def _footnote_header_footer_penalty(text: str) -> int:
    lower = text.lower()
    if re.search(r"\b(?:footnote|note\s+\d+|page\s+\d+\s+of\s+\d+|continued|unaudited)\b", lower):
        return 30
    return 0


def _source_quality_bonus(source_quality_tier: str) -> int:
    return {
        "tier_1_asx_lodged_pdf": 15,
        "tier_2_company_results_pdf": 10,
        "tier_3_company_annual_report_pdf": 6,
        "tier_3_structured_online_annual_report": 6,
    }.get(source_quality_tier, -50)


def _document_role_bonus(document_role: str) -> int:
    return {
        "appendix_4e": 12,
        "financial_report_pdf": 11,
        "annual_report": 10,
        "results_presentation": 8,
        "investor_presentation": 4,
    }.get(document_role, -20)


def _section_relevance_bonus(section_title: str, text: str) -> int:
    if section_title == "navigation_or_table_of_contents" or _is_navigation_or_toc(text):
        return -40
    if section_title in {
        "financial_statement_tables",
        "segment_product_tables",
        "segment_product_performance",
        "cash_debt_gearing",
        "capex_commitments",
        "cash_flow_statement",
        "revenue_income_npat",
    }:
        return 8
    if section_title != "unclassified_text":
        return 4
    return 0


def _plugin_section_bonus(profile: dict[str, Any], section_title: str, text: str) -> int:
    haystack = f"{section_title} {text}".lower()
    bonus = 0
    if any(str(term).lower() in haystack for term in profile.get("preferred_sections", []) or []):
        bonus += 10
    if any(str(term).lower() in haystack for term in profile.get("preferred_tables", []) or []):
        bonus += 8
    if any(str(term).lower() in haystack for term in profile.get("reject_sections", []) or []):
        bonus -= 35
    if any(str(term).lower() in haystack for term in profile.get("reject_contexts", []) or []):
        bonus -= 35
    return bonus


def _metric_status_rank(status: str) -> int:
    return {
        "value_extracted": 5,
        "segment_growth": 5,
        "profitability_metric": 5,
        "portfolio_mix_narrative": 4,
        "guidance_narrative": 4,
        "plasma_network_narrative": 4,
        "table_row_unparsed": 3,
        "direction_extracted": 2,
        "metric_mentioned_only": 1,
        "context_only": 0,
        "unavailable": -1,
    }.get(status, -1)


def _metric_candidate_from_association(
    *,
    association: dict[str, Any],
    source: dict[str, Any],
    page_number: str,
    section_title: str,
    candidate_text: str,
    candidate_origin: str,
    profile: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    status = str(association.get("metric_value_status") or "unavailable")
    if status == "unavailable":
        return None
    source_quality_tier = str(source.get("source_quality_tier") or "tier_5_navigation_or_archive_page")
    document_role = str(source.get("document_role") or "unknown")
    navigation_penalty = 50 if section_title == "navigation_or_table_of_contents" or _is_navigation_or_toc(candidate_text) else 0
    footnote_penalty = _footnote_header_footer_penalty(candidate_text)
    association_score = _int_metric_field(association.get("association_score"))
    table_mapping_confidence = _int_metric_field(association.get("table_mapping_confidence"))
    table_bonus = 8 if table_mapping_confidence >= 80 else 0
    unmapped_table_text_penalty = 12 if candidate_origin == "table" and table_mapping_confidence < 80 else 0
    plugin_section_bonus = _plugin_section_bonus(profile or {}, section_title, candidate_text)
    candidate_score = max(
        0,
        min(
            100,
            association_score
            + _source_quality_bonus(source_quality_tier)
            + _document_role_bonus(document_role)
            + _section_relevance_bonus(section_title, candidate_text)
            + plugin_section_bonus
            + table_bonus
            - navigation_penalty
            - footnote_penalty
            - unmapped_table_text_penalty,
        ),
    )
    source_page = str(association.get("source_page") or page_number or "unavailable")
    if source_page == "unavailable" and page_number:
        source_page = page_number
    return {
        **association,
        "candidate_score": candidate_score,
        "candidate_origin": candidate_origin,
        "source_quality_tier": source_quality_tier,
        "document_role": document_role,
        "extraction_status": str(source.get("extraction_status") or "unavailable"),
        "metric_eligibility": str(source.get("metric_eligibility") or "not_eligible"),
        "section_title": section_title,
        "source_page": source_page,
        "metric_label_value_distance_tokens": _metric_label_value_distance(association),
        "competing_labels_near_value": _competing_labels_from_association(association),
        "navigation_toc_penalty": navigation_penalty,
        "footnote_header_footer_penalty": footnote_penalty,
        "ticker_plugin": source.get("ticker_plugin", "unavailable"),
    }


def _downgrade_unmapped_table_text_association(association: dict[str, Any]) -> dict[str, Any]:
    return {
        **association,
        "metric_value_status": "table_row_unparsed",
        "clean_metric_value": "unavailable",
        "value_unit": "unavailable",
        "value_context": "value association below acceptance threshold",
        "cell_value": "unavailable",
        "confidence": "low",
        "confidence_reason": "clean value withheld because table-origin text lacked row/column mapping",
        "association_reason": (
            f"{association.get('association_reason', 'table-origin text candidate')}; "
            "clean value withheld because table-origin text lacked row/column mapping"
        ),
    }


def _metric_candidate_sort_key(candidate: dict[str, Any]) -> tuple[int, int, int, int, int, int]:
    source_quality_tier = str(candidate.get("source_quality_tier") or "")
    table_mapping_confidence = _int_metric_field(candidate.get("table_mapping_confidence"))
    origin_rank = 2 if table_mapping_confidence >= 80 else (1 if candidate.get("candidate_origin") == "text_block" else 0)
    return (
        _metric_status_rank(str(candidate.get("metric_value_status") or "")),
        _int_metric_field(candidate.get("candidate_score")),
        _int_metric_field(candidate.get("association_score")),
        table_mapping_confidence,
        origin_rank,
        -SOURCE_QUALITY_RANK.get(source_quality_tier, 99),
    )


def _extract_metric_value_from_document(
    document_structure: dict[str, Any],
    metric_name: str,
    source: dict[str, Any],
    *,
    ticker_plugin: dict[str, Any] | None = None,
) -> dict[str, Any]:
    profile = _profile_for_metric_context(metric_name, ticker_plugin)
    if not profile:
        return _extract_metric_value_from_text("", metric_name)
    targeted = _extract_ticker_targeted_metric_value(
        document_structure=document_structure,
        metric_name=metric_name,
        ticker_plugin=ticker_plugin,
        source=source,
        profile=profile,
    )
    targeted_diagnostics = targeted.get("metric_diagnostics") if targeted else None
    if targeted.get("metric_value_status") == "value_extracted":
        return targeted
    candidates: list[dict[str, Any]] = []
    for page in document_structure.get("pages", []):
        page_number = str(page.get("page_number") or "unavailable")
        for table in page.get("tables", []):
            table_text = _table_text_from_structured_table(table)
            if not table_text or (
                not _metric_label_present(table_text, profile)
                and not _narrative_context_present(metric_name, table_text, profile)
            ):
                continue
            association = _extract_metric_value_from_text(table_text, metric_name, ticker_plugin=ticker_plugin)
            if (
                profile.get("reject_unmapped_table_text")
                and association.get("metric_value_status") == "value_extracted"
                and _int_metric_field(association.get("table_mapping_confidence")) < 80
            ):
                association = _downgrade_unmapped_table_text_association(association)
            candidate = _metric_candidate_from_association(
                association=association,
                source=source,
                page_number=page_number,
                section_title=str(table.get("section_title") or "financial_statement_tables"),
                candidate_text=table_text,
                candidate_origin="table",
                profile=profile,
            )
            if candidate:
                candidates.append(candidate)
        for block in page.get("text_blocks", []):
            block_text = str(block.get("text") or "")
            if not block_text or (
                not _metric_label_present(block_text, profile)
                and not _narrative_context_present(metric_name, block_text, profile)
            ):
                continue
            association = _extract_metric_value_from_text(block_text, metric_name, ticker_plugin=ticker_plugin)
            candidate = _metric_candidate_from_association(
                association=association,
                source=source,
                page_number=page_number,
                section_title=str(block.get("section_title") or _section_title_for_text(block_text)),
                candidate_text=block_text,
                candidate_origin="text_block",
                profile=profile,
            )
            if candidate:
                candidates.append(candidate)
    if not candidates:
        result = _extract_metric_value_from_text("", metric_name)
        result["association_reason"] = "metric label was not found in eligible structured pages, sections, or tables"
        if targeted_diagnostics:
            result["metric_diagnostics"] = targeted_diagnostics
        return result
    best = max(candidates, key=_metric_candidate_sort_key)
    if targeted_diagnostics and best.get("metric_value_status") != "value_extracted":
        best["metric_diagnostics"] = targeted_diagnostics
    return best


def _metric_subtype(metric_name: str, association: dict[str, Any]) -> str:
    value_type = str(association.get("value_type") or "").lower()
    column_label = str(association.get("column_label") or "").lower()
    row_label = str(association.get("row_label") or "").lower()
    value_unit = str(association.get("value_unit") or "").lower()
    if metric_name == "inventory":
        if "net investment" in row_label or "variance" in column_label or "change" in column_label or value_type in {
            "variance_value",
            "variance_percent",
        }:
            return "inventory_or_working_capital_movement"
        return "inventory_balance"
    if metric_name in {"dividend", "dividends"}:
        if value_unit == "%" or "variance" in column_label or "change" in column_label or value_type == "variance_percent":
            return "dividend_change_percent"
        return "dividend_amount_or_dps"
    return ""


def _extract_sector_metrics(
    text: str,
    source: dict[str, Any],
    excerpt_chars: int,
    sector: str,
    *,
    ticker_plugin: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    specs = _metric_specs_for_sector(sector)
    if not specs:
        return []
    metrics: list[dict[str, Any]] = []
    document_structure = source.get("document_structure")
    if not isinstance(document_structure, dict):
        document_structure = _build_document_structure(text)
    metric_source = {
        **source,
        "source_quality_tier": source.get("source_quality_tier") or "tier_1_asx_lodged_pdf",
        "document_role": source.get("document_role") or "annual_report",
        "extraction_status": source.get("extraction_status") or "available",
    }
    metric_source["metric_eligibility"] = source.get("metric_eligibility") or _metric_eligibility(
        str(metric_source["source_quality_tier"]),
        str(metric_source["document_role"]),
        str(metric_source["extraction_status"]),
    )
    if metric_source["metric_eligibility"] != "eligible_financial_document":
        return []
    for metric_name, metric_label, supports_claims in specs:
        section_name = f"sector_metric_{metric_name}"
        association = _extract_metric_value_from_document(
            document_structure,
            metric_name,
            metric_source,
            ticker_plugin=ticker_plugin,
        )
        if association["metric_value_status"] == "unavailable":
            reason = f"{metric_label} was not identified in extracted ASX document text."
            metrics.append(
                {
                    **_section_unavailable(
                        section_name=section_name,
                        section_type="sector_metric",
                        source=source,
                        supports_claims=supports_claims,
                        reason=reason,
                    ),
                    "metric_name": metric_name,
                    "metric_label": metric_label,
                    "sector": sector,
                    "metric_subtype": "",
                    "source_quality_tier": metric_source["source_quality_tier"],
                    "document_role": metric_source["document_role"],
                    "extraction_status": metric_source["extraction_status"],
                    "metric_eligibility": metric_source["metric_eligibility"],
                    "candidate_score": 0,
                    "candidate_origin": "unavailable",
                    "section_title": "unavailable",
                    "metric_label_value_distance_tokens": 999,
                    "competing_labels_near_value": [],
                    "navigation_toc_penalty": 0,
                    "footnote_header_footer_penalty": 0,
                    "metric_confidence": "low",
                    "clean_metric_value": "unavailable",
                    "value_unit": "unavailable",
                    "value_context": "metric label unavailable",
                    "metric_value_status": "unavailable",
                    "association_score": 0,
                    "association_reason": reason,
                    "period_reference": "unavailable",
                    "comparison_reference": "unavailable",
                    "supporting_sentence": "no supporting sentence extracted",
                    "comparison_basis": "unavailable",
                    "direction": "unavailable",
                    "confidence": "low",
                    "confidence_reason": reason,
                    "table_title": "unavailable",
                    "row_label": "unavailable",
                    "column_label": "unavailable",
                    "source_page": "unavailable",
                    "ticker_plugin": metric_source.get("ticker_plugin", "unavailable"),
                }
            )
            continue
        excerpt = str(association["supporting_sentence"])[:excerpt_chars].rsplit(" ", 1)[0].strip()
        metrics.append(
            {
                "section_name": section_name,
                "section_type": "sector_metric",
                "status": "available",
                "source_type": source["source_type"],
                "filing_date": source["announcement_date"],
                "url": source.get("url", ""),
                "excerpt": excerpt,
                "supports_claims": supports_claims,
                "unavailable_reason": "",
                "evidence_gap": "",
                "metric_name": metric_name,
                "metric_label": metric_label,
                "sector": sector,
                "metric_confidence": association["confidence"],
                "extracted_value_or_phrase": association["supporting_sentence"],
                **association,
                "metric_subtype": _metric_subtype(metric_name, association),
            }
        )
    return metrics


def _extract_sections(
    text: str,
    source: dict[str, Any],
    excerpt_chars: int,
    sector: str = "general",
    *,
    include_sector_metrics: bool = True,
    ticker_plugin: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    clean = _clean_text(text)
    for section_name, pattern, supports_claims in SECTION_PATTERNS:
        match = re.search(pattern, clean, re.IGNORECASE)
        if not match:
            sections.append(
                _section_unavailable(
                    section_name=section_name,
                    source=source,
                    supports_claims=supports_claims,
                    reason=f"{section_name} was not identified in extracted ASX document text.",
                )
            )
            continue
        excerpt = clean[match.start() : match.start() + excerpt_chars]
        sections.append(
            {
                "section_name": section_name,
                "section_type": section_name,
                "status": "available",
                "source_type": source["source_type"],
                "filing_date": source["announcement_date"],
                "url": source.get("url", ""),
                "excerpt": excerpt.rsplit(" ", 1)[0].strip(),
                "supports_claims": supports_claims,
                "unavailable_reason": "",
                "evidence_gap": "",
            }
        )
    if include_sector_metrics:
        sections.extend(_extract_sector_metrics(text, source, excerpt_chars, sector, ticker_plugin=ticker_plugin))
    return sections


def _table_extraction_diagnostics(text: str, sections: list[dict[str, Any]]) -> dict[str, Any]:
    table_rows: list[dict[str, Any]] = []
    by_strategy: dict[str, int] = {}
    by_table: dict[str, int] = {}
    metric_rows: list[dict[str, Any]] = []
    for line in text.splitlines():
        if TABLE_ROW_MARKER not in line:
            continue
        metadata, cells = _parse_structured_table_line(line)
        title = metadata.get("table_title", "unavailable")
        table_key = f"page_{metadata.get('source_page', 'unavailable')}_table_{metadata.get('table_index', 'unavailable')}_{title}"
        strategy = _table_strategy_from_title(title)
        by_strategy[strategy] = by_strategy.get(strategy, 0) + 1
        by_table[table_key] = by_table.get(table_key, 0) + 1
        row = {
            "source_page": metadata.get("source_page", "unavailable"),
            "table_index": metadata.get("table_index", "unavailable"),
            "row_index": metadata.get("row_index", "unavailable"),
            "table_title": title,
            "strategy": strategy,
            "cell_count": len(cells),
            "numeric_cell_count": sum(1 for cell in cells if _cell_has_number(cell)),
            "raw_row_text": " | ".join(cells),
        }
        table_rows.append(row)
        if any(re.search(rf"\b{re.escape(label)}\b", " ".join(cells), re.IGNORECASE) for label in DENSE_TABLE_ROW_LABELS):
            metric_rows.append(row)
    unparsed_metrics = [
        {
            "metric_name": section.get("metric_name", "unavailable"),
            "metric_value_status": section.get("metric_value_status", "unavailable"),
            "association_score": section.get("association_score", 0),
            "association_reason": section.get("association_reason", ""),
            "supporting_sentence": section.get("supporting_sentence", ""),
            "row_label": section.get("row_label", "unavailable"),
            "column_label": section.get("column_label", "unavailable"),
        }
        for section in sections
        if section.get("section_type") == "sector_metric" and section.get("metric_value_status") == "table_row_unparsed"
    ]
    return {
        "table_rows_detected": len(table_rows),
        "table_rows_by_strategy": by_strategy,
        "table_rows_by_table": by_table,
        "metric_like_table_rows": metric_rows[:50],
        "table_row_unparsed_metrics": unparsed_metrics,
    }


def _table_strategy_from_title(title: str) -> str:
    lower = title.lower()
    if "crop" in lower:
        return "pdfplumber_crop"
    if "words" in lower:
        return "pdfplumber_words"
    if "text_table" in lower:
        return "pdfplumber_text"
    if "lines_table" in lower:
        return "pdfplumber_lines"
    return "pdfplumber_default"


def _source_selection_sort_key(source: dict[str, Any]) -> tuple[int, int, str]:
    source_quality_tier = str(source.get("source_quality_tier") or "tier_5_navigation_or_archive_page")
    document_role = str(source.get("document_role") or "unknown")
    return (
        SOURCE_QUALITY_RANK.get(source_quality_tier, 99),
        DOCUMENT_ROLE_RANK.get(document_role, 99),
        str(source.get("announcement_date") or source.get("lodgement_date") or ""),
    )


def _eligible_metric_source(source: dict[str, Any]) -> bool:
    return (
        source.get("status") == "available"
        and source.get("extraction_status") == "available"
        and source.get("metric_eligibility") == "eligible_financial_document"
        and source.get("source_quality_tier") in ELIGIBLE_SOURCE_QUALITY_TIERS
    )


def _select_authoritative_metric_sources(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted([source for source in sources if _eligible_metric_source(source)], key=_source_selection_sort_key)


def _remove_existing_sector_metrics(sources: list[dict[str, Any]]) -> None:
    for source in sources:
        source["extracted_sections"] = [
            section
            for section in source.get("extracted_sections", [])
            if section.get("section_type") != "sector_metric"
        ]


def _unavailable_sector_metric_section(
    *,
    source: dict[str, Any],
    metric_name: str,
    metric_label: str,
    supports_claims: list[str],
    sector: str,
    reason: str,
) -> dict[str, Any]:
    section_name = f"sector_metric_{metric_name}"
    return {
        **_section_unavailable(
            section_name=section_name,
            section_type="sector_metric",
            source=source,
            supports_claims=supports_claims,
            reason=reason,
        ),
        "metric_name": metric_name,
        "metric_label": metric_label,
        "sector": sector,
        "source_quality_tier": source.get("source_quality_tier", "tier_5_navigation_or_archive_page"),
        "document_role": source.get("document_role", "unknown"),
        "extraction_status": source.get("extraction_status", "unavailable"),
        "metric_eligibility": source.get("metric_eligibility", "not_eligible"),
        "metric_subtype": "",
        "candidate_score": 0,
        "candidate_origin": "unavailable",
        "section_title": "unavailable",
        "metric_candidate_count": 0,
        "metric_label_value_distance_tokens": 999,
        "competing_labels_near_value": [],
        "navigation_toc_penalty": 0,
        "footnote_header_footer_penalty": 0,
        "metric_confidence": "low",
        "clean_metric_value": "unavailable",
        "value_unit": "unavailable",
        "value_context": "metric label unavailable",
        "metric_value_status": "unavailable",
        "association_score": 0,
        "association_reason": reason,
        "period_reference": "unavailable",
        "comparison_reference": "unavailable",
        "supporting_sentence": "no supporting sentence extracted",
        "comparison_basis": "unavailable",
        "direction": "unavailable",
        "confidence": "low",
        "confidence_reason": reason,
        "table_title": "unavailable",
        "row_label": "unavailable",
        "column_label": "unavailable",
        "source_page": "unavailable",
        "cell_value": "unavailable",
        "table_mapping_confidence": 0,
        "table_mapping_reason": "no table row mapping available",
        "raw_row_text": "unavailable",
        "current_period_value": "unavailable",
        "prior_period_value": "unavailable",
        "variance_value": "unavailable",
        "variance_percent": "unavailable",
    }


def _sector_metric_section_from_candidate(
    *,
    source: dict[str, Any],
    association: dict[str, Any],
    metric_name: str,
    metric_label: str,
    supports_claims: list[str],
    sector: str,
    excerpt_chars: int,
    candidate_count: int,
) -> dict[str, Any]:
    excerpt = str(association.get("supporting_sentence") or "")[:excerpt_chars].rsplit(" ", 1)[0].strip()
    return {
        "section_name": f"sector_metric_{metric_name}",
        "section_type": "sector_metric",
        "status": "available",
        "source_type": source["source_type"],
        "filing_date": source["announcement_date"],
        "url": source.get("url", ""),
        "excerpt": excerpt,
        "supports_claims": supports_claims,
        "unavailable_reason": "",
        "evidence_gap": "",
        "metric_name": metric_name,
        "metric_label": metric_label,
        "sector": sector,
        "metric_confidence": association["confidence"],
        "extracted_value_or_phrase": association["supporting_sentence"],
        "metric_candidate_count": candidate_count,
        **association,
        "metric_subtype": _metric_subtype(metric_name, association),
    }


def _apply_authoritative_sector_metric_extraction(
    sources: list[dict[str, Any]],
    *,
    sector: str,
    excerpt_chars: int,
    ticker_plugin: dict[str, Any] | None = None,
) -> tuple[str, list[dict[str, Any]]]:
    _remove_existing_sector_metrics(sources)
    specs = _metric_specs_for_sector(sector)
    if not specs:
        return "no_sector_metric_profile", []
    selected_sources = _select_authoritative_metric_sources(sources)
    if not selected_sources:
        return "no_eligible_financial_sources", []
    for metric_name, metric_label, supports_claims in specs:
        candidates: list[tuple[dict[str, Any], dict[str, Any]]] = []
        for source in selected_sources:
            document_structure = source.get("document_structure")
            if not isinstance(document_structure, dict):
                document_structure = _build_document_structure(str(source.get("excerpt") or ""))
            association = _extract_metric_value_from_document(
                document_structure,
                metric_name,
                source,
                ticker_plugin=ticker_plugin,
            )
            if association["metric_value_status"] != "unavailable":
                candidates.append((source, association))
        if candidates:
            selected_source, selected_association = max(
                candidates,
                key=lambda item: _metric_candidate_sort_key(item[1]),
            )
            selected_source.setdefault("extracted_sections", []).append(
                _sector_metric_section_from_candidate(
                    source=selected_source,
                    association=selected_association,
                    metric_name=metric_name,
                    metric_label=metric_label,
                    supports_claims=supports_claims,
                    sector=sector,
                    excerpt_chars=excerpt_chars,
                    candidate_count=len(candidates),
                )
            )
            continue
        primary_source = selected_sources[0]
        primary_source.setdefault("extracted_sections", []).append(
            _unavailable_sector_metric_section(
                source=primary_source,
                metric_name=metric_name,
                metric_label=metric_label,
                supports_claims=supports_claims,
                sector=sector,
                reason=f"{metric_label} was not identified in selected eligible ASX financial documents.",
            )
        )
    return "metrics_extracted_from_authoritative_sources", selected_sources


def _source_from_row(
    row: dict[str, Any],
    *,
    trade_date: str,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
    source_type: str = "asx_announcement",
    asx_sector: str = "general",
    ticker_plugin: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    title = _field(row, "title", "header", "headline", "description")
    url = _document_url(row)
    document_type = _classify_document_with_plugin(title, url, ticker_plugin)
    if not document_type:
        return None
    raw_date = _field(row, "announcement_date", "lodgement_date", "date", "releaseDate", "lodgementDate")
    try:
        parsed_date = _parse_date(raw_date)
    except ValueError:
        return None
    if parsed_date > _parse_date(trade_date):
        return None
    initial_document_role = _document_role(document_type, url=url, title=title)
    source: dict[str, Any] = {
        "ticker": "",
        "market": "ASX",
        "asx_sector": asx_sector,
        "source_type": source_type,
        "document_type": document_type,
        "document_role": initial_document_role,
        "title": title,
        "announcement_date": parsed_date.strftime("%Y-%m-%d"),
        "lodgement_date": parsed_date.strftime("%Y-%m-%d"),
        "url": url,
        "status": "available",
        "extraction_status": "unavailable" if not url else "pending",
        "source_quality_tier": _source_quality_tier(
            source_type=source_type,
            document_role=initial_document_role,
            url=url,
            fallback_page_url=str(row.get("fallback_page_url") or ""),
            title=title,
        ),
        "metric_eligibility": "not_eligible",
        "excerpt": "",
        "extracted_sections": [],
        "document_structure": {"pages": [], "page_count": 0, "table_count": 0, "text_block_count": 0},
    }
    if ticker_plugin:
        source["ticker_plugin"] = str(ticker_plugin.get("ticker") or "unavailable")
    if row.get("fallback_page_url"):
        source["fallback_page_url"] = str(row["fallback_page_url"])
    if not url:
        source["extraction_status"] = "unavailable"
        source["metric_eligibility"] = _metric_eligibility(
            str(source["source_quality_tier"]),
            str(source["document_role"]),
            str(source["extraction_status"]),
        )
        source["reason"] = "Announcement had no document URL."
        return source
    try:
        raw_document = http_get(url, headers)
        expanded_document, structured_child_urls = _expand_structured_online_annual_report(
            raw_document,
            url,
            title,
            http_get,
            headers,
            ticker_plugin,
        )
        structured_document = _document_text_for_structure(expanded_document, url, title)
        text = _excerpt(structured_document, excerpt_chars)
        source["extraction_status"] = "available" if text else "unavailable"
        source["document_role"] = _document_role(document_type, raw_document=raw_document, url=url, title=title)
        source["source_quality_tier"] = _source_quality_tier(
            source_type=source_type,
            document_role=str(source["document_role"]),
            url=url,
            fallback_page_url=str(row.get("fallback_page_url") or ""),
            raw_document=raw_document,
            title=title,
        )
        source["metric_eligibility"] = _metric_eligibility(
            str(source["source_quality_tier"]),
            str(source["document_role"]),
            str(source["extraction_status"]),
        )
        source["document_structure"] = _build_document_structure(structured_document)
        if structured_child_urls:
            source["structured_online_child_urls"] = structured_child_urls
        source["excerpt"] = text
        if _is_html_like_document(raw_document) and source["metric_eligibility"] == "discovery_only":
            source["discovered_child_rows"] = [
                child_row
                for child_row in _fallback_rows(
                    raw_document,
                    url,
                    inherited_title=title,
                    inherited_date=str(source["announcement_date"]),
                    ticker_plugin=ticker_plugin,
                )
                if child_row.get("url") and child_row.get("url") != url
            ]
        source["extracted_sections"] = _extract_sections(
            structured_document,
            source,
            excerpt_chars,
            asx_sector,
            include_sector_metrics=False,
            ticker_plugin=ticker_plugin,
        )
        source["table_extraction_diagnostics"] = _table_extraction_diagnostics(
            structured_document,
            source["extracted_sections"],
        )
    except Exception as exc:  # noqa: BLE001 - keep discovered announcement with extraction failure.
        source["extraction_status"] = "error"
        source["metric_eligibility"] = _metric_eligibility(
            str(source["source_quality_tier"]),
            str(source["document_role"]),
            str(source["extraction_status"]),
        )
        source["reason"] = str(exc)
    return source


def _collect_fallback_sources(
    *,
    symbol: str,
    asx_code: str,
    trade_date: str,
    identity: dict[str, Any] | None,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
    ticker_plugin: dict[str, Any] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sources: list[dict[str, Any]] = []
    fallback_attempts: list[dict[str, Any]] = []
    asx_sector = _sector_for_asx_code(asx_code)
    seen_source_urls: set[str] = set()
    for page_url in _fallback_page_urls(asx_code, identity, ticker_plugin):
        try:
            page_html = http_get(page_url, headers)
            discovered_rows = _fallback_rows(page_html, page_url, ticker_plugin=ticker_plugin)
            self_row = _fallback_page_self_row(page_html, page_url)
            if self_row:
                discovered_rows.append(self_row)
            rows = _prefilter_fallback_rows(discovered_rows, ticker_plugin)
            fallback_attempts.append(
                {
                    "source_type": "asx_fallback_page",
                    "status": "available",
                    "url": page_url,
                    "documents_found": len(rows),
                }
            )
        except Exception as exc:  # noqa: BLE001 - record fallback access failures.
            fallback_attempts.append(
                {
                    "source_type": "asx_fallback_page",
                    "status": "error",
                    "url": page_url,
                    "reason": str(exc),
                }
            )
            continue
        for row in rows:
            row_url = str(row.get("url") or "")
            if row_url and row_url in seen_source_urls:
                continue
            if row_url:
                seen_source_urls.add(row_url)
            source = _source_from_row(
                row,
                trade_date=trade_date,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
                source_type="asx_fallback_document",
                asx_sector=asx_sector,
                ticker_plugin=ticker_plugin,
            )
            if source:
                child_rows = _prefilter_fallback_rows(source.pop("discovered_child_rows", []), ticker_plugin)
                source["ticker"] = symbol
                sources.append(source)
                for child_row in child_rows:
                    child_url = str(child_row.get("url") or "")
                    if child_url and child_url in seen_source_urls:
                        continue
                    if child_url:
                        seen_source_urls.add(child_url)
                    child_source = _source_from_row(
                        child_row,
                        trade_date=trade_date,
                        http_get=http_get,
                        headers=headers,
                        excerpt_chars=excerpt_chars,
                        source_type="asx_fallback_document",
                        asx_sector=asx_sector,
                        ticker_plugin=ticker_plugin,
                    )
                    if child_source:
                        child_source.pop("discovered_child_rows", None)
                        child_source["ticker"] = symbol
                        sources.append(child_source)
    return sources, fallback_attempts


def _has_available_section(sources: list[dict[str, Any]], claim: str) -> bool:
    claim = claim.lower()
    for source in sources:
        for section in source.get("extracted_sections", []):
            supports = " ".join(str(item) for item in section.get("supports_claims", []))
            haystack = f"{section.get('section_name', '')} {supports}".lower()
            if section.get("status") == "available" and claim in haystack:
                return True
    return False


def _needs_section_supplement(sources: list[dict[str, Any]]) -> bool:
    available_sources = [source for source in sources if source.get("status") == "available"]
    if not available_sources:
        return True
    return not (
        _has_available_section(available_sources, "management discussion")
        and _has_available_section(available_sources, "cash flow statement")
    )


def _merge_unique_sources(primary: list[dict[str, Any]], supplemental: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen_urls = {str(source.get("url", "")) for source in primary if source.get("url")}
    merged = [*primary]
    for source in supplemental:
        url = str(source.get("url", ""))
        if url and url in seen_urls:
            continue
        if url:
            seen_urls.add(url)
        merged.append(source)
    return merged


def _source_selection_summaries(sources: list[dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "title": str(source.get("title") or ""),
            "url": str(source.get("url") or ""),
            "source_type": str(source.get("source_type") or ""),
            "source_quality_tier": str(source.get("source_quality_tier") or ""),
            "document_role": str(source.get("document_role") or ""),
            "extraction_status": str(source.get("extraction_status") or ""),
            "metric_eligibility": str(source.get("metric_eligibility") or ""),
            "ticker_plugin": str(source.get("ticker_plugin") or "unavailable"),
        }
        for source in sources
    ]


def collect_asx_financial_document_sources(
    ticker: str,
    trade_date: str,
    *,
    identity: dict[str, Any] | None = None,
    http_get: HttpGet = _default_http_get,
    excerpt_chars: int = 6000,
) -> dict[str, Any]:
    symbol = ticker.upper().strip()
    asx_code = normalize_asx_code(symbol)
    asx_sector = _sector_for_asx_code(asx_code)
    ticker_plugin = _load_ticker_plugin(symbol)
    if not is_asx_ticker(symbol, identity):
        return {
            "ticker": symbol,
            "market": "ASX",
            "asx_sector": asx_sector,
            "trade_date": trade_date,
            "status": "unavailable",
            "sources": [
                {
                    "source_type": "asx_announcements",
                    "status": "unavailable",
                    "reason": "Ticker was not identified as ASX; ASX collector skipped.",
                }
            ],
        }
    headers = _headers()
    endpoint_error = ""
    fallback_attempts: list[dict[str, Any]] = []
    rows: list[dict[str, Any]] = []
    endpoint_attempts: list[dict[str, Any]] = []
    for endpoint_url in _announcement_endpoint_urls(asx_code):
        try:
            endpoint_rows = _announcement_rows(http_get(endpoint_url, headers))
            endpoint_attempts.append(
                {
                    "source_type": "asx_announcements_endpoint",
                    "status": "available",
                    "url": endpoint_url,
                    "announcements_found": len(endpoint_rows),
                }
            )
            rows = endpoint_rows
            break
        except Exception as exc:  # noqa: BLE001 - try the next official endpoint before falling back.
            endpoint_error = str(exc)
            endpoint_attempts.append(
                {
                    "source_type": "asx_announcements_endpoint",
                    "status": "error",
                    "url": endpoint_url,
                    "reason": endpoint_error,
                }
            )
    if rows:
        sources = [
            source
            for row in rows
            if (
                source := _source_from_row(
                    row,
                    trade_date=trade_date,
                    http_get=http_get,
                    headers=headers,
                    excerpt_chars=excerpt_chars,
                    asx_sector=asx_sector,
                    ticker_plugin=ticker_plugin,
                )
            )
        ]
        if not sources:
            sources = [
                {
                    "ticker": symbol,
                    "market": "ASX",
                    "source_type": "asx_announcements",
                    "status": "unavailable",
                    "reason": "No ASX financial report announcement was discovered on or before the trade date.",
                }
            ]
            fallback_sources, fallback_attempts = _collect_fallback_sources(
                symbol=symbol,
                asx_code=asx_code,
                trade_date=trade_date,
                identity=identity,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
                ticker_plugin=ticker_plugin,
            )
            if fallback_sources:
                sources = fallback_sources
        elif _needs_section_supplement(sources):
            fallback_sources, fallback_attempts = _collect_fallback_sources(
                symbol=symbol,
                asx_code=asx_code,
                trade_date=trade_date,
                identity=identity,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
                ticker_plugin=ticker_plugin,
            )
            if fallback_sources:
                sources = _merge_unique_sources(sources, fallback_sources)
        for source in sources:
            source["ticker"] = symbol
        metric_extraction_status, authoritative_sources = _apply_authoritative_sector_metric_extraction(
            sources,
            sector=asx_sector,
            excerpt_chars=excerpt_chars,
            ticker_plugin=ticker_plugin,
        )
        return {
            "ticker": symbol,
            "market": "ASX",
            "asx_code": asx_code,
            "asx_sector": asx_sector,
            "trade_date": trade_date,
            "status": "ok" if any(source.get("status") == "available" for source in sources) else "unavailable",
            "as_of_rule": "Only ASX announcements with announcement/lodgement date <= trade_date are included.",
            "metric_extraction_status": metric_extraction_status,
            "ticker_plugin": ticker_plugin.get("ticker", "unavailable") if ticker_plugin else "unavailable",
            "authoritative_financial_sources": _source_selection_summaries(authoritative_sources),
            "endpoint_attempts": endpoint_attempts,
            "fallback_attempts": fallback_attempts,
            "sources": sources,
        }
    fallback_sources, fallback_attempts = _collect_fallback_sources(
        symbol=symbol,
        asx_code=asx_code,
        trade_date=trade_date,
        identity=identity,
        http_get=http_get,
        headers=headers,
        excerpt_chars=excerpt_chars,
        ticker_plugin=ticker_plugin,
    )
    if fallback_sources:
        metric_extraction_status, authoritative_sources = _apply_authoritative_sector_metric_extraction(
            fallback_sources,
            sector=asx_sector,
            excerpt_chars=excerpt_chars,
            ticker_plugin=ticker_plugin,
        )
        return {
            "ticker": symbol,
            "market": "ASX",
            "asx_code": asx_code,
            "asx_sector": asx_sector,
            "trade_date": trade_date,
            "status": "ok",
            "as_of_rule": "ASX endpoint failed; fallback official ASX/company IR documents still require date <= trade_date.",
            "primary_endpoint_error": endpoint_error,
            "metric_extraction_status": metric_extraction_status,
            "ticker_plugin": ticker_plugin.get("ticker", "unavailable") if ticker_plugin else "unavailable",
            "authoritative_financial_sources": _source_selection_summaries(authoritative_sources),
            "endpoint_attempts": endpoint_attempts,
            "fallback_attempts": fallback_attempts,
            "sources": fallback_sources,
        }
    return {
        "ticker": symbol,
        "market": "ASX",
        "asx_code": asx_code,
        "asx_sector": asx_sector,
        "trade_date": trade_date,
        "status": "error",
        "endpoint_attempts": endpoint_attempts,
        "fallback_attempts": fallback_attempts,
        "sources": [
            {
                "source_type": "asx_announcements",
                "status": "error",
                "reason": endpoint_error,
            }
        ],
    }
