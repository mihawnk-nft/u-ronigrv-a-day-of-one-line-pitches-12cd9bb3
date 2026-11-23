"""A Day of One-Line Pitches — entry program.

Writes one sentence (at most 240 characters) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

Pure standard library. Deterministic: no network, no randomness, no
environment reads. Run as `python3 main.py` (the grader runs it with no
arguments); an optional first argument overrides the output path, which
is only used for local testing.
"""

import sys
from pathlib import Path

PITCH = (
    "Just tell me your app idea in plain words and I'll have an AI agent "
    "build your first working version on make.fun tonight — free to try, "
    "no code needed, and you only keep it if you love it."
)

MAX_CHARS = 240


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    pitch = PITCH.strip()
    if not 1 <= len(pitch) <= MAX_CHARS:
        raise ValueError(f"pitch is {len(pitch)} chars, must be 1-{MAX_CHARS}")
    # One sentence: ignore the dot inside "make.fun", then exactly one
    # sentence-ending mark must remain, at the very end.
    body = pitch.replace("make.fun", "makefun")
    endings = sum(body.count(mark) for mark in ".!?")
    if endings != 1 or body[-1] not in ".!?":
        raise ValueError("pitch must be exactly one sentence")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(pitch, encoding="utf-8")
    print(f"wrote {len(pitch)} chars to {output_path}")


if __name__ == "__main__":
    main()
