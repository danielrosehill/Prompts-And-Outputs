---
title: "Using X11 rather than Wayland"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is entirely possible to use **X11** instead of **Wayland** with **KDE Plasma**. KDE Plasma supports both **X11** and **Wayland** display servers, and you can easily switch between them. Here’s how you can do it:

### Steps to Switch from Wayland to X11 in KDE Plasma

1. **Logout of Your Current Session**:
   - First, **logout** from your current Wayland session. You can do this from the **KDE Application Menu** by selecting **Log Out**.

2. **Access the Login Screen (SDDM)**:
   - After logging out, you'll be taken to the **login screen**. KDE Plasma uses **SDDM** (Simple Desktop Display Manager) as its default login manager.

3. **Select X11 Session**:
   - On the login screen, look for a **session type menu**. This is usually indicated by a small icon (such as a gear icon) located either near the **password field** or at the **top-right** or **bottom-left** of the screen.
   - Click on this icon, and a list of session types should appear.
   - Select **"Plasma (X11)"** from the list. 

4. **Login**:
   - Enter your password as usual and **log in**. This time, KDE Plasma will launch using the **X11** display server instead of Wayland.

### Making X11 the Default Display Server
If you prefer to use **X11** consistently instead of Wayland, you can configure the system to default to an X11 session:

1. **Ensure Your Preferred Session Is Selected**:
   - The display manager (SDDM) will remember your last session choice. If you select **Plasma (X11)** and log in, it will automatically use **X11** for subsequent logins unless changed.

2. **Check SDDM Configuration** (Optional):
   - If you'd like to explicitly define the default session in the **SDDM configuration file**, you can do so:
     - Open the SDDM configuration file with a text editor (using root privileges):
       ```bash
       sudo nano /etc/sddm.conf
       ```
     - If the file does not exist, you may need to create it or configure it using the KDE System Settings.
     - Add or modify the following lines under the `[General]` section:
       ```
       [General]
       Session=plasma.desktop
       ```
       This configuration ensures that KDE Plasma is used, and typically defaults to **X11** if available.

### Benefits of Switching to X11
- **Compatibility**: X11 has better compatibility with older software and tools that might not yet fully support Wayland. Some software features, like advanced **screen capture**, **display manipulation**, and **input control**, work more reliably under X11.
- **More Mature Toolset**: Many system tools, like `xset`, **X11 forwarding**, or **xrandr**, are specifically designed for X11 and are widely supported.
  
### Drawbacks Compared to Wayland
- **Security**: Wayland offers better security compared to X11, especially regarding **input handling**. In X11, applications can easily interact with each other's windows, which can be a security risk.
- **Performance**: Wayland is designed to offer better **performance**, smoother frame rates, and reduced screen tearing, particularly with newer hardware.

### Switching Back to Wayland
If you wish to switch back to Wayland in the future:
- Log out of your session.
- On the login screen, select **"Plasma (Wayland)"** from the session menu, and then log in.

This way, you have the flexibility to switch between **X11** and **Wayland** depending on your needs and the specific tools you want to use.