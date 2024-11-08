---
title: "Looking into the hybrid setup option for TWM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you show me some documentation on getting the hybrid KDE Plasma + i3 setup working? Does it require a custom login screen? Because I have never seen or heard of it

# Output

Setting up a **hybrid KDE Plasma + i3** environment is not a common setup out of the box, but it is possible to configure **i3** to act as the window manager within KDE Plasma, combining the best of both worlds. This setup will allow you to use KDE’s desktop environment (panels, widgets, etc.) while having **i3** manage windows, which means you can tile windows but keep KDE’s overall look and feel.

Here's how to achieve this, along with some documentation and explanation. You won't necessarily need a custom login screen, but you will have to modify some configuration files to start **i3** alongside KDE Plasma.

### Steps to Create a Hybrid KDE Plasma + i3 Setup

#### 1. **Install i3 on Fedora**
   - First, you need to install **i3**.
   - Open a terminal and run the following command:
     ```bash
     sudo dnf install i3
     ```
   - This will install the i3 tiling window manager on your system.

#### 2. **Modify KDE Plasma to Use i3 as the Window Manager**
   - By default, KDE Plasma uses **KWin** as its window manager, but you can modify it to use **i3** instead.
   
   ##### Method 1: Using the `KDEWM` Environment Variable
   - KDE Plasma allows you to set an alternative window manager using the `KDEWM` environment variable.
   - Create or edit the following file:
     ```bash
     nano ~/.config/plasma-workspace/env/set_window_manager.sh
     ```
   - Add the following line to tell KDE to use **i3** as the window manager:
     ```bash
     export KDEWM=/usr/bin/i3
     ```
   - Save and close the file.
   
   ##### Method 2: Directly Modify the Session
   - Alternatively, you can modify the KDE Plasma session by creating a custom `.desktop` file for the session.
   - Create a file named `plasma-i3.desktop` in the `/usr/share/xsessions/` directory:
     ```bash
     sudo nano /usr/share/xsessions/plasma-i3.desktop
     ```
   - Add the following content to the file:
     ```ini
     [Desktop Entry]
     Type=XSession
     Exec=/usr/bin/startplasma-x11
     TryExec=/usr/bin/i3
     DesktopNames=KDE
     Name=Plasma with i3
     Comment=Plasma desktop with i3 window manager
     ```
   - Save and close the file.

   **Note**: The `/usr/bin/startplasma-x11` command ensures that KDE Plasma starts, but **i3** will replace **KWin** as the window manager.

#### 3. **Log Out and Select the New Session**
   - After modifying the session file, log out of your current session.
   - On the login screen (typically **SDDM** for KDE), select **Plasma with i3** from the session options.
   - This session will launch KDE Plasma, but **i3** will manage the windows instead of **KWin**.

#### 4. **Configure i3 for Use with KDE Plasma**
   - You can now configure **i3** as usual. The standard **i3** configuration file is located at `~/.config/i3/config`. You can customize your **i3** keybindings and behavior in this file.
   - For example, you might want to adjust **i3's** behavior to leave gaps around windows or manage specific applications differently when they interact with KDE's desktop components.

   A typical `i3` config might include some KDE-specific customizations like:
   ```bash
   # Start KDE's compositor manually
   exec --no-startup-id kwin_x11 --replace

   # Set up KDE's system tray and panels
   exec --no-startup-id plasmashell
   ```

#### 5. **Managing KDE Plasma Components**
   - KDE’s desktop environment, including **plasmashell** (for desktop icons and widgets) and **krunner** (application launcher), will continue to function as expected. 
   - You can still use **KDE Plasma's panels** and widgets while **i3** manages window tiling.

### 6. **Optional: Make KWin and i3 Interchangeable**
If you'd like to have an easy way to switch back to **KWin** from **i3** in case you want the classic KDE experience, you can add a keybinding in **i3** to replace it with KWin:

- In your i3 config file, add the following keybinding:
  ```bash
  bindsym $mod+Shift+q exec --no-startup-id kwin_x11 --replace
  ```
- This allows you to quickly switch back to **KWin** if needed.

---

### Useful Documentation and References:

1. **i3 User Guide**: The official i3 documentation is very thorough and covers all the key configurations:
   - [i3 Documentation](https://i3wm.org/docs/)

2. **KDE WM Swapping**: KDE's flexibility with the `KDEWM` variable is mentioned in the KDE Wiki:
   - [KDE Plasma with Custom Window Manager](https://userbase.kde.org/KWin#Use_a_different_window_manager)

3. **i3 with KDE Plasma GitHub Projects**:
   - There are community-maintained scripts and config examples for using i3 alongside KDE Plasma. Some of these setups are discussed in GitHub repositories, such as this [i3-KDE Integration Script](https://github.com/heckelson/i3-and-kde-plasma).

---

### Does This Require a Custom Login Screen?
No, you don't need to create a **custom login screen**. However, you do need to select the **custom session** (Plasma with i3) from the login screen (SDDM or whichever display manager you are using).

By following the steps above, you can retain most of KDE Plasma's functionality while using **i3** as the window manager for tiling. You can always switch back to **KWin** by logging into a regular **Plasma (KWin)** session or using a custom keybinding.

---

### Conclusion
- **Hybrid KDE Plasma + i3** can be achieved by replacing **KWin** with **i3** using the `KDEWM` environment variable or a custom session.
- You’ll be able to tile windows using **i3** while keeping KDE's desktop environment, including panels and widgets.
- No custom login screen is needed, but you will select the session from the default login screen.

Let me know if you need more help with the setup or troubleshooting!