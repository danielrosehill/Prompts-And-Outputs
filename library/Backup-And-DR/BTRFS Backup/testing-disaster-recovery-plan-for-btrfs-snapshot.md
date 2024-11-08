---
title: "Testing disaster recovery plan for BTRFS snapshot"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt summary:** You want a disaster recovery plan where you have a Btrfs snapshot backup, and you've reinstalled Fedora on new hardware. Now you need to restore that snapshot from your SSD to recover your files.

Here’s a step-by-step disaster recovery plan to restore your system from a Btrfs snapshot backup after reinstalling Fedora on new hardware.

---

## **Disaster Recovery Plan: Restoring Btrfs Snapshot on New Fedora Installation**

### **Prerequisites:**
- **Btrfs snapshot** stored on your external SSD.
- **Fresh installation of Fedora** (or any Linux distribution with Btrfs support).
- **Access to the external SSD** where your backup is stored.
- **Sufficient disk capacity** on the new hardware (equal to or greater than the original size).

---

### **Step 1: Prepare the System**

1. **Boot into the Fedora installation** you’ve performed on the new hardware.
   - Ensure that Btrfs is installed and supported by the kernel.
   - If necessary, install the `btrfs-progs` package:
     ```bash
     sudo dnf install btrfs-progs
     ```

2. **Mount the external SSD** that contains the snapshot backup.
   - Assuming the SSD is at `/dev/sdc1`:
     ```bash
     sudo mkdir -p /mnt/backup
     sudo mount /dev/sdc1 /mnt/backup
     ```

3. **Identify the Snapshot Directory** on your backup drive.
   - Check where the snapshots are stored, for example:
     ```bash
     ls /mnt/backup/snapshots
     ```

   You should see directories like `root_snapshot_DATE` and possibly `home_snapshot_DATE`.

---

### **Step 2: Prepare the New Filesystem for Restoration**

1. **Check Subvolume Setup**:
   - On the new Fedora installation, verify the subvolume setup. Fedora typically uses subvolumes like `@` for root and `@home` for the home directory.
   ```bash
   sudo btrfs subvolume list /
   ```

   You should see the root and home subvolumes listed.

2. **Create New Subvolumes for Restoration**:
   - If your snapshot backup uses subvolumes for root and home, recreate them on the new installation:
     ```bash
     sudo btrfs subvolume create /mnt/new-root
     sudo btrfs subvolume create /mnt/new-home
     ```

   This will provide a location to receive the Btrfs snapshots.

---

### **Step 3: Restore the Btrfs Snapshot**

1. **Restore the Root Filesystem Snapshot**:
   - Use `btrfs receive` to restore the root subvolume snapshot:
     ```bash
     sudo btrfs receive /mnt/new-root < /mnt/backup/snapshots/root_snapshot_DATE
     ```

   This command will restore the backup from the external SSD to the new root subvolume (`/mnt/new-root`).

2. **Restore the Home Directory Snapshot** (if applicable):
   - If you have a separate snapshot for `/home`, restore it similarly:
     ```bash
     sudo btrfs receive /mnt/new-home < /mnt/backup/snapshots/home_snapshot_DATE
     ```

   This will recover your user data (dotfiles, configurations, personal files).

3. **Verify the Restoration**:
   - Confirm that the snapshots have been properly restored by checking the files in `/mnt/new-root` and `/mnt/new-home`:
     ```bash
     ls /mnt/new-root
     ls /mnt/new-home
     ```

---

### **Step 4: Reinstall the Bootloader**

Since the Btrfs snapshot restore doesn't include the bootloader, you’ll need to reinstall the bootloader (GRUB) on the new hardware.

1. **Chroot into the New Root**:
   - Mount necessary directories:
     ```bash
     sudo mount --bind /mnt/new-root /mnt
     sudo mount --bind /dev /mnt/dev
     sudo mount --bind /proc /mnt/proc
     sudo mount --bind /sys /mnt/sys
     ```

   - Chroot into the newly restored system:
     ```bash
     sudo chroot /mnt
     ```

2. **Reinstall GRUB**:
   - Reinstall GRUB for your new system, specifying the correct disk (adjust `sdX` to match your system’s boot disk):
     ```bash
     grub2-install /dev/sdX
     ```

   - Regenerate the GRUB configuration:
     ```bash
     grub2-mkconfig -o /boot/grub2/grub.cfg
     ```

3. **Exit the Chroot** and unmount the directories:
   ```bash
   exit
   sudo umount /mnt/dev /mnt/proc /mnt/sys
   sudo umount /mnt
   ```

---

### **Step 5: Final System Configuration and Adjustments**

1. **Fstab Configuration**:
   - After restoring the snapshot, you may need to adjust `/etc/fstab` in the restored system to match the UUIDs of the new disks. Find the new UUIDs of your disks:
     ```bash
     blkid
     ```

   - Then, update the UUID entries in `/mnt/new-root/etc/fstab` to reflect the new environment.

2. **Hardware-Specific Drivers**:
   - If the hardware has changed significantly, you may need to install additional drivers or firmware for the new hardware after restoration.

3. **Reboot**:
   - After completing the restoration and configuring the system, reboot your machine:
     ```bash
     sudo reboot
     ```

---

### **Step 6: Post-Restoration Tasks**

1. **Test System Functionality**:
   - Ensure that the system boots properly and that your files and applications are restored correctly.
   - Check for any system services that may need reconfiguration (e.g., networking or hardware-specific services).

2. **Verify Backup Integrity**:
   - Go through your critical files and programs to ensure everything was restored properly and functions as expected.

---

### **Summary of Commands:**

1. **Mount the backup drive**:
   ```bash
   sudo mkdir -p /mnt/backup
   sudo mount /dev/sdc1 /mnt/backup
   ```

2. **Create subvolumes for restoration**:
   ```bash
   sudo btrfs subvolume create /mnt/new-root
   sudo btrfs subvolume create /mnt/new-home
   ```

3. **Restore snapshots**:
   ```bash
   sudo btrfs receive /mnt/new-root < /mnt/backup/snapshots/root_snapshot_DATE
   sudo btrfs receive /mnt/new-home < /mnt/backup/snapshots/home_snapshot_DATE
   ```

4. **Chroot and reinstall GRUB**:
   ```bash
   sudo mount --bind /mnt/new-root /mnt
   sudo mount --bind /dev /mnt/dev
   sudo mount --bind /proc /mnt/proc
   sudo mount --bind /sys /mnt/sys
   sudo chroot /mnt
   grub2-install /dev/sdX
   grub2-mkconfig -o /boot/grub2/grub.cfg
   exit
   sudo umount /mnt/dev /mnt/proc /mnt/sys
   sudo umount /mnt
   ```

5. **Update `/etc/fstab` and reboot**:
   ```bash
   blkid
   sudo reboot
   ```

---

This disaster recovery plan will allow you to restore as much of your Fedora system as possible using the Btrfs snapshots, while ensuring compatibility with new hardware. You'll be able to recover the majority of your files and configurations, with minimal reconfiguration needed after restoration.