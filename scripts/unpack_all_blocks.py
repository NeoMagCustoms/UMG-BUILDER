# File: scripts/unpack_all_blocks.py

import os
import json

def unpack_blocks(base_path="data/blocks"):
    print(f"🧠 Scanning block directory at: {base_path}\n")
    count = 0
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as f:
                    try:
                        block = json.load(f)
                        print(f"✅ Block loaded: {block.get('label', file)} — {block.get('molt_type', 'Unknown')}")
                        count += 1
                    except Exception as e:
                        print(f"❌ Failed to load {file}: {str(e)}")
    print(f"\n🔍 {count} blocks successfully unpacked.\n")

if __name__ == "__main__":
    unpack_blocks()
