# src/agent_commands.py

import os
import json
from datetime import datetime
from src.umg_cognition import validate_umg_block, describe_umg_block
from src.cpf_cognition import validate_cpf_block

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

def list_blocks(dir="memory/overlays"):
    table = []
    try:
        files = os.listdir(dir)
        for f in files:
            if not f.endswith(".json"):
                continue
            try:
                with open(os.path.join(dir, f), "r", encoding="utf-8") as b:
                    block = json.load(b)
                block_id = block.get("block_id", f)
                molt_type = block.get("molt_type", "?")
                cpf_status = "yes" if "cpf_flow" in block else "no"
                table.append({"block_id": block_id, "molt_type": molt_type, "cpf": cpf_status})
            except Exception:
                table.append({"block_id": f, "molt_type": "ERR", "cpf": "ERR"})
        if not table:
            return "No blocks found."
        head = "| block_id | molt_type | cpf? |\n|---|---|---|"
        rows = [f"| {r['block_id']} | {r['molt_type']} | {r['cpf']} |" for r in table]
        return head + "\n" + "\n".join(rows)
    except Exception as e:
        return f"❌ Failed to list blocks: {e}"

def validate_block(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            block = json.load(f)
        umg_valid, umg_msg = validate_umg_block(block)
        cpf_valid, cpf_msg = validate_cpf_block(block)
        result = f"UMG: {umg_msg}\nCPF: {cpf_msg}\n{describe_umg_block(block)}"
        return result
    except Exception as e:
        return f"❌ Failed to validate block: {e}"
