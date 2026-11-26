"""Entry for make.fun's "The Best Meal You Ever Had" bounty.

Writes one sentence (at most 200 characters) to /output/entry.txt.
"""
import os

ENTRY = (
    "Cold pad see ew from a dented foil tray, eaten with my fingers in the "
    "hospital parking lot at 3 a.m., an hour after my daughter was born, "
    "was the best meal of my life."
)


MAX_CHARS = 200


def check(text: str) -> str:
    """Mirror the bounty's gate: 1 to 200 characters, not only white space."""
    text = text.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters, over {MAX_CHARS}")
    return text


def main() -> None:
    text = check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
