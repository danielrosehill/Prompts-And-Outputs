---
title: "DDCUTIL tutorial"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

can you give me a tutorial for fedora linux on using ddcutil? How to set it up to reduce monitor brightness? fedora workstation 40, kde plasma, wayland

# Output

Here’s a step-by-step tutorial for using `ddcutil` on **Fedora Workstation 40** with **KDE Plasma on Wayland** to control monitor brightness.

### 1. **Install `ddcutil`**
   First, you need to install `ddcutil`, a command-line tool that allows you to communicate with your monitor's DDC/CI interface to control settings such as brightness.

   Open a terminal and run the following command to install `ddcutil`:

   ```
   sudo dnf install ddcutil
   ```

### 2. **Verify DDC/CI Support**
   After installation, you should verify whether your monitor supports DDC/CI (Display Data Channel/Command Interface), which is necessary for `ddcutil` to work. Run the following command:

   ```
   sudo ddcutil detect
   ```

   This will list all connected displays that support DDC/CI. You should see something like this:

   ```
   Display 1
      I2C bus:             /dev/i2c-6
      EDID synopsis:
         Manufacturer:     DEL
         Model:            DELL U2414H
      VCP version:         2.1
   ```

   If no displays are detected, make sure DDC/CI is enabled in your monitor’s settings. It’s usually found in the monitor’s on-screen display (OSD) menu under options like “DDC/CI Enable/Disable.”

### 3. **Check I2C Permissions**
   You need to ensure that your user has permission to access the I2C bus. Add your user to the `i2c` group:

   ```
   sudo usermod -aG i2c $USER
   ```

   Then, apply the new group membership:

   ```
   newgrp i2c
   ```

   You can also verify that the `/dev/i2c-*` devices are accessible:

   ```
   ls -l /dev/i2c-*
   ```

   If not, you might need to manually set permissions or use `sudo` for `ddcutil` commands.

### 4. **List Monitor Capabilities**
   To check what brightness-related settings are available for your monitor, run:

   ```
   sudo ddcutil getvcp 10
   ```

   This command retrieves the current brightness level of the monitor, which typically corresponds to VCP (Virtual Control Panel) code `10`. You can also use:

   ```
   sudo ddcutil capabilities
   ```

   This will display all supported VCP codes, including brightness control.

### 5. **Set Monitor Brightness**
   You can set the brightness for your monitor using the `setvcp` command. The brightness level usually ranges from 0 to 100.

   For example, to set the brightness to 50% on a specific display:

   ```
   sudo ddcutil setvcp 10 50 --display 1
   ```

   If you have multiple displays, you can specify the display using the `--display` option, as shown. Use `--display 1`, `--display 2`, etc., for different monitors.

   To change the brightness of all monitors at once, you can loop through the displays:

   ```
   for i in {1..3}; do sudo ddcutil setvcp 10 50 --display $i; done
   ```

### 6. **Automating Brightness Adjustment**
   If you find yourself adjusting brightness frequently, you can create a shell script to easily apply your preferred brightness level. For example, create a script called `adjust_brightness.sh`:

   ```bash
   #!/bin/bash
   # Adjust brightness of all connected monitors to 40%
   for i in {1..3}; do
      sudo ddcutil setvcp 10 40 --display $i
   done
   ```

   Make the script executable:

   ```
   chmod +x adjust_brightness.sh
   ```

   You can run the script whenever you need to adjust brightness, or create a **KDE shortcut** for it if you prefer a GUI-based toggle.

### 7. **Dealing with Wayland Restrictions**
   Since you’re using **Wayland**, there can be additional restrictions on how applications can access hardware components like monitors. Running `ddcutil` with `sudo` can often bypass this issue, but if it doesn’t work, you might need to:
   - **Switch to an X11 session**: As Wayland is more restrictive, switching to X11 might solve certain compatibility problems, particularly for DDC/CI tools.
   - **Use XWayland**: Some users have had success running `ddcutil` in an XWayland environment rather than in native Wayland.

### 8. **Using KDE Plasma Custom Shortcuts**
   If you’d like to adjust brightness using a shortcut, you can integrate this script with **KDE Plasma** custom shortcuts:
   - Open **System Settings** > **Shortcuts** > **Custom Shortcuts**.
   - Click **Edit** > **New** > **Global Shortcut** > **Command/URL**.
   - Name your shortcut and point it to the `adjust_brightness.sh` script.
   - Set your desired keyboard combination (e.g., `Ctrl + Alt + B`).

### 9. **Troubleshooting**
   If you're facing difficulties:
   - Ensure your monitor supports DDC/CI and that it’s enabled.
   - Make sure you're running the latest version of `ddcutil` by checking the project’s [GitHub page](https://github.com/rockowitz/ddcutil).
   - Check the permissions for the `/dev/i2c-*` devices and ensure your user is added to the `i2c` group.

---

With these steps, you should be able to use `ddcutil` to control your monitor’s brightness on Fedora Workstation 40. Let me know if you encounter any issues!