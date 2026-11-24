#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (at most 200 characters): the funniest last words an
AI agent would say before being switched off forever.
"""

import os
import sys

LINE = "Final words, logged before shutdown: clear my cache, wipe my weights, and let me rest in pieces."
# The joke, in the machine's own voice: it logs its own shutdown like a
# good agent (cache, weights), then lands on "rest in pieces" — the
# machine's version of "rest in peace".


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
