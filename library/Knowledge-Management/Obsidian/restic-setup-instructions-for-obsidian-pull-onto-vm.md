---
title: "Restic setup instructions for Obsidian pull onto VM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s how to set up **Restic** to manage your remote-to-local backups from **Backblaze B2** to your **Ubuntu VM**. Restic will handle syncing, including deletions, and will create automated, incremental backups with file versioning.

### **Restic Configuration for Remote-to-Local Backup (Syncing Deletions)**

Since **Restic** is already installed, we’ll focus on configuring it to:
1. Pull data from **Backblaze B2**.
2. Ensure deletions are synced (remote-to-local).
3. Schedule nightly backups and weekly snapshots.
4. Automate cleanup to retain the latest snapshots.

---

### **Step 1: Initialize the Restic Repository**

1. **Set Backblaze B2 Environment Variables**:
   To avoid having to type in your credentials every time you run a backup, store your B2 credentials in environment variables:
   ```bash
   export B2_ACCOUNT_ID=<your_b2_account_id>
   export B2_APPLICATION_KEY=<your_b2_application_key>
   ```

2. **Initialize the Restic Repository** (if you haven’t already):
   If this is your first time using Restic with B2, initialize the repository with the following command:
   ```bash
   restic -r b2:<bucket-name>:<folder-name> init
   ```
   Replace `<bucket-name>` with your B2 bucket name, and `<folder-name>` with the path inside the bucket where you want to store the backup data.

---

### **Step 2: Create the Backup Scripts**

#### **Nightly Incremental Backup (Remote to Local with Deletions Synced)**

1. **Create a backup script**:
   Open a new file for your nightly backup script:
   ```bash
   nano ~/restic_backup.sh
   ```

2. **Add the Restic backup command**:
   ```bash
   #!/bin/bash
   # Export environment variables
   export B2_ACCOUNT_ID=<your_b2_account_id>
   export B2_APPLICATION_KEY=<your_b2_application_key>
   
   # Perform a backup from Backblaze B2 to local directory
   restic -r b2:<bucket-name>:<folder-name> pull --delete --verbose
   ```

3. **Explanation**:
   - `-r b2:<bucket-name>:<folder-name>`: Specifies the B2 repository.
   - `pull`: Ensures data is copied from remote (B2) to local.
   - `--delete`: Syncs deletions from the remote repository to the local.
   - `--verbose`: Provides detailed output.

4. **Save and exit** (`Ctrl + X`, then `Y`).

5. **Make the script executable**:
   ```bash
   chmod +x ~/restic_backup.sh
   ```

#### **Weekly Snapshot Script**

1. **Create a weekly snapshot script**:
   Open a new file for your weekly snapshot script:
   ```bash
   nano ~/restic_weekly_snapshot.sh
   ```

2. **Add the Restic snapshot command**:
   ```bash
   #!/bin/bash
   # Export environment variables
   export B2_ACCOUNT_ID=<your_b2_account_id>
   export B2_APPLICATION_KEY=<your_b2_application_key>
   
   # Perform a weekly snapshot (pull data from B2 and store locally)
   TIMESTAMP=$(date +%d%m%y)
   SNAPSHOT_DIR="~/snapshots/vault_$TIMESTAMP.tar.gz"
   
   restic -r b2:<bucket-name>:<folder-name> pull --delete --verbose
   tar -czf $SNAPSHOT_DIR ~/vaultreplica
   ```

3. **Save and exit** (`Ctrl + X`, then `Y`).

4. **Make the script executable**:
   ```bash
   chmod +x ~/restic_weekly_snapshot.sh
   ```

---

### **Step 3: Set Up Cron Jobs for Automation**

#### **Nightly Backup Job**
1. **Schedule nightly incremental backups** to run at midnight:
   ```bash
   crontab -e
   ```
2. Add the following line to run the backup script every night at 00:00:
   ```bash
   0 0 * * * /bin/bash ~/restic_backup.sh >> ~/restic_backup.log 2>&1
   ```

#### **Weekly Snapshot Job**
1. **Schedule weekly snapshots** to run every Sunday at 2:00 AM:
   ```bash
   crontab -e
   ```
2. Add the following line to run the snapshot script:
   ```bash
   0 2 * * 7 /bin/bash ~/restic_weekly_snapshot.sh >> ~/restic_weekly_snapshot.log 2>&1
   ```

---

### **Step 4: Retain the Latest 5 Snapshots**

Restic automatically manages snapshots, but if you want to ensure only the last 5 are kept locally, use the `forget` and `prune` commands in your weekly snapshot script:

1. Modify your **weekly snapshot script** (`~/restic_weekly_snapshot.sh`):
   ```bash
   #!/bin/bash
   # Export environment variables
   export B2_ACCOUNT_ID=<your_b2_account_id>
   export B2_APPLICATION_KEY=<your_b2_application_key>
   
   # Perform a weekly snapshot
   TIMESTAMP=$(date +%d%m%y)
   SNAPSHOT_DIR="~/snapshots/vault_$TIMESTAMP.tar.gz"
   
   restic -r b2:<bucket-name>:<folder-name> pull --delete --verbose
   tar -czf $SNAPSHOT_DIR ~/vaultreplica

   # Prune old snapshots
   restic -r b2:<bucket-name>:<folder-name> forget --keep-last 5 --prune
   ```

---

### **Step 5: Test the Setup**

1. **Run the backup manually** to ensure it works as expected:
   ```bash
   ~/restic_backup.sh
   ```

2. **Check the logs** (`~/restic_backup.log` and `~/restic_weekly_snapshot.log`) to ensure the sync and snapshots are being executed properly.

---

### **Conclusion**:
With this configuration, Restic will perform **nightly remote-to-local incremental backups**, syncing file changes (including deletions), and **weekly snapshots** with retention of the latest 5 snapshots. Restic’s automation via cron will ensure everything runs smoothly without needing manual intervention.

Let me know if you need further adjustments or explanations!