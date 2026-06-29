from __future__ import annotations

import html
import json
import re
import urllib.request
from collections.abc import Callable
from datetime import datetime
from typing import Any
from urllib.parse import urljoin

ASX_ANNOUNCEMENTS_URL = "https://www.asx.com.au/asx/1/company/{code}/announcements?count=100"
ASX_COMPANY_PAGE_URL = "https://www.asx.com.au/markets/company/{code}"
DEFAULT_ASX_USER_AGENT = "CodexTradingAgents/0.1 ASX document research"

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
    ("Results Presentation", r"\bresults presentation\b"),
    ("Investor Presentation", r"\binvestor presentation\b"),
    ("AGM Presentation", r"\bagm presentation\b|annual general meeting presentation"),
    ("Sustainability Report", r"\bsustainability report\b"),
]

SECTION_PATTERNS: list[tuple[str, str, list[str]]] = [
    ("revenue_income_npat", r"\b(revenue|income|npat|profit after tax)\b", ["revenue", "income", "NPAT"]),
    ("eps_dps", r"\b(eps|earnings per share|dps|dividend per share)\b", ["EPS", "DPS", "dividends"]),
    ("operating_cash_flow", r"\boperating cash flow\b", ["operating cash flow"]),
    ("free_cash_flow_or_cash_movement", r"\bfree cash flow\b|cash movement|net cash", ["free cash flow", "cash movement"]),
    ("cash_debt_gearing", r"\b(cash|debt|gearing|cet1|capital ratio)\b", ["cash", "debt", "gearing", "capital"]),
    ("segment_product_performance", r"\b(segment|production|realised price|nim|loan growth|arr|premium)\b", ["segment performance", "sector metrics"]),
    ("management_commentary_outlook", r"\b(outlook|guidance|commentary|expects?|forecast)\b", ["outlook", "management commentary"]),
    ("dividends_capital_management", r"\b(dividend|buy-back|buyback|capital management)\b", ["dividends", "capital management"]),
    ("capex_commitments", r"\b(capex|capital expenditure|commitments?)\b", ["capex", "commitments"]),
    ("material_risks", r"\b(risk|uncertain|impairment|arrears|claims ratio)\b", ["risks"]),
    ("one_off_items", r"\b(one-off|significant item|non-recurring|impairment)\b", ["one-off items"]),
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
        return response.read().decode("utf-8", errors="replace")


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
    return []


def _field(row: dict[str, Any], *names: str) -> str:
    for name in names:
        value = row.get(name)
        if value not in (None, ""):
            return str(value)
    return ""


def _document_url(row: dict[str, Any]) -> str:
    return _field(row, "url", "document_url", "pdf_url", "file_url", "documentReleaseUrl", "downloadUrl")


def _date_from_text(text: str) -> str:
    iso = re.search(r"\b\d{4}-\d{2}-\d{2}\b", text)
    if iso:
        return iso.group(0)
    dated = re.search(r"\b\d{1,2}\s+[A-Z][a-z]{2,8}\s+\d{4}\b", text)
    if dated:
        return dated.group(0)
    return ""


def _title_without_date(text: str) -> str:
    date_text = _date_from_text(text)
    if date_text:
        text = text.replace(date_text, " ")
    return re.sub(r"\s+", " ", text).strip()


def _fallback_rows(page_html: str, page_url: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for href, label in re.findall(r"(?is)<a[^>]+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", page_html):
        clean_label = _clean_text(label)
        if not _classify_document(clean_label):
            continue
        date_text = _date_from_text(clean_label)
        if not date_text:
            continue
        rows.append(
            {
                "title": _title_without_date(clean_label),
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
    return list(dict.fromkeys(urls))


def _extract_sections(text: str, source: dict[str, Any], excerpt_chars: int) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    clean = _clean_text(text)
    for section_name, pattern, supports_claims in SECTION_PATTERNS:
        match = re.search(pattern, clean, re.IGNORECASE)
        if not match:
            sections.append(
                {
                    "section_name": section_name,
                    "status": "unavailable",
                    "source_type": source["source_type"],
                    "filing_date": source["announcement_date"],
                    "url": source.get("url", ""),
                    "excerpt": "",
                    "supports_claims": supports_claims,
                    "unavailable_reason": f"{section_name} was not identified in extracted ASX document text.",
                }
            )
            continue
        excerpt = clean[match.start() : match.start() + excerpt_chars]
        sections.append(
            {
                "section_name": section_name,
                "status": "available",
                "source_type": source["source_type"],
                "filing_date": source["announcement_date"],
                "url": source.get("url", ""),
                "excerpt": excerpt.rsplit(" ", 1)[0].strip(),
                "supports_claims": supports_claims,
                "unavailable_reason": "",
            }
        )
    return sections


def _source_from_row(
    row: dict[str, Any],
    *,
    trade_date: str,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
    source_type: str = "asx_announcement",
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
        source["extracted_sections"] = _extract_sections(raw_document, source, excerpt_chars)
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
            )
            if source:
                source["ticker"] = symbol
                sources.append(source)
    return sources, fallback_attempts


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
    if not is_asx_ticker(symbol, identity):
        return {
            "ticker": symbol,
            "market": "ASX",
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
    try:
        rows = _announcement_rows(http_get(ASX_ANNOUNCEMENTS_URL.format(code=asx_code), headers))
        sources = [
            source
            for row in rows
            if (source := _source_from_row(row, trade_date=trade_date, http_get=http_get, headers=headers, excerpt_chars=excerpt_chars))
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
        for source in sources:
            source["ticker"] = symbol
        return {
            "ticker": symbol,
            "market": "ASX",
            "asx_code": asx_code,
            "trade_date": trade_date,
            "status": "ok" if any(source.get("status") == "available" for source in sources) else "unavailable",
            "as_of_rule": "Only ASX announcements with announcement/lodgement date <= trade_date are included.",
            "fallback_attempts": fallback_attempts,
            "sources": sources,
        }
    except Exception as exc:  # noqa: BLE001 - ASX access should degrade gracefully.
        endpoint_error = str(exc)
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
            "trade_date": trade_date,
            "status": "ok",
            "as_of_rule": "ASX endpoint failed; fallback official ASX/company IR documents still require date <= trade_date.",
            "primary_endpoint_error": endpoint_error,
            "fallback_attempts": fallback_attempts,
            "sources": fallback_sources,
        }
    return {
        "ticker": symbol,
        "market": "ASX",
        "asx_code": asx_code,
        "trade_date": trade_date,
        "status": "error",
        "fallback_attempts": fallback_attempts,
        "sources": [
            {
                "source_type": "asx_announcements",
                "status": "error",
                "reason": endpoint_error,
            }
        ],
    }
