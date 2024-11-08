---
title: "LLMs and programs for running them locally"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great work! Could you refine that output a little by giving me an LLM -> program pairing. What I mean by that... for every LLM I could run, tell me how best I could run it (locally)

Also give me some instructions on how I can monitor RAM and CPU consumption to make sure that the LLM runs within reasonable limits. Can I configure throttling?

# Output

Certainly! I'll provide you with LLM -> program pairings and include information on monitoring resource consumption and throttling options.

## LLM -> Program Pairings

Here are some recommended pairings of LLMs and programs to run them locally on your system:

1. LLaMA 2 7B -> Ollama
2. Mistral 7B -> LM Studio
3. Phi-2 -> Ollama
4. GPT-J 6B -> GPT4All
5. BLOOM 7B -> LM Studio

These pairings are chosen based on compatibility, ease of use, and performance on your system specifications.

## Installation and Usage

### Ollama

1. Install Ollama:
   ```
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Run a model:
   ```
   ollama run llama2
   ```

### LM Studio

1. Download LM Studio from their official website.
2. Install and launch the application.
3. Use the interface to download and run models like Mistral 7B or BLOOM 7B.

### GPT4All

1. Download GPT4All from their official website.
2. Install and launch the application.
3. Use the interface to download and run models like GPT-J 6B.

## Monitoring Resource Consumption

To monitor RAM and CPU consumption while running LLMs, you can use built-in system tools or third-party applications:

### For Fedora (your OS):

1. Use the `top` command in the terminal:
   ```
   top
   ```
   This will show real-time CPU and memory usage for all processes.

2. For a more user-friendly interface, install and use `htop`:
   ```
   sudo dnf install htop
   htop
   ```

3. To monitor GPU usage (important for your AMD Radeon RX 7700 XT), use `radeontop`:
   ```
   sudo dnf install radeontop
   radeontop
   ```

### Specific to LLM tools:

- Ollama: Use the `--verbose` flag to see memory usage and generation speed:
  ```
  ollama run llama2 --verbose
  ```

- LM Studio: Provides built-in performance metrics in its interface.

- GPT4All: Displays token generation speed in its GUI.

## Throttling and Resource Management

1. **CPU Throttling**: 
   Use the `cpulimit` tool to restrict CPU usage:
   ```
   sudo dnf install cpulimit
   cpulimit -l 50 -p [PID]
   ```
   This limits the process to 50% CPU usage.

2. **RAM Limitations**:
   - For Ollama, you can set a maximum RAM usage in the Modelfile:
     ```
     PARAMETER max_memory 8000M
     ```
   - For LM Studio and GPT4All, choose smaller model sizes or quantized versions to reduce RAM usage.

3. **GPU Management**:
   - Use AMD's ROCm tools to monitor and manage GPU usage.
   - For Ollama, you can disable GPU acceleration if needed:
     ```
     OLLAMA_HOST=unix:///tmp/ollama.sock ollama serve
     ```

4. **Cgroups**:
   Fedora uses systemd, which leverages cgroups. You can create a specific cgroup for your LLM processes to limit resources:
   ```
   sudo systemd-run --unit=llm-limiter --scope -p MemoryMax=8G -p CPUQuota=50% [your command to run LLM]
   ```

Remember to monitor system performance while running LLMs and adjust settings as needed. Start with smaller models and gradually increase complexity as you optimize resource usage. Your system's 32GB of RAM and powerful CPU should handle most 7B parameter models comfortably, but always be prepared to close other resource-intensive applications when running LLMs locally.

 