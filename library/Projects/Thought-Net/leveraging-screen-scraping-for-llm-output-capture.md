---
title: "Leveraging screen scraping for LLM output capture"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

The screen scraping tool is interesting and one I've thought about. It almost seems the most ideal of all the options. Of course, I'd need to find a tool that was capable of automatically detecting the various parts of the conversation and of disintinguishing between my prompts and the outputs I generate. Do any such programs exist, perhaps leveraging RPA? I use Fedora Linux

# Output

Based on your requirements and the use of Fedora Linux, there are a few potential options for screen scraping tools that could work for automatically capturing LLM conversations:

1. TagUI:
TagUI is an open-source RPA tool that supports Linux and has screen scraping capabilities[5]. It uses Python and can perform OCR, UI automation, and interact with both desktop and web applications[5]. TagUI could potentially be customized to detect and distinguish between your prompts and the LLM outputs.

2. UI.Vision RPA:
UI.Vision is another open-source RPA tool that works on Linux and offers screen scraping functionality[5]. It can extract data from user interfaces and produce automation scripts for Linux systems[5]. With some customization, it might be able to differentiate between user inputs and AI responses.

3. RoboCorp:
RoboCorp is an open-source RPA platform that supports Linux and uses Python[5]. While not specifically designed for screen scraping, its automation capabilities could potentially be adapted for this purpose.

4. Sikulix:
Though not mentioned in the search results, Sikulix is a well-known open-source tool for GUI automation and screen scraping that works on Linux. It supports Python scripting, which could be useful for developing custom logic to distinguish between prompts and outputs.

To achieve the specific functionality you're looking for - automatically detecting different parts of the conversation and distinguishing between prompts and outputs - you would likely need to combine one of these tools with custom scripting. This might involve:

1. Using OCR capabilities to read text from the screen
2. Implementing logic to identify patterns that differentiate user prompts from AI responses (e.g., formatting, position on screen, or specific markers)
3. Developing a system to automatically capture and organize the extracted text

Keep in mind that while these tools provide the foundation, significant customization would be required to create a seamless, automated solution for your specific use case. You might need to experiment with different tools and approaches to find the best fit for your needs on Fedora Linux.

 