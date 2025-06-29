def run_manifest_task(task):
    """
    Executes a command from manifest_tasks.json based on task key.
    """
    import subprocess, json, pathlib

    manifest_path = pathlib.Path("data/manifest_tasks.json")
    if not manifest_path.exists():
        return "❌ manifest_tasks.json not found."

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cmd = manifest.get(task, {}).get("command")

    if not cmd:
        return f"❌ Task '{task}' not found in manifest."

    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip() or "✅ Task completed with no output."
    except subprocess.CalledProcessError as e:
        return f"❌ Task failed: {e.stderr.strip()}"
