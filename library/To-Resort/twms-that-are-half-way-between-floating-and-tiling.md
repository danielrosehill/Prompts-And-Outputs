---
title: "TWMs that are half way between floating and tiling"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

are there any TWMs that are kind of middle ground solutions between traditional desktops and tiled displays? Like perhaps you can use tiling on only one screen?

# Output

Yes, there are **tiling window managers (TWMs)** that strike a **middle ground** between traditional desktops (floating windows) and tiled displays, and many of them allow you to **toggle between tiling and floating modes**, use tiling **on specific monitors**, or provide a hybrid experience. These options give you more flexibility than pure tiling or floating layouts.

Here are some **middle-ground TWMs** that offer a balance between tiled and floating window management, as well as features like enabling tiling on only one screen or dynamically switching between tiling and floating:

### 1. **AwesomeWM**
   - **Description**: **AwesomeWM** is a highly customizable and dynamic window manager that allows for both **tiling and floating windows**. It provides a range of layouts (tiling, floating, maximized, etc.), and you can toggle between them on a per-screen or per-workspace basis.
   - **Key Features**:
     - **Hybrid layouts**: You can tile windows on one monitor while keeping others in floating mode.
     - **Per-tag (workspace) configuration**: Each workspace can have its own layout, so you can have tiling on one and floating on another.
     - **Manual tiling**: You can tile windows on demand while keeping most in floating mode.
   - **Tiling on One Screen**: Yes, you can configure **AwesomeWM** to tile windows on one monitor while using floating windows on another.
   - **Why it's a middle ground**: It allows both tiling and floating layouts, with flexible configuration for each workspace and monitor.
   - **How to install on Fedora**:
     ```bash
     sudo dnf install awesome
     ```

### 2. **bspwm**
   - **Description**: **bspwm** is a tiling window manager that works with a **binary space partitioning** scheme, but it is also highly scriptable and lets you have more control over how windows behave. While primarily a tiling WM, you can easily set floating windows on one screen or workspace while tiling on another.
   - **Key Features**:
     - **Per-monitor tiling**: You can configure **bspwm** to tile windows only on a specific monitor.
     - **Per-window floating mode**: You can make certain windows float while others are tiled.
     - **Manual control**: You can script specific layouts and switch between floating and tiling modes on demand.
   - **Tiling on One Screen**: Yes, bspwm supports tiling on one monitor and floating windows on others.
   - **Why it's a middle ground**: Offers scriptable tiling and floating configurations, making it flexible for mixed setups.
   - **How to install on Fedora**:
     ```bash
     sudo dnf install bspwm
     ```

### 3. **XMonad**
   - **Description**: **XMonad** is a highly customizable tiling window manager written in **Haskell**. By default, it uses tiling, but it can be configured to switch between tiling and floating modes dynamically on a per-monitor or per-workspace basis.
   - **Key Features**:
     - **Multiple layouts**: You can define specific layouts for each workspace, including tiling on one screen and floating on another.
     - **Toggle floating mode**: You can toggle between floating and tiling modes for individual windows or entire workspaces.
     - **Custom layouts**: Create custom layouts based on your needs, such as enabling tiling only for certain applications or screens.
   - **Tiling on One Screen**: Yes, you can assign tiling to specific monitors or workspaces.
   - **Why it's a middle ground**: XMonad’s flexibility allows for tiling, floating, or hybrid modes depending on how you configure it.
   - **How to install on Fedora**:
     ```bash
     sudo dnf install xmonad
     ```

### 4. **HerbstluftWM**
   - **Description**: **HerbstluftWM** is a manual tiling window manager that lets you tile or float windows based on your preferences. It allows you to have **manual control over layouts**, so you can tile windows on one monitor and float them on another.
   - **Key Features**:
     - **Manual tiling**: You can choose which windows or screens are tiled or floating.
     - **Per-monitor workspaces**: Each monitor can have its own workspace with a different layout (tiling or floating).
     - **Scriptable control**: HerbstluftWM is scriptable, meaning you can configure layouts and window behavior in a very flexible way.
   - **Tiling on One Screen**: Yes, HerbstluftWM can be configured to tile only on one screen and float on others.
   - **Why it's a middle ground**: It offers manual tiling and floating, so you can have a mixed environment.
   - **How to install on Fedora**:
     ```bash
     sudo dnf install herbstluftwm
     ```

