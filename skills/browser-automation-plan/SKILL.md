---
name: browser-automation-plan
description: Design a reliable browser automation flow before implementing selectors and actions. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: web
  short-description: Browser Automation Plan
---

# Browser Automation Plan

## Purpose

Design a reliable browser automation flow before implementing selectors and actions.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **user flow, target pages, authentication boundary, artifacts, failure cases**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. define the business outcome and safe stopping point.
2. choose stable semantic selectors before CSS paths.
3. separate navigation, assertion and mutation steps.
4. plan screenshots, traces and cleanup.
5. add retry limits and manual handoff conditions.

## Output contract

Return: An automation plan with selectors, assertions, artifacts, retries and authorization gates.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The flow never guesses destructive confirmation.
- [ ] Assertions prove state before the next mutation.
- [ ] Authentication and secrets stay outside page text.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A form-filling flow checks the account and draft state before submitting, then saves a confirmation screenshot.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
