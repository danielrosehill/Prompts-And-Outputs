---
title: "Finding a better way to capture LLM outputs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm currently building a system for capturing LLM outputs and organising them in a sort of knowledge base. At the moment, I'm capturing them into Obsidian by copying and pasting. While I have developed some hotkeys for speeding up the process, it's quite inefficient. I've thought about using LLMs via their APIs, but this is expensive and (more problematically) it makes it much harder to engage in continuous conversations with LLMs. I'm wondering if you can think of any ways that I can achieve my goal of capturing my conversations with LLMs without having to do so much manual data entry

# Output

Based on your requirements, there are a few potential approaches you could consider to streamline the process of capturing LLM conversations into Obsidian:

1. Browser Extension + Obsidian Plugin:
   You could develop a browser extension that captures your LLM conversations directly from the web interface you're using (e.g. ChatGPT). This extension could then communicate with an Obsidian plugin to automatically create and populate notes with the conversation content.

2. Automated Clipboard Monitoring:
   Create a script or Obsidian plugin that monitors your clipboard for new content. When it detects LLM conversation text, it could automatically create a new note or append to an existing one in Obsidian. This would still require you to copy the text, but eliminate the need for manual pasting and formatting.

3. QuickAdd Plugin Automation:
   Utilize Obsidian's QuickAdd plugin to create a macro that streamlines the capture process[1]. You could set up a template for LLM conversations and use QuickAdd's capture feature to quickly input conversation snippets with minimal manual effort.

4. API Integration with Proxy:
   If you're concerned about API costs but still want some automation, consider setting up a proxy server that intercepts your interactions with the LLM's web interface. This proxy could then use the conversation data to automatically create notes in Obsidian without incurring additional API costs.

5. Screen Scraping Tool:
   Develop or use an existing screen scraping tool that can extract text from your LLM conversation window. This tool could then automatically format and send the extracted text to Obsidian.

6. Voice Dictation + Automation:
   Use voice dictation software to "read out" important parts of your LLM conversations. Combined with a tool that monitors audio input, this could automatically transcribe and send content to Obsidian.

7. Custom LLM Interface:
   Create a custom interface for interacting with LLMs that integrates directly with Obsidian. This would allow you to have conversations and automatically save them without any manual steps.

Each of these approaches has its own trade-offs in terms of development effort, ease of use, and flexibility. The QuickAdd plugin approach might be the quickest to implement, while a custom browser extension or LLM interface would provide the most seamless experience but require more development work.

Remember to consider privacy and security implications, especially if you're dealing with sensitive information in your LLM conversations. Always ensure that any automation tools you use comply with the terms of service of the LLM platforms you're interacting with.

 