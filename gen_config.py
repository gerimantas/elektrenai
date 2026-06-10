#!/usr/bin/env python
"""Read MAPS_API_KEY from .env and write config.js (git-ignored).
Run after editing .env:  python gen_config.py
"""
import re, pathlib, sys

env = pathlib.Path(".env")
if not env.exists():
    sys.exit(".env not found. Copy .env.example to .env and add your key.")

key = None
for line in env.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line.startswith("#") or "=" not in line:
        continue
    k, v = line.split("=", 1)
    if k.strip() == "MAPS_API_KEY":
        key = v.strip()

if not key or key == "YOUR_KEY_HERE":
    sys.exit("MAPS_API_KEY not set in .env")

out = pathlib.Path("config.js")
out.write_text(f"window.MAPS_API_KEY = {key!r};\n", encoding="utf-8")
print(f"wrote {out} (key length {len(key)})")
