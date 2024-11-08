---
title: "Most powerful LLMs I could run locally"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. Please provide me with a list of the most powerful LLMs that I could run on this desktop and how I could run it.

For every LLM that I could run, tell me how I could run it and provide some thoughts on how to monitor resource consumption.

Start with the most powerful and work your way down to the least, providing 5 options

# Output

Based on your desktop specifications and the information available, here are 5 powerful LLMs you could run locally, listed from most to least powerful, along with instructions on how to run them and monitor resource consumption:

1. Mixtral 8x7B

How to run:
Use Ollama to run Mixtral 8x7B locally:
```
ollama run mixtral
```

Resource monitoring:
- Use `top` or `htop` in the terminal to monitor CPU and RAM usage.
- For GPU monitoring, use `radeontop` for your AMD GPU:
  ```
  sudo dnf install radeontop
  radeontop
  ```

Thoughts: Mixtral 8x7B is one of the most powerful open-source LLMs available. With your 32GB RAM and powerful CPU, you should be able to run it comfortably, but it may be resource-intensive[3][6].

2. LLaMA 2 13B

How to run:
Use Ollama to run LLaMA 2 13B:
```
ollama run llama2:13b
```

Resource monitoring:
- Same as Mixtral 8x7B.
- Additionally, use Ollama's verbose mode for more detailed information:
  ```
  ollama run llama2:13b --verbose
  ```

Thoughts: LLaMA 2 13B should run smoothly on your system, offering a good balance between performance and resource usage[1][6].

3. Falcon 40B

How to run:
Use LM Studio to download and run Falcon 40B:
1. Download LM Studio from their official website.
2. Install and launch the application.
3. Search for and download the Falcon 40B model.
4. Select the model and start chatting.

Resource monitoring:
- LM Studio provides built-in performance metrics in its interface.
- Use system monitoring tools mentioned earlier for overall system performance.

Thoughts: Falcon 40B is a powerful model, but it may push your system's limits. Monitor resource usage closely and be prepared to close other applications if needed[3][4].

4. GPT-J 6B

How to run:
Use GPT4All to run GPT-J 6B:
1. Download GPT4All from their official website.
2. Install and launch the application.
3. Download the GPT-J 6B model from within the app.
4. Select the model and start using it.

Resource monitoring:
- GPT4All displays token generation speed in its GUI.
- Use system monitoring tools for overall performance.

Thoughts: GPT-J 6B should run comfortably on your system, allowing for smooth operation alongside other tasks[3][6].

5. BLOOM 7B

How to run:
Use Ollama to run BLOOM 7B:
```
ollama run bloom:7b
```

Resource monitoring:
- Use the same methods as mentioned for Mixtral 8x7B and LLaMA 2 13B.

Thoughts: BLOOM 7B is a versatile model that should run efficiently on your system, leaving resources for other tasks[3][4].

General resource management tips:
1. Use `cpulimit` to restrict CPU usage for LLM processes if needed:
   ```
   sudo dnf install cpulimit
   cpulimit -l 50 -p [PID]
   ```
2. Create a specific cgroup for LLM processes to limit resources:
   ```
   sudo systemd-run --unit=llm-limiter --scope -p MemoryMax=16G -p CPUQuota=50% [your command to run LLM]
   ```
3. Start with smaller models and gradually increase complexity as you optimize resource usage[1].

Your system's 32GB of RAM and powerful CPU should handle most of these models comfortably. However, always monitor system performance and be prepared to adjust settings or close resource-intensive applications when running larger models.

# Input
Based on your desktop specifications and the desire for a balanced option that offers good performance without overly taxing your system, I would recommend trying LLaMA 2 13B. Here's why:

1. Performance: LLaMA 2 13B offers a good balance between capability and resource usage. It's more powerful than the 7B variant but less demanding than larger models like Mixtral 8x7B or Falcon 40B.

2. Resource usage: With your 32GB of RAM and powerful CPU (Intel Core i7-12700F), LLaMA 2 13B should run comfortably without overwhelming your system resources.

3. Ease of use: You can easily run it using Ollama, which is straightforward to set up and use.

To run LLaMA 2 13B on your system:

1. Install Ollama (if you haven't already):
   ```
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Run the model:
   ```
   ollama run llama2:13b
   ```

To monitor resource consumption:

1. Use `htop` for overall system monitoring:
   ```
   sudo dnf install htop
   htop
   ```

2. For GPU monitoring (AMD Radeon RX 7700 XT):
   ```
   sudo dnf install radeontop
   radeontop
   ```

3. Use Ollama's verbose mode for model-specific information:
   ```
   ollama run llama2:13b --verbose
   ```

This setup should provide a good balance of performance and resource usage, allowing you to run the LLM while still having system resources available for other tasks. If you find that LLaMA 2 13B runs very smoothly and you want to try something more powerful, you could consider stepping up to Mixtral 8x7B. Conversely, if you need to free up more resources, you could step down to LLaMA 2 7B.
 