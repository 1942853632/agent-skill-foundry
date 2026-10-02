---
name: decision-memo
description: Write a concise decision memo that makes alternatives and trade-offs auditable. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: writing
  short-description: Decision Memo
---

# Decision Memo

## Purpose

Write a concise decision memo that makes alternatives and trade-offs auditable.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **decision, context, options, constraints, evidence, owner**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. state the decision and deadline first.
2. separate must-have constraints from preferences.
3. compare two or three viable options.
4. make trade-offs explicit with evidence.
5. record the chosen option, reversibility and follow-up owner.

## Output contract

Return: A decision memo with recommendation, alternatives, rationale, risks and next actions.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The recommendation follows from stated criteria.
- [ ] Rejected options have a reason.
- [ ] The memo names who decides and what happens next.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A team choosing between a queue and a database receives a memo that compares durability, latency and operational cost.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
