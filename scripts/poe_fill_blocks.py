import os, json
from pathlib import Path
from datetime import datetime

BLOCKS_ROOT = Path("data/blocks")
REQUIRED_FIELDS = ["block_id", "label", "description", "molt_type", "ledger"]

TEMPLATE = {
    "category": "AutoFilled",
    "tags": [],
    "cantocore": "",
    "snap_config": {
        "snap_to": ["stack"],
        "fit_score": 100
    },
    "merge_logic": {},
    "display": {},
    "code_modules": [],
    "runtime_behavior_flags": {},
    "agent_orchestration": {},
    "integration_layer": {},
    "future_extensions": [],
    "example_block_data": {},
    "ledger": {
        "originator": "Christopher L Haynes",
        "verified_by": "PoeUMG",
        "created_at": datetime.now().isoformat(),
        "edit_log": []
    }
}

def fill_template(block):
    for key, default in TEMPLATE.items():
        if key not in block:
            block[key] = default
    return block

def is_valid_block(block):
    return all(field in block for field in REQUIRED_FIELDS)

def normalize_block_file(file_path):
    with open(file_path, 'r') as f:
        block = json.load(f)

    changed = False

    # Fill missing fields
    original = block.copy()
    block = fill_template(block)
    if not is_valid_block(block):
        print(f"⚠️  Incomplete block: {file_path}")
    if block != original:
        changed = True

    # Rewrite file if changed
    if changed:
        with open(file_path, 'w') as f:
            json.dump(block, f, indent=2)
        print(f"✅ Updated: {file_path}")

def normalize_all_blocks():
    for folder in BLOCKS_ROOT.iterdir():
        if not folder.is_dir(): continue
        for file in folder.glob("*.json"):
            normalize_block_file(file)

if __name__ == "__main__":
    normalize_all_blocks()
