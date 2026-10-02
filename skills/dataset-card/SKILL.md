---
name: dataset-card
description: Document a dataset's provenance, composition, intended use and limitations. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: data
  short-description: Dataset Card
---

# Dataset Card

## Purpose

Document a dataset's provenance, composition, intended use and limitations.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **dataset files, collection process, labels, license, known issues**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. describe source and version.
2. summarize population, fields and missingness.
3. record collection and labeling choices.
4. define intended and prohibited uses.
5. list bias, privacy, drift and maintenance risks.

## Output contract

Return: A dataset card that lets a downstream user judge fitness before use.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] License and consent claims are sourced.
- [ ] Known exclusions are visible.
- [ ] Limitations are specific enough to test.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A text dataset card documents language mix, duplicate policy, PII removal and domain shift risk.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
