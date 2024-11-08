---
title: "Text snippet manager for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I spend a lot of time prompting LLMs and working with them professionally. Frequently I need to enter the same text strings whether in prompts or in feedback messages - things like "please return the full codeblock in one go". I'd love to be able to speed this up a bit. This seems like an ideal application for text snippets. Can you think of some way that I could leverage them for this purpose? Perhaps a hotkey triggers a little snippet library I can search through or something less elaborate? I use KDE Plasma + Wayland

# Output

Using text snippets can indeed significantly speed up your workflow when working with LLMs. For KDE Plasma on Wayland, there are a few options you can consider:

## KDE Plasma Built-in Features

KDE Plasma offers some built-in functionality that can help:

1. **Custom Shortcuts**: 
   - Go to System Settings > Shortcuts > Custom Shortcuts
   - Create a new shortcut and set it to run a command that copies your snippet to the clipboard
   - Use `echo "Your snippet text" | wl-copy` as the command

2. **KRunner Snippets**:
   - KRunner (activated with Alt+Space by default) has a calculator feature
   - You can create aliases for your snippets, e.g., `snippet1 := "please return the full codeblock in one go"`
   - Then type `snippet1` in KRunner to copy it to clipboard

## Third-Party Solutions

For a more robust snippet management system, consider:

1. **KDE Plasma Clipboard**:
   - While not a dedicated snippet manager, you can pin frequently used text in the clipboard
   - Access it quickly with the default shortcut Ctrl+Alt+V

2. **Espanso**:
   - A cross-platform text expander that works on Wayland[1]
   - Create a configuration file with your snippets
   - Trigger snippets by typing short forms, e.g., `;full` expands to "please return the full codeblock in one go"

3. **Custom Script with fzf**:
   - Create a script similar to the one described in the search results[3]
   - Use `fzf` for fuzzy searching through your snippets
   - Bind the script to a custom shortcut in KDE

Here's a simple implementation of the fzf method:

1. Create a text file (`~/.snippets.txt`) with your snippets:

```
---
please return the full codeblock in one go
tags: llm, code
---
another common snippet
tags: llm, feedback
```

2. Create a script (`~/bin/fzsnip`):

```bash
#!/bin/bash

selected="$(cat ~/.snippets.txt | sed -e 's/^---$/\n/g' | fzf -i -e)"
echo -e "$selected" | sed -e 's/tags:.*$//;$d' | wl-copy
```

3. Make the script executable: `chmod +x ~/bin/fzsnip`

4. Create a custom shortcut in KDE Plasma:
   - Command: `alacritty --class 'snippets' -e bash -c '~/bin/fzsnip'`
   - Shortcut: Choose your preferred key combination

This setup will allow you to quickly search and copy snippets to your clipboard, which you can then paste into your LLM interface.

Remember to choose the method that best fits your workflow and preferences. The fzf method offers flexibility and quick searching, while Espanso provides seamless expansion without additional windows.

Citations:
[1] https://github.com/knqyf263/pet
[2] https://phabricator.kde.org/T17406
[3] https://luxagraf.net/src/replacing-autokey-wayland-plain-text-snippets
[4] https://wiki.documentfoundation.org/Documentation/XHP_Code_Snippets_for_KDE_Editors
[5] https://wiki.archlinux.org/title/Screen_capture
[6] https://www.youtube.com/watch?v=90xoathBYfk
[7] https://ubuntuforums.org/showthread.php?t=2498017