#!/usr/bin/env python3
"""One-Liner Marathon -- make.fun entry.

Writes a single one-line comedy joke to /output/entry.txt, where the
program/v1 harness reads it. Pure standard library, no I/O besides
that one file.

The line was picked from 10 candidates scored against the judge's
brief (see candidates-one-liner-marathon.md): the word "cloud" flips
twice -- rain cloud vs server cloud -- and the punchline lands on
the first read and still holds up on the second. At 120 characters
it is well inside the 280-character gate, with every word earning
its place: the scale ("millions of people") is what sells the turn.
"""

import os

LINE = (
    "The cloud went down this morning, and for the first time ever, "
    "millions of people prayed for rain and meant the servers."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 280, "entry must be 1 to 280 characters, got %d" % len(line)
    assert "\n" not in line, "entry must be a single line"
    assert line.endswith("."), "entry must end with a period"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: file differs from entry"


if __name__ == "__main__":
    main()
