from __future__ import annotations

from openai import APIConnectionError, APIError, AuthenticationError, RateLimitError

from week01.chat import ChatSession
from week01.config import Settings
from week01.conversation import Conversation
from week01.openai_model import OpenAIStreamingModel


def main() -> None:
    settings = Settings.from_environment()
    session = ChatSession(
        model=OpenAIStreamingModel(settings.model),
        conversation=Conversation(max_messages=settings.max_history_messages),
    )

    print(f"Week 1 chat — model: {settings.model}")
    print("Commands: /history, /clear, /quit")

    while True:
        try:
            user_text = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return

        if not user_text:
            continue
        if user_text == "/quit":
            return
        if user_text == "/clear":
            session.conversation.messages.clear()
            print("History cleared.")
            continue
        if user_text == "/history":
            for index, message in enumerate(session.conversation.snapshot(), start=1):
                print(f"{index:02d} {message['role']}: {message['content']}")
            continue

        print("Assistant: ", end="", flush=True)
        try:
            for text in session.reply(user_text):
                print(text, end="", flush=True)
            print()
        except AuthenticationError:
            print("\nAuthentication failed. Check OPENAI_API_KEY.")
        except RateLimitError:
            print("\nRate limit reached. Wait briefly, then retry.")
        except APIConnectionError:
            print("\nCould not reach the API. Check the network connection.")
        except APIError as exc:
            print(f"\nAPI request failed: {exc}")


if __name__ == "__main__":
    main()

