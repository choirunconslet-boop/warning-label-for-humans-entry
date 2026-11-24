"""Warning Label for Humans — one-line entry.

Writes a single-line safety warning label for every human being to
/output/entry.txt. Pure stdlib, no I/O outside the output path.
"""

import os

LINE = (
    "WARNING: This human is 90% water, 10% coffee, "
    "and 100% convinced everyone else is the problem."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
