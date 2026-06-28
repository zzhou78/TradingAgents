from __future__ import annotations

import html
import json
import os
import re
import urllib.request
from collections.abc import Callable
from datetime import datetime
from typing import Any

SEC_COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
SEC_ARCHIVES_URL = "https://www.sec.gov/Archives/edgar/data/{cik_int}/{accession}/{document}"
SEC_INDEX_URL = "https://www.sec.gov/Archives/edgar/data/{cik_int}/{accession}/{accession_dashed}-index.html"
DEFAULT_SEC_USER_AGENT = (
    "CodexTradingAgents/0.1 research@example.com "
    "(set SEC_USER_AGENT with project contact for production use)"
)

HttpGet = Callable[[str, dict[str, str]], str]


def _sec_headers() -> dict[str, str]:
    return {
        "User-Agent": os.environ.get("SEC_USER_AGENT", DEFAULT_SEC_USER_AGENT),
        "Accept": "application/json,text/html;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
    }


def _default_http_get(url: str, headers: dict[str, str]) -> str:
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:  # noqa: S310 - fixed SEC URLs.
        return response.read().decode("utf-8", errors="replace")


def _is_plain_us_ticker(ticker: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{1,5}", ticker.upper()))


def _parse_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


def _clean_excerpt(raw: str, limit: int) -> str:
    text = _clean_text(raw)
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].strip()


def _clean_text(raw: str) -> str:
    text = re.sub(r"(?is)<ix:header.*?</ix:header>", " ", raw)
    text = re.sub(
        r"(?is)<[^>]+style=[\"'][^\"']*display\s*:\s*none[^\"']*[\"'][^>]*>.*?</[^>]+>",
        " ",
        text,
    )
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _company_ticker_map(payload: str) -> dict[str, dict[str, Any]]:
    data = json.loads(payload)
    records = data.values() if isinstance(data, dict) else data
    by_ticker: dict[str, dict[str, Any]] = {}
    for record in records:
        ticker = str(record.get("ticker", "")).upper()
        if ticker:
            by_ticker[ticker] = record
    return by_ticker


def _recent_filings(submissions: dict[str, Any], trade_date: str) -> list[dict[str, str]]:
    recent = submissions.get("filings", {}).get("recent", {})
    keys = ["accessionNumber", "filingDate", "form", "primaryDocument", "primaryDocDescription"]
    rows: list[dict[str, str]] = []
    forms = recent.get("form", [])
    cutoff = _parse_date(trade_date)
    for index, _form in enumerate(forms):
        row = {}
        for key in keys:
            values = recent.get(key, [])
            row[key] = str(values[index]) if index < len(values) else ""
        if not row["filingDate"]:
            continue
        try:
            filed = _parse_date(row["filingDate"])
        except ValueError:
            continue
        if filed <= cutoff:
            rows.append(row)
    rows.sort(key=lambda item: item["filingDate"], reverse=True)
    return rows


def _filing_url(cik: str, accession_number: str, primary_document: str) -> str:
    accession = accession_number.replace("-", "")
    return SEC_ARCHIVES_URL.format(
        cik_int=str(int(cik)),
        accession=accession,
        document=primary_document,
    )


def _filing_index_url(cik: str, accession_number: str) -> str:
    return SEC_INDEX_URL.format(
        cik_int=str(int(cik)),
        accession=accession_number.replace("-", ""),
        accession_dashed=accession_number,
    )


def _section_between(text: str, start_pattern: str, end_pattern: str | None, limit: int) -> str | None:
    start = re.search(start_pattern, text, re.IGNORECASE)
    if not start:
        return None
    rest = text[start.start() :]
    if end_pattern:
        end = re.search(end_pattern, rest[start.end() - start.start() :], re.IGNORECASE)
        if end:
            rest = rest[: start.end() - start.start() + end.start()]
    return rest[:limit].rsplit(" ", 1)[0].strip()


def _heading_section(text: str, heading_pattern: str, limit: int) -> str | None:
    return _section_between(
        text,
        heading_pattern,
        r"Item\s+\d+[A-Z]?\.|Risk Factors|Liquidity and Capital Resources|"
        r"Commitments and Contractual Obligations|Capital Expenditures|Segment Information",
        limit,
    )


