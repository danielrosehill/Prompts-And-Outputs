---
title: "Guidance for BTRFS backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

It seems that the server is actually Ubuntu. But I could set up a Fedora server. In fact, I would be willing to set up a server just for the purpose of storing incremental BRTFS snapshots. I use Proxmox. Can you estimate what size the snapshot would be and recommend a tool?

# Output

Based on the information provided and your willingness to set up a dedicated server for BTRFS snapshots, here's a recommendation:

1. Snapshot Size Estimation:
   From the provided code, we can estimate the size of an incremental snapshot:

   ```python
   used_space_gb = 220.47  # Current used space in GB
   snapshot_overhead_percentage = 0.05  # Estimated overhead, typically around 5%
   incremental_snapshot_size = used_space_gb * snapshot_overhead_percentage
   # Result: 11.0235 GB
   ```

   So, each incremental snapshot is estimated to be around 11 GB. However, this can vary based on the amount of data changed between snapshots.

2. Server Setup Recommendation:
   Since you're using Proxmox, you can easily set up a Fedora VM dedicated to storing these snapshots. Here's a recommendation:

   - VM Size: Start with 500 GB to 1 TB, depending on how many snapshots you want to retain.
   - RAM: 4-8 GB should be sufficient for this purpose.
   - CPU: 2-4 cores, as the main task will be I/O operations.

3. Tool Recommendation:
   For managing BTRFS snapshots and transfers, I recommend using BTRBK (BTRFS Backup). It's specifically designed for managing BTRFS snapshots and backups, and it works well with remote systems.

   Key features of BTRBK:
   - Snapshot management with retention policies
   - Incremental backups
   - SSH support for remote backups
   - Configurable backup schedules

To set this up:

1. Install Fedora on your Proxmox VM.
2. Configure the VM's storage as BTRFS.
3. Install BTRBK on both your main system and the backup VM:
   ```
   sudo dnf install btrbk
   ```
4. Configure BTRBK on your main system to send snapshots to the backup VM.
5. Set up SSH key authentication between your main system and the backup VM for secure, password-less transfers.

Example BTRBK configuration:

```
snapshot_dir /snapshots
snapshot_create ondemand

target_preserve_min latest
target_preserve 24h 8
target_preserve 7d  4
target_preserve 30d 6
target_preserve 180d 4

volume /
  subvolume root
    snapshot_name root_snap
    target ssh://backup-vm/mnt/backup/root

volume /home
  subvolume @home
    snapshot_name home_snap
    target ssh://backup-vm/mnt/backup/home
```

This setup will provide you with a dedicated, flexible solution for storing and managing your BTRFS snapshots, allowing for easy recovery and efficient use of storage space.
 