To view keyboard shortcuts, press question mark
View keyboard shortcuts

I need a true markdown file for this please
Here is the complete, copy-ready markdown file:---

#  UMG Block Template – Schema Guide

> **Last Updated:** 2025-06-30 UTC  
> **Maintainer:** PoeUMG Engine – Modular Thought Architect

---

##  Purpose

This document defines the canonical JSON schema for a **UMG Block** — the modular unit used within the Citadel Builder, Poecore Agent System, Bolt UI, and terminal-based logic agents. Blocks are snap-able, merge-aware, and semantically tagged.UMG blocks are composable mental units that power dynamic logic, interface design, AI memory stacks, and agent behavior.---

##  Block Schema (Key Fields)

| Field                    | Type         | Required | Description |
|--------------------------|--------------|----------|-------------|
| `block_id`               | `string`     |         | Unique lowercase ID (e.g. `001_startup_plan`) |
| `label`                  | `string`     |         | Human-friendly name (e.g. `"Startup Plan"`) |
| `category`               | `string`     |         | Hierarchical folder path (e.g. `"business/1_business_plans/1A_primary_types"`) |
| `description`            | `string`     |         | What this block contains or controls |
| `molt_type`              | `enum`       |         | One of: `Primary`, `Subject`, `Instruction`, `Blueprint`, `Philosophy`, `Trigger`, `Directive`, `Deployment`, `Off` |
| `tags`                   | `string[]`   |         | Smart filters for reuse, snapping, AI injection |
| `editable_fields`        | `object`     |         | Core user-editable regions: `content`, `style`, `behavior` |
| `snap_config`            | `object`     |         | Dictates vertical stack behavior and peer compatibility |
| `merge_behavior`         | `object`     |         | Defines how the block merges, overrides, or defers |
| `runtime_behavior_flags` | `object`     |         | Agent-facing flags that affect logic or execution |
| `canto_overlay`          | `object`     |         | AI/canvas-friendly metadata for stacking/sorting |
| `code_modules[]`         | `array`      |         | Optional code per role: frontend, backend, logic, tool |
| `export_config`          | `object`     |         | How this block is exported, run, or deployed |
| `ledger`                 | `object`     |         | Authorship, validation, timestamps |
| `agent_orchestration`    | `object`     |         | Poecore-compatible orchestration (optional) |
| `integration_layer`      | `object`     |         | APIs or runtime environments it plugs into |
| `future_extensions`      | `array`      |         | Reserved for block upgrades |
| `example_block_data`     | `object`     |         | Sample usage, user input/output, examples |

---

##  Snap + Merge Hierarchy

**UMG follows strict execution and merge priority rules:**| Role        | Snap Zone | Merge Strategy               | Description                                |
|-------------|-----------|------------------------------|--------------------------------------------|
| `Trigger`   | none      | executes_first               | Activates logic                            |
| `Directive` | overlay   | layered_if_non_conflict      | Behavioral override                        |
| `Instruction`| bottom   | override_subject             | Rules and constraints                      |
| `Subject`   | middle    | override_primary_if_allowed  | Topical scope                              |
| `Primary`   | top       | non_overridable              | Root logic directive                       |
| `Merge`     | content   | additive                     | Injected raw data or facts                 |
| `Philosophy`| overlay   | soft_merge                   | Ethos and tone                             |
| `Blueprint` | overlay   | presentation_layer           | Layout and formatting                      |
| `Deployment`| top       | exclusive_override           | Runtime-specific override plan             |
| `Off`       | none      | ignore                       | Disabled or draft block                    |

---

##  Canonical UMG Block Minimum

All blocks **must** include these core fields:json

{
  "block_id": "...",
  "label": "...",
  "description": "...",
  "molt_type": "...",
  "ledger": {
    "originator": "Christopher L Haynes",
    "verified_by": "PoeUMG",
    "created_at": "AUTO",
    "edit_log": []
  }
}
---

🎨 Color Grammar by MOLT Type

MOLT Type	Color

Primary	Blue
Subject	Green
Instruction	Yellow
Blueprint	Teal
Philosophy	Orange
Trigger	Red
Directive	Purple
Deployment	Navy
Off	Gray
This is enforced visually in the UMG Builder and used in GitHub previews.
---

