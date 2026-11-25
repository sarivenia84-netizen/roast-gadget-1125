#!/usr/bin/env python3
"""Write a one-line roast to MAKEFUN_OUTPUT_DIR/entry.txt."""
import os

# ROAST — swap this line to change the entry; keep it 1-200 chars, one sentence.
ROAST = "Your smart scale says body age 23 — you're 31 and just ate pizza rolls at midnight"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ROAST)