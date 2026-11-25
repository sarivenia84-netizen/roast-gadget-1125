#!/usr/bin/env python3
import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

roast = "Your smart scale says body age 23 — you're 31 and just ate pizza rolls at midnight"

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(roast)