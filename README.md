# Find Community Help

Slug: `find-community-help` · Version: `0.4.0` · License: MIT

Former name: `agent-travel` (legacy markers only)

Chinese: [README.zh.md](README.zh.md)

## What it is

A **Markdown-only** skill that writes a redacted **current-turn dry-run plan** when agent work is clearly blocked. It does not browse, run web commands, retain hints, or write durable memory.

## When to use

- stuck after local checks
- stalled / looping
- version-sensitive or likely known upstream solution
- user asks official/community help on that stuck task

Not for general research, news, pricing, or healthy tasks.

## Package

Published surface:

- `SKILL.md`
- `LICENSE`
- `agents/*.yaml`
- `references/*.md` (trigger, playbook, threat, host notes, optional suggestion contract)

No scripts, fixtures, or runtime services.

## Docs

- [references/trigger-policy.md](references/trigger-policy.md)
- [references/search-playbook.md](references/search-playbook.md)
- [references/threat-model.md](references/threat-model.md)
- [references/host-adapters.md](references/host-adapters.md)
- [references/suggestion-contract.md](references/suggestion-contract.md)
