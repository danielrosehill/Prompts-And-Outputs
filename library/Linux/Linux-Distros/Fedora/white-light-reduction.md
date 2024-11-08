---
title: "White light reduction"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are tools for Linux that can apply a similar effect to **Dark Reader**, but at the desktop level, reducing the intensity of pure white and making the entire desktop environment easier on the eyes. These tools act by overlaying or filtering the display, making it softer and reducing brightness. Here are some options:

### 1. **SafeEyes** (with Blue Light Filter)
   - **SafeEyes** is primarily a tool to reduce eye strain by enforcing breaks during long sessions, but it also has a **blue light filter** feature, which dims the screen and applies a softer color filter.
   - While it doesn’t directly replace white with another color, it can make the screen much more comfortable by reducing overall brightness and intensity.
   - Install on Fedora:
     ```bash
     sudo dnf install safeeyes
     ```
   - Configure the blue light filter and intensity settings within the tool's preferences.

### 2. **Redshift** (For Desktop)
   - **Redshift** is commonly used for reducing blue light and adjusting screen warmth, but it can also serve as a general dimming tool that makes whites less harsh.
   - It applies a warmer color temperature to the whole display, similar to what **Dark Reader** does for web pages, but at the desktop level.
   - Run Redshift with a custom color temperature and brightness:
     ```bash
     redshift -O 3000K -b 0.8
     ```
   - This reduces brightness and applies a warmer tone, making pure white much less intense.

### 3. **Xcalib** (For X11)
   - **Xcalib** is a tool that allows you to change the contrast, brightness, and gamma of your entire display in an **X11** environment, helping to soften white colors across the desktop.
   - Install via:
     ```bash
     sudo dnf install xcalib
     ```
   - Use the following command to adjust the contrast and reduce the intensity of bright whites:
     ```bash
     xcalib -co 80 -a
     ```
   - This reduces the contrast by 20%, giving the screen a softer and dimmer feel, especially for white backgrounds.

### 4. **Gamma Correction via `xrandr`**
   - **Xrandr** can be used to adjust the gamma settings on X11, reducing the brightness and intensity of the display and softening pure white.
   - To reduce the gamma for a softer look:
     ```bash
     xrandr --output <display_name> --gamma 0.8:0.8:0.8
     ```
   - This dims the white and adjusts the color output to a less intense configuration.

### 5. **Window Managers or Desktop Environments with Dark Themes**
   - Many modern **Linux desktop environments** such as **GNOME**, **KDE Plasma**, and **XFCE** come with **dark themes** that can be applied globally. These dark themes reduce the amount of white by default and use shades of gray or black instead. While not exactly an overlay, this is the easiest way to achieve a desktop-wide dark appearance.
   - For **KDE Plasma**:
     - Go to **System Settings** → **Appearance** → **Global Themes** and select a dark theme like **Breeze Dark**.
   - For **GNOME**:
     - Go to **Settings** → **Appearance** and choose a **Dark** theme.

### 6. **Iris** (Cross-platform, for Advanced Filtering)
   - **Iris** is a cross-platform application designed to adjust the color temperature, reduce blue light, and lower the brightness of the entire display. It allows you to adjust these settings to filter out bright whites and make the screen more comfortable.
   - Iris allows more customization compared to Redshift, and you can adjust the warmth and intensity dynamically.
   - You can download **Iris** from their official website, and it works well on most Linux distributions.

### 7. **Dimmer**
   - **Dimmer** is a simple tool that applies an overlay on top of your desktop, reducing the overall brightness and intensity, including reducing pure white areas.
   - It doesn’t change the color temperature but can be useful to reduce brightness globally when your display is too bright, especially for sensitive users.
   - Install on Fedora:
     ```bash
     sudo dnf install dimmer
     ```
   - You can adjust the level of dimming directly through the app.

### 8. **KDE Plasma Night Color / GNOME Night Light**
   - If you're using **KDE Plasma** or **GNOME**, both desktops have built-in **Night Mode** or **Night Light** options, which adjust the color temperature of the display to reduce blue light and brightness.
   - This option is great for reducing harshness from white backgrounds.
   - **KDE Plasma**:
     - Go to **System Settings** → **Display and Monitor** → **Night Color**.
     - Adjust the temperature and schedule it to stay on throughout the day.
   - **GNOME**:
     - Go to **Settings** → **Displays** → **Night Light**.

### Summary of Options:
- **Redshift** and **Iris**: These are great for applying desktop-wide color temperature adjustments to make pure white less intense.
- **Xcalib** and **xrandr**: These tools can reduce contrast and brightness at the system level, making the entire display softer.
- **Dimmer** and **SafeEyes**: These tools apply overlays to dim the display further, reducing brightness, including white areas.
- **KDE Plasma Night Color / GNOME Night Light**: Integrated options to reduce blue light and brightness across the desktop.

If you're looking for a true desktop-wide overlay similar to **Dark Reader**, **Iris** or **Redshift** combined with dark themes and gamma adjustments will likely be the best approach for reducing white light across the entire Linux desktop. Let me know if you need further assistance with setup or installation!