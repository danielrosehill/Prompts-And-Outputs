---
title: "Inspecting B2 bucket to verify Obsidian is storing correctly"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I'm syncing my Obsidian notes to B2. I'd love to have some way to make sure that the sync is working correctly. Ideally this would involve inspecting the B2 bucket that I'm syncing these with. Can you think of any way to do this? I'm using Fedora Linux.

# Output

Certainly! You can set up a system to verify that your Obsidian notes are syncing correctly to your Backblaze B2 bucket. Here's an approach you can use on your Fedora Linux system:

## Using rclone to Verify Sync

Rclone is an excellent tool for this purpose, as it supports Backblaze B2 and can be easily automated. Here's how you can set it up:

1. Install rclone:
   ```
   sudo dnf install rclone
   ```

2. Configure rclone for your B2 bucket:
   ```
   rclone config
   ```
   Follow the prompts to set up a new remote for your B2 bucket.

3. Create a script to check sync status:
   Create a file named `check_obsidian_sync.sh` with the following content:

   ```bash
   #!/bin/bash

   # Path to your local Obsidian vault
   LOCAL_PATH="/path/to/your/obsidian/vault"

   # Name of your rclone B2 remote and bucket
   B2_REMOTE="your-b2-remote:your-bucket-name"

   # Run rclone check
   OUTPUT=$(rclone check "$LOCAL_PATH" "$B2_REMOTE" --fast-list)

   # Count the number of differences
   DIFF_COUNT=$(echo "$OUTPUT" | grep -c "ERROR")

   # Send email with results
   if [ $DIFF_COUNT -eq 0 ]; then
     echo "Obsidian sync check: OK" | mail -s "Obsidian Sync Status" your@email.com
   else
     echo "Obsidian sync check: $DIFF_COUNT differences found. Details:\n\n$OUTPUT" | mail -s "Obsidian Sync Status - ATTENTION NEEDED" your@email.com
   fi
   ```

4. Make the script executable:
   ```
   chmod +x check_obsidian_sync.sh
   ```

5. Set up a cron job to run this script regularly:
   ```
   crontab -e
   ```
   Add a line like this to run the check daily at 9 AM:
   ```
   0 9 * * * /path/to/check_obsidian_sync.sh
   ```

## Additional Considerations

1. **File Count Check**: You can add a simple file count comparison to your script:

   ```bash
   LOCAL_COUNT=$(find "$LOCAL_PATH" -type f | wc -l)
   B2_COUNT=$(rclone size "$B2_REMOTE" --fast-list | grep "Total objects:" | awk '{print $3}')

   echo "Local files: $LOCAL_COUNT, B2 files: $B2_COUNT" >> $OUTPUT
   ```

2. **Size Comparison**: Similarly, you can compare total sizes:

   ```bash
   LOCAL_SIZE=$(du -sb "$LOCAL_PATH" | cut -f1)
   B2_SIZE=$(rclone size "$B2_REMOTE" --fast-list | grep "Total size:" | awk '{print $3}')

   echo "Local size: $LOCAL_SIZE, B2 size: $B2_SIZE" >> $OUTPUT
   ```

3. **Last Modified Check**: You can check the last modified time of the most recent file in both locations to ensure recent changes are syncing:

   ```bash
   LOCAL_LATEST=$(find "$LOCAL_PATH" -type f -printf '%T@ %p\n' | sort -n | tail -1)
   B2_LATEST=$(rclone lsl "$B2_REMOTE" --max-depth 1 --fast-list | sort -k2 | tail -1)

   echo "Local latest: $LOCAL_LATEST, B2 latest: $B2_LATEST" >> $OUTPUT
   ```

4. **Email Setup**: Ensure your system is configured to send emails. You might need to install and configure a mail transfer agent like `postfix` or use a tool like `ssmtp` to send emails through an external SMTP server.

By implementing these checks, you'll have a robust system to verify that your Obsidian notes are syncing correctly to your B2 bucket. The script will alert you via email if any discrepancies are found, allowing you to address sync issues promptly[1][2][5].

 




## Extracted Prompts
[[Prompts/Inspecting B2 bucket to verify Obsidian is storing correctly.md#Prompt 1|Prompt 1]]
