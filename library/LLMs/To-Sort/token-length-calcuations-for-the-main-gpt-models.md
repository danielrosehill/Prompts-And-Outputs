---
title: "Token length calcuations for the main GPT models"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s the raw markdown version of the GPT token usage matrix for **GPT-3.5**, **GPT-4 (8K)**, and **GPT-4 (32K)**, with input percentages ranging from 20% to 100%:

```markdown
| **Model**     | **Input %** | **Input Tokens** | **Output Tokens** |
|---------------|-------------|------------------|-------------------|
| GPT-3.5       | 20%         | 819              | 3277              |
| GPT-3.5       | 30%         | 1228             | 2868              |
| GPT-3.5       | 40%         | 1638             | 2458              |
| GPT-3.5       | 50%         | 2048             | 2048              |
| GPT-3.5       | 60%         | 2457             | 1639              |
| GPT-3.5       | 70%         | 2867             | 1229              |
| GPT-3.5       | 80%         | 3276             | 820               |
| GPT-3.5       | 90%         | 3686             | 410               |
| GPT-3.5       | 100%        | 4096             | 0                 |

| **Model**     | **Input %** | **Input Tokens** | **Output Tokens** |
|---------------|-------------|------------------|-------------------|
| GPT-4 (8K)    | 20%         | 1638             | 6554              |
| GPT-4 (8K)    | 30%         | 2457             | 5735              |
| GPT-4 (8K)    | 40%         | 3276             | 4916              |
| GPT-4 (8K)    | 50%         | 4096             | 4096              |
| GPT-4 (8K)    | 60%         | 4915             | 3277              |
| GPT-4 (8K)    | 70%         | 5734             | 2458              |
| GPT-4 (8K)    | 80%         | 6554             | 1638              |
| GPT-4 (8K)    | 90%         | 7373             | 819               |
| GPT-4 (8K)    | 100%        | 8192             | 0                 |

| **Model**     | **Input %** | **Input Tokens** | **Output Tokens** |
|---------------|-------------|------------------|-------------------|
| GPT-4 (32K)   | 20%         | 6553             | 26215             |
| GPT-4 (32K)   | 30%         | 9830             | 22938             |
| GPT-4 (32K)   | 40%         | 13107            | 19661             |
| GPT-4 (32K)   | 50%         | 16384            | 16384             |
| GPT-4 (32K)   | 60%         | 19660            | 13108             |
| GPT-4 (32K)   | 70%         | 22937            | 9831              |
| GPT-4 (32K)   | 80%         | 26214            | 6554              |
| GPT-4 (32K)   | 90%         | 29491            | 3277              |
| GPT-4 (32K)   | 100%        | 32768            | 0                 |
```

This table shows how the input and output token limits are split based on the total token window for each model.