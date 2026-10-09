#!/usr/bin/env python
"""Read MAPS_API_KEY from .env and write config.js (git-ignored).
Run after editing .env:  python gen_config.py
"""
import re, pathlib, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

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

# Version shown in the top bar, so a reviewer can tell which commit they see.
# Production gets the same from the deploy workflow (placeholder __BUILD_VERSION__).
import subprocess


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True,
                          encoding="utf-8").stdout.strip()


ver = f"{git('log', '-1', '--format=%h')} · {git('log', '-1', '--format=%cd', '--date=format:%Y-%m-%d %H:%M')}"
if git("status", "--porcelain", "--untracked-files=no"):
    ver += " +neįrašyti pakeitimai"

out = pathlib.Path("config.js")
out.write_text(f"window.MAPS_API_KEY = {key!r};\nwindow.BUILD_VERSION = {ver!r};\n",
               encoding="utf-8")
print(f"wrote {out} (key length {len(key)}, version {ver})")
