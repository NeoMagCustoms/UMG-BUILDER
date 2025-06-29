"""
Sleeve Manager: Load or switch PoeUMG sleeves into active_state.json
"""

import json
import pathlib

STATE_PATH = pathlib.Path("memory/active_state.json")

def load_sleeve(sleeve_path):
    """Load a single sleeve file and set as active"""
    with open(sleeve_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    state = {"active_sleeve": data.get("block_id", "UNKNOWN")}
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    return f"✅ Loaded sleeve: {state['active_sleeve']}"

def get_active_sleeve():
    """Return the currently loaded sleeve ID"""
    if STATE_PATH.exists():
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        return data.get("active_sleeve", "None")
    return "No sleeve loaded."

if __name__ == "__main__":
    # For test purposes
    print("Current:", get_active_sleeve())
	
