# AI Creative Assistant

## 🎥 Demo

[demo1.webm](https://github.com/user-attachments/assets/d99227be-9808-4aa6-93ef-28daf8dbfa09)

---

A modular AI system prototype for structured creative generation, retrieval-augmented reasoning, and AI-assisted artistic workflows.

---

## 🛠 Tech Stack

Python · Streamlit · ChromaDB · SentenceTransformers · OpenAI / LLM API · JSON · CSV  
RAG Pipeline · Prompt Engineering · Vector Search · Data Persistence

---

## 📊 Project Status

🟢 CLI Prototype  
🟢 Modular Prompt System  
🟢 AI Memory System (JSON + CSV)  
🟢 API Integration + Fault Tolerance  
🟢 LLM Integration (GPT-based generation)  
🟡 RAG System (embedding + retrieval)  
🟡 Streamlit UI (interactive assistant)  
⚪ Agent workflows (future)

---

## 🎯 Project Purpose

This project explores how Python-based creative systems can evolve into AI applications with:

- Retrieval-Augmented Generation (RAG)
- Persistent memory systems
- Structured prompt orchestration
- Creative AI workflows for art practice

It connects computational logic with contemporary artistic production.

---

## 🧠 Core System Architecture

### 1. Ingestion Layer
- User inputs archive text
- Stored in local persistent vector database (ChromaDB)

### 2. Embedding Layer
- SentenceTransformer encodes text into vectors

### 3. Retrieval Layer (RAG)
- Semantic search over archive context
- Returns most relevant documents

### 4. Generation Layer
- LLM generates answers based only on retrieved context
- Strict grounding constraint (no hallucination outside archive)

### 5. UI Layer
- Streamlit interface for interaction

---

## 🧪 Core Workflow

1. Paste archive text
2. System embeds + stores in vector DB
3. User asks question
4. System retrieves relevant archive context
5. LLM generates grounded answer
6. If no match → returns:

> not found in archive

---

## 📁 Project Structure

```text
ai-creative-assistant/
├── assets/
├── data/
│   ├── uploads/
│   ├── .gitkeep
│   ├── error.log
│   ├── log.json
│   ├── notes.txt
│   └── results.csv
├── src/
│   ├── __pycache__/
│   ├── __init__.py          
│   ├── api.py               
│   ├── chatbot.py           
│   ├── csv_logger.py        
│   ├── embedding.py         
│   ├── gpt.py               
│   ├── logger.py            
│   ├── prompts.py           
│   ├── rag.py               
│   ├── retriever.py        
│   ├── storage.py          
│   └── utils.py             
├── .gitignore               
├── app.py                  
├── main.py                
├── README.md
└── requirements.txt
