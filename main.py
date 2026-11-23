"""One-Line Laugh Sprint entry.

Writes a single original one-liner about everyday life to
/output/entry.txt. Deterministic: the same line, byte for byte,
on every run.
"""

import os

LINE = (
    "I meal-prepped for the week on Sunday, then ordered takeout "
    "on Monday out of respect for tradition."
)


def main() -> None:
    # Fail loudly instead of submitting an invalid entry: the gate
    # only accepts UTF-8 text of 1-200 characters.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
