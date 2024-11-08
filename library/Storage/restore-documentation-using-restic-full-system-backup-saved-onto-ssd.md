---
title: "Restore documentation using Restic full system backup saved onto SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Restoring Fedora Workstation from Restic Backup on SSD

This guide will help you restore your Fedora workstation from the Restic backup you have created on your external SSD. We assume that your system has crashed and you've just reinstalled Fedora on the same storage. Follow these steps to use your backup to restore your previous configuration as fully as possible.

### Prerequisites
- Fedora is freshly reinstalled on your system.
- Your external SSD containing the Restic backup is connected and mounted.
- You remember the password for the Restic repository.

### Step 1: Install Restic
First, reinstall Restic on your new Fedora system. Open a terminal and run:
```bash
sudo dnf install restic
```
This will install Restic and its required dependencies.

### Step 2: Mount the SSD
Ensure the SSD is mounted at the location you originally used for your backup (e.g., `/mnt/desktop-backups`). If not already mounted, do so:
```bash
sudo mkdir -p /mnt/desktop-backups
sudo mount /dev/sdX1 /mnt/desktop-backups  # Replace sdX1 with the appropriate device identifier.
```
To determine the correct device identifier for your SSD, use:
```bash
lsblk
```
### Step 3: Verify Restic Repository
Navigate to the location of the Restic backup repository on your SSD to confirm its existence and integrity. You can list the contents of the backup repository to verify:
```bash
restic snapshots -r /mnt/desktop-backups
```
- Enter your repository password when prompted.
- This will display all the backup snapshots you have available.

### Step 4: Select Snapshot and Start Restoration
To restore the entire system from the most recent snapshot, run the following command:
```bash
sudo restic restore latest -r /mnt/desktop-backups --target /
```
- **`latest`**: Specifies the most recent snapshot.
- **`--target /`**: Restores the files to the root directory.

This command will restore your files and directories to their original locations, overwriting the freshly installed system.

### Step 5: Restore Specific Directories (Optional)
If you only want to restore specific parts of the system (e.g., your `/home` directory), you can use the `--include` option:
```bash
sudo restic restore latest -r /mnt/desktop-backups --target / --include /home/daniel
```
- Replace `/home/daniel` with the path of the directory you wish to restore.

### Step 6: Verify Restored Files
After the restoration, verify that your files have been restored properly:
- Navigate to key locations, such as `/home/`, and verify that your personal files are present.
- You may need to adjust permissions, especially if restoring system files, to ensure all applications work as expected.

### Step 7: Reinstall Applications and System Configuration
The backup restores your files, but you may still need to:
1. **Reinstall Software**: Install the software that was not part of the fresh installation using `dnf` or another package manager.
   - You may have a list of installed applications in your backup. If so, you can use it to reinstall:
   ```bash
   xargs sudo dnf install -y < package-list.txt
   ```
2. **Restore Configurations**: Configuration files (such as those in `/etc`) may require manual adjustment to work with the new installation. Be cautious with system-level configurations to avoid conflicts.

### Step 8: Restore Bootloader (If Needed)
If the restored system files include critical bootloader configurations, you may need to reinstall and update the bootloader:
1. **Chroot into the System**:
   ```bash
   sudo chroot /
   ```
2. **Reinstall GRUB** (assuming an EFI system):
   ```bash
   grub2-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Fedora
   grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
   ```
3. **Exit chroot**:
   ```bash
   exit
   ```

### Step 9: Post-Restoration Checks
- **Test System Functionality**: Reboot your system and check that all services and programs work as expected.
- **User Permissions**: Ensure that user permissions, particularly for your home directories, are correct. Use `chown` if necessary:
  ```bash
  sudo chown -R daniel:daniel /home/daniel
  ```
- **Review Restored Files**: Double-check that everything you need has been restored, particularly personal data and configuration files.

### Notes
- **File Conflicts**: Be aware that restoring system files onto a freshly installed system may create conflicts if version mismatches exist between configuration files and newly installed software. Always review and merge configurations carefully.
- **Password**: Make sure you have the Restic repository password. Without it, you cannot decrypt and restore the backup.

### Summary
- **Install Restic** and **mount the SSD** containing the backup.
- **Restore files** either entirely or selectively from the snapshot.
- **Reinstall applications** and verify configurations to return your system to the previous working state.

By following these steps, you should be able to restore your Fedora workstation as fully as possible using your Restic backup on the SSD.

