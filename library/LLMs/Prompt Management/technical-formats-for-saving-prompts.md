---
title: "Technical formats for saving prompts"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Nice work. What about technical formats. Best to save it as a JSON, markdown, both, something else?

# Output

It depends on how you plan to use and retrieve your prompts. Here’s a breakdown of the advantages of each format:

### **Markdown**: 
- **Advantages**:
  - Readable and easy to modify.
  - Great for human interaction and organizing prompts in a text editor or document-based system.
  - Works well with many documentation tools like GitHub, Notion, etc.

  **Example**:
  ```markdown
  ## Small Business Management Tool Recommendations
  
  **Category**: Business Tools, SaaS Solutions
  
  **Use Case**: Request for business management software with specific features and requirements for a consultant.
  
  **Core Prompt**:  
  "I'm looking for a tool to help me manage my small business. ... *[remaining text]*"
  
  **Special Instructions**:  
  Exclude certain tools. Focus on SaaS solutions under $100/month.
  
  **Notes**:  
  Can be modified to ask for other business models (e.g., inventory-based, product-based).
  ```

### **JSON**: 
- **Advantages**:
  - Best for structured data storage and programmatic retrieval.
  - Easily parsed by software, useful if you're using databases or automating prompt handling.
  - Can integrate with code-based systems (e.g., for AI models or automation tools).

  **Example**:
  ```json
  {
    "title": "Small Business Management Tool Recommendations",
    "category": "Business Tools, SaaS Solutions",
    "use_case": "Request for business management software with specific features and requirements for a consultant.",
    "core_prompt": "I'm looking for a tool to help me manage my small business. ... *[remaining text]*",
    "special_instructions": "Exclude certain tools (Zoho, Odoo, Indian companies). Focus on SaaS solutions under $100/month.",
    "notes": "Can be modified to ask for other business models (e.g., inventory-based, product-based)."
  }
  ```

### **Both**:
- **Advantages**:
  - You get the best of both worlds: human readability from Markdown and structured data from JSON.
  - You can maintain the Markdown for documentation and export the JSON when programmatic access is needed.

If you're primarily using these prompts for manual reference or light automation, **Markdown** works well. If you're integrating these into more complex systems or automations (like NoCodeDB, Airtable, etc.), **JSON** will be more efficient.

If unsure, storing both formats ensures flexibility down the road!