from pathlib import Path
import json

# Define valid molt types
valid_types = {
    "Primary", "Subject", "Instruction", "Philosophy", "Trigger", "Directive",
    "Blueprint", "Merge", "Off"
}

# Path to blocks
base = Path("data/blocks")
errors = []

for molt_type_folder in base.iterdir():
    if molt_type_folder.name not in valid_types:
        continue

    for block_path in molt_type_folder.glob("block_*.json"):
        with open(block_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                errors.append((block_path.name, "❌ Invalid JSON"))
                continue

            # Check molt_type matches folder
            if data.get("molt_type") != molt_type_folder.name:
                errors.append((block_path.name, "❌ MOLT type mismatch"))

            # Check ledger
            ledger = data.get("ledger", {})
            if not ledger.get("originator") or not ledger.get("verified_by"):
                errors.append((block_path.name, "❌ Missing ledger fields"))

            # Check snap_config
            snap = data.get("snap_config", {})
            if "snap_to" not in snap or "priority" not in snap:
                errors.append((block_path.name, "❌ Missing snap_config"))

            # Tags, overlay
            if not data.get("tags") or not data.get("canto_overlay"):
                errors.append((block_path.name, "❌ Missing tags or canto_overlay"))

print("\n🔍 Audit Results:")
if not errors:
    print("✅ All blocks passed inspection.")
else:
    for blk, err in errors:
        print(f"{err} → {blk}")
    print(f"\n⚠️ {len(errors)} issues found.")
