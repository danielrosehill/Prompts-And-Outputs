---
title: "Backup script - but what if the SSD gets a different mount point"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt summary:** You're asking if the SSD gets a random mount point every time it's plugged in and whether there's a way to modify the backup script to identify the correct device regardless of its mount point.

Yes, external drives can often get mounted to different paths, especially if auto-mounted by the system. Instead of relying on the random mount point, you can use the **UUID** of the SSD to ensure that the script always finds and uses the correct drive.

### Steps to Modify the Script for Consistent SSD Mounting:

1. **Identify the UUID of the SSD**:
   To ensure the script consistently identifies the correct drive, you'll use its **UUID** (Universally Unique Identifier). You can find the UUID of your SSD with the following command:
   ```bash
   sudo blkid /dev/sdc1
   ```

   The output will look something like this:
   ```bash
   /dev/sdc1: UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" TYPE="btrfs"
   ```

   Copy the **UUID** value from this output, as you'll use it in your script.

2. **Modify the Script to Use the UUID**:
   In the script, instead of relying on a fixed mount point like `/run/media/daniel/Workstation`, you can mount the SSD using its UUID dynamically. Here's the updated version of your script:

   ```bash
   #!/bin/bash

   # UUID of the external SSD
   SSD_UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"   # Replace with your SSD's UUID

   # Path where the SSD will be temporarily mounted
   MOUNT_POINT="/mnt/ssd_backup"

   # Subvolume paths
   ROOT_SUBVOLUME="/root"
   HOME_SUBVOLUME="$HOME"

   # Current date for snapshot naming
   CURRENT_DATE=$(date +%F)
   ROOT_SNAPSHOT="$MOUNT_POINT/daniel-workstation/root_snapshot_$CURRENT_DATE"
   HOME_SNAPSHOT="$MOUNT_POINT/daniel-workstation/home_snapshot_$CURRENT_DATE"

   # Previous snapshot paths (update manually to the most recent snapshot)
   PREVIOUS_ROOT_SNAPSHOT="$MOUNT_POINT/daniel-workstation/root_snapshot_PREVIOUS_DATE"
   PREVIOUS_HOME_SNAPSHOT="$MOUNT_POINT/daniel-workstation/home_snapshot_PREVIOUS_DATE"

   # Ensure the SSD is mounted
   if ! grep -qs "$MOUNT_POINT" /proc/mounts; then
       sudo mkdir -p $MOUNT_POINT
       sudo mount UUID=$SSD_UUID $MOUNT_POINT
   fi

   # Create new snapshots for root and home
   sudo btrfs subvolume snapshot $ROOT_SUBVOLUME $ROOT_SNAPSHOT
   sudo btrfs subvolume snapshot $HOME_SUBVOLUME $HOME_SNAPSHOT

   # Incremental backup for root subvolume
   if [ -d "$PREVIOUS_ROOT_SNAPSHOT" ]; then
       echo "Performing incremental backup for root..."
       sudo btrfs send -p $PREVIOUS_ROOT_SNAPSHOT $ROOT_SNAPSHOT | sudo btrfs receive $MOUNT_POINT/daniel-workstation/incremental-backups/
   else
       echo "No previous root snapshot found, performing full backup..."
       sudo btrfs send $ROOT_SNAPSHOT | sudo btrfs receive $MOUNT_POINT/daniel-workstation/incremental-backups/
   fi

   # Incremental backup for home subvolume
   if [ -d "$PREVIOUS_HOME_SNAPSHOT" ]; then
       echo "Performing incremental backup for home..."
       sudo btrfs send -p $PREVIOUS_HOME_SNAPSHOT $HOME_SNAPSHOT | sudo btrfs receive $MOUNT_POINT/daniel-workstation/incremental-backups/
   else
       echo "No previous home snapshot found, performing full backup..."
       sudo btrfs send $HOME_SNAPSHOT | sudo btrfs receive $MOUNT_POINT/daniel-workstation/incremental-backups/
   fi

   # Optional: Prune old snapshots, keeping the last 7 snapshots
   sudo btrfs subvolume delete $(ls -t $MOUNT_POINT/daniel-workstation/root_snapshot_* | tail -n +8)
   sudo btrfs subvolume delete $(ls -t $MOUNT_POINT/daniel-workstation/home_snapshot_* | tail -n +8)

   # Unmount the SSD
   sudo umount $MOUNT_POINT
   ```

### Key Modifications:

1. **Mounting the SSD by UUID**:
   - The script dynamically mounts the SSD using its UUID (`sudo mount UUID=$SSD_UUID $MOUNT_POINT`), ensuring it works regardless of where it’s mounted by the system.
   - The SSD is mounted to a fixed directory (`/mnt/ssd_backup`) that you control, ensuring consistency in your script.

2. **Unmounting the SSD**:
   - After the backup is complete, the script unmounts the SSD (`sudo umount $MOUNT_POINT`) to avoid leaving it mounted unnecessarily.

3. **Previous Snapshots**:
   - Make sure to update the `PREVIOUS_ROOT_SNAPSHOT` and `PREVIOUS_HOME_SNAPSHOT` values with the correct paths from your last backup. You could automate this by storing the last backup date in a file, but for now, manual updates are required.

### To Test the Script:

1. **Update the UUID**:
   Replace the `SSD_UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` line with your actual SSD UUID from the `blkid` command.

2. **Test the Script**:
   Run the script manually to ensure it works:
   ```bash
   ~/btrfs_incremental_backup.sh
   ```

3. **Schedule with Cron**:
   Once you're satisfied with the script, schedule it as before with cron:
   ```bash
   crontab -e
   ```

   Add the following line to run the script daily at midnight:
   ```bash
   0 0 * * * /home/daniel/btrfs_incremental_backup.sh
   ```

### Summary:

- **UUID-based mounting** ensures your script works no matter where the SSD is mounted.
- The script mounts the SSD to a specific directory (`/mnt/ssd_backup`), performs the backup, and unmounts it afterward.
- You now have a flexible and robust solution for automating your Btrfs incremental backups to the SSD.