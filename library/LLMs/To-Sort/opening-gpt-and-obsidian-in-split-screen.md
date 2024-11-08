---
title: "Opening GPT and Obsidian in split screen"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To ensure both the **ChatGPT** and **Obsidian** windows take up exactly 50% of the screen and are in full screen, you will need to adjust their window sizes and positions to divide the screen equally between the two.

Assuming you are using a **single monitor** setup (or you want this on a specific monitor), here’s how you can calculate the window positions and sizes:

### Key Steps:
1. **Determine your screen resolution**: 
   - Use `xrandr` to find the resolution of your monitor. For example, let’s assume your screen resolution is **1920x1080**.
   - You want to split the screen horizontally, so each window will take up half of the screen width.

2. **Calculate Window Positions and Sizes**:
   - **ChatGPT**: Left half of the screen (50% width), full height.
   - **Obsidian**: Right half of the screen (50% width), full height.

   If your screen resolution is **1920x1080**, each window will be **960 pixels wide** (half of 1920) and **1080 pixels high** (full screen height).

### Programmatic Representation:

For a screen resolution of 1920x1080, the window positions and sizes would be as follows:

- **ChatGPT** (left half):
   - **Position**: `x=0`, `y=0`
   - **Width**: `960`
   - **Height**: `1080`

- **Obsidian** (right half):
   - **Position**: `x=960`, `y=0`
   - **Width**: `960`
   - **Height**: `1080`

### Adjusting the Script:
Now, you can modify your bash script to apply these new sizes and positions:

```bash
#!/bin/bash
# Move and resize ChatGPT to left half of the screen
wmctrl -i -r 0x02800004 -e 0,0,0,960,1080

# Move and resize Obsidian to right half of the screen
wmctrl -i -r 0x01e00004 -e 0,960,0,960,1080
```

### General Formula for Other Screen Resolutions:
- You can adjust this script for different screen resolutions by dividing the width by 2 for the two windows.
- For example, if your screen width is **2560px**, each window would get **1280px** in width, while the height would remain the full screen height (e.g., 1440px).

Here’s how you can compute it for other resolutions:

- **Left window (ChatGPT)**: 
   - x-coordinate = 0
   - width = screen width / 2
   - height = screen height
   - y-coordinate = 0

- **Right window (Obsidian)**:
   - x-coordinate = screen width / 2
   - width = screen width / 2
   - height = screen height
   - y-coordinate = 0

### Full Screen Option:
If you want to **maximize** both windows in KDE without manually adjusting each size, you can use KWin’s built-in window management shortcuts:

```bash
# Maximize ChatGPT (left half)
wmctrl -i -r 0x02800004 -b toggle,maximized_vert,maximized_horz

# Maximize Obsidian (right half)
wmctrl -i -r 0x01e00004 -b toggle,maximized_vert,maximized_horz
```

This approach will **automatically maximize** both windows to take up their respective portions of the screen.