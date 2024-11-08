---
title: "LLMs I could run locally on workstation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here are the specifications of my current desktop. please provide a list of some LLMs that I could run locally and how I might go about installing them on my machine. Remember of course that I would need to use the computer for general purpose tasks while running the LLMs, so they can't degrade performance too drastically

# Output

Based on your desktop specifications, you have a capable system that can run several local Large Language Models (LLMs) without significantly impacting general-purpose tasks. Here are some LLMs you could run locally and how to install them:

## Recommended LLMs

1. LLaMA 2 7B
2. Mistral 7B
3. Phi-2
4. GPT-J 6B
5. BLOOM 7B

These models should run comfortably on your system, leaving resources for other tasks. The 12GB GPU will be particularly helpful for accelerating inference.

## Installation Method

The easiest way to install and run these LLMs locally is using Ollama, a user-friendly tool for managing local LLMs. Here's how to set it up:

1. Install Ollama:
   ```
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Once installed, you can run models directly from the command line. For example:
   ```
   ollama run llama2
   ```

3. To use a specific model size or variant, you can specify it like this:
   ```
   ollama run llama2:7b
   ```

4. You can also run models with a graphical interface by installing Open WebUI:
   ```
   docker run -d --name openwebui -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --restart always ghcr.io/open-webui/open-webui:main
   ```

   Then access the interface at `http://localhost:3000` in your web browser.

## Additional Considerations

- Your system should handle these models well, but monitor resource usage to ensure it doesn't impact other tasks.
- Start with smaller models (like 7B parameter versions) and work your way up if you need more capability.
- Experiment with different models to find the best balance of performance and resource usage for your needs.
- Consider using Ollama's GPU acceleration feature to leverage your NVIDIA GPU for faster inference.

By using Ollama, you can easily manage and switch between different LLMs without complex setup procedures, making it ideal for your use case of running LLMs alongside other tasks on your desktop[1][2][3][4][5].
 