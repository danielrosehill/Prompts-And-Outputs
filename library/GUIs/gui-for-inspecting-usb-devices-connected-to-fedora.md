---
title: "GUI for inspecting USB devices connected to Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are several **GUI tools** available on **Fedora Linux** that allow you to inspect the details of connected USB devices. Here are a few that are commonly used:

### 1. **GNOME Disks**
Even though primarily used for managing storage, **GNOME Disks** can also give you details about connected USB storage devices.

- **Install** (if not already installed):
  ```bash
  sudo dnf install gnome-disk-utility
  ```

- **How to use**:
  - Open **Disks** (it might be listed as **Disks** or **GNOME Disks** in your applications).
  - Select a connected USB device to see details like model, serial number, and partitions.

However, GNOME Disks is mostly for storage devices and might not provide detailed information for other types of USB devices (e.g., keyboards, mice).

### 2. **USBView**
**USBView** is a simple yet powerful GUI tool that provides detailed information about all connected USB devices, including non-storage devices. It’s very user-friendly and gives you a clear hierarchy of USB ports and devices connected to each.

- **Install**:
  ```bash
  sudo dnf install usbview
  ```

- **How to use**:
  - Run `usbview` from the terminal or find it in your applications menu.
  - It provides a tree view of all USB devices connected to your system. When you click on a device, it shows detailed information such as the vendor ID, product ID, manufacturer, and more.

This tool is very useful for identifying USB dongles and other devices.

### 3. **HardInfo (Hardware Information)**
**HardInfo** is a system profiler and benchmarking tool that provides a lot of details about your hardware, including USB devices.

- **Install**:
  ```bash
  sudo dnf install hardinfo
  ```

- **How to use**:
  - Launch **HardInfo** from your applications menu or via the terminal (`hardinfo`).
  - In the **Devices** section, you’ll find a **USB Devices** category, which lists all connected USB devices along with their details (vendor, model, serial, etc.).

### 4. **KDE Plasma’s Info Center (For KDE Users)**
If you're using the **KDE Plasma** desktop environment, **KDE Info Center** provides detailed information about your hardware, including USB devices.

- **Install** (if needed):
  ```bash
  sudo dnf install kinfocenter
  ```

- **How to use**:
  - Open **Info Center** from your applications menu.
  - In the **Devices** section, look for **USB Devices**. This will give you detailed information about all connected USB peripherals, similar to `lsusb`.

### 5. **LSHW-gtk**
**LSHW-gtk** is the graphical front-end for the `lshw` command, which provides detailed information about hardware, including USB devices.

- **Install**:
  ```bash
  sudo dnf install lshw-gtk
  ```

- **How to use**:
  - Run `lshw-gtk` from the terminal, or find **Hardware Lister** in your applications menu.
  - Navigate to the **USB Devices** section for details on each device.

### Summary of GUI Tools for USB Device Inspection:
- **GNOME Disks**: For inspecting storage-related USB devices.
- **USBView**: For detailed inspection of all USB devices (highly recommended for general USB device management).
- **HardInfo**: For a system-wide view, including USB devices.
- **KDE Info Center**: For users running KDE Plasma.
- **LSHW-gtk**: A versatile hardware inspection tool with a graphical interface.

For general USB device identification and inspection, I recommend **USBView**, as it provides the most comprehensive view of all connected USB devices.

Let me know if you need help with installation or using any of these tools!