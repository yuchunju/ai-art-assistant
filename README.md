# AI Creative Assistant — Core Python Exercise (Day 1)

This is the foundational exercise for building an AI application development workflow.

---

## 🧠 What This Covers

This script demonstrates core programming concepts required for AI application development:

### 1. User Interaction Layer

Basic CLI input system for collecting user data.

### 2. Structured Data Handling

Using lists and dictionaries to represent simple data models.

### 3. Iteration Logic

Processing collections of data, a fundamental pattern in AI pipelines.

---

## 💻 Code Overview

### User Input Example

```python
name = input("name: ")
age = input("age: ")
print(f"Hello {name}, you are {age}")
```

### List Processing

```python
foods = ["pizza", "tea", "rice"]

for food in foods:
    print(food)
```

### Dictionary Processing

```python
person = {"name": "Alice", "age": 25}

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## ▶️ Run

```bash
python main.py
```

---

## 📁 Project Structure

```text
ai-creative-assistant/
│
├── README.md
├── main.py
├── requirements.txt
└── .gitignore
```

---

## 🔍 Learning Outcome

* Basic Python syntax
* Input/output handling
* Data structure manipulation
* Looping patterns used in real-world applications
* Basic Git project organization

---

## 🚀 Next Step

Extend this into:

* Functions (modularization)
* API integration (real AI calls)
* Prompt-based generation system
* AI-assisted content workflow

---

## 📌 Development Goal

This repository documents the process of transitioning from foundational Python programming toward practical AI application development.
