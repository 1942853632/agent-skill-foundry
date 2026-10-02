---
name: citation-normalizer
description: Normalize a mixed reference list and make citation fields consistent without fabricating metadata. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: research
  short-description: Citation Normalizer
---

# Citation Normalizer

## Purpose

Normalize a mixed reference list and make citation fields consistent without fabricating metadata.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **raw references, target style, available identifiers**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. parse author, title, venue, year and identifier fields.
2. resolve obvious formatting differences.
3. mark missing fields and ambiguous matches.
4. render the target style consistently.
5. return an unresolved-items list.

## Output contract

Return: A normalized bibliography plus a list of fields requiring human verification.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] No missing DOI or year is invented.
- [ ] Duplicate works are merged only with evidence.
- [ ] In-text keys remain stable.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A list containing URLs, DOI strings and copied titles becomes one consistent bibliography with unresolved entries marked.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
