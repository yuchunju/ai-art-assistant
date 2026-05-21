# AI Creative Assistant

A modular AI system prototype designed for structured creative generation and future LLM integration.

> CLI-based AI workflow prototype for structured creative generation

A Python-based learning project evolving toward an AI application development workflow, integrating structured data handling, CLI interaction, and foundations for LLM-powered tools.

---

## 🛠 Tech Stack

Python · CLI · JSON · API Integration · Data Persistence · (Future: OpenAI API · RAG · Streamlit)

---

## 📊 Project Status

🟢 Phase 1: CLI prototype (completed)  
🟢 Phase 2: Modular workflow + Prompt system (completed)  
🟢 Phase 3: AI Memory System + Data Persistence Layer (completed)  
🟢 Phase 4: API Integration + Fault-Tolerant Pipeline (completed)
🟡 Phase 5: LLM integration (next)
⚪ Phase 6: RAG + UI system (planned)

---

## 🎯 Project Purpose

This project explores how basic Python programming can be structured into an AI application workflow, serving as the foundation for future development in:

* LLM-based applications
* AI automation tools
* Prompt-driven systems
* Data processing pipelines

---

## 🧪 What This Tool Does (Core Workflow)

This CLI-based tool simulates a minimal AI generation pipeline:

1. User inputs structured data (text / metadata)
2. System processes input → calls external API → injects memory context
3. Structured output is generated and stored persistently
4. System logs runtime data into JSON + CSV pipelines
5. Fault-tolerant retry logic prevents runtime crashes


---


## 🧠 Core Concept

This project demonstrates how simple Python constructs map to real AI application patterns:

* User input → Prompt input layer
* Lists & dictionaries → Structured data models (JSON-like structures)
* Loops → Batch processing in AI pipelines
* CLI scripts → Early-stage AI tools

---

## 📈 System Evolution

🟢 Day 1 — Initial Commit

Built basic CLI workflow
Practiced Python input/output
Learned lists and dictionaries
First GitHub repository setup


🟢 Day 2 — Modular AI Workflow Architecture

Refactored project into modular structure
Introduced src/utils.py
Introduced src/prompts.py

System upgrade:

main.py → execution layer
utils.py → logic layer
prompts.py → AI generation layer


🟢 Day 3 — AI Memory + Data Persistence System

Built persistent AI memory system using JSON + CSV
Implemented structured logging pipeline
Enabled multi-turn contextual responses
Designed unified data schema for AI interactions

System upgrade:

storage.py → memory engine (JSON persistence)
csv_logger.py → logging engine (CSV analytics)
main.py → full AI pipeline orchestration


🟢 Day 4 — API Integration + Fault-Tolerant Pipeline

Integrated external API communication layer  
Implemented JSON response parsing  
Added retry mechanism and graceful fallback handling  
Built fault-tolerant AI processing pipeline  

System upgrade:

api.py → external API communication layer  
main.py → runtime orchestration + API pipeline  
memory system → contextual runtime injection  


---

### User Interaction Layer

```python
name = input("name: ")
age = input("age: ")
print(f"Hello {name}, you are {age}")
```

---

### List Processing

```python
foods = ["pizza", "tea", "rice"]

for food in foods:
    print(food)
```

---

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

## 📤 Example Output

```text
[INPUT]
name: Juju

[API]
{'name': 'Juju', 'age': 57, 'count': 1}

[OUTPUT]
Hello Juju, you are 57 years old.
(Memory: last input was 'Alice', last output was 'Hello Alice, you are 31 years old.')
```
---

## 📁 Project Structure

```text
ai-creative-assistant/
├── data/
│   ├── log.json
│   ├── results.csv
│   ├── notes.txt
│   └── error.log

├── src/
│   ├── api.py
│   ├── prompts.py
│   ├── storage.py
│   ├── csv_logger.py
│   ├── logger.py
│   └── utils.py

├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## 🔍 Learning Outcome

* Understand Python input/output workflows
* Work with structured data (lists, dictionaries)
* Apply iteration patterns for data processing
* Learn basic project organization with Git
* Establish foundation for AI application architecture thinking
* Build persistent AI memory systems with JSON
* Design structured logging pipelines for AI applications
* Integrate external APIs into Python applications
* Handle API failures with retry mechanisms
* Design fault-tolerant runtime pipelines
* Process structured JSON responses
* Simulate AI application orchestration workflows

---

## 🧠 Prompt Template System (Day 2)

The project now includes reusable prompt templates for:

- Artist statement generation  
- Exhibition introduction generation  
- Proposal refinement  
- Social media caption generation  
- Translation workflows  

---

## 🧩 AI Development Mapping

This project acts as a bridge between basic programming and AI systems:

* CLI input → Prompt engineering input layer
* Python data structures → JSON / API payloads
* Loop logic → Batch inference / dataset processing
* Scripts → AI automation tools
* AI memory system → persistent context + multi-turn reasoning capability
* API layer → external model/service communication
* Retry system → fault-tolerant AI infrastructure
* JSON persistence → conversational memory storage
* Runtime orchestration → AI application control flow

---

## 🚀 Next Development Steps

Planned evolution of this project:

* Modular functions (code organization)
* API integration (OpenAI / external AI services)
* Prompt template system
* JSON-based data pipeline
* AI-assisted content generation system
* Streamlit UI for interaction

---

## 📌 Long-Term Goal

To evolve this repository into a minimal but functional AI application framework capable of:

* Generating structured creative outputs
* Processing user inputs via LLM APIs
* Serving as a lightweight AI assistant prototype

This project will evolve into a modular AI creative assistant for generating structured artistic and curatorial content.

---

## 🧭 Development Philosophy

This project follows a progressive learning approach:

> From simple Python scripts → to structured AI workflows → to usable AI applications

This project demonstrates the ability to translate simple logic into AI system design thinking.