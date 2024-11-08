---
title: "Protocol for creating backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To create a Btrfs snapshot of your full system while excluding specific directories and enabling incremental backups, follow these steps:

### Step-by-Step Guide:

1. **Ensure the SSD is Mounted**:
   Make sure your external SSD is mounted at `/mnt/desktop-backups`:
   ```bash
   sudo mount /dev/sdX1 /mnt/desktop-backups
   ```

2. **Initial Full System Snapshot**:
   Use `rsync` to copy your root filesystem while excluding unnecessary directories:
   ```bash
   sudo rsync -aAXv --delete --exclude={"/dev","/proc","/sys","/run","/tmp","/mnt","/media","/lost+found"} / /mnt/desktop-backups/initial_backup/
   ```

3. **Create Subsequent Incremental Backups Using Btrfs Snapshots**:
   After the initial setup, use the following approach to incrementally sync:
   - **Take the First Snapshot**:
     ```bash
     sudo btrfs subvolume snapshot /mnt/desktop-backups/initial_backup /mnt/desktop-backups/snapshot1
     ```
   - **For Subsequent Snapshots**:
     ```bash
     sudo btrfs send -p /mnt/desktop-backups/snapshot1 /mnt/desktop-backups/snapshot2 | sudo btrfs receive /mnt/desktop-backups
     ```

### Explanation:
- **`rsync`** is used initially to copy everything except the excluded directories.
- **Btrfs snapshots** provide incremental backups by only saving changes, making future snapshots efficient.
- **Subsequent Snapshots**: Using `btrfs send -p`, you can incrementally sync changes to create efficient backups without redundancy. 

This method ensures you have an up-to-date, system-wide backup that can be restored or cloned onto a new machine if needed.