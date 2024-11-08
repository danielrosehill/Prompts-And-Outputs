---
title: "Local LLMs with Fedora support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. Please provide a list of local LLM platforms that can be run on Fedora

# Output

If you're looking to run local Large Language Models (LLMs) on Fedora, there are several platforms available that cater to different needs and preferences. Here are some of the most robust options:

## OpenLLM

- **Overview**: OpenLLM allows you to run open-source LLMs like Llama 3.2, Qwen2.5, and Phi3 as OpenAI-compatible APIs. It provides a built-in chat UI and supports enterprise-grade cloud deployment with Docker and Kubernetes.
- **Features**: Supports a wide range of models, offers a chat interface, and allows for custom model integration.
- **Installation**: You can install it via pip with `pip install openllm` and start a server using `openllm serve`[1].

## Ollama

- **Overview**: Ollama is designed to run LLMs locally without internet access, making it a good choice for privacy-conscious users. It supports models like Gemma and Llama.
- **Features**: Offers various model sizes (e.g., 2b, 7b, 13b) depending on your hardware capabilities.
- **Installation**: Install using a script from their website or through manual methods. It's compatible with Fedora and other major Linux distributions[2][4].

## LM Studio

- **Overview**: LM Studio is a cross-platform tool that lets you run LLMs on your computer entirely offline. It supports models from providers like Llama, Mistral, and Phi.
- **Features**: Provides an in-app chat UI, supports downloading models from Hugging Face, and is designed for privacy by keeping data local.
- **Installation**: Available for Linux, Mac, and Windows. You can download it from their website[3][5].

## GPT4All

- **Overview**: GPT4All is an easy-to-use framework that allows running LLMs locally across different operating systems. It integrates well with applications like VSCode.
- **Features**: Offers API integration and supports a variety of models for local use.
- **Installation**: Downloadable from the nomic-ai GitHub repository[4].

## llama.cpp

- **Overview**: A backend technology that powers local LLM tools like Ollama. It's efficient and requires minimal configuration.
- **Features**: Supports significant model inferences locally with excellent performance.
- **Installation**: Clone the repository from GitHub and build the project using C/C++[4].

These platforms provide various options to run LLMs locally on Fedora, catering to different levels of technical expertise and hardware configurations. Whether you prioritize privacy, ease of use, or flexibility in model selection, there is likely a suitable tool among these options.

 