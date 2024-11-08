---
title: "Really probing for the best BTRFS backup tool"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Let me restate my requirements. I want to create a backup of my OS for disaster recovery purposes. I know that a BTRFS snapshot isn't "bare metal", but I'd like to get as close to that as possible. I'm happy with creating either incremental or taking full snapshots, but taking them regularly on a schedule would be ideal. I'm going to be using an external SSD for this purpose that's already formatted as BTRFS. Please just recommend the best tool. If my computer were to break down, I'd like to be able to restore from this snapshot , potentially onto new hardware. So whatever will give me the most versatility

# Output

**Prompt summary:** You want to create a disaster recovery backup of your Fedora OS using Btrfs, aiming for near bare-metal recovery. You are looking for a tool that supports regular, scheduled snapshots and offers the ability to restore to new hardware. You're using an external SSD formatted as Btrfs.

Given your requirements for **disaster recovery, regular incremental backups, and versatility for restoring on new hardware**, the best tool for your needs is:

### **btrbk**

Here’s why **btrbk** is the best choice for your scenario:

1. **Supports Full and Incremental Snapshots**: It allows you to take both full and incremental backups using Btrfs’s `send` and `receive` functionality, which is perfect for disaster recovery scenarios. You can easily restore to the same or different hardware.

2. **Automated Scheduling**: You can configure **btrbk** to take snapshots on a regular schedule. This is crucial for disaster recovery, as it ensures you have up-to-date backups without manual intervention.

3. **Efficient Storage**: Since it uses Btrfs's native snapshot and incremental features, **btrbk** minimizes space usage on your external SSD, especially when creating incremental backups.

4. **Versatility for Restoration**: Since **btrbk** uses Btrfs’s native send/receive commands, you can restore the backup to new hardware, regardless of whether the layout or hardware is different. You may need to reinstall the bootloader and adjust configuration files after restoration, but it provides close-to-bare-metal recovery.

5. **Pruning Old Snapshots**: You can set up retention policies to automatically prune older snapshots, keeping only the most recent ones, which is ideal for managing storage on your external SSD.

---

### Setting up **btrbk** for Your Use Case:

1. **Install btrbk**:
   ```bash
   sudo dnf install btrbk
   ```

2. **Create Configuration for Regular Backups**:
   You’ll need to edit the configuration file for **btrbk** to define how and where the snapshots should be saved. Let’s assume your root filesystem is mounted at `/` and your external SSD is mounted at `/mnt/backup`.

   Create a basic configuration file (`/etc/btrbk/btrbk.conf`):
   ```bash
   sudo nano /etc/btrbk/btrbk.conf
   ```

   Add the following (adjust paths as necessary):
   ```ini
   snapshot_dir = /.snapshots
   target = /mnt/backup
   snapshot_preserve_min = 7d
   snapshot_preserve = 14d
   send_receive_preserve_min = 7d
   send_receive_preserve = 30d
   volume /             # root filesystem
   subvolume /          # subvolume for /
   target /mnt/backup   # external backup
   ```

   - **snapshot_dir**: Directory where local snapshots are stored.
   - **snapshot_preserve**: Defines how many days of snapshots to keep.
   - **target**: Backup destination (external SSD).

3. **Run btrbk to Perform an Initial Backup**:
   ```bash
   sudo btrbk run
   ```

4. **Automate Snapshots with a Cron Job**:
   You can schedule regular backups using a cron job. For example, to take a backup every day at midnight:
   ```bash
   sudo crontab -e
   ```

   Add this line:
   ```bash
   0 0 * * * /usr/bin/btrbk run
   ```

5. **Restoration Process**:
   If disaster strikes and you need to restore the snapshot to a new system:
   - Boot into a live Fedora session or any Linux environment with Btrfs support.
   - Mount the backup drive:
     ```bash
     sudo mount /dev/sdc1 /mnt/backup
     ```
   - Create a new Btrfs subvolume on the new machine:
     ```bash
     sudo btrfs subvolume create /mnt/new-root
     ```
   - Use **btrfs receive** to restore the snapshot:
     ```bash
     sudo btrfs receive /mnt/new-root < /mnt/backup/snapshots/root_snapshot_DATE
     ```

   After this, you'll need to:
   - Reinstall the bootloader (e.g., GRUB).
   - Adjust system configurations (especially if the hardware has changed).

---

### Why **btrbk** is the Best Choice for You:

- **Ease of use** with both full and incremental backups.
- **Automation** through scheduled backups and snapshot management.
- **Versatile restoration** to new hardware using Btrfs’s send/receive functionality.
- **Efficient storage management** with incremental snapshots and retention policies.
- **Comprehensive disaster recovery** tool, bringing you as close as possible to bare-metal recovery with Btrfs.

This setup gives you the most flexibility and ensures you’re prepared for disaster recovery, even on new hardware.