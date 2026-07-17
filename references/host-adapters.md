# Host Adapters

Use this file only when wiring a host adapter. Manual agent use can skip it.

## Shared Rule

- Advisory help-retrieval for stuck active threads only
- Require a semantic trigger; delivery windows alone are not enough
- Default `public-only`, chat-visible, current-response scoped
- Do not read old suggestion channels on later tasks

## Markdown-First Boundary

- `SKILL.md` and `references/*.md` are behavioral source of truth
- If a script preview disagrees with Markdown, follow Markdown and fix the script later
- Installed packages may omit `scripts/`; 0-script manual use is supported
- Source-repo script names keep legacy `*_travel.py` for compatibility; they are optional helpers, not prompt authority
- `should_travel.py`: host-state dry-run for automatic windows only
- `plan_travel.py`: redacted query-plan preview only
- `validate_suggestions.py`: structure checks only, not advice quality
- Other `scripts/*test*.py` files are release harnesses only

## OpenClaw

- Prefer heartbeat, task-end, failure-recovery, scheduled, or explicit user windows only after the semantic gate is true.
- Keep background execution redacted, quiet, rate-limited, and free of pending tool approvals.
- Do not let heartbeat or cron alone become the reason to seek help.

## Hermes

- Treat `find-community-help` as a progressive-disclosure skill.
- Do not load large reference files unless the skill is invoked.
- Prefer small-scope help retrieval by default.
- Keep temporary hints advisory-only and current-response scoped.

## OpenAI / Codex-style hosts

- Keep manual invocation available for operators who want a one-off community-help pass.
- Keep automatic model invocation disabled unless the host has an explicit safety wrapper around the delivery window.
- Prefer the same `public-only`, advisory-only, current-response flow used by the other adapters.
