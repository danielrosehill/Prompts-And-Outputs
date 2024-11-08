---
title: "Trying Qtile to manage Obsidian and ChatGPT"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt:** You want to try the QTile approach to manage ChatGPT and Obsidian in a split-screen layout, and you're requesting a full configuration script for this setup.

Here’s a basic **QTile** configuration script that sets up a split-screen layout with **ChatGPT** (in a browser) on the left and **Obsidian** on the right. This script also includes keybindings to launch both applications and manage them within a tiling layout.

### Full QTile Configuration Script

```python
from libqtile import layout, bar, widget
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy
from libqtile import hook
import subprocess

# Mod key (you can change this to mod4 for the Super/Windows key)
mod = "mod4"

# Keybindings for managing ChatGPT and Obsidian windows
keys = [
    # Launch ChatGPT in browser (you can modify this to the browser of your choice)
    Key([mod], "Return", lazy.spawn("firefox --new-window https://chat.openai.com"), desc="Launch ChatGPT in browser"),
    
    # Launch Obsidian
    Key([mod], "o", lazy.spawn("obsidian"), desc="Launch Obsidian"),

    # Window navigation
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    
    # Move windows in the layout
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    
    # Resize windows in the layout
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),

    # Toggle between layouts (optional)
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Close focused window
    Key([mod], "w", lazy.window.kill(), desc="Close focused window"),

    # Restart qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
]

# Define groups (workspaces) for different layouts
groups = [
    Group("1", layout="monadtall"),  # Main workspace with tiled windows (ChatGPT & Obsidian)
]

# Layout settings for tiling
layouts = [
    layout.MonadTall(border_focus="#ff0000", border_width=2, margin=8),  # Split layout
]

# Screen with bar (optional)
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
            ],
            24,
        ),
    ),
]

# Mouse and floating window configuration
mouse = []

floating_layout = layout.Floating()

@hook.subscribe.startup_once
def autostart():
    # Autostart applications (you can modify these as needed)
    subprocess.run(["firefox", "--new-window", "https://chat.openai.com"])  # Start ChatGPT
    subprocess.run(["obsidian"])  # Start Obsidian

# Qtile main configuration
main = None

# Focus follows mouse pointer
follow_mouse_focus = True

# Auto fullscreen
auto_fullscreen = True

# Config settings
wmname = "Qtile"
```

### Breakdown of the Key Components:

1. **Keybindings**:
   - `Mod + Return` launches **ChatGPT** in Firefox.
   - `Mod + o` launches **Obsidian**.
   - Navigation keys (`Mod + h`, `Mod + l`, etc.) control the focus and position of windows within the layout.
   - `Mod + Shift + h/l` resizes the windows to adjust the layout balance between ChatGPT and Obsidian.
   
2. **Layout**:
   - The layout used is **MonadTall**, which is a vertical tiling layout. The left window (ChatGPT) takes up one part of the screen, and the right window (Obsidian) takes the other.
   - You can modify the layout if you want to experiment with different styles (e.g., **Bsp** or **Tile**).

3. **Autostart**:
   - The `autostart` hook runs **Firefox** with the ChatGPT URL and **Obsidian** at startup, so they will automatically be in place when you log in to QTile.

4. **Screen Bar** (Optional):
   - The script includes a bar at the top with widgets like the clock, layout switcher, and system tray. You can remove or customize this section as needed.

### Installation and Setup:

1. **Install QTile**:
   If you don’t have QTile installed, use the following command:
   ```bash
   sudo dnf install qtile
   ```

2. **Apply the Configuration**:
   - Save the script above to `~/.config/qtile/config.py`.
   - Restart your session and select **Qtile** from the session options in your display manager (login screen).

3. **Start QTile**:
   After logging in to the QTile session, **ChatGPT** and **Obsidian** should open side by side automatically.

---

Let me know if you need any adjustments!