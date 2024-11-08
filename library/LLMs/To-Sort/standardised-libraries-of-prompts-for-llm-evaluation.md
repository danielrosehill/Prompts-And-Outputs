---
title: "Standardised libraries of prompts for LLM evaluation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Are there existing and/or standardised libraries of prompts which are intended for the purpose I'm describing (evaluating and comparing LLMs?) If so, can you list a few? Do you think that it still makes sense for me to create my own prompt evaluation library? I feel like it's better to have one that's honed in on the use-cases that are of interest to me

# Output

There are a few existing and standardized libraries of prompts for **evaluating and comparing LLMs** that you might find useful:

### Existing Prompt Libraries:
1. **BIG-bench (Beyond the Imitation Game Benchmark)**:
   - A large-scale benchmark for LLMs covering a variety of tasks, including reasoning, language understanding, and creative tasks.
   - [BIG-bench on GitHub](https://github.com/google/BIG-bench)

2. **EleutherAI's LM Evaluation Harness**:
   - A framework for evaluating language models across many benchmarks, including text classification, reasoning, and factual recall.
   - [EleutherAI LM Evaluation](https://github.com/EleutherAI/lm-evaluation-harness)

3. **SuperGLUE**:
   - A benchmark suite for LLMs that includes tasks like reading comprehension, textual entailment, and more.
   - [SuperGLUE Benchmark](https://super.gluebenchmark.com/)

4. **PromptSource**:
   - A collection of templates for prompting and evaluating LLMs, organized by task and dataset.
   - [PromptSource on GitHub](https://github.com/bigscience-workshop/promptsource)

### Should You Create Your Own Prompt Library?
Yes, creating your own prompt evaluation library is still beneficial, especially if your use cases are unique or specific to your interests. While existing libraries cover broad tasks, a customized prompt library allows you to focus on tasks, formats, and criteria that are **highly relevant to your needs**, enabling better evaluation and comparison for your specific workflows or projects. You can also adjust evaluation metrics to suit your goals.