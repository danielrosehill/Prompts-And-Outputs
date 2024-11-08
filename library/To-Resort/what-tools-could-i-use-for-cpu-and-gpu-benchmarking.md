---
title: "What tools could I use for CPU and GPU benchmarking_"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt


To benchmark the CPU (Intel Core i7-12700F) and GPU (AMD Radeon RX 7700 XT Pulse Gaming) on your Fedora 40 workstation, here are some recommended tools:

# Output

To benchmark the CPU (Intel Core i7-12700F) and GPU (AMD Radeon RX 7700 XT Pulse Gaming) on your Fedora 40 workstation, here are some recommended tools:

### CPU Benchmarking Tools:
1. **Phoronix Test Suite**:
   - One of the most popular open-source benchmarking platforms for Linux.
   - It offers a wide range of tests, including CPU, GPU, and other hardware components.
   - You can install it via the terminal:
     ```bash
     sudo dnf install phoronix-test-suite
     ```
   - It provides detailed performance results, which can be compared with online benchmarks.

2. **sysbench**:
   - A simple and effective tool for benchmarking the CPU and other system components.
   - You can install it using:
     ```bash
     sudo dnf install sysbench
     ```
   - To run a CPU benchmark, you can use:
     ```bash
     sysbench --test=cpu --cpu-max-prime=20000 run
     ```

### GPU Benchmarking Tools:
1. **GLMark2**:
   - A popular GPU benchmarking tool that tests the performance of OpenGL.
   - To install it:
     ```bash
     sudo dnf install glmark2
     ```
   - You can run the benchmark by typing:
     ```bash
     glmark2
     ```

2. **Basemark GPU**:
   - A cross-platform GPU benchmark that tests performance under Vulkan, OpenGL, and more.
   - You can download it from their [official site](https://www.basemark.com/benchmarks/basemark-gpu/) and run it on Fedora.

These tools will provide both comprehensive and specific performance metrics for your system's CPU and GPU. If you'd like to know more about how to interpret the results or additional benchmarking tools, feel free to ask!