# 🧠 UMG-Builder

Terminal-first framework for building **Universal Modular Generation** (UMG) AI assistants.  
You assemble cognition as JSON blocks (MOLTs), snap on sleeves (personas), and run everything through a ChatGPT-powered loop called **Poe**.

---

## 📁 Directory Guide

| Path | Purpose |
|------|---------|
| `src/agent_commands.py` | Low-level file / block / git actions |
| `src/sleeve_manager.py` | (WIP) load / switch persona sleeves |
| `poe_terminal_agent.py` | Main interactive CLI loop |
| `poe_executor.py` | Executes JSON tasks & writes provenance |
| `data/command_registry.json` | Maps `"action"` ➜ module.function |
| `blocks/` | Source MOLTs (Primary, Subject, etc.) |
| `memory/overlays/` | Runtime-active blocks after `load_*` |
| `memory/adaptation_logs/` | Self-improve & provenance logs |
| `scripts/` | One-off helpers (`bulk_import.py`, etc.) |
| `.github/workflows/` | CI: auto-commit blocks + QA validate |

---

## 🏃 Quick-Start

```bash
# enter repo
cd ~/Downloads/UMG-Builder

# run validation
python validate_blocks.py

# launch Poe terminal
python poe_terminal_agent.py
