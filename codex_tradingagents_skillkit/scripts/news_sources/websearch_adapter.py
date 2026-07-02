from __future__ import annotations

from news_sources.base import NewsCandidate, SourceAttempt


class WebSearchAdapter:
    name = "websearch_adapter"

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        return [], SourceAttempt(
            adapter=self.name,
            status="unavailable",
            limitations=["No approved websearch bridge is configured for unattended Python collection."],
        )
