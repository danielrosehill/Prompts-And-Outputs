---
title: "Rclone built in sync and conflict handling"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Please expand upon the built in conflict resolution mechanisms available in rclone. I would ideally like to set up an automatic sync mechanism with my bucket whenever Obsidian is open. But if the app is closed, the sync shouldn't run so as to save on system resources. Would setting this up be possible?

# Output
Rclone offers several built-in conflict resolution mechanisms, particularly when using the `bisync` command. Here's an overview of the key options and how you might set up an automatic sync mechanism for your Obsidian vault:

## Rclone Conflict Resolution Mechanisms

1. `--conflict-resolve`: This flag allows you to automatically resolve conflicts by preferring one version over another. Options include:
   - `newer`: Prefer the newer file
   - `older`: Prefer the older file
   - `larger`: Prefer the larger file
   - `smaller`: Prefer the smaller file
   - `path1`: Always prefer the file from the first path (source)
   - `path2`: Always prefer the file from the second path (destination)

2. `--conflict-loser`: This determines what happens to the "losing" file in a conflict. Options include:
   - `delete`: Delete the losing file
   - `num`: Rename the losing file with a number suffix
   - `pathname`: Rename the losing file with a pathname suffix

3. `--conflict-suffix`: Allows you to specify a custom suffix for renamed conflict files.

4. `--resync`: This flag performs a full resync, useful after interruptions or when you suspect the sync state is incorrect.

5. `--resilient` and `--recover`: These flags help the sync process recover from interruptions automatically.

## Setting Up Automatic Sync for Obsidian

To set up an automatic sync mechanism that runs only when Obsidian is open, you could create a script that:

1. Checks if Obsidian is running
2. If it is, runs the rclone sync command
3. Sleeps for a set interval before checking again

Here's a basic bash script that could achieve this:

```bash
#!/bin/bash

OBSIDIAN_VAULT="/path/to/your/obsidian/vault"
B2_BUCKET="b2:your-bucket-name/obsidian"

while true; do
    if pgrep -x "obsidian" > /dev/null
    then
        echo "Obsidian is running. Syncing..."
        rclone bisync "$OBSIDIAN_VAULT" "$B2_BUCKET" \
            --create-empty-src-dirs \
            --compare size,modtime,checksum \
            --conflict-resolve newer \
            --conflict-loser num \
            --resilient \
            --recover
    else
        echo "Obsidian is not running. Skipping sync."
    fi
    sleep 300  # Wait for 5 minutes before checking again
done
```

To use this script:

1. Save it as `obsidian_sync.sh` and make it executable with `chmod +x obsidian_sync.sh`.
2. You can run this script in the background when you log in to your system.
3. Adjust the `OBSIDIAN_VAULT` and `B2_BUCKET` variables to match your setup.
4. Modify the sleep interval (currently set to 5 minutes) as needed.

This script will continuously check if Obsidian is running, perform a sync if it is, and then wait for 5 minutes before checking again. When Obsidian is closed, it will skip the sync operation.

Remember to test this setup thoroughly with non-critical data before using it with your actual Obsidian vault. Also, consider adding error handling and logging to the script for better monitoring and troubleshooting.




## Extracted Prompts
[[Prompts/Rclone built in sync and conflict handling.md#Prompt 1|Prompt 1]]
