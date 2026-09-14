# 14-Week Roadmap

Recommended workload: 8–12 hours per week.

## Week 1 — LLM foundations

Learn transformers at a practical level, tokens, context windows, inference,
message roles, streaming, conversation state, and hallucinations. Build a small
streaming chat application using a direct model API.

## Week 2 — Structured outputs and tool calling

Learn JSON Schema, typed validation, tool selection, dispatch, retries, timeouts,
and idempotency. Build a validated tool registry with argument bounds and step
limits.

## Week 3 — Embeddings and vector search

Learn embedding spaces, similarity metrics, exact and approximate search, HNSW,
metadata filtering, and when vector search is inappropriate. Implement and
compare semantic and keyword retrieval.

## Week 4 — RAG and document ingestion

Learn parsing, chunking, hybrid retrieval, reranking, grounded generation,
citations, provenance, retrieval evaluation, and retrieval-based prompt
injection. Build a cited document assistant.

## Week 5 — The basic agent loop

Learn the difference between agents and workflows, state machines, stopping
conditions, and model-controlled versus code-controlled decisions. Build a
provider-independent execution loop with state and an event log.

## Week 6 — Reliable tool execution

Learn partial failure, retries, backoff, idempotency, cancellation, concurrency,
transactions, compensation, checkpoints, and replay. Separate read capabilities
from consequential write capabilities.

## Week 7 — Context, state, and memory

Learn working, episodic, and semantic memory; context selection; compression;
retention; and memory poisoning. Build persistent task state and a token-budgeted
context manager.

## Week 8 — Guardrail architecture

Build a deterministic policy engine that can allow, deny, or require approval for
proposed actions. Study least privilege, capability security, argument policies,
trust boundaries, and fail-open versus fail-closed behavior.

## Week 9 — Prompt injection and adversarial safety

Study direct and indirect prompt injection, exfiltration, confused-deputy
attacks, excessive agency, tool-result poisoning, and cross-tool escalation.
Create trust labels, secret protection, approval flows, and an adversarial suite.

## Week 10 — MCP architecture

Learn MCP hosts, clients, servers, tools, resources, prompts, transports,
capability discovery, authentication, and authorization. Build an MCP server and
connect it to the agent harness with server-specific permissions.

## Week 11 — Planning and multi-agent systems

Compare fixed workflows with dynamic planning. Build a planner-worker workflow
with typed delegation, restricted capabilities, depth limits, global budgets, and
measurable comparisons against a simpler single-agent system.

## Week 12 — Evaluation

Build repeatable tests for task success, retrieval quality, tool selection,
argument accuracy, groundedness, policy compliance, attack resistance, latency,
and cost. Learn appropriate and inappropriate uses of LLM judges.

## Week 13 — Observability and debugging

Add runs, traces, spans, structured events, correlation identifiers, token and
cost accounting, failure classification, privacy-conscious logging, checkpoint
inspection, and replay.

## Week 14 — Production capstone

Complete the research and knowledge agent with an API, UI, authentication,
database-backed state, vector retrieval, MCP integrations, policy enforcement,
approvals, evaluations, tracing, containers, CI, and deployment configuration.
Run normal, failure, recovery, and adversarial assessments.

## Final outcome

The capstone is not merely an agent demo. It is an inspectable system in which the
model has bounded authority, consequential actions are controlled by deterministic
policy, failures can be diagnosed and replayed, and behavioral changes can be
measured with evaluations.

