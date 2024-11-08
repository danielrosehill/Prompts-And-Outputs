---
title: "OpenSUSE - exclusion paths for full-system backups"
---

![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)

Based on the search results and standard Linux system architecture, here's a comprehensive guide for directories that can be safely excluded from OpenSUSE system backups:

## Virtual and Temporary Filesystems

**System Virtual Directories**

- /proc (virtual filesystem for system processes)\[2]
- /sys (kernel and hardware information)\[2]
- /dev (device files)\[2]

**Temporary Directories**

- /tmp (temporary files)\[2]
- /run (runtime data)\[2]
- /var/run (runtime data)\[2]
- /var/lock (lock files)\[2]
- /var/tmp (temporary files)\[2]

## Mount Points

- /media (mounted devices)\[2]
- /mnt (mounted devices)\[2]
- /cdrom (mounted media)\[2]

## Cache Directories

- /var/cache (system caches)\[2]
- /home/\*/.cache (user caches)\[2]
- /var/cache/dnf (package manager cache)\[7]

## User-Specific Temporary Files

- /home/\*/.local/share/Trash (user trash)\[2]
- /home/\*/.gvfs (virtual filesystem)\[2]
- /home/\*/.dbus (IPC data)\[2]
- /home/\*/.xsession-errors (X session logs)\[2]

## System Files

- /lost+found (filesystem recovery)\[2]
- /swapfile (swap space)\[2]

## Best Practices

For a reliable backup strategy on OpenSUSE, focus on backing up\[5]\[6]:

- /home (user data and configurations)
- /etc (system configurations)
- List of installed packages

The rest of the system can be restored through a fresh installation if needed, making the backup process more efficient and manageable\[5].

Citations:\
&#x20;
