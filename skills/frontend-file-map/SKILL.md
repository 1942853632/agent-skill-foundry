---
name: frontend-file-map
description: Explain an unfamiliar frontend repository so a contributor can find the correct files safely. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: web
  short-description: Frontend File Map
---

# Frontend File Map

## Purpose

Explain an unfamiliar frontend repository so a contributor can find the correct files safely.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **repository tree, package scripts, routes, entry points, target change**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. locate build entry, routes and shared UI boundaries.
2. trace the target screen from route to data to component.
3. record state ownership and styling conventions.
4. identify tests, fixtures and generated files.
5. return a smallest-change map with unknowns.

## Output contract

Return: A repository map with relevant files, data flow, conventions and safe edit boundaries.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Generated and source files are distinguished.
- [ ] The map cites inspected paths.
- [ ] Unknown ownership is stated rather than guessed.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A request to change a settings panel maps route, loader, form component, validation schema and existing tests.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
