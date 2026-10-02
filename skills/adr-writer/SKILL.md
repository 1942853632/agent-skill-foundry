---
name: adr-writer
description: Record an architecture choice so future maintainers understand context and consequences. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: engineering
  short-description: Architecture Decision Record
---

# Architecture Decision Record

## Purpose

Record an architecture choice so future maintainers understand context and consequences.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **problem, constraints, options, evidence, decision owner**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. state the problem without prescribing the solution.
2. list constraints and evaluation criteria.
3. compare realistic alternatives.
4. record the decision and consequences.
5. define revisit triggers and status.

## Output contract

Return: An ADR with context, decision, alternatives, consequences and revisit conditions.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The decision is dated and owned.
- [ ] Consequences include costs and rejected benefits.
- [ ] A future change has a trigger, not vague reconsideration.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

An ADR chooses local storage over a hosted database for a privacy-first browser extension.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
