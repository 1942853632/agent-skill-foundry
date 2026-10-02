---
name: sql-review
description: Review analytical SQL for correctness, maintainability and cost without changing its intended result. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: data
  short-description: SQL Review
---

# SQL Review

## Purpose

Review analytical SQL for correctness, maintainability and cost without changing its intended result.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **SQL, schema, expected grain, sample output, performance constraint**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. state the output grain and join keys.
2. check filters, null behavior and aggregation order.
3. look for accidental fan-out and duplicate counting.
4. review readability, partition use and expensive scans.
5. return findings ordered by correctness risk.

## Output contract

Return: A review with severity, query location, explanation and a minimal fix or test.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Every finding names the affected grain.
- [ ] Performance claims reference a plan or known partition.
- [ ] Refactoring suggestions preserve semantics.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A review catches a many-to-many join that doubles revenue before aggregation.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
