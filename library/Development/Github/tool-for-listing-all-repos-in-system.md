---
title: "Tool for listing all repos in system"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm looking for an extension that can show all the Github repos in my system. They're all nested in /Git but they're in subfolders so it would need to have recursion. More importantly I'd like to be able to use the command palette to quickly switch between this list of repos ... so it would need to integrate with that. Can you think of any good options?

# Output

Based on your requirements, there are a couple of VS Code extensions that could potentially meet your needs. Here are two options that seem particularly well-suited:

1. Git Project Manager (GPM)

The Git Project Manager extension seems to align closely with your requirements:

- It can recursively search for Git repositories in specified folders.
- It integrates with the VS Code command palette.
- It allows quick switching between repositories.

Key features:
- Configurable search depth for nested repositories
- Caching of repository information for faster access
- Command palette integration for quick repository switching
- Option to open repositories in new windows

To set it up:
1. Install the "Git Project Manager" extension from the VS Code marketplace.
2. Configure the base folders to search in settings.json:
   ```json
   {
     "gitProjectManager.baseProjectsFolders": ["/path/to/your/Git/folder"]
   }
   ```
3. Adjust the max depth recursion if needed:
   ```json
   {
     "gitProjectManager.maxDepthRecursion": 4
   }
   ```

You can then use the "GPM: Open Git Project" command in the palette to quickly switch between repositories[3].

2. Projects

The "Projects" extension by Luis Balbinot (L13) is another good option:

- Auto-detects Git repositories, VS Code folders, and workspace files.
- Allows adding folders and workspace files to a project list.
- Supports quick switching between projects via the command palette.
- Offers favorites and custom grouping features.

Key features:
- Auto-detection of Git repositories
- Customizable search paths and depth
- Integration with VS Code's command palette
- Options to open projects in new windows or reveal in file explorer

To set it up:
1. Install the "Projects" extension from the VS Code marketplace.
2. Configure the Git folders to search in settings:
   ```json
   {
     "l13Projects.git.folders": ["/path/to/your/Git/folder"]
   }
   ```
3. Adjust the max depth recursion if needed:
   ```json
   {
     "l13Projects.git.maxDepthRecursion": 4
   }
   ```

You can then use the extension's commands in the palette to manage and switch between projects[7].

Both of these extensions offer the core functionality you're looking for - recursive searching for Git repositories and quick switching via the command palette. The Git Project Manager might be slightly more focused on your specific use case, while Projects offers some additional workspace management features.

I'd recommend trying out both to see which fits your workflow better. You can easily install and test them, then keep the one that works best for you.

 