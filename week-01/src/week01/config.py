from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Runtime configuration read from environment variables."""

    model: str
    max_history_messages: int

    @classmethod
    def from_environment(cls) -> "Settings":
        model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna").strip()
        raw_limit = os.getenv("MAX_HISTORY_MESSAGES", "20")

        try:
            limit = int(raw_limit)
        except ValueError as exc:
            raise ValueError("MAX_HISTORY_MESSAGES must be an integer") from exc

        if not model:
            raise ValueError("OPENAI_MODEL cannot be empty")
        if limit < 2:
            raise ValueError("MAX_HISTORY_MESSAGES must be at least 2")

        return cls(model=model, max_history_messages=limit)

