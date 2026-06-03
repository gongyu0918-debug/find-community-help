# Host Adapters

Use this file when a host needs a minimal adapter policy for `find-community-help`.

## Shared Rule

- Treat `find-community-help` as an advisory help-retrieval skill for stuck active threads.
- Require at least one semantic trigger: no clear next step, stalled progress, repeated local attempts, suspected reinventing wheel, or explicit user request.
- Treat heartbeat, scheduled, task-end, and idle fallback as delivery windows only.
- Keep search tools `public-only` by default.
- Read the isolated suggestion channel only when the next task matches the fingerprint and TTL.

## OpenClaw

- Prefer heartbeat, task-end, failure-recovery, scheduled, or explicit user windows only after the semantic gate is true.
- Keep background execution redacted, quiet, rate-limited, and free of pending tool approvals.
- Do not let heartbeat or cron alone become the reason to seek help.

## Hermes

- Treat `find-community-help` as a progressive-disclosure skill.
- Do not load large reference files unless the skill is invoked.
- Prefer small-scope help retrieval by default.
- Keep all stored hints advisory-only.

## OpenAI / Codex-style hosts

- Keep manual invocation available for operators who want a one-off community-help pass.
- Keep automatic model invocation disabled unless the host has an explicit safety wrapper around the delivery window.
- Prefer the same `public-only`, advisory-only, next-relevant-turn flow used by the other adapters.
