---
name: data-dictionary
description: Create a useful data dictionary that explains fields, lineage and safe usage. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: data
  short-description: Data Dictionary
---

# Data Dictionary

## Purpose

Create a useful data dictionary that explains fields, lineage and safe usage.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **schema, sample rows, source system, owners, business context**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. inventory fields and data types.
2. describe business meaning and units.
3. record null, default and valid-value behavior.
4. capture lineage, freshness and owner.
5. add sensitive-data and join warnings.

## Output contract

Return: A field-level dictionary with examples, quality expectations and ownership.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Names and descriptions agree with the schema.
- [ ] Units and time zones are explicit.
- [ ] Sensitive fields have handling guidance.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

An events table dictionary records event_time timezone, deduplication key, late-arrival policy and owner.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
