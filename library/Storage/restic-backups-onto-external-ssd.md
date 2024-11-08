---
title: "Restic backups onto external SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can run backups using Restic from your Fedora computer directly onto the SSD mounted at `/mnt/desktop-backups`. Here’s how to set it up step by step:

### Step 1: Ensure Restic is Installed
Make sure Restic is installed on your Fedora system. If it’s not installed yet, you can do so with the following command:

```bash
sudo dnf install restic
```

### Step 2: Initialize the Restic Repository on the SSD
1. **Open a terminal** and initialize a new Restic repository on the SSD:
   ```bash
   restic init -r /mnt/desktop-backups
   ```
   - You will be prompted to set a password for the repository. Remember this password, as you'll need it for future backups and restores.

### Step 3: Create the Backup Script
Create a script that will handle the backup process. This script will specify what to back up and include options for excluding unnecessary files or directories.

1. **Create a Backup Script**:
   ```bash
   nano /home/daniel/backup-restic.sh
   ```

2. **Add the Following Content**:
   ```bash
   #!/bin/bash

   # Define variables
   REPOSITORY="/mnt/desktop-backups"
   EXCLUDES_FILE="/home/daniel/restic-excludes.txt"

   # Export the Restic repository password
   export RESTIC_PASSWORD="your-repository-password"

   # Run the Restic backup command
   restic backup --exclude-file=$EXCLUDES_FILE --one-file-system --verbose --progress -r $REPOSITORY /

   # Unset the password variable
   unset RESTIC_PASSWORD
   ```

   - Replace `"your-repository-password"` with the password you set when initializing the repository.

### Step 4: Create an Exclusion File
1. **Create an Exclusion File**:
   ```bash
   nano /home/daniel/restic-excludes.txt
   ```

2. **Add Directories to Exclude**:
   Here are some common directories to exclude:
   ```
   /mnt
   /proc
   /sys
   /dev
   /run
   /tmp
   /var/tmp
   ```
   - Save the file and exit.

### Step 5: Make the Backup Script Executable
```bash
chmod +x /home/daniel/backup-restic.sh
```

### Step 6: Run the Backup Script
You can now run your backup script:

```bash
./home/daniel/backup-restic.sh
```

### Step 7: Automate the Backup Process (Optional)
If you want to automate the backup process, you can schedule it using `cron`.

1. **Edit the Cron Jobs**:
   ```bash
   crontab -e
   ```

2. **Add a Line to Schedule the Backup**:
   For example, to run the backup script every Sunday at 2 AM, add:
   ```bash
   0 2 * * 0 /home/daniel/backup-restic.sh >> /var/log/restic-backup.log 2>&1
   ```

### Summary
1. **Install Restic**: Ensure it’s installed on your Fedora system.
2. **Initialize the Repository**: Set up a Restic repository on your SSD.
3. **Create a Backup Script**: Write a script to perform the backups, including exclusions.
4. **Run the Backup**: Execute the script to perform the backup.
5. **Automate with Cron**: Optionally, set up a cron job to automate future backups.

This setup will allow you to back up your Fedora system directly to your SSD, leveraging Restic's efficiency and features!