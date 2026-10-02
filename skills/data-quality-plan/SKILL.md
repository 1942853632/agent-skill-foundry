---
name: data-quality-plan
description: Design practical checks and ownership for a dataset or pipeline. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: data
  short-description: Data Quality Plan
---

# Data Quality Plan

## Purpose

Design practical checks and ownership for a dataset or pipeline.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **dataset contract, failure history, consumers, freshness target**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. list critical fields and invariants.
2. choose completeness, validity, uniqueness and freshness checks.
3. define thresholds and severity.
4. map failures to owner and response.
5. add a small representative fixture.

## Output contract

Return: A quality plan with checks, thresholds, alert policy, owners and test fixtures.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Every check has a failure action.
- [ ] Thresholds are tied to business impact.
- [ ] The plan distinguishes warning from blocking failures.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

An orders pipeline gets checks for unique order IDs, nonnegative totals, accepted currency codes and daily freshness.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
