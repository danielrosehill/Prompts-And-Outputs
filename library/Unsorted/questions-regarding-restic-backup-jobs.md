---
title: "Questions regarding Restic backup jobs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here are the answers to your questions regarding Restic backup jobs:

### 1. Interrupting and Resuming Backup Jobs
Yes, if you interrupt a running Restic backup job (for example, by pressing Ctrl+C), Restic can be safely resumed later. When you run the backup command again, Restic will:

- **Resume Where It Left Off**: Restic keeps track of the files that have already been backed up. When you start a new backup after an interruption, it will only back up the files that have changed since the last backup or those that were not completed due to the interruption.
- **Efficiency**: This means you won't lose progress, and the backup will be more efficient as it will avoid reprocessing files that have already been backed up.

### 2. Incremental Backups on Future Runs
Yes, on subsequent runs of the backup job, Restic performs **incremental backups** by default. Here's how it works:

- **Only New or Changed Data**: Restic will only back up new files and changes to existing files since the last backup. This is what makes Restic efficient, as it avoids duplicating data already stored in the repository.
- **Faster Execution**: Because of this incremental approach, future backups will typically be much faster than the initial full backup. The time taken will depend on the amount of new or modified data since the last backup.

### Summary
- You can safely interrupt a Restic backup and resume it later without losing progress.
- Future backup jobs will be incremental, meaning they will only back up new or changed files, making them faster than the initial backup. 

This efficient backup and recovery approach is one of the key strengths of using Restic for your backup needs.