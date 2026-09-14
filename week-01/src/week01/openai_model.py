from __future__ import annotations

from collections.abc import Iterable

from openai import OpenAI

from week01.conversation import Message


class OpenAIStreamingModel:
    """Small adapter around the OpenAI Responses API."""

    def __init__(self, model: str, client: OpenAI | None = None) -> None:
        self.model = model
        self.client = client or OpenAI()

    def stream(self, messages: list[Message]) -> Iterable[str]:
        stream = self.client.responses.create(
            model=self.model,
            instructions=(
                "You are a concise teaching assistant. Be accurate, state uncertainty, "
                "and do not claim access to information or tools you do not have."
            ),
            input=messages,
            stream=True,
        )
        for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta

