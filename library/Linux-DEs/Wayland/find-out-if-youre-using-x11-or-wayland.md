---
title: "Find out if you're using X11 or Wayland"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

# Output

Yes, there are a few simple ways to check whether you're currently using Wayland or X11:

### 1. **Using `echo $XDG_SESSION_TYPE` (Terminal Method)**
   - Open a terminal and run the following command:
     ```
     echo $XDG_SESSION_TYPE
     ```
   - If the output is `x11`, you're using X11. If it says `wayland`, you're using Wayland.

### 2. **Using `loginctl` (Terminal Method)**
   - You can also use `loginctl` to check your session type:
     ```
     loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type
     ```
   - This command will return `Type=x11` if you're using X11 or `Type=wayland` if you're on Wayland.

### 3. **System Settings in KDE Plasma**
   - In KDE Plasma, you can go to **System Settings** > **About this System** (or **Info Center**) to see information about your display server. It will show whether Wayland or X11 is in use.

These methods will give you a quick answer about which display server protocol you’re currently running.