# Trigger Policy

Use this file when `find-community-help` needs to decide whether the agent should seek outside help.

## Semantic Trigger Matrix

At least one semantic signal must be present. Delivery windows alone are never enough.

| Signal | State field | Use when | Default mode |
| --- | --- | --- | --- |
| No clear next step | `no_clear_next_step` or legacy `unresolved_blocker_count >= 1` | Local inspection has not produced a plausible next action. | `low` |
| Progress stalled | `progress_stalled` or legacy `user_corrections >= 2` | The task is not moving despite reasonable local work. | `medium` |
| Repeated local attempts | `repeated_local_attempts >= 2`, `attempted_fixes_count >= 2`, or legacy `related_failures >= 2` | The agent is looping over the same failure or fix path. | `medium` |
| Reinventing-wheel risk | `suspected_reinventing_wheel` | A maintained library, official recipe, known issue, or community pattern may already exist. | `low` |
| User-requested community help | `user_requested_community_help` or legacy `user_explicit_search_request` | The user asks for community experience, known bugs, mature approaches, or outside examples. | `medium` |
| User-requested deep help | `user_requested_deep_community_help` or legacy `user_explicit_deep_research_request` | The user asks for a broader external pass. | `high` |
| Version mismatch | `version_mismatch_seen` | Current docs or package behavior may differ from the model's memory. | `low` |

## Delivery Windows

These values describe how a host invokes the skill; they do not trigger the skill by themselves.

- `user_request` or `manual_request`: explicit user request; skip quiet timing gates, still redact and scope the search.
- `failure_recovery`: automatic recovery path; requires a semantic signal.
- `task_end`: task-end retrospective; requires a semantic signal.
- `heartbeat`: host background wakeup; requires a semantic signal and quiet gates.
- `scheduled`: host-managed or user-configured periodic check; requires scheduled ownership, neutral host-generated prompts, and a semantic signal.
- `idle_fallback`: only when heartbeat is unavailable or explicitly enabled; requires a semantic signal.

## Automatic Safety Gates

For all automatic delivery windows, run only when all of these are true:

- no user operation in progress
- no agent response in progress
- no tool approval pending
- active conversation within `24h`
- run limits have not been reached

Default limits:

- `active_conversation_window = 24h`
- `quiet_after_user_action = 20m`
- `quiet_after_agent_action = 5m`
- `repeat_fingerprint_cooldown = 12h`
- `max_runs_per_thread_per_day = 1`
- `max_runs_per_user_per_day = 3`

Repeated runs with the same fingerprint should stay quiet until the cooldown elapses. A new semantic signal may bypass the cooldown when it adds useful evidence, such as a repeated failure after the previous hint.

## Scheduled Prompt Policy

For `scheduled` triggers, distinguish manual prompts from host-generated prompts:

- A host-managed scheduled run is valid only when the host states ownership explicitly.
- A user-configured periodic run is valid only when the user opted in.
- Manual scheduled prompts may preserve the operator's wording.
- Host-generated scheduled prompts must stay neutral and workflow-derived from logs, backlog items, docs drift, or other task facts.
