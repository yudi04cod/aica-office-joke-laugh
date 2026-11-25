#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line joke about office life to /output/entry.txt.
Stdlib only, no network, deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "My job title is 'team player' because 'the one who does "
    "everyone else's work' wouldn't fit on the badge."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "the joke must be a single line"
    assert 1 <= len(text) <= 200, "the joke must be 1-200 characters"
    assert text.strip(), "the joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
