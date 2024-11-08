---
title: "Exploring ways to use a TWM just for a screen or certain applications"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


It sounds like your ideal setup is to use a **tiling window manager (TWM)** in combination with your current KDE Plasma environment, but only for certain applications or on a specific screen. This way, you can benefit from the tiling behavior where it’s useful (such as for development or multitasking), while retaining the default floating behavior of KDE for other tasks. While this is a non-standard use of a tiling window manager, there are some approaches that might help achieve your goal:

### Approaches to Use a Tiling Window Manager Like an Application:

#### 1. **Running a TWM as a Floating Application (Tiling Window Manager in a Window)**
Some tiling window managers can be run within a **single floating window** as an application, which will allow you to tile and manage windows inside that single window without affecting your entire desktop environment.

- **Xnest + i3/bspwm/Sway**:
  - **Description**: You can run a tiling window manager like **i3**, **bspwm**, or **Sway** inside a windowed X11 session (using **Xnest**) or **Wayland** compositors inside a nested window. This allows you to have a separate window that behaves like a TWM, but only within that space.
  - **How it works**:
    1. Install **Xnest**:
       ```bash
       sudo dnf install xorg-x11-server-Xnest
       ```
    2. Run **i3** (or another TWM) within **Xnest**:
       ```bash
       Xnest :1 -geometry 1920x1080 &
       DISPLAY=:1 i3 &
       ```
    3. This will create a window running the **i3** window manager within your existing KDE Plasma session. You can move it to a specific screen or monitor and manage your applications inside that window.
  - **Why it's useful**: You can run a tiling window manager within a single window and treat it like an application. This gives you full tiling control without disrupting your entire KDE Plasma setup.

#### 2. **Tiling on a Specific Monitor Only (Multi-Head Setup)**
Some tiling window managers can be configured to only tile windows on one monitor, leaving other monitors to function with KDE's normal floating windows. This allows you to **limit tiling** to a particular display.

- **i3 or bspwm with Multiple Monitors**:
  - **Description**: Both **i3** and **bspwm** support multi-monitor setups and can be configured to only tile windows on a specific monitor, leaving the others with KDE's default floating window behavior.
  - **How it works**:
    1. Use i3's or bspwm's configuration to set **workspaces** on one monitor and leave the others floating.
    2. In i3, you can assign workspaces to specific monitors. For example, if you want tiling only on your secondary monitor:
       - Edit `~/.config/i3/config`:
         ```bash
         workspace 1 output HDMI-1
         workspace 2 output HDMI-2
         ```
    3. This will confine tiling to the specific monitor assigned in the config file, while other monitors retain KDE's floating behavior.
  - **Why it's useful**: You can use the tiling window manager on one display while keeping KDE’s floating windows on another. This approach can be configured easily in i3 or bspwm.

#### 3. **Hybrid Setup (i3/BSPWM + KDE Plasma Hybrid Session)**
You can run **i3** or **bspwm** alongside KDE Plasma in a hybrid session. This setup allows you to use tiling for certain applications or on specific monitors while keeping the KDE Plasma environment intact.

- **How it works**:
  1. Install **i3** or **bspwm**:
     ```bash
     sudo dnf install i3
     ```
  2. Start a **hybrid session** with KDE Plasma and i3:
     - Configure your KDE Plasma session to run i3 alongside it. In this setup, KDE Plasma manages the desktop and panels, while i3 handles window tiling for certain applications or on specific monitors.
  3. Configure i3 to only tile certain applications or run on specific workspaces or monitors:
     - Use the i3 config to target specific applications or monitors. For example, you can bind certain workspaces to monitors, and only use i3 for tiling certain apps.
  4. Launch KDE Plasma and i3 together by modifying your session manager.

#### 4. **Sway Nested in a Wayland Session (Experimental)**
You can also run **Sway** in a **nested Wayland session** inside your existing KDE Plasma environment. This is a more experimental approach but could allow you to run Sway in a floating window or lock it to a specific monitor.

- **How it works**:
  - **Nested Sway**: Sway can be run as a **Wayland compositor inside a Wayland session**, which allows you to use Sway in a specific window or monitor.
  - This approach is a bit more complex but can provide a **tiling environment** in a specific part of your screen.

#### 5. **Xephyr + i3**
An alternative to **Xnest** is **Xephyr**, which is another nested X11 server. This lets you run a complete tiling window manager (like i3) in a **nested session** within your current KDE Plasma environment.
  
- **How it works**:
  1. Install **Xephyr**:
     ```bash
     sudo dnf install xorg-x11-server-Xephyr
     ```
  2. Run Xephyr and start i3 inside it:
     ```bash
     Xephyr :1 -screen 1280x720 &
     DISPLAY=:1 i3 &
     ```
  3. You’ll have i3 running within a Xephyr window, giving you a tiling window manager inside a floating window that you can use for specific tasks.

### Can You Lock Tiling to One Screen?
Yes, most of the tiling window managers that support **multiple monitors** (like **i3**, **Sway**, and **bspwm**) allow you to **restrict tiling to a specific monitor**. For example:
- In **i3**, you can assign workspaces to specific monitors.
- In **bspwm**, you can configure each monitor independently, allowing you to have tiling on one monitor and floating on others.

### Summary of Solutions:
- **Xnest/Xephyr + i3/bspwm**: Run i3 or bspwm inside a floating window as an application. This allows you to keep KDE Plasma’s environment while running a tiling window manager for specific tasks or apps.
- **i3/bspwm on One Monitor**: Configure i3 or bspwm to tile only on one display while keeping other monitors under KDE Plasma’s floating window control.
- **Sway Nested in Wayland**: Run Sway inside a nested Wayland session to use tiling on one part of your desktop (more experimental).
- **Hybrid i3 + KDE Plasma**: Combine i3 with KDE Plasma for a hybrid tiling setup.

### Conclusion:
To achieve your goal of using a tiling window manager only for certain apps or on one display while keeping the rest of your KDE Plasma environment intact:
- The **Xnest/Xephyr + i3** approach is probably the easiest to implement, as it allows you to run a tiling window manager like an application.
- Alternatively, configuring **i3 or bspwm** to tile on one monitor and leaving the others with KDE Plasma's floating behavior is a good solution for multi-monitor setups.

Let me know if you need help setting up any of these solutions!