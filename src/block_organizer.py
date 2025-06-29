"""
Block Organizer: Inspect, group, and refactor UMG blocks by metadata (molt_type, tags, snap logic).
"""

import json
import pathlib
from collections import defaultdict

BLOCKS_DIR = pathlib.Path("blocks")

def scan_blocks():
    """
    Scans all .json files under /blocks and categorizes them by molt_type, snap_zone, etc.
    """
    summary = defaultdict(list)
    for path in BLOCKS_DIR.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            molt_type = data.get("molt_type", "UNKNOWN")
            category = data.get("category", "uncategorized")
            snap_zone = data.get("snap_config", {}).get("snap_zone", "none")
            fit_score = data.get("canto_overlay", {}).get("fit_score", 0)

            summary["by_molt_type"].append((molt_type, str(path)))
            summary["by_category"].append((category, str(path)))
            summary["by_snap_zone"].append((snap_zone, str(path)))
            summary["low_fit_score"].extend([str(path)] if fit_score < 0.85 else [])

        except Exception as e:
            summary["errors"].append(f"{path.name}: {str(e)}")

    return summary

if __name__ == "__main__":
    results = scan_blocks()
    for section, items in results.items():
        print(f"\\n🔹 {section.upper()}")
        for item in items:
            print("-", item)
