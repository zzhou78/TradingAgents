from __future__ import annotations

from sentiment_sources.base import SocialCandidate


class StockTwitsAdapter:
    name = "stocktwits_adapter"

    def __init__(self, *, lines: list[str]) -> None:
        self.lines = lines

    def collect(self) -> list[SocialCandidate]:
        return [
            SocialCandidate(source="stocktwits", source_url="local://tool/fetch_stocktwits_messages", posted_at="", text=line)
            for line in self.lines
        ]
