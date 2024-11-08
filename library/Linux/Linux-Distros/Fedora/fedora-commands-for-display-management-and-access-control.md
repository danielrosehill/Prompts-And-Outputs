---
title: "Fedora commands for display management and access control"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you provide commands for Fedora that would do the following: turn off all connected displays; lock desktop (screensaver); turn on all connected displays

# Output

Since you’re using **KDE Plasma** with **Wayland**, here are some revised commands and workarounds tailored to that setup:

### 1. **Turn Off All Connected Displays**
On Wayland, direct control of displays can be a bit more restrictive compared to X11. Unfortunately, `xset` does not work under Wayland. However, you can use a workaround with **KDE Plasma** tools:

To turn off all connected displays, you can use **KWin's DBus interface**. Here’s how you can do it:

```bash
qdbus org.kde.KWin /KWin org.kde.KWin.setAllOutputsEnabled false
```

This command will turn off all displays. Note that this method relies on KDE's internal control over displays.

### 2. **Lock Desktop (Screensaver)**
To lock your desktop on KDE Plasma under Wayland, you can use the following command:

```bash
qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock
```

This command will lock the current session using KDE's built-in lock mechanism.

### 3. **Turn On All Connected Displays**
To turn the displays back on, you can enable them again using the following command:

```bash
qdbus org.kde.KWin /KWin org.kde.KWin.setAllOutputsEnabled true
```

This should re-enable all displays that were previously turned off.

### Combined Command Sequence
If you want to execute these commands in sequence:

```bash
qdbus org.kde.KWin /KWin org.kde.KWin.setAllOutputsEnabled false && qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock && sleep 5 && qdbus org.kde.KWin /KWin org.kde.KWin.setAllOutputsEnabled true
```

This sequence will:
1. Turn off all connected displays.
2. Lock the desktop.
3. Turn on all connected displays after 5 seconds (you can adjust the sleep duration as needed).

### Additional Notes for Wayland and KDE Plasma:
- **Wayland** restricts direct hardware access for security reasons, which is why some commands that work under X11 (like `xset`) aren't available. The **qdbus** commands are KDE's way of interacting with the desktop environment over **DBus** and are effective in controlling session behavior under **KDE Plasma**.
- You may need **qdbus** installed. If it’s not already available, you can install it with:
  ```bash
  sudo dnf install qt5-qdbus
  ``` 

These commands should help achieve the desired behavior under KDE Plasma with Wayland. Let me know if you need further adjustments or explanations!