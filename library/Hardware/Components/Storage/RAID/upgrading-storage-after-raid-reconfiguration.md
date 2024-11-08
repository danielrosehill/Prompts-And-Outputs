---
title: "Upgrading storage after RAID reconfiguration"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. I'm now running a RAID1 filesystem with 3 drives: 1 x NVME, 2 x  SSD. Each 1 TB in sizes. Let's say that I want to upgrade my capacity. How would I go about doing that?

# Output

Upgrading the capacity of a **Btrfs RAID1 filesystem** with three drives (1 x NVMe, 2 x SSD) is a relatively straightforward process thanks to the flexibility of Btrfs. Here’s how you can expand your storage by adding or replacing drives while maintaining RAID1 redundancy.

### Option 1: **Adding New Drives to the RAID**

If you want to **increase capacity** by simply adding more drives to your RAID setup, follow these steps:

#### Steps to Add Drives:
1. **Add the New Drive**:
   - Physically connect the new drive to your system (let's assume you're adding another SSD or NVMe drive).
   - Format the new drive if it hasn’t been initialized yet.

2. **Add the New Drive to the Btrfs Filesystem**:
   Use the following command to add the new drive to your Btrfs filesystem:
   
   ```bash
   sudo btrfs device add /dev/sdX /mount/point
   ```

   Replace `/dev/sdX` with the actual device name of your new drive (e.g., `/dev/nvme1n1` or `/dev/sdb`), and `/mount/point` with the mount point of your Btrfs filesystem (e.g., `/mnt/data`).

3. **Rebalance the RAID to Use the New Drive**:
   After adding the new drive, you need to rebalance the RAID1 filesystem so that Btrfs can redistribute the data across all the drives, utilizing the new capacity:

   ```bash
   sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /mount/point
   ```

   This command will rebalance both **data** and **metadata** in RAID1 mode, spreading the data across the new and existing drives.

4. **Check the Status**:
   You can monitor the status of the balance operation by running:
   
   ```bash
   sudo btrfs balance status /mount/point
   ```

Once the rebalance is complete, your Btrfs filesystem will use the additional space provided by the new drive, maintaining RAID1 redundancy.

---

### Option 2: **Replacing an Existing Drive with a Larger One**

If you prefer to **replace** one or more of your existing 1 TB drives with larger ones (say, 2 TB drives), follow these steps:

#### Steps to Replace Drives:
1. **Add the New Larger Drive**:
   - First, physically connect the new larger drive (e.g., a 2 TB SSD or NVMe) to your system.

2. **Add the New Drive to the RAID**:
   Use the same command as before to add the new drive:

   ```bash
   sudo btrfs device add /dev/sdX /mount/point
   ```

   Where `/dev/sdX` is the new drive.

3. **Remove the Old Drive**:
   Once the new drive has been added, you can remove one of the existing drives (say, one of the 1 TB SSDs). Btrfs will automatically rebalance the data before removing the drive.

   ```bash
   sudo btrfs device remove /dev/sdY /mount/point
   ```

   Replace `/dev/sdY` with the device name of the drive you want to remove.

4. **Rebalance the RAID**:
   After replacing the drive, rebalance the filesystem to distribute the data across the new set of drives:

   ```bash
   sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /mount/point
   ```

   The system will now utilize the extra capacity of the new larger drive.

5. **Repeat for Other Drives**:
   If you plan to replace other drives with larger ones, repeat this process for each of the remaining 1 TB drives until they are all upgraded.

---

### Option 3: **Mix of Adding and Replacing Drives**

You can also combine **adding new drives** and **replacing old drives** if you want to further scale your storage or mix SSDs with NVMe for performance reasons. Btrfs is flexible enough to allow such operations while maintaining redundancy.

### **Monitoring Capacity and Usage**:
After upgrading, you can check the current status of your RAID array with:

```bash
sudo btrfs filesystem df /mount/point
```

This command will show how the data and metadata are distributed across your devices.

---

### Notes:
- **RAID1 in Btrfs**: In Btrfs RAID1, data is mirrored across at least two devices, so the available capacity is limited to the size of the smallest drive. If you have mixed sizes of drives, the smallest drive will limit the maximum capacity unless you use RAID1c3 (triple mirroring).
- **Balance Process**: Depending on the size of your data, the balance process might take some time, so make sure to monitor it. You can pause and resume the rebalance operation if needed.

Would you like more details on handling larger capacities or dealing with different drive configurations in RAID1?