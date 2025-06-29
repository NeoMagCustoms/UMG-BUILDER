"""
Ability Guard: Restricts command execution based on the current sleeve's abilities.
"""

import json
import pathlib

ACTIVE_STATE_PATH = pathlib.Path("memory/active_state.json")

def check_ability(ability_required):
    """
    Checks if the current sleeve grants permission to perform a given ability.
    """
    if not ACTIVE_STATE_PATH.exists():
        return False, "❌ No active_state.json found."

    state = json.loads(ACTIVE_STATE_PATH.read_text(encoding="utf-8"))
    active_sleeve = state.get("active_sleeve")
    if not active_sleeve:
        return False, "❌ No sleeve loaded."

    # Load sleeve definition
    sleeve_path = pathlib.Path(f"sleeves/{active_sleeve}.json")
    if not sleeve_path.exists():
        return False, f"❌ Sleeve file not found: {active_sleeve}.json"

    sleeve = json.loads(sleeve_path.read_text(encoding="utf-8"))
    abilities = sleeve.get("abilities", [])
    if ability_required in abilities:
        return True, f"✅ Ability '{ability_required}' granted by sleeve '{active_sleeve}'."
    return False, f"🚫 Ability '{ability_required}' not allowed in sleeve '{active_sleeve}'."

if __name__ == "__main__":
    print(check_ability("git_ops"))
