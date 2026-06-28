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
    text = re.sub(r"(?is)<ix:header.*?</ix:header>", " ", raw)
    text = re.sub(
        r"(?is)<[^>]+style=[\"'][^\"']*display\s*:\s*none[^\"']*[\"'][^>]*>.*?</[^>]+>",
        " ",
        text,
    )
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].strip()


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
        source["excerpt"] = _clean_excerpt(http_get(url, headers), excerpt_chars)
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
            excerpt = _clean_excerpt(http_get(url, headers), excerpt_chars)
        except Exception:
            excerpt = ""
        if not _has_earnings_8k_hint(f"{description} {excerpt}"):
            continue
        return {
            "source_type": "earnings_release_8k",
            "source_name": "Latest SEC 8-K earnings-release evidence on or before trade date",
            "status": "available",
            "form": filing["form"],
            "filing_date": filing["filingDate"],
            "description": description,
            "url": url,
            "excerpt": excerpt,
        }
    return {
        "source_type": "earnings_release_8k",
        "source_name": "Latest SEC 8-K earnings-release evidence",
        "status": "unavailable",
        "reason": "No 8-K with earnings/results-of-operations evidence was found on or before the trade date.",
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
