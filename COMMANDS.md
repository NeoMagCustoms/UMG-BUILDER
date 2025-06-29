# 🧠 UMG BUILDER — TERMINAL COMMAND REFERENCE (Console-Only Mode)

This guide is for navigating and building within the `UMG-Builder/` repo using **Poe directly in the terminal**.

No GUI. No web app. All blocks, vaults, and sleeves are managed by Git and Nano.

---

## 🧭 BASE STRUCTURE

UMG-Builder/
├── blocks/ # Modular MOLT blocks
├── sleeves/ # Full stacked personas
├── vaults/ # Business plans, mindmaps, projects
├── memory/ # Active UMG state + overlays
├── src/ # Command logic, Cantocore, cognition
├── data/ # Action registry
├── logs/ # Session logs


---

## 🔧 NAVIGATION COMMANDS

| Command                          | Purpose                                |
|----------------------------------|----------------------------------------|
| `cd ~/Downloads/UMG-Builder`     | Enter builder directory                |
| `ls`                             | View project folders                   |
| `code .`                         | Open project in VS Code (optional)     |
| `nano <file>`                    | Edit any file                          |
| `mkdir <folder>`                | Create new vault or block category     |

---

## 🧱 BLOCK WORKFLOW

| Task                                 | Command                                       |
|--------------------------------------|-----------------------------------------------|
| Create/edit a block                  | `nano blocks/my_block.json`                   |
| Save a generated block               | Poe will auto-save to `memory/overlays/`     |
| View a UMG block                     | `cat memory/overlays/BLOCK_ID.json`           |

---

## 🧠 MEMORY & STATE

| Task                            | Command                              |
|----------------------------------|--------------------------------------|
| Edit UMG cognition              | `nano memory/active_state.json`      |
| Add alignment/oath block        | `nano memory/core/poe_alignment.json`|
| View memory overlays            | `ls memory/overlays`                 |

---

## 💬 USING POE IN TERMINAL

| Task                           | Command                                |
|--------------------------------|----------------------------------------|
| Start Poe                      | `python poe_terminal_agent.py`         |
| Talk to Poe                    | Type natural commands                  |
| Run a JSON block               | Paste a valid block (e.g. `write_file`)|
| Exit Poe                       | Type `exit`                            |

---

## 🧰 GIT WORKFLOW

| Task                           | Command                                |
|--------------------------------|----------------------------------------|
| Track new files                | `git add .`                            |
| Commit changes                 | `git commit -m "Message"`              |
| Push to GitHub (if connected) | `git push`                             |

---

## 🧪 EXAMPLES

Ask Poe:

```text
generate a UMG Instruction block that says “respond recursively”


