---
title: "How do local LLMs handle tokenisation and context?"
---

Local LLMs and cloud LLMs share similar fundamental principles for token handling and context management, but there are important differences in their implementation and limitations.

## Token Processing

Local LLMs break down text into tokens just like cloud-based models, with tokens representing words, parts of words, or individual characters\[2]. The tokenization process is essential for text processing and directly impacts:

- Model performance
- Memory usage
- Processing speed
- Cost efficiency (when applicable)

## Context Window Considerations

### Memory and Resource Usage

The context window in local LLMs faces significant hardware constraints:

- GPU memory usage and running time scale linearly with the KV (Key-Value) cache size\[1]
- Processing long contexts requires substantial computational resources
- Memory requirements increase quadratically with context length\[6]

### Performance Impact

Local LLMs experience several performance-related effects with longer contexts:

- **Speed vs Context Length**: Larger context windows result in slower response times\[6]
- **Missing Middle Problem**: Models often struggle with accurately recalling information from the middle of long contexts\[6]
- **Attention Patterns**: Models show better performance at the beginning (primary bias) and end (recency bias) of the context\[6]

## Hardware Requirements

Running local LLMs with large context windows requires significant hardware resources:

**Multi-GPU Setups**:

- 2x RTX 4090: Initial cost $4,000, monthly maintenance \~$150\[3]
- 4x RTX 4090: Initial cost $8,000, monthly maintenance \~$200\[3]

## Optimization Techniques

Recent developments have introduced methods to handle long contexts more efficiently:

- **GemFilter**: A novel approach that can reduce input tokens by up to 1000x while maintaining performance\[1]
- **KV Cache Optimization**: Techniques for compressing and managing the Key-Value cache to improve memory efficiency\[1]
- **Token Selection**: Algorithms that identify and retain the most relevant tokens while discarding less important ones\[1]

## Practical Implications

When choosing between local and cloud LLMs, consider:

- **Control**: Local deployment offers more control over the model and data processing\[4]
- **Latency**: Local models can provide faster response times for certain applications\[4]
- **Scalability**: Local setups have limited scalability compared to cloud solutions\[4]
- **Privacy**: Running locally ensures data stays within your infrastructure\[4]

&#x20;
