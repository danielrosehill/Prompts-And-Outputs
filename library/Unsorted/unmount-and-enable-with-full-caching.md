---
title: "Unmount and enable with full caching"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

How can I unmounted the drive & remount it with the full cache mode enabled?

# Output

To unmount the Google Shared Drive that you previously mounted with **rclone** and then remount it with **full cache mode** enabled, follow these steps:

### Step 1: Unmount the Drive
You can unmount the drive using the `fusermount` command. Run the following command in the terminal:

```bash
fusermount -u /home/daniel/Cloud_Drives/Google/Shared-Drives/DSR-Holdings-Accounts
```

### Step 2: Remount the Drive with Full Cache Mode
Once the drive is unmounted, you can remount it with the full cache mode by running the following command:

```bash
rclone mount yourbusinessaccounts: /home/daniel/Cloud_Drives/Google/Shared-Drives/DSR-Holdings-Accounts --vfs-cache-mode full
```

### Additional Tips:
- Make sure to wait a moment after unmounting before remounting to ensure the system is ready for the new mount.
- You can also add any other desired options to the mount command based on your preferences (e.g., `--allow-other` if you want other users to access the mount).

### Full Command Sequence:
Here's the complete sequence you would run in your terminal:

```bash
# Unmount the existing mount
fusermount -u /home/daniel/Cloud_Drives/Google/Shared-Drives/DSR-Holdings-Accounts

# Remount with full cache mode
rclone mount yourbusinessaccounts: /home/daniel/Cloud_Drives/Google/Shared-Drives/DSR-Holdings-Accounts --vfs-cache-mode full
```

This will unmount the drive and then remount it with the desired caching mode. Let me know if you need further assistance!