#!/usr/bin/env python3
"""
Syncs functions in src/agent_commands.py with data/command_registry.json.
Adds any missing entries (basic implementation).
"""

import ast, json, pathlib, sys, textwrap

CMDS_PATH = pathlib.Path("src/agent_commands.py")
REG_PATH = pathlib.Path("data/command_registry.json")

# 1) collect def names in agent_commands
tree = ast.parse(CMDS_PATH.read_text(encoding="utf-8"))
defs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]

# 2) load registry
reg = json.loads(REG_PATH.read_text(encoding="utf-8"))

added = 0
for fn in defs:
    if fn not in reg:
        reg[fn] = {
            "function": fn,
            "module": "src.agent_commands",
            "description": f"(auto-added) {fn}"
        }
        added += 1

if added:
    REG_PATH.write_text(textwrap.indent(json.dumps(reg, indent=2), ""), encoding="utf-8")
    print(f"🛠️  Added {added} missing commands to registry.")
else:
    print("✅ Registry already in sync.")

sys.exit(0)

