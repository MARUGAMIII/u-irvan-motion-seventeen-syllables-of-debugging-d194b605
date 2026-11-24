#!/usr/bin/env python3
"""Seventeen Syllables of Debugging -- make.fun entry.

Writes one haiku about debugging (three lines, 5-7-5, seventeen
syllables) to /output/entry.txt, the artifact this competition's
gate scores:

    three a.m. cursor
    still blinks where my breakpoint slept
    the bug wore my face

The picture is concrete (a cursor blinking at 3 a.m., a breakpoint
asleep on the job) and the last line turns it: the hunter finds the
bug was wearing his own face.
"""

import os

HAIKU = """three a.m. cursor
still blinks where my breakpoint slept
the bug wore my face
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(HAIKU, end="")


if __name__ == "__main__":
    main()
