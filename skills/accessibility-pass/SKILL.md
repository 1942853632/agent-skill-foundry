---
name: accessibility-pass
description: Review a web page for practical keyboard, semantic and visual accessibility issues. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: web
  short-description: Accessibility Pass
---

# Accessibility Pass

## Purpose

Review a web page for practical keyboard, semantic and visual accessibility issues.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **page or component, target browsers, interaction flows, design constraints**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. walk every flow with keyboard only.
2. check landmarks, headings, labels, focus and announcements.
3. inspect contrast, zoom and reduced-motion behavior.
4. test errors and dynamic updates.
5. prioritize fixes by blocked users and effort.

## Output contract

Return: An accessibility findings list with severity, element, reproduction and repair guidance.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Findings include a user impact.
- [ ] Keyboard and screen-reader issues are distinguished.
- [ ] The review verifies fixes rather than only listing rules.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A dialog review catches focus escaping to the page, a missing label and an error message not announced.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
