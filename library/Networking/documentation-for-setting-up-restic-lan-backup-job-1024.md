---
title: "Documentation for setting up Restic LAN backup job 1024"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

OK, restic sounds good. Please write a full guide. Please cover how to set up the backup job on my fedora computer recalling that I'll want to exclude directories that would not be helpful in the event of a restore (but otherwise capture a full system backup). My local is Fedora. The backup server is at 192.168.1.1 and is an Ubuntu VM. And the target path on the backup server is /srv/backups/daniel-desktpo

# Output

Here is a complete guide to setting up Restic for incremental backups from your Fedora desktop to an Ubuntu VM located at `192.168.1.1`, with the target path being `/srv/backups/daniel-desktop`. The guide will cover installation, configuration, and setting up automated backups.

### Step 1: Install Restic on Both Fedora and Ubuntu
1. **On Fedora (Desktop)**:
   ```bash
   sudo dnf install restic
   ```

2. **On Ubuntu (Backup Server)**:
   ```bash
   sudo apt install restic
   ```

### Step 2: Prepare the Backup Repository on the Ubuntu Server
1. **SSH into the Ubuntu Server**:
   ```bash
   ssh daniel@192.168.1.1
   ```

2. **Create the Target Directory**:
   ```bash
   sudo mkdir -p /srv/backups/daniel-desktop
   sudo chown daniel:daniel /srv/backups/daniel-desktop
   ```

3. **Initialize the Restic Repository**:
   ```bash
   restic init -r /srv/backups/daniel-desktop
   ```
   - You will be prompted to create a password for the repository. Make sure to remember this password, as it will be required for backups and restores.

### Step 3: Set Up SSH Access Without Passwords
To automate the backup process, it’s best to set up SSH key-based authentication so that your Fedora desktop can access the Ubuntu VM without needing to enter a password every time.

1. **Generate SSH Keys on Fedora**:
   ```bash
   ssh-keygen
   ```
   - Save the keys (use default paths), and **do not set a passphrase** to allow automation.

2. **Copy the Public Key to the Ubuntu Server**:
   ```bash
   ssh-copy-id daniel@192.168.1.1
   ```

3. **Test the Connection**:
   ```bash
   ssh daniel@192.168.1.1
   ```
   - You should be able to log in without entering a password.

### Step 4: Create the Backup Script on Fedora
1. **Choose What to Exclude**:
   Based on your requirement to exclude unnecessary directories, consider excluding the following:
   - `/mnt`: To avoid backing up mounted drives.
   - `/proc`, `/sys`, `/dev`, `/run`, `/tmp`: System directories that do not need to be backed up.
   - `/var/tmp`: Temporary data.

2. **Create a File with Excluded Paths**:
   ```bash
   nano /home/daniel/restic-excludes.txt
   ```
   - Add the following content:
     ```
     /mnt
     /proc
     /sys
     /dev
     /run
     /tmp
     /var/tmp
     ```

3. **Write the Backup Script**:
   ```bash
   nano /home/daniel/backup-restic.sh
   ```
   - Add the following script:
     ```bash
     #!/bin/bash

     # Define variables
     REPOSITORY="sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop"
     EXCLUDES_FILE="/home/daniel/restic-excludes.txt"

     # Export the Restic repository password
     export RESTIC_PASSWORD="your-repository-password"

     # Run the Restic backup command
     restic backup --exclude-file=$EXCLUDES_FILE --one-file-system -r $REPOSITORY /

     # Unset the password variable
     unset RESTIC_PASSWORD
     ```

   - Replace `"your-repository-password"` with the password you set up when you initialized the repository.
   - **Explanation**:
     - `--exclude-file=$EXCLUDES_FILE`: Excludes directories listed in `restic-excludes.txt`.
     - `--one-file-system`: Ensures Restic doesn’t cross filesystem boundaries, which prevents it from backing up mounted drives.

4. **Make the Script Executable**:
   ```bash
   chmod +x /home/daniel/backup-restic.sh
   ```

### Step 5: Automate Backups Using Cron
1. **Edit the Cron Jobs**:
   ```bash
   crontab -e
   ```

2. **Add the Following Line for Weekly Backups (e.g., Every Sunday at 2 AM)**:
   ```bash
   0 2 * * 0 /home/daniel/backup-restic.sh >> /var/log/restic-backup.log 2>&1
   ```

3. **Verify the Cron Job**:
   - Check your cron jobs:
     ```bash
     crontab -l
     ```

### Step 6: Verify and Test Backups
1. **List Snapshots**:
   You can check the backups by listing the snapshots from your Fedora machine:
   ```bash
   export RESTIC_PASSWORD="your-repository-password"
   restic snapshots -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop
   unset RESTIC_PASSWORD
   ```

2. **Restore a Backup**:
   - To restore a full backup to a specific directory:
     ```bash
     restic restore latest -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop --target /restore-directory
     ```

### Step 7: Additional Recommendations
1. **Security**: Make sure your backup script and exclude file are secured so that sensitive information is not exposed.
   ```bash
   chmod 600 /home/daniel/backup-restic.sh /home/daniel/restic-excludes.txt
   ```
2. **Monitoring**: Regularly check `/var/log/restic-backup.log` to confirm that backups are running successfully.

### Summary
1. **Install Restic** on both systems.
2. **Set up SSH keys** for passwordless authentication.
3. **Initialize the Restic repository** on the Ubuntu server.
4. **Create a backup script** on Fedora, specifying what to exclude.
5. **Automate backups using cron** to run once a week.
6. **Verify backups and perform test restores** as needed.

This setup ensures regular, automated incremental backups of your Fedora desktop to the Ubuntu VM, with exclusions for unnecessary directories.