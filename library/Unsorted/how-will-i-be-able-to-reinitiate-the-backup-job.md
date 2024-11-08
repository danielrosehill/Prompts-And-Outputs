---
title: "How will I be able to reinitiate the backup job"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt summary:** You’re asking if you need to run the snapshot commands every time you do an incremental backup, and whether you need to recreate the snapshots each time for a regularly repeated incremental backup job.

For **incremental backups** with **Btrfs**, you do not need to recreate full snapshots every time. Instead, you can use **Btrfs send/receive** to perform **incremental backups** based on the differences between snapshots. This approach is efficient and ideal for your needs since it avoids duplicating data that hasn’t changed.

Here’s how to set it up for regular incremental backups:

### 1. **Initial Full Snapshot (Baseline)**
   The first time, you’ll need to take full snapshots of both the root (`/root`) and home (`/home`) subvolumes. You’ve already done this with the following commands:
   ```bash
   sudo btrfs subvolume snapshot /root /run/media/daniel/Workstation/daniel-workstation/root_snapshot_$(date +%F)
   sudo btrfs subvolume snapshot /home /run/media/daniel/Workstation/daniel-workstation/home_snapshot_$(date +%F)
   ```

### 2. **Incremental Backups Using Btrfs Send/Receive**
   After creating your initial full snapshot, you can use **Btrfs send/receive** to create **incremental backups** by referencing the previous snapshot and only sending changes.

   Here’s the procedure for your incremental backup job:

#### Step 1: Create a New Snapshot for Root and Home
   Each time you run the backup, you’ll need to create new snapshots. However, since the send/receive process will only transfer changes, this won’t be a full backup.

   Example for taking new snapshots:
   ```bash
   sudo btrfs subvolume snapshot /root /run/media/daniel/Workstation/daniel-workstation/root_snapshot_$(date +%F)
   sudo btrfs subvolume snapshot /home /run/media/daniel/Workstation/daniel-workstation/home_snapshot_$(date +%F)
   ```

#### Step 2: Perform Incremental Backup with `btrfs send/receive`
   To send only the differences (incremental changes) from the previous snapshot, you can use the `btrfs send -p` command, where `-p` refers to the previous snapshot.

   For **root**:
   ```bash
   sudo btrfs send -p /run/media/daniel/Workstation/daniel-workstation/root_snapshot_PREVIOUS_DATE /run/media/daniel/Workstation/daniel-workstation/root_snapshot_$(date +%F) | sudo btrfs receive /run/media/daniel/Workstation/incremental-backups/
   ```

   For **home**:
   ```bash
   sudo btrfs send -p /run/media/daniel/Workstation/daniel-workstation/home_snapshot_PREVIOUS_DATE /run/media/daniel/Workstation/daniel-workstation/home_snapshot_$(date +%F) | sudo btrfs receive /run/media/daniel/Workstation/incremental-backups/
   ```

   - Replace `root_snapshot_PREVIOUS_DATE` with the most recent snapshot you used for backup.
   - Replace `$(date +%F)` with the current date or your desired naming scheme.

   This command will compare the current snapshot against the previous one and only send the differences (incremental data) to the backup location.

### 3. **Automate the Backup Process with a Script**

   To avoid manually running these commands, you can create a script that handles the snapshot creation and incremental backup, and then schedule it with **cron** for automatic execution.

   Example script (`btrfs_backup.sh`):

   ```bash
   #!/bin/bash

   # Define paths
   BACKUP_PATH="/run/media/daniel/Workstation/daniel-workstation"
   INCREMENTAL_BACKUP_PATH="/run/media/daniel/Workstation/incremental-backups"

   # Create new snapshots
   sudo btrfs subvolume snapshot /root "$BACKUP_PATH/root_snapshot_$(date +%F)"
   sudo btrfs subvolume snapshot /home "$BACKUP_PATH/home_snapshot_$(date +%F)"

   # Send incremental backups for root
   sudo btrfs send -p "$BACKUP_PATH/root_snapshot_PREVIOUS_DATE" "$BACKUP_PATH/root_snapshot_$(date +%F)" | sudo btrfs receive "$INCREMENTAL_BACKUP_PATH"

   # Send incremental backups for home
   sudo btrfs send -p "$BACKUP_PATH/home_snapshot_PREVIOUS_DATE" "$BACKUP_PATH/home_snapshot_$(date +%F)" | sudo btrfs receive "$INCREMENTAL_BACKUP_PATH"
   ```

   You can replace `PREVIOUS_DATE` dynamically by tracking the last snapshot date, or you can manually edit the script before each run.

### 4. **Schedule the Script with Cron**
   To schedule this script to run automatically, add it to your **cron** jobs. For example, to run the backup script every night at midnight:

   ```bash
   crontab -e
   ```

   Add the following line:
   ```bash
   0 0 * * * /path/to/btrfs_backup.sh
   ```

### 5. **Pruning Old Snapshots**
   You may want to prune older snapshots to avoid consuming excessive disk space. You can use `btrfs subvolume delete` to remove old snapshots, or configure tools like **btrbk** to manage snapshot retention automatically.

### Summary of Workflow:

- **Step 1**: Create new snapshots for root and home.
- **Step 2**: Perform an incremental backup using `btrfs send -p` to send only the changes since the last snapshot.
- **Step 3**: Automate the process using a script and schedule it with **cron** for regular execution.
- **Step 4**: Optionally prune old snapshots to manage disk space.

By using **incremental snapshots** and **btrfs send/receive**, you'll only transfer changes, making your backups more efficient, while keeping the ability to fully restore your system from the SSD.