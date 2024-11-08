---
title: "TUI for browsing Obsidian vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


can you suggest a TUI for Fedora that would allow me to search through my vault of markdown files and allow me to browse their contents all within the terminal?

# Output

To search through your vault of Markdown files and browse them all within the terminal on Fedora, you can use a combination of **TUI** (Text User Interface) tools. Below are some highly effective options for this workflow:

### 1. **nnn (File Manager + Search)**
   - **Description**: `nnn` is a terminal file manager with integrated support for plugins, including search functions. It’s lightweight, highly customizable, and can be extended to view Markdown files and even search through them using tools like `ripgrep`.
   - **Features**:
     - Quick navigation through directories and files.
     - Plugin system for extended functionality, including file previews and text search.
     - Can integrate with `bat` to provide rich previews of Markdown files.
   - **Installation**:
     ```bash
     sudo dnf install nnn
     ```
   - **How to Use**:
     - Open `nnn` in the directory of your vault.
     - Use its **search** feature to locate Markdown files.
     - Use a previewer like **bat** (syntax highlighting) for Markdown content.
     - Plugins like **`nuke`** can allow you to use `ripgrep` for fast text searches within files.

   **Link**: [nnn on GitHub](https://github.com/jarun/nnn)

### 2. **ranger + ripgrep**
   - **Description**: **ranger** is another popular terminal file manager that provides a TUI for browsing files, and can be extended with **ripgrep** for fast, full-text search within your Markdown files.
   - **Features**:
     - Provides a multi-pane layout to easily navigate and view Markdown files.
     - Can integrate with `ripgrep` to search the contents of files.
     - Supports previewing files directly in the terminal, using tools like `less` or `bat` for Markdown.
   - **Installation**:
     ```bash
     sudo dnf install ranger ripgrep
     ```
   - **How to Use**:
     - Use `ranger` to navigate through your Markdown vault.
     - Use the search keybindings (e.g., `/` in ranger) along with `ripgrep` to search for content within the Markdown files.
     - You can also configure ranger to preview files with Markdown syntax highlighting using **`bat`**.

   **Link**: [ranger GitHub](https://github.com/ranger/ranger)

### 3. **fzf (Fuzzy Finder) + bat**
   - **Description**: **fzf** is a general-purpose fuzzy finder that can be combined with **ripgrep** and **bat** to create a highly efficient TUI workflow for searching and viewing Markdown files in your terminal.
   - **Features**:
     - Fuzzy file search based on partial matches.
     - Can be combined with `ripgrep` to search contents of Markdown files.
     - Use `bat` to view Markdown files with syntax highlighting.
   - **Installation**:
     ```bash
     sudo dnf install fzf ripgrep bat
     ```
   - **How to Use**:
     - Search for files within your vault:
       ```bash
       fzf --preview 'bat --style=numbers --color=always {}'
       ```
     - Search within files using `ripgrep`:
       ```bash
       rg "search_term" | fzf
       ```

   **Link**: [fzf GitHub](https://github.com/junegunn/fzf)

### 4. **Vifm**
   - **Description**: **Vifm** is a file manager inspired by **vim** that can be used to navigate and manage files in a TUI. It supports file searching and browsing in a directory structure, and it works well with external tools like `grep` or `ripgrep` for searching within files.
   - **Features**:
     - Keyboard-driven interface similar to **vim**.
     - Supports integration with external search tools.
     - Previews of Markdown files with external viewers.
   - **Installation**:
     ```bash
     sudo dnf install vifm
     ```
   - **How to Use**:
     - Use `vifm` to browse through your Markdown files.
     - Search through the contents using `grep` or `ripgrep`.
     - Set up `vifm` to open Markdown files with `less`, `vim`, or `bat` for better previews.

   **Link**: [Vifm GitHub](https://vifm.info/)

### 5. **mdless**
   - **Description**: **mdless** is a simple tool designed to display Markdown files with styles and formatting in the terminal. While it doesn’t provide search functionality, it can be combined with search tools like `ripgrep` to give you the ability to search and preview Markdown files.
   - **Features**:
     - Displays Markdown files with headers, bold text, and lists rendered in the terminal.
     - Works well with search tools like `fzf` or `ripgrep` to find specific files and browse content.
   - **Installation**:
     ```bash
     gem install mdless
     ```
   - **Usage**:
     - Use `mdless` to open and view Markdown files after searching for them using `fzf` or `ranger`.

   **Link**: [mdless GitHub](https://github.com/ttscoff/mdless)

---

### Conclusion:
For searching and browsing your Markdown files in the terminal on Fedora, tools like **nnn**, **ranger**, or **fzf** combined with **ripgrep** and **bat** provide a powerful TUI experience. These tools can search, filter, and display the content of Markdown files, all within the terminal, giving you a fast and efficient way to work with large vaults of text-based notes.

If you're a **vim** user, tools like **Vifm** integrate well with the **vim** workflow, while **mdless** is a good option for rendering Markdown content more legibly within the terminal.