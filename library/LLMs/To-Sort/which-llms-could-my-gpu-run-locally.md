---
title: "Which LLMs could my GPU run locally"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here's my current GPU. Please tell me what kind of LLMs I could realistically run locally with this hardware:

AMD Radeon RX7700 XT Pulse Gaming 12GB Sapphire

# Output

Based on your current GPU, the AMD Radeon RX 7700 XT with 12GB VRAM, you can realistically run several LLMs locally, though with some limitations compared to higher-end or NVIDIA GPUs. Here's an analysis of what you can expect:

## Capabilities of the RX 7700 XT for LLMs

1. **VRAM Capacity**: With 12GB of VRAM, you have a decent amount of memory for running medium-sized models.

2. **Architecture**: The RX 7700 XT is based on RDNA 3 architecture, which includes AI acceleration hardware, specifically Wave Matrix Multiply Accumulate (WMMA) support.

3. **Memory Bandwidth**: It offers about 430 GB/s memory bandwidth, which is beneficial for LLM inference.

## LLMs You Can Realistically Run

1. **Smaller to Medium-Sized Models**:
   - You should be able to run models up to about 13B parameters, such as LLaMA 2 13B or similar sized models.
   - Mistral 7B and other 7B models should run comfortably.

2. **Quantized Models**:
   - Using quantization techniques, you might be able to run larger models in 4-bit or 8-bit precision, potentially allowing for models up to 20B parameters.

3. **Stable Diffusion**:
   - Your GPU is capable of running Stable Diffusion models, including SDXL, which requires more than 8GB VRAM.

4. **Code Generation Models**:
   - Code Llama and similar code generation models in their smaller variants (7B, possibly 13B) should be feasible.

## Limitations and Considerations

1. **Large Models**: You won't be able to run very large models like GPT-3 175B or GPT-4 locally.

2. **Performance**: While capable, the performance might not match equivalent NVIDIA GPUs due to better optimization and support for CUDA in many AI frameworks.

3. **Software Support**: AMD GPUs have improved in terms of AI support, but you may still encounter some compatibility issues or need to use specific versions of software.

4. **ROCm Compatibility**: Ensure you're using a compatible version of ROCm (AMD's open-source software stack for GPU computing) that works with your system and doesn't interfere with other GPU functionalities.

## Practical Advice

1. Start with smaller models like Mistral 7B or LLaMA 2 7B and work your way up.

2. Experiment with quantization techniques to run larger models with reduced precision.

3. Keep an eye on updates for AMD GPU support in popular LLM frameworks and tools.

4. Be prepared to do some troubleshooting, as AMD GPUs might require more setup and configuration compared to NVIDIA GPUs for some LLM tasks.

In conclusion, while your RX 7700 XT is capable of running a variety of LLMs locally, you'll be mostly limited to models up to 13B parameters in full precision, with the possibility of running larger models using quantization techniques. It's a good GPU for experimenting with and running medium-sized LLMs, but it may require more effort in setup and optimization compared to NVIDIA alternatives.





## Extracted Prompts
[[Prompts/Which LLMs could my GPU run locally.md#Prompt 1|Prompt 1]]
