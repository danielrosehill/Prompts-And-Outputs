---
title: "Guide to move the data to the new drive in VM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Great! Since we’ve confirmed that **`sda3`** is the existing drive and **`sdb`** is the new, unpartitioned 100GB disk, let's resume the guide from **Step 8** where we will partition and format the new disk, then copy the data over.

### Step 8: Partition and Format the New Disk

1. **Partition the New Disk (`sdb`)**:

   We'll create a single partition on the new disk (`sdb`), which will take up the entire 100GB of space.

   - Start the `fdisk` utility to partition the disk:
     ```bash
     fdisk /dev/sdb
     ```

   - Once inside `fdisk`, use the following steps:
     - **`n`** to create a new partition.
     - **`p`** to make it a primary partition.
     - Accept defaults for the **partition number** (likely `1`), **first sector**, and **last sector** to use the full disk space.
     - **`w`** to write the partition table and exit.

2. **Format the New Partition**:

   Now that the partition (`/dev/sdb1`) is created, you need to format it as **ext4** to prepare it for data transfer.

   - Format the partition:
     ```bash
     mkfs.ext4 /dev/sdb1
     ```

   This command creates an **ext4** filesystem on `/dev/sdb1`.

### Step 9: Mount the Old and New Partitions

1. **Mount the New Disk (`/dev/sdb1`)**:
   - Create a mount point for the new disk:
     ```bash
     mkdir /mnt/newdisk
     ```
   - Mount the new disk:
     ```bash
     mount /dev/sdb1 /mnt/newdisk
     ```

2. **Mount the Old Disk (`/dev/mapper/ubuntu--vg-ubuntu--lv`)**:
   - Create a mount point for the old disk:
     ```bash
     mkdir /mnt/olddisk
     ```
   - Mount the old disk (logical volume):
     ```bash
     mount /dev/mapper/ubuntu--vg-ubuntu--lv /mnt/olddisk
     ```

### Step 10: Copy Data from the Old Disk to the New Disk

To ensure that all data is copied correctly, we'll use `rsync` to transfer the files from the old disk to the new one.

- Use the following `rsync` command to copy the data from `/mnt/olddisk` (your current root filesystem) to `/mnt/newdisk`:
  ```bash
  rsync -aAXv /mnt/olddisk/ /mnt/newdisk/ --exclude=/mnt --exclude=/proc --exclude=/sys --exclude=/dev --exclude=/tmp
  ```

   - **`-aAXv`**: Ensures all data, including permissions and special files, are copied.
   - **Exclusions**: We exclude certain directories that don’t need to be copied (like `/mnt`, `/proc`, `/sys`, etc.).

### Step 11: Update `fstab` on the New Disk

Now that the data is copied over, we need to update the new disk's **`fstab`** file to point to its own UUID (instead of the old disk's UUID).

1. **Get the UUID of the New Disk**:
   - Use the following command to get the UUID of the new partition (`/dev/sdb1`):
     ```bash
     blkid /dev/sdb1
     ```

   - The output will look something like this:
     ```
     /dev/sdb1: UUID="1234abcd-56ef-78gh-90ij-1234567890kl" TYPE="ext4"
     ```

   - Copy the UUID value.

2. **Edit `fstab` on the New Disk**:
   - Open the **`fstab`** file on the new disk for editing:
     ```bash
     nano /mnt/newdisk/etc/fstab
     ```

   - In the file, replace the old UUID (from the old root partition) with the new UUID you copied for `/dev/sdb1`.
     For example, replace something like:
     ```
     UUID=old-uuid-here / ext4 defaults 0 1
     ```
     with:
     ```
     UUID=1234abcd-56ef-78gh-90ij-1234567890kl / ext4 defaults 0 1
     ```

   - Save the changes and exit the editor.

### Step 12: Install GRUB on the New Disk

1. **Mount necessary filesystems** for the chroot environment:
   ```bash
   mount --bind /dev /mnt/newdisk/dev
   mount --bind /proc /mnt/newdisk/proc
   mount --bind /sys /mnt/newdisk/sys
   ```

2. **Change root to the new disk**:
   ```bash
   chroot /mnt/newdisk
   ```

3. **Install GRUB on the new disk**:
   - Install GRUB to the new disk (`/dev/sdb`):
     ```bash
     grub-install /dev/sdb
     ```

4. **Update the GRUB configuration**:
   - After installing GRUB, update the GRUB configuration to reflect the changes:
     ```bash
     update-grub
     ```

5. **Exit the chroot environment**:
   ```bash
   exit
   ```

6. **Unmount the filesystems**:
   ```bash
   umount /mnt/newdisk/dev /mnt/newdisk/proc /mnt/newdisk/sys
   ```

### Step 13: Set the New Disk as the Boot Disk

1. **Shutdown the VM**:
   - Use the shutdown command from the **SystemRescue** environment:
     ```bash
     shutdown now
     ```

2. **Set the New Disk to Boot**:
   - In Proxmox, go to the VM's **Options** > **Boot Order** and set the new disk (`sdb`) as the primary boot device.

### Step 14: Boot and Verify the System

1. **Start the VM** and ensure it boots correctly from the new 100GB disk.
2. Once the VM has booted, verify everything is working properly by checking that the root filesystem is now on the new 100GB disk:
   ```bash
   df -h
   ```

   You should see the root partition (`/`) now on the 100GB disk (`/dev/sdb1`).

### Step 15: Remove the Old 2TB Disk

Once you’ve confirmed that everything is working properly, you can remove the old 2TB disk:

1. **Shutdown the VM**.
2. In Proxmox, go to the **Hardware** tab of the VM.
3. Select the old **2TB disk (sda)** and click **Remove** to free up the space.

---

### Conclusion:
At this point, you’ve successfully:
1. Created a new 100GB disk.
2. Partitioned, formatted, and copied the data from the old disk.
3. Updated the `fstab` and installed GRUB on the new disk.
4. Booted from the new disk and removed the old 2TB disk.

Let me know if you encounter any issues or if you'd like further clarification!