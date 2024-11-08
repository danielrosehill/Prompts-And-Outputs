---
title: "Check if Sway is properly configured"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To verify that Sway is properly configured and set up to boot into, you can follow these steps:

### 1. **Check if Sway is Installed**
Ensure Sway is installed on your system by running:
```bash
sway --version
```
If Sway is correctly installed, this command will show the installed version. If it’s not installed, you’ll need to install it via your package manager:
- **Fedora**: `sudo dnf install sway`
- **Debian/Ubuntu**: `sudo apt install sway`
- **Arch**: `sudo pacman -S sway`

### 2. **Verify Configuration Files**
The default configuration file for Sway is located at:
```
~/.config/sway/config
```
Make sure this file exists and is properly configured. You can check if it's there by running:
```bash
ls ~/.config/sway/config
```
If the file does not exist, you can copy the default configuration:
```bash
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/
```
You can then edit the configuration file to customize it if needed.

### 3. **Test Sway Without Logging Out**
If you’re currently in another desktop environment (like KDE Plasma) and want to test Sway without logging out, you can switch to a TTY (press `Ctrl + Alt + F2`) and log in. Then, run:
```bash
sway
```
This will start a Sway session directly. If everything is correctly configured, Sway should launch without issues. Press `Ctrl + Alt + F1` to switch back to your original session.

### 4. **Check Display Manager (if Using One)**
If you intend to boot directly into Sway, ensure your Display Manager (like SDDM, GDM, or LightDM) is configured to list Sway as a session option. You can check this by logging out and seeing if Sway appears as a session you can select.

To add Sway as a session option, you might need to create a `.desktop` file:
1. Create a new file:
   ```
   sudo nano /usr/share/wayland-sessions/sway.desktop
   ```
2. Add the following content:
   ```ini
   [Desktop Entry]
   Name=Sway
   Comment=An i3-compatible Wayland compositor
   Exec=sway
   Type=Application
   DesktopNames=Sway
   ```
3. Save and exit.

### 5. **Verify Wayland Support**
Make sure your system supports Wayland by checking if Wayland libraries are installed:
```bash
echo $XDG_SESSION_TYPE
```
If it returns `wayland`, your current session is running on Wayland. If it's `x11`, Sway might still work, but you are currently using Xorg.

### 6. **Check Logs for Errors**
If you’ve attempted to start Sway and encountered issues, you can check logs to troubleshoot:
```bash
journalctl -xe | grep sway
```
This can help you identify any configuration errors or missing dependencies.

### 7. **Set Sway as Default for Boot**
If you want to set Sway as the default environment when you boot, make sure to:
- Select it manually in your Display Manager, or
- If not using a Display Manager, add `exec sway` to your `.bash_profile` or `.bashrc`, though this will auto-start Sway for every terminal login (usually better to manage through `~/.xinitrc` or `~/.profile`).

By following these steps, you should be able to verify and ensure that Sway is configured properly and ready to boot into.