---
title: "Creating a full system backup of Fedora without BTRFS"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm looking for a way to incrementally backup my Fedora computer onto an external SSD. I've set up a mount point for the SSD at /mnt/desktop-backups
As Fedora already has excellent snapshotting abilities with BTRFS, this backup will serve a different purpose: it would be intended to help with system recovery if the computer were broken beyond repair and I had to install a new Fedora sytem from scratch.
While I want to backup the computer as thoroughly as possible, I obviously don't want to backup /mnt (to prevent recursive backups) or a few other folders.
I'd like to run this backup regularly so while using rsync is possible, I'd prefer something with a GUI that's a little easier to run repeatedly. 
Can you suggest some tools that would be suitable?

# Output

Yes, **Bacula** can create backups onto mounted SSDs or any other storage device that your system can access. Bacula is highly flexible and can be configured to back up to various storage media, including local drives, external SSDs, NAS devices, and even cloud storage.

### How to Configure Bacula for Backups to a Mounted SSD:
1. **Mount the SSD**: Ensure your external SSD is mounted at `/mnt/desktop-backups` (or your desired mount point). Confirm that it is correctly mounted and accessible by checking:
   ```bash
   df -h /mnt/desktop-backups
   ```

2. **Set Up Bacula**:
   - During Bacula’s setup, you will define a **Storage** resource in the configuration file (`bacula-sd.conf`). You can specify the backup destination as your mounted SSD.
   - Edit `bacula-sd.conf`:
     ```bash
     Storage {
       Name = Local-SSD
       Device = /mnt/desktop-backups
       Media Type = File
     }
     ```
   - Configure **FileSet** to specify what should be backed up, allowing you to exclude `/mnt` and any other directories:
     ```bash
     FileSet {
       Name = "Full System Backup"
       Include {
         Options {
           Exclude = yes
           WildFile = "/mnt/*"
           WildFile = "/proc/*"
           WildFile = "/sys/*"
           WildFile = "/dev/*"
           WildFile = "/tmp/*"
           WildFile = "/run/*"
         }
         File = /
       }
     }
     ```
3. **Scheduling**: Bacula allows you to define **Job** schedules to run backups at regular intervals (e.g., daily, weekly). You can automate this to ensure backups are created regularly.

4. **Performing Restores**: In case you need to restore your system on new hardware, Bacula can recreate the filesystem on the new machine, making it suitable for complete system restoration.

### Benefits:
- **Flexibility**: Bacula’s configurability means you can customize what gets backed up and where it’s stored.
- **Scheduling**: Automate regular backups to your mounted SSD, ensuring your data stays up-to-date.
- **Recovery**: Supports full system restores, making it easier to set up new hardware with your backed-up configuration.

While Bacula does require some initial configuration, it’s quite powerful and versatile for comprehensive system backups. If you need a GUI to manage Bacula, you can use **Bacula-Web** or **Bat (Bacula Administration Tool)**.