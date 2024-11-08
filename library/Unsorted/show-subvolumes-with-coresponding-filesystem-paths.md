---
title: "Show subvolumes with coresponding filesystem paths"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You asked if it's possible to list the existing Btrfs subvolumes on your machine and see which filesystem paths they correspond to.

Yes, you can list all existing Btrfs subvolumes along with their paths using the following command:

### Command to List Subvolumes and Paths
```bash
sudo btrfs subvolume list /
```

### Output Explanation:
The output of this command will display details including:
- **ID:** The unique identifier for each subvolume.
- **Gen:** The generation (a version-like number that changes with updates).
- **Top level:** The parent subvolume or volume.
- **Path:** The relative path of the subvolume from the root of the Btrfs filesystem.

### Example Output Interpretation
Here’s how to interpret the output:
```
ID 256 gen 202170 top level 5 path home
ID 260 gen 202170 top level 5 path root
ID 262 gen 201521 top level 260 path var/lib/machines
```
- **`ID 256, path home`**: This indicates that there is a subvolume located at `/home`.
- **`ID 260, path root`**: This could mean the main root filesystem.
- **`ID 262, path var/lib/machines`**: A subvolume specifically for `/var/lib/machines`.

### Determining Full Filesystem Paths
The paths provided in the list are relative to the Btrfs filesystem’s mount point. If you want to confirm the exact paths, simply check where your root (`/`) or other Btrfs volumes are mounted. If your system’s root filesystem is mounted at `/`, then the paths in the list can be read as full filesystem paths directly.

This command will help you identify existing subvolumes and understand how they map to your directories, allowing you to plan further adjustments or backups accordingly.