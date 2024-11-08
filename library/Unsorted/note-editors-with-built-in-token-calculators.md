---
title: "Note editors with built in token calculators"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are several ways to draft prompts in note editors while calculating tokens for GPT models, including options that work well on **Fedora Linux**. While there might not be native token calculators in most note editors by default, some tools and plugins can help you achieve this functionality.

### 1. **Obsidian with Plugins** (Works on Fedora)
   - **Obsidian** is a popular note-taking tool that works on Fedora Linux, and it supports **plugins** that could be adapted to help with token calculations.
   - **How to calculate tokens**:
     - Use the **Obsidian GPT-3 Plugin** or **Custom Code Snippets** to integrate token counting logic into your notes.
     - You can use **JavaScript or Python scripts** within Obsidian to count the tokens of selected text, potentially through the OpenAI API or by integrating a local tokenizer.

   **Steps**:
   1. Install Obsidian on Fedora from [Obsidian.md](https://obsidian.md/).
   2. Add a custom plugin for **token counting** or write a custom snippet that uses an API like OpenAI's to estimate tokens based on the text in your prompt.

### 2. **VS Code with Token Calculator Extensions** (Works on Fedora)
   - **Visual Studio Code (VS Code)** works on Fedora and has **extensions** that can integrate token calculation with prompt drafting.
   - **Extensions**:
     - **ChatGPT Tokenizer**: A VS Code extension that allows you to draft prompts and calculates the token count directly in the editor.
     - **Prompt Tools**: An extension focused on helping users write prompts for LLMs, including token calculation.
   
   **Steps**:
   1. Install VS Code from [Microsoft's repository](https://code.visualstudio.com/) or use **VSCodium** for an open-source variant.
   2. Search for **ChatGPT Tokenizer** or **Prompt Tools** in the VS Code extensions marketplace and install the one that fits your needs.
   3. You’ll be able to draft your prompt, and the extension will show you how many tokens you’ve used, helping you optimize your input.

### 3. **Joplin with Custom Scripts** (Works on Fedora)
   - **Joplin** is an open-source note-taking application that works on Fedora. Although it doesn’t have native token calculation, you can use **custom Python scripts** or plugins to calculate tokens.
   - You can set up a script that calculates the token count from your notes and integrates it into the interface.

   **Steps**:
   1. Install Joplin on Fedora from [Joplin’s website](https://joplinapp.org/).
   2. Use a **Python script** to calculate tokens from your prompt. Joplin allows running external commands, so you can use this to calculate the token count after drafting your prompt.

### 4. **Markdown Editors + Token Calculator Integration**
   - Many **markdown editors** like **Typora** or **MarkText** work on Fedora. While they don’t natively support token calculation, you can pair them with token calculation tools by writing a simple script to estimate the number of tokens in your markdown files.
   - Use **Python scripts** that count tokens based on the GPT tokenizer and trigger them with a hotkey or external tool.

### 5. **Custom Script + Any Editor (Sublime Text, Vim, Gedit)**
   - For other editors like **Sublime Text**, **Vim**, or **Gedit**, you can use custom **Python** or **JavaScript** scripts that interact with the OpenAI tokenizer to count tokens in real time or upon request.
   - Example: You can write a **Python script** that uses the OpenAI tokenizer to count tokens in the text you're drafting a**n**d integrate it with the editor of your choice.

### 6. **Online Note Editors with Token Calculation**
   - If you prefer online editors, **Notion** or **Google Docs** can be used in combination with **browser extensions** or external scripts that provide token counting capabilities.
   - **Prompt Perfect** and **AIPRM for ChatGPT** are browser extensions that help optimize prompts and calculate tokens in real time, but these are typically for Chrome-based browsers.

### Conclusion:
For **Fedora Linux**, **VS Code** with token calculator extensions like **ChatGPT Tokenizer** is one of the best options. If you prefer lightweight or open-source tools, **Obsidian** with custom plugins or **Joplin** with scripts also work well. Additionally, you can use custom Python scripts for token calculation in almost any text editor to create a seamless workflow for drafting and optimizing prompts.

