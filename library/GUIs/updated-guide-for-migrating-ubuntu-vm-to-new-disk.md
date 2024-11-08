---
title: "Updated guide for migrating Ubuntu VM to new disk"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Certainly! Let's pick up the process **after the `rsync`** operation has completed and all data has been copied from the old disk to the new one. Now, we need to finalize the transition by ensuring the new disk is bootable and the system can properly boot from it. Here's a step-by-step guide:

### 1. **Update `fstab` on the New Disk**

Now that the data has been copied to the new disk, you need to update the **`fstab`** file on the new disk to reflect the correct UUID of the new partition.

1. **Get the UUID of the New Disk**:
   - Run the following command to get the UUID of the new partition (`/dev/sdb1`):
     ```bash
     blkid /dev/sdb1
     ```

   - The output should look something like this:
     ```
     /dev/sdb1: UUID="1234abcd-56ef-78gh-90ij-1234567890kl" TYPE="ext4"
     ```

2. **Edit the `fstab` on the New Disk**:
   - Open the `fstab` file on the new disk for editing:
     ```bash
     nano /mnt/newdisk/etc/fstab
     ```

   - Look for the line that references the old root partition UUID (usually for `/`) and replace it with the new UUID from the `blkid` command.

   For example, replace something like this:
   ```
   UUID=old-uuid-here / ext4 defaults 0 1
   ```
   with:
   ```
   UUID=1234abcd-56ef-78gh-90ij-1234567890kl / ext4 defaults 0 1
   ```

3. **Save the changes** and exit the editor (`Ctrl + O`, then `Enter`, then `Ctrl + X`).

### 2. **Install GRUB on the New Disk**

Next, you need to install **GRUB** (the bootloader) on the new disk so that the system can boot from it.

1. **Mount necessary filesystems** for the chroot environment:
   - Bind-mount the essential directories into the new root filesystem:
     ```bash
     mount --bind /dev /mnt/newdisk/dev
     mount --bind /proc /mnt/newdisk/proc
     mount --bind /sys /mnt/newdisk/sys
     ```

2. **Chroot into the new disk**:
   - Change root into the new disk so you can operate on it as if it's the root filesystem:
     ```bash
     chroot /mnt/newdisk
     ```

3. **Install GRUB on the new disk**:
   - Install GRUB to the new disk (`/dev/sdb` in this case):
     ```bash
     grub-install /dev/sdb
     ```

4. **Update GRUB configuration**:
   - After installing GRUB, update the configuration to ensure everything is recognized:
     ```bash
     update-grub
     ```

5. **Exit the chroot environment**:
   - Once GRUB is installed, exit the chroot environment:
     ```bash
     exit
     ```

6. **Unmount the filesystems**:
   - Unmount the directories that were bound earlier:
     ```bash
     umount /mnt/newdisk/dev /mnt/newdisk/proc /mnt/newdisk/sys
     ```

### 3. **Shutdown the VM**

Once everything is set up, it's time to shut down the VM so you can configure the boot order in Proxmox.

1. **Shutdown the VM**:
   ```bash
   shutdown now
   ```

### 4. **Set the New Disk as the Boot Disk in Proxmox**

Now that the new disk is ready to boot from, you need to set it as the primary boot device in **Proxmox**.

1. **Open the Proxmox Web UI**:
   - Go to the **Hardware** tab for your VM.

2. **Set the New Disk as the Boot Disk**:
   - Go to the **Options** tab and find the **Boot Order** setting.
   - Ensure that the new disk (`sdb` or its Proxmox equivalent) is set as the first boot device.
   - You can uncheck the old disk to make sure it doesn’t try to boot from it.

### 5. **Start the VM and Verify the System**

1. **Start the VM**:
   - Boot the VM from the new disk.

2. **Verify that the VM is Booting from the New Disk**:
   - Once the VM has booted, run the following command to confirm that the root filesystem is on the new 100GB disk (`/dev/sdb1`):
     ```bash
     df -h
     ```

   - You should see that the root partition (`/`) is now on the new disk (`/dev/sdb1`), and the disk size is around 100GB.

### 6. **Remove the Old 2TB Disk**

Once you're sure the VM is booting properly from the new disk and everything is working as expected, you can remove the old 2TB disk to free up space.

1. **Shutdown the VM**:
   - Shut down the VM again to safely remove the old disk.

2. **Remove the Old Disk in Proxmox**:
   - Go to the **Hardware** tab in Proxmox.
   - Select the old 2TB disk (`/dev/sda`) and click **Remove** to detach and delete it from the VM.
   
   This will free up the 2TB of space on your Proxmox host.

3. **Start the VM** again to ensure everything works fine without the old disk attached.

### Summary of Post-`rsync` Steps:
1. **Update `fstab`** on the new disk with the correct UUID.
2. **Install GRUB** on the new disk.
3. **Shutdown the VM** and set the new disk as the boot disk in Proxmox.
4. **Verify** the system is booting from the new disk.
5. **Remove the old 2TB disk** from Proxmox.

With these steps completed, you will have successfully migrated from the old 2TB disk to the new 100GB disk.

Let me know if you encounter any issues or need further clarification on any of the steps!