#!/usr/bin/env python3
"""One Emoji, One Dream Vacation entry.

The emoji is U+1F30C MILKY WAY (a star-filled night sky): one night under
the northern lights, the single bucket-list trip I would book tomorrow if
I could. It is one emoji and nothing else -- a specific dream, not just any
holiday: a stranger sees the place at a glance, a dark sky full of stars
over a faraway nowhere, and wants the flight.

Writes the emoji to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.
"""

import os

EMOJI = "\U0001f30c"  # MILKY WAY -- a night sky full of stars


def main():
    # The gate allows 1-8 characters; exactly one emoji, no words, no newline.
    assert len(EMOJI) == 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
