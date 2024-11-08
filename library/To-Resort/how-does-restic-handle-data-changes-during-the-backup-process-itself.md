---
title: "How does Restic handle data changes during the backup process itself"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Restic is designed to handle the situation where files are being read, written, or deleted during the backup process, but there are some important considerations about **consistency** and **snapshot integrity**. Here’s how Restic deals with changes on a live filesystem while backing it up:

### How Restic Handles a Live Filesystem

1. **Snapshot Consistency**:
   - Restic performs backups by creating a **snapshot** of the filesystem at the point in time when it scans it. Since it takes some time to scan and backup all the files, if any changes (like modifications or deletions) happen after Restic has already scanned certain files, the backup **snapshot might not fully reflect** the latest state of those files.
   - Restic does not lock the filesystem, meaning it does not "freeze" files in place. This means that **files might change while Restic is backing up**, and these changes may or may not be included in the backup, depending on when Restic reaches those files.

2. **File-Level Backup Granularity**:
   - Restic operates at the file level, so as it processes each file:
     - If a **file is modified before Restic processes it**, the updated version will be included in the backup.
     - If a **file is deleted after it has been scanned** but before it is backed up, Restic will ignore it (since it no longer exists).
     - If a **file is written to or modified while it is being backed up**, there is a risk that the backed-up version will be inconsistent. In other words, you might end up with a partially updated file or inconsistent data if the content changes during the backup.

3. **Handling Open Files**:
   - **Open Files**: Restic can still back up open files (e.g., databases or logs), but it does not have built-in application-level quiescing mechanisms (i.e., it does not "pause" databases or other open file operations to achieve a consistent state). For databases, it is generally advisable to use specialized tools to create consistent snapshots that can be backed up.

4. **Incremental Backups Mitigate Inconsistency**:
   - During incremental backups, Restic will only back up files that have changed since the last snapshot. This behavior reduces the chance of data inconsistency in follow-up backups, as modified files are re-evaluated each time a new backup runs.

### Ways to Improve Backup Consistency on a Live Filesystem

1. **Use Filesystem Snapshots (Recommended for Consistency)**:
   - For the most reliable and consistent backups of a live system, consider using filesystem snapshots:
     - **Btrfs**: Since your system is using Btrfs, you can use its native snapshot feature to take a point-in-time snapshot of your filesystem. You can then instruct Restic to back up the snapshot, which remains unchanged during the backup process, ensuring consistency.
     - Example for Btrfs:
       ```bash
       sudo btrfs subvolume snapshot / /mnt/snapshot
       restic backup /mnt/snapshot
       sudo btrfs subvolume delete /mnt/snapshot
       ```
     - This approach ensures Restic is always working on a consistent, static version of your data, even if the live filesystem is changing.

2. **Pause Applications**:
   - If possible, pause applications that are constantly writing to disk (e.g., databases) during the backup to minimize the risk of inconsistencies. For example, using MySQL, you might dump the database to a file first (`mysqldump`) and then let Restic back up that file.

3. **Use LVM Snapshots (If Applicable)**:
   - If your system is using **LVM** (Logical Volume Manager), you can create an LVM snapshot before the backup. This snapshot can then be mounted and backed up by Restic. This method is especially useful if your setup includes databases or frequently changing system files.

4. **Quiescing Tools for Databases**:
   - For databases, consider using quiescing or export tools to create a consistent point-in-time copy of the data. This dump file can then be backed up with Restic.

### Summary
- **Live Filesystem Changes**: Restic does not lock files, so if a file changes during the backup, the resulting backup may be inconsistent with respect to those specific files.
- **File-Level Approach**: Restic works at a file level, and changes made to files during the backup process may or may not be fully reflected.
- **Snapshots for Consistency**: The best practice for ensuring backup consistency is to use filesystem snapshots (Btrfs, LVM) to create a stable snapshot of the filesystem that Restic can back up. This guarantees a point-in-time consistent backup.

Restic is resilient to changes but, like most file-level backup tools, cannot guarantee consistency across actively changing files without the use of such snapshots or other quiescing techniques. Using a stable, snapshot-based approach is highly recommended for accurate and consistent full-system backups.