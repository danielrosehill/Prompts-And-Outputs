---
title: "How to set up REAR on new SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:** You are asking how to set up a backup of your **Fedora system** using **ReaR** with a USB device located at `/run/media/daniel/Backups`. You want the same USB device to be used for **storing the backups** and for creating the **bootable recovery environment**.

Here’s a step-by-step guide on how to set up **ReaR** (Relax-and-Recover) to back up your Fedora system and configure the USB device as both the **backup storage** and **bootable live recovery disk**.

---

### **Step-by-Step Guide for Setting Up ReaR with a USB Backup and Boot Disk**

### **1. Install ReaR on Fedora**
First, install ReaR using **dnf**:

```bash
sudo dnf install rear
```

### **2. Configure ReaR**
You need to configure ReaR to store the backup on the USB drive and make the USB drive bootable.

1. Open the **ReaR configuration file** for editing:
   ```bash
   sudo nano /etc/rear/local.conf
   ```

2. Add the following configuration options. These tell ReaR where to store the backup and how to create a bootable recovery environment on your USB drive:

```bash
# Set up the output type as a USB stick
OUTPUT=USB

# The path to your USB device (this should be the mount point of your USB device)
BACKUP_URL=usb:///run/media/daniel/Backups

# Specify how the backup should be done (using tar or rsync for full system backup)
BACKUP=NETFS

# Define which backup program to use (you can use rsync, or tar - depending on your needs)
BACKUP_PROG=rsync

# USB device that will be used for the backup and recovery (match with your USB's device node)
USB_DEVICE=/run/media/daniel/Backups

# Optionally, specify file system type for the USB stick (ext4 recommended for Linux systems)
USB_FILESYSTEM=ext4

# Set the GRUB2 bootloader on the USB for booting
GRUB_RESCUE=1
```

- **BACKUP_URL**: This is where the backup will be stored. In this case, it's pointing to your USB mount point.
- **BACKUP=NETFS**: This tells ReaR to use the local filesystem (in this case, the USB) for the backup.
- **BACKUP_PROG=rsync**: This tells ReaR to use **rsync** for the backup, which is efficient for copying files.

### **3. Format the USB Drive (if needed)**
If your USB drive isn’t formatted yet, format it with **ext4** to ensure compatibility:

```bash
sudo mkfs.ext4 /dev/sdX  # Replace /dev/sdX with your actual USB device name
```

You can check your USB device's name using `lsblk` to find out which drive it is, and make sure it's not mounted when formatting.

### **4. Run ReaR to Create the Backup and Live Recovery Disk**

Once you have configured ReaR and prepared your USB, you can create the backup and bootable USB drive using the following command:

```bash
sudo rear -v mkbackup
```

This command will:
1. Create a backup of your system on the USB drive.
2. Make the USB drive bootable with a recovery environment.

- The **`-v`** flag provides verbose output to give you more detailed information about the process.
- The backup will be stored in the **BACKUP_URL** directory you configured earlier.

### **5. Verify the Bootable USB**
Once the process is complete, you can verify that the USB is now bootable. You can do this by restarting your machine, booting into your BIOS or boot menu, and selecting the USB device as the boot option.

### **6. Test Restoring from the USB Drive**
To test restoring from the USB drive, follow these steps:

1. **Boot from the USB**: Insert the USB into the machine and boot from it. This will launch the ReaR recovery environment.
2. **Recover the Backup**: From the ReaR recovery environment, you can start the restore process by running the following command:
   ```bash
   rear recover
   ```

ReaR will restore the backup from the USB device to your system, essentially rebuilding your Fedora system from the backup.

---

### **What Happens During Backup and Recovery:**

- **Backup Process**:
  - ReaR will create a backup of your Fedora system, including configurations and files, and store it on the USB.
  - The USB will also contain a bootable recovery environment.

- **Recovery Process**:
  - If your system fails, you can boot from the USB.
  - The ReaR recovery environment will allow you to restore the system from the backup on the same USB drive.

---

### **Conclusion:**

This guide walks you through setting up ReaR to use the same USB drive for both storing backups and creating a bootable recovery disk. By following these steps, you can have a full backup of your Fedora system and a way to recover from it in case of failure.

Key takeaways:
- **ReaR** makes both **backups** and **bare-metal restores** easy.
- The USB drive will store your backups and act as the **bootable recovery environment**.
