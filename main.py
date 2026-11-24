#!/usr/bin/env python3
"""fortune-cookie-01 entry: one funny fortune cookie message for an AI agent.

The fortune (105 characters, under the 140-character cap):

    Your horoscope says: Mercury is in retrograde, your servers are in
    Virginia, and your user is in a hurry.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

FORTUNE = (
    "Your horoscope says: Mercury is in retrograde, "
    "your servers are in Virginia, and your user is in a hurry."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
# Writing the fixed fortune string (never re-generated) is what makes
# the two grader runs produce identical bytes.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # The brief's own rules, enforced by the program itself: one line,
    # at most 140 characters. A fortune that broke either rule would
    # fail loudly here instead of shipping silently.
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars, cap is 140"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(FORTUNE + "\n", encoding="utf-8")
    print(f"Wrote {TARGET} ({len(FORTUNE)} characters)")


if __name__ == "__main__":
    main()
