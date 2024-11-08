---
title: "Can you have an internal drive that powers on just for backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking whether it is possible to have an **internal hard drive** that is only powered on periodically for the purpose of taking backups and remains **unpowered** otherwise.

Yes, it is possible to configure an internal hard drive to power on only during specific times or when needed for backup, and to power it off when not in use. This can be achieved by controlling the power state of the drive through various methods such as manual or automated power management settings. Here’s how you can accomplish this on your **Fedora Linux** system:

### Approaches for Powering On/Off Internal Drives Periodically

#### 1. **Using `hdparm` to Manage Power State**
   - **`hdparm`** is a tool that allows you to configure and manage power settings for hard drives. You can use it to put a hard drive into standby (low-power) or spin-down mode when it's not needed.
   
   - **To put the drive in standby mode (low power)**:
     - First, identify the drive you want to manage (e.g., `/dev/sdb`):
       ```bash
       lsblk
       ```
     - Then, put the drive into standby mode (it will stop spinning and use minimal power):
       ```bash
       sudo hdparm -y /dev/sdb
       ```

   - **To spin down the drive (completely stop the drive)**:
     ```bash
     sudo hdparm -Y /dev/sdb
     ```

   - **Wake up the drive when needed**:
     - The drive will automatically wake up when accessed (e.g., when performing a backup), but you can also manually wake it up by sending a simple read command:
       ```bash
       sudo hdparm -C /dev/sdb
       ```

   - **Automate with Cron Jobs**:
     You can use cron jobs to schedule when the drive powers down and when it should be available for backups. For example, to schedule a backup at 2:00 AM every day and power down the drive afterward:
     - Create a cron job to run your backup script:
       ```bash
       0 2 * * * /path/to/your/backup_script.sh
       ```
     - Add a command to the backup script to spin down the drive after the backup is done:
       ```bash
       sudo hdparm -Y /dev/sdb
       ```

#### 2. **Using `udisksctl` to Control Drive Power**
   - **`udisksctl`** is a tool that manages block devices. You can use it to unmount and power off a specific drive.
   
   - **Unmount and Power Off the Drive**:
     - Unmount the drive:
       ```bash
       sudo udisksctl unmount -b /dev/sdb1
       ```
     - Power off the drive:
       ```bash
       sudo udisksctl power-off -b /dev/sdb
       ```

   - **Mount the Drive When Needed**:
     - To mount the drive again and power it on, you can use:
       ```bash
       sudo udisksctl mount -b /dev/sdb1
       ```
     - This will automatically power the drive back on.

#### 3. **Using `hd-idle` to Automatically Spin Down the Drive**
   - **`hd-idle`** is a daemon that can automatically spin down inactive drives after a specified period of time.
   
   - **Install `hd-idle`**:
     - It may not be available directly from Fedora repositories, but you can build it from source or install from a third-party repository:
       ```bash
       git clone https://github.com/adelolmo/hd-idle
       cd hd-idle
       sudo make install
       ```
   
   - **Configure `hd-idle`**:
     - Set the idle time for your internal backup drive (e.g., `/dev/sdb`):
       ```bash
       sudo hd-idle -i 600 -a /dev/sdb
       ```
     - This example sets the drive to spin down after **600 seconds (10 minutes)** of inactivity.
   
   - **Automate Wake-Up**:
     - The drive will automatically spin up when accessed, meaning it will only power up when your backup process starts or when the drive is otherwise needed.

#### 4. **Using `systemd` to Control the Drive's Power State**
   - You can use **systemd** services to schedule when the drive should be mounted and unmounted, giving you control over when it powers up or down.

   - **Create a Custom Systemd Service**:
     - First, create a service to **mount and power on** the drive:
       ```bash
       sudo nano /etc/systemd/system/mount-backup-drive.service
       ```
     - Add the following content:
       ```ini
       [Unit]
       Description=Mount Backup Drive

       [Service]
       Type=oneshot
       ExecStart=/usr/bin/udisksctl mount -b /dev/sdb1

       [Install]
       WantedBy=multi-user.target
       ```
     - Then create another service to **unmount and power off** the drive:
       ```bash
       sudo nano /etc/systemd/system/unmount-backup-drive.service
       ```
     - Add the following:
       ```ini
       [Unit]
       Description=Unmount Backup Drive

       [Service]
       Type=oneshot
       ExecStart=/usr/bin/udisksctl unmount -b /dev/sdb1
       ExecStop=/usr/bin/udisksctl power-off -b /dev/sdb

       [Install]
       WantedBy=multi-user.target
       ```
     - You can then use **systemd timers** to automate when the drive is mounted for backups and when it is powered off.

#### 5. **Physical Solutions: SATA Power Switches**
   If you want to physically control when the drive gets power, you can install a **SATA power switch** inside your computer. This allows you to toggle power to the drive manually or with a scheduled relay system. This is a more advanced and hardware-based solution but gives you full control over when the drive is powered.

---

### Summary of Methods:
1. **`hdparm`**: Control drive power by manually or automatically spinning it down and waking it up when needed.
2. **`udisksctl`**: Unmount and power off the drive, then mount it when required for backups.
3. **`hd-idle`**: Automatically spin down inactive drives after a configurable idle period.
4. **`systemd` Services**: Automate the mounting/unmounting and powering on/off of the drive using systemd services and timers.
5. **Physical SATA Switch**: Install a hardware-based solution to manually control power.

### Conclusion:
The easiest method is likely using **`hdparm`** or **`udisksctl`** combined with cron jobs or systemd timers to automate when the drive is powered on for backups and when it powers off. This approach keeps the drive inactive most of the time, reducing wear and energy consumption while ensuring the drive is available for scheduled backups.

Let me know if you'd like more detailed instructions on any of these solutions!