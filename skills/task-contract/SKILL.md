---
name: task-contract
description: Specify an Agent task so success, permissions and failure handling are explicit. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: agent
  short-description: Agent Task Contract
---

# Agent Task Contract

## Purpose

Specify an Agent task so success, permissions and failure handling are explicit.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **user goal, available tools, data boundaries, success signal**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. define the task outcome and non-goals.
2. list allowed inputs, tools and side effects.
3. set evidence and stop conditions.
4. describe retries, escalation and human approval.
5. create a small acceptance test set.

## Output contract

Return: A task contract with inputs, outputs, permissions, evidence, failure states and tests.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The agent cannot silently expand scope.
- [ ] Side effects require the named authorization.
- [ ] Success is observable without judging prose style.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A repository documentation agent may read source and open a draft PR but cannot merge or alter credentials.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