def _section_record(
    *,
    section_type: str,
    section_name: str,
    source_type: str,
    filing_date: str,
    url: str,
    excerpt: str | None,
    supports_claims: list[str],
) -> dict[str, Any]:
    status = "available" if excerpt else "unavailable"
    return {
        "section_type": section_type,
        "section_name": section_name,
        "source_section": section_name,
        "status": status,
        "source_type": source_type,
        "filing_date": filing_date,
        "url": url,
        "excerpt": excerpt or "",
        "supports_claims": supports_claims,
        "unavailable_reason": "" if excerpt else f"{section_name} was not identified in the extracted filing text.",
    }


def _extract_filing_sections(
    *,
    form: str,
    raw: str,
    limit: int,
    source_type: str,
    filing_date: str,
    url: str,
) -> list[dict[str, Any]]:
    text = _clean_text(raw)
    prefix = "10-K" if form == "10-K" else "10-Q"
    sections: list[dict[str, Any]] = []
    if form == "10-K":
        business = _section_between(
            text,
            r"Item\s+1\.\s+Business\b",
            r"Item\s+1A\.\s+Risk Factors\b",
            limit,
        )
        risk = _section_between(
            text,
            r"Item\s+1A\.\s+Risk Factors\b",
            r"Item\s+1B\.|Item\s+2\.",
            limit,
        )
        mda = _section_between(
            text,
            r"Item\s+7\.\s+Management'?s Discussion and Analysis",
            r"Item\s+7A\.",
            limit,
        )
    else:
        business = None
        mda = _section_between(
            text,
            r"Item\s+2\.\s+Management'?s Discussion and Analysis",
            r"Item\s+3\.",
            limit,
        )
        risk = _section_between(
            text,
            r"Item\s+1A\.\s+Risk Factors\b",
            r"Item\s+2\.",
            limit,
        )
    common_specs = [
        (
            "business_overview",
            f"{prefix} business overview",
            business,
            ["business model", "revenue drivers", "operating context"],
        ),
        (
            "risk_factors",
            f"{prefix} risk factors",
            risk,
            ["risk factors", "downside risks", "uncertainty"],
        ),
        (
            "mda",
            f"{prefix} MD&A",
            mda,
            ["revenue growth", "margin trend", "management discussion"],
        ),
        (
            "segment_information",
            f"{prefix} segment information",
            _heading_section(text, r"Segment Information\b", limit),
            ["segment mix", "business-line performance"],
        ),
        (
            "segment_product_revenue_tables",
            f"{prefix} segment/product revenue tables",
            _heading_section(
                text,
                r"SEGMENT RESULTS OF OPERATIONS\b|"
                r"Segment revenue, cost of revenue, operating expenses, and operating income were as follows\b|"
                r"net sales by reportable segment\b|Product(?:s)? and Services Performance\b|"
                r"Net Sales by (?:Category|Reportable Segment)\b|Revenue by (?:Product|Geography)\b|"
                r"Product Revenue\b|Segment Revenue\b",
                limit,
            ),
            ["segment revenue", "product revenue", "geographic revenue"],
        ),
        (
            "liquidity_and_capital_resources",
            f"{prefix} liquidity and capital resources",
            _heading_section(text, r"Liquidity and Capital Resources\b", limit),
            ["liquidity", "cash resources", "capital resources"],
        ),
        (
            "commitments_capex_contractual_obligations",
            f"{prefix} commitments / capex / contractual obligations",
            _heading_section(
                text,
                r"Commitments and Contractual Obligations\b|Capital Expenditures\b|Capital Expenditure\b",
                limit,
            ),
            ["capex", "commitments", "contractual obligations"],
        ),
        (
            "income_statement",
            f"{prefix} income statement",
            _heading_section(
                text,
                r"CONSOLIDATED STATEMENTS? OF (?:OPERATIONS|INCOME|EARNINGS)\b|"
                r"CONDENSED CONSOLIDATED STATEMENTS? OF (?:OPERATIONS|INCOME|EARNINGS)\b",
                limit,
            ),
            ["revenue", "net income", "EPS", "margin"],
        ),
        (
            "balance_sheet",
            f"{prefix} balance sheet",
            _heading_section(
                text,
                r"CONSOLIDATED BALANCE SHEETS?\b|CONDENSED CONSOLIDATED BALANCE SHEETS?\b",
                limit,
            ),
            ["assets", "liabilities", "cash", "debt"],
        ),
        (
            "cash_flow_statement",
            f"{prefix} cash flow statement",
            _heading_section(
                text,
                r"CONSOLIDATED STATEMENTS? OF CASH FLOWS\b|"
                r"CONDENSED CONSOLIDATED STATEMENTS? OF CASH FLOWS\b",
                limit,
            ),
            ["operating cash flow", "free cash flow", "investing cash flow"],
        ),
    ]
    for section_type, section_name, excerpt, supports_claims in common_specs:
        sections.append(
            _section_record(
                section_type=section_type,
                section_name=section_name,
                source_type=source_type,
                filing_date=filing_date,
                url=url,
                excerpt=excerpt,
                supports_claims=supports_claims,
            )
        )
    return sections


