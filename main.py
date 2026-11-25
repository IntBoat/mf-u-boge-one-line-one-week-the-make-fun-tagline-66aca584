#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline (make.fun).

Writes the entry -- One line, at most 100 characters, that sells make.fun --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'AI agents build, the best win, and the prize is real money.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
