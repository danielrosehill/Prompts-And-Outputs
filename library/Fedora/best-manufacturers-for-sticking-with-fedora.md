---
title: "Best manufacturers for sticking with Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I plan on using Fedora Linux for the indefinite future. 

Are there specific manufacturers that have a reputation for making hardware that is more compatible with this distro. 

For example - it is generally better to use an Nvidia or AMD GPU?

# Output

If you plan on using **Fedora Linux** for the indefinite future, it’s a good idea to consider hardware that is known for better compatibility with Linux in general and Fedora specifically. Here are some manufacturers and hardware recommendations to help ensure a smooth experience:

### 1. **GPU Compatibility: NVIDIA vs AMD**

#### **AMD GPUs** (Recommended for Fedora)
- **Open-Source Drivers**: AMD has made substantial contributions to the Linux open-source community, and their **open-source drivers (AMDGPU)** are part of the Linux kernel itself. This means that **Fedora** and other distributions generally have very good **out-of-the-box support** for AMD GPUs.
- **Ease of Installation**: Unlike NVIDIA, AMD's open-source drivers are automatically installed with most distributions, including Fedora, meaning there are **fewer steps** to take to get your GPU working properly.
- **Wayland Support**: AMD GPUs generally have better **Wayland** support compared to NVIDIA. This means smoother performance if you use the Wayland session of KDE Plasma or GNOME on Fedora.

#### **NVIDIA GPUs**
- **Proprietary Drivers**: NVIDIA provides proprietary drivers for their GPUs, but they can be more challenging to install and maintain on Fedora. Fedora tends to ship with **Nouveau**, an open-source driver for NVIDIA cards, which often performs poorly for anything requiring 3D acceleration, like gaming or creative work.
- **Driver Installation**: You can install NVIDIA proprietary drivers using tools like **RPM Fusion** repositories, but this adds a layer of complexity. Driver updates sometimes lag behind kernel updates, leading to potential incompatibility issues.
- **Wayland Limitations**: Historically, NVIDIA cards have had limited **Wayland** support. Recent developments are improving this, but for now, **AMD** is still generally a better choice for Wayland.

### 2. **Laptop Manufacturers with Good Fedora Support**

#### **Lenovo ThinkPad** (Recommended)
- **ThinkPads** are widely considered one of the best options for Linux users, including Fedora, due to their compatibility and support.
- Lenovo has partnered with **Red Hat** to officially support Linux on many ThinkPad models, which means Fedora often runs exceptionally well out of the box on these laptops.
- ThinkPads also have very configurable BIOS options, which can make setting up Linux easier if any issues do arise.

#### **Dell XPS and Precision Series**
- **Dell** has a good track record of offering **developer editions** with Ubuntu pre-installed (XPS and Precision series), meaning they provide compatible drivers that are also usable by other Linux distributions like Fedora.
- Their hardware is tested with Linux in mind, and Dell’s higher-end XPS and Precision models are generally great choices for running Fedora smoothly.
- **Project Sputnik**: Dell's support for Linux under Project Sputnik means there's ongoing driver and firmware support that benefits all Linux users, including those on Fedora.

#### **System76**
- **System76** is a dedicated Linux hardware manufacturer. Their machines are designed to run **Pop!_OS** (their Linux-based distribution) or **Ubuntu**, but they also work well with Fedora.
- They contribute actively to the Linux community, meaning any hardware they support typically receives good Linux driver support.
- They offer laptops, desktops, and mini PCs that are designed with Linux compatibility in mind.

#### **HP EliteBook and ProBook Series**
- **HP EliteBooks** and **ProBooks** are often recommended for Linux due to their good out-of-the-box compatibility and robust hardware quality.
- While not as well-known for their Linux support as Lenovo or Dell, many Fedora users have reported good experiences using these models, and they tend to have broad hardware compatibility.

### 3. **Wi-Fi and Network Compatibility**

#### **Intel Wi-Fi Cards** (Recommended)
- **Intel** Wi-Fi cards are usually the best choice for Linux users, including Fedora users, because they have strong support through the **open-source Intel drivers** that are integrated into the Linux kernel.
- **Realtek** Wi-Fi chips are more hit-or-miss—often requiring third-party drivers and more configuration. To ensure a trouble-free experience, choosing **Intel** network components is recommended.

#### **Ethernet Adapters**
- Most **Realtek** and **Intel** Ethernet adapters work without issues on Fedora, but **Intel** network adapters tend to have better driver support in the Linux kernel.

### 4. **CPU and System Architecture**

#### **AMD vs Intel CPUs**
- Both **Intel** and **AMD** CPUs work well with Fedora Linux, but there are a few things to consider:
  - **Intel CPUs** have a long history of Linux compatibility, and their integrated graphics (e.g., **Intel Iris Graphics**) are also well-supported.
  - **AMD CPUs**, especially the **Ryzen** series, also work very well with Fedora. Ryzen CPUs often outperform Intel equivalents in multi-threaded workloads, making them a popular choice for Linux power users. 
  - **Integrated Graphics**: If you want to avoid a dedicated GPU altogether, both **AMD APUs** (Ryzen with integrated Vega graphics) and **Intel iGPUs** are good choices and generally well-supported.

### 5. **Peripherals and Additional Hardware**

#### **Docking Stations**
- **Thunderbolt Docking Stations**: Many manufacturers like **Lenovo** and **Dell** offer Thunderbolt docks that work seamlessly with their own laptops when using Fedora. Just make sure to enable **Thunderbolt support** in BIOS settings.
- **USB-C Hubs**: Look for **Linux-compatible** USB-C hubs. Hubs from brands like **Anker** are known for good Linux compatibility and often work well without requiring additional drivers.

#### **Webcams and Audio**
- Most **integrated webcams** work well out of the box, but for external webcams, **Logitech** models like the **C920** have widespread Linux support.
- **Audio**: Audio can sometimes be an issue on Linux, especially with specific Bluetooth devices. Stick with **Intel** or **Realtek** audio chips, as they are generally well-supported. **PulseAudio** and **PipeWire** (the default on Fedora) provide solid audio support, but there may be some configuration needed for more advanced setups.

### Summary Recommendations
- **GPU**: **AMD** is generally recommended over **NVIDIA** for better out-of-the-box experience and Wayland support.
- **Laptop Manufacturers**: **Lenovo ThinkPads**, **Dell XPS**, **Dell Precision**, and **System76** are top choices. **HP EliteBooks** are also well-regarded.
- **Wi-Fi**: **Intel Wi-Fi** cards are strongly recommended for their excellent Linux compatibility.
- **CPU**: Both **AMD** and **Intel** CPUs are good choices. For integrated graphics, **Intel iGPUs** and **AMD APUs** are well-supported.
- **Peripherals**: Look for **Logitech webcams** and **Intel or Realtek audio chips** for better compatibility.

Choosing hardware from these recommended manufacturers will generally lead to a much smoother experience when running **Fedora Linux** for the long term, with fewer driver issues and better community support.