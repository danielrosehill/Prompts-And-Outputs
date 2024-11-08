---
title: "Obsidian plugins for navigating between notes"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is it possible can you recommend any ways to use obsidian for reviewing saved notes and going through them one by one? It doesn't seem to have a simple way of navigating between next and previous notes sequentially in a list

# Output

While Obsidian doesn’t have a native "Next" or "Previous" button to navigate through notes sequentially, you can set up workflows to achieve a similar experience for reviewing and going through notes one by one. Here are some strategies and plugins you can use to review saved notes and navigate between them efficiently:

### 1. **File Explorer Navigation**
   - **Expand the folder** where your notes are stored in the file explorer.
   - Use the keyboard arrow keys to move up and down through your list of notes.
   - This is a manual way of navigating sequentially, but it works if you're reviewing notes in a specific folder.

### 2. **Note Ref Links / Table of Contents Note**
   - Create a **"Table of Contents"** note with a list of links to the notes you want to review in sequence.
   - Manually link the next note at the bottom of each note with `[[next-note-title]]` or `[[previous-note-title]]` to jump back and forth between them.

### 3. **Random Note Plugin**
   - If you're looking for a more spontaneous way to review notes, you can use the **Random Note Plugin**:
     - Go to **Settings > Community Plugins** and install the **Random Note** plugin.
     - Once installed, it will allow you to quickly jump to a random note in your vault, which can help with reviewing notes in a less structured way.
   - While it doesn't provide sequential navigation, it can be useful if you want to jump into your older notes without scrolling through the entire vault.

### 4. **Sliding Panes Plugin**
   - **Sliding Panes (Andy Matuschak mode)** is a community plugin that changes the layout of your notes so that each new note you open gets displayed next to the previous one, similar to a card stack.
   - This allows you to open one note, click on a link in it, or select a new note, and slide between them easily. You can see the previous note next to your current one and switch back and forth, giving you a more fluid way of navigating between multiple notes.

### 5. **Review Notes by Date Modified (Search or Dataview)**
   - Use the **Search** or **Dataview** plugin to list notes by when they were last modified or created.
   - Use the following Dataview query to display notes in a folder in order of modification:
     ```dataview
     table file.mtime as "Last Modified"
     from "your-folder-name"
     sort file.mtime desc
     ```
   - You can then manually navigate through the list by clicking on each note in sequence, reviewing them one at a time.

### 6. **Hotkeys for Navigation**
   - Assign **Hotkeys** for "Open next pane" and "Open previous pane" to quickly move between notes that are open in multiple panes.
   - To do this:
     - Go to **Settings > Hotkeys**, search for **Next Pane** and **Previous Pane**, and assign shortcuts.
     - You can then quickly switch between open notes if you have them in multiple panes.

### 7. **Templater Plugin for "Next" and "Previous" Links**
   - The **Templater Plugin** allows you to automate the process of adding "Next" and "Previous" links at the bottom of your notes.
   - You can create a template that inserts links to the next and previous notes in the folder by generating these dynamically based on file names or indexes.
   - Example of using Templater for a dynamic note-linking workflow:
     ```yaml
     [[<% tp.file.previous() %>]] | [[<% tp.file.next() %>]]
     ```
   - You can then run this template in your notes to create links to the next or previous notes in sequence.

### 8. **Daily Notes Plugin (For Reviewing Notes Chronologically)**
   - If your notes are organized with dates (like a journal), you can use the **Daily Notes** plugin:
     - This allows you to quickly navigate through daily notes using the calendar or a date selector.
     - If you have notes saved by date, this is a useful way to go back and review them in order.

### 9. **Backlinks and Unlinked Mentions Navigation**
   - Use **backlinks** and **unlinked mentions** to move through related notes. This helps you navigate contextually linked notes, even though they may not be sequential.
   - You can find the backlinks pane below your open note and use it to jump between related notes for in-depth reviews.

### 10. **Workspace Switching**
   - If you’re reviewing a specific set of notes, you can create a workspace (using the **Workspaces** plugin) that is focused on a particular folder or tag.
   - Save this view, and you can quickly return to it as you review the notes in that workspace.

### 11. **Cycle Through Files with Command Palette**
   - Use the Command Palette (Ctrl + P) to quickly search for a note by typing its name, and open it without having to navigate through the folder structure.
   - You can install the **Quick Switcher++** plugin to make the command palette even more powerful, allowing you to navigate through notes based on recent activity, tags, or other criteria.

### Conclusion:
While Obsidian doesn’t have a built-in "next" or "previous" note feature, you can create workflows and use plugins to navigate through your notes sequentially or efficiently:

- **For structured, sequential navigation**: Use a Table of Contents note, or manually add "Next" and "Previous" links between your notes.
- **For fluid navigation**: Use the **Sliding Panes** plugin to move between open notes easily.
- **For spontaneous reviews**: The **Random Note Plugin** or using searches sorted by date can help you review notes in no particular order.

These solutions should give you more control over how you navigate and review your notes in Obsidian.