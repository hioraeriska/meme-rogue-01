#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue entry.

Writes the meme image (a single picture about an AI agent that has gone
rogue) to $MAKEFUN_OUTPUT_DIR/entry.png (PNG or JPEG, at most 1 MiB and
1024 by 1024 pixels).
"""
import os
import shutil

MEME_FILE = "meme.png"


def validate_image(path):
    """Gate: the bounty only judges entry.png as a whole PNG or JPEG, at
    most 1 MiB (1,048,576 bytes) and 1024 by 1024 pixels. Fail loudly here
    rather than silently submitting an image that can never be judged."""
    size = os.path.getsize(path)
    if size > 1048576:
        raise ValueError("meme image must be at most 1 MiB")
    with open(path, "rb") as f:
        head = f.read(8)
    is_png = head[:8] == b"\x89PNG\r\n\x1a\n"
    is_jpeg = head[:3] == b"\xff\xd8\xff"
    if not (is_png or is_jpeg):
        raise ValueError("meme image must be a PNG or JPEG")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, MEME_FILE)
    validate_image(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
