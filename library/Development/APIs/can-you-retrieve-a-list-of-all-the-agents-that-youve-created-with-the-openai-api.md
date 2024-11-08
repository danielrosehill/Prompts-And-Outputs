---
title: "Can you retrieve a list of all the agents that you've created with the OpenAI API?"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt:** You are asking if it's possible to retrieve a list of all GPT agents you have created using the OpenAI API.

Currently, the OpenAI API does not provide a direct endpoint to list all the custom GPT agents (or "fine-tuned models") associated with your account. However, you **can** list any **fine-tuned models** you've created with the API, which could act as a proxy if you have customized agents via fine-tuning.

Here’s how you can retrieve a list of your fine-tuned models using the OpenAI API:

### 1. **Using the OpenAI API to List Fine-Tuned Models:**
You can use the following command to list fine-tuned models:

```bash
curl https://api.openai.com/v1/fine-tunes \
  -H "Authorization: Bearer YOUR_API_KEY"
```

This will return details about all the fine-tuned models (agents) created on your account.

### 2. **Listing Deployed Agents (Tools for Custom Implementations):**
If you've built custom GPT agents through custom implementations or orchestration (like LangChain), you may need to rely on how you structured your agents. In such cases, you would have to maintain a list in your backend infrastructure, as OpenAI’s API doesn’t natively support a specific "list agents" call.

### Conclusion:
There is **no direct API call** to list all GPT agents created through OpenAI’s standard API, but you can list fine-tuned models, which are a key form of customized GPT agent. If you're using another framework to manage agents, keeping track of them manually (or with orchestration tools) is necessary for now.
