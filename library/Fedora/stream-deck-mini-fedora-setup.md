---
title: "Stream Deck mini Fedora setup"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you provide a setup guide for getting the Elegato Stream Deck Mini working on Fedora

# Output

While the search results don't specifically cover Fedora, I can provide a guide for setting up the Elgato Stream Deck Mini on Fedora based on the information available and my knowledge of Fedora systems. Here's a step-by-step guide:

## Setting Up Elgato Stream Deck Mini on Fedora

1. Install Dependencies:
   Open a terminal and run:
   ```
   sudo dnf install python3-pip hidapi libxcb
   ```

2. Set Up udev Rules:
   Create a new udev rules file:
   ```
   sudo nano /etc/udev/rules.d/70-streamdeck.rules
   ```
   
   Paste the following content:
   ```
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0060", TAG+="uaccess"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0063", TAG+="uaccess"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006c", TAG+="uaccess"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006d", TAG+="uaccess"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0080", TAG+="uaccess"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0084", TAG+="uaccess"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="008f", TAG+="uaccess"
   ```

   Save and exit the editor.

3. Reload udev Rules:
   ```
   sudo udevadm control --reload-rules
   ```

4. Install streamdeck-ui:
   ```
   pip3 install --user streamdeck_ui
   ```

5. Add Local bin to PATH:
   Edit your ~/.bashrc file:
   ```
   nano ~/.bashrc
   ```
   
   Add this line at the end:
   ```
   export PATH=$PATH:$HOME/.local/bin
   ```
   
   Save, exit, and reload the bashrc:
   ```
   source ~/.bashrc
   ```

6. Launch streamdeck-ui:
   ```
   streamdeck &
   ```

7. Set Up Auto-start:
   Create a .desktop file:
   ```
   mkdir -p ~/.config/autostart
   nano ~/.config/autostart/streamdeck.desktop
   ```
   
   Add the following content:
   ```
   [Desktop Entry]
   Type=Application
   Name=StreamDeck
   Exec=streamdeck
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   ```

   Save and exit.

8. Install xdotool (for window management):
   ```
   sudo dnf install xdotool
   ```

## Configuring Your Stream Deck

1. Use the streamdeck-ui interface to set up buttons.
2. For commands, use the "Command" field.
3. For shortcuts, use the "Press Keys" field.
4. For window switching, use xdotool commands like:
   ```
   xdotool search --desktop 0 --class Firefox windowactivate
   ```

## Tips for Fedora Users

1. Fedora uses DNF instead of APT, so package installation commands differ from Ubuntu.
2. Fedora might have different default applications, so adjust your commands accordingly.
3. If you encounter permission issues, ensure your user is in the correct groups (usually "input" and "users").

By following these steps, you should be able to set up and use your Elgato Stream Deck Mini on Fedora. Remember to unplug and replug your Stream Deck after setting up the udev rules. If you encounter any issues, check the system logs or run the streamdeck-ui from the terminal to see any error messages.

 