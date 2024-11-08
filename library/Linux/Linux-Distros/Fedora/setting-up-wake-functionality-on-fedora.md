---
title: "Setting up wake functionality on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's say that I wanted to configure a specific shortcut or key pair to wake the computer up from sleep on fedora. Is there a way to do that and what would the custom shortcut be

# Output
Unfortunately, waking a computer from **sleep/suspend** is typically controlled at the hardware and BIOS/UEFI level, meaning software shortcuts (like key combinations) generally won’t work while the system is in sleep mode. This is because once the system is suspended, the operating system is no longer active to listen for input from keyboard shortcuts.

However, **wake-on-keyboard** functionality can be enabled at the BIOS and operating system level. This would allow the computer to wake up from a specific key press (e.g., pressing any key on the keyboard or a specific key like the spacebar). Here's how you can configure that on **Fedora**:

### Steps to Enable Wake-on-Keyboard on Fedora:

1. **Enable USB Wake in BIOS/UEFI**:
   - During boot, enter your system's **BIOS/UEFI settings** (usually by pressing `DEL`, `F2`, or a similar key).
   - Find the setting for **USB Wake Support** or **Wake on USB** (it may be under "Power Management" or "Advanced Settings").
   - Ensure this option is **enabled**.

2. **Configure Fedora to Recognize Keyboard for Wake-Up**:
   You can configure Fedora to allow your keyboard to wake up the system from suspend with the following steps:

   - First, check which USB devices are set to wake up the system:
     ```bash
     cat /proc/acpi/wakeup
     ```
     This will show a list of devices and their current wake status (`enabled` or `disabled`).

   - Find the device related to your keyboard or USB controller (it should look like `USB1`, `USB2`, etc.). Then, enable it:
     ```bash
     echo 'USB0' | sudo tee /proc/acpi/wakeup
     ```
     Replace `USB0` with the identifier for your USB keyboard.

3. **Configure a Specific Key for Waking the System**:
   To configure **a specific key** (for example, `Spacebar` or `Ctrl` + `Alt`) to wake the system, you need to modify how the system handles keyboard events.

   - Use `evtest` to detect key presses and associate a specific key with wake-up functionality. Install `evtest` if not already installed:
     ```bash
     sudo dnf install evtest
     ```

   - Run `evtest` to see which device is your keyboard:
     ```bash
     sudo evtest
     ```
     Press a few keys, and look for the event associated with your keyboard.

   - Now, bind a specific key event to wake the system. You can use udev rules or a custom script to listen for the desired keypress.

### Example:
Here’s an example of a simple script to enable a specific key to wake the system (e.g., spacebar):

```bash
#!/bin/bash
while true; do
  if evtest | grep --line-buffered "KEY_SPACE"; then
    echo enabled > /sys/bus/usb/devices/usbX/power/wakeup
  fi
done
```
Replace `usbX` with the appropriate USB device number. You can add this script to your startup applications, ensuring it runs at boot and listens for the key press.

### Note:
This solution allows **waking** the computer from sleep using a **specific key** on your keyboard, but a keyboard shortcut won’t work directly once the system is asleep. Waking with a specific key is as close as you can get to using a shortcut while the system is in suspend.