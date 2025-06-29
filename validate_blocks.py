#!/usr/bin/env python3
"""
Light-weight schema sanity checker.
Scans blocks/ and memory/overlays/ for JSON files
and ensures each has a 'block_id' and 'molt_type'.
"""

import json, sys, pathlib

ERRORS = []
def check(path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            ERRORS.append(f"{path}: invalid JSON — {e}")
            return
    for key in ("block_id", "molt_type"):
        if key not in data:
            ERRORS.append(f"{path}: missing '{key}'")

root = pathlib.Path(".")
for folder in ("blocks", "memory/overlays"):
    for p in root.joinpath(folder).rglob("*.json"):
        check(p)

if ERRORS:
    print("❌ Block validation FAILED:")
    for e in ERRORS:
        print("  -", e)
    sys.exit(1)
print("✅ All blocks valid.")
