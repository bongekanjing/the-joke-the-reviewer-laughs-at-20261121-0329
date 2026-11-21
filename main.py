#!/usr/bin/env python3
"""One-line joke about working beside an AI coding agent.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure standard library; no network; deterministic.
"""

import os

JOKE = "My agent rewrote the whole module; the diff was perfect except for the one line I wrote myself."


def output_path() -> str:
    """Where the entry goes: the grader's /output, or an override dir."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    # The gate refuses anything outside 1..280 code points or only
    # whitespace, so fail loudly here instead of emitting an invalid entry.
    assert 1 <= len(JOKE) <= 280, "joke outside the 1..280 gate"
    assert JOKE.strip(), "joke is only whitespace"
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
