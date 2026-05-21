# AI Creative Assistant

A modular AI system prototype designed for structured creative generation and future LLM integration.

> CLI-based AI workflow prototype for structured creative generation

A Python-based learning project evolving toward an AI application development workflow, integrating structured data handling, CLI interaction, and foundations for LLM-powered tools.

---

## 🛠 Tech Stack

Python · CLI · JSON · OpenAI SDK · SiliconFlow API ·
LLM Integration · Prompt Routing · Data Persistence ·
(Future: RAG · Streamlit)

---

## 📊 Project Status

🟢 Phase 1: CLI prototype (completed)  
🟢 Phase 2: Modular workflow + Prompt system (completed)  
🟢 Phase 3: AI Memory System + Data Persistence Layer (completed)  
🟢 Phase 4: API Integration + Fault-Tolerant Pipeline (completed)  
🟢 Phase 5: LLM Integration + AI Text Assistant (completed)  
🟡 Phase 6: RAG + Retrieval System (next)  
⚪ Phase 7: Streamlit UI + Agent Workflows (planned)

---

## 🎯 Project Purpose

This project explores how basic Python programming can be structured into an AI application workflow, serving as the foundation for future development in:

* LLM-based applications
* AI automation tools
* Prompt-driven systems
* Data processing pipelines

---

## 🧪 What This Tool Does (Core Workflow)

This project now functions as a modular AI text assistant system:

1. User selects a creative writing task
2. System routes request through prompt templates
3. GPT model generates structured creative output
4. Outputs are persisted into JSON + CSV memory systems
5. Runtime logs and retry mechanisms improve stability
6. Modular architecture supports future RAG and agent expansion


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


🟢 Day 5 — LLM Integration + AI Text Assistant

Integrated GPT-based text generation using SiliconFlow API  
Built multi-task prompt routing system  
Implemented reusable prompt registry architecture  
Added AI generation persistence into JSON + CSV pipelines  
Designed modular AI text assistant workflow  

System upgrade:

gpt.py → LLM inference layer  
prompts.py → prompt registry system  
main.py → multi-task AI orchestration engine
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
Choose task:

1. statement
2. exhibition
3. caption
4. proposal
5. translation
6. keywords

Select task: 1

Describe your art project:

Plastic waste archive and AI memory systems

=== GENERATED TEXT ===

My work explores the intersection between discarded material,
digital memory, and algorithmic systems...

---

## 📁 Project Structure

```text
ai-creative-assistant/
├── data/
│   ├── log.json
│   ├── results.csv
│   ├── notes.txt
│   └── error.log
│
├── src/
│   ├── api.py
│   ├── gpt.py
│   ├── prompts.py
│   ├── storage.py
│   ├── csv_logger.py
│   ├── logger.py
│   └── utils.py
│
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
* Prompt registry → modular prompt routing architecture
* GPT inference layer → LLM orchestration pipeline
* Multi-task routing → AI assistant workflow control

---

## 🚀 Next Development Steps

Planned evolution of this project:

* Retrieval-Augmented Generation (RAG)
* Embedding-based memory search
* Vector database integration
* Streamlit interaction UI
* Autonomous agent workflows
* Multi-step reasoning pipelines
* Tool-using AI assistants

---

## 📌 Long-Term Goal

To evolve this repository into a modular AI creative assistant platform capable of:

* LLM-powered creative writing
* Persistent conversational memory
* Retrieval-based contextual generation
* Multi-agent creative workflows
* Structured artistic and curatorial content generation

The project aims to bridge contemporary creative practice with practical AI application engineering.

---

## 🧭 Development Philosophy

This project follows a progressive learning approach:

> From simple Python scripts → to structured AI workflows → to usable AI applications

This project demonstrates the ability to translate simple logic into AI system design thinking.