from collections.abc import Iterable

import pytest

from week01.chat import ChatSession
from week01.conversation import Conversation, Message


class FakeModel:
    def __init__(self, pieces: list[str]) -> None:
        self.pieces = pieces
        self.received: list[Message] = []

    def stream(self, messages: list[Message]) -> Iterable[str]:
        self.received = messages
        yield from self.pieces


class FailingModel:
    def stream(self, messages: list[Message]) -> Iterable[str]:
        yield "partial"
        raise RuntimeError("network failed")


def test_reply_streams_and_records_both_sides() -> None:
    model = FakeModel(["hello", " there"])
    conversation = Conversation()
    session = ChatSession(model, conversation)

    assert list(session.reply("Hi")) == ["hello", " there"]
    assert model.received == [{"role": "user", "content": "Hi"}]
    assert conversation.messages == [
        {"role": "user", "content": "Hi"},
        {"role": "assistant", "content": "hello there"},
    ]


def test_failed_turn_is_not_committed_to_history() -> None:
    conversation = Conversation()
    session = ChatSession(FailingModel(), conversation)

    with pytest.raises(RuntimeError, match="network failed"):
        list(session.reply("Will this fail?"))

    assert conversation.messages == []


def test_failed_turn_restores_history_that_would_have_been_trimmed() -> None:
    conversation = Conversation(max_messages=2)
    conversation.add("user", "old question")
    conversation.add("assistant", "old answer")
    session = ChatSession(FailingModel(), conversation)

    with pytest.raises(RuntimeError, match="network failed"):
        list(session.reply("new question"))

    assert conversation.messages == [
        {"role": "user", "content": "old question"},
        {"role": "assistant", "content": "old answer"},
    ]
