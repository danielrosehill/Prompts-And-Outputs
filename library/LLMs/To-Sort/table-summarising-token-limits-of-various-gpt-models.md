---
title: "Table summarising token limits of various GPT models"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s a matrix table summarizing the **token limits** for various models of GPT, including earlier models often used for cost optimization.

| **Model**           | **Token Limit** | **Description**                                                               | **Use Cases**                                   |
| ------------------- | --------------- | ----------------------------------------------------------------------------- | ----------------------------------------------- |
| **GPT-4 (32K)**     | 32,768 tokens   | Large-context model in GPT-4, available via API only.                         | Large documents, extended conversations.        |
| **GPT-4 (8K)**      | 8,192 tokens    | Standard GPT-4 model, available via API and in ChatGPT web UI (ChatGPT Plus). | General-purpose, rich-text tasks, dialogue.     |
| **GPT-3.5 (Turbo)** | 4,096 tokens    | Available in ChatGPT free and Plus versions.                                  | Cost-efficient, most common usage model.        |
| **GPT-3.5**         | 4,096 tokens    | Original GPT-3.5 version, often used in API for cost optimization.            | Good for typical GPT applications.              |
| **GPT-3 (Davinci)** | 4,096 tokens    | GPT-3's most powerful variant (davinci-003), high-quality text generation.    | Complex tasks, creative writing, summarization. |
| **GPT-3 (Curie)**   | 2,048 tokens    | Faster and cheaper than Davinci, still powerful.                              | Moderation, classification, language tasks.     |
| **GPT-3 (Babbage)** | 2,048 tokens    | Faster and cheaper than Curie, lower performance.                             | Simple tasks, lower cost.                       |
| **GPT-3 (Ada)**     | 2,048 tokens    | Fastest and cheapest GPT-3 model.                                             | Simple text tasks, least expensive.             |

### Notes:
- **Token definition**: A token can be as short as one character or as long as one word (usually ~4 characters in English). For example, the sentence "ChatGPT is great!" is 5 tokens.
- **Shared token limit**: Both the input (prompt) and the model's output share the same token pool. The longer the input, the fewer tokens available for the response.
- **Cost optimization**: Using smaller GPT-3 models (Curie, Babbage, Ada) can help reduce costs when high-quality generation isn't necessary.

### Practical Examples:
- If you're working with large documents or want to have extended conversations, **GPT-4 (32K)** is ideal but more expensive.
- For general usage, **GPT-4 (8K)** or **GPT-3.5** are often the best trade-off between cost and performance.
- For cost-sensitive, simpler tasks like text classification or basic summarization, **GPT-3 (Curie)** or **GPT-3 (Ada)** can be good alternatives.

