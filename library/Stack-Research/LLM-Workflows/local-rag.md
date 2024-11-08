---
title: "Local LLM + RAG prototype setup"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



You are interested in building a prototype **Retrieval-Augmented Generation (RAG)** system on your local machine, using a **locally hosted large language model (LLM)**. Since you are running **OpenSUSE**, you would need tools that are compatible with Linux and can operate fully offline. Here’s a breakdown of tools and frameworks that can help you achieve this:

## 1. Local LLM Hosting Options

To host an LLM locally on OpenSUSE, you'll need to choose a framework that supports offline operation and is compatible with your hardware. Some of the best tools for this purpose include:

- **GPT4All**: This tool allows you to run various open-source models locally, including LLaMA, Mistral, and others. It has an easy-to-use interface and supports privacy-first applications where no data leaves your machine\[1]\[2]. You can also integrate it with RAG systems by connecting it to local document stores.
- **Llama.cpp**: A highly efficient C++ framework for running Meta’s LLaMA models locally. It is optimized for performance and works well even on modest hardware setups, making it a great choice for local inference\[1]\[2]. It can be integrated into custom applications or used as a backend for other tools.
- **Ollama**: A user-friendly platform that simplifies running LLaMA models locally. It supports Linux and allows you to run models like LLaMA 2 with minimal setup\[1]\[5]. Ollama also operates entirely offline, ensuring data privacy.
- **AnythingLLM**: This is an all-in-one open-source desktop app that integrates RAG capabilities with local LLM hosting. It supports multiple LLMs like Ollama, LMStudio, or LocalAI, and comes with built-in document embedding and vector storage options\[4].

## 2. Building the RAG System

For the RAG system itself, you will need components for both **retrieval** (to fetch relevant documents) and **generation** (to answer questions based on retrieved documents). Here are some tools that can help:

### A. Retrieval Component

- **Chroma** or **LanceDB**: These are vector databases that can store document embeddings for fast retrieval during the RAG process. Both databases are lightweight and can be used locally without requiring cloud services\[4].
- **LocalAI**: This framework supports text generation models like `llama.cpp` and `gpt4all.cpp`, but also includes support for embedding models like `all-MiniLM-L6-v2`, which is useful for document retrieval in RAG systems\[5].

### B. Generation Component

- Any of the local LLM frameworks mentioned earlier (e.g., GPT4All, Llama.cpp, Ollama) can serve as the generation engine in your RAG pipeline.

### C. Integration Frameworks

- **LangChain**: This Python framework is designed for building AI applications such as RAG systems. It provides abstractions for integrating retrieval mechanisms with generation models, making it easier to build a fully functional RAG pipeline\[6].
- **llmware**: A unified framework specifically designed for building RAG pipelines using small specialized models that can be deployed privately. It supports integration with various vector databases (e.g., Milvus, Chroma) and allows easy access to models from Hugging Face or other sources\[3].

## 3. Example Setup

Here’s how you could set up a basic prototype:

1. **Install GPT4All or Llama.cpp**:
   - For GPT4All:
     ```bash
     git clone https://github.com/nomic-ai/gpt4all.git
     cd gpt4all
     ./install.sh
     ```
   - For Llama.cpp:
     ```bash
     git clone https://github.com/ggerganov/llama.cpp.git
     cd llama.cpp
     make
     ```
2. **Set Up Document Embeddings**:
   - Use LocalAI to run an embedding model like `all-MiniLM-L6-v2` locally to generate embeddings from your documents.
   - Store these embeddings in a local vector database like Chroma or LanceDB.
3. **Build the Retrieval Pipeline**:
   - Use LangChain or llmware to connect your vector database to the LLM.
   - When a query is made, retrieve relevant documents based on their embeddings.
4. **Run Inference Locally**:
   - Use GPT4All or Llama.cpp to generate responses based on the retrieved documents.

This setup will allow you to build a fully local RAG system that operates offline on OpenSUSE.

&#x20;
