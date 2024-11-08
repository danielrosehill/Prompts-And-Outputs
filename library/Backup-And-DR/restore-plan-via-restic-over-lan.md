---
title: "Restore plan via Restic over LAN"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here's a step-by-step guide on how to restore your Fedora computer from a Restic backup stored on your Ubuntu VM over the LAN. This guide assumes you've reinstalled Fedora on your system and are ready to restore data from the backup.

### Step 1: Reinstall Restic on Your Reinstalled Fedora
1. **Install Restic**:
   ```bash
   sudo dnf install restic
   ```

### Step 2: Set Up SSH Access to the Ubuntu VM
Since the backup is on the Ubuntu VM, you need to ensure you can access it via SSH.

1. **Generate SSH Keys (If Needed)**:
   If you don’t have SSH keys set up, you can generate them:
   ```bash
   ssh-keygen
   ```
   - Press **Enter** to accept the defaults.

2. **Copy SSH Key to Ubuntu VM**:
   ```bash
   ssh-copy-id daniel@192.168.1.1
   ```
   - This will allow you to access the server without needing a password each time.

3. **Test SSH Connection**:
   ```bash
   ssh daniel@192.168.1.1
   ```
   - Ensure you can connect without entering a password.

### Step 3: List Available Backups on the Ubuntu VM
Before restoring, you should verify which snapshots are available in the Restic repository.

1. **List Snapshots**:
   ```bash
   restic snapshots -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop
   ```
   - This will show all snapshots stored on the Ubuntu VM.

### Step 4: Choose How to Restore
You have a couple of options when restoring data:
1. **Full System Restore**: Restore all backed-up data to the system. This is useful for getting everything back, but be cautious if the new system has been partially configured or has important data.
2. **Selective Restore**: Restore specific directories or files. Useful if you only need to recover certain parts of your backup.

### Step 5: Full System Restore (Overwrite Current System)
1. **Prepare the System**:
   - Ensure there’s enough disk space available for the restore.
   - If you want to restore to the root directory `/`, make sure you boot from a live environment or have a backup method for overriding existing files.

2. **Run the Restore Command**:
   ```bash
   sudo restic restore latest -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop --target /
   ```
   - **`latest`**: Use the latest snapshot. You can replace this with a specific snapshot ID if needed.
   - **`--target /`**: Restores data to the root directory, effectively placing everything back as it was.

3. **Restart Your System**:
   ```bash
   sudo reboot
   ```

### Step 6: Selective Restore (Restore Specific Files or Directories)
If you only need to restore specific files or directories (e.g., `/home/daniel`), you can do so without affecting other parts of the system.

1. **Run the Selective Restore Command**:
   ```bash
   sudo restic restore latest -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop --target / --include /home/daniel
   ```
   - **`--include /home/daniel`**: Only restores the `/home/daniel` directory.

### Step 7: Verify the Restored Data
1. **Check the Restored Files**:
   After the restore, ensure all your files have been correctly restored by navigating through the directories and checking the contents.

2. **Verify Permissions**:
   Ensure that file permissions and ownership are correct, especially if you restored system files or configurations:
   ```bash
   ls -l /restored-directory
   ```

### Step 8: Clean Up
1. **Remove Unnecessary Files**:
   If there are files or directories that shouldn’t have been restored, you can manually remove them.
   ```bash
   sudo rm -rf /path/to/unwanted-files
   ```

### Step 9: Additional Steps if Restoring from a Live Environment
If you need to perform a full system restore from a live environment (because your main system is not bootable):
1. **Boot from a Fedora Live USB**:
2. **Mount the Root Filesystem**:
   ```bash
   sudo mount /dev/sdXn /mnt
   ```
   - Replace `/dev/sdXn` with the appropriate device identifier for your root partition.
3. **Restore to the Mounted Partition**:
   ```bash
   sudo restic restore latest -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop --target /mnt
   ```
4. **Chroot Into the Mounted Environment** (Optional):
   ```bash
   sudo chroot /mnt
   ```

### Recap:
- **Reinstall Restic**: Make sure Restic is available on your system.
- **Access the Backup Repository**: Ensure you can SSH to the Ubuntu VM.
- **Identify and Restore**: Choose whether to restore the entire system or specific files.
- **Verify and Reboot**: Ensure everything is working correctly after the restore.

By following this guide, you should be able to recover your Fedora system from a Restic backup stored on your Ubuntu VM over the LAN.