---
title: "Long outputs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

i find that i keep running into text limits when using ChatGPT and Claude over the web UI. is it easier to avoid these when using the API? Or are there perhaps specific LLMs that do not have these limits? I am doing things like editing SQL DDLs which means that the outputs can easily extend past 1000 words

# Output

When using the web UI of models like ChatGPT and Claude, you're more likely to encounter text limits, especially for tasks that generate long outputs like editing SQL DDLs. The API offers more flexibility in handling larger inputs and outputs, as the token limits tend to be higher than those on the web UI.

For example, OpenAI's GPT-4 Turbo has a token limit of 128k tokens, which allows for much longer interactions compared to the typical web interface limit. Similarly, Anthropic's Claude models offer higher token limits when accessed through the API.

However, even with the API, there are still token limits, so if your tasks regularly exceed these, you might need to:

1. **Chunk Your Inputs/Outputs**: Break down your tasks into smaller parts and handle them sequentially.
2. **Stream Outputs**: If available, streaming can allow you to handle longer outputs more effectively.
3. **Use Models with Higher Token Limits**: As mentioned, using models like GPT-4 Turbo via the API can provide significantly higher token limits.

If you're finding that you're consistently running into limits, utilizing the API and these strategies should help mitigate those issues.## Extracted Prompts
[[Prompts/Autocapture/Long outputs.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Long outputs.md#Prompt 1|Prompt 1]]
