---
title: "Which directories could be excluded in a BTRFS full system backup"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


When performing a full backup of your Btrfs + RAID1 system, you can generally exclude the following directories without impairing the ability to restore the OS:

### Directories to Exclude:
1. **`/dev`**: Contains device files that are recreated at boot.
2. **`/proc`**: Virtual filesystem for process information; rebuilt on boot.
3. **`/sys`**: Virtual filesystem for system information; not needed in backups.
4. **`/tmp`**: Temporary files that are not necessary to restore.
5. **`/run`**: Runtime data; created fresh on boot.
6. **`/mnt`** and **`/media`**: Mount points for external devices.

### Reasoning:
These directories contain temporary or dynamically generated data. Excluding them ensures your backups remain efficient without affecting the restore process.