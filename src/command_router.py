"""
Command Router: Maps natural language or alias commands to registered functions.
"""

import json
import pathlib
from importlib import import_module

REGISTRY_PATH = pathlib.Path("data/command_registry.json")
ALIASES_PATH = pathlib.Path("data/command_aliases.json")

def resolve_command(command_key):
    """
    Resolves a command key or alias into a function call.
    """
    if not REGISTRY_PATH.exists():
        return f"❌ Registry file missing at {REGISTRY_PATH}"

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    # Check if it's a direct match
    if command_key in registry:
        return dispatch(registry[command_key])

    # If not, try alias map
    if ALIASES_PATH.exists():
        aliases = json.loads(ALIASES_PATH.read_text(encoding="utf-8"))
        canonical = aliases.get(command_key)
        if canonical and canonical in registry:
            return dispatch(registry[canonical])

    return f"❌ Unknown command or alias: {command_key}"

def dispatch(command_entry):
    """
    Loads and executes a registered function.
    """
    try:
        module = import_module(command_entry["module"])
        func = getattr(module, command_entry["function"])
        return func()
    except Exception as e:
        return f"❌ Dispatch error: {str(e)}"

if __name__ == "__main__":
    print(resolve_command("git_status"))
