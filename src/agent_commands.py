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

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"❌ Failed to read file: {e}"

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
        os.makedirs("memory/overlays", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(block, f, indent=2)
        return f"✅ Block saved to {path}"
    except Exception as e:
        return f"❌ Failed to save block: {e}"

def log_block(filename, block):
    os.makedirs("memory/logs", exist_ok=True)
    path = f"memory/logs/{filename}"
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(block, f, indent=2)
        return f"📓 Block logged to {path}"
    except Exception as e:
        return f"❌ Failed to log block: {e}"
