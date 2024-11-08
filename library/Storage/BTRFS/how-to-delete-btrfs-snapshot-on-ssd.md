---
title: "How to delete BTRFS snapshot on SSD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To delete a **Btrfs snapshot** stored on an SSD, use the following command:

1. **Identify the Snapshot Path**:
   Locate the exact path of the snapshot you want to delete. It should be something like `/mnt/your_btrfs/subvolume_name/snapshot_name`.

2. **Delete the Snapshot**:
   Run:
   ```bash
   sudo btrfs subvolume delete /mnt/your_btrfs/subvolume_name/snapshot_name
   ```
   Replace with the actual path to your snapshot.

3. **Verify Deletion**:
   List subvolumes to ensure it’s deleted:
   ```bash
   sudo btrfs subvolume list /mnt/your_btrfs
   ```

These steps should remove the snapshot from your SSD.