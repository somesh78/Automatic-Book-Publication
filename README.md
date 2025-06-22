# 📚 Automated Book Publication Workflow

This project is a complete **LLM-based Agentic System with RL Search**, built as part of an internship assignment. It scrapes a book chapter, applies AI rewriting and review, facilitates human edits, stores versioned content, and uses a reinforcement learning-based search system to retrieve intelligently ranked chapters.

---

## 🎯 Objective

> Build a Python system that fetches chapter content from a URL, rewrites it using AI agents, allows human editing, saves versions, and retrieves similar versions using RL-enhanced search.

---

## 🧩 Features

- ✅ **Scraping & Screenshots** – Fetches full chapter text and saves a screenshot using Playwright
- ✅ **AI Writing & Review** – Groq-hosted LLM spins the original chapter and auto-reviews it
- ✅ **Human-in-the-Loop Editing** – Prompts the user to edit/rewrite the content manually
- ✅ **Agentic Pipeline** – AI Writer → Human Review → AI Reviewer → Versioning
- ✅ **Versioning with ChromaDB** – Saves all final chapter versions with metadata
- ✅ **RL-Based Search** – Uses a reward-scored reranker to retrieve relevant content versions
- ✅ **Offline Python App** – Simple CLI-based workflow

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Playwright** – for scraping
- **Groq + transformers** – for LLM-based rewriting
- **ChromaDB** – for vector DB storage and semantic search
- **Sentence-Transformers** – for RL-style reward calculation
- **ONNX / MiniLM** – for embedding model
- **Rich Logging + Modular Scripts**

---

## 🚀 Installation

```bash
git clone https://github.com/somesh78/auto-book-pub.git
cd auto-book-pub
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
