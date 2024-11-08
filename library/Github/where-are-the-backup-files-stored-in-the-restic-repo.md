---
title: "Where are the backup files stored in the Restic repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Restic stores backups in a deduplicated format within its repository, and the files are not directly visible as traditional files and folders. Instead, the data is stored in a way that optimizes storage by deduplicating repeated content across backups. However, you can still navigate the backup data using Restic commands to explore and restore files as needed.

### Step 1: List Snapshots
To see a list of all available snapshots (backups) in your Restic repository, use:
```bash
restic snapshots -r /path/to/repo
```
Or if you're connecting over SSH:
```bash
restic snapshots -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop
```

### Step 2: Browse the Contents of a Snapshot
To see the contents of a specific snapshot (like a directory listing), you can use the `restic ls` command. 

**Example**:
```bash
restic ls <snapshot-id> -r /path/to/repo
```
Or for an SSH repository:
```bash
restic ls <snapshot-id> -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop
```

- **`<snapshot-id>`**: You can use the snapshot ID or part of it, as listed by the `restic snapshots` command.

### Step 3: Explore the Backup Repository Internals (Advanced)
If you want to see the internal structure of the Restic repository (though it won’t be in a traditional file format), you can manually navigate the repository directory. Here are some key folders:

1. **`data/`**: Contains the actual deduplicated data blocks.
2. **`index/`**: Contains metadata about where the data blocks are stored.
3. **`snapshots/`**: Contains information about each snapshot.
4. **`locks/`**: Contains lock files to prevent multiple backups from running simultaneously.

**Navigate the Repository**:
```bash
cd /srv/backups/daniel-desktop
ls -l
```
But keep in mind, these files are not in a directly readable format.

### Step 4: Restore Specific Files or Directories
To extract specific files from a backup snapshot:
```bash
restic restore <snapshot-id> -r sftp:daniel@192.168.1.1:/srv/backups/daniel-desktop --target /restore/location --include /path/to/file
```

**Explanation**:
- **`<snapshot-id>`**: The ID or part of the ID of the snapshot you want to restore from.
- **`--target`**: Where you want the restored files to be placed.
- **`--include`**: Specify the files or directories you want to extract.

### Summary:
- Use **`restic snapshots`** to list available backups.
- Use **`restic ls <snapshot-id>`** to view the contents of a specific snapshot.
- Restic stores data in a deduplicated format, so directly browsing the repository folders won't show traditional files.
- Use **`restic restore`** to recover specific files or the entire snapshot.

Restic’s internal storage format is designed for efficiency, so viewing the actual backup files directly isn't straightforward. However, the commands provided should help you explore and restore the data you need.