---
title: "TMWs with Fedora support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here's a list of **tiling window managers (TWMs)** that work well on **Fedora**, along with the most popular and well-supported options. I’ll also cover features like **multi-monitor support** and whether they allow tiling on only one display.

### Popular Tiling Window Managers for Fedora

1. **i3**
   - **Description**: One of the most popular tiling window managers, i3 is lightweight and highly configurable. It allows you to manage windows efficiently with keyboard shortcuts.
   - **Popularity**: Very popular, especially among those who want simplicity and speed.
   - **Multi-Monitor Support**: Yes, supports multiple monitors natively.
   - **Tiling on One Display**: You can tile windows on one monitor while leaving others untouched. i3 supports independent workspaces on each monitor, so tiling behavior can be customized per display.
   - **Well-Supported**: i3 has extensive documentation and a large user base, making it well-supported.

2. **Sway**
   - **Description**: Sway is a drop-in replacement for i3 but runs on **Wayland** instead of X11. It uses the same configuration syntax as i3 but works with Wayland's modern display features.
   - **Popularity**: Gaining popularity, especially as Wayland adoption increases.
   - **Multi-Monitor Support**: Yes, fully supports multiple monitors with Wayland’s advanced handling.
   - **Tiling on One Display**: Yes, like i3, Sway allows you to configure tiling per monitor, so you can choose which display gets tiled windows.
   - **Well-Supported**: Actively developed and well-supported, especially in the Wayland ecosystem.

3. **bspwm**
   - **Description**: A minimalist tiling window manager that organizes windows in a binary tree structure. It’s highly scriptable and controlled through the **bspc** utility.
   - **Popularity**: Popular among users who prefer a highly configurable, scriptable tiling manager.
   - **Multi-Monitor Support**: Yes, bspwm supports multiple monitors and independent workspaces on each.
   - **Tiling on One Display**: You can control window tiling on a per-monitor basis. Each monitor can have its own set of workspaces and tiling behavior.
   - **Well-Supported**: Has a strong community, but customization requires scripting.

4. **AwesomeWM**
   - **Description**: A highly customizable tiling window manager that uses Lua for configuration. It’s dynamic and provides many features out of the box, including widgets.
   - **Popularity**: Popular among users who want more customization options and built-in features.
   - **Multi-Monitor Support**: Yes, supports multiple monitors and handles them well.
   - **Tiling on One Display**: You can configure tiling layouts per monitor. Each monitor can have a different workspace and tiling mode.
   - **Well-Supported**: Very well supported with active development and a large community.

5. **XMonad**
   - **Description**: A tiling window manager written in Haskell. It’s very minimal but powerful, with configurations written in Haskell.
   - **Popularity**: Popular among developers, especially those familiar with functional programming and Haskell.
   - **Multi-Monitor Support**: Yes, supports multiple monitors natively and handles them well.
   - **Tiling on One Display**: Yes, XMonad allows you to configure tiling independently for each monitor.
   - **Well-Supported**: Well-supported, but configuration requires knowledge of Haskell, which may have a steeper learning curve.

6. **HerbstluftWM**
   - **Description**: A manual tiling window manager that uses an external command interface for configuration. It allows for very precise control over window placement and layout.
   - **Popularity**: Popular among users who prefer manual tiling and scripting.
   - **Multi-Monitor Support**: Yes, supports multiple monitors and lets you control how each monitor behaves.
   - **Tiling on One Display**: You can tile windows on specific monitors and leave others with floating windows or different tiling behavior.
   - **Well-Supported**: Has an active community, but less popular than i3 or AwesomeWM.

7. **dwm (Dynamic Window Manager)**
   - **Description**: A minimal tiling window manager written in C. It is extremely lightweight, with minimal features out of the box. You customize dwm by editing its source code and recompiling.
   - **Popularity**: Popular among minimalists who want full control over their window manager.
   - **Multi-Monitor Support**: Yes, dwm supports multiple monitors with Xinerama.
   - **Tiling on One Display**: You can tile windows on one monitor while having different layouts on other monitors, but customization is manual and requires modifying the source code.
   - **Well-Supported**: Has a strong community, but requires a hands-on approach to configuration.

8. **Qtile**
   - **Description**: A tiling window manager written in Python. It's highly configurable and designed to be simple to extend, making it accessible for users who prefer scripting in Python.
   - **Popularity**: Popular among Python users who want a programmable window manager.
   - **Multi-Monitor Support**: Yes, Qtile supports multiple monitors.
   - **Tiling on One Display**: You can customize layouts and tiling behavior per monitor, making it easy to tile on only one screen.
   - **Well-Supported**: Has a good community and active development.

9. **SpectrWM**
   - **Description**: A simple and lightweight tiling window manager that aims to be easy to configure while remaining minimal.
   - **Popularity**: Popular among users who want a fast, minimal window manager that’s easy to configure.
   - **Multi-Monitor Support**: Yes, SpectrWM supports multiple monitors natively.
   - **Tiling on One Display**: You can control the tiling behavior per monitor.
   - **Well-Supported**: Has a smaller but active community.

---

### Most Popular & Well-Supported Tiling Window Managers:
1. **i3** – Extremely popular, widely used, and highly configurable.
2. **Sway** – Growing in popularity with Wayland support; best for those using modern systems.
3. **bspwm** – Popular among users who want scriptability and customization.
4. **AwesomeWM** – Best for users who need more built-in features and a flexible layout.
5. **XMonad** – Popular among developers, especially those familiar with Haskell.

### Multi-Monitor Support:
All of the tiling window managers listed above support multiple monitors. Each of them allows you to:
- **Manage different workspaces or layouts** on each monitor.
- **Tile on one display** while leaving others either floating or with different layouts. Most of them allow independent control of tiling behavior per display.

### Which Should You Choose?
- **i3** or **Sway**: Best for most users who want a straightforward, widely supported tiling window manager with great multi-monitor support.
- **bspwm** or **AwesomeWM**: If you want more control, scriptability, or built-in features.
- **XMonad**: Ideal for users who want a highly customizable environment and are comfortable with Haskell.

If you want specific features (like tiling on only one monitor), all of the window managers listed support that feature in some form, so your choice comes down to how much customization and control you want.

Let me know if you need any help configuring any of these or further details on setting them up on Fedora!