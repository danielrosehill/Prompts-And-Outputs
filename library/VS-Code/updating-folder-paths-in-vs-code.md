---
title: "Updating folder paths in VS Code"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. I'm reorganising a Github repository. The problem is that whenever I do this, I end up breaking internal paths for images (the repo is on Github and some of the files are markdown files with images). Are there any VS code extensions which can automatically update relative paths so that I can move around image folders freely without this being a concern?

# Output

Yes, there are a couple of Visual Studio Code extensions that can help manage and update relative paths automatically when you move files or folders within a GitHub repository. These extensions ensure that links to images and other files in your Markdown documents remain intact when reorganizing your repository.

### 1. **Path Autocomplete**
   - **Description:** This extension enhances path suggestions and automatically updates paths when you move files or folders within your project. It ensures that paths to images, links, and other files in your Markdown are kept up-to-date.
   - **Features:**
     - Auto-updates paths when moving files.
     - Provides intelligent path suggestions while typing.
   - **Link:** [Path Autocomplete](https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete)

### 2. **Markdown Links**
   - **Description:** This extension helps you maintain the integrity of links in your Markdown files, including image paths. It updates paths automatically when files are moved and helps prevent broken links.
   - **Features:**
     - Auto-updates relative paths when moving Markdown files or linked assets.
     - Provides warnings for broken links.
   - **Link:** [Markdown Links](https://marketplace.visualstudio.com/items?itemName=tchayen.markdown-links)

### 3. **vscode-file-link**
   - **Description:** This extension helps manage file links in your Markdown documents, especially when moving or renaming files. It automatically adjusts the paths in your Markdown files to ensure that all links remain correct.
   - **Features:**
     - Automatically updates paths in Markdown files when you move or rename linked files.
     - Works well with images and other assets.
   - **Link:** [vscode-file-link](https://marketplace.visualstudio.com/items?itemName=jaydenlin.vscode-file-link)

### 4. **Relative Path Refactor**
   - **Description:** This extension automatically updates all relative paths in your project when you move or rename files. It's particularly useful for keeping image paths in Markdown documents up-to-date after restructuring your repository.
   - **Features:**
     - Auto-updates relative paths for images and other files in Markdown.
     - Easy to use with drag-and-drop file movements.
   - **Link:** [Relative Path Refactor](https://marketplace.visualstudio.com/items?itemName=jakob101.relativepathrefactor)

### 5. **Auto Rename Tag**
   - **Description:** Although originally intended for renaming HTML tags, this extension also works well with Markdown files, especially for ensuring that image paths remain correct when you move or rename files.
   - **Features:**
     - Automatically updates matching tags, including image paths, when renaming or moving files.
   - **Link:** [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)

Using these extensions, you can freely reorganize your GitHub repository without worrying about breaking internal paths for images or other linked files in your Markdown documents. These tools will save you time and reduce errors when managing large repositories with many files.## Extracted Prompts
[[Prompts/Autocapture/Updating folder paths in VS Code.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Updating folder paths in VS Code.md#Prompt 1|Prompt 1]]
