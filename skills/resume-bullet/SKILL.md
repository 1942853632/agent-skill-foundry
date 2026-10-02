---
name: resume-bullet
description: Turn real work notes into concise, evidence-based resume bullets for a target role. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: writing
  short-description: Resume Bullet Builder
---

# Resume Bullet Builder

## Purpose

Turn real work notes into concise, evidence-based resume bullets for a target role.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **work notes, role description, tools used, outcomes, constraints**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. identify the action, artifact, method and result.
2. select language that matches the target role.
3. quantify only values supported by the source.
4. remove internal jargon and vague ownership.
5. produce two lengths and flag missing evidence.

## Output contract

Return: Role-targeted bullets with a factual version and a shorter scan-friendly version.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] No invented metrics, titles or responsibilities.
- [ ] Each bullet has a concrete artifact or outcome.
- [ ] Technology names appear only when they explain the work.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A note about a rules engine becomes a bullet describing deterministic checks, evidence output and regression tests.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
