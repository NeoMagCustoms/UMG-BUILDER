# 🌐 UMG Web Stack Blueprint for Bolt Integration

This document outlines how to interpret and scaffold the UMG-Builder's modular website using the `blocks/web/` structure. Each block is a self-contained unit of logic, UI, or structure.

---

## 🧠 What is UMG?

UMG (Universal Modular Generation) is a block-based framework for composing AI logic and UI scaffolding using modular "thought units" called MOLT blocks.

In the web context, each block (stored in JSON) represents:
- a page,
- a page section,
- a component,
- a layout style,
- or a deploy/export rule.

---

## 📁 Folder Structure to Scaffold

blocks/web/
├── pages/         → Each JSON = a page (e.g., homepage, about)
├── sections/      → Page sections (hero, features, footer)
├── components/    → Reusable UI elements (buttons, navbars)
├── flow/          → UX logic flows (e.g., onboarding, CTA)
├── blueprint/     → Layout logic (columns, themes)
└── deploy/        → Export rules for Bolt + TSX integration
🧩 Bolt Build Instructions
Each PAGE.*.json becomes a full route/page

Inject SECTION.* blocks based on snap_config.snap_zone into page blocks

Render COMPONENT.* blocks inside their parent sections

Apply UI layout from BLUEPRINT.* blocks if present

**Use DEPLOY.BOLT.PAGES.json (or equivalent) to define:

default page

export rules

route priorities

build commands (if any)**

📦 Export Behavior
Bolt should export:

Pages and sections into TSX or JSX

Blueprint blocks as layout scaffolds (columns, flex, container logic)

Any block with "bolt_ready": true into the generated component/page tree

Optional: Group by category, molt_type, or export_target

🧬 Core Stack Contracts
All blocks must define:

block_id

molt_type

ledger (with originator + signature)

Optional tags:

"category" → enables folder-based UI filters

"export_target" → allows bolt, pdf, or json export routing

Metadata like fit_score, snap_zone, style_notes used for UI planning

