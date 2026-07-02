from __future__ import annotations

from sentiment_sources.base import SocialCandidate


class UpstreamTradingAgentsSentimentAdapter:
    name = "upstream_tradingagents_sentiment_adapter"

    def __init__(self, *, lines: list[str], source_url: str = "local://tool/upstream_social") -> None:
        self.lines = lines
        self.source_url = source_url

    def collect(self) -> list[SocialCandidate]:
        return [
            SocialCandidate(source="upstream_tradingagents", source_url=self.source_url, posted_at="", text=line)
            for line in self.lines
        ]
