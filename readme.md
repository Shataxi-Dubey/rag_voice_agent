# 🎙️ RAG-Based Voice Agent  

This project is a **Retrieval-Augmented Generation (RAG) based Voice Agent** that lets you interact with documents through voice.  

- 📂 Upload **multiple PDF and TXT files**.  
- 🧩 The system chunks your documents and stores embeddings in a **Qdrant vector database**.  
- 🎤 After uploading documents, you can either:  
  - **Record your voice** using the built-in recorder, or  
  - **Upload an audio file**.  
- 🤖 The question is passed to an LLM, and the response is generated back in **voice form**.  

The system uses:  
- **Streamlit frontend** (for uploading documents and recording/uploading voice).  
- **FastAPI backend** (for handling processing, chunking, and querying).  
- **Qdrant vector database** (for storing embeddings of document chunks).  

---

## ⚡ Getting Started  

### 1. Clone the repository  
```bash
git clone https://github.com/Shataxi-Dubey/rag_voice_agent.git
cd rag_voice_agent
```
### 2. Start the application with docker compose
``bash
docker compose up --build
```
---

This will:

- Start **Qdrant vector database**.  
- Start the **FastAPI backend**.  
- Start the **Streamlit frontend**.  

---

## 🖥️ Application Flow  

1. Upload one or more **PDF/TXT files** in the frontend.  
2. Once uploaded, you will see options to:  
   - **Record audio directly** 🎙️  
   - **Upload a recorded audio file** 🎧  
3. The backend will:  
   - Convert your **voice to text**.  
   - Query the relevant **chunks from Qdrant**.  
   - Pass the **query + context** to the LLM.  
   - Convert the response back to **speech**.  
4. The answer will be returned as **voice output**.  

---

## 📦 Tech Stack  

- **Frontend** → Streamlit  
- **Backend** → FastAPI  
- **Database** → Qdrant (Vector DB)  
- **Orchestration** → Docker Compose  

# Important: replace the placeholders in .env.example with the API keys and then rename it to .env. If not done so there will be many API key missing errors.
