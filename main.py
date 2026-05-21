from src.storage import create_record, append_record
from src.csv_logger import append_csv
from src.gpt import generate_text
from src.prompts import PROMPTS

import os

print("CWD:", os.getcwd())

# =========================
# 1. Task Selection
# =========================
print("""

Choose task:

1. statement
2. exhibition
3. caption
4. proposal
5. translation
6. keywords

""")

task = input("Select task: ").strip()

# =========================
# 2. Task Router
# =========================
task_map = {
    "1": "statement",
    "2": "exhibition",
    "3": "caption",
    "4": "proposal",
    "5": "translation",
    "6": "keywords"
}

task_type = task_map.get(task)

if not task_type:
    print("Invalid task.")
    exit()

# =========================
# 3. User Input
# =========================
description = input("\nDescribe your art project:\n")

# =========================
# 4. Prompt Template
# =========================
prompt = PROMPTS[task_type].format(
    description=description
)

# =========================
# 5. GPT Generation
# =========================
output = generate_text(prompt)

print("\n=== GENERATED TEXT ===\n")

print(output)

# =========================
# 6. Save Memory
# =========================
record = create_record(
    input_text=description,
    output_text=output,
    type=task_type
)

append_record(record)

print("\nDEBUG: writing JSON...")

# =========================
# 7. CSV Logging
# =========================
clean_output = output.replace("\n", " ")[:200]

append_csv(
    "data/results.csv",
    row=[task_type, description, clean_output],
    header=["task", "input", "output"]
)

print("DEBUG: writing CSV...")
