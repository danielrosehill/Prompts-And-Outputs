---
title: "Using a cloud LLM to pick a local LLM"
---

# Prompting Strategy

- Supply hardware parameters as context
- Supply screenshot of options in LM Studio as additional context
- Prompt then asks for specific recommendations

---

Based on the search results and your hardware specifications, here's a clear recommendation:

## Best Option: DeepSeek Coder V2 Lite

**Why This Version:**

- 15.7B parameter size will run well on your hardware\[1]
- Supports 338 programming languages\[1]
- 128K context window\[1]
- Strong Python performance (81.1% on HumanEval)\[4]
- Only requires 10.36GB storage\[1]

## Performance Benefits

**Capabilities:**

- Excellent Python code generation
- Comparable performance to much larger models
- Fast inference on your hardware
- Full offline capability

## Hardware Compatibility

Your system (i7-12700F, 64GB RAM, RX 7700 XT 12GB) is well-suited for this model because:

- 64GB RAM is more than sufficient
- RX 7700 XT 12GB provides adequate VRAM
- Storage requirements (10.36GB) are minimal

## Installation

The model can be downloaded directly through LM Studio as shown in your screenshot\[1]. Look for:

- Model name: "DeepSeek Coder V2 Lite"
- Format: GGUF
- Size: 10.36GB

This version offers the best balance of performance and resource usage for your hardware while maintaining excellent Python code generation capabilities.

&#x20;
