---
title: "Viewing only one folder in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is it possible to create a view in obsidian that is focused on only one folder in my vault? By which I mean that the folder navigation doesn't show the whole vault but only this one? And which allows me to easily navigate back and forth between notes in it? 

# Output

Yes, you can create a focused view in Obsidian that only shows one folder in your vault and allows for easy navigation within that folder. There are several ways to achieve this:

### 1. **Obsidian's Folder Pane Filtering (Native Solution)**
   While Obsidian doesn't have a specific feature to show *only* one folder in the file explorer, you can use the following workarounds:

   - **Pin a Specific Folder**:
     - You can right-click a folder in the file explorer and choose the "Pin" option. This will keep the folder expanded while minimizing other folders.
   
   - **Open Folder in New Pane**:
     - You can right-click a folder and select "Open in New Pane." This will open the folder as a separate pane and give you a split view to focus on that folder.
     - Afterward, you can navigate between notes in this folder by clicking directly on them in the folder pane.

### 2. **Workspaces Plugin**
   - **Workspaces** let you save a particular layout and configuration of your Obsidian environment.
   - You can create a workspace where the focus is solely on a specific folder. In this setup, the folder is expanded, and the rest of the vault is minimized or hidden.
   - You can easily switch between different workspaces as needed (e.g., a workspace dedicated to the specific folder).

### 3. **Custom Query View Using Dataview Plugin**
   - You can use the Dataview plugin to create a filtered view that only shows notes from a specific folder.
   - For example, a query like this:
     ```dataview
     table file.name
     from "your-folder-name"
     ```
   - This will create a table view of all the notes in the specified folder. You can click on the notes to open them, and it will act as a filtered navigation system within that folder.

### 4. **Folder Note Plugin**
   - The **Folder Note** plugin allows you to associate a note with a folder. You could use this feature to create a note at the top of the folder, listing links to the notes in the folder. This way, when you open the "Folder Note," you can navigate back and forth between notes within that folder easily.

### 5. **Create a Sidebar with Only Specific Folder Notes**
   - You can create a sidebar with links to all the notes in a specific folder. 
     - To do this, you can make a note inside the folder that serves as a "Table of Contents" with links to all the notes in the folder. 
     - Pin that note to the sidebar, and it will act as a navigator for the folder.

### 6. **Folder Context Using Quick Switcher++ Plugin**
   - With the **Quick Switcher++** plugin, you can restrict searches to a specific folder. You can use the plugin to navigate through notes in the folder by customizing it to only search within that folder. This way, you’ll focus solely on the notes in that specific folder when using the switcher.

### How to Create the Focused View:
- **Step 1**: Organize your target folder by pinning or opening it in a dedicated pane.
- **Step 2**: Use the native file explorer to collapse other folders and focus only on the desired folder.
- **Step 3**: Optionally, save this configuration using the Workspaces plugin to quickly return to the view.
- **Step 4**: For an even more focused view, combine this with the Dataview or Folder Note plugin to create a dedicated navigation panel just for the folder's contents.

These methods will give you a focused workflow for one folder, allowing you to easily navigate and switch between notes without distractions from the rest of the vault.