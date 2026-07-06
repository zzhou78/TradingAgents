from __future__ import annotations

import html
import io
import json
import re
import sys
import urllib.request
from collections.abc import Callable
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

ASX_MARKIT_API_BASE = "https://asx.api.markitdigital.com/asx-research/1.0"
ASX_MARKIT_ANNOUNCEMENTS_URL = ASX_MARKIT_API_BASE + "/companies/{code}/announcements"
ASX_ANNOUNCEMENTS_URL = "https://www.asx.com.au/asx/1/company/{code}/announcements?count=100"
ASX_COMPANY_PAGE_URL = "https://www.asx.com.au/markets/company/{code}"
DEFAULT_ASX_USER_AGENT = "CodexTradingAgents/0.1 ASX document research"
REPO_ROOT = Path(__file__).resolve().parents[2]
ASX_IR_RULES_PATH = REPO_ROOT / "data" / "rules" / "asx_investor_relations_urls.yaml"
ASX_METRIC_PROFILE_PATH = Path(__file__).resolve().parents[1] / "data" / "rules" / "asx_sector_metric_extraction_profiles.yaml"
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
    "segment_revenue",
    "production",
    "commodity_exposure",
    "reserves_resources",
    "capex",
    "membership",
}
TABLE_ROW_MARKER = "__TABLE_ROW__"
PDFPLUMBER_WORD_TABLE_INDEX = 1001
PDF_WORD_ROW_TOLERANCE = 3.0
PDF_WORD_COLUMN_GAP = 18.0
PDF_TABLE_TITLE_CROP_HEIGHT = 320
PDFPLUMBER_MAX_TABLE_PAGES = 60

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
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            continue
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


