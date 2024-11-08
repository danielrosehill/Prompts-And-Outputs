---
title: "How to shrink VM drive using System Rescue"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Using **SystemRescue** to shrink the partition and filesystem on your **Ubuntu VM**'s disk, then reducing the size of the virtual disk in Proxmox, involves the following steps:

### Overview of the Process
1. **Boot into SystemRescue**.
2. **Shrink the filesystem** using `resize2fs`.
3. **Shrink the LVM logical volume** using `lvreduce`.
4. **Verify the changes**.
5. **Create a new smaller disk in Proxmox**.
6. **Copy the data** from the old disk to the new one.
7. **Configure the new disk as the boot disk**.

Let’s walk through each step:

---

### 1. **Boot into SystemRescue**

1. Download the **SystemRescue ISO** if you haven't already: [SystemRescue Download](https://www.system-rescue.org/Download/).
2. In Proxmox, go to your VM’s **Hardware** tab and mount the **SystemRescue ISO** as a CD/DVD device.
3. **Reboot the VM** and boot from the SystemRescue ISO:
   - In the Proxmox interface, go to **Options** > **Boot Order**, and set the CD/DVD drive as the first boot device.
   - Start the VM and press any key if prompted to boot from the ISO.
   
Once booted, you’ll be in the **SystemRescue terminal**.

---

### 2. **Shrink the Filesystem**

#### Check the filesystem:
First, verify the partitions and filesystems:
```bash
lsblk
```
You should see your logical volume (e.g., `/dev/mapper/ubuntu--vg-ubuntu--lv`).

1. **Check filesystem integrity** before resizing:
   ```bash
   e2fsck -f /dev/mapper/ubuntu--vg-ubuntu--lv
   ```

2. **Resize the filesystem**:
   - To shrink the filesystem to 90 GB (or adjust the size according to your needs):
     ```bash
     resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv 90G
     ```

   - You can also specify slightly less than your target disk size to leave some buffer room (e.g., 90 GB if your target is 100 GB).

---

### 3. **Shrink the LVM Logical Volume**

1. **Reduce the logical volume** to match the resized filesystem:
   ```bash
   lvreduce -L 95G /dev/mapper/ubuntu--vg-ubuntu--lv
   ```
   This reduces the logical volume to **95 GB**, slightly larger than the filesystem.

2. **Check the new logical volume size**:
   ```bash
   lvdisplay
   ```

   Ensure the size reflects the new target (e.g., 95 GB).

---

### 4. **Verify the Changes**

1. **Resize the filesystem to fill the logical volume** (as a precaution):
   ```bash
   resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
   ```

2. **Check the disk usage**:
   ```bash
   df -h
   ```
   Ensure the filesystem has been resized to the new, smaller size (under 100GB).

---

### 5. **Create a New Smaller Disk in Proxmox**

1. **Shutdown the VM** from SystemRescue.
2. In **Proxmox**, add a new smaller disk (100GB):
   - Go to the VM's **Hardware** tab.
   - Click **Add** > **Hard Disk**.
   - Choose the storage, and set the disk size to **100GB**.
   - **Add** the disk.

3. **Boot the VM back into SystemRescue**.

---

### 6. **Copy the Data from the Old Disk to the New Disk**

1. **Partition the new disk**:
   - Use `fdisk` to create a partition on the new disk (e.g., `/dev/sdb`):
     ```bash
     fdisk /dev/sdb
     ```
   - Create a new partition with the full 100GB size.

2. **Format the new partition** as ext4:
   ```bash
   mkfs.ext4 /dev/sdb1
   ```

3. **Mount both the old and new partitions**:
   - Mount the new disk:
     ```bash
     mkdir /mnt/newdisk
     mount /dev/sdb1 /mnt/newdisk
     ```
   - Mount the old disk:
     ```bash
     mkdir /mnt/olddisk
     mount /dev/mapper/ubuntu--vg-ubuntu--lv /mnt/olddisk
     ```

4. **Copy data from the old disk to the new disk**:
   - Use `rsync` to copy the contents of the old disk to the new one:
     ```bash
     rsync -aAXv /mnt/olddisk/ /mnt/newdisk/ --exclude=/mnt
     ```

   This will copy all the files from the old root partition to the new one.

---

### 7. **Configure the New Disk as the Boot Disk**

1. **Update the UUIDs**:
   - Get the **UUID** of the new disk using:
     ```bash
     blkid
     ```
   - Edit `/mnt/newdisk/etc/fstab` to update the root partition’s UUID to the new one (use a text editor like `nano` or `vim`).

2. **Install GRUB on the new disk**:
   - Bind-mount necessary filesystems to the new root:
     ```bash
     mount --bind /dev /mnt/newdisk/dev
     mount --bind /proc /mnt/newdisk/proc
     mount --bind /sys /mnt/newdisk/sys
     ```
   - Chroot into the new disk:
     ```bash
     chroot /mnt/newdisk
     ```
   - Install GRUB on the new disk:
     ```bash
     grub-install /dev/sdb  # Replace sdb with the new disk
     update-grub
     ```

3. **Exit the chroot environment**:
   ```bash
   exit
   ```

4. **Shutdown the VM**, go to **Proxmox** and change the boot order:
   - Go to **Options** > **Boot Order**, and set the new disk as the primary boot device.

5. **Boot the VM** from the new disk and verify that everything works as expected.

---

### 8. **Remove the Old Disk**
Once you've verified that the new smaller disk works fine, you can remove the old 2TB disk from the VM in Proxmox:
- Go to **Hardware**.
- Select the old disk and click **Remove**.

---

### Summary of the Process:
1. Boot into **SystemRescue**.
2. Shrink the **filesystem** and **LVM logical volume**.
3. Create a new, smaller disk in Proxmox (100GB).
4. Copy data from the old disk to the new disk.
5. Configure the new disk as the boot disk and remove the old 2TB disk.

This process avoids having to directly resize the original disk and ensures you retain a working copy of your data throughout.

Let me know if you need further details or assistance at any step!