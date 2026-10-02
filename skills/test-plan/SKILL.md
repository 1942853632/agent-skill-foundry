---
name: test-plan
description: Design a focused test plan from behavior, risk and system boundaries. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: engineering
  short-description: Test Plan
---

# Test Plan

## Purpose

Design a focused test plan from behavior, risk and system boundaries.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **feature spec, interfaces, risk areas, environments**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. map behavior to unit, integration and end-to-end layers.
2. prioritize boundary and failure cases.
3. define fixtures, mocks and cleanup.
4. set exit criteria and evidence artifacts.
5. identify tests that are expensive or flaky.

## Output contract

Return: A test matrix with cases, layer, owner, data and release gates.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Critical behavior has a deterministic test.
- [ ] Mocks do not erase the risk being tested.
- [ ] Exit criteria are observable.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A file import feature gets parser unit tests, storage integration tests and one browser smoke test.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