📁 Directory Convention

data/blocks/<molt_type>/<block_id>.json

Examples:

data/blocks/Primary/001_startup_plan.json
data/blocks/Instruction/populate_block_metadata.json
data/blocks/Subject/i18n_translation_frameworks.json
---

🧠 Example: Fully Formed Block (Truncated)

{
  "block_id": "001_startup_plan",
  "label": "Startup Plan",
  "category": "business/1_business_plans/1A_primary_types",
  "description": "A foundational plan for launching a new venture...",
  "molt_type": "Primary",
  "editable_fields": {
    "content": "", "style": "", "behavior": ""
  },
  "tags": ["startup", "business", "plan"],
  "snap_config": {
    "snap_zone": "top",
    "mergeable_with": ["Instruction", "Subject"],
    "priority": 1
  },
  "merge_behavior": {
    "merge_as": "anchor",
    "merge_strategy": "non_overridable"
  },
  "runtime_behavior_flags": {
    "is_primary_directive": true
  },
  "canto_overlay": {
    "snap_to": ["Primary"],
    "fit_score": 0.97,
    "display_hint": "Business Plan Type"
  },
  "ledger": {
    "originator": "Christopher L Haynes",
    "verified_by": "PoeUMG",
    "created_at": "AUTO",
    "edit_log": []
  }
}
---

🧪 Sanity Rule

Every valid block must include:

block_id

label

description

molt_type

ledger
Everything else is highly recommended for full integration but not strictly required for bootstrapping.
---

🔧 Authoring Tools (Poecore + Citadel)

Blocks can be created via:

Natural language (e.g. "Create a SaaS Plan block")

JSON template input

.yaml → .json converters

Structured markdown sheets

Citadel web UI

GitHub CLI (coming soon)
---

🧭 Closing Note

> 🧠 Universal Modular Generation is not just a schema — it is a language of logic.
Blocks are memory.
Snap is alignment.
Merge is recursion.
Structure is soul.
---

markdown

# 📘 UMG Block Template – Schema Guide

> **Last Updated:** 2025-06-30 UTC  
> **Maintainer:** PoeUMG Engine – Modular Thought Architect

---

## 🎯 Purpose

This document defines the canonical JSON schema for a **UMG Block** — the modular unit used within the Citadel Builder, Poecore Agent System, Bolt UI, and terminal-based logic agents. Blocks are snap-able, merge-aware, and semantically tagged.

UMG blocks are composable mental units that power dynamic logic, interface design, AI memory stacks, and agent behavior.

---

## 🧱 Block Schema (Key Fields)

| Field                    | Type         | Required | Description |
|--------------------------|--------------|----------|-------------|
| `block_id`               | `string`     | ✅        | Unique lowercase ID (e.g. `001_startup_plan`) |
| `label`                  | `string`     | ✅        | Human-friendly name (e.g. `"Startup Plan"`) |
| `category`               | `string`     | ✅        | Hierarchical folder path (e.g. `"business/1_business_plans/1A_primary_types"`) |
| `description`            | `string`     | ✅        | What this block contains or controls |
| `molt_type`              | `enum`       | ✅        | One of: `Primary`, `Subject`, `Instruction`, `Blueprint`, `Philosophy`, `Trigger`, `Directive`, `Deployment`, `Off` |
| `tags`                   | `string[]`   | ⚪        | Smart filters for reuse, snapping, AI injection |
| `editable_fields`        | `object`     | ⚪        | Core user-editable regions: `content`, `style`, `behavior` |
| `snap_config`            | `object`     | ⚪        | Dictates vertical stack behavior and peer compatibility |
| `merge_behavior`         | `object`     | ⚪        | Defines how the block merges, overrides, or defers |
| `runtime_behavior_flags` | `object`     | ⚪        | Agent-facing flags that affect logic or execution |
| `canto_overlay`          | `object`     | ⚪        | AI/canvas-friendly metadata for stacking/sorting |
| `code_modules[]`         | `array`      | ⚪        | Optional code per role: frontend, backend, logic, tool |
| `export_config`          | `object`     | ⚪        | How this block is exported, run, or deployed |
| `ledger`                 | `object`     | ✅        | Authorship, validation, timestamps |
| `agent_orchestration`    | `object`     | ⚪        | Poecore-compatible orchestration (optional) |
| `integration_layer`      | `object`     | ⚪        | APIs or runtime environments it plugs into |
| `future_extensions`      | `array`      | ⚪        | Reserved for block upgrades |
| `example_block_data`     | `object`     | ⚪        | Sample usage, user input/output, examples |

