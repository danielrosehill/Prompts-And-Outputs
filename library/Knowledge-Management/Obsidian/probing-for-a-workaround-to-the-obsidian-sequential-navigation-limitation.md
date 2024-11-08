---
title: "Probing for a workaround to the Obsidian sequential navigation limitation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

There's one limitation in Obsidian that is very frustrating. I'm going through a very long folder of documents (about 2,000 of them). The folder is organised from newest to oldest). I am reviewing them one by one so that I can bookmark those which I want to review more closely. As far as I can tell, I don't have any logical way of choosing to show the "next" or the "previous" note. Keyboard shortcuts would be great for this. So would arrow buttons. Are there any workarounds to would allow me to get this?

# Output

Obsidian currently lacks a built-in feature for navigating notes in a folder sequentially, which can be frustrating when working with a large number of notes. However, there are some **workarounds** and **plugins** that can help you achieve smoother navigation.

### 1. **Templater Plugin for Custom Shortcuts**
You can use the **Templater** plugin to create a custom script that simulates "next" and "previous" functionality. This approach allows you to navigate between the notes in the folder:

- **How It Works**:
  - You can use the Templater plugin to create **two buttons or keyboard shortcuts** to open the "next" or "previous" note in the current folder.
  - This involves creating a custom script that queries the note list and opens the desired one based on the current note’s index.

### 2. **Quick Explorer Plugin**
The **Quick Explorer** plugin allows you to quickly open the next or previous note in a list, based on the note's position in the folder pane:

- **How to Use It**:
  - Install the plugin through the community plugins store.
  - Once installed, it can allow you to set **keyboard shortcuts** to navigate between the next or previous files in a folder.

### 3. **Note Navigator Plugin**
The **Note Navigator** plugin adds navigation functionality that allows you to move through notes more easily:

- **Features**:
  - This plugin adds **arrows** or **buttons** to navigate to the next or previous note.
  - You can also assign **hotkeys** to navigate through notes, effectively solving the issue of going through 2,000 notes one by one.

### 4. **Custom Hotkey Setup**
- If plugins don't fully solve the issue, you could consider using **AutoHotkey (for Windows)** or a similar scripting tool to create a custom solution that interacts with Obsidian's UI.
- You could set up a script that mimics a click on the "next note" or "previous note" by simulating the interaction with the file list in the sidebar.

### Summary of Solutions:
- **Templater Plugin**: Create custom scripts for navigation buttons.
- **Quick Explorer Plugin**: Provides simple keyboard shortcuts for next/previous notes.
- **Note Navigator Plugin**: Adds arrow buttons and hotkey navigation.
- **AutoHotkey Scripting**: Create custom interactions for more control.

These workarounds can help streamline the review process by allowing you to quickly move from one note to the next without manually navigating the sidebar. Let me know if you'd like more detailed instructions on any of these options!