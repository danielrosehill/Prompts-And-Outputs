---
title: "Ways to control brightness on fedora 40"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I use fedora workstation 40 (with kde plasma + wayland). I'm trying to find a way to control the brightness of my 3 x displays. I've had difficulties with ddcutil. Can you suggset all the approaches that might work. I'd like to be able to adjust the brightness of the 3 displays at once with a simple slider interface if possible

# Output

Controlling the brightness of multiple external displays simultaneously on Fedora Workstation 40 with KDE Plasma and Wayland can be tricky, especially with issues related to DDC/CI and tools like `ddcutil`. Here are some alternative approaches and tools you can try to achieve the control you’re looking for:

### 1. **KScreen**
KScreen, KDE’s monitor configuration utility, can be extended with scripts to manage brightness, but unfortunately, it doesn’t natively support brightness control for external monitors through DDC/CI. However, you could script adjustments for internal displays if needed.

### 2. **Custom DDC/CI via Command Line**
If `ddcutil` has issues, it might be related to driver or Wayland support. You could try running `ddcutil` in conjunction with specific tweaks:
- Make sure your user is in the `i2c` group: `sudo usermod -aG i2c your-username`
- Test running `ddcutil` as root to see if permissions are causing issues.
- Try using `ddcutil` with XWayland (run a session using X11 instead of Wayland), as some DDC tools don’t work well in native Wayland environments.

### 3. **ddcci-driver-linux**
If `ddcutil` doesn’t work directly, try using **ddcci-driver-linux**, a kernel module that helps manage DDC/CI via backlight devices:
   - Install and load the module: `sudo modprobe ddcci_backlight`
   - You may then be able to control brightness using KDE’s built-in brightness tools or other system tools by exposing displays as backlight devices.

   You can find more about this [ddcci-driver](https://github.com/udevbe/ddcci-driver-linux).

### 4. **Wayland-Specific Tools**
Wayland has more restricted access to hardware compared to X11. However, some tools may still work with Wayland:
- **Wlr-randr**: It’s a simple command-line tool for changing display properties like brightness. You can try using this on Wayland if DDC tools don’t work well.
   - Install: `sudo dnf install wlroots`
   - Use it to control displays via command line scripts, though not all monitors may support brightness control in this manner.

### 5. **ClickMonitorDDC (Alternative GUI)**
ClickMonitorDDC is a GUI tool primarily for Windows, but it works well with Wine on Linux for DDC/CI control. You can try installing it via Wine on Fedora and see if it can control all three monitors’ brightness:
   - Install Wine: `sudo dnf install wine`
   - Download and run **ClickMonitorDDC** from Wine.

### 6. **KDE Custom Script via Slider in Panel**
A workaround solution is to create a custom slider on the KDE panel linked to a script that adjusts brightness using `ddcutil` (if you can get it working) or another command-line tool.
   - You can use a **KDE Plasma applet** for sliders.
   - Write a simple shell script to loop through the displays and adjust brightness:
   
```bash
#!/bin/bash
# Adjust brightness for all three displays
ddcutil setvcp 10 50 --display 1
ddcutil setvcp 10 50 --display 2
ddcutil setvcp 10 50 --display 3
```

### 7. **X11 Session (as a Backup Plan)**
If none of the Wayland-specific tools work, switching to an **X11 session** may resolve the issue. DDC/CI tools like `ddcutil` are more reliable in X11 environments. You can easily switch to an X11 session from your login screen if KDE allows you to.

### 8. **Light Command Line Utility**
Another alternative for internal displays is the `light` utility, which might help if you mix internal and external displays. While it may not control all monitors, it works well with internal displays.
   - Install: `sudo dnf install light`
   - Usage example: `light -S 50` (Sets brightness to 50%).

Unfortunately, with Wayland’s limitations, DDC/CI support can be hit or miss. Trying these approaches can help you find the best solution for controlling the brightness of multiple displays simultaneously.

Let me know if you'd like specific details on setting up any of these!