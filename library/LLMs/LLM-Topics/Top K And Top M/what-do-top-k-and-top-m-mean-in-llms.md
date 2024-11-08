---
title: "What do top K and top M mean in LLMs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 
Based on the information provided in the search results, here's an explanation of Top-K and Top-P in Large Language Models (LLMs):

Top-K and Top-P are token selection strategies used during text generation by LLMs to control the randomness and diversity of the output. They both operate on the probability distribution of potential next tokens that the model predicts.

Top-K:
- Limits the selection to only the K most probable tokens at each step of generation.
- For example, if K=5, only the 5 tokens with the highest probabilities are considered for selection.
- Pros: Reduces chances of generating highly improbable words, provides more controlled output.
- Cons: Can be too restrictive if K is set too low, potentially leading to repetitive outputs.

Top-P (also called Nucleus Sampling):
- Selects tokens based on a cumulative probability threshold P.
- The model considers tokens until their cumulative probability exceeds P.
- For example, if P=0.9, it selects tokens until their combined probability is 90% or higher.
- Pros: More dynamic than Top-K, adapts to the probability distribution, captures more diversity.
- Cons: Less predictable than Top-K, risk of generating implausible outputs if P is set too high.

Key differences:
- Top-K uses a fixed number of tokens, while Top-P adapts based on the probability distribution.
- Top-P is generally considered more flexible and can produce more diverse outputs.

Both parameters allow fine-tuning of the balance between creativity and coherence in generated text. They are often used in conjunction with temperature, another parameter that affects the randomness of token selection.

The choice between Top-K and Top-P (and their specific values) depends on the desired output characteristics and the specific application of the LLM.

 