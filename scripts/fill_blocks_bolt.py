import os, json
from datetime import datetime

def append_provenance(block, action="fill_blocks"):
    if "ledger" not in block:
        block["ledger"] = {
            "originator": "Christopher L Haynes",
            "verified_by": "PoeUMG",
            "created_at": datetime.now().isoformat(),
            "edit_log": []
        }
    if "edit_log" not in block["ledger"]:
        block["ledger"]["edit_log"] = []
    block["ledger"]["edit_log"].append({
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "user": "Mag",
        "change": f"Filled block via Poe in Bolt"
    })
    return block

def fill_block_fields(block, category):
    label = block.get("label") or block.get("block_id", "").split("_", 1)[-1]
    if not block.get("label"):
        block["label"] = label.replace("_", " ").title()
    if not block.get("description"):
        block["description"] = f"A UMG block for {label.replace('_', ' ')}."
    if not block.get("category"):
        block["category"] = category.replace("_", " ").title()
    if not block.get("molt_type"):
        block["molt_type"] = "Subject"
    if not block.get("tags"):
        block["tags"] = list(set(label.lower().split("_") + ["umg", "builder", "ai", "block"]))
    if not block.get("cantocore"):
        block["cantocore"] = f"SUBJ:{label.upper()}"
    if not block.get("snap_config"):
        block["snap_config"] = {
            "snap_to": ["stack"],
            "fit_score": 100
        }

def fill_blocks():
    base_path = "data/blocks"
    updated = 0

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                block_path = os.path.join(root, file)
                category = os.path.basename(os.path.dirname(block_path))

                try:
                    with open(block_path, "r", encoding="utf-8") as f:
                        block = json.load(f)

                    fill_block_fields(block, category)
                    block = append_provenance(block)

                    with open(block_path, "w", encoding="utf-8") as f:
                        json.dump(block, f, indent=2)

                    print(f"✅ Filled: {block_path}")
                    updated += 1

                except Exception as e:
                    print(f"❌ Error in {block_path}: {e}")

    print(f"🧠 Poe filled {updated} blocks.")

# To run manually if needed:
if __name__ == "__main__":
    fill_blocks()
