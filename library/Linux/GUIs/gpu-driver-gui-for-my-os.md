---
title: "GPU driver GUI for my OS"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Speaking of my GPU: AMD Radeon RX 7700 XT s
As you know, I use Fedora Linux Workstation 40
I think that I'm using the right driver but I don't have a GUI where I can see or change any of the settings
Is there one available?

# Output

Based on your setup with an AMD Radeon RX 7700 XT GPU and Fedora Workstation 40, you have a few options for GUI tools to monitor and control your GPU settings:

1. CoreCtrl
   - This is one of the most comprehensive GUI tools for AMD GPUs on Linux[5].
   - It allows you to control fan speeds, clock speeds, and monitor various GPU parameters.
   - Installation on Fedora: 
     ```
     sudo dnf copr enable erife/CoreCtrl
     sudo dnf install corectrl
     ```

2. LACT (Linux AMDGPU Control Application)
   - This is a newer tool written in Rust with a GTK4 interface[3][4].
   - It offers fan control, overclocking, and information reporting.
   - You can find installation instructions on its GitHub page.

3. RadeonTop
   - While not a full control panel, it provides a GUI for monitoring GPU usage.
   - Install with: `sudo dnf install radeontop`

4. AMDGPU-TOP
   - This is a command-line tool, but it offers detailed real-time statistics for AMD GPUs[2].
   - It can be compiled from source or installed via your package manager if available.

To ensure you have the right driver and necessary kernel parameters:

1. Check if the AMDGPU driver is loaded:
   ```
   lsmod | grep amdgpu
   ```

2. For full functionality (especially overclocking), you may need to add the kernel parameter `amdgpu.ppfeaturemask=0xffffffff` to your bootloader configuration.

Remember that while these tools offer great functionality, they may require some setup and could potentially cause system instability if not used carefully. Always research and understand the changes you're making to your GPU settings.

 