---
title: "Fedora workstation backup tools"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I would like to enhance the protection of my Fedora Workstation 40 desktop.

I'd like to find a way to backup the system configuration and back that up to the cloud.

A managed service would be ideal, although I could also provision my own B2 storage.

I'd like this backup tool to back up my list of installed programmes covering rpm packages, app images, and flatpaks. I would also like to backup any important configuration files for these programs. 

I would like to create a backup that would be good enough to use to restore the system in case a disk failed and I needed to provision a new system with new hardware.

Do any suitable tools come to mind?

# Output

Based on your requirements for backing up your Fedora Workstation 40 desktop, here are some suitable tools and approaches to consider:

## Borg Backup

Borg Backup is a powerful and flexible backup solution that would work well for your needs:

- It supports deduplication and compression to efficiently store backups[1].
- You can easily backup system configuration files and package lists.
- It allows backing up to remote storage, including cloud services.
- Borg can be automated with scripts and scheduled jobs.

To backup installed packages:

```bash
rpm -qa > installed_packages.txt
flatpak list --app --columns=application > installed_flatpaks.txt
```

Then include these files and important config directories like /etc in your Borg backup.

## Restic 

Restic is another excellent option:

- Supports backing up to many cloud storage providers directly[4].
- Offers encryption, deduplication, and compression.
- Can easily backup system files and package lists.
- Allows for scheduled backups and retention policies.

## Déjà Dup

For a more user-friendly GUI option:

- Integrates well with GNOME desktop environments[3].
- Supports cloud backups to services like Google Drive.
- Offers encryption and scheduled backups.
- Can backup system files and user data.

## Implementation Recommendations

1. Use Borg or Restic to backup:
   - /etc directory
   - Package lists (rpm, flatpak, AppImage)
   - Any other important config locations

2. Store backups on a cloud service like Backblaze B2 for off-site protection[4].

3. Set up automated daily or weekly backups using cron jobs or systemd timers.

4. For full system recovery, consider also using tools like:
   - `rpm-ostree` for system snapshots (if using Silverblue)[1]
   - Clonezilla for full disk images

5. Test your backup and restore process regularly to ensure it meets your recovery needs.

By combining these tools and approaches, you can create a robust backup solution that protects your system configuration, installed programs, and allows for efficient restoration in case of hardware failure.
 