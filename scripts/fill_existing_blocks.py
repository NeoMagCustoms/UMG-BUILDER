import os, json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("data/blocks")

def infer_description(label):
    return f"A UMG block for {label.replace('_', ' ').capitalize()}."

def infer_tags(label):
    return list(set(label.lower().split('_') + ["umg", "ai", "builder", "block"]))

def infer_cantocore(label, molt_type):
    return f"{molt_type[:4].upper()}:{label.upper()}"

def fill_block_fields(block, file_path, category):
    changed = False

    if not block.get("label"):
        block["label"] = block["block_id"].split("_", 1)[-1].replace("_", " ").title()
        changed = True

    if not block.get("description"):
        block["description"] = infer_description(block["label"])
        changed = True

    if not block.get("category"):
        block["category"] = category.replace("_", " ").title()
        changed = True

    if not block.get("molt_type"):
        block["molt_type"] = "Subject"
        changed = True

    if not block.get("tags"):
        block["tags"] = infer_tags(block["block_id"])
        changed = True

    if not block.get("cantocore"):
        block["cantocore"] = infer_cantocore(block["block_id"], block["molt_type"])
        changed = True

    if not block.get("ledger"):
        block["ledger"] = {
            "originator": "Christopher L Haynes",
            "verified_by": "PoeUMG",
            "created_at": datetime.now().isoformat(),
            "edit_log": []
        }
        changed = True

    if not block.get("snap_config"):
        block["snap_config"] = {
            "snap_to": ["stack"],
            "fit_score": 100
        }
        changed = True

    if changed:
        with open(file_path, "w") as f:
            json.dump(block, f, indent=2)
        print(f"✅ Updated: {file_path}")

def run_fill():
    for molt_type_folder in BASE_DIR.iterdir():
        if not molt_type_folder.is_dir(): continue

        for category_folder in molt_type_folder.iterdir():
            if not category_folder.is_dir(): continue

            category = category_folder.name

            for block_file in category_folder.glob("*.json"):
                with open(block_file, "r") as f:
                    block = json.load(f)

                fill_block_fields(block, block_file, category)

if __name__ == "__main__":
    run_fill()
