---
title: "Incremental block level backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Block level backups are very robust but they tend to be take up a lot of space. Is there any way to take a backup (on Fedora) that is both block level and incremental (so that one backup archive can be maintained and only the changes are synced between runs)?

# Output

Yes, it is possible to create block-level backups on Fedora that are **incremental**, meaning only changes are backed up after the initial full backup. This approach allows you to maintain an efficient and space-saving backup system while preserving the robustness of block-level backups. Below are some tools and techniques that allow block-level, incremental backups on Fedora:

### 1. **BorgBackup (Borg) + LVM Snapshots**
While Borg itself is file-based, when combined with **LVM snapshots**, it can provide block-level, incremental backups. LVM snapshots allow you to capture a point-in-time snapshot of your filesystem at the block level, while Borg efficiently deduplicates and compresses the data, allowing only changed blocks to be backed up in subsequent runs.

#### How It Works:
- **LVM Snapshot**: Take a snapshot of your logical volume (LVM) so that you capture the state of the filesystem at the block level.
- **Borg for Incremental Backups**: Borg will only back up the blocks that have changed since the last backup, thanks to its built-in deduplication.
  
#### Example Workflow:
1. Create an LVM snapshot:
   ```bash
   sudo lvcreate --size 5G --snapshot --name backup_snapshot /dev/vg0/root
   ```

2. Use Borg to back up the snapshot:
   ```bash
   sudo borg create /path/to/backup::archive-name /mnt/snapshot
   ```

3. Remove the snapshot after backup:
   ```bash
   sudo lvremove /dev/vg0/backup_snapshot
   ```

**Advantages**:
- Deduplication and compression help minimize space usage.
- Incremental backups are efficient and reduce the amount of data stored.

### 2. **BTRFS Snapshots + rsync**
If you’re using **BTRFS** as your filesystem (which is recommended for its snapshotting and compression features), you can leverage **BTRFS snapshots** and **rsync** to perform incremental block-level backups. BTRFS snapshots are copy-on-write, so only the changed blocks are backed up, saving space.

#### Example Workflow:
1. Create a snapshot of your root volume (or any other BTRFS volume):
   ```bash
   sudo btrfs subvolume snapshot / /path/to/snapshot
   ```

2. Use `rsync` to back up the snapshot incrementally:
   ```bash
   sudo rsync -aAX /path/to/snapshot /path/to/backup/location
   ```

3. Remove old snapshots to conserve space:
   ```bash
   sudo btrfs subvolume delete /path/to/snapshot
   ```

**Advantages**:
- BTRFS snapshots are lightweight and don’t require duplicating data.
- Snapshots allow for fast, incremental backups.

### 3. **Restic with LVM Snapshots**
**Restic** is another powerful backup tool that supports deduplication and incremental backups. It’s file-based by default but can be combined with **LVM snapshots** to offer block-level incremental backups.

#### Example Workflow:
1. Create an LVM snapshot of your logical volume:
   ```bash
   sudo lvcreate --size 5G --snapshot --name backup_snapshot /dev/vg0/root
   ```

2. Backup the snapshot with Restic:
   ```bash
   restic -r /path/to/repo backup /mnt/snapshot
   ```

3. Remove the snapshot:
   ```bash
   sudo lvremove /dev/vg0/backup_snapshot
   ```

**Advantages**:
- Restic supports encryption, deduplication, and incremental backups, making it highly space-efficient.
- Restic works well across different storage backends (local, remote, cloud).

### 4. **rsync + ZFS Snapshots**
If you're using **ZFS** instead of BTRFS or LVM, **ZFS snapshots** provide block-level incremental backups similar to BTRFS.

#### Example Workflow:
1. Take a snapshot of the ZFS dataset:
   ```bash
   sudo zfs snapshot pool/dataset@snapshot_name
   ```

2. Use `rsync` to perform an incremental backup:
   ```bash
   sudo rsync -aAX /path/to/zfs/snapshot /path/to/backup/location
   ```

3. Remove old snapshots as needed:
   ```bash
   sudo zfs destroy pool/dataset@snapshot_name
   ```

**Advantages**:
- ZFS provides compression and block-level snapshots natively.
- rsync works well for syncing only the changes between backups.

### 5. **Veeam Agent for Linux (Free)**
**Veeam Agent** is a commercial-grade solution that supports block-level incremental backups. It is free for personal use and provides a robust solution for Fedora users.

#### Features:
- Supports incremental, block-level backups.
- Compression and deduplication features.
- Supports both local and cloud-based backup targets.

#### Example Workflow:
1. Install Veeam Agent for Linux:
   Download the RPM from the [Veeam website](https://www.veeam.com) and install it using `dnf`:
   ```bash
   sudo rpm -ivh veeam-release*
   sudo dnf install veeam
   ```

2. Configure the backup job:
   Use the command-line tool to create a backup job:
   ```bash
   sudo veeamconfig job create --name "Backup Job" --realtime --mode full --path /path/to/backup/location
   ```

3. Enable incremental backups:
   Veeam automatically handles incremental backups after the initial full backup.

**Advantages**:
- Veeam is highly reliable and enterprise-grade.
- It supports full system and incremental backups, reducing storage usage.

### Summary of Optimal Solution:
For your needs—efficient, block-level, incremental backups on Fedora—I recommend using **BorgBackup or Restic with LVM snapshots** or **BTRFS with rsync** if you're using the BTRFS filesystem. These methods ensure you capture changes at the block level while maintaining incremental backups, optimizing storage usage, and providing flexibility for restoration.

If you're looking for a more polished, user-friendly experience, **Veeam Agent** would be an excellent choice for handling block-level incremental backups with minimal setup.