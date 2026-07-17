# Project notes

Markdown-only maintenance skill. Goal: small surface, clear triggers, no runtime.

## Keep

- `SKILL.md` + five `references/*.md`
- MIT license consistency
- `user-invocable: true`, `disable-model-invocation: true`
- advisory / current-response boundaries
- legacy `agent-travel` marker acceptance note only

## Do not reintroduce

- scripts, fixtures, smoke harnesses as product surface
- durable memory / next-turn hint transport
- broad research / browsing tool behavior
- host state machine as required agent API

## Release

1. Edit Markdown only
2. Bump `version` in `SKILL.md` and README
3. Commit + tag
4. `clawhub skill publish . --version <ver> ...`
5. Optional SkillHub.cn via `skillhub-upload`
