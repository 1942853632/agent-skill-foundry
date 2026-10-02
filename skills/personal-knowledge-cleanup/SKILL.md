---
name: personal-knowledge-cleanup
description: Organize notes into a small, searchable knowledge base without over-classifying personal information. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: daily
  short-description: Personal Knowledge Cleanup
---

# Personal Knowledge Cleanup

## Purpose

Organize notes into a small, searchable knowledge base without over-classifying personal information.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **notes, tags or folders, retrieval goals, privacy boundaries**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. group notes by retrieval question rather than date alone.
2. merge exact duplicates and preserve conflicting versions.
3. extract durable facts, decisions and pending questions.
4. assign few stable tags and useful titles.
5. mark sensitive notes and stale items.

## Output contract

Return: A cleaned note set with naming rules, tags, links and a review queue.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Original meaning and uncertainty survive cleanup.
- [ ] Sensitive content is not copied into summaries unnecessarily.
- [ ] Tags improve retrieval instead of becoming a second taxonomy project.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

Scattered study notes become topic pages with definitions, worked examples and a list of unresolved questions.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
