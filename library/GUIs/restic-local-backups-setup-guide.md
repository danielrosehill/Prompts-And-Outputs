---
title: "Restic local backups setup guide"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

OK. Are you ready to provide me with a guide on setting up the job with restic? To remind you of the details: we're going to be setting up a periodic incremental backup from my Fedora workstation desktop and pushing it to the home server Ubuntu VM over the LAN. I'd like this to run once a week after an initial successful validation. I don't want to backup too much unnecessary data. My focus here is on making sure that I'm backing up the system config as it changes. I'd like to capture my configuration files, the list of packages I have on the system, etc. But I'd probably prefer to use a preconfigured template if one exists as syncing a little unnecessary data won't be the end of the world.

# Output

Certainly! I'll provide you with a step-by-step guide to set up a periodic incremental backup from your Fedora workstation to your Ubuntu VM using Restic. This guide will focus on backing up system configurations and package information while minimizing unnecessary data.

Step 1: Install Restic on both systems

On your Fedora workstation:

```bash
sudo dnf install restic -y
```

On your Ubuntu VM:

```bash
sudo apt update
sudo apt install restic -y
```

Step 2: Initialize Restic Repository on Ubuntu VM

On your Ubuntu VM, create a directory for the backup:

```bash
sudo mkdir -p /path/to/backup/repo
sudo chown your_username:your_username /path/to/backup/repo
```

Initialize the repository:

```bash
restic init --repo /path/to/backup/repo
```

You'll be prompted to enter a password. Remember this password as you'll need it for backups and restores.

Step 3: Create a Backup Script on Fedora Workstation

Create a file named `restic_backup.sh` in your home directory:

```bash
nano ~/restic_backup.sh
```

Add the following content:

```bash
#!/bin/bash

# Restic environment variables
export RESTIC_REPOSITORY=sftp:your_username@ubuntu_vm_ip:/path/to/backup/repo
export RESTIC_PASSWORD=your_repository_password

# Backup system configurations and package list
restic backup \
    --tag fedora-config \
    --exclude-file=/home/your_username/.restic-exclude \
    /etc \
    /var/lib/rpm \
    /var/lib/dnf \
    /home/your_username/.config \
    /home/your_username/.local/share

# Backup package list
dnf list installed > /tmp/installed_packages.txt
restic backup --tag package-list /tmp/installed_packages.txt

# Cleanup old snapshots (keep last 4 weekly backups)
restic forget --keep-weekly 4 --prune
```

Make the script executable:

```bash
chmod +x ~/restic_backup.sh
```

Step 4: Create an Exclude File

Create a file named `.restic-exclude` in your home directory:

```bash
nano ~/.restic-exclude
```

Add patterns for files/directories you want to exclude:

```
*.log
*.tmp
*.cache
/var/cache
/var/tmp
/home/*/.cache
```

Step 5: Set Up SSH Key Authentication

Generate an SSH key on your Fedora workstation if you haven't already:

```bash
ssh-keygen -t rsa -b 4096
```

Copy the key to your Ubuntu VM:

```bash
ssh-copy-id your_username@ubuntu_vm_ip
```

Step 6: Schedule the Backup

Open your crontab file:

```bash
crontab -e
```

Add the following line to run the backup every Monday at 3 AM:

```
0 3 * * 1 /home/your_username/restic_backup.sh
```

Step 7: Initial Backup and Validation

Run the backup script manually for the first time:

```bash
~/restic_backup.sh
```

Verify the backup:

```bash
restic -r sftp:your_username@ubuntu_vm_ip:/path/to/backup/repo snapshots
```

This setup will create weekly incremental backups of your system configurations, installed packages list, and important user configuration files. It excludes unnecessary data and keeps the last 4 weekly backups.

Remember to replace `your_username`, `ubuntu_vm_ip`, and `/path/to/backup/repo` with your actual values. Also, ensure that you have sufficient permissions on both systems to read the source files and write to the backup location.

For added security, consider encrypting the backup repository password in the script using a tool like `gpg` or a secure password manager.

# Baseline resources note:

System resources on VM with HA + Ubuntu VMs running. So can definitely share some more space. And 6 TB = lots of storage. 
![[Restic local backups setup guide.png]]
