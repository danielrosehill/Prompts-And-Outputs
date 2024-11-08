---
title: "A tool for storing your favorite Linux commands"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. I come back to a previous question. With your help, I'm building up an excellent repository of Linux commands that were previously unknown to me and which are saving me much time! I'd love to keep them in some kind of repository! I plan on versioning them through Git. But can you think of any programs which are designed for this job ... helping sysadmins to remember their favorite commands?

# Output

That’s fantastic! There are a few programs and tools that can help sysadmins or developers maintain a structured and easily accessible repository of their favorite or most-used Linux commands. Here are some of the best tools and approaches designed for this purpose:

### 1. **tldr (Too Long; Didn't Read)**
   - **Description**: **tldr** is a community-driven project that provides simplified, example-based documentation for Unix commands. It's very useful for quickly recalling how to use commands without wading through long man pages.
   - **Why it helps**: You can either look up commands from its built-in database or add your own custom pages if needed.
   - **How to install**:
     ```bash
     sudo apt install tldr
     ```
   - **Usage**:
     ```bash
     tldr <command>
     ```
   - **Link**: [tldr.sh](https://tldr.sh)

### 2. **Cheat.sh**
   - **Description**: **Cheat.sh** is a powerful command-line tool that provides simple "cheat sheets" for most Linux commands. You can query for the command directly from the terminal and get short, precise examples.
   - **Why it helps**: It allows you to quickly look up commands and options without leaving the terminal. You can even store your own snippets if you need to customize.
   - **How to use**:
     ```bash
     curl cheat.sh/<command>
     ```
   - **Link**: [cheat.sh](https://cheat.sh/)

### 3. **BashHub**
   - **Description**: **BashHub** records all your shell history and syncs it to the cloud. You can easily search for any command you've used in the past. It's especially useful for sysadmins who want to recall previously used commands across machines.
   - **Why it helps**: It organizes and stores your history across all your machines, meaning you never lose track of commands you've executed in the past.
   - **How to install**:
     ```bash
     curl -OL https://bashhub.com/install
     ./install
     ```
   - **Link**: [bashhub.com](https://bashhub.com/)

### 4. **Commandlinefu.com**
   - **Description**: **Commandlinefu** is a community-driven collection of Linux command-line gems. You can search for commands contributed by others, or submit your own.
   - **Why it helps**: It acts as a crowdsourced reference for discovering useful commands and adding them to your workflow.
   - **Link**: [Commandlinefu](https://www.commandlinefu.com/)

### 5. **cheat (Cheat Sheets for Your Own Commands)**
   - **Description**: **cheat** is a command-line tool that allows you to create, manage, and view cheat sheets for any command, including your own custom ones.
   - **Why it helps**: You can create your own repository of Linux commands, organize them, and version them using Git. It's simple, extensible, and personalized to your needs.
   - **How to install**:
     ```bash
     sudo apt install cheat
     ```
   - **Usage**:
     ```bash
     cheat <command>
     ```
   - **Link**: [GitHub - cheat](https://github.com/cheat/cheat)

### 6. **Obsidian**
   - **Description**: Although **Obsidian** is not specifically built for managing command repositories, it is an excellent note-taking tool that allows you to create structured, markdown-based notes and organize them in a hierarchical way. You could create your own note vault for storing useful Linux commands, categorized by type or usage.
   - **Why it helps**: If you’re already using Obsidian for other things, this tool can be extended to track your favorite commands with powerful linking and search capabilities.
   - **Link**: [Obsidian.md](https://obsidian.md/)

---

### Recommended Workflow:
Since you’re already using **Git**, I’d recommend combining **cheat** or **Obsidian** for local cheat sheets (stored in a markdown format for easy Git versioning) with **tldr** or **cheat.sh** for instant command lookups.

- **Store Your Commands in Git**: Use **cheat** or **Obsidian** to write and manage your personalized Linux command repository. Each cheat sheet (or note) can be committed to a Git repository, allowing version control, collaboration, and backups.
- **Quick Lookups**: Use **tldr** or **cheat.sh** to quickly find commands that you may not have committed to your repository yet.

Let me know if you'd like more detailed guidance on any of these tools!