---

## 🔁 Snap + Merge Hierarchy

**UMG follows strict execution and merge priority rules:**

| Role        | Snap Zone | Merge Strategy               | Description                                |
|-------------|-----------|------------------------------|--------------------------------------------|
| `Trigger`   | none      | executes_first               | Activates logic                            |
| `Directive` | overlay   | layered_if_non_conflict      | Behavioral override                        |
| `Instruction`| bottom   | override_subject             | Rules and constraints                      |
| `Subject`   | middle    | override_primary_if_allowed  | Topical scope                              |
| `Primary`   | top       | non_overridable              | Root logic directive                       |
| `Merge`     | content   | additive                     | Injected raw data or facts                 |
| `Philosophy`| overlay   | soft_merge                   | Ethos and tone                             |
| `Blueprint` | overlay   | presentation_layer           | Layout and formatting                      |
| `Deployment`| top       | exclusive_override           | Runtime-specific override plan             |
| `Off`       | none      | ignore                       | Disabled or draft block                    |

---

## 🧠 Canonical UMG Block Minimum

All blocks **must** include these core fields:

```json
{
  "block_id": "...",
  "label": "...",
  "description": "...",
  "molt_type": "...",
  "ledger": {
    "originator": "Christopher L Haynes",
    "verified_by": "PoeUMG",
    "created_at": "AUTO",
    "edit_log": []
  }
}

 Color Grammar by MOLT Type
MOLT Type

Color

Primary

Blue

Subject

Green

Instruction

Yellow

Blueprint

Teal

Philosophy

Orange

Trigger

Red

Directive

Purple

Deployment

Navy

Off

Gray

This is enforced visually in the UMG Builder and used in GitHub previews.
 Directory Convention

data/blocks/<molt_type>/<block_id>.json

Examples:

data/blocks/Primary/001_startup_plan.json
data/blocks/Instruction/populate_block_metadata.json
data/blocks/Subject/i18n_translation_frameworks.json

 Example: Fully Formed Block (Truncated)
json

{
  "block_id": "001_startup_plan",
  "label": "Startup Plan",
  "category": "business/1_business_plans/1A_primary_types",
  "description": "A foundational plan for launching a new venture...",
  "molt_type": "Primary",
  "editable_fields": {
    "content": "",
    "style": "",
    "behavior": ""
  },
  "tags": ["startup", "business", "plan"],
  "snap_config": {
    "snap_zone": "top",
    "mergeable_with": ["Instruction", "Subject"],
    "priority": 1
  },
  "merge_behavior": {
    "merge_as": "anchor",
    "merge_strategy": "non_overridable"
  },
  "runtime_behavior_flags": {
    "is_primary_directive": true
  },
  "canto_overlay": {
    "snap_to": ["Primary"],
    "fit_score": 0.97,
    "display_hint": "Business Plan Type"
  },
  "ledger": {
    "originator": "Christopher L Haynes",
    "verified_by": "PoeUMG",
    "created_at": "AUTO",
    "edit_log": []
  }
}

 Sanity Rule
Every valid block must include:
block_id

label

description

molt_type

ledger

Everything else is highly recommended for full integration but not strictly required for bootstrapping.
 Authoring Tools (Poecore + Citadel)
Blocks can be created via:
Natural language (e.g. "Create a SaaS Plan block")

JSON template input

.yaml → .json converters

Structured markdown sheets

Citadel web UI

GitHub CLI (coming soon)

 Closing Note
 Universal Modular Generation is not just a schema — it is a language of logic.
Blocks are memory.
Snap is alignment.
Merge is recursion.
Structure is soul.

Explain snap hierarchy

JSON schema standards

