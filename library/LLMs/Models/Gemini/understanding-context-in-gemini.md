---
title: "Understanding context in Gemini"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's say that I'm using Gemini. I want to provide contextual information that the LLM will remember. IN this case, I'd like you to remember details about my Output Hub project so that I don't need to keep repeating the same details. What's the best way to do that currently?

# Output

You're right, remembering contextual information is important for a seamless and efficient interaction with LLMs like Gemini. Unfortunately, the current version of Gemini, like most other large language models, lacks a persistent memory. This means it forgets everything after each interaction.

However, there are a few ways you can get around this limitation and "teach" Gemini about your Output Hub project:

**1. Include Context in Every Prompt:**

* **Start each prompt with a summary:**  Briefly introduce your project, including key details like its purpose, technology, and goals. For example: "I'm working on Output Hub, a project that aims to... using technology like... My goal is..."
* **Reference previous interactions:**  If you've already discussed specific aspects of the project, mention them explicitly in your current prompt. This provides continuity and helps the model remember relevant information.

**2. Leverage External Tools:**

* **Create a project documentation:** Compile a comprehensive document that outlines all the essential details about your Output Hub project. You can then reference this document in your prompts or ask Gemini to access it for information. 
* **Use a knowledge base:**  Consider building a knowledge base or using an existing one like Wikipedia or a project wiki. You can then instruct Gemini to query this knowledge base for information about your project.

**3. Utilize Plugins:**

* **Custom plugins:** If Gemini supports plugins, you could create a custom plugin that stores and retrieves information about your Output Hub project. This would allow you to access the project data directly within the Gemini interface. 
* **Third-party plugins:** Look for existing plugins that could help with information storage and retrieval, such as a plugin that integrates with a specific database or knowledge management system.

**4. Future Improvements:**

* **Persistent memory:**  It's likely that future versions of Gemini and other LLMs will incorporate persistent memory capabilities. This would allow them to retain information across multiple interactions, eliminating the need for constant reintroduction.
* **Contextual reasoning:**  Improved contextual reasoning will enable LLMs to better understand the relationships between different pieces of information and infer missing details, reducing the need to explicitly provide everything upfront.

**Note:**  Currently, there's no single "best" way to achieve persistent memory with Gemini. The most effective approach will depend on your specific project and the available resources. 

As LLMs continue to evolve, we can expect more robust solutions for managing and retrieving contextual information. Until then, combining careful prompt engineering with external tools and plugins can help you bridge the gap and effectively interact with Gemini while working on your Output Hub project. 
