elif "fill blocks" in user_input.lower():
    import os, json
    from datetime import datetime
    from scripts.fill_existing_blocks import fill_block_fields

    def append_provenance(block, event):
        if "ledger" not in block:
            block["ledger"] = {
                "originator": "Christopher L Haynes",
                "verified_by": "PoeUMG",
                "created_at": datetime.now().isoformat(),
                "edit_log": []
            }
        if "edit_log" not in block["ledger"]:
            block["ledger"]["edit_log"] = []
        block["ledger"]["edit_log"].append(event)
        return block

    def log_fill_run():
        base_path = "data/blocks"
        action = "fill_blocks"

        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith(".json"):
                    block_path = os.path.join(root, file)
                    try:
                        with open(block_path, "r", encoding="utf-8") as f:
                            block = json.load(f)

                        category = os.path.basename(os.path.dirname(block_path))
                        fill_block_fields(block, block_path, category)

                        event = {
                            "timestamp": datetime.now().isoformat(),
                            "action": action,
                            "user": "Mag",
                            "change": f"Ran {action} via Poe executor"
                        }
                        block = append_provenance(block, event)

                        with open(block_path, "w", encoding="utf-8") as f:
                            json.dump(block, f, indent=2)

                        print(f"✅ Updated with provenance: {block_path}")

                    except Exception as e:
                        print(f"❌ Error in {block_path}: {e}")

    log_fill_run()
    print("🧠 All blocks filled and logged.")
