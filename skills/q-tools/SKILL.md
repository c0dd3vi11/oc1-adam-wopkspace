---
name: q-tools
description: Use local q-tools toolbox (q CLI + reusable scripts) to convert verbal logic into repeatable algorithms and operational commands. Use when tasks should be standardized, scripted, reused, or composed into larger workflows.
---

# q-tools

## Read first

- `/home/adam/dev/tools/q-tools/AGENTS.md`

## Home

- Repo: `/home/adam/dev/tools/q-tools`
- CLI: `/home/adam/dev/tools/q-tools/bin/q`

## Core idea

Use q-tools when a process should become deterministic and reusable instead of redoing manual ad-hoc steps.

## Typical usage

1. Discover existing command in `q` first.
2. If missing, implement/extend script in q-tools repo.
3. Validate by running command/tests (`q tests` when code changed).
4. Reuse the command in future workflows.

## Operational notes

- Follow repo rules from q-tools AGENTS.md (including commit/push policy when changing q-tools repo).
- Prefer concise, meaningful step checkpoints and verifiable outputs.
