---
title: "What's the best data type for storing rich text in Postgres"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


NocoDB, when storing "rich text" in a PostgreSQL database, the likely data type used is `TEXT`. The `TEXT` data type in PostgreSQL is designed to store variable-length character strings and can handle large amounts of text, making it suitable for storing rich text content, such as HTML, Markdown, or other formatted text.

Here’s why `TEXT` is commonly used for rich text:

*   **Flexible Length**: The `TEXT` type can store long strings of text without a predefined limit, which is important for rich text content that can vary greatly in length.
    
*   **Storage Efficiency**: PostgreSQL handles `TEXT` efficiently, storing large text data in a way that optimizes performance.
    
*   **Compatibility**: The `TEXT` type is widely supported and can accommodate various text encodings, making it suitable for rich text that may include special characters.
    

If you are working with rich text in NocoDB and using PostgreSQL as the backend, you can safely assume that the underlying data type for such fields is `TEXT`.