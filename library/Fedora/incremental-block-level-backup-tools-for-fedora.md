---
title: "Incremental block level backup tools for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking for ways to take **block-level backups** of your **Fedora computer** that support **incremental backups** and can be run while the system is powered on **without noticeable slowdown**.

Yes, there are several backup solutions available for Fedora that support **block-level incremental backups** and allow for **online backups** (i.e., backups while the system is running). These tools differ in performance and feature sets, but many are well-suited for creating system restore points without interrupting your workflow.

### Recommended Block-Level Backup Solutions:

#### 1. **BorgBackup (Borg)**
   - **Description**: BorgBackup is an efficient, deduplicating backup tool. It supports **incremental backups** and operates at the **file system level**, but it is highly efficient for block-level changes due to its deduplication capabilities. Borg is widely praised for being fast and resource-friendly.
   - **Key Features**:
     - **Incremental backups**: Only backs up the changes since the last backup.
     - **Compression** and **deduplication**: Reduces storage needs.
     - Can run with the system **powered on** without significant performance impact.
     - **Encrypted backups**: Protect your data.
   - **Use Case**: Ideal for creating system backups and restoring specific files or entire file systems.
   - **Installation**:
     ```bash
     sudo dnf install borgbackup
     ```
   - **Example Usage**:
     - Initialize the repository:
       ```bash
       borg init --encryption=repokey /path/to/backup/location
       ```
     - Perform an incremental backup:
       ```bash
       borg create /path/to/backup/location::backup-name /path/to/data
       ```
     - Restore a backup:
       ```bash
       borg extract /path/to/backup/location::backup-name
       ```

#### 2. **Timeshift**
   - **Description**: Timeshift is popular for creating **system snapshots** and allows for incremental backups. It is more known for **file-level** backups, but its snapshot approach can be used to restore entire systems quickly. Timeshift can back up the system while running without causing noticeable slowdowns.
   - **Key Features**:
     - **Incremental backups** based on file system snapshots (supports **rsync** and **Btrfs snapshots**).
     - Can schedule regular system backups.
     - **Minimal resource consumption** when creating backups.
     - Easily restores the system to previous states in the event of failure.
   - **Installation**:
     ```bash
     sudo dnf install timeshift
     ```
   - **Example Usage**:
     - Launch **Timeshift** and set it up via the GUI.
     - Schedule backups and set the frequency.
     - Restore the system from snapshots in case of system issues.

#### 3. **Restic**
   - **Description**: Restic is a modern, open-source backup tool that supports **incremental backups**. It is optimized for speed and minimal resource usage, making it a good choice for backing up while the system is running.
   - **Key Features**:
     - **Incremental backups**: Only saves data that has changed since the last backup.
     - **Encryption**: Data is encrypted by default.
     - **Deduplication**: Reduces storage needs.
     - Can back up to local storage, network storage (like your NAS), or cloud.
   - **Use Case**: Great for incremental and block-level backups with minimal system performance impact.
   - **Installation**:
     ```bash
     sudo dnf install restic
     ```
   - **Example Usage**:
     - Initialize the repository:
       ```bash
       restic init --repo /path/to/backup/location
       ```
     - Perform a backup:
       ```bash
       restic backup /path/to/data --repo /path/to/backup/location
       ```
     - Restore a backup:
       ```bash
       restic restore latest --target /path/to/restore/location
       ```

#### 4. **Duplicacy**
   - **Description**: Duplicacy is a cross-platform backup tool that supports **incremental backups** and is designed for efficiency. It supports deduplication and can back up while the system is running.
   - **Key Features**:
     - **Incremental backups** with deduplication.
     - Backup to local, NAS, or cloud storage.
     - **Encrypted** backups for security.
     - Minimal resource impact during backup operations.
   - **Installation**: Duplicacy offers both CLI and GUI versions.
   - **Example Usage**:
     - Initialize a repository:
       ```bash
       duplicacy init backup-name /path/to/backup/location
       ```
     - Backup your system:
       ```bash
       duplicacy backup -stats
       ```
     - Restore from backup:
       ```bash
       duplicacy restore -r 1
       ```

#### 5. **Btrfs Snapshots (if using Btrfs)**:
   - **Description**: If your Fedora system uses **Btrfs** as its file system, you can use its native **snapshot** capabilities. **Btrfs** is a modern file system that supports block-level snapshots, making it highly efficient for incremental backups.
   - **Key Features**:
     - **Incremental snapshots**: Only changes are saved, making backups very fast.
     - **Low system impact**: Snapshots can be created without affecting system performance.
     - Native **block-level** functionality, making it highly efficient.
   - **Use Case**: Best suited if your root or data partitions use **Btrfs**.
   - **Example Usage**:
     - Create a snapshot:
       ```bash
       sudo btrfs subvolume snapshot / /path/to/snapshot
       ```
     - List snapshots:
       ```bash
       sudo btrfs subvolume list /
       ```
     - Restore from a snapshot:
       ```bash
       sudo btrfs subvolume delete /path/to/snapshot
       ```

#### 6. **Amanda (Advanced Maryland Automatic Network Disk Archiver)**
   - **Description**: Amanda is an open-source backup solution that supports incremental and full backups. It is optimized for minimal performance impact and supports both local and network backups.
   - **Key Features**:
     - Supports **incremental backups**.
     - Works with local storage or NAS.
     - Can perform backups while the system is running with minimal resource use.
   - **Use Case**: Amanda is more advanced and often used in enterprise environments, but it can be adapted for personal systems.
   - **Installation**:
     ```bash
     sudo dnf install amanda
     ```

---

### Conclusion:
For **incremental block-level backups** that can run while the system is powered on and without noticeable slowdowns:
- **BorgBackup** and **Restic** are excellent choices for block-level incremental backups, offering encryption and deduplication with minimal performance impact.
- **Timeshift** is a solid option if you're looking for a snapshot-based approach that is easy to configure and restore.
- **Btrfs snapshots** are ideal if you're already using Btrfs as your file system.

Each of these solutions offers a different balance of features, depending on whether you're looking for incremental backups, low system impact, or specific file system support.

Let me know if you'd like more details on setting up any of these tools!