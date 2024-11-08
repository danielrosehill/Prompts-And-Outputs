---
title: "Using Obsidian and ChatGPT together - another try"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

This is how I'm using Obsidian and ChatGPT (via a Google Chrome app) in conjunction on Fedora + KDE Plasma. It's an amazing setup. I just need a way to keep this layout "saved" or fixed or .... some way that I can quickly launch this and make sure that it keeps this way. Any suggestions?

![[Using Obsidian and ChatGPT together - another try.png]]

# Output

Creating a desktop wrapper to hold your applications together on a Linux desktop can be achieved in various ways, depending on your needs and technical skills. Below are several methods you could consider to create a "wrapper" for your applications like Obsidian and ChatGPT:

### 1. **Use a Window Manager like i3 or AwesomeWM**
Switching to a tiling window manager (like **i3** or **AwesomeWM**) allows you to manage window layouts more effectively. These window managers automatically tile windows, which can help you keep your applications together without much effort.

- **i3**: You can create workspaces and define rules for where windows open, making it easy to maintain your layout.
- **AwesomeWM**: Allows for extensive customization using Lua scripts, which can be set to position windows in specific layouts.

### 2. **Create a Custom Shell Script**
You can create a shell script that launches your applications and uses `wmctrl` to group them together visually. Additionally, you can use a tool like `devilspie` to ensure that the windows are opened in the correct positions.

#### Example Shell Script
```bash
#!/bin/bash

# Launch Obsidian
obsidian &

# Wait for the window to open
sleep 2

# Move Obsidian to specific position (X=0, Y=0)
obsidian_window_id=$(wmctrl -l | grep "Obsidian" | awk '{print $1}')
wmctrl -ir $obsidian_window_id -e 0,0,0,960,1080

# Launch ChatGPT app in Chrome
/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx &

# Wait for the window to open
sleep 2

# Move ChatGPT to specific position (X=960, Y=0)
chatgpt_window_id=$(wmctrl -l | grep "ChatGPT" | awk '{print $1}')
wmctrl -ir $chatgpt_window_id -e 0,960,0,960,1080
```

### 3. **Use `devilspie` or `devilspie2`**
**Devilspie** is a window matching utility that allows you to define rules for how windows are managed. You can specify rules to always open your apps in a specific position or size.

#### Setting Up Devilspie
1. **Install Devilspie**:
   ```bash
   sudo dnf install devilspie
   ```

2. **Create Configuration Files**:
   Create a directory for your scripts:
   ```bash
   mkdir -p ~/.devilspie
   ```

3. **Example Configuration**:
   Create a file named `obsidian.lua` in `~/.devilspie` with the following content:

   ```lua
   if (get_application_name() == "Obsidian") then
       set_window_position(0, 0)
       set_window_size(960, 1080)
   end
   ```

   And another named `chatgpt.lua`:

   ```lua
   if (get_application_name() == "Google Chrome") then
       set_window_position(960, 0)
       set_window_size(960, 1080)
   end
   ```

4. **Run Devilspie**:
   You can start Devilspie in the background:
   ```bash
   devilspie &
   ```

### 4. **Use a Custom Desktop Environment or Panel**
If you have experience with desktop environments, you can create a custom panel or launcher that groups your applications together and manages their layouts. However, this is significantly more complex and would require deeper programming knowledge.

### 5. **Virtual Desktops or Workspaces**
Use virtual desktops or workspaces to separate different tasks. You could have one workspace dedicated to your workflow with Obsidian and ChatGPT, which you can quickly switch to when needed.

### Conclusion
Creating a wrapper to hold applications together can be accomplished through various means, from using tiling window managers to utilizing scripts with `wmctrl` or `devilspie`. Each method has its pros and cons, so choose the one that best fits your workflow and technical comfort level. If you need more guidance on a specific method, feel free to ask!

# Input

The script idea seems fine but I want something that will kind of group the two windows together and hole them in place unless I close the app. In other words, I'm looking for some way to be able to control these two windows as one if that makes sense. Any ideas?

If you're looking to group the two windows (Obsidian and the ChatGPT Chrome app) together and control them as a single entity while maintaining their layout, you can explore a few methods that simulate this behavior. Here are some ideas:

### 1. **Using a Script with a Window Management Tool**
You can use a combination of `wmctrl` and a shell script to launch and control both windows as if they were a single entity. Here’s a strategy:

- **Launch Both Applications**: Use a script to launch both applications and position them side by side.
- **Use `wmctrl` to Move Them Together**: Whenever you need to move or resize, you can have the script adjust both windows at once.

### Example Script
Here’s a modified version of the script that includes functions to move and resize both windows together. It also includes a basic loop to monitor the application state and reposition them if they’re moved:

```bash
#!/bin/bash

# Function to reposition windows
reposition_windows() {
    obsidian_window_id=$(wmctrl -l | grep "Obsidian" | awk '{print $1}')
    chatgpt_window_id=$(wmctrl -l | grep "ChatGPT" | awk '{print $1}')

    if [ ! -z "$obsidian_window_id" ]; then
        wmctrl -ir $obsidian_window_id -e 0,0,0,960,1080
    fi

    if [ ! -z "$chatgpt_window_id" ]; then
        wmctrl -ir $chatgpt_window_id -e 0,960,0,960,1080
    fi
}

# Launch Obsidian
obsidian &

# Wait for the window to open
sleep 2

# Move Obsidian to specific position (X=0, Y=0)
reposition_windows

# Launch ChatGPT app in Chrome
/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx &

# Wait for the window to open
sleep 2

# Move ChatGPT to specific position (X=960, Y=0)
reposition_windows

# Keep the script running to maintain the layout
while true; do
    reposition_windows
    sleep 1  # Adjust the interval as needed
done
```

### 2. **Using `xbindkeys` for Keyboard Shortcuts**
You can bind the repositioning function to specific keyboard shortcuts using `xbindkeys`, so you can quickly adjust their positions or close both windows at once.

1. **Install xbindkeys** (if you haven't already):
   ```bash
   sudo dnf install xbindkeys
   ```

2. **Create a configuration file**:
   ```bash
   xbindkeys --defaults > ~/.xbindkeysrc
   ```

3. **Edit the configuration file** to include a binding for your repositioning script:

   ```bash
   # Bind to reposition both windows
   "/path/to/your/script.sh"
       Control + Alt + R
   ```

### 3. **Using a Tiling Window Management Script**
Although you mentioned not wanting to install a tiling window manager, you could create a tiling script that resizes and repositions both windows whenever you run it. This wouldn’t fully group them, but it would allow you to adjust their layout easily.

### 4. **Using a Dedicated Tool**
Consider using a dedicated window management tool like **"Window Group"** if available on your system or a similar tool that allows you to group and manage multiple windows together as a single unit.

### Conclusion
The best way to achieve your goal of managing two windows as a single entity while controlling their layout is through a combination of scripting and `wmctrl`. This method allows for flexibility while maintaining control over their positions. Let me know if you would like further adjustments to the script or any additional features!