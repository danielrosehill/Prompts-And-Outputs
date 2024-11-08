---
title: "Can I get a programmatic representation of these two display windows"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


![[Can I get a programmatic representation of these two display windows.png]]

# Prompt

here's how I currently have Obsidian and ChatGPT laid out on my KDE Plasma + Fedora desktop. Is there any way to get a programmatic representation of this layout from a CLI?

# Output

To programmatically capture the layout of your windows in KDE Plasma, you can use **KWin's** built-in window management system via the command line. This will allow you to fetch window IDs, positions, and dimensions. Here’s a general approach you can take:

### Step 1: Use `wmctrl` to List Open Windows
You can install and use `wmctrl`, a command-line tool that interacts with the X Window Manager, to get the details of the currently open windows.

1. Install `wmctrl` (if not already installed):
   ```bash
   sudo dnf install wmctrl
   ```

2. List all open windows:
   ```bash
   wmctrl -lG
   ```

   This will output something like:
   ```
   0x03800007  0  1920 0   960  1080  daniel-Desktop ChatGPT Window
   0x03a00007  0  0    0   1920 1080  daniel-Desktop Obsidian
   ```

   - The columns represent the **window ID**, **desktop number**, **x-coordinate**, **y-coordinate**, **width**, **height**, and **window name**.
   - This information gives you the position and size of each window.

### Step 2: Use `xrandr` to Get Display Resolution
To understand the layout in terms of your screen resolution, you can check your display resolution using `xrandr`.

1. Run:
   ```bash
   xrandr
   ```

   This will output information about your display resolution and connected monitors. Example:
   ```
   Screen 0: minimum 320 x 200, current 3840 x 2160, maximum 16384 x 16384
   eDP1 connected primary 1920x1080+0+0
   HDMI1 connected 1920x1080+1920+0
   ```

   - This helps understand how the windows are laid out across multiple monitors.

### Step 3: Automate or Save the Layout
You can create a script to capture the window positions and dimensions using `wmctrl` and then later use `wmctrl` to move and resize the windows to their previous positions.

For example, to move a window to a specific position:
```bash
wmctrl -i -r 0x03800007 -e 0,1920,0,960,1080
```

- The `-i` flag refers to the window ID (from `wmctrl -lG`).
- The `-e` option takes `gravity,x,y,width,height` values to reposition and resize the window.

### Alternative: Use KWin Scripts
KDE Plasma’s KWin allows more advanced scripting for window management. You can write **KWin scripts** that could save and restore window positions, but this requires a bit more setup and scripting knowledge using JavaScript.

### Summary:
Using tools like `wmctrl` and `xrandr`, you can get a programmatic view of your desktop layout, including window positions and sizes. If needed, you can write a script to save the current layout and restore it later using similar tools.