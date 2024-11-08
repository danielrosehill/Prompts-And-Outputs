---
title: "Programmable keyboards with QMK support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You are asking about macro keyboards that would work well with Fedora, and whether compatibility with QMK ensures they will be compatible with Fedora.

---

Yes, if a macro keyboard is compatible with **QMK** firmware, it is generally safe to say that it will work with Fedora (or any Linux distribution). QMK is a highly flexible, open-source keyboard firmware that works across various operating systems, including Linux, macOS, and Windows. Here’s more on why this is true and a few recommended macro keyboards:

### **Why QMK Compatibility Ensures Fedora Compatibility**
1. **Cross-Platform Support:**
   - **QMK Firmware**: Because QMK operates at the firmware level, once the firmware is flashed onto the keyboard, the operating system (including Fedora) will recognize the keyboard as a standard USB input device. You can program the keyboard on any OS and expect it to work seamlessly across different systems.
   - **No Additional Drivers Required:** Since QMK-based keyboards act as standard HID (Human Interface Device) devices, there’s no need for special drivers or software on Linux to get basic functionality.
   - **Configuration via QMK CLI:** You can set up and customize your keymaps, macros, and functions directly via QMK’s command-line tools on Fedora, giving you full control over how the keyboard behaves.

2. **Real-Time Configuration with Tools Like VIA and VIAL:**
   - **VIA and VIAL Compatibility**: Many QMK-based keyboards are also compatible with **VIA** or **VIAL**, allowing real-time programming and macro setup via a graphical interface. This makes configuring your macros on Fedora much easier.
   - **QMK Firmware Flashing:** With QMK, once you have flashed your custom firmware to the keyboard, it stores those configurations directly on the device. This means you can move the keyboard to any machine (including Fedora) without needing to reconfigure anything.

### **Recommended Macro Keyboards Compatible with QMK**
Here are a few macro keyboards that work well with QMK, and by extension, should work perfectly on Fedora:

#### **1. Drop ALT/CTRL/SHIFT**
   - **Description:** These are compact, highly customizable mechanical keyboards from Drop that are fully compatible with QMK firmware. They are designed to be modular, allowing easy swapping of switches, and offer robust macro programming via QMK.
   - **Features:**
     - Full QMK support for deep customization.
     - RGB lighting that can be controlled via QMK.
     - Compact designs with options for 65% (ALT), 75% (CTRL), and TKL (SHIFT).
   - **Best For:** Users who want a compact, fully programmable keyboard that can double as a macro keyboard.

#### **2. Ergodox EZ**
   - **Description:** A highly customizable, ergonomic split keyboard that excels in macro programming and supports QMK. You can program each half of the keyboard separately, making it easy to create layouts specifically tailored to your workflow.
   - **Features:**
     - Full QMK compatibility for custom macros and layouts.
     - Modular design allows for easy swapping and upgrading.
     - Ergonomic split design to reduce strain.
   - **Best For:** Users who prioritize ergonomics and need a lot of macro customization.

#### **3. System76 Launch Keyboard**
   - **Description:** Built specifically for Linux users, the System76 Launch Keyboard is compatible with QMK and has open-source firmware. It’s designed to be versatile, with customizable keys, macros, and profiles, and works seamlessly with Linux systems, including Fedora.
   - **Features:**
     - QMK support with easy configuration through open-source tools.
     - Hot-swappable switches for easy customization.
     - Configurable layouts with macro programming.
   - **Best For:** Linux enthusiasts who want a premium, Linux-focused keyboard with full QMK support.

#### **4. Varmilo V Series Keyboards**
   - **Description:** Varmilo’s V Series is known for high build quality and comes with basic programmability. While not as flexible as full QMK keyboards, they do offer macro programming and can be configured to suit various needs.
   - **Features:**
     - Programmable keys (though not as extensive as QMK).
     - High-quality build with multiple form factors.
     - Solid Linux compatibility out of the box.
   - **Best For:** Users who want a simple, reliable macro setup without the need for deep customization.

#### **5. BM40/BM60 40%/60% Macro Pads**
   - **Description:** These are smaller form factor macro pads that you can customize via QMK. They are perfect if you want to add additional programmable keys alongside your existing keyboard setup. 
   - **Features:**
     - Full QMK compatibility, allowing each key to be programmed with custom macros, shortcuts, or even layers.
     - Small, portable design that complements existing setups.
   - **Best For:** Users who want extra macro keys without replacing their main keyboard.

### **Conclusion**
If a keyboard is **QMK-compatible**, it’s safe to assume that it will work seamlessly on Fedora. This is because QMK keyboards act as standard USB devices, requiring no additional drivers. Furthermore, the ability to flash firmware and save macros directly onto the keyboard makes QMK devices versatile across different systems.

**Recommended Choice:**
- For a **dedicated macro keyboard**, consider a **BM40/BM60 macro pad** or a similar device for adding programmable keys to your existing setup.
- If you want a fully programmable main keyboard, the **Drop ALT/CTRL** or **System76 Launch Keyboard** would be excellent choices, offering deep customization and robust Linux support. 

In any case, if you are comfortable using QMK, you will find that the flexibility it offers makes it easy to create a keyboard setup that matches your workflow on Fedora.