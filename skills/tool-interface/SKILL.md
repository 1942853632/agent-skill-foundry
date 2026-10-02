---
name: tool-interface
description: Design narrow, predictable tool interfaces for an Agent workflow. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: agent
  short-description: Tool Interface Designer
---

# Tool Interface Designer

## Purpose

Design narrow, predictable tool interfaces for an Agent workflow.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **agent task, external system, data model, error cases**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. define the smallest useful operation.
2. choose typed inputs and bounded outputs.
3. separate preview from mutation.
4. design idempotency and pagination behavior.
5. specify errors, authorization and audit fields.

## Output contract

Return: A tool contract with schema, examples, error taxonomy and safety notes.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] A tool does not hide multiple unrelated actions.
- [ ] Mutation and preview are distinguishable.
- [ ] Errors are actionable and machine-readable.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A ticket tool exposes search, preview-update and apply-update separately with an idempotency key.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