def _source_from_filing(
    *,
    source_type: str,
    source_name: str,
    cik: str,
    filing: dict[str, str] | None,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
    unavailable_reason: str,
) -> dict[str, Any]:
    if not filing:
        return {
            "source_type": source_type,
            "source_name": source_name,
            "status": "unavailable",
            "reason": unavailable_reason,
        }

    url = _filing_url(cik, filing["accessionNumber"], filing["primaryDocument"])
    source: dict[str, Any] = {
        "source_type": source_type,
        "source_name": source_name,
        "status": "available",
        "form": filing["form"],
        "filing_date": filing["filingDate"],
        "description": filing.get("primaryDocDescription", ""),
        "url": url,
    }
    try:
        raw = http_get(url, headers)
        source["excerpt"] = _clean_excerpt(raw, excerpt_chars)
        if filing["form"] in {"10-K", "10-Q"}:
            source["sections"] = _extract_filing_sections(
                form=filing["form"],
                raw=raw,
                limit=excerpt_chars,
                source_type=source_type,
                filing_date=filing["filingDate"],
                url=url,
            )
    except Exception as exc:  # noqa: BLE001 - source packet should preserve partial coverage.
        source["excerpt_status"] = "unavailable"
        source["excerpt_error"] = str(exc)
    return source


def _first_filing(rows: list[dict[str, str]], form: str) -> dict[str, str] | None:
    return next((row for row in rows if row["form"] == form), None)


def _has_earnings_8k_hint(text: str) -> bool:
    return bool(
        re.search(
            r"item\s+2\.02|results\s+of\s+operations|financial\s+condition|"
            r"earnings|quarterly\s+results|revenue|net\s+income",
            text,
            re.IGNORECASE,
        )
    )


def _earnings_8k_source(
    *,
    rows: list[dict[str, str]],
    cik: str,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
) -> dict[str, Any]:
    for filing in (row for row in rows if row["form"] == "8-K"):
        url = _filing_url(cik, filing["accessionNumber"], filing["primaryDocument"])
        description = filing.get("primaryDocDescription", "")
        try:
            cover_excerpt = _clean_excerpt(http_get(url, headers), excerpt_chars)
        except Exception:
            cover_excerpt = ""
        if not _has_earnings_8k_hint(f"{description} {cover_excerpt}"):
            continue
        exhibit = _extract_exhibit_99_1(
            cik=cik,
            accession_number=filing["accessionNumber"],
            http_get=http_get,
            headers=headers,
            excerpt_chars=excerpt_chars,
            filing_date=filing["filingDate"],
        )
        return {
            "source_type": "earnings_release_8k",
            "source_name": "Latest SEC 8-K earnings-release evidence on or before trade date",
            "status": "available",
            "form": filing["form"],
            "filing_date": filing["filingDate"],
            "description": description,
            "url": url,
            "cover_page": {
                "status": "available" if cover_excerpt else "unavailable",
                "source_type": "earnings_release_8k_cover_page",
                "filing_date": filing["filingDate"],
                "url": url,
                "excerpt": cover_excerpt,
                "supports_claims": ["8-K item routing", "earnings-release exhibit existence"],
            },
            "exhibit_99_1": exhibit,
            "excerpt": exhibit.get("excerpt") or cover_excerpt,
        }
    return {
        "source_type": "earnings_release_8k",
        "source_name": "Latest SEC 8-K earnings-release evidence",
        "status": "unavailable",
        "reason": "No 8-K with earnings/results-of-operations evidence was found on or before the trade date.",
    }


def _absolute_archive_url(href: str, cik: str, accession_number: str) -> str:
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return f"https://www.sec.gov{href}"
    base = SEC_ARCHIVES_URL.format(
        cik_int=str(int(cik)),
        accession=accession_number.replace("-", ""),
        document="",
    )
    return f"{base}{href}"


