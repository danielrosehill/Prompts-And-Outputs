---
title: "Who currently can access the 32K GPT4o"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To access the **32K token version of GPT-4** (GPT-4-32k), you currently need to be a user of **OpenAI’s API** rather than the web interface. Here's how you can access it and some relevant details:

### 1. **API Access**
   - **OpenAI API**: To use the 32K token version of GPT-4, you must have access to the GPT-4 model via the **OpenAI API**. You can sign up for an API key via the [OpenAI Platform](https://platform.openai.com/signup).
   - Once you have API access, you can choose the **GPT-4-32k** model for your calls, which provides up to **32,768 tokens** (four times the capacity of the 8K version).
   - To select the model in API calls, you will specify the model as `gpt-4-32k`.

### 2. **Availability and Pricing**
   - **Pricing**: The cost for using GPT-4-32k is higher than the 8K version due to the increased token capacity. You can check the current pricing for API usage on OpenAI's [pricing page](https://openai.com/pricing).
   - **Access**: Initially, GPT-4-32k may not be available to all users by default, and you might need to request higher-tier API access, especially if you plan on using it at scale.

### 3. **Web UI (ChatGPT) Version**
   - The **ChatGPT web UI** (accessible through chat.openai.com) currently defaults to the **8K token** version of GPT-4 for users, including those subscribed to the **ChatGPT Plus** plan.
   - As of now, OpenAI has not provided direct access to the 32K version via the web interface (ChatGPT), and it's exclusively available through the API.

### Steps to Get Access to GPT-4-32k via API:
1. **Sign Up** for an account on the [OpenAI platform](https://platform.openai.com/).
2. **Get API Access**: Once registered, obtain an API key.
3. **Set Model to `gpt-4-32k`**: When making requests via the API, specify the `gpt-4-32k` model.
4. **Monitor Token Usage**: Keep in mind that the token limits cover both the input prompt and the output response, and costs are proportional to the number of tokens used.

### Conclusion:
To use the GPT-4-32k model, you’ll need to access it through the OpenAI API rather than the web-based ChatGPT interface. The web UI generally provides access to the 8K token version, and the larger model is available through API calls with a higher pricing structure.