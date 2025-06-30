import os, json
from datetime import datetime
from pathlib import Path

# Define full list
BLOCK_LIST = [
    ("CATEGORY_01_BUSINESS_PLANS", "001_startup_plan"),
    ("CATEGORY_01_BUSINESS_PLANS", "002_lean_plan"),
    ("CATEGORY_01_BUSINESS_PLANS", "003_strategic_plan"),
    # (Add your full list here or paste later)
]

def create_block_file(category, block_name):
    block_id = f"block_{block_name}"
    label = block_name.split("_", 1)[-1].replace("_", " ").title()
    path = Path(f"data/blocks/Subject/{category}")
    path.mkdir(parents=True, exist_ok=True)
    block = {
        "block_id": block_id,
        "label": label,
        "category": category.replace("_", " ").title(),
        "description": f"A UMG block for {label}.",
        "molt_type": "Subject",
        "tags": list(set(label.lower().split(" ") + ["umg", "builder", "block", "ai"])),
        "cantocore": f"SUBJ:{label.replace(' ', '_').upper()}",
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
    with open(path / f"{block_id}.json", "w", encoding="utf-8") as f:
        json.dump(block, f, indent=2)
    print(f"✅ {path / f'{block_id}.json'}")

def run():
    for category, block_name in BLOCK_LIST:
        create_block_file(category, block_name)

if __name__ == "__main__":
    run()
