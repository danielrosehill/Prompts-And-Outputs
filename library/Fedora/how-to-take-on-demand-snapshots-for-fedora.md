---
title: "How to take on demand snapshots for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you give me a guide on how to take snapshots on my Fedora computer before making major system changes. Can I take an on demand snapshot in BTRFS? Would this be sufficient to roll back to if the changes broke some aspect of the OS?

# Output

### Guide to Taking Snapshots on Fedora with BTRFS

BTRFS (B-tree File System) is a modern file system that supports snapshotting, which is incredibly useful for taking backups or snapshots of your system before making major changes. In Fedora, BTRFS is often the default file system, and you can create **on-demand snapshots** that allow you to **roll back** in case something goes wrong during system updates or modifications.

#### **What is a BTRFS Snapshot?**
A BTRFS snapshot is a point-in-time copy of a subvolume (such as your root or home directory) that allows you to restore your system to that exact state if something goes wrong. Snapshots are lightweight because they only store changes made after the snapshot, not a full copy of the entire data.

### **Step-by-Step Guide to Taking BTRFS Snapshots**

#### **1. Check Your Setup**
First, confirm that your system is using BTRFS, and identify the subvolumes you want to snapshot.
- Run the following command to check if your root filesystem is on BTRFS:
  ```bash
  df -Th
  ```
  Look for entries with the **btrfs** type. If `/` (the root) is listed under BTRFS, you're good to go.

#### **2. Install `btrfs-progs` (if not already installed)**
The **btrfs-progs** package provides the necessary utilities to manage BTRFS subvolumes and snapshots. It is usually pre-installed on Fedora systems with BTRFS, but you can install it if needed:
  ```bash
  sudo dnf install btrfs-progs
  ```

#### **3. Identify the Subvolume to Snapshot**
To snapshot your system, you need to know which subvolume you’re working with. The most common subvolumes to snapshot are:
- The **root filesystem** (usually mounted at `/`).
- Your **home directory** (usually mounted at `/home`).

You can list your BTRFS subvolumes with the following command:
  ```bash
  sudo btrfs subvolume list /
  ```

#### **4. Take an On-Demand Snapshot**
Once you’ve identified the subvolume, you can create a snapshot. The following command creates a snapshot of your root subvolume:

  ```bash
  sudo btrfs subvolume snapshot / /path/to/snapshot-directory/snapshot-name
  ```

For example, to snapshot the root filesystem and store it in `/snapshots`, you can run:
  ```bash
  sudo mkdir -p /snapshots
  sudo btrfs subvolume snapshot / /snapshots/root-snapshot-$(date +%Y%m%d-%H%M%S)
  ```

To take a snapshot of your home directory:
  ```bash
  sudo btrfs subvolume snapshot /home /snapshots/home-snapshot-$(date +%Y%m%d-%H%M%S)
  ```

This will create a snapshot in the `/snapshots` folder. The snapshot name will include the current date and time.

#### **5. Verify the Snapshot**
Once the snapshot is created, you can list all snapshots using:
  ```bash
  sudo btrfs subvolume list /
  ```

#### **6. Rolling Back to a Snapshot**
If something goes wrong after making system changes, you can roll back to a previous snapshot.

##### **Option 1: Mount the Snapshot**
You can manually mount the snapshot and check its contents:
  ```bash
  sudo mount -o subvol=/snapshots/root-snapshot-YYYYMMDD-HHMMSS /dev/sdX /mnt
  ```
  Replace `/dev/sdX` with the appropriate device and `/snapshots/root-snapshot-YYYYMMDD-HHMMSS` with your snapshot.

##### **Option 2: Replace the Current Subvolume with the Snapshot**
To roll back, you would remove the current root subvolume and replace it with the snapshot. Be **careful** when doing this:
  1. Boot into a **live environment** (e.g., a Fedora live USB) to avoid issues with modifying a mounted subvolume.
  2. Mount the root filesystem:
     ```bash
     sudo mount /dev/sdX /mnt
     ```
  3. Delete the current root subvolume (this won’t delete the snapshot):
     ```bash
     sudo btrfs subvolume delete /mnt/@
     ```
  4. Rename the snapshot to replace the root subvolume:
     ```bash
     sudo mv /mnt/snapshots/root-snapshot-YYYYMMDD-HHMMSS /mnt/@
     ```
  5. Reboot your system.

#### **7. Automating Snapshots with Snapper (Optional)**
For automated snapshots, you can use **Snapper**, a snapshot management tool that integrates with BTRFS and can automate the creation and deletion of snapshots.

- Install Snapper:
  ```bash
  sudo dnf install snapper
  ```

- Set up Snapper for root:
  ```bash
  sudo snapper -c root create-config /
  ```

You can now manage snapshots with Snapper, including automated snapshots before and after package installations.

#### **8. Managing Snapshot Storage**
Over time, snapshots can accumulate and take up space. BTRFS snapshots don’t consume much space initially, but as changes accumulate, they will take up more room. To delete old snapshots, run:
  ```bash
  sudo btrfs subvolume delete /snapshots/root-snapshot-YYYYMMDD-HHMMSS
  ```

#### **Is BTRFS Snapshot Sufficient for Rolling Back?**
Yes, **BTRFS snapshots** are typically **sufficient for rolling back** changes, especially if you're making system updates, configuration changes, or installing packages. Since the snapshot captures the entire state of the filesystem at the time of the snapshot, rolling back to it should restore your system to the exact state it was in before making changes.

However, snapshots are only effective if your system can boot into them. If a critical system failure occurs (such as bootloader corruption), additional recovery methods may be required.

### Conclusion:
Taking BTRFS snapshots on Fedora before making major system changes is an effective way to ensure you can safely roll back if needed. You can easily create on-demand snapshots using `btrfs` commands or automate the process using tools like Snapper. The snapshot will allow you to roll back to a previous state without affecting your current working data.