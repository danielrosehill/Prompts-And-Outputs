---
title: "Asking for configuration for a Borg backup job while maintaining hardware agnosticism"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Setting Up a Recurrent Backup Job on Fedora Using Borg Backup

This guide will show you how to set up a **recurrent backup job** on your Fedora desktop using **Borg Backup**. The goal is to create a **complete backup** of your local filesystem that remains **hardware-agnostic**. This means excluding RAID-specific configurations and ensuring the backup is as flexible as possible for restoration onto different hardware setups.

The backup target is an external SSD mounted at `/mnt/desktop-backup`, and the backup job will run periodically to keep your data up to date. We will make use of **Borg’s incremental backup** capabilities to efficiently manage storage.

### Prerequisites
- Fedora is installed on your system.
- An external SSD is mounted at `/mnt/desktop-backup`.
- **Borg Backup** is installed.
- Sufficient storage space on the SSD to accommodate your backups.

### Step 1: Install Borg Backup
First, you need to install Borg Backup on your Fedora system:

```bash
sudo dnf install borgbackup
```

### Step 2: Initialize the Borg Repository
Before you can create backups, you need to initialize a Borg repository on the SSD.

```bash
borg init --encryption=repokey /mnt/desktop-backup/borg-repo
```

- **`--encryption=repokey`**: This ensures that backups are encrypted, and a key is stored in the repository.
- **`/mnt/desktop-backup/borg-repo`**: This specifies where the repository will be created.

### Step 3: Create Backup Script
To simplify the backup process and make it repeatable, we will create a backup script.

1. **Create a New Script**:

   ```bash
   nano ~/borg-backup.sh
   ```

2. **Add the Following Script Contents**:

   ```bash
   #!/bin/bash

   # Define variables
   REPOSITORY=/mnt/desktop-backup/borg-repo
   BACKUP_NAME=$(hostname)-$(date +%Y-%m-%d_%H-%M-%S)

   # Paths to include in the backup
   INCLUDE_PATHS=(
       "/etc"
       "/home"
       "/var"
       "/usr/local"
       "/root"
       "/opt"
       "/var/lib/flatpak"
       "/var/lib/snapd"
       "/usr/share/applications"
       "/usr/share/icons"
       "$(python3 -m site --user-base)/lib/python3.*/site-packages"
   )

   # Paths to exclude from the backup
   EXCLUDE_PATHS=(
       "/dev"
       "/proc"
       "/sys"
       "/tmp"
       "/run"
       "/mnt"
       "/media"
       "/lost+found"
       "/var/tmp"
       "/home/*/.cache"
   )

   # Create the backup
   borg create -v --stats \
       $REPOSITORY::$BACKUP_NAME \
       ${INCLUDE_PATHS[@]} \
       --exclude ${EXCLUDE_PATHS[@]}

   # Prune old backups (keep last 7 daily, 4 weekly, and 6 monthly backups)
   borg prune -v --list $REPOSITORY --keep-daily=7 --keep-weekly=4 --keep-monthly=6

   # Finish script
   echo "Backup completed successfully at $(date)"
   ```

3. **Save and Make the Script Executable**:

   ```bash
   chmod +x ~/borg-backup.sh
   ```

### Step 4: Set Up Recurrent Backup with `cron`
To make the backup job recurrent, you can schedule it with **cron** to run periodically.

1. **Edit the Crontab**:

   ```bash
   crontab -e
   ```

2. **Add the Following Cron Job** (this example schedules the backup to run every day at 2 AM):

   ```bash
   0 2 * * * /home/$(whoami)/borg-backup.sh >> /var/log/borg-backup.log 2>&1
   ```

- **Explanation**:
  - `0 2 * * *`: Schedule to run every day at 2:00 AM.
  - **Log Output**: The output and any errors are logged to `/var/log/borg-backup.log` for easy monitoring.

### Step 5: Verify and Monitor Backups
- **Monitor Backup Status**: You can check the log file created by the cron job to see if the backup was successful:
  ```bash
  cat /var/log/borg-backup.log
  ```
- **Verify Backups**: Occasionally verify the integrity of your backups to ensure they are working correctly:
  ```bash
  borg check /mnt/desktop-backup/borg-repo
  ```

### Paths to Include or Exclude for Hardware Independence
To ensure your backup remains **hardware-agnostic** and can be restored on different hardware setups, it is important to include essential parts of the system while avoiding RAID or hardware-specific files. Below is a suggested list of paths to include and exclude:

**Paths to Include**:
- `/etc`: System configuration files.
- `/home`: User data and settings.
- `/var`: Logs and data. (Note: You may exclude specific directories within `/var` that are not important for restore, like `/var/tmp`.)
- `/usr/local`: Custom-installed software and scripts.
- `/root`: Root user’s home directory.
- `/opt`: Typically used for manually installed applications, including some AppImages.
- `/var/lib/flatpak`: Flatpak application files to ensure Flatpak apps are backed up.
- `/var/lib/snapd`: Snap application files to ensure Snap apps are backed up.
- `/usr/share/applications`: Desktop entry files, useful for app shortcuts.
- `/usr/share/icons`: Icons used by installed applications.
- Python packages in the user directory (`$(python3 -m site --user-base)/lib/python3.*/site-packages`): Ensures user-installed Python packages are included.

**Paths to Exclude**:
- `/dev`: Device files, dynamically generated.
- `/proc`: Kernel and process files, dynamically generated.
- `/sys`: System information, dynamically generated.
- `/tmp`: Temporary files.
- `/run`: Runtime files, dynamically generated.
- `/mnt` and `/media`: Mounted devices, excluding this prevents recursive backups and issues.
- `/lost+found`: Filesystem recovery data, generally not useful for backups.
- `/var/tmp`: Temporary files that are not necessary for a system restore.
- `/home/*/.cache`: User cache files, generally not needed for restoration.

**RAID Configuration**: Files such as `/etc/mdadm.conf` (used for RAID configurations) may be excluded if you plan to avoid RAID in your new hardware. However, if you want the option to recreate RAID, keep this file in the backup.

### Step 6: Restoring from the Backup
In the event that you need to restore from the backup, follow these steps:

1. **Mount the Borg Repository**:
   ```bash
   borg mount /mnt/desktop-backup/borg-repo /mnt/recovery
   ```
   This command will mount the backup so you can browse and selectively restore files.

2. **Restore Files**:
   Navigate to `/mnt/recovery` and copy the files you need back to their original locations:
   ```bash
   cp -a /mnt/recovery/etc /etc
   cp -a /mnt/recovery/home /home
   # Continue for other directories as needed.
   ```

3. **Unmount the Repository**:
   Once the restoration is complete, unmount the repository:
   ```bash
   borg umount /mnt/recovery
   ```

### Summary
- **Install Borg Backup** using `dnf`.
- **Initialize the Borg repository** on your external SSD.
- **Create a backup script** that includes key system paths while excluding unnecessary directories.
- **Set up a cron job** to run the backup script on a schedule.
- **Monitor backups** by checking logs and verifying repository integrity.

By following these steps, you will have a robust, **hardware-agnostic** backup of your Fedora system that can be easily restored or migrated to new hardware, regardless of RAID or other storage configurations. This provides peace of mind knowing your data is safe and easily retrievable in case of hardware failure or migration.

