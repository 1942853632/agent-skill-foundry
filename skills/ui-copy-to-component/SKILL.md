---
name: ui-copy-to-component
description: Turn a UI description into a small, accessible web component plan before writing code. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: web
  short-description: UI Copy to Component
---

# UI Copy to Component

## Purpose

Turn a UI description into a small, accessible web component plan before writing code.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **screen goal, content, states, interaction, framework, constraints**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. identify the primary task and semantic elements.
2. map content to component boundaries.
3. define loading, empty, error and success states.
4. choose keyboard and screen-reader behavior.
5. specify responsive constraints and acceptance checks.

## Output contract

Return: A component plan with markup semantics, state table, props, interaction and test cases.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Every interactive control has an accessible name.
- [ ] Mobile behavior is explicit.
- [ ] Error and empty states are designed, not left to defaults.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A dashboard filter description becomes a form with labeled controls, URL state and a no-results explanation.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
