---
title: "LLMs that can handle long outputs in a chat UI"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

As you know I'm trying to generate a CSV with 1,000 rows from an LLM. Are there any LLMs that I could use to do this in the chat interface without running into tokenisation issues?

# Output

Yes, there are several LLMs that can handle large token limits, which would allow you to generate a CSV with 1,000 rows without running into tokenization issues:

1. **Claude by Anthropic**: Claude 2 and Claude 3 support up to 100,000 tokens, which makes them ideal for large tasks like generating a CSV with 1,000 rows. You can easily use these in an API or chat interface without concerns about token limits.

2. **GPT-4 (32k context window)**: Available through OpenAI’s API, GPT-4 with a 32,768-token context window can handle large datasets, including generating a 1,000-row CSV, provided the individual tokens don’t exceed the limit.

These tools are designed to handle large requests like generating lists or datasets programmatically.

# What token settings would I need

To generate a CSV with 1,000 rows, you need to adjust the **max tokens** setting based on the approximate token consumption of each row. Here's a rough estimate for token settings:

- Each row typically takes around 10-15 tokens (depending on length).
- For 1,000 rows, you'd need approximately **10,000–15,000 tokens**.

To achieve this:
1. Use an LLM like **Claude 2/3** (with a 100k token limit).
2. For **GPT-4 with 32k** tokens, you might need to break the task into smaller batches of about 500 rows at a time. 

Set **max tokens** to 30,000 or as high as possible to handle larger outputs.