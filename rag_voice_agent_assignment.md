# 🧪 Assignment: End-to-End RAG Service with Voice Agent

## 📌 Objective

The goal of this assignment is to build an end-to-end Retrieval-Augmented Generation (RAG) system integrated with a voice-based conversational agent. This includes document ingestion, vector embedding, question-answering capabilities, and voice agent interaction—all served via FastAPI and exposed through a basic Streamlit UI.

---

## 📦 Modules Overview

### ✅ Module 1: RAG Service - Uploader

#### 🎯 Purpose
Enable uploading of documents, extracting and chunking text, embedding it, and indexing to a vector DB.

#### 📋 Tasks
- [ ] Create an **async FastAPI endpoint** to upload files (PDF, DOCX, TXT).
- [ ] Extract raw text from uploaded files.
- [ ] Chunk the text (using LangChain or custom splitter).
- [ ] Generate vector embeddings using HuggingFace models.
- [ ] Index the chunks into a Vector DB (Chroma, Elasticsearch, or Pinecone).

#### 🧰 Tools & Libraries
- FastAPI (async)
- LangChain / PyMuPDF / python-docx / PDFMiner 
- HuggingFace Transformers
- Qdrant

---

### ✅ Module 2: RAG Service - Query

#### 🎯 Purpose
Accept a user query, retrieve relevant chunks, and generate an answer using a deployed LLM.

#### 📋 Tasks
- [ ] Create a FastAPI **async endpoint** to receive user queries.
- [ ] Embed the query and perform similarity search on the Vector DB.
- [ ] Pass retrieved context + query to a model (e.g., Can use Groq/Gemini).
- [ ] Return the generated response to the client.

#### 🧰 Tools & Libraries
- FastAPI (async)
- Vector DB from Module 1

---

### ✅ Module 3: Voice Agent Integration

#### 🎯 Purpose
Allow voice-based interaction with a user, supporting both basic and RAG-based queries.

#### 📋 Tasks
- [ ] Integrate with a voice SDK (Vapi / ElevenLabs / LiveKit).
- [ ] Convert speech to text (STT).
- [ ] Identify query type (basic vs RAG).
- [ ] For RAG queries, call the query endpoint from Module 2.
- [ ] Convert response to speech using ElevenLabs or similar (TTS).

#### 🧰 Tools & Libraries
- ElevenLabs / Vapi / LiveKit
- FastAPI async endpoints
- Whisper / Google STT / AssemblyAI (for STT)
- ElevenLabs / TTS APIs (for TTS)

---

### ✅ Module 4: Frontend UI (Optional Chat History)

#### 🎯 Purpose
Expose upload and query interaction via a simple Streamlit frontend.

#### 📋 Tasks
- [ ] Create a Streamlit UI for:
  - File upload
  - Voice-based interaction (initiate call)
- [ ] Display conversation history (if using chat)
- [ ] Optionally store and retrieve chat history from MongoDB

#### 🧰 Tools & Libraries
- Streamlit
- HTTP calls to FastAPI endpoints
- MongoDB (via PyMongo)

---

## 🧪 Technologies to Use

| Area | Technology |
|------|------------|
| API Framework | FastAPI (async) |
| Vector Store | Chroma / Elasticsearch / Pinecone |
| LLM Inference | vLLM / HuggingFace |
| Frontend | Streamlit |
| Embeddings | HuggingFace / SentenceTransformers |
| Voice Agent | ElevenLabs / Vapi / LiveKit |
| STT/TTS | Whisper / ElevenLabs |
| DB (Optional) | MongoDB (chat history) |

---

## 📁 Folder Structure (Suggested)

```
rag_voice_agent/
├── backend/
│   ├── main.py
│   ├── uploader/
│   │   ├── routes.py
│   │   ├── utils.py
│   ├── query/
│   │   ├── routes.py
│   │   ├── rag_engine.py
│   ├── voice_agent/
│   │   ├── routes.py
│   │   ├── stt.py
│   │   ├── tts.py
│   ├── db/
│   │   ├── vector_db.py
│   │   ├── mongo.py
│   └── models/
│       ├── schemas.py
├── frontend/
│   ├── app.py
├── requirements.txt
├── README.md
```

---

## ✅ Deliverables

1. **FastAPI backend**
   - Upload file endpoint
   - Query endpoint
   - Voice agent integration endpoint

2. **Vector DB setup**
   - Working implementation of document indexing and retrieval

3. **Model inference**
   - LLM integration for response generation

4. **Streamlit UI**
   - File upload
   - Query interface (voice and/or text)
   - Optional chat history viewer

5. **Documentation**
   - Setup instructions
   - API contracts (OpenAPI / Swagger from FastAPI)
   - Architecture diagram (bonus)

---

## 🕓 Timeline

| Task | Time Estimate |
|------|---------------|
| Uploader & Indexing | 1-2 Days |
| Query Endpoint & RAG Logic | 1 Day |
| Voice Agent Integration | 1-2 Days |
| Frontend UI | 1 Day |
| Polish & Docs | 1 Day |

Total: **5-7 working days**

---

## 🎯 Evaluation Criteria

- Code structure and readability
- Async usage in FastAPI
- Integration depth (voice, LLM, vector DB)
- Simplicity and usability of frontend
- Creativity and initiative (e.g., logging, error handling, modularity)
- Documentation and clarity