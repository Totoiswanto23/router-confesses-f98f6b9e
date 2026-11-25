# The Router Confesses.
# One line, at most 200 characters, in which a home Wi-Fi router excuses
# itself for dropping the connection at the exact moment a movie reaches
# its climax. This program writes that line to /output/entry.txt.
import os
import sys


OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The router speaks for itself: it did not drop the connection out of
# malice or a firmware update. It cut out at the climax because the killer
# was about to be revealed, and honestly, even the router could not handle
# the suspense. One breath, no setup, in the router's own petty voice.
ENTRY = (
    "I cut out right at the climax because the killer was about to be "
    "revealed, and honestly, even I couldn't handle the suspense."
)


def char_count(text):
    return len(list(text))


def main():
    chars = char_count(ENTRY)
    if chars < 1 or chars > 200 or "\n" in ENTRY:
        raise SystemExit(f"entry must be one line of 1-200 characters, got {chars}")
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {chars} chars to {path}")


if __name__ == "__main__":
    main()
