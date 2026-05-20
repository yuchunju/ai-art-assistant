# ===== Day 1: Basic I/O/Functions =====
from src.utils import greet_user
from src.utils import average
from src.utils import is_palindrome

# test functions
print(average([1, 2, 3, 4]))
print(is_palindrome("level"))

# user input
name = input("name: ")
age = input("age: ")

print(greet_user(name, age))

# ===== Day 3: File Persistence =====
# write to file
with open("data/notes.txt", "w") as file:
    file.write("AI workflow started.")

# read from file
with open("data/notes.txt", "r") as file:
    content = file.read()

print("read content:", content)

# CSV handling
import csv

rows = [
    ["prompt", "output"],
    ["artist statement", "generated successfully"]
]

with open("data/results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV saved.")

# read CSV
import csv

with open("data/results.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# JSON handling
import json

data = {
    "user": "Alice",
    "prompt": "Generate artist statement",
    "output": "Statement generated successfully"
}

with open("data/log.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON saved.")

# read JSON
import json

with open("data/log.json", "r") as file:
    content = json.load(file)

print(content)
print(content["prompt"])