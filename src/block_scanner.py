"""
Block Scanner: Validates and reports on block structure and schema conformance.
"""

import json
import pathlib

TAXONOMY_PATH = pathlib.Path("data/block_taxonomy.json")
BLOCKS_DIR = pathlib.Path("blocks")

def load_taxonomy():
    if not TAXONOMY_PATH.exists():
        return {}, "❌ Taxonomy file missing."
    return json.loads(TAXONOMY_PATH.read_text(encoding="utf-8")), None

def scan_and_validate_blocks():
    taxonomy, error = load_taxonomy()
    if error:
        return [error]

    molt_types = set(taxonomy.get("molt_types", []))
    snap_zones = set(taxonomy.get("snap_zones", []))
    flags = set(taxonomy.get("runtime_behavior_flags", []))
    issues = []

    for path in BLOCKS_DIR.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            block_id = data.get("block_id", "<missing block_id>")
            mt = data.get("molt_type", "<missing molt_type>")
            if mt not in molt_types:
                issues.append(f"{block_id}: invalid molt_type '{mt}'")

            snap = data.get("snap_config", {}).get("snap_zone", None)
            if snap and snap not in snap_zones:
                issues.append(f"{block_id}: unknown snap_zone '{snap}'")

            rbf = data.get("runtime_behavior_flags", {})
            for flag in rbf:
                if flag not in flags:
                    issues.append(f"{block_id}: unrecognized behavior flag '{flag}'")

        except Exception as e:
            issues.append(f"{path.name}: JSON parse error – {str(e)}")

    return issues or ["✅ All blocks passed validation."]

if __name__ == "__main__":
    for line in scan_and_validate_blocks():
        print(line)
