from __future__ import annotations

import re
from dataclasses import dataclass
from html.parser import HTMLParser


@dataclass(frozen=True)
class ArticleRetrievalResult:
    text: str
    fetch_status: str = "ok"
    http_status: int | None = None
    final_url: str = ""
    content_type: str = "text/html"
    extraction_method: str = "html_text"


class _TextExtractor(HTMLParser):
    def __init__(self, preferred_tags: set[str] | None = None) -> None:
        super().__init__()
        self.preferred_tags = preferred_tags or set()
        self._skip_depth = 0
        self._capture_depth = 0 if self.preferred_tags else 1
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
            return
        if self.preferred_tags and tag in self.preferred_tags:
            self._capture_depth += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
            return
        if self.preferred_tags and tag in self.preferred_tags and self._capture_depth:
            self._capture_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._skip_depth or not self._capture_depth:
            return
        text = re.sub(r"\s+", " ", data).strip()
        if text:
            self.parts.append(text)


def _extract_with_tags(html: str, tags: set[str]) -> str:
    parser = _TextExtractor(tags)
    parser.feed(html)
    return re.sub(r"\s+", " ", " ".join(parser.parts)).strip()


def extract_article_text_from_html(html: str, *, title: str = "", final_url: str = "") -> ArticleRetrievalResult:
    del title
    for tags, method in [
        ({"article"}, "article_tag"),
        ({"main"}, "main_tag"),
        ({"p"}, "paragraph_fallback"),
    ]:
        text = _extract_with_tags(html, tags)
        if len(text.split()) >= 8:
            return ArticleRetrievalResult(text=text, final_url=final_url, extraction_method=method)

    text = _extract_with_tags(html, set())
    return ArticleRetrievalResult(text=text, final_url=final_url, extraction_method="html_text")
