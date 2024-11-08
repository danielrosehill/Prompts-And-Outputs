---
title: "Editing default config file for ChatGPT TUI"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s the updated configuration file for your **ChatGPT TUI**, based on your request to set the model to **GPT-4** (assuming `gpt-4` is the correct model identifier in the TUI) and increasing the max tokens to the highest available:

```yaml
api_key: "sk-proj-xxxxxxxBKI-IZDsVCvZsA-F3DHPcOKe-xxxxxxx2MrBDnKq_G-xxxxxxx_Zr_Z2FpwRhYCj-R5rf8SDkA"
auth_header: Authorization
auth_token_prefix: 'Bearer '
auto_create_new_thread: true
command_prompt: '[%datetime] [Q%counter] [%usage]'
completions_path: /v1/chat/completions
context_window: 8192  # Depending on the model, GPT-4 might allow up to 8192 or more
debug: false
frequency_penalty: 0
max_tokens: 8192  # Set to the maximum for GPT-4, which can handle up to 8192 tokens (or higher with certain GPT-4 versions)
model: gpt-4  # Changed from gpt-3.5-turbo to gpt-4
models_path: /v1/models
multiline: false
name: openai
omit_history: false
output_prompt: ""
presence_penalty: 0
role: You are a helpful assistant.
skip_tls_verify: false
temperature: 1
thread: default
top_p: 1
track_token_usage: true
url: https://api.openai.com
```

### Explanation of Changes:
1. **Model**: Changed from `gpt-3.5-turbo` to `gpt-4`.
2. **Max Tokens**: Increased to `8192` to reflect the maximum token length that **GPT-4** can handle in some versions. The token limit can vary based on the specific GPT-4 model (some support up to 32k tokens, so you may need to adjust based on your usage and API plan).
3. **Context Window**: Kept as `8192` since it's typically in sync with the maximum token size for certain GPT-4 models.

This configuration should now be set for **GPT-4** with the maximum token length available. Make sure the OpenAI plan you're using supports **GPT-4** and high token counts. If you're using a specific GPT-4 model (like `gpt-4-32k` for the 32k context version), update the `model` field accordingly.