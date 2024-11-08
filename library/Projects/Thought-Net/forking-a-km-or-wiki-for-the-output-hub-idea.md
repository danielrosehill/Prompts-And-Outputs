---
title: "Forking a KM or wiki for the Output Hub idea"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Using something like Outline is a very interesting idea. I should add as a requirement that the knowledge base tool should be markdown native. LLM outputs are typically delivered in markdown and it's important that the user not have to edit basic formatting to be able to work with the outputs. 

I don't believe there's any "off the shelf" knowledge base that has the functionality I'm looking for. 

Can you think of any knowledge base or wiki or document editing tools that I could (legally) either fork or add custom modules to in order to enable this use-case?

# Output

Based on your requirements for a markdown-native knowledge base that can be customized or extended, here are some open-source options you could potentially fork or add custom modules to:

1. Obsidian: While primarily designed for personal use, Obsidian is markdown-native and has a plugin system. You could potentially fork it and adapt it for multi-user, cloud-based use.

2. Wiki.js: This is a powerful, extensible wiki software that supports markdown. It has a modular architecture, making it easier to add custom functionality[3].

3. BookStack: While it offers both WYSIWYG and markdown editing, it's open-source and could be modified to be markdown-only if needed[4].

4. Gollum: This is a simple, Git-powered wiki with a focus on markdown. It's designed to be easily customizable.

5. Raneto: A lightweight knowledge base that uses markdown files. It's built on Node.js and is designed to be easy to customize[2].

6. TiddlyWiki: A unique non-linear notebook that uses a wiki-like structure. It supports markdown and is highly customizable.

7. Joplin: While primarily a note-taking app, Joplin is open-source, markdown-native, and has a plugin system that could potentially be extended for your needs.

Of these options, Wiki.js and BookStack are probably the most feature-complete for a knowledge base system, while still being open-source and customizable. They both have active communities and are designed with extensibility in mind.

For your specific use-case of handling LLM outputs, you might need to create a custom module or plugin that can automatically process and format the incoming markdown from the LLM, ensuring it's properly integrated into the knowledge base structure.

Remember that any modifications or forks should comply with the original software's license terms. Most of these projects use permissive licenses like MIT or GPL, but it's always good to double-check the specific requirements and restrictions.

 




## Extracted Prompts
[[Prompts/Forking a KM or wiki for the Output Hub idea.md#Prompt 1|Prompt 1]]
