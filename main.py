#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

Competition: u-kreutzx-the-funniest-out-of-office-054815cf
("The Funniest Out-of-Office").

The gate allows UTF-8 text of 1 to 140 characters, not only whitespace,
so the program writes one fixed line of 136 characters and nothing else:
no trailing newline, no second line, no link, no image.

The entry is deterministic: the same line on every run, with no input,
no network and no randomness. The OUTPUT_DIR environment variable only
exists so the program can be exercised locally; the grader runs it with
the default /output.
"""

import os

LINE = "I'm on holiday. My inbox is being looked after by my houseplants, who have no thumbs, no Wi-Fi, and strong opinions about your deadline."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line must not be empty")
    if len(line) > 140:
        raise SystemExit(f"entry line is {len(line)} characters, over the 140 cap")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
