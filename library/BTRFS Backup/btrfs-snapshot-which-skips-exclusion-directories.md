---
title: "BTRFS snapshot which skips exclusion directories"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is possible to configure a Btrfs snapshot that excludes specific directories. However, Btrfs itself does not have built-in options to exclude paths during a snapshot. You can achieve this by creating separate subvolumes for the directories you want to exclude and then snapshotting only the relevant subvolumes.

### Approach:
1. **Convert Directories to Separate Subvolumes**:
   To exclude directories like `/dev`, `/proc`, etc., convert them to separate subvolumes:
   ```bash
   sudo btrfs subvolume create /mnt
   sudo btrfs subvolume create /tmp
   # Repeat for other directories you want to exclude
   ```

2. **Snapshot the Main System**:
   Once the directories are separate subvolumes, you can snapshot the root without including these:
   ```bash
   sudo btrfs subvolume snapshot -r / /mnt/desktop-backups/system_snapshot
   ```

3. **Automate with a Script**:
   Create a script that takes periodic snapshots, ensuring you exclude unwanted directories by configuring them as separate subvolumes:
   ```bash
   #!/bin/bash
   TIMESTAMP=$(date +%Y%m%d%H%M)
   sudo btrfs subvolume snapshot -r / /mnt/desktop-backups/system_snapshot_$TIMESTAMP
   ```

4. **Set Up Cron Job for Automation**:
   Automate periodic snapshots by adding a cron job:
   ```bash
   crontab -e
   ```
   Add:
   ```plaintext
   0 2 * * * /path/to/your/snapshot-script.sh
   ```

This way, you can manage automated, periodic snapshots of your system while excluding specific directories.