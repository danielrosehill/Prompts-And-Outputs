---
title: "Tools to calculate live power consumption in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are several applications available for **Fedora** that can help you estimate how much electricity your computer is using during operation:

### 1. **PowerTOP**
   - **Description**: PowerTOP is a popular tool for Linux systems, designed primarily for optimizing power consumption. It provides detailed information about the system's power usage and suggests tweaks to reduce energy consumption.
   - **Features**:
     - Real-time monitoring of power usage by components (CPU, GPU, devices, etc.).
     - Provides an estimate of the current power consumption (in watts).
   - **Installation**:
     ```bash
     sudo dnf install powertop
     ```
   - **Usage**: Run it in terminal using `sudo powertop`. It will display the power consumption of your system in real-time.

### 2. **GNOME Power Statistics (gnome-power-manager)**
   - **Description**: If you are using a GNOME desktop environment, this tool provides simple power statistics about your device.
   - **Features**:
     - Monitor power consumption over time.
     - View the power usage of various system components.
   - **Installation**:
     ```bash
     sudo dnf install gnome-power-manager
     ```
   - **Usage**: It is typically integrated into the GNOME desktop, providing graphical statistics on power consumption.

### 3. **s-tui (Stress Terminal UI)**
   - **Description**: While primarily used for monitoring CPU temperature and stress testing, s-tui can also give you an overview of system power consumption when used with Intel’s RAPL (Running Average Power Limit) framework.
   - **Features**:
     - Graphical interface in the terminal.
     - CPU power consumption statistics.
   - **Installation**:
     ```bash
     sudo dnf install s-tui
     ```
   - **Usage**: Run `s-tui` in the terminal, and it will show real-time data on CPU usage, power, and temperature.

### 4. **TLP**
   - **Description**: TLP is a command-line tool that helps to optimize and monitor laptop power consumption. While it doesn't display real-time power usage directly, it helps in managing and reducing overall consumption by applying various system tweaks.
   - **Installation**:
     ```bash
     sudo dnf install tlp
     ```

### Combining with External Tools:
If your hardware supports **Intel RAPL** or **AMD PowerCap** technologies, applications like PowerTOP can provide detailed estimates of power usage. You may also need to consult the BIOS/UEFI for additional power data.

These tools should give you a good estimation of your system's power usage while running Fedora.