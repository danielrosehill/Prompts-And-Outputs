---
title: "Creating the Borg backup job using Vorta"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Setting Up a Recurrent Backup Job on Fedora Using Vorta (Borg Backup GUI)

This guide will help you set up a **recurrent backup job** on your Fedora desktop using **Vorta**, a graphical interface for **Borg Backup**. The goal is to create a **complete, hardware-agnostic backup** of your local filesystem. We’ll configure Vorta to run regular incremental backups, storing them on an external SSD mounted at `/mnt/desktop-backup`. The backup will be flexible enough to allow restoration onto different hardware setups.

### Prerequisites
- Fedora is installed on your system.
- An external SSD is mounted at `/mnt/desktop-backup`.
- **Vorta** (Borg Backup GUI) is installed.
- Sufficient storage space on the SSD to accommodate your backups.

### Step 1: Install Borg Backup and Vorta
First, you need to install **Borg Backup** and **Vorta** on your Fedora system:

```bash
sudo dnf install borgbackup
```

Next, install **Vorta** using `dnf` or `flatpak`:

```bash
sudo dnf install vorta
```

Or, if using Flatpak:

```bash
flatpak install flathub com.borgbase.Vorta
```

### Step 2: Launch Vorta and Initialize Borg Repository
1. **Launch Vorta**:
   - Open the Applications Menu and search for **Vorta**, then click to launch it.

2. **Initialize the Borg Repository**:
   - In Vorta, go to the **Repositories** tab.
   - Click **Add Repository** and choose **Initialize New Repository**.
   - Set the **Repository Location** to `/mnt/desktop-backup/borg-repo`.
   - Set **Encryption** to **Repokey** (recommended for better security).
   - Click **Initialize**.

### Step 3: Set Up Backup Profile
1. **Add a Backup Profile**:
   - In Vorta, go to the **Backup** tab.
   - Set the **Source Directories** to include all the necessary paths:
     - **Include**:
       - `/etc`: System configuration files.
       - `/home`: User data and settings.
       - `/var`: Logs and application data. *(Note: Exclude specific subdirectories like `/var/tmp` if not needed.)*
       - `/usr/local`: Custom-installed software and scripts.
       - `/root`: Root user’s home directory.
       - `/opt`: Typically used for manually installed applications, including AppImages.
       - `/var/lib/flatpak`: Flatpak application files.
       - `/var/lib/snapd`: Snap application files.
       - `/usr/share/applications`: Desktop entry files.
       - `/usr/share/icons`: Icons used by installed applications.
       - `/home/daniel/local/lib/python3.*/site-packages`: Python packages installed in the user directory.

2. **Exclude Paths**:
   - **Add the following paths to the Exclude List** to ensure a hardware-agnostic backup:
     - `/dev`: Device files, dynamically generated.
     - `/proc`: Kernel and process files, dynamically generated.
     - `/sys`: System information, dynamically generated.
     - `/tmp`: Temporary files.
     - `/run`: Runtime files, dynamically generated.
     - `/mnt` and `/media`: Avoid recursive backups.
     - `/lost+found`: Filesystem recovery data.
     - `/var/tmp`: Temporary files.
     - `/home/*/.cache`: User cache files.

3. **Repository**:
   - Choose the repository you just created (`/mnt/desktop-backup/borg-repo`) in the **Repositories** tab.

### Step 4: Configure Backup Schedule
1. **Set Up Backup Schedule**:
   - Go to the **Schedule** tab in Vorta.
   - Click **Add Schedule**.
   - Set the **Backup Frequency** to your preference, such as **Daily** at **2:00 AM**.
   - Ensure the **Incremental Backup** option is enabled to optimize storage usage.

2. **Pruning Settings**:
   - Under the **Schedule** tab, configure the **Prune Options** to manage older backups effectively.
   - Use the following settings to ensure that older backups are pruned automatically:
     - **Keep Daily**: 7
     - **Keep Weekly**: 4
     - **Keep Monthly**: 6
   - These settings will keep recent backups while pruning older ones, helping you save storage space.

### Step 5: Run the Initial Backup
- **Run the First Backup**:
  - Go to the **Backup** tab and click **Backup Now** to start the first backup.
  - This first backup may take some time depending on the size of your data.

### Step 6: Monitoring and Verification
1. **Monitoring Backups**:
   - You can monitor the progress of your backups from the **Activity** tab in Vorta.
   - Once completed, you can see statistics, such as the size of the data and the time taken for the backup.

2. **Verify Backups**:
   - It’s important to periodically verify the integrity of your backups.
   - Go to the **Archives** tab and click **Check** to verify that your backup repository is consistent and contains no errors.

### Step 7: Restoring from Backup
1. **Mount the Repository**:
   - Go to the **Archives** tab in Vorta.
   - Select the backup snapshot you want to restore.
   - Click **Mount** and choose a mount point (e.g., `/mnt/recovery`). This will mount the backup so you can browse through the files.

2. **Restore Files**:
   - Navigate to the mount point (e.g., `/mnt/recovery`) and copy the files you need back to their original locations.
   - You can use commands like `cp -a` or a file manager to restore files.

3. **Unmount the Repository**:
   - Once done, click **Unmount** in Vorta to safely detach the backup.

### Notes on Hardware-Agnostic Backups
- **Avoid Including RAID Configurations**: Exclude `/etc/mdadm.conf` if you plan on restoring the backup to a non-RAID setup.
- **AppImages and Flatpaks**: By including `/opt`, `/var/lib/flatpak`, and `/var/lib/snapd`, your AppImages, Flatpak apps, and Snap apps will be backed up, making reinstallation straightforward.
- **Python Packages**: Including the user-level Python packages directory ensures that any Python environments or packages installed are preserved.

### Summary
- **Install Borg Backup and Vorta** on your Fedora system.
- **Initialize a Borg repository** on your external SSD using Vorta.
- **Set up the Backup Profile** to include necessary system paths and exclude unnecessary ones for a hardware-agnostic backup.
- **Schedule automated backups** using Vorta’s Schedule tab to ensure backups are up-to-date.
- **Monitor backups** and verify their integrity periodically to ensure they remain usable.
- **Restore files** using the Vorta interface by mounting and copying files as needed.

By following these steps, you will have a reliable, **hardware-agnostic** backup of your Fedora system that is regularly updated and can be restored to new hardware easily if necessary. Vorta provides a convenient GUI for managing your backups, ensuring that all critical data and applications are backed up securely and efficiently.

