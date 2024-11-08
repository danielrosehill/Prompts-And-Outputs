---
title: "Copying data from logical volume"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The error you encountered (`unknown filesystem type LVM2_member`) indicates that you're trying to mount a **Logical Volume (LVM)** directly, but LVM volumes need to be handled a bit differently compared to regular partitions.

Here's how you can properly mount an **LVM** volume:

### 1. **Activate the LVM Volumes**
Before you can mount an LVM partition, you need to activate the volume group and logical volumes. Here's how you can do that:

1. **Activate the LVM Volume Group**:
   - First, list the available volume groups to see what's on the disk:
     ```bash
     vgscan
     ```
   - Once you’ve identified the volume group name (e.g., `ubuntu-vg`), activate it:
     ```bash
     vgchange -ay
     ```

2. **List Logical Volumes**:
   - After activating the volume group, list the logical volumes:
     ```bash
     lvscan
     ```

   This will show the available logical volumes and their paths (e.g., `/dev/ubuntu-vg/ubuntu-lv`).

### 2. **Mount the Logical Volume**

Once the logical volumes are activated, you can mount the root logical volume (usually named something like `ubuntu--vg-ubuntu--lv`).

1. **Create a mount point**:
   ```bash
   mkdir /mnt/olddisk
   ```

2. **Mount the logical volume**:
   - Replace `/dev/ubuntu-vg/ubuntu-lv` with the actual logical volume path you saw in the previous command:
     ```bash
     mount /dev/ubuntu-vg/ubuntu-lv /mnt/olddisk
     ```

   This should now mount your root filesystem properly.

### 3. **Proceed with the Data Copy**

Once you’ve successfully mounted the old LVM volume, you can proceed with **Step 10** from the earlier instructions:

- **Mount the new disk** (if not done already):
  ```bash
  mkdir /mnt/newdisk
  mount /dev/sdb1 /mnt/newdisk
  ```

- **Copy the data** from the old LVM volume to the new disk:
  ```bash
  rsync -aAXv /mnt/olddisk/ /mnt/newdisk/ --exclude=/mnt --exclude=/proc --exclude=/sys --exclude=/dev --exclude=/tmp
  ```

Let me know if you run into any issues while mounting the logical volume or need further clarification!