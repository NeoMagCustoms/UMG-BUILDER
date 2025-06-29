#!/usr/bin/env python3
"""
Bulk-import all JSON blocks from `archive_blocks/` (or any given folder)
into `memory/overlays/`, stamping each ledger with 'imported_from'.
Run once after extracting Citadel-v2 zip.
"""

import json, shutil, pathlib, datetime, sys, textwrap

SRC_DIR  = pathlib.Path("archive_blocks")          # adjust if different
DEST_DIR = pathlib.Path("memory/overlays")
DEST_DIR.mkdir(parents=True, exist_ok=True)

count = 0
for p in SRC_DIR.rglob("*.json"):
    dest = DEST_DIR / p.name
    # 1️⃣ copy file
    shutil.copyfile(p, dest)
    # 2️⃣ stamp provenance
    data = json.loads(dest.read_text(encoding="utf-8"))
    ledger = data.setdefault("ledger", {})
    ledger.setdefault("originator", "Citadelv2-Import")
    ledger.setdefault("verified_by", "PoeUMG")
    ledger.setdefault("created_at", datetime.datetime.utcnow().isoformat())
    prov   = ledger.setdefault("provenance", [])
    prov.append({
        "timestamp": ledger["created_at"],
        "action": "bulk_import",
        "note": f"Imported from {p.relative_to(SRC_DIR)}"
    })
    dest.write_text(textwrap.indent(json.dumps(data, indent=2), ""), encoding="utf-8")
    count += 1

print(f"✅ Imported {count} blocks to {DEST_DIR}")
