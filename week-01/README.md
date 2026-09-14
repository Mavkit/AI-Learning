# Week 1 — LLM foundations through a streaming chat client

## The mental model

An LLM receives a sequence of tokens and predicts a probability distribution for
the next token. It repeats that operation to generate a response. The application
around it decides what context to send, what capabilities to expose, and what to
do with the output.

Keep these distinctions clear:

- **Model:** predicts tokens from context. It does not inherently know current
  facts, remember prior API calls, or execute actions.
- **Instructions:** text included in context that steers behavior. Instructions
  influence a model; they are not an authorization or security boundary.
- **Conversation state:** messages the application stores and resends. This lab
  owns that state explicitly in `Conversation`.
- **Streaming:** partial output events delivered while generation continues. It
  improves perceived latency but introduces partial-failure behavior.
- **Context window:** the finite token budget shared by instructions, input,
  history, retrieved material, tool data, reasoning, and output.

## Architecture

```text
terminal input
     |
     v
ChatSession ----> Conversation (application-owned state)
     |
     v
StreamingModel protocol
     |
     v
OpenAI Responses API ----> text delta events ----> terminal
```

The provider adapter is deliberately thin. `ChatSession` can be tested with a
fake model, which is faster, deterministic, and free.

## Set up

From this directory, create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Set configuration for the current PowerShell session. Use a model available to
your API project if the example value is unavailable:

```powershell
$env:OPENAI_API_KEY = "your-key"
$env:OPENAI_MODEL = "gpt-5.6-luna"
```

Do not commit an API key or put it directly in source code.

Run tests and then the client:

```powershell
pytest
week1-chat
```

Inside the client, use `/history`, `/clear`, and `/quit`.

## Code-reading order

1. `src/week01/conversation.py`
2. `src/week01/chat.py`
3. `src/week01/openai_model.py`
4. `src/week01/cli.py`
5. `tests/`

## Experiments

### 1. Inspect context

Have a five-turn conversation, use `/history`, and answer:

- Where is memory actually stored?
- What will the next API request contain?
- What happens after message 20?

### 2. Instruction hierarchy

Change the `instructions` text in `openai_model.py`. Try asking for behavior that
conflicts with it. Record what happens, but do not interpret consistent obedience
as a security guarantee.

### 3. Sampling

Temporarily add a supported sampling setting to the API request. Ask for ten names
for the same product several times and compare diversity. Change one sampling
control at a time.

### 4. Partial failure

Read `test_failed_turn_is_not_committed_to_history`. Decide whether removing the
entire failed turn is the right production behavior. Write down at least two other
policies.

### 5. Context pressure

Set `MAX_HISTORY_MESSAGES=4`, conduct a longer conversation, and observe how a
message-pair can be split. This intentionally naive behavior motivates the context
manager we will build later.

## Knowledge check

Write short answers without using an AI assistant:

1. What does a language model calculate at each generation step?
2. Why can the same input produce different outputs?
3. Where does this application's conversation memory live?
4. Why is streaming more complicated than a normal function return?
5. Why are system instructions not a security boundary?
6. What competes for space inside a context window?
7. How does a model hallucination differ from an ordinary exception?

## Completion criteria

Week 1 is complete when:

- All tests pass.
- You can run a multi-turn streaming conversation.
- You complete experiments 1, 4, and 5.
- You answer all seven knowledge-check questions.
- You can explain the model/application boundary in your own words.

Do not proceed merely because the client works. The observations and explanations
are the actual learning outcome.

