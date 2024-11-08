---
title: "Fedora notepads with split pane support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Are there any notepads for Fedora that have split pane support so that I could work on a few notes simultaneously?

# Output

For simple notepads on Fedora that support **split pane functionality** (useful for jotting down text notes), here are some excellent options:

### 1. **Gedit (with Plugins)**
   - **What it is**: Gedit is the default GNOME text editor, lightweight and designed for simplicity, but can be extended with plugins to enable more advanced functionality like split panes.
   - **How to enable split panes**: Install the **Multi-Edit plugin** using the Gedit Plugins package. This will allow you to split the editor into multiple panes to view or edit different files simultaneously.
   - **Installation**:
     ```bash
     sudo dnf install gedit-plugins
     ```
   - **Why it's great**: It’s lightweight, fast, and integrates well with the GNOME desktop.

### 2. **Notepadqq**
   - **What it is**: Notepadqq is a **Linux alternative to Notepad++**, designed for jotting down text notes and supporting basic development tasks.
   - **How to enable split panes**: Notepadqq supports split panes natively. You can split the editor both vertically and horizontally to work on multiple text files simultaneously.
   - **Installation**:
     ```bash
     sudo dnf install notepadqq
     ```
   - **Why it's great**: It's simple to use, similar to Notepad++, and has built-in split screen support for multitasking across different notes.

### 3. **Kate (KDE Text Editor)**
   - **What it is**: **Kate** is the advanced text editor for the KDE desktop, designed for text editing but also powerful enough to handle multiple documents at once through split panes.
   - **How to enable split panes**: In Kate, you can split the view horizontally or vertically using the "Split View" option under the `View` menu.
   - **Installation**:
     ```bash
     sudo dnf install kate
     ```
   - **Why it's great**: Kate is highly customizable and allows for flexible pane layouts, making it great for jotting down multiple notes at the same time.

### 4. **Xed (Text Editor)**
   - **What it is**: **Xed** is a simple text editor based on **Pluma** and **Gedit**. It provides a clean interface for taking text notes and can be extended with plugins to support split panes.
   - **How to enable split panes**: Use the Multi-Edit plugin to enable split panes.
   - **Installation**:
     ```bash
     sudo dnf install xed
     ```
   - **Why it's great**: Xed is lightweight, user-friendly, and a good option for taking simple notes with the potential for multi-pane views.

### Summary:
If you're looking for **simple notepads** that support split-pane layouts:
- **Notepadqq** and **Gedit (with Plugins)** are great lightweight options.
- **Kate** offers more flexibility if you prefer working in a more powerful text editor environment with built-in split functionality.

Would you like help configuring any of these tools for multi-pane usage?