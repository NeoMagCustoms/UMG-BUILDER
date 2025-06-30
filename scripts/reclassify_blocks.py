from pathlib import Path
import json

# Base paths
base_path = Path("data/blocks/Subject")
output_base = Path("data/blocks")

# Keywords and MOLT type mapping
molt_type_map = {
    "philosophy": "Philosophy",
    "instruction": "Instruction",
    "blueprint": "Blueprint",
    "trigger": "Trigger",
    "directive": "Directive",
    "merge": "Merge",
    "off": "Off",
}

default_molt_type = "Subject"

# Go through each block
for block_file in base_path.glob("block_*.json"):
    with open(block_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    label = data.get("label", "").lower()
    description = data.get("description", "").lower()
    combined = f"{label} {description}"

    assigned_type = default_molt_type
    for keyword, molt_type in molt_type_map.items():
        if keyword in combined:
            assigned_type = molt_type
            break

    # Ensure destination exists
    target_folder = output_base / assigned_type
    target_folder.mkdir(parents=True, exist_ok=True)

    # Write block into correct folder
    with open(target_folder / block_file.name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

print("✅ Block reclassification complete.")
