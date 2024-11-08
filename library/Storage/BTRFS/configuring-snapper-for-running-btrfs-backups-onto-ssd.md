---
title: "Configuring Snapper for running BTRFS backups onto SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


### Guide: Configuring Snapper for Full System Snapshots on an External SSD with Exclusions

#### Step 1: Install Snapper
```bash
sudo dnf install snapper
```

#### Step 2: Create Snapper Configuration for Root Filesystem
```bash
sudo snapper -c root create-config /
```

#### Step 3: Mount External SSD
Ensure your SSD is mounted:
```bash
sudo mount /dev/sdX1 /mnt/desktop-backups
```

#### Step 4: Create Exclusion List
To exclude directories like `/dev`, `/proc`, `/sys`, etc., you need to make them subvolumes:
```bash
sudo btrfs subvolume create /dev
sudo btrfs subvolume create /proc
sudo btrfs subvolume create /sys
sudo btrfs subvolume create /run
sudo btrfs subvolume create /tmp
sudo btrfs subvolume create /mnt
sudo btrfs subvolume create /media
sudo btrfs subvolume create /lost+found
```

These subvolumes ensure they are treated separately and excluded when the root snapshot is made.

#### Step 5: Configure Snapper Settings
Edit `/etc/snapper/configs/root`:
- Define **TIMELINE_LIMIT_DAILY**, **NUMBER_LIMIT** to control frequency and retention.
- Use **ALLOW_USERS** to specify permitted users.

#### Step 6: Create Initial Snapshot
```bash
sudo snapper -c root create --description "Initial Full Backup"
```

#### Step 7: Use Btrfs Send/Receive for Incremental Backups
Initial snapshot:
```bash
sudo btrfs send /.snapshots/1/snapshot | sudo btrfs receive /mnt/desktop-backups/
```
Subsequent snapshots:
```bash
sudo btrfs send -p /.snapshots/1/snapshot /.snapshots/2/snapshot | sudo btrfs receive /mnt/desktop-backups/
```

### Explanation:
This setup ensures efficient full system snapshots, excluding unnecessary directories, with incremental backup capabilities to the external SSD.