---
title: "Wayland monitor brightness options"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Your prompt asks for a comprehensive list of tools that might work on **Fedora Linux + Wayland** to control the brightness of displays.

On Fedora with **Wayland**, controlling display brightness can be more challenging compared to X11 due to Wayland's stricter security model. However, there are several tools that may work to adjust screen brightness. Here’s a list of options that could be effective:

### 1. **Brightnessctl**
   - **Description**: A command-line tool to adjust the brightness of your screen or keyboard backlight.
   - **Wayland Support**: Works under Wayland and supports both laptop screens and external displays, as long as they are compatible with hardware backlight control.
   - **Installation**: Available in Fedora’s repositories.
     ```bash
     sudo dnf install brightnessctl
     ```
   - **Usage**: You can adjust the brightness like this:
     ```bash
     brightnessctl set 50%  # Sets brightness to 50%
     ```

### 2. **Gamma Control Tools (Gammastep)**
   - **Description**: Gammastep adjusts the color temperature and brightness of your screen based on the time of day, similar to f.lux. It can also control brightness through gamma correction, though this is not a direct backlight adjustment.
   - **Wayland Support**: Works on Wayland for both brightness and color temperature adjustments.
   - **Installation**: Available via DNF.
     ```bash
     sudo dnf install gammastep
     ```
   - **Usage**: Gammastep will run in the background and adjust brightness automatically.

### 3. **Redshift**
   - **Description**: Redshift adjusts the color temperature of your screen to reduce eye strain. It can be configured to control screen brightness as well, though this is done via gamma, which affects color accuracy.
   - **Wayland Support**: Works on Wayland, but brightness control may not be as reliable as on X11.
   - **Installation**: Available via DNF.
     ```bash
     sudo dnf install redshift
     ```
   - **Usage**: To adjust brightness and color temperature manually:
     ```bash
     redshift -O 3500K -b 0.8  # Set color temperature and brightness
     ```

### 4. **Wlr-randr**
   - **Description**: A Wayland-specific tool that works with the **wlroots** library to adjust display settings, including brightness and gamma for Wayland compositors like Sway or Wayfire.
   - **Wayland Support**: Works natively on Wayland compositors using wlroots.
   - **Installation**: Available in the community repositories.
     ```bash
     sudo dnf install wlr-randr
     ```
   - **Usage**: After installation, use wlr-randr to list displays and adjust brightness:
     ```bash
     wlr-randr --output <display-name> --brightness 0.8
     ```

### 5. **Wayland Compositor Settings**
   - **Description**: Some Wayland compositors (such as **GNOME** or **Sway**) have built-in options for controlling brightness, especially on laptops. These are typically accessible via the **System Settings** or **keyboard shortcuts**.
   - **Wayland Support**: Fully compatible as they are integrated directly into the Wayland compositor.
   - **Usage**: For GNOME, you can adjust brightness in the system tray or **Settings → Power**.

### 6. **ddcutil (for External Monitors)**
   - **Description**: A tool for controlling the settings of external monitors via **DDC/CI**, including brightness. Useful for controlling brightness on external monitors.
   - **Wayland Support**: Works well on Wayland for external monitors, but requires monitors that support DDC/CI.
   - **Installation**: Available in Fedora’s repositories.
     ```bash
     sudo dnf install ddcutil
     ```
   - **Usage**: Detect monitors and adjust brightness:
     ```bash
     ddcutil detect
     ddcutil setvcp 10 50  # Set brightness to 50% (code 10 refers to brightness)
     ```

### 7. **Supergfxctl (for Hybrid Graphics)**
   - **Description**: If you're using a laptop with **hybrid graphics (NVIDIA + Intel/AMD)**, supergfxctl helps manage power modes, which indirectly can influence brightness and display settings.
   - **Wayland Support**: Works with Wayland on Fedora systems with hybrid graphics.
   - **Installation**: Available via DNF for supported hardware.
     ```bash
     sudo dnf install supergfxctl
     ```
   - **Usage**: Adjust graphics modes that affect brightness by managing the graphics setup.

### 8. **Wayland Brightness Slider Extensions (GNOME)**
   - **Description**: On GNOME with Wayland, there are GNOME Shell extensions that add more granular brightness controls to the system tray.
   - **Wayland Support**: These extensions work on Wayland but are specific to GNOME.
   - **Installation**: Available from the GNOME Extensions website or via the GNOME tweak tool.
     - Example extension: [Brightness Control Slider](https://extensions.gnome.org/extension/882/brightness-control/)

### 9. **Xrandr Alternative for Wayland (Wlr-gamma)**:
   - **Description**: **Wlr-gamma** allows gamma adjustments on Wayland, which can influence screen brightness in a similar way to xrandr.
   - **Wayland Support**: Designed for Wayland compositors that use **wlroots** (e.g., Sway).
   - **Installation**: You may need to build it from source, depending on your compositor.
   - **Usage**: Adjust gamma values to control brightness.

### Other Considerations:
- **Direct Backlight Control**: On some laptops, brightness controls are handled at the hardware level and accessible via keyboard shortcuts, which are often supported out of the box on Wayland with Fedora.
  
- **Hardware Compatibility**: Some tools like **brightnessctl** and **ddcutil** rely on the hardware's ability to support certain features like DDC/CI for external monitors, so not all monitors may be adjustable using these tools.

### Conclusion:
While **Wayland** limits some of the traditional tools used on **X11**, there are still a number of solutions for controlling brightness, including **brightnessctl**, **ddcutil**, and **Wayland-specific tools** like **wlr-randr** and **Gammastep**. If you're using **GNOME** or another Wayland compositor, checking their integrated settings is a great starting point.