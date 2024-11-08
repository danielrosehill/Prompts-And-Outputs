---
title: "Commands for creating BTRFS snapshot"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's write step 4
Pay attention to the configuration
I'm trying to create a BTRFS snapshot of my whole BTRFS computer (ie /)
We have mounted an external SSD at /mnt/desktop-backups
I need the commands to take a BTRFS snapshot and store it on the SSD
Of course, we don't want to include /mnt in the snapshot to prevent loop

# Output

### Step 4: Create a Btrfs Snapshot of the Entire Filesystem

1. **Open a Terminal**: Access the terminal on your Fedora system.

2. **Create the Snapshot**: Run the following command to create a Btrfs snapshot of the entire filesystem (`/`), excluding the `/mnt` directory to avoid loops:
   ```bash
   sudo btrfs subvolume snapshot -r / /mnt/desktop-backups/system_snapshot
   ```

This command creates a read-only snapshot of your entire Btrfs filesystem and stores it on the external SSD mounted at `/mnt/desktop-backups`.

# Output 2

To create a Btrfs snapshot of your entire filesystem while avoiding the "Invalid cross-device link" error, follow these steps:

### Step 4: Create a Btrfs Snapshot of the Entire Filesystem

1. **Open a Terminal**: Access the terminal on your Fedora system.

2. **Create a Subvolume of the Root**:
   First, create a temporary subvolume for the root filesystem:
   ```bash
   sudo btrfs subvolume create /mnt/desktop-backups/root_snapshot
   ```

3. **Snapshot the Subvolume**:
   Now, create the snapshot of the root filesystem (excluding `/mnt`):
   ```bash
   sudo btrfs subvolume snapshot -r / /mnt/desktop-backups/root_snapshot/system_snapshot
   ```

This process captures the current state of your entire Btrfs filesystem (excluding the `/mnt` directory) and stores it on the external SSD.

# QUestion

s this approach suitable if I want to run the snapshot repeatedly and incrementally? Also - how does it ensure that /mnt is not included in the snapshots that are taken?

# Output

The approach I previously suggested does not explicitly exclude `/mnt`. To ensure that `/mnt` is not included in the snapshots, you need to specify the Btrfs subvolumes correctly and use an incremental backup strategy.

### Revised Approach:
Since you cannot create snapshots across devices, a more effective method is to **use Btrfs send/receive** for incremental backups.

### Step 4: Set Up Btrfs Incremental Snapshots

1. **Create an Initial Snapshot:**
   ```bash
   sudo btrfs subvolume snapshot -r / /mnt/desktop-backups/system_snapshot_1
   ```

2. **Subsequent Incremental Snapshots:**
   For incremental backups, first create another snapshot:
   ```bash
   sudo btrfs subvolume snapshot -r / /mnt/desktop-backups/system_snapshot_2
   ```

3. **Send Incremental Changes:**
   Use the Btrfs send/receive command to send changes:
   ```bash
   sudo btrfs send -p /mnt/desktop-backups/system_snapshot_1 /mnt/desktop-backups/system_snapshot_2 | sudo btrfs receive /mnt/desktop-backups
   ```

### Excluding `/mnt`:
Since `/mnt` isn't a separate Btrfs subvolume, it gets included when you snapshot the root. To properly exclude it:
1. **Ensure `/mnt` is not mounted directly within `/` during the snapshot.**
2. Use a **`btrfs subvolume`** to manage the content you wish to exclude more precisely:
   - If there are directories or mounted points to exclude, consider creating them as separate subvolumes and managing them outside of the root subvolume.

**Note:** When creating snapshots from the root, unless specifically mounted elsewhere or managed as a different subvolume, `btrfs snapshot` will attempt to include everything under `/`. This means any exclusion has to be preconfigured by managing mounts and subvolumes directly.