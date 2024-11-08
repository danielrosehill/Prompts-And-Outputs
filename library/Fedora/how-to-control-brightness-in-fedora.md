---
title: "How to control brightness in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You are using an AMD Radeon RX 7700 XT GPU, and Fedora Workstation 40 with KDE Plasma as your desktop environment. Here's how you can attempt to control the display brightness using either KWin or the GPU driver:

### Controlling Brightness with KWin (Wayland)
KWin, the Wayland compositor used by KDE Plasma, allows direct control over display settings. For brightness, you might have less direct access compared to X11, but you can try the following:

1. **Adjusting Gamma in KWin**:
   While brightness control is not always directly exposed, you can modify the gamma settings to affect the perceived brightness. Run this command in your terminal:

   ```bash
   kwriteconfig5 --file kwinrc --group NightColor --key Active true
   kwriteconfig5 --file kwinrc --group NightColor --key Mode 1
   qdbus org.kde.KWin /KWin reconfigure
   ```

   This would enable KDE's night color feature, which adjusts the screen color temperature, indirectly reducing brightness. You can further tweak the configuration in the KDE System Settings under **Display and Monitor > Night Color**.

### Controlling Brightness with the AMD GPU Driver

The AMD GPU driver for Linux provides more direct control over the GPU and display. Here's how you can try to control brightness through the GPU:

1. **AMDGPU Driver**:
   If you're using the `amdgpu` driver (which is standard on modern AMD GPUs like your RX 7700 XT), you can try using `xrandr` (if on X11) or some low-level tools for Wayland.

   - For X11 (via `xrandr`):
     You can adjust brightness using the `xrandr` tool. First, check your display's name by running:
     ```bash
     xrandr --verbose
     ```
     Then, set the brightness (replace `DISPLAY_NAME` with your display name):
     ```bash
     xrandr --output DISPLAY_NAME --brightness 0.7
     ```
     The value `0.7` represents 70% brightness. Adjust as necessary.

2. **`ddcutil` for DDC/CI Control**:
   Many modern monitors support the DDC/CI protocol, which allows brightness control directly through the monitor:
   - Install `ddcutil`:
     ```bash
     sudo dnf install ddcutil
     ```
   - Use `ddcutil` to check if your monitor supports brightness control:
     ```bash
     ddcutil capabilities
     ```
   - To adjust brightness:
     ```bash
     ddcutil setvcp 10 70
     ```
     `10` is the VCP (Virtual Control Panel) code for brightness, and `70` is the brightness percentage.

If you're using Wayland and `xrandr` is unavailable, you can fall back to the `ddcutil` method to control the brightness directly on your monitors.

Let me know if you'd like more specific instructions or if you encounter any issues!