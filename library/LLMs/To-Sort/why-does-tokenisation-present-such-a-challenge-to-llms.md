---
title: "Why does tokenisation present such a challenge to LLMs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you explain how tokenisation presents a constraint in this respect (LLM's being able to leverage lengthy context documents)? What I'm asking is: why is it exactly that LLMs can only generate outputs from finite inputs when they are such powerful programs?

# Output

Tokenization, and the limitations it imposes, is a key factor in understanding why LLMs (Large Language Models) can only generate outputs from finite inputs, despite their power. Let’s break down what this means and how it relates to the model’s ability to use context effectively.

### 1. **What is Tokenization?**
Tokenization is the process of breaking down text into smaller units (tokens) that the model can process. These tokens are typically words, parts of words, or even individual characters, depending on the model and the complexity of the language. 

For example:
- The sentence "ChatGPT is powerful." could be tokenized into:
  - **4 tokens**: ["ChatGPT", "is", "powerful", "."]
  - In some cases, more complex words might be broken into sub-tokens. For instance, "powerful" could be broken down into ["power", "ful"].

LLMs like GPT-4 operate on these tokens. Everything you input into the model (and everything it outputs) is handled in terms of tokens, not words or characters.

### 2. **Token Limits**
Every LLM has a limit to how many tokens it can handle at one time. For example:
- GPT-4’s **context window** can handle up to 8,192 tokens (for GPT-4 Turbo) or 32,768 tokens (for the larger versions of GPT-4).
- This window includes both the input (your prompt, including all the context) and the output (the model's response).

This means that the model cannot process more than this number of tokens at any given moment. If the combined size of the input context and the generated output exceeds this token limit, it will either truncate the input or be unable to generate more output.

### 3. **Why Token Limits Exist**
Token limits are a practical constraint imposed by the architecture of transformers, the deep learning model that underlies GPT-4 and other similar models. Here’s why these limits are necessary:

#### a. **Memory and Computational Resources**
LLMs are incredibly powerful, but that power comes at a cost. The transformer model that powers LLMs requires immense computational resources to process inputs. Each token that the model processes requires significant memory and computational power to calculate the relationships between that token and all other tokens in the input.

The transformer architecture uses **attention mechanisms**, which allow the model to focus on different parts of the input to generate contextually appropriate responses. However, as the input length increases, the amount of computation required grows **quadratically**. For example:
- If there are 1,000 tokens, the model must compute relationships between every pair of tokens, leading to 1,000 x 1,000 comparisons.
- If this grows to 8,000 tokens, the number of comparisons jumps to 8,000 x 8,000, which significantly increases the computational cost.

This scaling behavior necessitates a cap on how many tokens the model can handle at once.

#### b. **Performance Trade-offs**
Even with enough computational power, processing extremely long contexts could slow down the model significantly and affect performance. LLMs need to make real-time decisions about which parts of the input are most important for generating relevant output. This becomes more difficult as the input size increases because the model would need to "attend" to many more potential tokens.

The balance between model size (number of parameters) and token length must be maintained to ensure that the LLM remains responsive, accurate, and efficient.

### 4. **How Token Limits Affect Context Usage**
When you provide a lengthy context document, the LLM can only "see" a portion of it at a time based on the token limit. If the entire document is within the token limit, the model can process and use all of it. But if the document exceeds the token limit, here’s what happens:
- **Truncation**: The model may truncate part of the input context, typically starting from the oldest part (beginning of the document), unless specified otherwise.
- **Selective Use of Context**: Models like GPT try to prioritize the most relevant or recent information within the token window to generate a useful output. However, long-term context retention across interactions remains a challenge because of this limit.

### 5. **Workarounds and Improvements**
Some techniques and approaches are being developed to mitigate these token limitations:
- **Summarization**: Before providing a long document as context, the document can be summarized to reduce the token load while retaining key information. This reduces the number of tokens while preserving important context.
- **Chunking**: Splitting long documents into chunks and processing them sequentially can allow the LLM to work with long documents more effectively. Each chunk can be provided in separate interactions, and the user (or model) can summarize or carry forward the relevant parts of each chunk.
- **Memory Systems**: Some newer implementations of LLMs, such as experimental "memory" features (e.g., OpenAI's memory feature in ChatGPT), aim to store information persistently across sessions, allowing the model to refer to past context without needing to re-process it fully each time.
- **Hybrid Approaches**: Using external systems like databases or APIs to store and query large sets of information can allow LLMs to refer to important data without needing to carry all that information within a single session.

### 6. **Why LLMs Are Still Powerful Despite Token Limits**
Even though LLMs are bound by token limits, they are still extremely powerful due to their ability to:
- **Generate contextually relevant responses**: Within the token window, LLMs are very good at interpreting and generating high-quality responses based on complex input.
- **Model vast amounts of knowledge**: Even with a finite context window, the model can pull from its pre-trained knowledge to augment responses, filling gaps where the input context might fall short.
- **Real-time reasoning**: Despite processing only a limited number of tokens, the model can reason and produce coherent outputs by focusing on the most relevant information within the token window.

### Conclusion
Tokenization is crucial to how LLMs process input, and the token limit is a practical constraint based on memory, computational costs, and architectural limitations. While LLMs are powerful, they are optimized for real-time performance and cannot handle infinitely large inputs at once. As technology evolves, techniques like memory systems, summarization, and chunking can help address these constraints and improve how LLMs leverage context over extended interactions.