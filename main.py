#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.

Chosen placard (the sinking chair): an ordinary broken office chair
recast as a ritual throne whose slow descent enforces brevity in council.
Catalogue date (c. 2017), material (gas-lift steel) and donor (Facilities)
are inside the line itself, as the brief requires. Revision round 2:
v1 ended by explaining the joke ("so no speaker may hold the floor
forever"); v2 cuts the explanation and lands on the image instead —
"inch by inch, through any council that runs too long" — drier, and
every word earns its place.
"""

import os
import sys

ENTRY = (
    "Office chair, c. 2017, gas-lift steel, gift of Facilities: "
    "a throne that sinks its occupant, inch by inch, "
    "through any council that runs too long."
)

MAX_CHARS = 180


def main() -> int:
    text = ENTRY.strip()
    # Gate self-check, mirroring the sealed scorer:
    # UTF-8 text of 1 to 180 characters, not only white space.
    if not text:
        print("gate: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"gate: entry is {len(text)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    if text != text.strip():
        print("gate: entry has leading/trailing whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
