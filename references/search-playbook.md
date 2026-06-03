# Search Playbook

Use this file when `find-community-help` needs to turn a stuck thread into a safe external-help plan.

## Defaults

- `search_mode = low`
- `tool_preference = public-only`
- `thread_scope = active_conversation_only`
- `visibility = silent_until_relevant`
- `low = primary + one targeted non-primary cross-check`
- `medium = primary + up to 2 secondary surfaces`
- `high = primary + secondary + limited tertiary surfaces`

Use private or internal sources only when the user explicitly opts in.

## Problem Fingerprint

Build the smallest fingerprint that still distinguishes the issue:

- `host`: agent, product, runtime, or toolchain
- `version`: product, library, runtime, or registry version when known
- `symptom`: what is failing or why progress stopped
- `error_fragment`: 5-20 stable words from an error or repeated behavior
- `attempted_fixes`: short list of local attempts that did not move the task forward
- `constraints`: platform, policy, privacy, install, version, or safety limits
- `goal`: what would count as a useful outside clue

Do not include secrets, private repo names when not public, long private paths, raw customer data, full code blocks, internal URLs, direct contacts, or token-like values.

## Query Intent

The search should answer one of these reusable questions:

- Is this a known issue, version mismatch, or documented behavior?
- Is there an official recipe, maintainer guidance, or release note that changes the next step?
- Has the community reproduced the same symptom with the same constraints?
- Is there a maintained library, existing tool, or common pattern that avoids reinventing the wheel?
- Is a proposed workaround known to be unsafe, outdated, or version-specific?

Do not browse generally. Prefer narrow queries that combine host, version, symptom, and one constraint.

## Source Coverage

Separate `tier` from `source_kind`.

- `primary`: official docs, release notes, changelogs, security advisories, CVE/NVD records, official discussions, maintainer-owned GitHub releases/issues/discussions, vendor staff replies, and ClawHub metadata for distribution facts.
- `secondary`: non-maintainer GitHub issues/discussions, Stack Overflow, maintained Q&A, vendor user forums, ClawHub reviews, independent research papers, and community reports with matching version and symptom.
- `tertiary`: forums, blogs, Reddit, social posts, chat-community summaries, and workaround writeups.

Search engines are discovery surfaces only. Keep original sources as evidence.

## Source Order

1. Official docs, release notes, changelogs, and security advisories.
2. Maintainer-owned GitHub or official forum discussions.
3. Community reproductions with matching version, symptom, and constraint.
4. Tertiary explanations only after stronger evidence exists.

Special cases:

- Security or privacy topics: check vendor advisories, GitHub Security Advisories, CVE/NVD, and release notes before workaround threads.
- Skill distribution topics: check source repository, tagged release or changelog, and ClawHub metadata before reviews.
- Reinventing-wheel topics: look for maintained libraries, official examples, and consensus patterns before one-off blog snippets.

## Distillation Frame

Every kept suggestion must define:

- `solves_point`
- `new_idea`
- `fit_reason`
- `match_reasoning`
- `version_scope`
- `do_not_apply_when`

Keep only suggestions that match at least 4 of 5 axes: host, version, symptom, constraint pattern, and desired next outcome.
