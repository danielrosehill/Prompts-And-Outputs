---
title: "Best live ISO for performing maintenance operations on Linux VMs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are several lightweight **Live ISO tools** specifically designed for disk management tasks such as resizing partitions, managing filesystems, and copying data, without the need to use a full Ubuntu ISO. These tools are perfect for the type of operation you're conducting—shrinking the filesystem and partition, managing LVM, and copying data between disks.

### Recommended Lightweight Live ISOs for Disk Management

#### 1. **GParted Live**
   - **GParted Live** is a small, dedicated Linux distribution built around the **GParted** partition editor. It’s a very lightweight and easy-to-use tool for resizing partitions, creating new partitions, and managing filesystems. It includes the necessary tools for LVM and filesystem resizing.
   
   **Key Features**:
   - Intuitive **GUI-based** interface.
   - Supports resizing **ext4**, **LVM**, and other filesystems.
   - Minimal resource usage, boots quickly.

   **How to Use**:
   - Download the **GParted Live ISO**: [GParted Live ISO Download](https://gparted.org/livecd.php)
   - Boot your VM using the GParted ISO via Proxmox.
   - Once booted, use **GParted** to shrink the filesystem and partition.
   - You can also mount the old and new disks and use `rsync` from the terminal to copy data.

#### 2. **SystemRescue (formerly SystemRescueCD)**
   - **SystemRescue** is another lightweight, bootable Linux distribution designed specifically for system and disk management. It includes all the necessary tools for managing LVM, resizing partitions, and copying data. Unlike GParted, this tool is more comprehensive, providing a wider range of system rescue and disk utilities.
   
   **Key Features**:
   - CLI-based tools for advanced users, with the option of GUI tools like **GParted**.
   - Includes **parted**, **rsync**, **lvm tools**, and **disk cloning** utilities.
   - Suitable for both partition management and system rescue.

   **How to Use**:
   - Download the **SystemRescue ISO**: [SystemRescue ISO Download](https://www.system-rescue.org/Download/)
   - Boot the VM from this ISO.
   - Use tools like `parted`, `lvreduce`, and `resize2fs` to shrink the partitions and filesystems.
   - Use `rsync` to copy data between old and new disks.

#### 3. **Parted Magic (Paid)**
   - **Parted Magic** is a well-known disk management toolkit that includes both **GParted** and a number of other tools for cloning, file recovery, and partitioning. It’s not free but has a very polished, professional set of tools that can simplify the process even more.
   
   **Key Features**:
   - GUI-based tools like **GParted** and **Clonezilla**.
   - Comprehensive disk utilities for partitioning, cloning, and file recovery.
   - Works well with both SSDs and traditional HDDs.

   **How to Use**:
   - Download the **Parted Magic ISO**: [Parted Magic ISO Download](https://partedmagic.com/)
   - Boot the VM using the ISO.
   - Use the **GParted** tool to manage partitions, or use **Clonezilla** to copy partitions and data between disks.

#### 4. **Clonezilla Live**
   - **Clonezilla Live** is primarily designed for cloning and imaging disks, but it also includes tools for disk partitioning and resizing. If you are comfortable with command-line tools and want to clone your 2TB disk to the new 100GB disk while resizing partitions, **Clonezilla** might be a good option.
   
   **Key Features**:
   - Excellent for cloning and imaging entire disks.
   - CLI-based tool, but includes support for partition resizing.
   - Works well for moving data between disks or shrinking partitions during cloning.

   **How to Use**:
   - Download the **Clonezilla Live ISO**: [Clonezilla ISO Download](https://clonezilla.org/downloads.php)
   - Boot the VM using Clonezilla from Proxmox.
   - Follow the **disk cloning** process and use Clonezilla’s options to resize the filesystem to fit within 100GB during the copy process.

#### 5. **Rescuezilla**
   - **Rescuezilla** is a graphical disk imaging and cloning tool that’s extremely easy to use. It is essentially a GUI front-end for Clonezilla but makes it more user-friendly and adds additional recovery and partitioning features.
   
   **Key Features**:
   - **Clonezilla**-based but more user-friendly, with a GUI.
   - Can resize partitions during cloning or imaging.
   - Great for disk-to-disk migration or backup with ease.

   **How to Use**:
   - Download the **Rescuezilla ISO**: [Rescuezilla ISO Download](https://rescuezilla.com/)
   - Boot the VM with Rescuezilla.
   - Clone the disk while resizing to the smaller size during the cloning process.

### Recommended Option:
For your purposes—shrinking a filesystem and copying data between disks—I recommend **GParted Live** or **SystemRescue**. These are lightweight and provide both graphical and command-line options for managing partitions and filesystems. Both include the necessary tools for managing **LVM**, **ext4**, and **rsync** for copying data between the old and new disk.

### Conclusion:
- **GParted Live**: Best for GUI-based operations. Simple and focused on disk management.
- **SystemRescue**: Best for advanced users needing more comprehensive CLI tools.
- **Clonezilla** or **Rescuezilla**: Best for cloning the entire disk while shrinking partitions during the process.

Let me know if you need more specific guidance on any of these tools or further steps in your disk resizing process!