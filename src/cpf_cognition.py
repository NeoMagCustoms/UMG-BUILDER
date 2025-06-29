# src/cpf_cognition.py

"""
CPF Cognition Module for PoeUMG

Validates CPF flow blocks and helps with provenance logic.
"""

def validate_cpf_block(block):
    if "cpf_flow" not in block:
        return False, "No CPF flow found (ok for UMG-only block)"
    cpf = block["cpf_flow"]
    required = ["flow_id", "pre", "action", "post"]
    missing = [k for k in required if k not in cpf]
    if missing:
        return False, f"Missing CPF fields: {', '.join(missing)}"
    return True, "✅ CPF flow present"

def extract_provenance(block):
    ledger = block.get("ledger", {})
    provenance = ledger.get("provenance", [])
    return provenance

def append_provenance(block, event):
    ledger = block.setdefault("ledger", {})
    provenance = ledger.setdefault("provenance", [])
    provenance.append(event)
    return block
