---
title: "Using Snapper to take incremental snapshots and save them onto external SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you teach me how I could use snapper to take incremental backups of the BTRFS filesystem (that is the host OS)? The target backup device is an external SSD mounted at /mnt/desktop-backups I would like to be able to run the full system snapshot job (of the host OS) regularly and incrementally, only sending over updated files

# Output

### Using Snapper for Incremental Btrfs Backups to an External SSD

Here’s how you can set up Snapper to take incremental Btrfs snapshots of your Fedora system:

### 1. **Install Snapper**
   ```bash
   sudo dnf install snapper
   ```

### 2. **Create a Snapper Configuration**
   - Run the following command:
     ```bash
     sudo snapper -c root create-config /
     ```
   This will set up a configuration for your root filesystem.

### 3. **Initial Full Backup Snapshot**
   - Manually create a snapshot using:
     ```bash
     sudo snapper -c root create --description "Initial Full Backup"
     ```

### 4. **Configure Snapper for Incremental Backups**
   - **Edit Configuration**:
     Open `/etc/snapper/configs/root` and customize:
     ```ini
     ALLOW_USERS="your_username"
     BACKGROUND_COMPARISON="yes"
     NUMBER_LIMIT="5-10"
     NUMBER_CLEANUP="yes"
     TIMELINE_CLEANUP="yes"
     ```
   - Configure `NUMBER_LIMIT` to retain a specific number of snapshots.

### 5. **Automate Snapshot Creation**
   - Schedule a cron job to run periodically, ensuring incremental updates:
     ```bash
     sudo crontab -e
     ```
   - Add:
     ```plaintext
     0 2 * * * /usr/bin/snapper -c root create --description "Scheduled Incremental Backup"
     ```

### 6. **Send Incremental Backups to External SSD**
   - First, create an initial full snapshot on the SSD:
     ```bash
     sudo btrfs send /.snapshots/1/snapshot | sudo btrfs receive /mnt/desktop-backups/
     ```
   - For future snapshots, send incrementals:
     ```bash
     sudo btrfs send -p /.snapshots/1/snapshot /.snapshots/2/snapshot | sudo btrfs receive /mnt/desktop-backups/
     ```

### Explanation:
- **Snapper Configuration**: Adjust settings for cleanup and limits.
- **Automated Snapshots**: Use cron jobs to schedule regular snapshots.
- **Incremental Sending**: Use Btrfs’s `send -p` to efficiently back up only changes.

This setup ensures that your snapshots are regular, incremental, and efficiently stored on your external SSD.