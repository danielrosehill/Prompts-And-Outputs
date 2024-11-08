---
title: "How to run an LLM locally - GUIs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

# Output

Yes, there are several ways to use local LLMs with a graphical user interface (GUI). Based on the information provided and my knowledge, here are some popular options:

1. Ollama with Open Web UI
Ollama is a tool for running LLMs locally, and Open Web UI provides a ChatGPT-like interface for interacting with these models.

How to set it up:
- Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh`
- Install Docker (required for Open Web UI)
- Run Open Web UI:
  ```
  docker run -d --name openwebui -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --restart always ghcr.io/open-webui/open-webui:main
  ```
- Access the interface at `http://localhost:3000` in your web browser

2. Text Generation WebUI
This is a versatile interface that supports various model formats and has many extensions.

How to set it up:
- Clone the repository: `git clone https://github.com/oobabooga/text-generation-webui`
- Follow the installation instructions in the repository's README

3. LM Studio
LM Studio provides a clean UI and focuses on GGUF format models.

How to set it up:
- Download LM Studio from their official website
- Install and launch the application
- Use the interface to download and run models

4. Kobold CPP
Known for its clean and easy-to-use interface.

How to set it up:
- Download from: https://github.com/LostRuins/koboldcpp
- Follow the installation instructions in the repository's README

5. H2O GPT
Good for file ingestion and has PDF and web search integration.

How to set it up:
- Clone the repository: `git clone https://github.com/h2oai/h2ogpt`
- Follow the installation instructions in the repository's README

To use these interfaces:

1. Install the chosen interface following its specific instructions.
2. Download a compatible LLM (e.g., LLaMA 2, Mistral, GPT-J) through the interface or separately.
3. Load the model in the interface.
4. Start interacting with the LLM through the provided GUI.

Remember to monitor your system resources, as running large language models locally can be computationally intensive. Your system with 32GB RAM and a powerful CPU should handle most 7B to 13B parameter models comfortably, but always be prepared to adjust settings or close other applications if needed.

 