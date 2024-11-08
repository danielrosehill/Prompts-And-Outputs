---
title: "Obsidian - create new note with specific template"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm using Obsidian. I've created a template which I would like to automatically apply as the default for new notes that I create using a hotkey - and I've specified a default folder. What I'd like to do now is bind my hotkey (Ctrl + N) so that whenever I use it it will automatically create a new note with the specified template. Show me how please

# Output
To set up Obsidian to automatically apply a template when creating a new note using a hotkey, you'll need to follow these steps:

## Install and Configure Templater Plugin

1. Install the Templater plugin if you haven't already.
2. Set up your template folder and create your desired template.

## Configure Hotkey for Template Creation

1. Go to Settings > Hotkeys.
2. Search for "Templater: Create new note from template".
3. Assign Ctrl+N as the hotkey for this command[1][4].

## Set Up Default Template

1. Open Templater plugin settings.
2. In the "Folder Templates" section, specify your default folder and the template you want to use[1].

## Modify Default "New Note" Behavior

1. Go back to Settings > Hotkeys.
2. Search for "Create new note".
3. Remove the existing Ctrl+N hotkey by clicking the "X" icon next to it.
4. Click the "+" icon to add a new hotkey, but don't assign anything[5].

Now, when you press Ctrl+N, it will create a new note using your specified template in the default folder you've set up.

## Additional Options

If you need more complex automation, consider these alternatives:

1. **QuickAdd plugin**: This plugin allows for more advanced automation, including creating notes with specific templates in designated folders[2].

2. **Folder-specific templates**: You can set up Templater to use different templates based on which folder you're creating the note in[1].

3. **Custom scripts**: For even more customization, you can create a custom Templater script that handles file creation, naming, and placement[3].

By following these steps, you should now have a streamlined process for creating new notes with your preferred template using the Ctrl+N hotkey.

 