# src/agent_commands.py

def write_file(path, content):
    """
    Writes the provided content to a file at the specified path.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ File written to {path}"
    except Exception as e:
        return f"❌ Failed to write file: {e}"
