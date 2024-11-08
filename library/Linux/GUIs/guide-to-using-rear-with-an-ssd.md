---
title: "Guide to using REAR with an SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you write me a guide on how to setup rear for creating a bootable backup of my operating system? The backup target is an SSD at /mnt/desktop-backups. So it's important that /mnt be excluded when creating the backup. I'd like the backup and recovery medium to be one and the same (the SSD)?

# Output

# Setting Up Relax-and-Recover (ReaR) to Create a Bootable Backup on an SSD

This guide will help you set up **Relax-and-Recover (ReaR)** to create a bootable backup of your Fedora system. The backup will be stored on an external SSD mounted at `/mnt/desktop-backups`. We will also ensure that `/mnt` is excluded during the backup, and the SSD will function as both the backup target and recovery medium.

### Prerequisites
- Fedora is installed on your system.
- An external SSD is mounted at `/mnt/desktop-backups`.
- Sufficient storage on the SSD to store your entire system.
- Root privileges on the system.

### Step 1: Install ReaR
First, you need to install ReaR. Open a terminal and run the following command:

```bash
sudo dnf install rear
```

### Step 2: Configure ReaR
ReaR uses a configuration file located at `/etc/rear/local.conf` to determine how to back up your system. We will edit this file to match your setup.

1. **Open the Configuration File**:

   ```bash
   sudo nano /etc/rear/local.conf
   ```

2. **Add the Following Configuration**:

   ```bash
   # Basic ReaR Configuration
   OUTPUT=ISO
   BACKUP=NETFS
   BACKUP_URL=file:///mnt/desktop-backups
   EXCLUDE_MOUNTPOINTS=( '/mnt' )

   # Create a Bootable Recovery ISO
   OUTPUT_URL=file:///mnt/desktop-backups

   # Ensure Grub and EFI Settings Are Backed Up
   GRUB_RESCUE=1
   ``
   
   - **OUTPUT=ISO**: Specifies that the output should be a bootable ISO image.
   - **BACKUP=NETFS**: This instructs ReaR to use filesystem-level backups.
   - **BACKUP_URL=file:///mnt/desktop-backups**: Specifies that the backup should be saved to the external SSD.
   - **EXCLUDE_MOUNTPOINTS=( '/mnt' )**: Ensures that the `/mnt` directory is excluded from the backup to avoid a recursive backup issue.
   - **OUTPUT_URL=file:///mnt/desktop-backups**: This makes sure that the bootable ISO is also saved to the external SSD so that it can be used as recovery media.
   - **GRUB_RESCUE=1**: Ensures that GRUB and EFI settings are saved, making the recovery medium bootable.

3. **Save and Close the File**: Press `CTRL + O` to save and `CTRL + X` to exit.

### Step 3: Create the Bootable Backup
Now that the configuration is in place, you can use ReaR to create the bootable backup.

1. **Create the Recovery ISO and Backup**:

   Run the following command to start the backup process:
   
   ```bash
   sudo rear mkbackup
   ```

   - This command will create a full backup of your system (excluding `/mnt`) and will create a bootable ISO image that is saved directly to `/mnt/desktop-backups` on your SSD.
   - Depending on the size of your system, this process may take some time.

2. **Verify the Backup**:

   Once the process is complete, navigate to `/mnt/desktop-backups` and verify that you see both the backup files and an ISO image. The ISO is the bootable recovery medium that you will use to restore the system if needed.

### Step 4: Test the Bootable Backup
To make sure the recovery media works, it's a good idea to test booting from the ISO.

1. **Prepare to Boot from the SSD**:
   - Restart your computer and enter your BIOS or UEFI settings (usually by pressing `F2`, `DEL`, or `ESC` during startup).
   - Change the boot order so that the external SSD is selected as the first boot device.

2. **Boot into Recovery Environment**:
   - Once booted, you should be presented with the ReaR recovery menu.
   - From here, you can proceed with the recovery process or exit to confirm that the bootable media is functional.

### Step 5: Restoring Your System
If your original system becomes unusable, you can restore it using the ReaR backup.

1. **Boot from the SSD**: Plug in your external SSD and boot into the ReaR recovery environment, as described in the previous step.

2. **Restore the Backup**:
   - In the ReaR menu, select the option to **recover** the system.
   - ReaR will locate the backup stored on the SSD and begin the restoration process.
   - Follow the on-screen prompts to proceed. The tool will recreate your partitions and restore all of the backed-up data to your new or repaired hardware.

### Notes
- **Make Sure the SSD is Always Properly Mounted**: Before running the backup command (`rear mkbackup`), ensure that your SSD is mounted at `/mnt/desktop-backups`.
- **Recovery Medium Limitations**: Since the SSD serves as both backup storage and recovery medium, make sure there is enough storage capacity to hold all of your data plus the recovery ISO.
- **Test Regularly**: It’s a good practice to test your recovery process periodically to ensure that you can successfully restore your system if needed.

### Summary
1. **Install ReaR** using `dnf`.
2. **Configure ReaR** in `/etc/rear/local.conf` to specify the backup and exclude `/mnt`.
3. **Create a Bootable Backup** using the `rear mkbackup` command.
4. **Test the Recovery Medium** by booting from the SSD.
5. Use the recovery environment to **restore your system** when necessary.

By following these steps, you'll have a reliable, bootable backup of your Fedora system on an SSD that can also function as recovery media, providing a straightforward recovery path if your system ever fails.

