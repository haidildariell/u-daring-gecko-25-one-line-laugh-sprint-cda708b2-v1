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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