def _fallback_rows(page_html: str, page_url: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for anchor in re.finditer(r"(?is)<a\b(?P<attrs>[^>]*)>(?P<label>.*?)</a>", page_html):
        attrs = anchor.group("attrs")
        href_match = re.search(r"href=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        if not href_match:
            continue
        href = href_match.group(1)
        title_match = re.search(r"title=['\"]([^'\"]+)['\"]", attrs, re.IGNORECASE)
        title = _clean_text(title_match.group(1)) if title_match else ""
        clean_label = _clean_text(anchor.group("label"))
        searchable_text = f"{clean_label} {title} {href.replace('-', ' ').replace('_', ' ')} {page_url}"
        if not _classify_document(searchable_text):
            continue
        date_text = _date_from_text(searchable_text)
        if not date_text:
            continue
        rows.append(
            {
                "title": _title_without_date(title) or _title_without_date(clean_label) or _title_without_date(searchable_text),
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
        searchable_text = f"{clean_label} {href.replace('-', ' ').replace('_', ' ')}"
        if not _classify_document(searchable_text):
            continue
        date_text = _date_from_text(searchable_text)
        if not date_text:
            continue
        rows.append(
            {
                "title": _title_without_date(clean_label) or _title_without_date(searchable_text),
                "announcement_date": date_text,
                "url": urljoin(page_url, href),
                "fallback_page_url": page_url,
            }
        )
    return rows


def _fallback_page_urls(asx_code: str, identity: dict[str, Any] | None) -> list[str]:
    urls = [ASX_COMPANY_PAGE_URL.format(code=asx_code)]
    identity = identity or {}
    for key in ("investor_relations_url", "investorRelationsUrl", "ir_url", "investors_url"):
        url = identity.get(key)
        if url:
            urls.append(str(url))
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


def _profile_for_metric(metric_name: str) -> dict[str, Any]:
    for sector_profiles in _load_metric_profiles().values():
        profile = sector_profiles.get(metric_name)
        if profile:
            return profile
    for specs in ASX_SECTOR_METRIC_PATTERNS.values():
        for name, label, pattern, _supports_claims in specs:
            if name == metric_name:
                return {
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
                }
    return {}


def _label_regex(label: str) -> str:
    if label.upper() == label and len(label) <= 5:
        return rf"\b{re.escape(label)}\b"
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
        r"(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)"
    )
    for match in re.finditer(generic_pattern, text, re.IGNORECASE):
        _clean_value, unit = _clean_value_and_unit(match.group(0))
        if _unit_compatible(unit, profile) and all(match.span() != existing.span() for existing in matches):
            matches.append(match)
    return sorted(matches, key=lambda match: match.start())


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
    elif "cents" in lower or "cps" in lower:
        unit = "cents" if "cents" in lower else "cps"
    elif "us$" in lower and "bn" in lower:
        unit = "US$bn"
    elif "us$" in lower and "m" in lower:
        unit = "US$m"
    elif ("a$" in lower or "$" in raw) and "bn" in lower:
        unit = "$bn"
    elif ("a$" in lower or "$" in raw) and "m" in lower:
        unit = "$m"
    elif "us$" in lower or "a$" in lower or "$" in raw:
        unit = "$"
    elif lower.endswith("bn"):
        unit = "bn"
    elif lower.endswith("m"):
        unit = "m"
    elif lower.endswith("mt"):
        unit = "mt"
    elif lower.endswith("kt"):
        unit = "kt"
    elif lower.endswith("moz"):
        unit = "moz"
    else:
        unit = "unit unavailable"
    return clean_value, unit


def _numeric_value_spans(text: str) -> list[re.Match[str]]:
    pattern = r"\(?-?(?:US\$|A\$|\$)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)?"
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
    value_match = re.search(r"\(?-?(?:US\$|A\$|\$)?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\)?\s*(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)?", cell, re.IGNORECASE)
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


def _table_key(metadata: dict[str, str]) -> tuple[str, str]:
    return (metadata.get("source_page", "unavailable"), metadata.get("table_index", "unavailable"))


def _header_continuation_row(cells: list[str]) -> bool:
    if not cells:
        return False
    first_cell = cells[0].strip().lower()
    non_empty = [cell for cell in cells if cell.strip()]
    if first_cell and any(label in first_cell for label in DENSE_TABLE_ROW_LABELS):
        return False
    unit_cells = sum(1 for cell in cells if re.search(r"\b(?:\$m|\$bn|bps|bpts|%|cents|mt|kt|moz|/t)\b|[$%]", cell, re.IGNORECASE))
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


def _row_label_matches(row_label: str, profile: dict[str, Any]) -> bool:
    row_profile = {**profile, "accepted_labels": _profile_row_labels(profile)}
    return bool(_label_matches(row_label, row_profile))


def _column_label_allowed(column_label: str, profile: dict[str, Any]) -> bool:
    lower = column_label.lower()
    normalized = re.sub(r"\bfy(\d{2})\b", lambda match: f"fy20{match.group(1)} 20{match.group(1)}", lower)
    rejected = [str(label).lower() for label in profile.get("rejected_column_labels", []) or []]
    if any(label and (label in lower or label in normalized) for label in rejected):
        return False
    accepted = [str(label).lower() for label in profile.get("accepted_column_labels", []) or []]
    return not accepted or any(label and (label in lower or label in normalized) for label in accepted)


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


def _unit_compatible(unit: str, profile: dict[str, Any]) -> bool:
    accepted = {str(item).lower() for item in profile.get("accepted_units", []) or []}
    if not accepted:
        return True
    normalized = unit.lower()
    if normalized in accepted:
        return True
    if normalized == "per cent" and "%" in accepted:
        return True
    return normalized in {"$m", "$bn"} and any(item in accepted for item in {normalized, f"a{normalized}", normalized[1:]})


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
    rejected_terms = [str(term).lower() for term in profile.get("rejected_nearby_terms", []) or []]
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
            window_start = max(0, min(label_match.start(), value_match.start()) - 80)
            window_end = min(len(text), max(label_match.end(), value_match.end()) + 80)
            window = text[window_start:window_end]
            lower_window = window.lower()
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
                own_distance = abs(value_match.start() - label_match.end())
                own_label_is_close_after_value = label_match.start() >= value_match.end() and token_distance <= 3
                for other_metric in competing:
                    if metric_name == "production" and other_metric == "commodity_exposure":
                        continue
                    other_profile = _profile_for_metric(other_metric)
                    for other_label in _label_matches(text, other_profile):
                        if own_label_is_close_after_value and other_label.end() <= value_match.start():
                            continue
                        if abs(value_match.start() - other_label.end()) < own_distance:
                            stronger = True
                if stronger:
                    score -= 35
            if token_distance <= 2:
                rejected_hits = [term for term in rejected_terms if term in lower_between]
            else:
                rejected_hits = [term for term in rejected_terms if term in lower_window]
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
                if (candidate["label_start"], candidate["value_start"]) < (best["label_start"], best["value_start"]):
                    best = candidate
            elif candidate["score"] > best["score"]:
                best = candidate
    return best


def _extract_table_metric_value(text: str, metric_name: str, profile: dict[str, Any]) -> dict[str, Any]:
    if "|" not in text:
        return {}
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
        if not _row_label_matches(cells[0], profile):
            if key in headers_by_table and _header_continuation_row(cells):
                headers_by_table[key] = _merge_table_header_rows(headers_by_table[key], cells)
            else:
                headers_by_table[key] = cells
            continue
        row_label = cells[0]
        header_cells = headers_by_table.get(key, [])
        values: list[dict[str, str]] = []
        for index, cell in enumerate(cells[1:], start=1):
            column_label = header_cells[index] if header_cells and index < len(header_cells) else cells[index - 1]
            inferred_unit = _unit_from_column_label(column_label)
            parsed = _numeric_cell_value(cell, inferred_unit)
            if not parsed:
                continue
            clean_value, unit = parsed
            if unit != "unit unavailable" and not _unit_compatible(unit, profile):
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
            "value_unit": unit,
            "value_context": "table row/column label association",
            "supporting_sentence": row,
            "association_reason": "table row label matches accepted metric label and value is taken from parsed row/column structure",
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


def _extract_metric_value_from_text(text: str, metric_name: str) -> dict[str, Any]:
    profile = _profile_for_metric(metric_name)
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
    label_present = _metric_label_present(clean, profile)
    if not label_present:
        return base
    navigation_context = _is_navigation_or_toc(clean)
    metric_context = _best_metric_context(clean, profile)
    metric_context_is_navigation = _is_navigation_or_toc(metric_context)
    best = _extract_table_metric_value(text, metric_name, profile)
    if not best:
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
    if not best and _dense_table_row_signal(metric_context):
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
    if unit_missing_for_profile:
        status = "direction_extracted" if best["direction"] != "neutral" else "metric_mentioned_only"
    clean_value = best["clean_metric_value"] if status == "value_extracted" else "unavailable"
    confidence = "medium" if status == "value_extracted" else "low"
    confidence_reason = (
        "clean value accepted because metric label, compatible unit, and proximity met threshold"
        if status == "value_extracted"
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
    return {
        **base,
        "clean_metric_value": clean_value,
        "value_unit": best["value_unit"] if status == "value_extracted" else "unavailable",
        "value_context": best["value_context"] if status == "value_extracted" else "value association below acceptance threshold",
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
        "cell_value": best.get("cell_value", "unavailable") if status == "value_extracted" else "unavailable",
        "table_mapping_confidence": best.get("table_mapping_confidence", 0),
        "table_mapping_reason": best.get("table_mapping_reason", "no structured table mapping available"),
        "raw_row_text": best.get("raw_row_text", "unavailable"),
        "current_period_value": best.get("current_period_value", "unavailable"),
        "prior_period_value": best.get("prior_period_value", "unavailable"),
        "variance_value": best.get("variance_value", "unavailable"),
        "variance_percent": best.get("variance_percent", "unavailable"),
    }


def _extract_sector_metrics(
    text: str,
    source: dict[str, Any],
    excerpt_chars: int,
    sector: str,
) -> list[dict[str, Any]]:
    profile_specs = _metric_profiles_for_sector(sector)
    legacy_specs = ASX_SECTOR_METRIC_PATTERNS.get(sector, [])
    specs = [
        (
            metric_name,
            str(profile.get("accepted_labels", [metric_name])[0]),
            "|".join(_label_regex(str(label)) for label in profile.get("accepted_labels", []) or [metric_name]),
            ASX_SECTOR_METRIC_PATTERNS.get(sector, []),
        )
        for metric_name, profile in profile_specs.items()
    ]
    if not specs:
        specs = legacy_specs
    if not specs:
        return []
    clean = _clean_text(text)
    metrics: list[dict[str, Any]] = []
    legacy_supports = {name: supports_claims for name, _label, _pattern, supports_claims in legacy_specs}
    for metric_name, metric_label, pattern, supports_claims_or_legacy in specs:
        supports_claims = legacy_supports.get(metric_name, supports_claims_or_legacy if isinstance(supports_claims_or_legacy, list) else [metric_label])
        section_name = f"sector_metric_{metric_name}"
        match = re.search(pattern, clean, re.IGNORECASE)
        if not match:
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
                }
            )
            continue
        excerpt_start = max(0, match.start() - min(300, excerpt_chars // 4))
        excerpt = clean[excerpt_start : match.start() + excerpt_chars].rsplit(" ", 1)[0].strip()
        association = _extract_metric_value_from_text(excerpt, metric_name)
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
            }
        )
    return metrics


def _extract_sections(text: str, source: dict[str, Any], excerpt_chars: int, sector: str = "general") -> list[dict[str, Any]]:
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
    sections.extend(_extract_sector_metrics(text, source, excerpt_chars, sector))
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


def _source_from_row(
    row: dict[str, Any],
    *,
    trade_date: str,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
    source_type: str = "asx_announcement",
    asx_sector: str = "general",
) -> dict[str, Any] | None:
    title = _field(row, "title", "header", "headline", "description")
    document_type = _classify_document(title)
    if not document_type:
        return None
    raw_date = _field(row, "announcement_date", "lodgement_date", "date", "releaseDate", "lodgementDate")
    try:
        parsed_date = _parse_date(raw_date)
    except ValueError:
        return None
    if parsed_date > _parse_date(trade_date):
        return None
    url = _document_url(row)
    source: dict[str, Any] = {
        "ticker": "",
        "market": "ASX",
        "asx_sector": asx_sector,
        "source_type": source_type,
        "document_type": document_type,
        "title": title,
        "announcement_date": parsed_date.strftime("%Y-%m-%d"),
        "lodgement_date": parsed_date.strftime("%Y-%m-%d"),
        "url": url,
        "status": "available",
        "extraction_status": "unavailable" if not url else "pending",
        "excerpt": "",
        "extracted_sections": [],
    }
    if row.get("fallback_page_url"):
        source["fallback_page_url"] = str(row["fallback_page_url"])
    if not url:
        source["extraction_status"] = "unavailable"
        source["reason"] = "Announcement had no document URL."
        return source
    try:
        raw_document = http_get(url, headers)
        text = _excerpt(raw_document, excerpt_chars)
        source["extraction_status"] = "available" if text else "unavailable"
        source["excerpt"] = text
        source["extracted_sections"] = _extract_sections(raw_document, source, excerpt_chars, asx_sector)
        source["table_extraction_diagnostics"] = _table_extraction_diagnostics(
            raw_document,
            source["extracted_sections"],
        )
    except Exception as exc:  # noqa: BLE001 - keep discovered announcement with extraction failure.
        source["extraction_status"] = "error"
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
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sources: list[dict[str, Any]] = []
    fallback_attempts: list[dict[str, Any]] = []
    asx_sector = _sector_for_asx_code(asx_code)
    for page_url in _fallback_page_urls(asx_code, identity):
        try:
            rows = _fallback_rows(http_get(page_url, headers), page_url)
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
            source = _source_from_row(
                row,
                trade_date=trade_date,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
                source_type="asx_fallback_document",
                asx_sector=asx_sector,
            )
            if source:
                source["ticker"] = symbol
                sources.append(source)
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
            )
            if fallback_sources:
                sources = _merge_unique_sources(sources, fallback_sources)
        for source in sources:
            source["ticker"] = symbol
        return {
            "ticker": symbol,
            "market": "ASX",
            "asx_code": asx_code,
            "asx_sector": asx_sector,
            "trade_date": trade_date,
            "status": "ok" if any(source.get("status") == "available" for source in sources) else "unavailable",
            "as_of_rule": "Only ASX announcements with announcement/lodgement date <= trade_date are included.",
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
    )
    if fallback_sources:
        return {
            "ticker": symbol,
            "market": "ASX",
            "asx_code": asx_code,
            "asx_sector": asx_sector,
            "trade_date": trade_date,
            "status": "ok",
            "as_of_rule": "ASX endpoint failed; fallback official ASX/company IR documents still require date <= trade_date.",
            "primary_endpoint_error": endpoint_error,
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
