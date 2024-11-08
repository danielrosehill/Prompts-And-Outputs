---
title: "Manual methods of B2 sync"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
At the moment, I'm using an Obsidian plugin called Remote Sync to sync my notepad with a b2 bucket. I primarily use my vault at my desktop (Fedora) but i sometimes use it on my phone too. As these are multiple devices, it's important that the sync has some automatic method of resolving any potential conflicts. Can you think of a way that would allow me to replace this plugin? On the desktop I could use rclone, perhaps. But I'm not sure if there's a comparable sync client for Android.

# Output

Based on your current setup and requirements, here's a potential solution to replace the Remote Sync plugin while maintaining sync functionality across your desktop and mobile devices:

## Desktop Solution (Fedora)

For your Fedora desktop, rclone is indeed an excellent choice for syncing with Backblaze B2. Here's how you can set it up:

1. Install rclone on your Fedora system:
   ```
   sudo dnf install rclone
   ```

2. Configure rclone for your B2 bucket:
   ```
   rclone config
   ```
   Follow the prompts to set up a new remote for your B2 bucket.

3. Set up a bidirectional sync using rclone's bisync command[2]:
   ```
   rclone bisync /path/to/your/obsidian/vault b2:your-bucket-name/obsidian --create-empty-src-dirs --compare size,modtime,checksum
   ```

4. Automate this sync process using a cron job or systemd timer to run periodically.

## Android Solution

For Android, there isn't a direct rclone equivalent, but you have a few options:

1. Backblaze B2 Android App[3]:
   - Backblaze offers an official Android app that allows you to access files stored in B2.
   - While it doesn't provide automatic syncing, you can manually download and upload files as needed.

2. FolderSync:
   - This is a third-party app available on the Google Play Store that supports Backblaze B2.
   - It offers automated, bidirectional syncing between your Android device and B2.

3. Obsidian Mobile with a different sync solution:
   - Consider using Obsidian's built-in sync feature (requires a subscription) or a different cloud provider that has better Android support (like Dropbox or Google Drive).

## Conflict Resolution

To handle potential conflicts:

1. Use rclone's bisync command on your desktop, which has built-in conflict resolution mechanisms[2].

2. On Android, if using FolderSync, it also has conflict resolution options.

3. Implement a version control system within your Obsidian vault using plugins like "Version History Diff" or "Git".

4. Use rclone's `--backup-dir` option to keep backups of changed or deleted files[2].

## Additional Considerations

1. Frequency of Syncs: Set up your desktop sync to run frequently enough to minimize the chance of conflicts.

2. Version Control: Consider using a Git-based solution alongside B2 for better version control and conflict resolution.

3. Monitoring: Set up a script to check sync status and notify you of any issues, as discussed in your previous query.

4. Manual Conflict Resolution: In cases where automatic resolution fails, have a process in place for manual conflict resolution.

While this solution may not be as seamless as the Remote Sync plugin, it offers more control and flexibility. The desktop side with rclone can be highly automated, while the Android side may require a bit more manual intervention unless you opt for a third-party sync app like FolderSync.

Remember to thoroughly test this setup with non-critical data before fully implementing it with your Obsidian vault to ensure it meets your needs and handles conflicts appropriately.

 




## Extracted Prompts
[[Prompts/Manual methods of B2 sync.md#Prompt 1|Prompt 1]]
