from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from week01.conversation import Conversation, Message


class StreamingModel(Protocol):
    def stream(self, messages: list[Message]) -> Iterable[str]: ...


class ChatSession:
    """Coordinates state and a model, without depending on a specific provider."""

    def __init__(self, model: StreamingModel, conversation: Conversation) -> None:
        self._model = model
        self.conversation = conversation

    def reply(self, user_text: str) -> Iterable[str]:
        history_before_turn = self.conversation.snapshot()
        self.conversation.add("user", user_text)
        pieces: list[str] = []

        try:
            for piece in self._model.stream(self.conversation.snapshot()):
                pieces.append(piece)
                yield piece
        except Exception:
            # Restore the entire snapshot: adding the user turn may have trimmed an
            # older message when history was already at capacity.
            self.conversation.messages[:] = history_before_turn
            raise

        answer = "".join(pieces).strip()
        if not answer:
            self.conversation.messages[:] = history_before_turn
            raise RuntimeError("The model returned no text")
        self.conversation.add("assistant", answer)
