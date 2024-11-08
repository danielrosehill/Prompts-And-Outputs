---
title: "How to show current RAID status on BTRFS"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

could you give me the commands i need on fedora linux to check whether i'm running raid on my btrfs  system and if so show my current raid config and status

# Output

To check if you're running RAID on your Btrfs system and display your current RAID configuration and status on Fedora Linux, you can use the following commands:

1. **Check Btrfs filesystem details, including RAID configuration:**

   ```
   sudo btrfs filesystem df /mount/point
   ```

   Replace `/mount/point` with the actual mount point of your Btrfs filesystem (e.g., `/`, `/home`, etc.).

2. **Show detailed Btrfs device information, including RAID levels:**

   ```
   sudo btrfs filesystem show /mount/point
   ```

3. **Check the status and RAID level of the Btrfs system:**

   ```
   sudo btrfs device stats /mount/point
   ```

4. **List all devices in the Btrfs filesystem with their RAID status:**

   ```
   sudo btrfs filesystem usage /mount/point
   ```

5. **Check if the RAID is healthy and its status:**

   ```
   sudo btrfs device usage /mount/point
   ```

These commands will provide an overview of your Btrfs RAID configuration and its status, including the data and metadata RAID levels.

