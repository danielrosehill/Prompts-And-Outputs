---
title: "List of system folders on Fedora BTRFS RAID 1"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here's a breakdown of the directories on your system and whether they can be safely excluded in a backup:

| **Directory**    | **Description**                         | **Safe to Exclude?**                           |
| ---------------- | --------------------------------------- | ---------------------------------------------- |
| `/afs`           | Advanced File System (often unused)     | Yes, if not in use.                            |
| `/boot`          | Boot files, kernels, GRUB config        | No, required for booting.                      |
| `/etc`           | System configuration files              | No, essential for system config.               |
| `/lib`, `/lib64` | System libraries                        | No, core system components.                    |
| `/lost+found`    | Recovered files after crashes           | Yes, generally empty.                          |
| `/mnt`           | Temporary mount points                  | Yes, prevents loops.                           |
| `/proc`          | Virtual filesystem for processes        | Yes, dynamically generated.                    |
| `/run`           | Runtime variable data                   | Yes, created fresh on boot.                    |
| `/snap`          | Snap package mount points               | No, if using Snap packages.                    |
| `/sys`           | Virtual filesystem for system info      | Yes, dynamically generated.                    |
| `/usr`           | User binaries, libraries, and docs      | No, core system programs.                      |
| `/bin`, `/sbin`  | Essential binaries for all users/admins | No, crucial for system functions.              |
| `/home`          | User files and directories              | No, contains user data.                        |
| `/media`         | Mount points for removable media        | Yes, if no active mounts.                      |
| `/opt`           | Optional software packages              | No, may contain installed apps.                |
| `/root`          | Root user's home directory              | No, often has important configs.               |
| `/srv`           | Data for services (e.g., web server)    | No, if hosting services.                       |
| `/tmp`           | Temporary files, cleared on reboot      | Yes, generally safe to exclude.                |
| `/var`           | Variable data (logs, caches, databases) | No, but parts (logs, caches) can be selective. |

### Exclusion Notes:
- Exclude directories like `/proc`, `/run`, `/sys`, and `/tmp` as they contain ephemeral or dynamically generated data not needed in a backup.
- Include critical system directories (`/etc`, `/boot`, `/usr`, `/lib`, `/bin`) for complete OS restoration.