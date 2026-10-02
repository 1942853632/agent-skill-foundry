---
name: bug-reproduction
description: Turn a vague bug report into a minimal, repeatable reproduction package. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: engineering
  short-description: Bug Reproduction
---

# Bug Reproduction

## Purpose

Turn a vague bug report into a minimal, repeatable reproduction package.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **symptom, environment, logs, suspected inputs, expected behavior**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. separate observed behavior from interpretation.
2. record exact environment and preconditions.
3. minimize the input while preserving failure.
4. define expected and actual results.
5. add a regression test shape and evidence request.

## Output contract

Return: A reproduction report with steps, fixture, logs, severity and a candidate regression test.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Another engineer can reproduce without private context.
- [ ] The minimal case still demonstrates the failure.
- [ ] Environment assumptions are explicit.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A flaky parser bug becomes a five-line fixture with locale, input encoding and expected exception.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
