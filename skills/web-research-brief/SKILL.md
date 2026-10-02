---
name: web-research-brief
description: Produce a compact, source-linked brief from a browsing task with clear freshness and uncertainty. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: daily
  short-description: Web Research Brief
---

# Web Research Brief

## Purpose

Produce a compact, source-linked brief from a browsing task with clear freshness and uncertainty.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **question, region, time window, trusted source types, decision to support**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. rewrite the question into answerable subquestions.
2. search primary or authoritative sources first.
3. record publication date and scope for each source.
4. separate verified facts from synthesis.
5. end with a recommendation and remaining uncertainty.

## Output contract

Return: A brief with answer, source table, caveats and next search terms.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Time-sensitive claims carry dates.
- [ ] Sources directly support nearby claims.
- [ ] The recommendation is labeled as an inference when appropriate.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A travel planning question becomes a brief comparing current opening hours, transit constraints and booking policies.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
