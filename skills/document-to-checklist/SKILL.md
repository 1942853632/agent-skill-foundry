---
name: document-to-checklist
description: Convert a policy, guide or long instruction into an actionable checklist without losing exceptions. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: daily
  short-description: Document to Checklist
---

# Document to Checklist

## Purpose

Convert a policy, guide or long instruction into an actionable checklist without losing exceptions.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **source document, audience, completion evidence, deadline**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. extract obligations and conditional branches.
2. rewrite each obligation as an observable action.
3. preserve exceptions beside the action they modify.
4. order actions by dependency.
5. add evidence and escalation fields.

## Output contract

Return: A checklist with action, evidence, owner, condition and escalation path.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Every checklist item can be marked complete from evidence.
- [ ] Exceptions are visible at the decision point.
- [ ] The checklist does not create requirements absent from the source.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A lab safety guide becomes a pre-run checklist with equipment checks, stop conditions and sign-off evidence.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
