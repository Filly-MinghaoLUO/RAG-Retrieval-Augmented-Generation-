# 🧠 RAG (Retrieval-Augmented Generation)

**Personal accumulation project by Filly (Minghao LUO).**

Retrieval-Augmented Generation (**RAG**) enhances large language models (**LLMs**) by integrating external knowledge retrieval.  
It retrieves relevant information from a vector database and combines it with user queries to generate accurate, grounded, and explainable responses.  
Ideal for **Q&A**, **chatbots**, and **knowledge-based systems**.

---

## 🔹 Embedding Model Overview

The **embedding model** determines how closely a piece of text relates to a user’s query.

- Input: a piece of text  
- Output: a fixed-length vector representation  
- The vector is a compressed semantic form — the meaning remains while details are condensed  
- Similar texts have closer vector distances, enabling semantic similarity detection  
- Real-world embedding dimensions often range from **1,000–3,000**  
- User queries are also embedded and compared to document vectors to find relevant information

---

## 🔹 Chunking: How AI Handles Long Documents

When dealing with long documents, RAG divides text into smaller **chunks** for better retrieval and reasoning.

Common chunking strategies:
- By **character count**  
- By **sentence**  
- By **paragraph**

Each chunk is embedded and stored in a **vector database**, enabling fast similarity-based retrieval.

---

## 🔹 Common Vector Databases

- 🪶 **Pinecone**  
- 💾 **Chroma**  
- 🧩 **PostgreSQL (pgvector)**  

These databases allow efficient similarity searches — given a query vector, they find the most related chunks.

---

## 🔹 RAG Workflow

1. User submits a question  
2. The question is converted into an embedding vector  
3. The system retrieves the most semantically similar chunks from the vector database  
4. The question and retrieved text are combined and passed to the language model  

➡️ This completes the **RAG cycle: Retrieval → Augmentation → Generation**

---

## ⚠️ Limitations

1. **Chunking strategy challenges** — no universal method fits all document types; key phrases may be split  
2. **Lack of global context** — the model only sees the retrieved segments, not the entire document

---

## 🧩 Possible Improvements

- Replace vague pronouns (*he, she, they*) with explicit entity names  
- Use LLM-assisted **semantic chunking** to preserve contextual meaning

---

## 📘 Summary

This repository serves as **a personal accumulation and experimental project** exploring the implementation of RAG systems.  
By combining embeddings, vector databases, and large language models, it demonstrates how retrieval-augmented methods enhance accuracy and factual grounding in AI-generated responses.

---

_✨ Author: Filly Minghao LUO — Personal RAG learning and implementation project._
