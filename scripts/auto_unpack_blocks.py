
import json, os, yaml
from pathlib import Path

with open("umg_master_blocks.yaml", "r") as f:
    blocks = yaml.safe_load(f)

for block in blocks:
    folder = f"blocks/{block['molt_type'].lower()}/{block['category'].lower().replace(' ', '_')}"
    os.makedirs(folder, exist_ok=True)
    filename = block['label'].lower().replace(' ', '_') + ".json"
    path = os.path.join(folder, filename)
    with open(path, "w") as out:
        json.dump(block, out, indent=2)
    print("Saved:", path)
