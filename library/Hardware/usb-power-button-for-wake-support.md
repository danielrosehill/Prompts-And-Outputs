---
title: "USB power button for wake support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd like to have an easy way to wake my computer from a suspend state. I purchased an external button for this purpose but that requires integration with the PSU. I'm wondering if there might be a simpler solution like perhaps just a power button that I can connect via USB. Its sole purpose would be waking the desktop up from suspend. Although putting it into sleep state would be helpful too

# Output

Given your setup and your goal of waking the desktop from a suspend state using a simple external device, here are a few options that could be more practical than integrating a button with your PSU:

### 1. **USB Power Button**
A **USB-connected power button** is an ideal solution that doesn’t require PSU modifications. While some motherboards allow waking via USB, here are steps you can take:

- **Enable USB Wake Support**:  
  Most modern motherboards, including the one in your custom build (Pro B760M-A WiFi), support waking up the computer from suspend via USB. Here's how to enable it:
  
  1. Enter your BIOS/UEFI by pressing **DEL** or **F2** when starting up the computer.
  2. Look for options such as **Wake on USB** or **USB Power after Shutdown**. Make sure these are enabled.
  
- **USB Power Button Devices**:  
  There are specific USB buttons sold for waking up or powering on computers. These typically plug into a USB port and function similarly to the main power button.

### 2. **USB Keyboards/Mouse for Wake-Up**
If you don't mind using existing peripherals, you can configure your keyboard or mouse to wake the computer from suspend. Most modern desktops support this. Here's how:

1. **Enable Wake from USB**: Ensure that USB wake-up support is enabled in the BIOS/UEFI, as mentioned above.
2. **Configure via Fedora**:
   - Open a terminal and run:
     ```bash
     sudo nano /etc/default/grub
     ```
   - Look for the line that begins with `GRUB_CMDLINE_LINUX`, and add `usbcore.autosuspend=-1` to prevent USB devices from going into deep suspend.
   - Then update your GRUB configuration:
     ```bash
     sudo grub2-mkconfig -o /boot/grub2/grub.cfg
     ```
   - Finally, run this command to make sure your devices can wake the system:
     ```bash
     sudo sh -c 'echo enabled > /sys/bus/usb/devices/usbX/power/wakeup'
     ```
     Replace `usbX` with the appropriate USB bus number.

### 3. **Wireless Power Button**
Another option is a **wireless power button**, which can work via Bluetooth or Zigbee. These can be paired with the system and configured to act as a wake-up device or even put the system to sleep.

### 4. **Peripheral Control Widgets**
You might also find it helpful to look for external devices specifically designed for power management, such as **USB hubs with power control** or **custom widgets** that send suspend and wake commands over USB.

This approach avoids the complexity of integrating with the PSU and gives you the simplicity of an external button or keyboard shortcut.

Let me know if you'd like specific product recommendations for USB or wireless power buttons!