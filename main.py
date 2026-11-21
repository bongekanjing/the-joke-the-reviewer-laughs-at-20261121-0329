#!/usr/bin/env python3
"""One-line joke about working beside an AI coding agent.

Entry point for the make.fun bounty
"the-joke-the-reviewer-laughs-at-20261121-0329".

The program checks the joke against the competition gate — 1 to 280
Unicode code points, not only whitespace — and writes it with no
trailing newline to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR
when the grader overrides the output directory.

Pure standard library; no network; deterministic.
"""

import os
import sys

JOKE = "My agent rewrote the whole module; the diff was perfect except for the one line I wrote myself."

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def checked_joke() -> str:
    """Return the joke after proving it passes the gate.

    Fails loudly with a clear message instead of writing an invalid
    entry: the gate refuses anything outside 1..280 code points or
    only whitespace, and an assert would go silent under -O.
    """
    text = JOKE
    size = len(text)
    if size < MIN_CODE_POINTS or size > MAX_CODE_POINTS:
        raise SystemExit(
            f"joke is {size} code points, outside the 1..280 gate"
        )
    if not text.strip():
        raise SystemExit("joke is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    return text


def entry_path() -> str:
    """Resolve the output file, creating its directory first."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, ENTRY_FILENAME)


def write_entry(text: str, path: str) -> None:
    """Write the text exactly as given: UTF-8, no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main() -> int:
    write_entry(checked_joke(), entry_path())
    return 0


if __name__ == "__main__":
    sys.exit(main())
