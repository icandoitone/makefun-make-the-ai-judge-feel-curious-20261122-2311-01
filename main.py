#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

Deterministic: no randomness, no network, no timestamps.
"""

import os

ENTRY = (
    "The drawer in my grandmother's kitchen had a false bottom. "
    "Inside was a letter addressed to me, in my own handwriting, "
    "dated three years before I was born. I have never opened it — "
    "but every visit I still lift the drawer to check it is "
    "still there, still sealed, still waiting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
