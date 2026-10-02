---
name: meeting-actions
description: Convert a meeting transcript or rough notes into accountable decisions and follow-ups. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: writing
  short-description: Meeting to Actions
---

# Meeting to Actions

## Purpose

Convert a meeting transcript or rough notes into accountable decisions and follow-ups.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **transcript or notes, participants, date, project context**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. distinguish decisions, proposals, questions and side discussion.
2. attach each action to one owner and a due date when stated.
3. preserve disagreements and unresolved questions.
4. remove conversational filler while retaining evidence.
5. return a decision log and an action list.

## Output contract

Return: A concise meeting record with decisions, owners, deadlines, dependencies and open questions.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] No speaker is assigned an action without evidence.
- [ ] Unresolved items are not presented as decisions.
- [ ] Dates and names remain faithful to the source.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A design review transcript becomes a decision log with three owners and two explicitly unresolved API questions.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
