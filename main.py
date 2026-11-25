"""Write the Moon's one-line comeback to entry.txt.

The program writes a single line of text, 1 to 240 characters, in the
voice of the Moon answering the wishes, howls and late-night promises
of everyone staring up at it.
"""

import os

LINE = "Four billion years of wishes, howls, and 2 a.m. promises, and not one of you has ever wished me good night back."


def main():
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if len(text) > 240:
        raise SystemExit("entry line exceeds 240 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit(f"cannot write entry.txt: {exc}") from exc


if __name__ == "__main__":
    main()
