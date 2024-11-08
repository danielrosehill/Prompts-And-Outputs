---
title: "Enabling hibernate in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

Can you explain the difference between sleep and hibernate? In Fedora I have a sleep option but hibernate is greyed out. Can it be enabled and why might it be useful?

# Output

### Difference Between Sleep and Hibernate:

1. **Sleep (Suspend)**:
   - **How it works**: In **sleep mode**, your computer enters a low-power state. The current session (open apps, windows, etc.) is kept in the **RAM**, which requires a small amount of power. The CPU, display, and most other components are powered down.
   - **Speed**: Waking up from sleep is almost instant because data is still in RAM.
   - **Power consumption**: Sleep mode consumes a small amount of power to keep the RAM active, so it's useful for short breaks where you want to resume quickly.
   - **Risk**: If power is lost (e.g., battery dies or power outage), the session will be lost because RAM is volatile memory.

2. **Hibernate**:
   - **How it works**: In **hibernate mode**, the computer writes the entire contents of RAM (open apps, data, etc.) to the **hard drive (swap partition)** and then powers off completely. When you turn the computer back on, it restores the data from the drive to RAM.
   - **Speed**: Waking from hibernate takes longer than sleep because it must load everything from the hard drive (or SSD).
   - **Power consumption**: Hibernate uses **zero power** because the computer is completely powered off.
   - **Benefit**: Hibernate is useful when you won’t be using your computer for a longer period but want to resume your session exactly where you left off without using any power. It also prevents data loss in case of power failure, unlike sleep.

---

### Why is Hibernate Greyed Out in Fedora?

By default, **hibernate** is often **disabled or greyed out** on Fedora (and other Linux distros) for several reasons:

1. **Swap Partition or Swap File**:
   - Hibernate requires a **swap partition** or **swap file** that is at least as large as the amount of **RAM** in your system. When you hibernate, the system copies the contents of the RAM to the swap partition.
   - If your system does not have enough swap space (or no swap at all), hibernate cannot be enabled.

2. **File System**:
   - Fedora needs to ensure that the file system (especially swap) is properly configured for hibernation. If the swap partition is not correctly set up, hibernate will not work.

3. **UEFI/BIOS Settings**:
   - Hibernate may be disabled in your system's BIOS/UEFI settings, which can prevent Fedora from accessing the necessary hardware features.

4. **System Stability**:
   - Hibernate may be disabled by default for stability reasons on certain hardware configurations (especially newer systems). Improper hibernate/resume cycles can cause system crashes or data corruption.

---

### How to Enable Hibernate in Fedora:

1. **Check for Swap Partition**:
   - Ensure your system has a swap partition or file that is large enough to store the contents of your RAM.
   - Check swap space with:
     ```bash
     free -h
     ```
     Look for the **Swap** line. The swap space should be at least as large as your system’s RAM.

2. **Configure Hibernate**:
   - If you have sufficient swap space, you can enable hibernate by configuring the **GRUB bootloader** and **systemd**:
   
   - Edit the GRUB configuration to include the swap partition:
     ```bash
     sudo nano /etc/default/grub
     ```
     Find the line that starts with `GRUB_CMDLINE_LINUX`, and add `resume=UUID=your-swap-partition-UUID` (replace `your-swap-partition-UUID` with the actual UUID of your swap partition, which you can find by running `blkid`).
     
     Update the GRUB configuration:
     ```bash
     sudo grub2-mkconfig -o /boot/grub2/grub.cfg
     ```

3. **Enable Hibernate in Systemd**:
   - To allow hibernate through **systemd**, check that the **resume** kernel parameter is set:
     ```bash
     sudo systemctl hibernate
     ```
   - If this works, you can add the hibernate option to your power management settings.

4. **Reboot and Test**:
   - After making the above changes, reboot your computer and test whether hibernate is working.

---

### Why Might Hibernate Be Useful?

- **Longer breaks**: Hibernate is ideal if you're taking an extended break from your computer and don’t want to lose your session.
- **Save power**: Hibernate uses zero power, so it's perfect for laptops or systems that may be unplugged for long periods.
- **Data safety**: Since the session is saved to disk, you don’t risk losing data due to power outages, unlike sleep.

Let me know if you need further help setting this up!