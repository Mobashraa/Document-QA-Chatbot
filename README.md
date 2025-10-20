# Document-QA-Chatbot

This project is an AI-powered Question Answering (Q&A) Bot that allows users to upload a document (PDF, TXT, DOCX, etc.) and ask natural language questions about its content.
The bot uses LangChain’s retrieval chain, OpenAI embeddings, and a FAISS vector database to provide accurate and context-aware answers.

🚀 Features

✅ Extracts and processes information from unstructured documents
✅ Stores document embeddings locally using FAISS
✅ Uses OpenAI’s GPT models for natural language reasoning
✅ Employs retrieval-augmented generation (RAG) via create_retrieval_chain
✅ Works offline after embedding generation (no re-upload needed)
✅ Modular and extendable — can easily integrate Groq or other LLMs

🏗️ Project Architecture
Document(s)
     │
     ▼
[LangChain Loader] ─► Extracts Text
     │
     ▼
[OpenAI Embeddings] ─► Converts Text → Vectors
     │
     ▼
[FAISS Vector Store] ─► Stores Embeddings Locally
     │
     ▼
[Retriever] ─► Fetches Relevant Chunks
     │
     ▼
[OpenAI LLM + Prompt Template]
     │
     ▼
[create_retrieval_chain] ─► Generates Final Answer
