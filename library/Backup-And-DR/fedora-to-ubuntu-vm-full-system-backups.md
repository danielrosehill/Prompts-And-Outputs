---
title: "Fedora to Ubuntu VM full system backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have an Ubuntu server on my LAN at 192.168.1.5.
I'd like to create incremental backups of my Fedora computer 
I would like these backups to be full system backups - although I would want to exclude a few directories like /mnt
The purpose of these backups would be to be able to restore the system onto new hardware if required (after the OS has already been reinstalled).
I'd like a backup tool that is easy to administer, so a GUI would be preferable. The backups should run automatically once a week. 
Please suggest some appropriate solutions and describe how to implement them

# Output

Here are some GUI-based solutions suitable for creating full system incremental backups from your Fedora computer to your Ubuntu server, which can be scheduled to run weekly:

### 1. **Veeam Agent for Linux**
   - **Description**: Veeam Agent is a powerful, user-friendly backup tool with a GUI that can perform full system backups, including incremental updates. It supports automated scheduling and restoration to different hardware.
   - **Pros**: Easy to set up and manage with a graphical interface. Supports incremental backups, encryption, and scheduling. Can restore the system to new hardware.
   - **Cons**: Proprietary software, but free for personal use.
   
#### Implementation:
1. **Install Veeam Agent**:
   - On **Fedora**:
     1. Download the Veeam Agent package from [Veeam's website](https://www.veeam.com/linux-backup-free.html).
     2. Follow the installation instructions provided on the website.
   - On **Ubuntu server**:
     Ensure the destination folder where the backups will be stored is ready and accessible via SSH.

2. **Configure Veeam Agent**:
   - Launch the Veeam Agent GUI on Fedora.
   - Create a new backup job, selecting the entire system for backup.
   - Specify the Ubuntu server as the destination:
     - Use an SSH connection (`user@192.168.1.5:/path/to/backup-folder`).
     - Provide authentication and ensure SSH keys are configured if needed.
   - Set up exclusions for directories you do not want to back up (e.g., `/mnt`).
   - Schedule the backup to run weekly.

3. **Automate Backups**:
   - Veeam's GUI allows for easy scheduling, ensuring backups run automatically.

4. **Restoration**:
   - If you need to restore, Veeam allows you to create bootable recovery media. You can use it to restore the backup to new hardware.

### 2. **UrBackup**
   - **Description**: UrBackup is an open-source backup solution with a web-based GUI. It supports full and incremental backups and can be configured to back up over a network.
   - **Pros**: Open-source, web interface for managing backups, supports incremental backups and easy setup.
   - **Cons**: More suitable for network environments, requires setting up both server and client components.

#### Implementation:
1. **Set Up UrBackup Server on Ubuntu**:
   - Install the server on your Ubuntu VM:
     ```bash
     sudo apt install urbackup-server
     ```
   - Access the web GUI at `http://192.168.1.5:55414`.

2. **Install UrBackup Client on Fedora**:
   - Download and install the client from the [UrBackup website](https://www.urbackup.org/).
   - During setup, specify the server address (`192.168.1.5`) and configure the directories to back up.
   - Exclude unwanted directories like `/mnt`.

3. **Configure Backup Jobs via Web GUI**:
   - Log into the UrBackup web interface.
   - Create a new backup job for the Fedora client, ensuring it’s set for full backups with incremental updates.
   - Schedule it to run weekly.

4. **Restoration**:
   - UrBackup allows easy file restoration through the web GUI or full recovery if you need to restore the system onto new hardware.

### 3. **Timeshift + Rsync Setup with GUI**
   - **Description**: While Timeshift is typically used for creating system snapshots, combining it with rsync and a manual configuration can allow you to back up full systems to remote destinations. The Timeshift GUI makes it easier to manage settings and schedules.
   - **Pros**: Integrated with many Linux environments, GUI for easy management, can use rsync to push backups to the Ubuntu server.
   - **Cons**: Primarily meant for local backups, so requires a bit of configuration for remote setups.

#### Implementation:
1. **Install Timeshift**:
   - On **Fedora**:
     ```bash
     sudo dnf install timeshift
     ```
   
2. **Configure Timeshift**:
   - Launch Timeshift and set it up to take snapshots of your system, excluding directories like `/mnt`.
   - Configure rsync as the backup type.

3. **Automate Transfer with Cron and Rsync**:
   - Set up a cron job to regularly use rsync to transfer Timeshift snapshots to your Ubuntu server.
   - Example rsync command:
     ```bash
     rsync -avz /timeshift/snapshots user@192.168.1.5:/path/to/backup-folder
     ```

4. **Schedule Automatic Snapshots**:
   - Use the Timeshift GUI to schedule weekly snapshots.

5. **Restoration**:
   - Timeshift provides tools to restore snapshots to a fresh install, though transferring to new hardware may involve more manual steps.

### Recommendation:
**Veeam Agent for Linux** is the best fit if you want an easy-to-administer solution with a clean GUI, straightforward scheduling, and comprehensive system recovery capabilities. For an open-source solution, **UrBackup** offers a reliable web-based interface that can handle full system backups and incremental updates over the network. Both solutions will allow you to set up automated weekly backups and manage them easily.