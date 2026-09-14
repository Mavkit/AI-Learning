import pytest

from week01.config import Settings


def test_settings_have_development_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    monkeypatch.delenv("MAX_HISTORY_MESSAGES", raising=False)

    settings = Settings.from_environment()

    assert settings.model == "gpt-5.6-luna"
    assert settings.max_history_messages == 20


def test_history_limit_must_be_valid(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MAX_HISTORY_MESSAGES", "one hundred")

    with pytest.raises(ValueError, match="must be an integer"):
        Settings.from_environment()

