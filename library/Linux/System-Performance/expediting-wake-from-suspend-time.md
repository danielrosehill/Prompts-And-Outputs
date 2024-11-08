---
title: "Expediting wake from suspend time"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

How can I Make the sleep and wake process work as quickly as possible?

# Output

To make the **sleep (suspend) and wake** process as fast as possible on your Fedora system, several optimizations can improve speed and reduce delays. Here are steps to ensure that both the sleep and wake processes are quick and efficient:

### 1. **Optimize Power Settings in BIOS/UEFI**
- **Fast Boot**: Enable **Fast Boot** in your system's BIOS/UEFI settings. This minimizes the time spent on hardware initialization during wake-up.
- **Enable USB Wake Support**: If you're waking up the system with a USB device (e.g., keyboard or power button), ensure that **USB wake** is enabled in BIOS.
- **Wake Timers**: Disable unnecessary **wake timers** to prevent devices from triggering wake events that slow down the process.

### 2. **Use Light Suspend States**
Fedora’s default sleep (suspend) state is usually **S3 (Suspend to RAM)**, but some modern systems support a lighter suspend state called **S2Idle**. This state can lead to faster suspend and wake times. You can check and configure suspend states:

- **Check Available Suspend States**:
  Run this command to see which states are supported on your system:
  ```bash
  cat /sys/power/state
  ```
  You'll see options like `freeze`, `mem`, `disk`:
  - `freeze`: Low-power idle (S2Idle).
  - `mem`: Suspend-to-RAM (S3).
  - `disk`: Hibernate (to disk).

- **Switch to S2Idle for Faster Suspend/Wake**:
  To force S2Idle (if supported), you can configure it with this command:
  ```bash
  sudo sh -c 'echo s2idle > /sys/power/mem_sleep'
  ```

You can also make this change persistent by adding it to your bootloader configuration in `/etc/default/grub`:
```bash
GRUB_CMDLINE_LINUX="... mem_sleep_default=s2idle"
```
Then update your GRUB configuration:
```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

### 3. **Optimize Swap Settings for Hibernate (Optional)**
If you're using **hibernate** (which saves your session to disk), ensuring that you have a fast **SSD** and optimized **swap** space is crucial. For faster hibernation and wake times:
- Use a **swap file** or **swap partition** on a fast SSD.
- Make sure your swap space is large enough to hold all the data from RAM.

### 4. **Disable Unnecessary Wake Devices**
Some devices (like network cards or USB devices) might be configured to wake up the system unnecessarily. This can slow down the wake process. You can disable wake on these devices:

- List devices capable of waking up the system:
  ```bash
  cat /proc/acpi/wakeup
  ```
- Disable unnecessary wake devices:
  ```bash
  sudo sh -c 'echo "XHC" > /proc/acpi/wakeup'  # Replace XHC with the device name
  ```

### 5. **Optimize Fedora Power Management**
- **Tuned profiles**: Fedora has **Tuned** profiles for various use cases. You can use the **balanced** or **latency-performance** profiles for faster sleep and wake transitions. Install and configure Tuned with:
  ```bash
  sudo dnf install tuned
  sudo systemctl enable tuned --now
  sudo tuned-adm profile balanced
  ```
  You can try switching to a low-latency profile for better performance:
  ```bash
  sudo tuned-adm profile latency-performance
  ```

### 6. **Remove Unnecessary Modules**
On some systems, certain kernel modules can slow down the sleep or wake process. You can blacklist modules that are unnecessary for your setup, which can shave off time from both suspend and resume processes.

- To remove unnecessary modules from the sleep process:
  - List loaded kernel modules:
    ```bash
    lsmod
    ```
  - Blacklist modules by adding them to `/etc/modprobe.d/blacklist.conf`.

### 7. **Optimize Display and Peripheral Management**
- **Reduce Display Turn-Off Delay**: Sometimes, delays in the wake process can be due to the display taking longer to turn on. You can adjust power settings to reduce screen off delay after waking up.
- **USB Power Settings**: For faster wake times, avoid allowing USB devices to go into deep power-saving modes that require a full reinitialization upon waking. You can configure these settings with **powertop**:
  ```bash
  sudo dnf install powertop
  sudo powertop --auto-tune
  ```

### 8. **Use `systemd` for Optimized Sleep**
The **systemd** service handles power management in modern Linux distributions, including Fedora. You can customize sleep/wake behavior by editing `systemd` configuration files:
- Open the sleep.conf file for editing:
  ```bash
  sudo nano /etc/systemd/sleep.conf
  ```
- Set desired behaviors for suspend:
  ```ini
  [Sleep]
  SuspendMode=freeze
  HibernateMode=platform shutdown
  SuspendState=mem
  HibernateState=disk
  ```
- Save and restart systemd:
  ```bash
  sudo systemctl restart systemd-logind
  ```

### 9. **Use SSDs and NVMe Drives**
If your system uses **SSD** or **NVMe** storage, your wake times will already be faster. Ensure you're using a fast storage solution for your swap space (if you're using hibernate) to minimize delays.

### 10. **Keep Firmware and Kernel Updated**
Firmware and kernel updates often improve system stability and hardware support for power management features like sleep and wake. Regularly updating your BIOS/UEFI and kernel will ensure optimal performance.

- To update Fedora’s kernel:
  ```bash
  sudo dnf update kernel
  ```

### Summary of Key Steps:
- **Enable USB wake** in BIOS and reduce wake sources.
- Use **S2Idle** suspend state if supported for quicker transitions.
- Optimize power settings in Fedora with **Tuned** profiles and **systemd**.
- Minimize wake-up time by disabling unnecessary modules and peripherals.

By following these steps, you should achieve faster suspend and wake times on your Fedora system. Let me know if you need help with any specific configurations!