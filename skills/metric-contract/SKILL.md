---
name: metric-contract
description: Define a metric so analysts, product teams and pipelines compute the same number. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: data
  short-description: Metric Contract
---

# Metric Contract

## Purpose

Define a metric so analysts, product teams and pipelines compute the same number.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **metric name, business question, entities, event schema, time window**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. define the entity and grain.
2. write numerator, denominator and exclusions.
3. specify time zone, late data and deduplication.
4. add dimensions and guardrail metrics.
5. define ownership, validation and change policy.

## Output contract

Return: A metric contract with formula, SQL-like pseudocode, examples and governance fields.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The denominator is unambiguous.
- [ ] A small example can be calculated by hand.
- [ ] Changes have an owner and compatibility rule.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

Weekly active users specifies user identity, qualifying event, calendar boundary and bot exclusion.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
