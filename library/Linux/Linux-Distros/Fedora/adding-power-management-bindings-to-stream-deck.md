---
title: "Adding power management bindings to Stream Deck"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm setting up my Stream Deck mini on my fedora workstation 40 computer. I would like to be able to put the computer into sleep mode and wake it from it using the shortcuts. Would it be possible to create power management bindings on this hardware? 

# Output

Yes, it's possible to create power management bindings on your Stream Deck Mini for your Fedora 40 workstation to put the computer into sleep mode or wake it up. Here’s a basic approach to achieve that:

### 1. **Install the `streamdeck-ui` Tool**:
   The open-source tool **`streamdeck-ui`** is available for Linux and can be used to configure your Stream Deck on Fedora. You can use it to assign custom commands to buttons, including power management shortcuts.
   
   To install:
   ```bash
   sudo dnf install python3-pillow python3-evdev
   pip install streamdeck-ui
   ```

   After installation, you can run `streamdeck` to open the configuration UI.

### 2. **Assign Sleep Mode Shortcut**:
   In Fedora, you can use a command to put the computer into sleep mode. Here’s how you can assign that command to a button on the Stream Deck:

   - Open the **`streamdeck-ui`** application.
   - Choose an empty button and assign it a custom action.
   - For sleep mode, you can bind the following command:
     ```bash
     systemctl suspend
     ```
   - This will immediately put your computer into sleep mode when you press the assigned button.

### 3. **Wake the Computer**:
   Unfortunately, waking the computer from sleep is usually hardware-dependent and often requires physical interaction, like pressing a keyboard key or a power button. The Stream Deck does not have built-in support for waking up a computer from sleep as it relies on USB power, which is typically turned off during sleep. 

   However, some workarounds include:
   - **USB Wakeup**: Ensure your USB ports are configured to wake the system. You can check this by enabling USB wakeup in your BIOS/UEFI settings or through specific kernel configurations.
   - **Wake-on-LAN (if applicable)**: If your computer supports Wake-on-LAN, you could potentially use a network-triggered wake-up as an alternative, although this would not involve the Stream Deck.

### 4. **Additional Power Commands**:
   You can also bind other power-related commands like shutting down or rebooting the system:
   - **Shutdown**:
     ```bash
     systemctl poweroff
     ```
   - **Reboot**:
     ```bash
     systemctl reboot
     ```

This setup will let you efficiently control power management through the Stream Deck for the actions that are feasible within the Fedora environment.