#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes exactly one sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt.

Deterministic: the same fixed sentence is written on every run, with no
randomness, no network access and no input read from anywhere.
"""

import os
import sys

PITCH = (
    "A shower curtain that, the moment it clings to your wet skin, "
    "puffs itself into a rigid little tent with a built-in fan and "
    "stays inflated until the water stops."
)


def main() -> int:
    # Output directory: /output by default (the sandbox output directory).
    # An optional first argument overrides it, so the entry can be verified
    # locally into a separate directory without touching /output.
    output_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
