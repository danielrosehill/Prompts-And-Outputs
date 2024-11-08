---
title: "Obsidian and ChatGPT - another prompt attempt"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm using Obsidian and ChatGPT together in a split screen laytout. On the left, I am running Obsidian. And on the right, I have a Chrome web app running ChatGPT. I run prompts in ChatGPT and then copy them into Obsidian. I'm looking for a way to group ChatGPT and Obsidian into something like a program so that I can launch one application and jump straight to my preferred laytout. I'm using Fedora with KDE Plasma and Wayland, although I'd be open to trying something that worked with X11. Please suggest some ways I could achieve this functionality. 

# Output
**Summary of your prompt:** You are using Obsidian and ChatGPT together in a split-screen layout and would like a way to group them so that you can launch both in your preferred layout as if they were one program. You’re using Fedora with KDE Plasma on Wayland but are open to trying something that works with X11.

Here are some ways you can achieve this functionality without switching environments:

### 1. **KDE Plasma Window Rules & Custom Scripts**
   KDE Plasma allows you to automate window placement using **window rules** combined with a custom startup script to launch both applications together in your preferred layout.

#### Steps:
   - **Set Up Window Rules**:
     1. Open **System Settings** > **Window Management** > **Window Rules**.
     2. Add new rules for **Obsidian** and the **Chrome ChatGPT web app**.
     3. In each rule, configure the following:
        - **Size and position**: Set specific geometry (e.g., Obsidian on the left half, Chrome on the right).
        - **Apply initially**: Enable this to have the rules applied whenever these apps are opened.
   
   - **Create a Startup Script**:
     1. Create a shell script to launch both apps:
        ```bash
        #!/bin/bash
        obsidian &
        sleep 2  # Give time for Obsidian to launch
        google-chrome --app=https://chat.openai.com/ &
        ```
     2. Save this script as `launch_obsidian_chatgpt.sh` and make it executable:
        ```bash
        chmod +x launch_obsidian_chatgpt.sh
        ```

     3. Add this script to KDE's autostart options if you want it to open at login:
        - Go to **System Settings** > **Startup and Shutdown** > **Autostart** and add the script.

   Now, whenever you run this script, Obsidian and the ChatGPT web app will open and snap into your predefined layout.

### 2. **KDE Activities for Workflow Separation**
   KDE Plasma’s **Activities** allow you to separate workflows. You can set up an Activity dedicated to **Obsidian + ChatGPT** and configure it so that when you switch to this Activity, both apps launch and arrange themselves automatically.

#### Steps:
   - Create a new Activity:
     1. Right-click the desktop and select **Configure Desktop and Wallpaper** > **Activities** > **Create New Activity**.
     2. Name the Activity something like "Obsidian + ChatGPT."
   
   - Configure the apps to launch automatically in this Activity:
     1. Go to **System Settings** > **Startup and Shutdown** > **Autostart**.
     2. Add both **Obsidian** and **Chrome ChatGPT** to the Autostart list but configure them to launch only in your new Activity.
     3. Add window rules (as mentioned in the first method) to make sure they open in the correct positions.
   
   Switching to this Activity will automatically arrange the windows, and you can jump into your workflow quickly.

### 3. **Use `krohnkite` (Tiling Script for KDE Plasma)**
   **Krohnkite** is a powerful KWin script that adds tiling features to KDE Plasma, making it behave more like a tiling window manager without leaving KDE.

#### Steps to install and configure:
   1. Open **System Settings** > **Window Management** > **KWin Scripts**.
   2. Click **Get New Scripts**, search for **Krohnkite**, and install it.
   3. Once installed, configure it to always tile **Obsidian** on the left and **Chrome ChatGPT** on the right by opening both apps and manually adjusting their layout once. Krohnkite will remember the layout in future sessions.
   
   **Hotkey Tip**: You can bind a custom keybinding to launch **Obsidian** and **ChatGPT** together, and Krohnkite will handle the tiling for you.

### 4. **Tiling with `wmctrl` and `xdotool` (X11 only)**
   If you're willing to switch to **X11**, you can use tools like **wmctrl** and **xdotool** to launch and place windows exactly where you want them.

#### Steps:
   - **Install wmctrl and xdotool**:
     ```bash
     sudo dnf install wmctrl xdotool
     ```
   
   - **Create a script to launch and position the windows**:
     ```bash
     #!/bin/bash
     obsidian &  # Launch Obsidian
     sleep 2  # Give it time to open
     google-chrome --app=https://chat.openai.com &  # Launch ChatGPT web app
     sleep 2  # Give it time to open

     # Move Obsidian to the left half of the screen
     wmctrl -r "Obsidian" -e 0,0,0,960,1080

     # Move Chrome to the right half of the screen
     wmctrl -r "ChatGPT - Google Chrome" -e 0,960,0,960,1080
     ```

   - Save this script, make it executable (`chmod +x script.sh`), and run it whenever you need both applications positioned correctly.

### 5. **X11 Option: Use `Devilspie2` for Automated Window Placement**
   **Devilspie2** is another tool that works with **X11** to automatically manage window placement, similar to the KDE window rules but with more customization.

#### Steps:
   1. **Install Devilspie2**:
      ```bash
      sudo dnf install devilspie2
      ```

   2. **Configure Devilspie2** for Obsidian and ChatGPT**:
      - Create a configuration file in `~/.config/devilspie2/obsidian_chatgpt.lua`:
        ```lua
        if (get_application_name() == "Obsidian") then
            set_window_workspace(1)
            set_window_geometry(0, 0, 960, 1080)
        end

        if (get_application_name() == "Google Chrome") then
            if (string.match(get_window_name(), "ChatGPT")) then
                set_window_workspace(1)
                set_window_geometry(960, 0, 960, 1080)
            end
        end
        ```

   3. **Run Devilspie2** automatically**:
      - Add `devilspie2` to your autostart applications.
      - Now, when you launch Obsidian and Chrome (ChatGPT), Devilspie2 will place them correctly.

---

### Summary of Options:
- **KDE Plasma’s Window Rules**: Automate window placement with simple rules and scripts.
- **KDE Activities**: Separate your workflow into an "Activity" where both apps open and are laid out automatically.
- **Krohnkite (KDE Script)**: Use tiling features directly within KDE Plasma to always arrange the windows properly.
- **wmctrl + xdotool (X11)**: Launch and arrange windows via a script in an X11 session.
- **Devilspie2 (X11)**: A more advanced tool to automatically position windows in X11.

The **KDE Plasma** options (window rules, activities, or Krohnkite) will work seamlessly on your current Wayland setup. If you are willing to switch to **X11**, `wmctrl`, `xdotool`, or `Devilspie2` can offer additional control.

Let me know which option seems most suitable, and I can help you configure it!