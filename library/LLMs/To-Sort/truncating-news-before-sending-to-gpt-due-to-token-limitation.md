---
title: "Truncating news before sending to GPT due to token limitation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Won't I need to truncate the news to make sure it fits within the token limit?

# Output

Absolutely, you're correct. Given the **token limit** for GPT-4 and the potentially long content of news articles, you will need to truncate the news data to ensure it fits within the request token limit, especially when including **title**, **description**, and **full content** in the prompt.

Here are some approaches to **truncate and manage the content** effectively:

### 1. **Summarize or Truncate Content Before Sending to GPT-4**
- **Title and Description**: The title and description fields are usually quite short, so you can include them fully.
- **Content Field**: The main content of the article can be long, often exceeding the token limit, especially for GPT-4 which has a maximum context length of around 8,000 tokens (depending on the exact model).

#### Steps to Truncate:
1. **Check Length of Content**:
   - In **Make.com**, you can use a **Text Length** or **Set Variable** module to check the length of the content string.
   - If the content exceeds a certain number of characters, truncate it to fit within a reasonable limit for GPT-4 processing.

2. **Truncate to a Specific Number of Tokens**:
   - A common approach is to **truncate the content** to a certain number of words or characters. For example, you could limit the content to **500-1000 characters** to ensure that the entire prompt is manageable.

3. **Include Only Key Parts of Content**:
   - If available, use the **first few paragraphs** of the content, as they typically summarize the most important parts.
   - Alternatively, you could use the **description** or add a sentence like "For more details, refer to the full content at [link]" if you want to maintain a short prompt.

### 2. **Modified Prompt for Truncated Content**
Below is a modified version of the prompt to incorporate a truncated version of the content:

```json
{
  "model": "gpt-4",
  "prompt": "Please produce a situational report (SITREP) based on the news items that you will receive in the context. The situational report should take the format:\n\n# Israel Hizbullah\nUpdates about Israel's war with Hizbullah and the Northern front.\n\n# Israel and Iran\nUpdates about Israel's war with Iran.\n\n# Israel & Gaza and West Bank\nGeopolitical developments from the West Bank and Gaza.\n\n# Israel Foreign Policy\nMajor foreign policy developments.\n\n# Other Militant Groups\nOther military and geopolitical news.\n\nNews Context:\n\nTitle: {{title}}\nDescription: {{description}}\nTruncated content: {{truncated_content}}\n\nBased on the above context, generate a situational report (SITREP) in the specified format.",
  "max_tokens": 500,
  "temperature": 0.7
}
```

#### Key Points for Implementation in Make.com:
1. **Add a Variable to Truncate Content**:
   - Use a **Set Variable** module before the HTTP request to GPT-4.
   - Name this variable `truncated_content`.
   - Use a text function to **truncate** the content to a certain character limit, for example, the first 500 characters:
     - In the **Set Variable** module, add a formula like:
       ```make
       {{substring(content; 0; 500)}}
       ```
     - This will take the first **500 characters** of the content field.

2. **Adjust Truncation Length Dynamically** (Optional):
   - You could make the truncation length **dynamic** depending on the length of the **title** and **description**, to maximize usage of available tokens while ensuring the prompt doesn’t exceed the token limit.

3. **Include a Summary or Key Sentences** (Alternative Approach):
   - Instead of truncating blindly, use Make’s text tools or GPT-4 to generate a **summary** of the content beforehand. This way, you can include the most important details, rather than the first `n` characters, which may or may not be informative enough.

### Truncation Example in Make.com Flow:
1. **HTTP Module**: Get news from NewsAPI.
2. **Iterator**: Iterate over the `articles` array.
3. **Set Variable for Truncated Content**:
   - Use a **Set Variable** module.
   - Set `truncated_content` to `{{substring(content; 0; 500)}}` to get the first 500 characters.
4. **HTTP POST Request to GPT-4**:
   - Include `title`, `description`, and `truncated_content` in your prompt to create the SITREP.

### Example of a Shortened Prompt with Truncated Content:
- **Prompt**:
  ```text
  Please produce a situational report (SITREP) based on the news items that you will receive in the context. The situational report should take the format:

  # Israel Hizbullah
  Updates about Israel's war with Hizbullah and the Northern front.

  # Israel and Iran
  Updates about Israel's war with Iran.

  # Israel & Gaza and West Bank
  Geopolitical developments from the West Bank and Gaza.

  # Israel Foreign Policy
  Major foreign policy developments.

  # Other Militant Groups
  Other military and geopolitical news.

  News Context:

  Title: {{title}}
  Description: {{description}}
  Truncated content: {{truncated_content}}

  Based on the above context, generate a situational report (SITREP) in the specified format.
  ```
  
### Summary:
- **Truncate Long Content**: Use Make to truncate or summarize long content to ensure the prompt fits within GPT-4’s token limit.
- **Use Key Information**: Always include the **title** and **description** fully, and decide whether the full content is needed or just a summary.
- **Set Variable Module**: Use this module to handle truncation and extract only the essential parts of the article.

By properly truncating or summarizing the content, you ensure that GPT-4 can process all the information without running into token limitations, leading to more accurate and concise outputs.

Let me know if you need any help setting up these steps in Make.com!