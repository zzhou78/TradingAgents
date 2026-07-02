from __future__ import annotations

import os

from news_sources.base import NewsCandidate, SourceAttempt


class NewsApiAdapter:
    name = "newsapi_adapter"

    def __init__(self, *, api_key_env: str = "NEWSAPI_KEY"):
        self.api_key_env = api_key_env

    def collect(self) -> tuple[list[NewsCandidate], SourceAttempt]:
        if not os.environ.get(self.api_key_env):
            return [], SourceAttempt(
                adapter=self.name,
                status="unavailable",
                limitations=[f"{self.api_key_env} is not configured"],
            )
        return [], SourceAttempt(
            adapter=self.name,
            status="unavailable",
            limitations=["NewsAPI live retrieval is not configured in this local workflow."],
        )
