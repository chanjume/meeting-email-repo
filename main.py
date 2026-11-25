#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one single-line joke to /output/entry.txt.
The joke: the host shares their screen, opens the email, and reads it
aloud to the very people the email was already sent to.
"""

import os

ENTRY = "The host shared their screen, opened the email, and read it aloud \u2014 to the same people the email was sent to."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
