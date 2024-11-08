---
title: "Other split screen and tiling tools for Fedora - open ended prompt"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I love using split screen and quad layouts for so many things. Can you think of any other programs for Fedora that leverage this functionality and which I man find benefit from using?

# Output

If you enjoy using **split screen** and **quad layouts** in your terminal workflow on Fedora, you might find these other programs that support multi-pane or tiling functionalities helpful for a variety of tasks:

### 1. **Tiling Window Managers**
If you want to extend split-screen functionality across your entire desktop environment, **tiling window managers** are perfect for this. These programs automatically arrange your windows into tiles, making it easy to manage multiple applications simultaneously, similar to split screens in terminal emulators.

#### a. **i3**
   - **What it is**: A lightweight tiling window manager that lets you split your entire desktop into horizontal or vertical panes.
   - **Why you’ll love it**: You can create **quad layouts** across your workspace for different apps—editors, terminals, browsers—all within neatly arranged, easily navigable tiles.
   - **Installation**:
     ```bash
     sudo dnf install i3
     ```

#### b. **bspwm**
   - **What it is**: A tiling window manager that lets you organize windows in tree-like layouts (including quad).
   - **Why you’ll love it**: You get fine control over your window arrangements with commands, creating flexible and clean workflows.
   - **Installation**:
     ```bash
     sudo dnf install bspwm
     ```

### 2. **Code Editors with Split-Screen Support**

#### a. **Visual Studio Code**
   - **What it is**: A popular code editor that natively supports **split panes** in both vertical and horizontal layouts.
   - **Why you’ll love it**: You can use a **quad layout** in your coding environment to compare multiple files or work on different parts of a project simultaneously.
   - **Installation**:
     ```bash
     sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
     sudo dnf install https://packages.microsoft.com/yumrepos/vscode/code.x86_64.rpm
     ```
   - **How to split**: Right-click on a file and choose "Split" or use the shortcuts: `Ctrl + \` (split editor) and `Ctrl + 1/2/3/4` to navigate panes.

#### b. **Sublime Text**
   - **What it is**: Another widely used text editor with built-in split-screen capabilities.
   - **Why you’ll love it**: It supports custom layouts (e.g., quads) for working on multiple files side by side.
   - **Installation**:
     ```bash
     sudo dnf install sublime-text
     ```

### 3. **Document Viewers**

#### a. **Zathura**
   - **What it is**: A lightweight, highly customizable PDF viewer with **split-screen support** via window managers or multiple instances.
   - **Why you’ll love it**: You can open multiple PDF files side by side in a split-screen setup, perfect for comparing documents or referencing multiple sources.
   - **Installation**:
     ```bash
     sudo dnf install zathura
     ```

#### b. **Okular**
   - **What it is**: A feature-rich document viewer for KDE with support for multiple document types.
   - **Why you’ll love it**: You can use tiling window managers (like **i3** or **bspwm**) to arrange multiple **Okular** windows in a quad layout for document comparison or research.
   - **Installation**:
     ```bash
     sudo dnf install okular
     ```

### 4. **Design and Development Tools**

#### a. **GIMP (GNU Image Manipulation Program)**
   - **What it is**: A powerful open-source image editor that supports multi-window mode.
   - **Why you’ll love it**: You can use tiling window managers or split screens to arrange **multiple toolboxes and images** for design work, creating a more efficient workflow.
   - **Installation**:
     ```bash
     sudo dnf install gimp
     ```

#### b. **Inkscape**
   - **What it is**: A vector graphics editor that supports managing multiple windows.
   - **Why you’ll love it**: If you need to view and compare multiple design elements, you can split your screen using a tiling window manager.
   - **Installation**:
     ```bash
     sudo dnf install inkscape
     ```

### 5. **Text Processors**

#### a. **Vim (with tmux or native split)**
   - **What it is**: Vim is a powerful text editor, and combined with **tmux** or by using Vim’s native **split screen** features, you can easily achieve quad layouts within the editor.
   - **Why you’ll love it**: It supports **horizontal and vertical splits**, letting you work on multiple files or different parts of the same file simultaneously.
   - **Installation**:
     ```bash
     sudo dnf install vim
     ```
   - **Split commands**: `:vsp` for vertical split and `:sp` for horizontal.

---

### Recommendations:
- **i3** and **bspwm** are fantastic for leveraging split-screen functionality across your entire desktop for multiple apps.
- **Visual Studio Code** and **Sublime Text** give you powerful quad layouts for development tasks.
- **Zathura** and **Okular** are excellent for working with documents, especially in research and comparison tasks.
- **GIMP** and **Inkscape** will benefit from tiling window managers for managing multiple tool and image windows.

These programs will allow you to extend your love of **split-screen** and **quad layouts** to a variety of tasks on **Fedora**!