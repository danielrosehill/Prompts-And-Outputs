---
title: "System for automatically archiving old Obsidian vault notes"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you suggest a technology I might implement for automatically archiving older notes in my Obsidian markdown repository? Let's assume that all the outputs are nested under /Outputs/Raw relative to the base of the vault. Let's say that the system was intended to automatically archive notes that are older than this month or the last month - so the start of a new calendar month serves as the trigger. For those older notes, they are automatically archived into a timestampped folder. For instance 0724.tar.gz would hold all notes from 07/24 (July). after the archiving process takes place, the archive is moved to a separate folder and the original files are deleted from the fault. Please outline how I might implement this?

# Output

You can implement this automated archiving system for your Obsidian markdown repository using a combination of bash scripting (or any other scripting language you're comfortable with) and a cron job to run the script periodically (monthly in this case). Here's how you might go about it:

### Steps to Implement the Archive System

1. **Define the Archive Structure:**
   - All the markdown files (notes) you want to archive reside under the `/Outputs/Raw` folder in your Obsidian vault.
   - You'll archive notes older than the current or last month.
   - After archiving, move the `.tar.gz` archive to a separate folder (e.g., `/Archives`), and delete the original notes.

2. **Create the Archive Script:**

   Create a bash script that:
   - Identifies all notes older than the last month.
   - Archives them into a timestamped tarball.
   - Moves the archive to a separate folder.
   - Deletes the original files from `/Outputs/Raw`.

### Example Bash Script

```bash
#!/bin/bash

# Set your base directory
VAULT_DIR="/path/to/your/obsidian/vault"
RAW_DIR="$VAULT_DIR/Outputs/Raw"
ARCHIVE_DIR="$VAULT_DIR/Archives"

# Get current month and previous month
current_month=$(date +%m)
current_year=$(date +%Y)
previous_month=$(date --date="1 month ago" +%m)
previous_year=$(date --date="1 month ago" +%Y)

# Format archive filename as MMYY.tar.gz (e.g., 0724.tar.gz for July 2024)
archive_name="${previous_month}${previous_year}.tar.gz"

# Find and archive files older than the first day of the current month
find "$RAW_DIR" -type f -not -newermt "$current_year-$current_month-01" -print0 | tar -cvzf "$ARCHIVE_DIR/$archive_name" --null -T -

# Check if the tarball was created successfully
if [ -f "$ARCHIVE_DIR/$archive_name" ]; then
    # Delete the original files
    find "$RAW_DIR" -type f -not -newermt "$current_year-$current_month-01" -exec rm {} \;
    echo "Archive created and original files deleted."
else
    echo "Archiving failed."
fi
```

### Script Breakdown
- **`find "$RAW_DIR" -type f -not -newermt "$current_year-$current_month-01"`**: This finds all the files in the `/Outputs/Raw` directory that were modified before the first day of the current month.
- **`tar -cvzf "$ARCHIVE_DIR/$archive_name" --null -T -`**: This command creates a `.tar.gz` archive of the identified files.
- **If statement**: Ensures that the original files are only deleted if the archive was created successfully.

3. **Set Up a Cron Job for Automation:**
   You can use a cron job to run this script at the beginning of each month.

   - Open your crontab editor:
     ```bash
     crontab -e
     ```
   - Add the following line to schedule the script to run at midnight on the 1st day of each month:
     ```bash
     0 0 1 * * /path/to/your/archive_script.sh
     ```

This cron job will automatically run the archiving process monthly, create a tarball for notes older than the previous month, move it to the `/Archives` folder, and delete the original files from the `/Outputs/Raw` directory.

Let me know if you need help with any part of this setup!