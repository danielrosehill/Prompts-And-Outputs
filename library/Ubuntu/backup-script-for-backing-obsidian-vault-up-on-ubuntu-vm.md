---
title: "Backup script for backing Obsidian vault up on Ubuntu VM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great work. Now let's work on a simplified version of this backup strategy. Let's write a script for a backup agent that runs on the Ubuntu VM. Every night at midnight it does an incremental pull. Once a week it takes an archive of the vault and it create a timestamped archive in the format ddmmyy.tar.gz that it writes to /snapshots (relative to the directory where the script is running. The live copy (which is remote to local only) can go to /vaultreplica
To preserve space, only the latest 5 archiveds should be retained. 

# Output

Here is a simplified **bash script** for your **Ubuntu VM** backup agent. This script will:

1. **Pull a nightly incremental backup** of your Obsidian vault to `/vaultreplica`.
2. **Once a week**, it will create a timestamped archive of the vault in `/snapshots`.
3. **Automatically remove older archives**, retaining only the most recent 5.

### Script: `vault_backup.sh`

```bash
#!/bin/bash

# Directories
VAULT_REMOTE="your_remote_vault_location"  # Replace with the actual remote vault location
VAULT_REPLICA_DIR="./vaultreplica"
SNAPSHOT_DIR="./snapshots"

# Create directories if they don't exist
mkdir -p "$VAULT_REPLICA_DIR"
mkdir -p "$SNAPSHOT_DIR"

# Step 1: Perform nightly incremental pull (sync from remote to local)
echo "Performing nightly incremental sync..."
rsync -avz --delete "$VAULT_REMOTE" "$VAULT_REPLICA_DIR"

# Step 2: Weekly snapshot (archive with timestamp)
DAY_OF_WEEK=$(date +%u)  # Get the day of the week (1 = Monday, 7 = Sunday)

if [ "$DAY_OF_WEEK" -eq 7 ]; then
    TIMESTAMP=$(date +%d%m%y)  # Format timestamp as ddmmyy
    ARCHIVE_NAME="vault_$TIMESTAMP.tar.gz"

    echo "Creating weekly snapshot: $ARCHIVE_NAME"
    tar -czf "$SNAPSHOT_DIR/$ARCHIVE_NAME" -C "$VAULT_REPLICA_DIR" .

    # Step 3: Remove older snapshots, retain only the latest 5
    echo "Removing older snapshots..."
    ls -tp "$SNAPSHOT_DIR"/*.tar.gz | tail -n +6 | xargs -I {} rm -- {}
fi

echo "Backup process completed."
```

### Explanation:

- **Nightly Sync**: The script runs `rsync` to sync from your remote vault location (`VAULT_REMOTE`) to the local directory `/vaultreplica`. It includes the `--delete` option to ensure that deleted files in the remote vault are reflected in the local copy.
  
- **Weekly Snapshot**: If the script is running on a Sunday (`DAY_OF_WEEK = 7`), it creates a timestamped `.tar.gz` archive of the current vault in `/snapshots`. The archive is named using the format `ddmmyy.tar.gz`.

- **Snapshot Retention**: The script retains only the **latest 5 snapshots**, removing older ones using `ls -tp` to list the files by time and `tail -n +6` to select the older files for deletion.

### How to Schedule the Script:
1. **Make the script executable**:
   ```bash
   chmod +x vault_backup.sh
   ```

2. **Set up a cron job** to run the script every night at midnight:
   ```bash
   crontab -e
   ```

   Add the following line to the crontab file:
   ```bash
   0 0 * * * /path/to/vault_backup.sh >> /path/to/vault_backup.log 2>&1
   ```

This will run the backup script at **00:00 (midnight)** every day and log the output to `vault_backup.log`.

### Additional Notes:
- Replace `your_remote_vault_location` with the actual path or remote address of your Obsidian vault.
- Ensure that the script has the necessary permissions to access the remote vault and local directories.
- **Error handling** and **logging** could be added for more advanced monitoring and troubleshooting.