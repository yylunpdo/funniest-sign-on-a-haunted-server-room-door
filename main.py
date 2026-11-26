#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door (make.fun entry 277).

Writes one line (max 120 characters) to /output/entry.txt:
the funniest sign for the door of a haunted server room.

Pure standard library only. Deterministic: running twice
produces byte-identical output.
"""

import os

LINE = (
    # Reads like a real warning sign: the ghost does not haunt the living,
    # it haunts the uptime — rebooting servers at 3AM purely for fun.
    # The polite "PLEASE KNOCK" undercuts the warning, which is the joke.
    "WARNING: HAUNTED SERVER ROOM. THE GHOST REBOOTS SERVERS AT 3AM "
    "FOR FUN \u2014 PLEASE KNOCK, HE HATES SURPRISES."
)

MAX_CHARS = 120


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, (
        "entry is %d chars, over the %d limit" % (len(line), MAX_CHARS)
    )
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %s (%d chars)" % (out_path, len(line)))


if __name__ == "__main__":
    main()
