#!/usr/bin/env python3
"""Midnight Fridge Roast — one-line roast of a smart fridge that refuses
to open after midnight. Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure stdlib."""

import os

# v3 (final): "locked me out" puts the refusal on the person at the door,
# and "cold box of leftovers" tightens the rhythm. One joke, one turn.
ROAST = (
    "My fridge locked me out at midnight like a bouncer \u2014 mate, "
    "you're a cold box of leftovers, not a nightclub door."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
