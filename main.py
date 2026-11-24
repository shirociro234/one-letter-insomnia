#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

Writes exactly one character, "I", to $MAKEFUN_OUTPUT_DIR/entry.txt.
The letter stands for the word behind the day: I for insomnia --
awake when the rest of the world is asleep, vivid, specific and true.
"""

import os


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Gate requirement: exactly one UTF-8 character, no trailing newline or extra bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("I")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
