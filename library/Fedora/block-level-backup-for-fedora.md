---
title: "Block level backup for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

are there any block level backup tools that can run on fedora workstations while the system is running? I don't use Clonezilla much for this reason - it's a hassle to use!

# Output

Based on your query and the search results provided, there are a few options for block-level backup tools that can run on Fedora workstations while the system is running:

1. Veeam Agent for Linux:
Veeam offers a free version of their backup agent for Linux, which supports Fedora:

- Supports block-level backups
- Can perform backups while the system is running
- Offers both file-level and volume-level backups
- Free version available with basic features
- Pricing for advanced features varies based on workload and support level

2. BDSync/BDSync-Manager:
While not a commercial solution, BDSync is mentioned in the search results as a tool that can perform block-level backups:

- Supports incremental backups
- Can perform live/hot backups
- Supports mounting, compression, and network backups

3. Acronis Backup:
Although not specifically mentioned for Fedora in the search results, Acronis does support Linux systems:

- Offers block-level backups
- Supports live backups of running systems
- Includes features like encryption and deduplication
- Pricing varies based on the number of workstations and features required

When considering these options, keep in mind:

- Veeam and Acronis are commercial solutions that offer more comprehensive features and support.
- BDSync is an open-source option that might require more setup but could be more flexible.
- All of these solutions should allow you to perform backups without shutting down your Fedora workstation, addressing the inconvenience you mentioned with Clonezilla.

It's important to test any backup solution thoroughly in your specific environment to ensure compatibility and performance. Also, consider factors like ease of use, restore capabilities, and integration with your existing backup strategy when making your decision.
# checking btrfs support

I assume that these tools support Fedora & BTRFS

# Output
Based on the search results and your query, here's what we can conclude about block-level backup tools that support Fedora and BTRFS:

1. Veeam Agent for Linux:
   - Supports Fedora (up to kernel 6.10 for Fedora 38 and 39) [3]
   - Supports BTRFS, but with some limitations:
     - BTRFS is supported only if it resides directly on a physical device with no additional abstraction layers (such as LVM, software RAID, dm-crypt) below or above it [2][3]
   - Can perform backups while the system is running
   - Offers both file-level and volume-level backups
   - Free version available with basic features

2. BDSync/BDSync-Manager:
   - Not mentioned specifically for Fedora or BTRFS in the search results
   - Supports block-level backups and can perform live/hot backups

It's important to note that while these tools support Fedora and BTRFS to some extent, there are limitations and considerations:

- BTRFS support in Veeam Agent for Linux is limited, especially when used with LVM or other abstraction layers [1][2]
- Some users have reported challenges with BTRFS in Fedora, citing complexity and compatibility issues with certain applications [4]

For Fedora-specific backup solutions:

- Fedora uses BTRFS by default, and you can use BTRFS snapshots for system backups [5]
- However, Fedora doesn't provide automatic snapshots out of the box [5]
- You can manually create and manage BTRFS snapshots, which can be used for system rollbacks [5]

Given your requirement for a tool that can run while the system is active, Veeam Agent for Linux seems to be the most suitable commercial option that explicitly supports both Fedora and BTRFS. However, you'll need to be mindful of the limitations regarding BTRFS configuration.

For a more integrated solution, you might want to explore BTRFS snapshot management tools specific to Fedora, which would allow you to create and manage backups using the native filesystem features.

 