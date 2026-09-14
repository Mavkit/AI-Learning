from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class Message(TypedDict):
    role: Literal["user", "assistant"]
    content: str


@dataclass
class Conversation:
    """Application-owned conversation history.

    Keeping this state locally makes the context sent on every request visible and
    testable. A production system will need a better strategy than simply dropping
    old messages; we intentionally confront that limitation in this week's labs.
    """

    max_messages: int = 20
    messages: list[Message] = field(default_factory=list)

    def add(self, role: Literal["user", "assistant"], content: str) -> None:
        text = content.strip()
        if not text:
            raise ValueError("A conversation message cannot be empty")
        self.messages.append({"role": role, "content": text})
        self._trim()

    def snapshot(self) -> list[Message]:
        return [message.copy() for message in self.messages]

    def _trim(self) -> None:
        overflow = len(self.messages) - self.max_messages
        if overflow > 0:
            del self.messages[:overflow]

