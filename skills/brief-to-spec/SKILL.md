---
name: brief-to-spec
description: Turn an ambiguous product or engineering brief into an implementation-ready specification. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: writing
  short-description: Brief to Specification
---

# Brief to Specification

## Purpose

Turn an ambiguous product or engineering brief into an implementation-ready specification.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **goal, users, constraints, non-goals, acceptance signals**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. separate facts, assumptions and open questions.
2. define user-visible outcomes and explicit non-goals.
3. turn each outcome into testable acceptance criteria.
4. choose a minimal domain model and interfaces.
5. record risks, dependencies and unresolved decisions.

## Output contract

Return: A short specification with context, scope, flows, interfaces, acceptance criteria and open questions.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Every requirement has an observable acceptance signal.
- [ ] Non-goals prevent scope creep.
- [ ] Unknowns are labeled instead of invented.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A request for a browser export feature becomes a spec with supported formats, failure states and an export acceptance test.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
