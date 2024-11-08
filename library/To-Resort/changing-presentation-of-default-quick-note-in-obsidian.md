---
title: "Changing presentation of default quick note in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt:** You are asking if it's possible to alter the default title of the "quick note" in Obsidian so that it starts blank. Additionally, you are asking if it's possible to create a system keybinding that opens the quick note in a specific vault.

### 1. Altering the Default Title of "Quick Note" to Start Blank
Unfortunately, in Obsidian's native settings, you can't directly alter the default title of the "quick note" to be blank. However, you can create a custom solution using community plugins or snippets:

- **Templater Plugin:** One solution is to use the [Templater plugin](https://github.com/SilentVoid13/Templater), which allows you to create templates that can automatically be applied to new notes. You can set the note title to be blank or customizable when you create a "quick note."
  1. Install the Templater plugin.
  2. Create a template that sets the note title to blank.
  3. Use a hotkey to apply the template to newly created notes or even set the template to apply by default to quick notes.

- **Custom Snippet:** Another approach would be to create a custom CSS snippet to hide the title line in the quick note, but this would affect the display rather than actually making the title blank.

### 2. Creating a System Keybinding to Open Quick Note in a Specific Vault
While Obsidian doesn’t natively support vault-specific quick note keybindings, you can work around this by setting up:

- **System-Level Keybinding:** If you're on Linux (which you are), you can use a tool like `xdotool` to simulate keyboard shortcuts and commands. Here's how you could go about it:
  1. **Assign a Shortcut to Open a Vault:**
     Obsidian has vault-specific command line options (`--vault <vault name>`). You can create a desktop shortcut or a system-wide keyboard shortcut that uses this command:
     ```bash
     obsidian --vault <vault_name>
     ```
  2. **Use a Keybinding Manager:** You can set a specific keybinding using your desktop environment (like KDE) to open a specific vault and trigger the quick note functionality.

This way, you could set up different keybindings for each vault and have a streamlined workflow!