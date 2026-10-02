---
name: responsive-layout-review
description: Turn screenshots or a page brief into responsive layout rules that remain stable across viewports. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: web
  short-description: Responsive Layout Review
---

# Responsive Layout Review

## Purpose

Turn screenshots or a page brief into responsive layout rules that remain stable across viewports.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **design or screenshots, target widths, content extremes, existing CSS**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. identify fixed, fluid and intrinsic dimensions.
2. find likely wrap and overflow boundaries.
3. define layout changes at content-driven breakpoints.
4. test long labels, empty states and zoom.
5. write CSS-level acceptance checks.

## Output contract

Return: A responsive layout note with constraints, breakpoints, overflow policy and test cases.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Breakpoints respond to content rather than device names alone.
- [ ] No state depends on hidden clipping.
- [ ] Long text and keyboard focus remain visible.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A card grid plan defines minmax tracks, a one-column fallback and behavior for a long project name.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
