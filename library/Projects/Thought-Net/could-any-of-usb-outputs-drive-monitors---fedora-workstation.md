---
title: "Could any of USB outputs drive monitors - Fedora workstation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking how many of the USB-C outputs on your system could potentially be used to drive USB-C monitors, and whether any of them would work for this purpose with Fedora Linux.

### Key Considerations:
- **USB-C vs. DisplayPort Alt Mode**: Not all USB-C ports can drive video signals. To drive a USB-C monitor, your USB-C port needs to support **DisplayPort Alternate Mode**. This allows USB-C ports to carry DisplayPort signals, which is required for video output.
- **Device Support for USB-C Video**: You need to verify which USB-C ports on your system (if any) support this feature, either through documentation, system specs, or using the `lsusb` output.
- **Driver Support on Fedora**: Fedora Linux generally has excellent support for DisplayPort Alt Mode over USB-C, especially with modern GPUs, but it depends on the specific GPU and USB-C implementation in your system.

### Steps to Determine Which Ports Support USB-C Video:
1. **Check System Documentation**:
   - Review the specs for your motherboard or laptop model to check if any of your USB-C ports support **DisplayPort Alt Mode**. Typically, this feature is only available on specific USB-C ports.

2. **Use `lspci` to Identify Video Capable USB Controllers**:
   - Run the following command to list your system's PCI devices:
     ```bash
     lspci | grep -i vga
     ```
   - Look for a USB controller linked to your GPU, indicating that it might support DisplayPort Alt Mode.

3. **Check USB-C Specifications in the Output of `lsusb -t`**:
   - You can check if any of your high-speed USB ports (on **Bus 002**, which supports 20Gbps) are capable of USB-C video output. Look for devices listed as **5000M** or higher, as these may correspond to USB 3.0 or USB 3.2 capable ports.

4. **Check for Driver Support in Fedora**:
   - Fedora generally supports USB-C monitors through DisplayPort Alt Mode as long as the **AMD GPU drivers** are correctly installed. Since you have an **AMD Radeon RX 7700 XT**, this should work seamlessly for video output.

### Conclusion:
- **Determine Capable USB-C Ports**: You need to check your system documentation or `lspci` output to confirm which, if any, USB-C ports support **DisplayPort Alt Mode**.
- **Fedora Compatibility**: With the **AMD Radeon RX 7700 XT** in your system and proper drivers installed, Fedora Linux should handle USB-C monitors via DisplayPort Alt Mode without issues.

If you provide more specific information about your motherboard or system's USB ports, I can help pinpoint which USB-C ports are likely to support video output. Let me know if you need further guidance!