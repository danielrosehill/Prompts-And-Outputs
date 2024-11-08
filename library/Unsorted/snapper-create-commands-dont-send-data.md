---
title: "Snapper create commands don't send data"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


No, the initial command:

```bash
sudo snapper -c root create --description "Initial Full Backup"
```

creates a snapshot on your local system and does not send any data to the target external SSD. This snapshot is stored within your root filesystem's `.snapshots` directory. It serves as a reference point for your backup.

The data only gets transferred to the external SSD when you use the `btrfs send` and `receive` commands to move the snapshot data from your local filesystem to `/mnt/desktop-backups`.