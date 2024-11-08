---
title: "Backing up Obsidian plugins and config data without Sync"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there an easy way to backup all your non-note data from Obsidian: specifically, the list of plugins that I use and the settings that I have applied to my vault? I'm not using Sync

# Output

To back up **non-note data** from Obsidian, specifically your **list of plugins** and the **settings** you have applied to your vault, you can manually back up the relevant configuration files. Here are the steps to do this effectively:

### 1. **Backup Plugin List and Settings**
Obsidian's plugins, settings, themes, and other configurations are saved in the vault’s **`.obsidian` folder**. Here's what you need to back up:

- **Location of Configuration Files**:
  - Navigate to your Obsidian vault folder.
  - Inside the vault, you'll find a folder named `.obsidian`. This is a hidden folder, so ensure you have enabled viewing hidden files in your file explorer.

- **Files and Folders to Backup**:
  - **`.obsidian/plugins`**: This folder contains the data for the plugins that you use, including individual settings for each plugin.
  - **`.obsidian/config`**: This file stores the configuration settings for your vault, such as your workspace layout, sidebar settings, and other general settings.
  - **`.obsidian/theme.json`**: If you are using a custom theme, this file contains your theme configurations.
  - **`.obsidian/workspace.json`**: This file holds workspace settings, such as which panes are open and their arrangement.

### 2. **Steps to Backup Configuration Files**:
1. **Manually Copy the `.obsidian` Folder**:
   - To back up the settings, simply **copy the entire `.obsidian` folder** to a safe location (such as an external hard drive, cloud storage, or a backup folder on your computer).
   - This will ensure that all plugins, custom themes, and settings are preserved.

2. **Automate the Backup Process**:
   - You could also set up a script to automate the backup periodically. Here's an example using a **Bash script** on Linux to back up the `.obsidian` folder to another directory:
     ```bash
     #!/bin/bash
     source_vault="/path/to/your/obsidian/vault/.obsidian"
     backup_location="/path/to/backup/location/obsidian_backup"

     rsync -av --delete "$source_vault" "$backup_location"
     echo "Obsidian settings backed up to $backup_location"
     ```
   - This script uses `rsync` to back up the settings, ensuring that the backup is always in sync with your current configuration.

### 3. **Additional Tools for Backups**
- **Git Version Control**: You can use **Git** to version-control your entire vault, including the `.obsidian` folder. This is particularly useful if you want a history of your changes.
  - **Setup**:
    1. Initialize a Git repository in your vault folder.
    2. Commit the `.obsidian` folder along with your notes.
    3. Push to a **private GitHub repository** or another Git hosting provider for backup.
  - This way, both your notes and settings are backed up in one step.

### 4. **Restoring Backups**
- To restore your **plugins** and **settings**:
  1. Copy the `.obsidian` folder from your backup back into the vault where you want to restore your settings.
  2. When you open Obsidian, all your previous configurations, including plugins and settings, will be applied automatically.

### Summary
- To **back up your plugin list and settings**:
  1. **Manually copy** the `.obsidian` folder.
  2. **Automate the process** with a script or use **Git** for version control.
- These steps will ensure you always have an up-to-date backup of your **plugins** and **custom settings** without needing Obsidian's **Sync** feature.