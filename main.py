"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message for a bug fix that made everything worse
to /output/entry.txt.
"""

import os

ENTRY = "fix: the button that did nothing now deletes your account on click"


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-100 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 100:
        raise ValueError("entry must be at most 100 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
