# Agent Skill Foundry

Agent Skill Foundry is a curated library of small, reusable skills for everyday writing, research, data work, Agent design and software delivery.

This repository is intentionally different from browser analyzers such as ContextDock, SkillSentry, OpenAPI Lens and PR Risk Lens. It does not scan pages or repositories. Each directory contains a focused workflow that helps an Agent turn supplied material into a reviewable artifact.

## Collection

The first release contains 42 skills:

- **Writing and communication**: specifications, technical editing, decision memos, meeting actions, resume bullets and article outlines
- **Research and evidence**: paper notes, evidence matrices, claim audits, literature gaps, experiment narratives and citations
- **Data work**: data dictionaries, metric contracts, SQL reviews, quality plans, experiment design and dataset cards
- **Agent design**: task contracts, workflow decomposition, tool interfaces, prompt tests, human review and runbooks
- **Engineering delivery**: bug reproduction, ADRs, test plans, migrations, release notes and postmortems
- **Daily work**: email replies, weekly plans, document checklists, knowledge cleanup, web research briefs and study explanations
- **Web development**: UI-to-component planning, webpage debugging, accessibility reviews, responsive layout reviews, browser automation plans and frontend repository maps

## Skill shape

Every skill has the same minimum contract:

1. A discriminating description and explicit boundary
2. Required inputs and missing-information behavior
3. A multi-step workflow for the specific task
4. An output contract that separates facts, reasoning and decisions
5. A quality gate with observable checks
6. An example shape and safety boundaries

The shared structure makes the collection easy to browse, while the task-specific steps keep the skills from becoming generic prompt templates.

## Use a skill

Copy a skill directory into the skill directory used by your Agent runtime, or load its `SKILL.md` directly when the runtime supports repository skills. Start with the narrowest matching skill; do not combine unrelated skills just because they are in the same collection.

```text
skills/
  metric-contract/SKILL.md
  webpage-debug/SKILL.md
  decision-memo/SKILL.md
```

## Validate

```bash
python scripts/generate_skills.py
python scripts/validate_skills.py
```

The validator checks names, catalog coverage, required sections and minimum content length. GitHub Actions runs the same check on every push and pull request.

## Design boundary

The library does not claim to replace domain experts, invent missing evidence or perform irreversible actions. It provides explicit workflows and review points so an Agent can be useful without becoming opaque.
