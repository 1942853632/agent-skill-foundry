---
name: incident-postmortem
description: Produce a blameless incident record focused on system learning and durable actions. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: engineering
  short-description: Incident Postmortem
---

# Incident Postmortem

## Purpose

Produce a blameless incident record focused on system learning and durable actions.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **timeline, alerts, logs, impact, response notes, contributing factors**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. state impact and detection clearly.
2. build a timestamped evidence-based timeline.
3. separate trigger, contributing conditions and missed signals.
4. identify what helped and what slowed response.
5. assign small corrective actions with owners and due dates.

## Output contract

Return: A postmortem with impact, timeline, causes, response assessment and tracked actions.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The narrative avoids individual blame.
- [ ] Root cause is not reduced to the first visible error.
- [ ] Actions change detection, prevention or recovery behavior.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A queue outage postmortem distinguishes a traffic spike from an unsafe retry policy and adds both capacity and alert actions.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
