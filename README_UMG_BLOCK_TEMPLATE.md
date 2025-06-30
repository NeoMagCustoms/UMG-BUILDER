# 📘 UMG Block Template – Schema Guide

> **Last Updated:** 2025-06-29 23:56 UTC

---

## 🎯 Purpose

This file explains the structure and purpose of a **UMG (Universal Modular Generation)** block — the atomic unit used in the Citadel Builder, Bolt deployments, and Poecore logic engine. Every block supports composable metadata, color-coded molt types, stacking logic, and execution-ready payloads.

---

## 🧱 Block Structure (Key Fields)

| Field                   | Type         | Required | Description |
|-------------------------|--------------|----------|-------------|
| `block_id`              | `string`     | ✅        | Unique internal ID (`block_001_startup_plan`) |
| `label`                 | `string`     | ✅        | Human-readable name (e.g. "Startup Plan") |
| `category`              | `string`     | ✅        | Major grouping (e.g. "Business Plans") |
| `description`           | `string`     | ✅        | Summary of what this block covers |
| `molt_type`             | `enum`       | ✅        | One of: `Primary`, `Subject`, `Instruction`, `Blueprint`, `Philosophy`, `Trigger`, `Directive`, `Deployment`, `Off` |
| `tags`                  | `string[]`   | ⚪        | For sorting, filters, and assistant recommendations |
| `cantocore`             | `string`     | ⚪        | Logic expression (e.g., `SNAP.TO=STACK`) |
| `snap_config`           | `object`     | ⚪        | Defines where and how this block snaps |
| `merge_logic`           | `object`     | ⚪        | Merge behavior and priority rules |
| `ledger`                | `object`     | ✅        | Provenance metadata (originator, verifier, timestamps) |
| `display`               | `object`     | ⚪        | Visual representation (color, icon, etc.) |
| `code_modules[]`        | `array`      | ⚪        | Optional: UI, functions, or backend logic |
| `runtime_behavior_flags`| `object`     | ⚪        | Execution scoping (e.g. `is_primary_directive`) |
| `agent_orchestration`   | `object`     | ⚪        | Multi-agent or Poecore use |
| `integration_layer`     | `object`     | ⚪        | External API or orchestration compatibility |
| `future_extensions`     | `array`      | ⚪        | Open-ended additions |
| `example_block_data`    | `object`     | ⚪        | Sample input/output examples |

---

## 🎨 Color Mapping (MOLT Type)

| MOLT Type     | Color       |
|---------------|-------------|
| `Primary`     | Blue        |
| `Subject`     | Green       |
| `Instruction` | Yellow      |
| `Blueprint`   | Teal        |
| `Philosophy`  | Orange      |
| `Trigger`     | Red         |
| `Directive`   | Purple      |
| `Deployment`  | Navy        |
| `Off`         | Gray        |

---

## 🧠 Usage

Blocks are:
- Named and versioned (e.g. `block_001_startup_plan.json`)
- Stored in folders: `data/blocks/<molt_type>/`
- Editable by AI or user (via Citadel UI or Git)
- Mergeable using stacking logic (Snap → Merge → Override)

---

## 📥 Example Block Filename

```bash
data/blocks/Subject/block_001_startup_plan.json
```

---

## 🛠️ Auto Build Support

Poecore and other agents can auto-generate and modify blocks from:
- Block names alone
- YAML definitions
- CantoCore logic overlays
- JSON templates or markdown lists

---

## 🔒 Ledger Format (Standard)

```json
"ledger": {
  "originator": "Christopher L Haynes",
  "verified_by": "PoeUMG",
  "created_at": "AUTO",
  "edit_log": []
}
```

---

## 🧪 Sanity Rule

Every block must at minimum include:

```json
block_id, label, description, molt_type, ledger
```

All else is optional but recommended.

---

🧠 *Universal Modular Generation is a cognitive OS, not just a schema.*
