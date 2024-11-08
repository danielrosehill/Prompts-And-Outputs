---
title: "Creating a keyboard binding for the Git push shortcut"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Do you remember that you helped me to create a bash alias earlier? It's working great. I'm wondering would it be possible to create a shortcut assignment. I'd like to be able to bind a button (let's say scroll lock) to execute this script. But I would need to be in the right context (say a terminal window). What's the best way to achieve this

# Output

To achieve this, you can create a keybinding that triggers the Bash script only in the terminal context. Here are a few options for setting this up:

### 1. **Using `xbindkeys` (For Global Keybindings)**
`xbindkeys` is a versatile tool that can help you map keys to commands, including your script, only if you're in the correct context (like the terminal).

#### Installation:
```bash
sudo apt install xbindkeys xdotool
```

#### Configuration:
1. **Create/Edit Configuration File:**
   Run:
   ```bash
   xbindkeys --defaults > ~/.xbindkeysrc
   ```
   This will create a default configuration file.

2. **Add Keybinding for Scroll Lock:**
   Edit `~/.xbindkeysrc` to include a new keybinding for Scroll Lock that executes your alias or script.

   Example:
   ```bash
   "xdotool search --class gnome-terminal windowactivate && bash -c 'source ~/.bash_aliases && your_alias'"
   Scroll_Lock
   ```

   - **`xdotool search --class gnome-terminal windowactivate`** will focus the terminal window.
   - **`your_alias`** should be replaced with the actual name of your alias or the full path to your script.

3. **Run `xbindkeys`:**
   ```bash
   xbindkeys
   ```
   You can add `xbindkeys` to your startup applications to ensure it runs on boot.

### 2. **Using `.inputrc` (For Terminal Shortcuts Only)**
If you only need this to work within the terminal (not globally), you can modify `.inputrc`, which is a configuration file for terminal input.

1. Edit `.inputrc` (usually located in your home directory):
   ```bash
   "\e[23~": "your_alias\n"
   ```
   - This will bind `Scroll Lock` (escape sequence may vary) to your alias.

2. Reload `.inputrc`:
   ```bash
   bind -f ~/.inputrc
   ```

### 3. **Using `autokey` (For More Control)**
If you want a GUI-based tool that can recognize specific context, `autokey` could be a good option.

#### Installation:
```bash
sudo apt install autokey-gtk
```

#### Configuration:
- Open `autokey` and create a new script.
- Set the **Hotkey** to `Scroll Lock`.
- In the **Script** field, add something like:
  ```python
  import os
  os.system('gnome-terminal -- bash -c "source ~/.bash_aliases && your_alias; exec bash"')
  ```
- You can also set a condition to trigger only when the terminal is focused.

### Summary:
- Use **`xbindkeys`** for a global solution to bind `Scroll Lock` to your script with context awareness.
- Modify **`.inputrc`** if you want this binding to only work in terminal sessions.
- Alternatively, use **`autokey`** if you prefer a more user-friendly GUI tool.

Let me know which approach you prefer, or if you need more specific steps to get started!