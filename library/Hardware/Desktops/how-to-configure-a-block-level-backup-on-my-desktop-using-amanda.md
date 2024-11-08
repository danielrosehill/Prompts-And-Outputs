---
title: "How to configure a block level backup on my desktop using Amanda"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking how to configure a **block-level backup** from your current Fedora computer to your **NAS** located at `192.168.1.50:/volume1/danieldesktopbackups`, mounted at `/mnt/nas`.

To configure a **block-level backup** using **Amanda** (or any similar tool), the process involves preparing the NAS as the backup target and configuring Amanda to back up an entire disk or partition from your Fedora system.

Here's how to set it up for a **block-level backup** using **Amanda**:

### Steps to Configure a Block-Level Backup from Fedora to Your NAS:

#### 1. **Mount the NAS Share on Fedora**
First, ensure the **NAS share** is correctly mounted. You can add it to `/etc/fstab` for automatic mounting at boot.

```bash
sudo mkdir -p /mnt/nas
sudo mount -t nfs 192.168.1.50:/volume1/danieldesktopbackups /mnt/nas
```

Make sure it's accessible:
```bash
df -h | grep /mnt/nas
```

If it's not mounted automatically after a reboot, add this to `/etc/fstab`:
```
192.168.1.50:/volume1/danieldesktopbackups /mnt/nas nfs defaults 0 0
```

#### 2. **Install Amanda on Fedora**
Install Amanda server and client packages:
```bash
sudo dnf install amanda amanda-server amanda-client
```

#### 3. **Configure Amanda for Block-Level Backup**
Now, let's configure Amanda to perform a **block-level backup**.

##### a. **Edit Amanda Configuration Files**
The Amanda configuration files are located in `/etc/amanda`. You'll need to edit the `amanda.conf` and `disklist` files to define how and where the backups will be stored.

- **Edit `/etc/amanda/<config>/amanda.conf`**:

  In `amanda.conf`, specify the location where the backups will be stored (your NAS in this case):

  - Add or modify the **holdingdisk** and **tapedev** parameters:
    ```bash
    holdingdisk {
        directory "/mnt/nas"    # Backup data is stored here before being written to tape (or NAS in this case)
        use 10000 MB             # Maximum space to use for holding data
    }

    tapedev "file:/mnt/nas"      # Backup is written to this file/tape device
    ```

  - You can adjust `holdingdisk` and `tapedev` depending on your needs (e.g., the size of your backups and available space).

##### b. **Configure Disklist for Block-Level Backup**
Edit `/etc/amanda/<config>/disklist` to specify which **block devices** (disks or partitions) should be backed up.

- **Block-level backup** uses Amanda's `amraw` feature, which backs up the entire block device.

  Example for `/dev/sda` (your primary disk):
  ```bash
  fedora-hostname /dev/sda amraw
  ```

  This tells Amanda to back up the entire `/dev/sda` disk as a raw block device. Replace `fedora-hostname` with your machine's hostname.

##### c. **Set Backup Schedule (Optional)**
If you want to automate this process, you can set up a backup schedule in Amanda. Typically, this is handled by Amanda's internal scheduling system, but you can also use **cron** to trigger Amanda backups at regular intervals.

#### 4. **Test the Configuration**
Run a test backup to ensure everything is set up correctly:
```bash
sudo amdump <config>
```
- `<config>` refers to the name of your Amanda configuration directory (e.g., `/etc/amanda/<config>`).

You can monitor the progress of the backup and check for any errors in Amanda's log files located in `/var/log/amanda/`.

#### 5. **Restore from Backup**
If you need to restore a block-level backup, you can use Amanda's **amrestore** tool to recover data from your NAS.

Example command to restore data:
```bash
sudo amrestore /mnt/nas <backup_name>
```

You will need to specify the backup name and destination for restoration.

### Conclusion:
- **Amanda** can be configured to perform **block-level backups** by specifying raw devices (e.g., `/dev/sda`) in the `disklist` file.
- The NAS at `192.168.1.50:/volume1/danieldesktopbackups` mounted at `/mnt/nas` will act as the storage location for the backups.
- With the correct configuration in **`amanda.conf`** and **`disklist`**, Amanda will back up your entire disk and store it on your NAS.
  
Let me know if you'd like further details on any part of this setup!