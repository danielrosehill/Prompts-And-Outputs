---
title: "one click obsidian notes for android"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can create a one-click shortcut in Obsidian for Android to automatically create a new note in a specific folder using Quick Actions or URL Schemes. Here’s how you can do it:

Method 1: Using Quick Actions in Obsidian

1. Enable Quick Actions:

Open Obsidian and go to Settings → Quick Actions.

Tap on New Quick Action.

Select Create New Note and specify the folder where you'd like the new note to be created.



2. Add the Quick Action to the Toolbar:

After setting up the Quick Action, tap Add to toolbar so that it becomes available in Obsidian’s toolbar as a one-click button.




Method 2: Using Tasker and Obsidian URI

Obsidian supports URL Schemes for creating new notes, which you can leverage with Tasker to create a homescreen shortcut.

1. Find the Folder Path:

Open Obsidian, go to Settings → Files & Links.

Find the folder path where you want the notes to be saved.



2. Use Tasker to Create a Shortcut:

Open Tasker and create a new Task.

In the Task, add an Action: Send Intent.

Action: android.intent.action.VIEW

Data: Use the Obsidian URL scheme for creating a new note in a folder, e.g., obsidian://new?vault=VaultName&file=FolderName/NoteName

Replace VaultName with your vault’s name and FolderName/NoteName with the folder and new note you want.


Once created, you can set this task as a widget on your home screen for one-click note creation.




These methods should allow you to quickly create notes with just one tap in your chosen folder.

