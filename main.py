#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

One robot makes awkward small talk to another robot while they ride
an elevator together. The line is written to ``entry.txt`` inside the
directory named by ``MAKEFUN_OUTPUT_DIR`` (then ``/output``).

The entry is a single line of UTF-8 text, 1-200 characters, with no
network access, no randomness and no clock: running it twice produces
byte-identical output.
"""

import os
import sys

LINE = (
    "My battery is at 98%. Yours? Sorry. That was invasive. "
    "I will now stare at the floor numbers with you."
)


def output_dir():
    """Resolve the output directory, honouring MAKEFUN_OUTPUT_DIR first."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print("entry line must be 1-200 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # Read it back: the file on disk must hold exactly the line we wrote.
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != text + "\n":
        print("entry.txt round-trip mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
