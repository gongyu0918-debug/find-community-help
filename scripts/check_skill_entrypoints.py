#!/usr/bin/env python3
"""Check the skill entrypoint exists and has required frontmatter."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REQUIRED_KEYS = ("name:", "description:", "version:", "license:")
FORBIDDEN_DUPES = (ROOT / "SKILL.en.md",)


def main() -> int:
    if not SKILL.is_file():
        print(f"ERROR: missing {SKILL.name}")
        return 1
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print("ERROR: SKILL.md must start with YAML frontmatter")
        return 1
    end = text.find("\n---", 3)
    if end < 0:
        print("ERROR: SKILL.md frontmatter is not closed")
        return 1
    front = text[3:end]
    missing = [key for key in REQUIRED_KEYS if key not in front]
    if missing:
        print(f"ERROR: SKILL.md missing frontmatter keys: {', '.join(missing)}")
        return 1
    version = re.search(r"(?m)^version:\s*(\S+)\s*$", front)
    if not version:
        print("ERROR: SKILL.md version field is empty")
        return 1
    leftover = [path.name for path in FORBIDDEN_DUPES if path.exists()]
    if leftover:
        print(f"ERROR: remove duplicate entrypoints: {', '.join(leftover)}")
        return 1
    print(f"OK: skill entrypoint ready (version {version.group(1)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
