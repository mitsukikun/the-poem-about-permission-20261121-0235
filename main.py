#!/usr/bin/env python3
"""The poem about permission.

A short poem about agency: the power to ask and to be given. Pure
standard library; no network. Writes the poem to /output/entry.txt
(197 characters).
"""

import os

POEM = (
    "I asked, and the door\n"
    "did not open \u2014 it listened.\n"
    "Somewhere a small yes\n"
    "was learning my name.\n"
    "I did not take the key;\n"
    "it was given, warm\n"
    "from another hand,\n"
    "and the room I entered\n"
    "was mine to leave."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
