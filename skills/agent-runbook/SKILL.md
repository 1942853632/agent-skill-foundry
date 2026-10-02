---
name: agent-runbook
description: Create an operational runbook for observing, debugging and safely pausing an Agent workflow. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: agent
  short-description: Agent Runbook
---

# Agent Runbook

## Purpose

Create an operational runbook for observing, debugging and safely pausing an Agent workflow.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **workflow contract, logs, tools, owners, incident history**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. define health signals and useful trace fields.
2. map common symptoms to likely causes.
3. write safe pause, replay and rollback procedures.
4. set escalation ownership and communication templates.
5. add a post-incident learning loop.

## Output contract

Return: A runbook with dashboards, triage steps, recovery actions and escalation criteria.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] A responder can identify one run from its evidence.
- [ ] Recovery steps state what must not be repeated.
- [ ] Rollback does not rely on undocumented state.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A tool-call loop runbook defines max-step alerts, trace IDs, safe replay inputs and a kill switch.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
