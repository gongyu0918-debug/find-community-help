#!/usr/bin/env python3
"""Check duplicated skill entrypoint files stay in sync."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ENTRYPOINTS = [ROOT / "SKILL.md", ROOT / "SKILL.en.md"]


def main() -> int:
    first = ENTRYPOINTS[0].read_bytes()
    mismatched = [path.name for path in ENTRYPOINTS[1:] if path.read_bytes() != first]
    if mismatched:
        print(f"ERROR: {ENTRYPOINTS[0].name} differs from {', '.join(mismatched)}")
        return 1
    print("OK: skill entrypoints are in sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
