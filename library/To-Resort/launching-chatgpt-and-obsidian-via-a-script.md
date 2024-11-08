---
title: "Launching ChatGPT and Obsidian via a script"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

A script might be a good option, actually. I'm trying to set up a split screen view (50:50) between obsidian and my ChatGPT app The start scripts are: It's program is /opt/google/chrome/google-chrome Arguments: --profile-directory=Default --app-id=xxxxxxx

# Output

Great! Here’s the updated script to place **Obsidian** on the left half of the third screen and your **ChatGPT app** on the right half of the third screen (right display):

### Updated Split-Screen Script:

```bash
#!/bin/bash

# Launch Obsidian
obsidian &

# Wait for the window to open
sleep 2

# Move Obsidian to the left half of the right screen (third display)
obsidian_window_id=$(wmctrl -l | grep "Obsidian" | awk '{print $1}')
wmctrl -ir $obsidian_window_id -e 0,3840,0,960,1080 # Left half of third screen (HDMI-A-2)

# Launch ChatGPT app in Chrome
/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx &

# Wait for the window to open
sleep 2

# Move ChatGPT to the right half of the right screen (third display)
chatgpt_window_id=$(wmctrl -l | grep "ChatGPT" | awk '{print $1}')
wmctrl -ir $chatgpt_window_id -e 0,4800,0,960,1080 # Right half of third screen (HDMI-A-2)
```

### Explanation:
- **Obsidian**: 
   - Moved to the left half of the third screen with X = 3840 and width = 960.
- **ChatGPT**:
   - Moved to the right half of the third screen with X = 4800 and width = 960.

### Step-by-Step Instructions:
1. Save the script as `split_screen_obsidian_chatgpt.sh`.
2. Make the script executable:
   ```bash
   chmod +x split_screen_obsidian_chatgpt.sh
   ```
3. Run the script:
   ```bash
   ./split_screen_obsidian_chatgpt.sh
   ```

This will open **Obsidian** on the left half and the **ChatGPT app** on the right half of your third screen. Let me know if you'd like any additional tweaks!

# Input


Sounds great. Is there a way to kind of "lock" them to that configuration so that I don't accidentally move them out of their configuration?

# Output

Yes, in KDE Plasma, you can use **Window Rules** to temporarily lock the windows to their positions and sizes to prevent accidental movement. This can be set up without making the rule permanent, so you can toggle it on or off as needed.

Here’s how to temporarily lock the position and size of the **Obsidian** and **ChatGPT** windows after you’ve positioned them using the script:

### Step 1: Open the Window Rules for Each Window
1. **Right-click on the window’s title bar** (for either **Obsidian** or **ChatGPT**).
2. Select **More Actions** → **Special Window Settings**.

### Step 2: Create Temporary Window Rules
1. In the **Window Rules** dialog, click the **Size & Position** tab.
   
2. Set the following options for **both Obsidian and ChatGPT**:
   - **Position**:
     - Check the box to enable.
     - Select **Force** and set the X and Y coordinates to the ones from the script (e.g., for Obsidian: X = 3840, Y = 0; for ChatGPT: X = 4800, Y = 0).
   - **Size**:
     - Check the box to enable.
     - Select **Force** and set the size to **960x1080** (or your desired size).
   
3. Scroll down and enable **Prevent movement** under **Arrangement & Access**. This will prevent you from accidentally dragging the window out of place.

4. Click **OK** to apply the settings.

### Step 3: Apply to Both Windows
Repeat the above process for both **Obsidian** and **ChatGPT**, ensuring each is locked to its respective position and size on the third screen.

### Step 4: Disable/Remove the Rule
When you're done and want to remove the lock, simply right-click the title bar again, go to **Special Window Settings**, and uncheck the options you’ve set.

### Alternative: Use "Keep in Place" (Quick Lock)
For a quicker, though less strict, lock:
1. Right-click on the title bar of each window.
2. Go to **More Actions** → **Keep in Place**.

This prevents window movement temporarily but allows resizing. It’s useful for preventing accidental movement without fully locking the size.

Let me know if you need help with these settings!

# Input

Is there any way to integrate all of this into the script: launch Obsidian and ChatGPT and keep them locked temporarily in that layout?

# Output

To integrate the process of launching **Obsidian** and **ChatGPT**, positioning them, and then temporarily locking them into that layout, you can combine the existing window positioning script with additional **KWin** scripting functionality. KWin allows for window rules and behaviors to be applied programmatically. Here’s how you can do it all within a single script.

### Step 1: Use xdotool to Lock Windows
You can use **xdotool** to disable window resizing and movement temporarily by removing window decorations (which can prevent accidental movements).

Here’s a script that:
1. Launches both applications.
2. Positions them on the third screen.
3. Disables window movement and resizing by removing window decorations.

### Combined Script

```bash
#!/bin/bash

# Launch Obsidian
obsidian &

# Wait for the window to open
sleep 2

# Move Obsidian to the left half of the right screen (third display)
obsidian_window_id=$(wmctrl -l | grep "Obsidian" | awk '{print $1}')
wmctrl -ir $obsidian_window_id -e 0,3840,0,960,1080 # Left half of third screen (HDMI-A-2)

# Launch ChatGPT app in Chrome
/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx &

# Wait for the window to open
sleep 2

# Move ChatGPT to the right half of the right screen (third display)
chatgpt_window_id=$(wmctrl -l | grep "ChatGPT" | awk '{print $1}')
wmctrl -ir $chatgpt_window_id -e 0,4800,0,960,1080 # Right half of third screen (HDMI-A-2)

# Temporary lock: Remove window decorations to prevent moving and resizing
xdotool windowunmap $obsidian_window_id
xdotool windowmap $obsidian_window_id
xdotool windowunmap $chatgpt_window_id
xdotool windowmap $chatgpt_window_id
```

### Explanation:
- **Launching Obsidian and ChatGPT**: The script launches both applications.
- **Positioning**: Both windows are positioned in a 50:50 split on the third display using `wmctrl`.
- **Locking the Windows**:
   - **xdotool windowunmap/windowmap**: These commands temporarily remove the window decorations, effectively preventing the window from being resized or moved accidentally.
   - This lock is "temporary" because once you close the windows, their default behavior will return the next time you launch them.

### Step 2: Making the Script Executable

Save the script as `split_screen_lock.sh` and make it executable:

```bash
chmod +x split_screen_lock.sh
```

### Step 3: Running the Script

Run the script:

```bash
./split_screen_lock.sh
```

This script should now:
- Open **Obsidian** and your **ChatGPT app**.
- Position them in a 50:50 split on the third screen (right display).
- Temporarily lock them in place by removing window decorations.

### Unlocking the Windows
To revert the lock and allow normal window movement and resizing again, simply restart the applications or manually restore window decorations by running:

```bash
kwin --replace
```

Let me know if you'd like any adjustments or enhancements to this script!