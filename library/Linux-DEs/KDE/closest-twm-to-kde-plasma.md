---
title: "Closest TWM to KDE Plasma"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm currently using KDE Plasma. So Sway would be the TWM that's closest to what I'm using? I don't want to find that a bunch of stuff stops working
# Output

If you’re using **KDE Plasma** and are looking to try a **tiling window manager (TWM)** while maintaining compatibility with most of your current setup, **Sway** may **not** be the closest option. Here’s why:

### Compatibility with KDE Plasma
- **KDE Plasma** is built on the **X11** or **Wayland** display server, but its window management and UI features are tightly integrated with the **KWin** window manager (the default window manager for KDE).
- **Sway** is a tiling window manager designed to run on **Wayland** and is a replacement for **i3**, but it **does not integrate directly** with KDE’s desktop environment, as it's a standalone Wayland compositor. Switching to Sway from KDE Plasma would require you to leave behind a lot of KDE’s desktop functionality, especially the Plasma panels and widgets.
  
If you want to **retain KDE Plasma's desktop environment and features** while using tiling, I would recommend looking at **KWin's built-in tiling features** or other options that work **within** the KDE Plasma environment.

### Best Options for Tiling with KDE Plasma

1. **KWin Tiling Scripts** (Most Compatible)
   - **Description**: **KWin**, KDE's window manager, supports **tiling via scripts**. This allows you to have tiling window management **without leaving KDE Plasma**.
   - **How it works**: You can install a **tiling script** to enable tiling functionality within KWin itself. This keeps your entire KDE setup intact, including Plasma panels, widgets, and other KDE-specific features.
   - **Tiling Features**: You can tile windows automatically, similar to how i3 works, but without losing the standard KDE Plasma desktop experience.
   - **Popular KWin Tiling Scripts**:
     - **Krohnkite**: Adds dynamic tiling to KWin. It supports features like dynamic tiling, multiple layouts, and advanced tiling similar to i3.
       - **How to install**: 
         1. Open KDE’s **System Settings**.
         2. Go to **Window Management** > **KWin Scripts**.
         3. Click **Get New Scripts** and search for **Krohnkite**.
         4. Install and enable it.
     - **Bismuth**: Another popular KWin tiling script, offering better tiling controls and customization for Plasma users.
       - **How to install**: It can be installed from the [Bismuth GitHub](https://github.com/Bismuth-Forge/bismuth) or through KDE’s KWin script repository.
   - **Why it’s ideal**: You maintain KDE Plasma's desktop environment and features while getting tiling functionality.

2. **i3 + KDE Plasma Hybrid** (Compatible but More Configuration)
   - **Description**: You can run **i3** as a tiling window manager **inside KDE Plasma**. This setup gives you the benefits of i3's tiling functionality while still using KDE Plasma for desktop management, panels, widgets, and other features.
   - **How it works**:
     1. Install **i3** on Fedora:
        ```bash
        sudo dnf install i3
        ```
     2. Configure i3 to run as an **alternative window manager** within KDE Plasma. You can modify your session to launch **i3** as the window manager while keeping KDE’s desktop components.
     3. This setup requires some tweaking to ensure KDE’s panels and widgets work well with i3’s tiling.
   - **Why it’s useful**: You retain Plasma’s features and gain the full tiling experience of i3. However, it requires more effort to set up and maintain than just using KWin’s tiling scripts.

3. **bspwm + KDE Plasma** (Similar to i3, but Manual Tiling)
   - **Description**: **bspwm** can also be run as a window manager within KDE Plasma. It allows for more control over window placement and tiling, but like i3, it will require configuring bspwm to work alongside KDE’s desktop environment.
   - **How it works**:
     1. Install **bspwm** on Fedora:
        ```bash
        sudo dnf install bspwm
        ```
     2. Modify your KDE session to run **bspwm** as the window manager, while keeping the KDE Plasma desktop active.
     3. As with i3, this requires configuring **bspwm** to coexist with Plasma components.
   - **Why it’s useful**: You get the flexibility of **bspwm** while still using KDE Plasma’s desktop features.

---

### Which Option is Closest to Your Current Setup?

- **KWin Tiling Scripts (Krohnkite or Bismuth)**: This is the **best option** if you want to add tiling functionality **without leaving KDE Plasma**. It integrates seamlessly with the desktop and requires minimal setup.
- **i3 or bspwm with KDE Plasma**: This gives you full tiling control but requires more configuration and doesn’t integrate as smoothly as KWin’s built-in features.
- **Sway**: While Sway is a great tiling window manager, it’s a **standalone compositor for Wayland** and would replace your entire KDE Plasma setup. You’d lose KDE’s desktop environment (like Plasma panels and widgets), which might cause some of your usual desktop functionality to stop working.

### Multi-Monitor Support
All of the mentioned solutions, whether **KWin Tiling Scripts**, **i3**, **bspwm**, or **Sway**, fully support multiple monitors. With any of these setups, you can configure tiling behavior on a per-monitor basis, meaning you can choose to use tiling only on one display while keeping the other(s) in floating or traditional mode.

### Conclusion:
- **For minimal disruption** and maintaining KDE Plasma’s features, I recommend using **Krohnkite** or **Bismuth** (KWin tiling scripts). They integrate directly into KWin, giving you tiling features without needing to switch window managers.
- If you want to try a true tiling window manager, **i3** or **bspwm** can be used within KDE Plasma, but this requires more setup and might introduce minor conflicts with KDE components.
- **Sway** is not ideal for KDE Plasma users unless you want to fully switch to Wayland with a standalone tiling environment, which would result in losing KDE’s desktop components.

Let me know if you’d like more details on installing or configuring any of these options!