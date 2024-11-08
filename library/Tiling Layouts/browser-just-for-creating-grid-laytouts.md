---
title: "Browser just for creating grid laytouts"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

perhaps you can think of a browser that can run on fedora and which has native support for creating grid layouts using tabs? Maybe even a browser that is designed just todo this?

# Output

Yes, there are several tools available on Fedora that allow you to manage windows in a **tiling grid layout** without replacing your desktop environment (KDE Plasma, in your case). These tools act as tiling window managers but can run **on top of your existing desktop environment**, allowing you to organize and manage application windows in a grid or tiling layout. Here are a few recommendations:

### 1. **Krohnkite (KWin Script for KDE)**
Krohnkite is a KWin script that adds tiling window management features to **KDE Plasma** without needing a full tiling window manager like i3 or bspwm. It lets you tile, stack, and manage windows in various layouts (grid, columns, etc.) and can work alongside your existing KDE setup.

#### Key Features:
- Tiling window management within **KDE Plasma**.
- Supports various tiling modes like **grid**, **monocle**, and **spiral**.
- Easily activated and deactivated, so you can switch between tiling and floating modes as needed.
- Configurable keyboard shortcuts for efficient window management.

#### Installation on Fedora:
1. **Install Krohnkite via KDE Store:**
   - Open **System Settings > Window Management > KWin Scripts**.
   - Search for **Krohnkite** in the KDE Store and install it.
   - Enable Krohnkite and configure its settings for tiling layouts.
   
2. **Manual Installation:**
   You can also install Krohnkite from GitHub:
   ```bash
   git clone https://github.com/esjeon/krohnkite.git
   cd krohnkite
   ./install.sh
   ```

#### Usage:
- Once installed, you can use Krohnkite to tile windows into a grid or other layouts. The tiling will automatically adjust as you open and close windows.

### 2. **Tiling Assistant (for GNOME, also works in KDE Plasma)**
**Tiling Assistant** is a GNOME Shell extension that brings tiling window management features to the GNOME desktop. However, it can also work on **KDE Plasma** with some tweaking or by running GNOME-based apps. It lets you create custom grid layouts for your applications.

#### Key Features:
- Create customizable grid layouts.
- Snap windows to predefined grid positions.
- Easily switch between tiled and floating modes.
  
#### Installation:
1. You can install it through GNOME extensions on Fedora.
2. Alternatively, search for **Tiling Assistant** in your software center, or run:
   ```bash
   sudo dnf install gnome-shell-extension-tiling-assistant
   ```

Note: While it's mainly intended for GNOME, some users report success using it with KDE apps via XWayland.

### 3. **WinTile**
**WinTile** is a simpler window manager application designed to tile windows into grid layouts. It doesn't replace your desktop environment but runs as an additional tool on top of your existing DE (KDE Plasma).

#### Key Features:
- Manages windows in grid layouts.
- Simple, lightweight, and easy to use.
- Keyboard shortcuts for tiling and resizing windows.

#### Installation:
Since WinTile is a lightweight tool, you can typically find it in your package manager:
```bash
sudo dnf install wintile
```

Once installed, you can configure the grid size and apply the tiling layouts to your open windows.

### 4. **Amethyst for Linux (Similar to Mac's Amethyst)**
While **Amethyst** is originally a tiling window manager for macOS, there are similar implementations for Linux, including Fedora. Amethyst-style tiling managers focus purely on tiling windows in custom grid layouts without modifying your entire desktop environment.

#### Installation and Setup:
For a similar tiling manager on Fedora, you may need to explore lightweight window management utilities like **Tiling Assistant**, or even write simple scripts to replicate Amethyst-style layouts if needed.

### 5. **Bismuth (Fork of Krohnkite)**
**Bismuth** is a fork of Krohnkite that works similarly but offers additional configuration options. It provides tiling capabilities within **KDE Plasma**, making it a good choice if you want a feature-rich tiling experience without switching to a full tiling window manager.

#### Installation:
You can install Bismuth directly from GitHub:
```bash
git clone https://github.com/Bismuth-Forge/bismuth.git
cd bismuth
./install.sh
```
Once installed, you can configure and control window tiling directly from your KDE environment.

### 6. **x-tile (General Tiling Utility)**
**x-tile** is a standalone window tiling manager that lets you arrange open windows in various tiling configurations without changing the desktop environment. You can manually control how windows are tiled, snapped, and resized.

#### Key Features:
- Supports grid, column, and row layouts.
- Simple graphical interface for configuring and arranging windows.
- Works with multiple window managers and desktop environments, including KDE.

#### Installation on Fedora:
```bash
sudo dnf install x-tile
```

#### Usage:
- Run `x-tile`, and it will provide a simple interface to manage the tiling of all open windows.
- You can define custom grid layouts for multiple applications, including ChatGPT.

### Summary of Options:
- **Krohnkite or Bismuth**: Ideal if you want to stay within KDE Plasma and add powerful tiling functionality without switching to a full tiling window manager.
- **Tiling Assistant**: Works best on GNOME but can work with KDE in some setups.
- **x-tile**: A simple standalone tiling manager that works with various environments.
- **WinTile**: For simple grid layouts without extensive setup.

Would you like assistance in setting up any of these tools on your Fedora system?