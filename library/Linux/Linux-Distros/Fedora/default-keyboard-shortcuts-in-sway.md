---
title: "Default keyboard shortcuts in Sway"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Prompt Summary: You asked if there's a shortcut to open a terminal, applications menu, or web browser if nothing appears on the screen after launching Sway.

Yes, Sway has default keybindings, much like i3. If you see a blank screen after launching Sway, you can use these shortcuts:

Default Keybindings in Sway

Mod Key (Default): The Mod key in Sway is usually set to the Super (Windows) key.

This can be changed in the configuration if needed.



Here are the essential shortcuts:

1. Open a Terminal:

Press Mod + Enter (Default opens the alacritty terminal, or whatever is set in the configuration file).



2. Open an Application Menu (Launcher):

Press Mod + D to open wofi, dmenu, or another configured application launcher.

This brings up a menu where you can type the name of the application (e.g., firefox) and launch it.



3. Open a Web Browser (Custom Shortcut):

By default, there's no specific shortcut for a web browser. However, you can add one to your ~/.config/sway/config file:

bindsym $mod+b exec firefox

After adding this, pressing Mod + B will open Firefox.




What to Do If These Shortcuts Don’t Work

1. Edit the Configuration:

If pressing Mod + Enter doesn’t work, check the terminal application defined in ~/.config/sway/config. You might need to change it if the default terminal (alacritty) isn’t installed.

# Example change to use GNOME Terminal
bindsym $mod+Return exec gnome-terminal



2. Reload Configuration:

Press Mod + Shift + C to reload the Sway configuration file after making changes.




Manually Running Commands in a TTY

If nothing works, you can:

1. Switch to a TTY using Ctrl + Alt + F2.


2. Log in and manually start applications using:

swaymsg exec firefox

or

swaymsg exec gnome-terminal



These should help you get a terminal or application menu up and running on Sway. Let me know if you need further assistance with configuration!