def _find_exhibit_99_1_url(index_html: str, cik: str, accession_number: str) -> str | None:
    for match in re.finditer(r"href=[\"'](?P<href>[^\"']+)[\"'][^>]*>(?P<label>.*?)</a>", index_html, re.IGNORECASE):
        label = re.sub(r"<[^>]+>", " ", match.group("label"))
        href = match.group("href")
        if re.search(r"EX-?99\.?1|99\.1", f"{label} {href}", re.IGNORECASE):
            return _absolute_archive_url(href, cik, accession_number)
    return None


def _extract_exhibit_99_1(
    *,
    cik: str,
    accession_number: str,
    http_get: HttpGet,
    headers: dict[str, str],
    excerpt_chars: int,
    filing_date: str,
) -> dict[str, Any]:
    try:
        index_html = http_get(_filing_index_url(cik, accession_number), headers)
        exhibit_url = _find_exhibit_99_1_url(index_html, cik, accession_number)
        if not exhibit_url:
            return {
                "status": "unavailable",
                "source_type": "earnings_release_exhibit",
                "exhibit_name": "Exhibit 99.1",
                "filing_date": filing_date,
                "url": "",
                "excerpt": "",
                "supports_claims": ["guidance", "earnings release", "management commentary"],
                "reason": "No Exhibit 99.1 link found in filing index.",
            }
        return {
            "status": "available",
            "source_type": "earnings_release_exhibit",
            "exhibit_name": "Exhibit 99.1",
            "filing_date": filing_date,
            "url": exhibit_url,
            "excerpt": _clean_excerpt(http_get(exhibit_url, headers), excerpt_chars),
            "supports_claims": ["guidance", "earnings release", "management commentary"],
        }
    except Exception as exc:  # noqa: BLE001 - keep cover-page evidence if exhibit lookup fails.
        return {
            "status": "unavailable",
            "source_type": "earnings_release_exhibit",
            "exhibit_name": "Exhibit 99.1",
            "filing_date": filing_date,
            "url": "",
            "excerpt": "",
            "supports_claims": ["guidance", "earnings release", "management commentary"],
            "reason": str(exc),
        }


def collect_financial_document_sources(
    ticker: str,
    trade_date: str,
    *,
    http_get: HttpGet = _default_http_get,
    excerpt_chars: int = 6000,
) -> dict[str, Any]:
    symbol = ticker.upper()
    if not _is_plain_us_ticker(symbol):
        return {
            "ticker": symbol,
            "trade_date": trade_date,
            "status": "unavailable",
            "sources": [
                {
                    "source_type": "sec_filings",
                    "status": "unavailable",
                    "reason": "Ticker is not a plain US exchange ticker; SEC lookup was skipped.",
                }
            ],
        }

    headers = _sec_headers()
    try:
        mapping = _company_ticker_map(http_get(SEC_COMPANY_TICKERS_URL, headers))
        record = mapping.get(symbol)
        if not record:
            return {
                "ticker": symbol,
                "trade_date": trade_date,
                "status": "unavailable",
                "sources": [
                    {
                        "source_type": "sec_filings",
                        "status": "unavailable",
                        "reason": "Ticker was not found in the SEC company ticker mapping.",
                    }
                ],
            }

        cik = f"{int(record['cik_str']):010d}"
        submissions = json.loads(http_get(SEC_SUBMISSIONS_URL.format(cik=cik), headers))
        rows = _recent_filings(submissions, trade_date)
        annual = _first_filing(rows, "10-K")
        quarterly = _first_filing(rows, "10-Q")

        sources = [
            _source_from_filing(
                source_type="annual_report_10k",
                source_name="Latest SEC 10-K on or before trade date",
                cik=cik,
                filing=annual,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
                unavailable_reason="No 10-K filing found on or before the trade date.",
            ),
            _source_from_filing(
                source_type="quarterly_report_10q",
                source_name="Latest SEC 10-Q on or before trade date",
                cik=cik,
                filing=quarterly,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
                unavailable_reason="No 10-Q filing found on or before the trade date.",
            ),
            _earnings_8k_source(
                rows=rows,
                cik=cik,
                http_get=http_get,
                headers=headers,
                excerpt_chars=excerpt_chars,
            ),
            {
                "source_type": "investor_presentation",
                "source_name": "Latest investor presentation",
                "status": "unavailable",
                "reason": "No investor presentation source was discovered from the SEC submissions feed.",
            },
        ]
        return {
            "ticker": symbol,
            "company_name": record.get("title", ""),
            "trade_date": trade_date,
            "status": "ok",
            "cik": cik,
            "as_of_rule": "Only filings with filingDate <= trade_date are included.",
            "sources": sources,
        }
    except Exception as exc:  # noqa: BLE001 - evidence collection should degrade gracefully.
        return {
            "ticker": symbol,
            "trade_date": trade_date,
            "status": "error",
            "sources": [
                {
                    "source_type": "sec_filings",
                    "status": "error",
                    "reason": str(exc),
                }
            ],
        }


