---
title: "Scoping out notepad idea for storing outputs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I'm building a system for storing chats with LLMs (including you ChatGPT!) in an organised personal knowledge manager. Right now, I'm using Obsidian and storing the outputs in B2. My system has three core modules: for prompts, for outputs, and for storing agent configurations. I am thinking that it might be worth trying to create my own notepad app specifically for this purpose. That way, I can build the features that I want and need rather than trying to hack around an existing tool. The relationships between the core entities are important and there's some additional metadata that I would like to capture. Firstly, how difficult might this project be? Secondly, can you think of any markdown notepad tools or projects which I might be able to fork to give me a head start?

# Output
Creating your own notepad app for storing chats with LLMs is a project that varies in complexity based on your desired features, your programming experience, and the technology stack you choose. Here’s a breakdown:

### **Project Difficulty**
1. **Basic Implementation**: If you’re looking to create a simple markdown editor with some extra features like metadata capture, tagging, and relational links between notes, this is a moderately difficult project, especially if you're already comfortable with web development and basic programming concepts.

2. **Advanced Features**: Adding features like a built-in markdown parser, robust search capabilities, B2 storage integration, and relational databases to link prompts, outputs, and configurations will increase the complexity. You might need to work with frameworks, manage state efficiently, and possibly integrate backend services.

3. **UI/UX**: Creating a user-friendly interface that is both intuitive and feature-rich can be challenging. You'll need to consider how users will interact with the different modules, how data will be presented, and ensure the system is performant.

### **Existing Markdown Notepad Tools/Projects to Fork**
Here are some open-source projects that you might consider forking to get a head start:

1. **Joplin**: 
   - **Description**: A free, open-source markdown note-taking app that supports syncing, end-to-end encryption, and various plugins.
   - **Why Fork?**: Joplin has a solid foundation with markdown support, metadata capture, and plugins. You could extend it to support your custom features like agent configurations and enhanced relationships between notes.
   - **GitHub**: [Joplin](https://github.com/laurent22/joplin)

2. **Notable**:
   - **Description**: A markdown-based note-taking app that focuses on simplicity and extensibility.
   - **Why Fork?**: Notable is minimalist but has a plugin architecture, making it easier to add custom features. It could serve as a lightweight base for your app.
   - **GitHub**: [Notable](https://github.com/notable/notable)

3. **Obsidian-like Tools**:
   - **TiddlyWiki**: A non-linear personal web notebook that uses wiki-style linking and can be customized extensively.
     - **Why Fork?**: While not purely markdown-based, TiddlyWiki’s extensibility and focus on relationships between notes make it a strong candidate.
     - **GitHub**: [TiddlyWiki](https://github.com/Jermolene/TiddlyWiki5)
  
4. **Boost Note**:
   - **Description**: An open-source markdown editor for developers, with support for collaborative editing and multiple workspaces.
   - **Why Fork?**: Boost Note is geared towards developers, making it easier to integrate with backend services and customize features.
   - **GitHub**: [Boost Note](https://github.com/BoostIO/BoostNote-App)

### **Additional Considerations**
- **Data Structure**: Consider how you will structure your data (e.g., YAML front matter for metadata, JSON files, etc.) to maintain relationships between prompts, outputs, and configurations.
- **Storage**: Since you're using B2 for storage, make sure the app has good cloud integration to handle backups and retrievals efficiently.
- **Extensibility**: Build your app in a modular way so that adding new features or altering existing ones in the future is straightforward.

This project is definitely achievable, especially with a strong foundation from one of these tools.## Extracted Prompts
[[Prompts/Autocapture/Scoping out notepad idea for storing outputs.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Scoping out notepad idea for storing outputs.md#Prompt 1|Prompt 1]]
