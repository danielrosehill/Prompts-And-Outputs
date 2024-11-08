---
title: "Finding compatible USB power buttons"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you identify any USB power buttons that might work with my hardware and software? That certainly seems like the easiest option

# Output
Here are some USB power buttons that could work with your hardware (custom desktop build with the Pro B760M-A WiFi motherboard) and software (Fedora Workstation 40 with KDE Plasma on Wayland):

### 1. **iFixit USB Power Button**
- **Compatibility**: Works via USB 2.0 or 3.0 ports and is recognized by most modern motherboards, including MSI boards like yours. This button is often used for DIY projects and can act as a physical power button.
- **Usage**: Plug it into any available USB port. After enabling USB wake support in the BIOS, this button can wake your system from suspend and also be configured for sleep with appropriate software settings.
- **Linux Support**: Fedora’s USB power management allows it to interact with suspend/resume commands without issue.

### 2. **ATX Universal USB Power Button by Eleduino**
- **Compatibility**: Plugs into any USB port and emulates a standard power button press. Designed specifically for users who want an external button for PC power control, which includes both wake-up and shutdown functions.
- **Usage**: No drivers needed for Linux. You may need to configure the system’s power settings to allow this button to send sleep commands as well.
- **Hardware Requirements**: Requires USB wake-up settings enabled in the BIOS.
- **Price**: Affordable and often available on marketplaces like Amazon.

### 3. **Sabrent External USB Power Switch (Model: HB-UML1)**
- **Compatibility**: While primarily a USB hub, it features individual power switches for each connected device. This could allow for quick system wake-ups or even control power to other peripherals.
- **Usage**: USB-powered and works with any system that supports USB wake from suspend.
- **Bonus**: If you have multiple USB devices that you want to manually control, this could provide extra functionality.

### 4. **Easyget USB External Power Button**
- **Compatibility**: This is another external power button with a simple setup, similar to the Eleduino product. It's connected via USB and typically used by DIY enthusiasts who need an external button for triggering power functions.
- **Usage**: Can be plugged into a front USB port for quick wake/suspend control. Works on Linux systems without additional drivers.
- **Features**: You can use it for waking your computer and even triggering suspend with software adjustments.

### 5. **Delock USB Push Button Switch**
- **Compatibility**: Delock offers a simple USB switch that mimics the behavior of a PC power button. It’s designed for use with a variety of systems, including custom builds like yours.
- **Usage**: Just plug it into a USB port and enable USB wake in your BIOS. This can also be configured in Fedora to allow suspend commands via the button.

### **Important Steps for Configuration**:
1. **Enable USB Wake Support**:
   As mentioned earlier, make sure to enable USB wake in the BIOS/UEFI. This is crucial for any of these devices to wake your computer from suspend.

2. **Check Linux USB Power Management**:
   You can use tools like `powertop` on Fedora to ensure your USB devices are set to stay active for waking the system.

These USB power buttons should give you the functionality you need for easily waking your desktop from suspend. Let me know if you’d like links to specific products or more technical setup guidance!