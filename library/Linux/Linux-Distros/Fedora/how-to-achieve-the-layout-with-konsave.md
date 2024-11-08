---
title: "How to achieve the layout with konsave"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Got it, you want the split-screen layout for Google Chrome and Obsidian on the left-most monitor (labelled as **2275W B63GCQA006616**) in your three-monitor setup. Let's adjust the earlier instructions to ensure that the split layout appears on this specific screen.

Here's how you can do it using `konsave` while ensuring that the applications are always launched and split on the left screen:

### Step 1: Arrange the Windows on the Left Monitor
First, manually set up your windows on the left-most screen:

1. **Open Google Chrome and Obsidian:**
   - Launch Google Chrome using the command you provided.
   - Launch Obsidian with your specified vault.
   
2. **Place Windows on the Left Monitor:**
   - Move both Google Chrome and Obsidian to the left-most monitor (`2275W B63GCQA006616`).
   - Snap **Google Chrome** to the left half and **Obsidian** to the right half of the left monitor.
   - Ensure both windows are positioned and sized to cover the desired halves of the screen.

### Step 2: Save the Layout with `konsave`
Once the windows are positioned correctly on the left monitor:

1. **Open a Terminal** and run the following command to save your current desktop layout:

   ```bash
   konsave -s my_left_screen_split
   ```

   - This will save a profile named `my_left_screen_split` which includes the positioning of Chrome and Obsidian on the left monitor.

2. **List Saved Profiles to Confirm:**

   ```bash
   konsave -l
   ```

   You should see `my_left_screen_split` listed.

### Step 3: Apply the Saved Layout
1. **Launch Both Applications First:**
   - You can use a script to launch Chrome and Obsidian:

   ```bash
   /opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx &
   obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub &
   ```

2. **Apply the Layout Using `konsave`:**

   Once both applications are launched, apply the saved layout to place them in the correct split configuration on the left monitor:

   ```bash
   konsave -a my_left_screen_split
   ```

### Step 4: Automate the Whole Process
To make launching and applying the layout easier, you can create a script that does everything for you.

1. **Create a Shell Script:**

   ```bash
   nano ~/launch_left_split.sh
   ```

2. **Add the Following Content to the File:**

   ```bash
   #!/bin/bash

   # Launch Chrome
   /opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx &

   # Launch Obsidian
   obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub &

   # Wait for applications to load
   sleep 5

   # Apply the konsave profile to arrange the layout
   konsave -a my_left_screen_split
   ```

3. **Make the Script Executable:**

   ```bash
   chmod +x ~/launch_left_split.sh
   ```

### Step 5: Create a Shortcut for Convenience
You can set up a keyboard shortcut to run the script for even quicker access:

1. **Open System Settings** -> **Shortcuts** -> **Custom Shortcuts**.

2. **Add a New Global Shortcut:**
   - **Edit** -> **New** -> **Global Shortcut** -> **Command/URL**.
   - **Name:** `Launch Split Layout on Left Monitor`.
   - **Trigger:** Assign a key combination of your choice.
   - **Action:** Set the path to the script:

     ```bash
     /home/daniel/launch_left_split.sh
     ```

### Summary
- **Set Up Manually:** Open Chrome and Obsidian, arrange them in split view on the left monitor.
- **Save Layout with `konsave`:** Save it as `my_left_screen_split`.
- **Automate with Script:** Create a script that launches both apps and applies the saved layout.
- **Assign a Shortcut:** Use KDE's custom shortcuts to make launching your setup even easier.

This way, you can easily restore your split layout on the specific monitor you desire with just a key press or by running the script!