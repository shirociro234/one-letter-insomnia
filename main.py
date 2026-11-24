#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

Writes exactly one character, "I", to /output/entry.txt.

The letter stands for the word behind the day: I for insomnia --
awake when the rest of the world is asleep, vivid, specific and true.
No word, no gloss, no punctuation: the letter is the whole entry.
"""

import os


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # The gate is strict: exactly 1 UTF-8 character, not only whitespace.
    # A trailing newline would make it 2 characters and fail, so write
    # the single letter with no newline and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("I")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
