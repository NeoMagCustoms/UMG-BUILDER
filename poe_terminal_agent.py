# poe_terminal_agent.py

import os
import json
from dotenv import load_dotenv
import openai
from poe_executor import execute

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

model = "gpt-4o"

def load_state():
    try:
        with open("memory/active_state.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def format_umg_header(state):
    lines = [f"- {k}: {v}" for k, v in state.items()]
    return "🧠 UMG State:\n" + "\n".join(lines)

print("\n🧠 Poe Terminal UMG — GPT mode ENABLED. Type natural commands, or 'exit'.\n")

while True:
    user_input = input("You > ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Poe > 🌒 Memory dims. Terminal closing.")
        break

    state = load_state()
    umg_header = format_umg_header(state)

    try:
        messages = [
            {"role": "system", "content": umg_header + "\nYou are Poe. Speak clearly and reply in JSON if possible."},
            {"role": "user", "content": user_input}
        ]
        response = openai.ChatCompletion.create(model=model, messages=messages)
        reply = response.choices[0].message["content"].strip()
        print(f"\nPoe > {reply}")

        if "```json" in reply:
            try:
                json_block = reply.split("```json")[1].split("```")[0].strip()
                task = json.loads(json_block)
                result = execute(task)
                print(f"\n🛠 Execution Result:\n{result}")
            except Exception as e:
                print(f"❌ JSON Parsing Error: {e}")
    except Exception as e:
        print(f"❌ GPT Error: {e}")
