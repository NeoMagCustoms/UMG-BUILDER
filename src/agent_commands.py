# src/agent_commands.py

import os
import json
from datetime import datetime

def write_file(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ File written to {path}"
    except Exception as e:
        return f"❌ Failed to write file: {e}"

def generate_umg_block(block_id, label, molt_type, instruction, category="Custom", tags=None):
    if tags is None:
        tags = []

    block = {
        "block_id": block_id,
        "label": label,
        "category": category,
        "molt_type": molt_type,
        "tags": tags,
        "ledger": {
            "originator": "PoeGPT",
            "verified_by": "Mag",
            "created_at": datetime.utcnow().isoformat() + "Z",
            "edit_log": []
        },
        "instruction": instruction
    }

    path = f"memory/overlays/{block_id}.json"
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(block, f, indent=2)
        return f"✅ Block saved to {path}"
    except Exception as e:
        return f"❌ Failed to save block: {e}"
