---
title: Gamma control on KDE Plasma
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You are asking about controlling the gamma settings while using **KDE Plasma on Wayland**, which can be useful to adjust brightness and contrast for comfort, especially if you are sensitive to screen brightness.

Unfortunately, as of now, Wayland does not natively support gamma adjustment in the same way that X11 does via `xrandr`. However, there are a few workarounds and potential upcoming features:

### 1. **KDE Plasma Display Settings (Night Color)**:
While gamma adjustment isn't directly supported, you can still use **Night Color** in KDE Plasma to reduce the blue light and change the color temperature, which may give a softer appearance similar to gamma reduction.
- Go to **System Settings** → **Display and Monitor** → **Night Color**.
- Enable **Night Color** and adjust the slider to make the screen warmer and less intense, which can be helpful for sensory overload.

### 2. **Wayland Gamma Support (Future Potential)**:
Gamma control via Wayland is still being developed. Some compositors are working on adding direct gamma control, but KDE Plasma does not have this feature yet. You might see it in future updates as the Wayland protocol evolves.

### 3. **Use Software Tools**:
For more control over display brightness and visual appearance, you can still use software-based tools to reduce brightness and adjust color settings:
   
- **Redshift**: While it cannot adjust gamma directly on Wayland, Redshift can still help reduce blue light and adjust brightness to mimic gamma changes.
   - Install Redshift and set the color temperature and brightness reduction:
     ```
     sudo dnf install redshift
     redshift -O 3000K -b 0.8
     ```

### 4. **Brightness Control Tools**:
Tools like **Brightness Controller** work on Wayland and can reduce brightness or adjust other display parameters via software:
   - Install on Fedora:
     ```
     sudo dnf install brightness-controller
     ```

### 5. **Monitors with Gamma Settings**:
If gamma control is essential and Wayland/KDE doesn't provide the necessary controls, consider using your monitor’s hardware controls. Many modern monitors offer manual gamma adjustment via the on-screen display (OSD) menu.

In summary, while direct gamma control on KDE Plasma Wayland isn't fully supported yet, you can use **Night Color** for some relief, and software tools like **Redshift** and **Brightness Controller** to achieve similar effects. Let me know if you'd like more help with any of these setups!