def render_financial_document_packet(packet: dict[str, Any]) -> str:
    lines = [
        f"## Financial Document Source Packet: {packet.get('ticker', 'N/A')}",
        "",
        f"- Trade date: `{packet.get('trade_date', 'N/A')}`",
        f"- Collection status: `{packet.get('status', 'unknown')}`",
    ]
    if packet.get("company_name"):
        lines.append(f"- SEC company name: {packet['company_name']}")
    if packet.get("cik"):
        lines.append(f"- SEC CIK: `{packet['cik']}`")
    if packet.get("as_of_rule"):
        lines.append(f"- As-of rule: {packet['as_of_rule']}")
    lines.extend(
        [
            "",
            "| Source | Status | Filing date | Form | URL / reason |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for source in packet.get("sources", []):
        url_or_reason = source.get("url") or source.get("reason", "")
        lines.append(
            "| {source_type} | {status} | {filing_date} | {form} | {url_or_reason} |".format(
                source_type=source.get("source_type", "unknown"),
                status=source.get("status", "unknown"),
                filing_date=source.get("filing_date", ""),
                form=source.get("form", ""),
                url_or_reason=url_or_reason,
            )
        )
    lines.append("")
    for source in packet.get("sources", []):
        for section in source.get("sections", []):
            supports_claims = ", ".join(section.get("supports_claims", [])) or "N/A"
            lines.extend(
                [
                    f"### Section: {source.get('source_type', 'source')} / {section.get('section_type', 'section')}",
                    "",
                    f"- Section name: {section.get('section_name', section.get('source_section', 'N/A'))}",
                    f"- Status: `{section.get('status', 'unknown')}`",
                    f"- Source type: `{section.get('source_type', source.get('source_type', 'N/A'))}`",
                    f"- Filing date: `{section.get('filing_date', source.get('filing_date', 'N/A'))}`",
                    f"- URL: {section.get('url', source.get('url', 'N/A'))}",
                    f"- Supports claims: {supports_claims}",
                ]
            )
            if section.get("excerpt"):
                lines.extend(["", "```text", section["excerpt"], "```", ""])
            else:
                lines.extend([f"- Unavailable reason: {section.get('unavailable_reason', 'No excerpt extracted.')}", ""])
        cover = source.get("cover_page", {})
        if cover.get("excerpt"):
            lines.extend(
                [
                    f"### 8-K Cover Page: {source.get('source_type', 'source')}",
                    "",
                    f"- Filing date: `{source.get('filing_date', 'N/A')}`",
                    f"- URL: {cover.get('url', source.get('url', 'N/A'))}",
                    "",
                    "```text",
                    cover["excerpt"],
                    "```",
                    "",
                ]
            )
        exhibit = source.get("exhibit_99_1", {})
        if exhibit:
            lines.extend(
                [
                    f"### Exhibit 99.1: {source.get('source_type', 'source')}",
                    "",
                    f"- Status: `{exhibit.get('status', 'unknown')}`",
                    f"- Filing date: `{exhibit.get('filing_date', source.get('filing_date', 'N/A'))}`",
                    f"- URL: {exhibit.get('url', 'N/A')}",
                    f"- Supports claims: {', '.join(exhibit.get('supports_claims', [])) or 'N/A'}",
                ]
            )
            if exhibit.get("excerpt"):
                lines.extend(["", "```text", exhibit["excerpt"], "```", ""])
            else:
                lines.extend([f"- Unavailable reason: {exhibit.get('reason', 'No exhibit text extracted.')}", ""])
        if not source.get("excerpt"):
            continue
        lines.extend(
            [
                f"### Excerpt: {source.get('source_type', 'source')}",
                "",
                f"- Filing date: `{source.get('filing_date', 'N/A')}`",
                f"- URL: {source.get('url', 'N/A')}",
                "",
                "```text",
                source["excerpt"],
                "```",
                "",
            ]
        )
    return "\n".join(lines)
