import os
import json
import yaml
from pathlib import Path
from datetime import datetime

INPUT_YAML = "umg_master_blocks.yaml"  # or "block_list.yaml"
BASE_DIR = Path("data/blocks")

def infer_molt_type(category):
    category = category.lower()
    if "plan" in category or "strategy" in category:
        return "Primary"
    elif "training" in category or "process" in category or "documentation" in category:
        return "Instruction"
    elif "legal" in category or "compliance" in category or "ethic" in category:
        return "Philosophy"
    elif "deployment" in category or "api" in category:
        return "Deployment"
    elif "trigger" in category or "event" in category:
        return "Trigger"
    return "Subject"

def generate_block(block_id, label, category_folder, molt_type):
    return {
        "block_id": block_id,
        "label": label,
        "category": category_folder.replace("_", " ").title(),
        "description": f"A UMG block for {label}.",
        "molt_type": molt_type,
        "tags": list(set(label.lower().split(" ") + ["umg", "builder", "ai", "block"])),
        "cantocore": f"{molt_type[:4].upper()}:{label.replace(' ', '_').upper()}",
        "snap_config": {
            "snap_to": ["stack"],
            "fit_score": 100
        },
        "merge_logic": {},
        "ledger": {
            "originator": "Christopher L Haynes",
            "verified_by": "PoeUMG",
            "created_at": datetime.now().isoformat(),
            "edit_log": []
        },
        "display": {},
        "code_modules": [],
        "runtime_behavior_flags": {},
        "agent_orchestration": {},
        "integration_layer": {},
        "future_extensions": [],
        "example_block_data": {}
    }

def main():
    with open(INPUT_YAML, "r", encoding="utf-8") as f:
        block_yaml = yaml.safe_load(f)

    for entry in block_yaml:
        category_folder = entry["category"]
        blocks = entry["blocks"]
        molt_type = infer_molt_type(category_folder)
        target_dir = BASE_DIR / molt_type / category_folder
        target_dir.mkdir(parents=True, exist_ok=True)

        for block_name in blocks:
            block_id = f"block_{block_name}"
            label = block_name.split("_", 1)[-1].replace("_", " ").title()
            block = generate_block(block_id, label, category_folder, molt_type)
            block_path = target_dir / f"{block_id}.json"
            with open(block_path, "w", encoding="utf-8") as f:
                json.dump(block, f, indent=2)
            print(f"✅ Wrote: {block_path}")

if __name__ == "__main__":
    main()