### 5. **Sway (for Wayland)**
   - **Description**: **Sway** is a tiling window manager for **Wayland** that is a drop-in replacement for **i3**. It allows both tiling and floating windows, and you can configure per-workspace or per-monitor tiling behavior. Sway offers the same flexibility as i3 but with Wayland’s advanced features.
   - **Key Features**:
     - **Per-monitor tiling**: You can configure Sway to only tile on one screen while keeping others floating.
     - **Floating windows**: Certain applications (like dialog boxes) can be kept floating while the rest are tiled.
     - **Wayland compositor**: Supports modern display protocols and smooth transitions between tiling and floating.
   - **Tiling on One Screen**: Yes, Sway allows tiling on a specific monitor while keeping others in floating mode.
   - **Why it's a middle ground**: You get the benefits of Wayland and i3’s tiling capabilities, with the option to float windows where necessary.
   - **How to install on Fedora**:
     ```bash
     sudo dnf install sway
     ```

### 6. **i3**
   - **Description**: **i3** is a lightweight tiling window manager, but it also supports **floating windows**. It’s possible to configure i3 to tile windows only on certain screens or for certain applications while allowing others to float.
   - **Key Features**:
     - **Floating mode**: You can mark certain windows as floating while others remain tiled.
     - **Per-screen tiling**: You can tile on specific monitors or workspaces while keeping others floating.
     - **Workspace-specific layouts**: You can configure specific workspaces to have floating or tiling behavior.
   - **Tiling on One Screen**: Yes, i3 allows tiling on one screen while keeping others in floating mode.
   - **Why it's a middle ground**: It's lightweight but flexible, allowing tiling on some screens or workspaces while floating windows on others.
   - **How to install on Fedora**:
     ```bash
     sudo dnf install i3
     ```

---

### Summary of Options:
| Tiling Window Manager | Key Feature                                                                 | Tiling on One Screen | Why It's a Middle Ground Solution                                   |
|-----------------------|-----------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------|
| **AwesomeWM**          | Hybrid layouts, per-monitor or per-workspace tiling/floating                 | Yes                  | Offers a blend of tiling and floating windows per workspace/monitor.|
| **bspwm**              | Scriptable tiling and floating control                                      | Yes                  | Highly scriptable, lets you tile on one screen and float on another.|
| **XMonad**             | Configurable layouts for per-monitor tiling and floating                     | Yes                  | Dynamic and customizable, allowing both tiling and floating setups. |
| **HerbstluftWM**       | Manual control over tiling and floating, scriptable for hybrid layouts       | Yes                  | Lets you manually tile certain screens or apps while floating others.|
| **Sway**               | Tiling and floating per-monitor, built on Wayland                           | Yes                  | Combines i3 tiling with modern Wayland display capabilities.         |
| **i3**                 | Floating windows, per-monitor or per-workspace tiling                        | Yes                  | Lightweight with flexible tiling and floating window control.       |

### Conclusion:
If you want a **middle-ground tiling window manager** that allows you to have tiling on only one screen while keeping the rest of your setup with floating windows, you have a few good options:

- **AwesomeWM** and **bspwm** are great choices for those who want scriptable, flexible environments where tiling can be applied per monitor or workspace.
- **Sway** is ideal if you want **Wayland support** with tiling and floating capabilities, and **i3** offers a similar experience for **X11**.
- **HerbstluftWM** and **XMonad** offer manual control and a lot of flexibility for mixed tiling and floating setups.

Let me know if you’d like help setting up any of these or more specific guidance on a particular window manager!