---
title: "Tiling window manager just for certain windows"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

For Sway, would it mean my whole desktop would need to be using a tiling window manger or could I just set it up to run on one window as desired?

# Output

In **Sway**, the entire desktop environment operates as a tiling window manager, meaning that if you run Sway, it will take over window management for your entire session. Unlike floating window managers (like KDE Plasma’s KWin), Sway and other tiling window managers manage all windows in a tiled, grid-like fashion across your entire desktop, rather than just in a single window or workspace.

### Option: Hybrid Setup with KDE Plasma (Floating + Tiling)

If you want **tiling** behavior for specific windows or applications without switching your entire desktop environment to a tiling window manager like Sway, you can achieve a **hybrid setup** within your existing **KDE Plasma** environment. Here’s how you can do this:

#### 1. **Enable Tiling Features in KWin (KDE Plasma)**

KDE Plasma's native window manager, **KWin**, has built-in support for tiling layouts, which can be customized with scripts or plugins. This means you can get tiling behavior for specific windows or applications while keeping the rest of your desktop in floating mode.

- **KWin Scripts**: There are scripts available for KWin that allow tiling behavior in a way similar to i3 or Sway but within Plasma's floating window manager. For example:
  - **Bismuth**: A popular tiling script for KDE Plasma. It allows you to tile windows dynamically and can be configured to tile only certain applications.
  - **Krohnkite**: Another great tiling script that works within KDE Plasma and enables tiling for selected applications.
  
  You can install these from KDE’s script store:
  - Go to **System Settings** → **Workspace** → **KWin Scripts** and download either **Bismuth** or **Krohnkite**.
  
  With these scripts, you can:
  - Tweak settings to tile only certain windows (like Vivaldi and external apps).
  - Keep the rest of your windows in floating mode.

#### 2. **Manually Tile Windows in KDE Plasma**

You can manually tile any combination of browser tabs and external programs by snapping windows to different parts of the screen in KDE Plasma. Plasma's **Window Snapping** feature lets you arrange windows side by side, which can somewhat mimic a tiling layout but isn't as dynamic as Sway or i3.

- Drag a window to the left or right edge of the screen to snap it to half of the screen.
- Use keyboard shortcuts (e.g., `Meta + Arrow Keys`) to tile windows into specific corners or halves of your screen.

#### 3. **Running Sway in Parallel (Nested in KDE)**

If you're specifically interested in **Sway** but don’t want it to take over your whole desktop session, you can run Sway inside a **nested session** on top of your current desktop environment (KDE Plasma). This allows you to run Sway in just one window, while still using KDE Plasma for everything else.

Here’s how to run Sway nested inside KDE Plasma:

1. Install **Sway** on Fedora:
   ```bash
   sudo dnf install sway
   ```

2. Run Sway in a nested Wayland session inside KDE:
   ```bash
   sway --nested
   ```

   This command runs Sway as a separate window inside your KDE Plasma session. You can tile browser windows and other apps inside this nested Sway window while leaving the rest of your desktop environment untouched.

#### 4. **Using Virtual Desktops or Activities**

Another KDE Plasma feature that can help with organization is **Virtual Desktops** or **Activities**. You could set up one virtual desktop or activity for tiling applications like Vivaldi and external programs, and leave the rest of your environment in floating mode.

- **Virtual Desktops**: Create a virtual desktop for tiling, where you manually tile and organize windows in a grid, while leaving other desktops as floating.
- **Activities**: Create a new activity dedicated to tiling, and switch between activities as needed.

### Summary of Options:
1. **KDE Plasma + Tiling Scripts**: Use tiling scripts like **Bismuth** or **Krohnkite** to tile specific applications while keeping your main desktop in floating mode.
2. **Manual Tiling in KDE Plasma**: Manually tile specific applications using KDE's built-in window snapping and keyboard shortcuts.
3. **Run Sway Nested**: Run Sway in a nested session on top of your KDE Plasma environment to use it for tiling only inside a single window.
4. **Virtual Desktops or Activities**: Organize tiling and floating applications across different virtual desktops or activities within KDE Plasma.

Would you like help setting up one of these options, or exploring a specific approach further?