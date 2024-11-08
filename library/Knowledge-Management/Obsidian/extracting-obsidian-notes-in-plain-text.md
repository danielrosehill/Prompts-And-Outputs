---
title: "Extracting Obsidian notes in plain text"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

How about this: By default I want to copy as plain text. 

Can I use a plugin that will copy the text as plain and then I can reassign the copy shortcut to use this by default?

# Output

Yes, you can achieve this in **Obsidian** by using a combination of a **plugin** to copy text as plain text and then **reassigning the default copy shortcut** to that action. Here’s how you can do it:

### **Steps to Copy as Plain Text by Default in Obsidian**

#### **1. Install a Plugin for Plain Text Copying**
To get started, you'll need a plugin that allows you to copy text without Markdown tags:

- **Markdown Formatting Assistant** or a similar plugin can help you strip Markdown formatting when copying text. Alternatively, you can use **Clipboard tools** available through the community plugin directory.
  
**To install the plugin**:
1. Go to **Settings** > **Community Plugins** > **Browse**.
2. Search for a plugin like **"Markdown Formatting Assistant"** or **“Obsidian Clipboard Tools”**.
3. **Install** and **enable** the plugin.

#### **2. Set Up a Command for Plain Text Copying**
Once installed, many plugins provide a custom command to **copy text as plain text**.

- In **Settings**, look for the plugin settings.
- There should be a command like **"Copy as Plain Text"** or similar.

#### **3. Reassign the Copy Shortcut**
To make **plain text copying** the default action, you can reassign the shortcut to this command:

1. **Open Hotkey Settings**:
   - Go to **Settings** > **Hotkeys**.
   
2. **Search for the Copy Command**:
   - Search for the plugin command, e.g., **"Copy as Plain Text"**.
   
3. **Assign the Shortcut**:
   - Assign the **default copy shortcut** (`Ctrl + C` or `Cmd + C`) to **"Copy as Plain Text"** by clicking on the command and pressing the desired keys.

4. **Remove the Default Copy Hotkey**:
   - To avoid conflicts, you can **unassign** the default **"Copy"** hotkey, ensuring only the plain text version is active.

#### **4. Test the New Shortcut**
- Now, whenever you press **`Ctrl + C` or `Cmd + C`**, it should copy text as **plain text** without Markdown tags.
- You can test by copying a Markdown snippet and pasting it into another application to ensure no tags are retained.

### **Summary**
- **Install a Plugin**: Use a plugin like **Markdown Formatting Assistant** or **Obsidian Clipboard Tools**.
- **Reassign Hotkey**: Set the plugin’s **plain text copy** command to the default **copy shortcut** (`Ctrl + C` or `Cmd + C`).
- **Unassign Default Copy**: Remove the original copy command to prevent conflicts.

This setup will allow you to **copy as plain text by default** in Obsidian, making it convenient when pasting into web browsers or other text editors. Let me know if you need any help with the plugin setup or hotkey reassignment process!