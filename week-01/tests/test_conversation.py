import pytest

from week01.conversation import Conversation


def test_conversation_returns_a_defensive_snapshot() -> None:
    conversation = Conversation()
    conversation.add("user", "hello")

    snapshot = conversation.snapshot()
    snapshot[0]["content"] = "changed"

    assert conversation.messages[0]["content"] == "hello"


def test_conversation_drops_oldest_messages_at_its_limit() -> None:
    conversation = Conversation(max_messages=2)
    conversation.add("user", "one")
    conversation.add("assistant", "two")
    conversation.add("user", "three")

    assert [item["content"] for item in conversation.messages] == ["two", "three"]


def test_conversation_rejects_empty_messages() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        Conversation().add("user", "   ")

