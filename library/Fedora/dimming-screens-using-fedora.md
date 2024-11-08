---
title: "Dimming screens using Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm using KDE Plasma on Fedora Linux. I use 3 x AOC E2275SWJ display screens. Are there any tools that would allow me to dim the screen brightness
# Output

Based on your setup of using KDE Plasma on Fedora Linux with 3 external AOC monitors, here are some options to control screen brightness:

1. DDCUtil:
   This command-line tool can control external monitor settings via the DDC/CI protocol. To install on Fedora:

   ```
   sudo dnf install ddcutil
   ```

   Usage example:
   ```
   ddcutil setvcp 10 50  # Set brightness to 50%
   ```

2. DDCCi Plasmoid:
   This is a KDE Plasma widget that provides a GUI for DDCUtil, allowing you to adjust brightness of external monitors directly from your desktop. You can install it from the KDE Store or GitHub:

   https://github.com/davidhi7/ddcci-plasmoid

3. xrandr:
   While not ideal for adjusting actual monitor brightness, xrandr can adjust the gamma and brightness of the video signal:

   ```
   xrandr --output HDMI-1 --brightness 0.7
   ```

   Replace HDMI-1 with your actual output name (find it with `xrandr --query`).

4. Brightness Controller:
   A Python-based GUI application that can adjust brightness on multiple monitors. Install it with:

   ```
   sudo dnf install brightness-controller
   ```

For your AOC monitors, DDCUtil or the DDCCi Plasmoid are likely the best options, as they can control the actual hardware brightness settings of external monitors. These tools should work well with your AOC E2275SWJ displays, assuming they support DDC/CI (which most modern monitors do).

Remember to check if your monitors support DDC/CI and enable it in the monitor's on-screen display menu if necessary. Also, you may need to add your user to the i2c group to use DDCUtil without root privileges:

```
sudo usermod -aG i2c $USER
```

After setting this up, you should be able to control the brightness of your external AOC monitors directly from your KDE Plasma desktop.
# Prompt

Do these work with Wayland?

# Output






## Extracted Prompts
[[Prompts/Dimming screens using Fedora.md#Prompt 1|Prompt 1]]
[[Prompts/Dimming screens using Fedora.md#Prompt 2|Prompt 2]]
