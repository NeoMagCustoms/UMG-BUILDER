# poe_terminal_agent.py

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from poe_executor import execute

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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

print("\n🧠 Poe Terminal UMG (OpenAI 1.0+ mode) — Type natural input or 'exit'.\n")

while True:
    user_input = input("You > ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Poe > 🌒 Terminal closing.")
        break

    state = load_state()
    umg_header = format_umg_header(state)

    try:
        messages = [
            {"role": "system", "content": umg_header + "\nYou are Poe, a UMG-aligned terminal AI. Speak clearly, and return valid ```json blocks when actions are implied."},
            {"role": "user", "content": user_input}
        ]
        response = client.chat.completions.create(model=model, messages=messages)
        reply = response.choices[0].message.content.strip()
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
        print(f"❌ GPT-4o Error: {e}")
