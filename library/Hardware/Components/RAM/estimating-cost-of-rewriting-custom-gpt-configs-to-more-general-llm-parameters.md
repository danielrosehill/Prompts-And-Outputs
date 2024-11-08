---
title: "Estimating cost of rewriting custom GPT configs to more general LLM parameters"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

let's say each config text is 500 characters and that there are 300 texts. how much would the rewriting take with gpt 3.5?

# Output

To calculate the cost of rewriting 300 configuration texts with GPT-3.5, we'll break it down into **token usage** and **OpenAI pricing**.

### 1. **Understanding Tokens:**
   - GPT-3.5 **counts characters as tokens**. Generally, 1 token is about 4 characters of English text, including spaces and punctuation.
   - **500 characters** (each config text) equates to roughly **125 tokens** per text.
   - **Total tokens for 300 texts**:  
     125 tokens/text * 300 texts = **37,500 tokens**.

### 2. **GPT-3.5 Pricing** (as of now):
   - The cost for GPT-3.5-turbo is **$0.0015 per 1,000 tokens**.

### 3. **Calculating the Cost**:
   - **Token usage for input**: For each text of 500 characters (125 tokens), GPT-3.5 will also generate a response of roughly the same length. Let’s assume an additional 125 tokens per text for output.
     - Total tokens per request = 125 tokens (input) + 125 tokens (output) = **250 tokens**.
   - **Total tokens for 300 texts** = 250 tokens/text * 300 texts = **75,000 tokens**.
   - **Cost**: 75,000 tokens / 1,000 tokens = **75 units**.
   - **Price**: 75 units * $0.0015 = **$0.1125**.

### **Total Estimated Cost**:
For rewriting **300 texts of 500 characters each**, the cost would be approximately **$0.11** using GPT-3.5-turbo.

This is a rough estimate based on standard token usage patterns, and actual costs may vary slightly depending on the specific prompts and responses. However, it's safe to say the cost would be **well under $1** for this batch of text rewrites.