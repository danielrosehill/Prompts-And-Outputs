---
title: "setting up sway with fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Prompt Summary: You are asking how to start using Sway on Fedora and what steps are needed to configure it after installation.

To start using Sway on Fedora, follow these steps:

Step 1: Install Sway

First, make sure you have Sway installed. You can install it via DNF:

sudo dnf install sway

This command installs Sway and its necessary dependencies.

Step 2: Log Out and Start a Sway Session

1. Log out of your current desktop environment.


2. At the login screen, select your user account.


3. Look for a session switcher (usually a gear icon or a drop-down menu) and choose "Sway" from the list of available sessions.


4. Log in, and Sway should start.



Step 3: Basic Configuration

Sway reads its configuration from a file located at ~/.config/sway/config. By default, it should already be set up with reasonable defaults, but you can customize it to suit your preferences.

1. Create or Edit the Configuration File:

mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/config

This command copies the default configuration to your user directory, so you can customize it.


2. Customize the Config File:

Open ~/.config/sway/config in your preferred text editor.

You can set custom keybindings, wallpaper, application autostarts, and more.


Examples:

Set a wallpaper:

output * bg /path/to/your/wallpaper.jpg fill

Change keybinding to launch applications:

bindsym $mod+Return exec alacritty  # Use Alacritty as the terminal
bindsym $mod+d exec rofi -show drun  # Use Rofi for app launcher




Step 4: Running Sway from the Command Line (Optional)

If you prefer to start Sway directly from a virtual console (without a display manager), do the following:

1. Switch to a virtual console by pressing Ctrl + Alt + F3 (or F2/F4).


2. Log in with your username and password.


3. Type:

sway

This starts Sway from the terminal.



Step 5: Install Additional Tools (Optional)

Wayland-Compatible Applications: Sway is a Wayland compositor, so you’ll need Wayland-compatible applications. Most modern apps support Wayland, but if some don’t, you might need compatibility layers like XWayland.

Sway Tools:

swayidle: Manage screen locking and idle states.

swaylock: Screen locker for Sway.

wlr-randr or swaymsg: Manage display outputs (resolution, position).


Install these tools via DNF:

sudo dnf install swayidle swaylock waybar wlr-randr


Step 6: Autostart Applications and Services

You can add applications to automatically start by adding exec lines in your configuration:

exec firefox  # Start Firefox on login
exec waybar   # Start a Waybar status bar

Step 7: Explore Sway Commands and Keybindings

Press Mod + Shift + C to reload the Sway configuration without restarting Sway.

Press Mod + Shift + E to exit Sway.

Use swaymsg to interact with Sway from the command line, useful for scripting and managing layouts.


Notes

Mod Key: By default, Sway uses the Super (Windows) key as the Mod key, but you can change this in the config file.

Wayland-Specific Configs: Sway might behave differently than X11-based window managers, so if you encounter issues, check the Wayland equivalents for certain settings (e.g., screen rotation, keyboard layouts).


Once you have everything set up, Sway should give you a clean, tiling window manager experience on Fedora, similar to i3 but built for Wayland. Let me know if you need any further configuration tips!

