---
title: "YAML frontmatter for agents repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm going through the custom GPTs that I previously created and adding them to Hugging Face The custom agents are currently a github repo I need to add frontmatter to them which notes: 1) Creation date 2) Added to Hugging Face (Y/N) 3) Hugging Face URL 4) ChatGPT URL

# Output

Here’s how you can add the required **frontmatter** to your custom GPTs for managing them in a GitHub repository and documenting their status on Hugging Face.

### **Frontmatter Format**:
This assumes that each of your custom agents is stored in individual files (such as Markdown or YAML) where you can easily add metadata at the top of the file. Here’s a suggested format for adding frontmatter to your custom GPT agents:

```yaml
---
creation_date: "YYYY-MM-DD"
added_to_hugging_face: "Yes/No"
hugging_face_url: "https://huggingface.co/your-model-url"
chatgpt_url: "https://chat.openai.com/chat/your-model-url"
---
```

### **Example**:

```yaml
---
creation_date: "2024-01-15"
added_to_hugging_face: "Yes"
hugging_face_url: "https://huggingface.co/your-username/custom-gpt-model"
chatgpt_url: "https://chat.openai.com/chat/custom-gpt-id"
---
```

### **Fields Explanation**:
- **`creation_date`**: The date you originally created the custom agent.
- **`added_to_hugging_face`**: A simple "Yes" or "No" indicating whether the agent has been uploaded to Hugging Face.
- **`hugging_face_url`**: The direct URL to the Hugging Face model page.
- **`chatgpt_url`**: The direct URL to the ChatGPT version of the custom model.

### **How to Use**:
- You can add this frontmatter at the beginning of each custom agent file in your GitHub repo.
- This will help you track which agents are live on Hugging Face and where users can find them.

By adding this frontmatter, you can better organize and keep track of your custom GPT agents across both platforms.