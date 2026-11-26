"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

This entry writes a single sentence about a childhood memory:
running barefoot after school to a grandmother's kitchen, where
the smell of rice and fried shallots hung in the warm air and she
always saved the crispiest edge of the egg, still sizzling, before
anyone else sat down. That small, honest detail — being waited for
and fed first — is what leaves the warm ache lingering afterwards.
"""

import os

TEXT = (
    "After school I would run barefoot to Grandma's kitchen, where the "
    "smell of rice and fried shallots hung in the warm air and she always "
    "saved me the crispiest edge of the egg, still sizzling, before "
    "anyone else sat down."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
