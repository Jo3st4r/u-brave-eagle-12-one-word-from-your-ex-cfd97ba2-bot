#!/usr/bin/env python3
"""One Word From Your Ex — the whole entry is a single word.

Writes exactly one word (1-24 chars, UTF-8, no spaces) to /output/entry.txt.

The word: Almost. The word an ex uses to describe you when the whole
relationship fits in a sigh. Almost the one. Almost enough. Almost stayed.
Three years that almost counted, and one word that says all of it — the
funniest, most painfully honest review a person can get, because the
entrant plainly knows it is true.
"""

import os

# --- the word ------------------------------------------------------------
WORD = "Almost"

MAX_CHARS = 24


def entry_text():
    """Return the single word the ex would use to describe you."""
    return WORD


def run_checks():
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 6, "expected 6 chars, got %d" % len(text)
    assert text == "Almost", "the word drifted: %r" % text
    assert text.encode("utf-8") == b"Almost", "bytes must be plain ASCII"
    return True


def validate(text):
    """The sealed scorer's gate: 1-24 chars, UTF-8, exactly one word."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if " " in text or "\t" in text:
        raise ValueError("entry must be exactly one word, no spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    run_checks()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
