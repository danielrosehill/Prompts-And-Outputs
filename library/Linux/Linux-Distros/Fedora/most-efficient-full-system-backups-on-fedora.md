---
title: "Most efficient full system backups on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

What's the most efficient way to take a full system backup of a fedora OS computer onto an external SSD? The Fedora computer I wish to backup is running BTRFS and RAID 1 (RAID 1 is spready over 3 physical disks)

# Output

**Prompt Summary:** You asked for the most efficient way to take a full system backup of a Fedora OS computer onto an external SSD, noting that the system uses Btrfs with RAID 1 across three physical disks.

Given your setup, Btrfs has built-in tools that can make backing up your system more efficient, especially since it's designed to handle snapshots and multi-device configurations like RAID. Here are a few approaches:

### 1. **Using Btrfs Snapshots and Send/Receive**
   - **Method:** Leverage Btrfs snapshots and the `btrfs send`/`btrfs receive` commands. This method efficiently transfers data by only copying the changes between snapshots.
   - **Steps:**
     1. Create a snapshot of the Btrfs subvolumes you wish to back up:
        ```bash
        sudo btrfs subvolume snapshot -r / /mnt/btrfs-backups/root_snapshot
        ```
     2. Use `btrfs send` to send the snapshot to the external SSD:
        ```bash
        sudo btrfs send /mnt/btrfs-backups/root_snapshot | sudo btrfs receive /path/to/external-ssd/
        ```
     3. For incremental backups (sending only changes since the last snapshot), create a new snapshot and run:
        ```bash
        sudo btrfs send -p /mnt/btrfs-backups/root_snapshot /mnt/btrfs-backups/root_snapshot_new | sudo btrfs receive /path/to/external-ssd/
        ```
   - **Pros:** Efficient use of space, fast incremental backups, native handling of Btrfs features (RAID, snapshots).
   - **Cons:** Requires familiarity with Btrfs commands.

### 2. **Using `btrfs-image` for a Disk Image**
   - **Method:** `btrfs-image` can create an image of the Btrfs filesystem, useful for full-system backups.
   - **Command Example:**
     ```bash
     sudo btrfs-image -c9 /dev/sdX /path/to/external-ssd/system-backup.img
     ```
   - **Options Explained:**
     - `-c9`: Compression level (adjust for speed vs. compression trade-off).
   - **Pros:** Efficient disk image backup, preserves all Btrfs features.
   - **Cons:** Full disk restoration can be more manual, and the process can be slow for large filesystems.

### 3. **Using `rsync` with Btrfs Snapshots**
   - **Method:** Combine Btrfs snapshots with `rsync` for incremental file-based backups.
   - **Steps:**
     1. Create a snapshot:
        ```bash
        sudo btrfs subvolume snapshot -r / /mnt/btrfs-backups/root_snapshot
        ```
     2. Use `rsync` to copy the snapshot:
        ```bash
        sudo rsync -aAXv /mnt/btrfs-backups/root_snapshot/ /path/to/external-ssd/
        ```
   - **Pros:** Versatile, supports incremental backups, preserves permissions.
   - **Cons:** Slightly more manual, may need extra steps to restore bootloader.

### Recommendations:
Given your RAID 1 setup on Btrfs, the **Btrfs `send`/`receive`** method is likely the most efficient and effective, especially for managing incremental backups. It allows you to take advantage of Btrfs’s built-in capabilities, making the process faster and less resource-intensive.