kk# poe_executor.py

import json
import importlib
from pathlib import Path
from datetime import datetime
from src.cpf_cognition import append_provenance

REGISTRY_FILE = Path("data/command_registry.json")
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
ADAPTATION_LOG_DIR = Path("memory/adaptation_logs")
ADAPTATION_LOG_DIR.mkdir(parents=True, exist_ok=True)

def load_registry():
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def log_event(action, args):
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = LOG_DIR / f"session_{today}.json"
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "args": args
    }
    data = []
    if log_path.exists():
        with open(log_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    data.append(entry)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def log_adaptation(action, args, result):
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = ADAPTATION_LOG_DIR / f"{today}.json"
    event = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "args": args,
        "result": result
    }
    data = []
    if log_path.exists():
        with open(log_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    data.append(event)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def execute(task):
    registry = load_registry()
    action = task.get("action")
    args = task.copy()
    args.pop("action", None)

    if not action or action not in registry:
        return f"⚠️ Unknown action: {action}"

    meta = registry[action]
    func_name = meta["function"]
    module_name = meta["module"]

    try:
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
    except Exception as e:
        return f"❌ Could not load function '{func_name}': {e}"

    try:
        # If block_path in args, update provenance before/after (if file exists)
        block_path = args.get("path") or args.get("block_path")
        if block_path and block_path.endswith(".json"):
            try:
                with open(block_path, "r", encoding="utf-8") as f:
                    block = json.load(f)
                event = {
                    "timestamp": datetime.now().isoformat(),
                    "action": action,
                    "user": "Mag",
                    "change": f"Ran {action} via Poe executor"
                }
                block = append_provenance(block, event)
                with open(block_path, "w", encoding="utf-8") as f:
                    json.dump(block, f, indent=2)
            except Exception:
                pass

        result = func(**args) if args else func()
        log_event(action, task)
        log_adaptation(action, args, result)
        return result
    except Exception as e:
        return f"🔥 Execution error in '{func_name}': {e}"

