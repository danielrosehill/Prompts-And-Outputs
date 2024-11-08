---
title: "API access to Ollama 70B"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's talk about companies which provide API access to Code Llama 70B. Can you give me a complete list and guide me towards a cost-effective option?

# Output

Based on the search results and available information, here's a list of companies providing API access to Code Llama 70B, along with guidance towards cost-effective options:

1. Together AI
2. Anyscale
3. Perplexity
4. Replicate
5. Microsoft Azure (Azure AI)
6. Amazon Web Services (AWS SageMaker)
7. Google Cloud (Vertex AI)
8. Deepinfra
9. Hyperbolic
10. Fireworks
11. Cerebras
12. Lepton AI
13. OctoAI
14. SambaNova
15. Groq

To guide you towards a cost-effective option, let's look at some pricing information from the search results:

1. Deepinfra offers the lowest blended price at $0.36 per million tokens.
2. Hyperbolic is the second most cost-effective at $0.40 per million tokens.
3. Cerebras and Groq follow, with prices around $0.60-$0.65 per million tokens.

For a cost-effective solution, Deepinfra or Hyperbolic appear to be the best options based on pricing alone. However, it's important to consider other factors such as:

1. Output speed: Cerebras (568 tokens/s) and SambaNova (410 tokens/s) are the fastest.
2. Latency: Cerebras (0.24s) and Perplexity (0.25s) have the lowest latency.
3. Context window: Most providers offer the full 128k context window, but some may be limited.

To get started with a cost-effective option:

1. Sign up for an account with Deepinfra or Hyperbolic.
2. Obtain an API key from your chosen provider.
3. Use their API documentation to integrate Code Llama 70B into your project.

For example, using Python with Replicate (which isn't the cheapest but offers easy integration):

```python
import replicate

for event in replicate.stream(
    "meta/meta-llama-3-70b-instruct",
    input={
        "prompt": "Write a Python function to calculate factorial"
    },
):
    print(str(event), end="")
```

Remember to consider your specific needs, such as request volume, speed requirements, and additional features offered by each provider. It might be worth testing a few options to find the best balance of cost and performance for your use case.






## Extracted Prompts
[[Prompts/API access to Ollama 70B.md#Prompt 1|Prompt 1]]
