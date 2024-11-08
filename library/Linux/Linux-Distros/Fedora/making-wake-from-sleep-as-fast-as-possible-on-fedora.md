---
title: "Making wake from sleep as fast as possible on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are several ways you can potentially reduce the time it takes for your **Fedora computer** to wake up from sleep. The wake-from-sleep process involves resuming hardware, reloading memory, and reconnecting peripherals, so optimizing these factors can significantly improve wake times. Here are some methods you can use:

### 1. **Update Firmware and Drivers**
Ensure that all firmware and drivers are up to date, including:
- **BIOS/UEFI Firmware**: Check for BIOS or UEFI updates from your computer or motherboard manufacturer. The latest firmware often has performance optimizations and fixes for wake issues.
- **Kernel Updates**: Update your Fedora kernel, as newer kernels can have better hardware support.
  ```bash
  sudo dnf update
  ```
  
### 2. **Disable Unnecessary Peripherals on Wake**
Some peripherals or drivers can delay waking from sleep, especially if the system is waiting for them to respond. You can disable certain hardware from being reinitialized during wake:
- **Disable USB Wakeup**: You can prevent certain USB devices from waking your computer, which can speed up the wake process:
  ```bash
  echo "XHC" | sudo tee /proc/acpi/wakeup
  ```
  Replace `"XHC"` with the appropriate USB device ID from `/proc/acpi/wakeup` that you want to disable.

### 3. **Disable Unneeded Background Services**
Background services can consume time when waking up, especially if they are set to auto-start.
- Use `systemctl` to identify and disable unnecessary services:
  ```bash
  systemctl list-unit-files --state=enabled
  ```
  Disable any services that you don’t need:
  ```bash
  sudo systemctl disable servicename
  ```
  Make sure not to disable any core services required for system operation.

### 4. **Use Suspend-to-RAM Instead of Hybrid Sleep**
- **Suspend-to-RAM (S3)** keeps the RAM powered while turning off other components, which is generally faster than hybrid sleep or suspend-to-disk. Fedora might sometimes use a hybrid sleep state that stores RAM data to disk (hibernation), which takes longer to wake up.
- Ensure that your computer is using **Suspend-to-RAM** rather than **Hybrid Sleep** or **Hibernate**. You can configure this in `/etc/systemd/sleep.conf`:
  ```bash
  sudo nano /etc/systemd/sleep.conf
  ```
  Look for the line:
  ```
  SuspendState=mem
  ```
  If it’s set to **hibernate** or **hybrid-sleep**, change it to **mem**.

### 5. **Optimize Swap Configuration**
If your system is using swap or if hybrid sleep mode is enabled, configuring swap efficiently can speed up waking:
- **Reduce Swap Usage**: By decreasing the swappiness parameter, the system will prefer keeping data in RAM rather than swapping it to disk, leading to quicker wake times.
  ```bash
  sudo sysctl vm.swappiness=10
  ```
  Add the following line to `/etc/sysctl.conf` to make it persistent:
  ```
  vm.swappiness=10
  ```

### 6. **Reduce Connected Devices**
Reducing the number of connected external devices can improve wake times, especially USB devices that require power and need to be reinitialized.

### 7. **Disable Intel ME or AMD PSP if Possible**
If your computer has **Intel Management Engine (ME)** or **AMD Platform Security Processor (PSP)**, disabling them in your BIOS can sometimes improve wake performance. These components often participate in power management and can introduce delays.

### 8. **Tweak Kernel Parameters**
You can experiment with kernel parameters to optimize the wake-up speed:
- **Disable Wake Locks**: Wake locks sometimes prevent the CPU from staying in a deep sleep state. You can tweak the boot parameters by editing GRUB:
  ```bash
  sudo nano /etc/default/grub
  ```
  Find the line starting with `GRUB_CMDLINE_LINUX`, and add parameters such as:
  ```
  GRUB_CMDLINE_LINUX="nowatchdog nosplash"
  ```
  Update GRUB afterwards:
  ```bash
  sudo grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
  ```

### 9. **Use SSD Instead of HDD**
If your Fedora system is running on an **SSD** (Solid State Drive) instead of an **HDD** (Hard Disk Drive), waking up from sleep will be significantly faster. SSDs have much quicker response times compared to traditional hard drives, which means that data can be accessed more quickly during resume.

### 10. **Disable or Minimize Network Manager Wake Actions**
Network interfaces often reinitialize during wake-up, and NetworkManager can delay the wake process while reconnecting:
- **Disable Wake-on-LAN**: Unless you need Wake-on-LAN, you can disable it to speed up wake times.
  ```bash
  sudo nmcli c modify "connection_name" 802-3-ethernet.wake-on-lan ignore
  ```
  Replace `"connection_name"` with your actual network connection name.

### Summary
To minimize the wake-from-sleep time on Fedora:
1. Update firmware, kernel, and drivers.
2. Disable unnecessary peripherals from waking the system.
3. Use **Suspend-to-RAM** instead of hybrid sleep.
4. Optimize swap usage by tweaking swappiness.
5. Minimize USB devices and peripherals attached.
6. Modify kernel parameters and BIOS settings to disable unnecessary checks or components.
7. Use SSD for faster data access during resume.
8. Optimize NetworkManager to reduce delays.

These steps should help to significantly reduce the time it takes for your Fedora computer to wake up from sleep. Let me know if you need further help optimizing your system!

