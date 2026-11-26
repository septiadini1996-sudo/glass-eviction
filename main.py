"""Eviction Notice — the one sentence a house cat says in its own defence
after knocking a glass off the table.

Writes the sentence to /output/entry.txt (the sandbox output path),
falling back to ./output/entry.txt for local runs.
"""

import os

SENTENCE = (
    "The glass spent all morning squatting in my sunbeam, "
    "so I evicted it to the floor, where cold things live."
)


def main() -> None:
    for candidate in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(candidate) or ".", exist_ok=True)
            with open(candidate, "w", encoding="utf-8") as f:
                f.write(SENTENCE)
            print(SENTENCE)
            print(f"characters: {len(SENTENCE)}")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to any output path")


if __name__ == "__main__":
    main()
