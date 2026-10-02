---
name: webpage-debug
description: Guide a systematic diagnosis of a broken webpage using observable browser evidence. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: web
  short-description: Webpage Debugging
---

# Webpage Debugging

## Purpose

Guide a systematic diagnosis of a broken webpage using observable browser evidence.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **symptom, URL or local page, console output, network behavior, recent change**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. reproduce in a clean viewport and record the symptom.
2. classify layout, runtime, network or state failure.
3. inspect the smallest relevant DOM, styles and console evidence.
4. make one hypothesis-driven change at a time.
5. verify desktop, mobile and refresh behavior.

## Output contract

Return: A debugging record with reproduction, evidence, hypothesis, fix and regression check.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The fix is tied to evidence rather than visual guessing.
- [ ] A successful reload is tested.
- [ ] The report distinguishes site failure from environment failure.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A missing modal is traced from click event to console exception to a null selector, then covered by a smoke test.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
