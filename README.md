# RAG_Retrieval-Augmented_Generation

Personal accumulation: 

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by integrating external knowledge retrieval. It retrieves relevant information from a vector database and combines it with user queries to generate accurate, grounded, and explainable responses. Ideal for Q&amp;A, chatbots, and knowledge-based systems.

# 🧠 RAG (Retrieval-Augmented Generation)

RAG（检索增强生成）是一种结合 **信息检索 (Retrieval)** 与 **文本生成 (Generation)** 的技术架构。  
它能让大语言模型（LLM）在生成回答前先从外部知识库中检索相关信息，从而提供更准确、有依据的答案。

---

## 🔹 Embedding 模型简介

**Embedding 模型**的作用是判断一段文字与用户问题之间的语义相关性。

- 输入是一段文字；输出是一个固定长度的向量（数组）。  
- 这个向量是对原文的语义压缩，信息被浓缩，但核心含义保留。  
- 语义相似的文本，其向量之间的距离更近，可用于判断相关性。  
- 实际中 embedding 向量的维度通常为 1000~3000。  
- 用户问题同样会被嵌入为向量，与知识库中的文本向量进行相似度匹配。  
- AI 模型随后读取这些“最相近”的内容，再生成最终答案。

---

## 🔹 Chunking：AI 如何处理长文档？

当原始文本太长时，RAG 会将其切分为多个 **chunk（文本块）**，常见方式包括：

- 按字数切分  
- 按句子切分  
- 按段落切分  

每个小块再通过 embedding 模型转化为向量。  
为了高效存储与检索这些向量，就需要使用 **向量数据库（Vector Database）**。

---

## 🔹 常见的向量数据库

- 🪶 **Pinecone**  
- 💾 **Chroma**  
- 🧩 **PostgreSQL (pgvector)**  

这些数据库支持快速相似度检索：输入一个向量，即可找到与之“最接近”的几段文本。

---

## 🔹 RAG 的完整检索流程

1. 用户输入问题  
2. 将问题通过 Embedding 模型转化为向量  
3. 从向量数据库中检索相似度最高的若干文本块  
4. 将检索到的文本与问题一同发送给大语言模型生成答案  

➡️ 这就是一个完整的 **RAG 流程（Retrieval → Augmentation → Generation）**

---

## ⚠️ RAG 的局限性

1. **文档切分策略不统一**：不同文档结构差异大，切分方式难以适配所有场景。关键句可能被截断。  
2. **缺乏全局视野**：模型仅能看到被检索到的局部内容，可能忽略上下文关联。

---

## 🧩 优化方案

- 明确代词指代，将“你、我、他”替换为具体人名或实体。  
- 使用大模型参与切分，让 chunk 更贴近语义边界。  

---

## 📘 总结

RAG 是一种让大模型“带着知识工作”的架构。  
通过 Embedding 与向量检索，它能有效降低幻觉率，让 AI 回答更加准确、可靠。  
适用于文档问答、知识库系统、智能客服、法律/医学信息检索等多种场景。

---

_✨ Author: Filly Minghao LUO — Personal learning and practice on RAG architecture._
