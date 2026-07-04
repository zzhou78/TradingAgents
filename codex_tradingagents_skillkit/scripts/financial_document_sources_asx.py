from __future__ import annotations

import html
import io
import json
import re
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
    ],
    "retailers": [
        ("sales_growth", "Sales growth", r"sales growth|comparable sales|same[- ]store sales|total sales", ["sales growth"]),
        ("ebit_margin", "EBIT margin", r"EBIT margin|operating margin", ["EBIT margin"]),
        ("inventory", "Inventory", r"inventor(?:y|ies)|stock loss|shrink", ["inventory"]),
        ("capex", "Capex", r"capex|capital expenditure", ["capex"]),
        ("dividends", "Dividends", r"dividend|DPS|dividend per share", ["dividends"]),
    ],
}

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
    pdfplumber_text = _extract_pdf_text_with_pdfplumber(body)
    if pdfplumber_text:
        return pdfplumber_text
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


def _extract_pdf_text_with_pdfplumber(body: bytes) -> str:
    try:
        import pdfplumber
    except ImportError:
        return ""
    parts: list[str] = []
    try:
        with pdfplumber.open(io.BytesIO(body)) as pdf:
            for page in pdf.pages:
                try:
                    text = page.extract_text() or ""
                except Exception:
                    text = ""
                if text:
                    parts.append(text)
                try:
                    tables = page.extract_tables() or []
                except Exception:
                    tables = []
                for table in tables:
                    for row in table or []:
                        cells = [str(cell or "").strip() for cell in (row or [])]
                        if any(cells):
                            parts.append(" | ".join(cells))
    except Exception:
        return ""
    return "\n".join(part for part in parts if part).strip()


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
        r"(?:US\$|A\$|\$)?\d+(?:\.\d+)?\s*"
        r"(?:bps|bpts|%|per cent|cents|cps|bn|m|mt|kt|moz|/t)"
    )
    for match in re.finditer(generic_pattern, text, re.IGNORECASE):
        _clean_value, unit = _clean_value_and_unit(match.group(0))
        if _unit_compatible(unit, profile) and all(match.span() != existing.span() for existing in matches):
            matches.append(match)
    return sorted(matches, key=lambda match: match.start())


def _clean_value_and_unit(raw: str) -> tuple[str, str]:
    value_match = re.search(r"(?:US\$|A\$|\$)?(?P<value>\d+(?:\.\d+)?)", raw, re.IGNORECASE)
    clean_value = value_match.group("value") if value_match else "unavailable"
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
                for other_metric in competing:
                    other_profile = _profile_for_metric(other_metric)
                    for other_label in _label_matches(text, other_profile):
                        if abs(value_match.start() - other_label.end()) < own_distance:
                            stronger = True
                if stronger:
                    score -= 35
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
                if (candidate["label_start"], candidate["value_start"]) < (best["label_start"], best["value_start"]):
                    best = candidate
            elif candidate["score"] > best["score"]:
                best = candidate
    return best


def _extract_table_metric_value(text: str, metric_name: str, profile: dict[str, Any]) -> dict[str, Any]:
    if "|" not in text:
        return {}
    for raw_row in re.split(r"\n|(?<=\d[%a-zA-Z])\s+(?=[A-Z][A-Za-z /&-]{2,}\s*\|)", text):
        row = raw_row.strip()
        if "|" not in row:
            continue
        cells = [_clean_text(cell) for cell in row.split("|")]
        if len(cells) < 3:
            continue
        row_label = cells[0]
        if not _label_matches(row_label, profile):
            continue
        for index, cell in enumerate(cells[1:], start=1):
            value_match = next(iter(_value_matches(cell, profile)), None)
            if not value_match:
                continue
            clean_value, unit = _clean_value_and_unit(value_match.group(0))
            column_label = cells[index - 1] if index > 1 else "value"
            comparison_reference = cells[index + 1] if index + 1 < len(cells) else "not specified"
            return {
                "score": 95,
                "clean_metric_value": clean_value,
                "value_unit": unit,
                "value_context": "table row/column label association",
                "supporting_sentence": row,
                "association_reason": "table row label matches accepted metric label and value unit is compatible",
                "direction": _direction_from_profile(row, profile),
                "period_reference": column_label,
                "comparison_reference": comparison_reference,
                "table_title": "unavailable",
                "row_label": row_label,
                "column_label": column_label,
            }
    return {}


def _metric_label_present(text: str, profile: dict[str, Any]) -> bool:
    return bool(_label_matches(text, profile))


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
    }
    if not profile:
        return base
    label_present = _metric_label_present(clean, profile)
    if _is_navigation_or_toc(clean):
        return {
            **base,
            "metric_value_status": "context_only",
            "association_reason": "navigation or table-of-contents context is not metric evidence",
            "supporting_sentence": clean[:240] or base["supporting_sentence"],
            "direction": "context_only",
            "confidence_reason": "downgraded because extracted text is navigation/table-of-contents context",
        }
    if not label_present:
        return base
    best = _extract_table_metric_value(clean, metric_name, profile)
    if not best:
        for sentence in _sentences(clean):
            if not _label_matches(sentence, profile):
                continue
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
    status = "value_extracted" if score >= 80 else ("direction_extracted" if best["direction"] != "neutral" or score >= 50 else "metric_mentioned_only")
    clean_value = best["clean_metric_value"] if status == "value_extracted" else "unavailable"
    confidence = "medium" if status == "value_extracted" else "low"
    return {
        **base,
        "clean_metric_value": clean_value,
        "value_unit": best["value_unit"] if status == "value_extracted" else "unavailable",
        "value_context": best["value_context"] if status == "value_extracted" else "value association below acceptance threshold",
        "metric_value_status": status,
        "association_score": score,
        "association_reason": best["association_reason"],
        "period_reference": best.get("period_reference", "not specified"),
        "comparison_reference": best.get("comparison_reference", "not specified"),
        "supporting_sentence": best["supporting_sentence"][:240],
        "comparison_basis": "period-over-period wording in extracted filing/report phrase"
        if best["direction"] != "neutral"
        else "metric mentioned without explicit comparative baseline",
        "direction": best["direction"],
        "confidence": confidence,
        "confidence_reason": "clean value accepted because metric label, compatible unit, and proximity met threshold"
        if status == "value_extracted"
        else "clean value withheld because association score is below accepted threshold",
        "table_title": best.get("table_title", "unavailable"),
        "row_label": best.get("row_label", "unavailable"),
        "column_label": best.get("column_label", "unavailable"),
        "source_page": "unavailable",
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
        excerpt = clean[match.start() : match.start() + excerpt_chars].rsplit(" ", 1)[0].strip()
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
