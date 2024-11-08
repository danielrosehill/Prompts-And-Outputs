---
title: "BTRFS snapshot with exclusion paths"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here is the full command using **btrfs send/receive** while ensuring the excluded directories are not part of the snapshot backup:

1. **Initial Snapshot Command**:
   Make sure your external SSD is mounted at `/mnt/desktop-backups`:
   ```bash
   sudo snapper -c root create --description "Initial Full Backup"
   ```

2. **Send Snapshot and Exclude Unwanted Directories**:
   To manually exclude directories, ensure they are mounted as separate subvolumes. Then use:
   ```bash
   sudo btrfs send -p /.snapshots/1/snapshot --exclude /dev --exclude /proc --exclude /sys --exclude /run --exclude /tmp --exclude /mnt --exclude /media --exclude /lost+found | sudo btrfs receive /mnt/desktop-backups/
   ```

### Explanation:
The command will exclude the specified directories from being transferred to the external SSD backup. Ensure the paths are mounted correctly to avoid including unwanted data during the backup process.