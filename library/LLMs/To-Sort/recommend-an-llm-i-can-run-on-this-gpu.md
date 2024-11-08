---
title: "Recommend an LLM I can run on this GPU"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. As you now, I use Fedora. So recommend a program for me to run one of these locally

# Output


Based on your use of Fedora Linux and the information provided in the search results, I recommend using Ollama to run LLMs like Llama 3 locally on your system. Here's why Ollama is a good choice for Fedora users:

1. Easy Installation: Ollama can be installed on Fedora using a simple curl command:

   ```
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Wide Model Support: Ollama supports various models, including Llama 3, Gemma, and Mixtral. You can choose the model size (2B, 7B, 13B, 34B, or 70B) based on your hardware capabilities[4].

3. Local Execution: Ollama allows you to run AI models locally and offline, which is ideal if you have privacy concerns about cloud-based services[4].

4. GPU Support: If you have an NVIDIA or AMD GPU, Ollama can utilize it for improved performance[5].

5. Systemd Integration: You can set up Ollama as a startup service on Fedora, making it easy to manage[5].

To get started with Ollama on Fedora:

1. Install Ollama using the curl command mentioned above.
2. Choose a model from the Ollama library (e.g., `ollama run llama3` or `ollama run gemma`).
3. If you want to set it up as a service, follow the instructions in the manual install section of the Ollama documentation[5].

Keep in mind that the hardware requirements depend on the model size you choose. For example, running a 7B parameter model would require at least 16GB of RAM[2].

If you encounter any issues with the installation script on Fedora, you can try the manual installation method described in the Ollama documentation[5].

Ollama provides a good balance of ease of use, performance, and flexibility for running LLMs locally on Fedora Linux.




## Extracted Prompts
[[Prompts/Recommend an LLM I can run on this GPU.md#Prompt 1|Prompt 1]]
