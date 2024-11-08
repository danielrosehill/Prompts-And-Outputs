---
title: "Obsidian plugin to take an inventory of your current plugin config"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there an obisidn plugin that I can use to take an inventory of the plugins I'm currently using in my vault ?

# Output

Yes, there are a couple of ways to create an inventory of the plugins you're using in your Obsidian vault. Here are the options:

### 1. **Plugin List Plugin**
   - **Plugin List** is a community plugin designed specifically for this purpose. It allows you to generate a list of all installed plugins within your vault.
   - The list can be exported as Markdown, making it easy to document which plugins are currently active.
   - You can install this plugin from the community plugins store:
     1. Go to **Settings > Community Plugins** and search for "Plugin List."
     2. After installation, run the plugin from the Command Palette (press `Ctrl/Cmd + P` and search for "Generate Plugin List").

### 2. **Metadata Extractor**
   - The **Metadata Extractor** plugin is another option that can be used to extract various pieces of metadata from your vault, including active plugin information.
   - This plugin is more general-purpose, but it can be configured to generate a detailed inventory, including settings and configurations for each plugin.

### 3. **Vault Statistics Plugin**
   - **Vault Statistics** provides detailed insights into your vault, including plugins. It’s not solely focused on plugins but can be useful for an overall inventory, including file types, notes, and installed plugins.
   - You can use the **Command Palette** to generate the inventory and save the results to a note if needed.

### 4. **Manual Method with "Obsidian Custom CSS & Settings Extractor"**
   - Another option, albeit manual, is to access the `plugins.json` file within your vault directory.
   - You could use a tool like the **Obsidian Custom CSS & Settings Extractor** to extract this information and save it in a more readable format within your vault.

These plugins will help you create an inventory of all the plugins you’re currently using in your vault. **Plugin List** is the simplest and most direct way to do this if your goal is just to document which plugins are active. Let me know if you need any assistance in setting these up!