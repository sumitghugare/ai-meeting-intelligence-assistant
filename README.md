# 🚀 MeetMind AI — AI Meeting Intelligence Assistant

<p align="center">
  <img src="screenshots/dashboard.png" width="100%" alt="MeetMind AI Dashboard"/>
</p>

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/Whisper-SpeechAI-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/RAG-LLM-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ChromaDB-VectorDB-yellow?style=for-the-badge"/>

</p>

---

# 🧠 Overview

MeetMind AI is an AI-powered Meeting Intelligence Assistant that automatically converts meeting recordings into structured, searchable, and interactive insights.

The system can:

- 🎤 Transcribe meetings using AI
- 📝 Generate meeting summaries
- ✅ Extract action items
- ⭐ Detect key decisions
- ❓ Identify open questions
- 💬 Enable conversational AI chat using RAG
- 🔎 Perform semantic search using vector embeddings

---

# ✨ Features

## 🎤 AI Transcription
- English + Hinglish support
- Whisper + Sarvam AI integration
- Intelligent audio chunking

---

## 🧠 AI Meeting Summary
- Executive-level meeting summaries
- Hierarchical chunk-based summarization
- Handles long meetings efficiently

---

## ✅ Action Item Detection
Automatically extracts:
- Tasks
- Owners
- Deadlines

---

## ⭐ Key Decision Tracking
Identifies important decisions discussed during meetings.

---

## ❓ Open Question Extraction
Detects unresolved discussion points and follow-up questions.

---

## 💬 Conversational AI Assistant
Ask questions directly from meeting transcript.

### Example:
```bash
What decisions were made?
Who is responsible for deployment?
What issues were discussed?
```

---

## 🔎 Semantic Search with RAG
- Embedding-based retrieval
- Chroma Vector Database
- Context-aware AI responses
- Reduced hallucinations

---

# 📸 Screenshots

## 🏠 AI Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 💬 AI Meeting Assistant

![Chat](screenshots/chat.png)

---

## 📄 Transcript & Insights

![Transcript](screenshots/transcript.png)

---

# 🏗️ System Architecture

```text
YouTube URL / Local File
            ↓
Audio Processing
            ↓
Speech-to-Text
   ├── Whisper
   └── Sarvam AI
            ↓
Transcript Generation
            ↓
AI Summarization
            ↓
Meeting Intelligence Extraction
   ├── Action Items
   ├── Key Decisions
   └── Open Questions
            ↓
Embeddings Generation
            ↓
Chroma Vector Database
            ↓
Retriever + RAG Pipeline
            ↓
Conversational AI Assistant
```

---

# ⚡ AI Workflow

## 1️⃣ Audio Processing
- Converts media into WAV format
- Mono channel conversion
- 16kHz optimization for speech models

---

## 2️⃣ Intelligent Audio Chunking
Long meetings are divided into smaller chunks for:
- Better scalability
- Faster processing
- API safety
- Improved transcription reliability

---

## 3️⃣ Speech Recognition
### Whisper
Used for:
- English transcription
- Local speech recognition

### Sarvam AI
Used for:
- Hinglish transcription
- Hindi-English mixed conversations

---

## 4️⃣ AI Summarization
The transcript is:
- Split into chunks
- Summarized individually
- Combined into one final summary

This solves:
- LLM context limitations
- Long transcript handling

---

## 5️⃣ RAG-based Question Answering
When user asks a question:

1. Question embeddings are generated
2. Relevant transcript chunks are retrieved
3. Context is injected into LLM prompt
4. AI generates grounded response

This improves:
- Accuracy
- Semantic understanding
- Hallucination reduction

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Python

## AI / NLP
- LangChain
- Mistral AI
- Whisper
- Sarvam AI

## Vector Database
- ChromaDB

## Embeddings
- HuggingFace Embeddings
- all-MiniLM-L6-v2

## Audio Processing
- yt-dlp
- pydub
- FFmpeg

---

# 📂 Project Structure

```text
AI-Meeting-Assistant/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── backend/
│   │
│   ├── core/
│   │   ├── extractor.py
│   │   ├── rag_engine.py
│   │   ├── summarizer.py
│   │   ├── transcriber.py
│   │   └── vector_store.py
│   │
│   ├── utils/
│   │   └── audio_processor.py
│   │
│   ├── api.py
│   ├── requirements.txt
│   └── .env
│
├── screenshots/
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/sumitghugare/ai-meeting-intelligence-assistant.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Add Environment Variables

Create `.env`

```env
MISTRAL_API_KEY=your_key
SARVAM_API_KEY=your_key
```

---

## Run Backend

```bash
uvicorn api:app --reload
```

---

## Run Frontend

Open:

```text
frontend/index.html
```

using Live Server.

---

# 🚀 Future Improvements

- 🎙️ Speaker diarization
- ⏱️ Timestamp-based retrieval
- 📄 PDF export
- ⚛️ React frontend
- ☁️ Cloud deployment
- 📊 Analytics dashboard
- ⚡ Real-time transcription

---

# 📈 Learning Outcomes

This project helped build practical experience in:

- Generative AI
- Retrieval-Augmented Generation (RAG)
- LangChain
- Vector Databases
- Semantic Search
- Speech Recognition
- Prompt Engineering
- FastAPI
- AI System Design

---

# 👨‍💻 Author

## Sumit Shivaji Ghugare

AI/ML Engineer | Generative AI Enthusiast

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
