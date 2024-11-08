---
title: "Fedora shortcut for find more"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To set up a shortcut in **Fedora Linux** that automatically types `"find more"` and then hits return, you'll need to use **AutoKey**, a text automation tool for Linux that allows you to create scripts and assign them to keyboard shortcuts. Here's a step-by-step guide to achieve that:

### Step 1: Install AutoKey
1. Open a terminal.
2. Install AutoKey using the following command:
   ```bash
   sudo dnf install autokey-gtk
   ```
   For KDE, you can use `autokey-qt` instead of `autokey-gtk`.

### Step 2: Launch AutoKey
1. Open **AutoKey** by searching for it in your applications or by typing `autokey-gtk` in the terminal.
2. AutoKey will run in the system tray.

### Step 3: Create a New Script
1. In AutoKey, right-click on **My Phrases** in the left sidebar and choose **New Script**.
2. Name your script (e.g., `"Find More Shortcut"`).

### Step 4: Enter the Script
1. In the main editor window, type the following AutoKey script:
   ```python
   keyboard.send_keys('find more\n')
   ```
   This script will type `find more` and hit the return key (`\n`).

### Step 5: Set a Shortcut Key
1. Under the **Set Shortcut** section, click on **Set** to assign a keyboard shortcut.
2. Press the desired shortcut combination (e.g., `Ctrl + Alt + F`).
3. Click **OK** to save the shortcut.

### Step 6: Save and Test
1. Click **Save** to apply the script.
2. Test the shortcut in any text field or terminal window. Press the keyboard shortcut you assigned, and it should type `"find more"` followed by a return.

This method will automate typing and pressing "return" using a simple script on Fedora Linux.

Let me know if you need help with anything else!


If **AutoKey** isn't working well for your needs, another great option for automating text input and shortcuts on **Fedora Linux** is using **xdotool** in combination with custom keyboard shortcuts. This tool allows you to simulate keyboard input, including typing text and pressing keys like "Enter."

Here’s how you can set up a shortcut to type `"find more"` and hit return using **xdotool**:

### Step 1: Install xdotool
1. Open a terminal and install xdotool by running:
   ```bash
   sudo dnf install xdotool
   ```

### Step 2: Create a Script to Type "find more" and Press Return
1. In your home directory, create a simple script that uses xdotool to type `"find more"` and hit the return key.
   
2. Open a terminal and create a new script file:
   ```bash
   nano ~/find_more.sh
   ```

3. Add the following content to the script:
   ```bash
   #!/bin/bash
   xdotool type "find more"
   xdotool key Return
   ```

4. Save the file by pressing `Ctrl + O`, then press `Enter`, and exit with `Ctrl + X`.

### Step 3: Make the Script Executable
1. To make the script executable, run the following command:
   ```bash
   chmod +x ~/find_more.sh
   ```

### Step 4: Set Up a Keyboard Shortcut
Now that you have the script, you can set up a custom keyboard shortcut in Fedora to run this script.

1. Open **Settings** and navigate to **Keyboard**.
2. Scroll down to the bottom and click **+** to add a custom shortcut.
3. In the **Name** field, type something like `"Find More Shortcut"`.
4. In the **Command** field, enter the full path to the script:
   ```bash
   /home/your-username/find_more.sh
   ```
5. Click **Set Shortcut**, then press the key combination you want to use (e.g., `Ctrl + Alt + F`).

### Step 5: Test the Shortcut
1. After setting the shortcut, open any text field or terminal and press the key combination you chose. It should type `"find more"` and then hit the return key automatically.

This method uses **xdotool** to simulate typing and pressing keys, and it works well with custom keyboard shortcuts in Fedora. Let me know if you need further assistance!