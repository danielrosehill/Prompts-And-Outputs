---
title: "Open and lock ChatGPT and Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can write a script to both **open** the apps (if they are not running), **resize** them to the dimensions you want (each taking 50% of the screen), and **lock them** into position so they don’t move.

Here’s how you can achieve this in two steps:

---

### Step 1: Open and Resize the Windows

You can create a bash script that:

- **Opens** the apps (ChatGPT and Obsidian) if they aren’t already running.
- **Resizes** and positions them, so they take up 50% of the screen.

### Sample Script:

```bash
#!/bin/bash

# Open ChatGPT (replace with the correct command to launch ChatGPT)
if ! pgrep -x "ChatGPT" > /dev/null
then
    # Assuming the command to launch ChatGPT is 'chatgpt'
    chatgpt &
    sleep 2 # Give the app a couple of seconds to start
fi

# Open Obsidian
if ! pgrep -x "Obsidian" > /dev/null
then
    # Assuming the command to launch Obsidian is 'obsidian'
    obsidian &
    sleep 2 # Give the app a couple of seconds to start
fi

# Use wmctrl to get window IDs of ChatGPT and Obsidian
CHATGPT_WIN_ID=$(wmctrl -l | grep "ChatGPT" | awk '{print $1}')
OBSIDIAN_WIN_ID=$(wmctrl -l | grep "Obsidian" | awk '{print $1}')

# Resize and move ChatGPT to left half (50% of screen width, full height)
wmctrl -i -r $CHATGPT_WIN_ID -e 0,0,0,960,1080

# Resize and move Obsidian to right half (50% of screen width, full height)
wmctrl -i -r $OBSIDIAN_WIN_ID -e 0,960,0,960,1080
```

### Step 2: Lock the Windows in Place

You can use **KWin rules** to **lock windows in place** after positioning them. KWin allows you to set window rules that enforce size, position, and other behavior.

1. Open the **KDE System Settings**.
2. Navigate to **Window Management** > **Window Rules**.
3. Click **Add New...** to create a new rule.

Here’s what you’ll do:
- **Identify Windows**: Set window class or window title to identify ChatGPT and Obsidian.
- **Set Specific Rules**:
  - **Size**: Enforce size by checking the box for "Size" and setting it to the dimensions (e.g., 960x1080).
  - **Position**: Enforce window position by checking the "Position" box and setting it to the appropriate coordinates (e.g., `x=0, y=0` for ChatGPT, and `x=960, y=0` for Obsidian).
  - **Prevent Moving/Resizing**: You can configure additional rules to **prevent** the windows from being moved or resized.

These rules will be automatically applied whenever the windows are open.

### Automating the Process:
Now, you can save the bash script to your preferred location and create a desktop launcher or set it up to run whenever you start your session.

---

### Additional Locking via KWin Scripting:
If you want a more programmatic solution to "locking" the windows in place, you can write a **KWin script**.

1. Open **KDE System Settings** > **Window Management** > **KWin Scripts**.
2. Click **Get New Scripts** to see available scripts for managing window behavior.
3. Alternatively, you can write a custom KWin script in **JavaScript** that locks the dimensions and positions.

Example to "lock" the windows via KWin script:
```javascript
// KWin Script to lock window positions and sizes

var chatGptWin = workspace.clientList().find(client => client.caption.includes("ChatGPT"));
var obsidianWin = workspace.clientList().find(client => client.caption.includes("Obsidian"));

if (chatGptWin) {
    chatGptWin.geometry = {x: 0, y: 0, width: 960, height: 1080};
}

if (obsidianWin) {
    obsidianWin.geometry = {x: 960, y: 0, width: 960, height: 1080};
}
```

### Conclusion:
- The bash script will **open, position, and resize** the windows to take up exactly 50% of the screen.
- Using **KWin rules** (GUI method) or **KWin scripts** (programmatic method), you can lock the windows to prevent further moving or resizing.

This setup will provide a consistent, structured window layout each time you start your session, and the windows will stay in place!