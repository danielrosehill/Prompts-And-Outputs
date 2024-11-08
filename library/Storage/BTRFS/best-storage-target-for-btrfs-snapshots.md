---
title: "Best storage target for BTRFS snapshots"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm very glad that I asked now. 

I have a few options for storing these backups:

1) A Fedora server on the LAN

2) An NAS on the LAN

3) An external SSD

Please recommend which device it would be most efficient to store these BTRFS snapshots onto

# Output

Based on your options and the information provided about BTRFS snapshots, here's a recommendation for storing your backups:

1. Fedora server on the LAN:
This is likely the best option for storing your BTRFS snapshots. Here's why:

   - BTRFS-aware: A Fedora server can be configured with BTRFS, allowing you to take full advantage of BTRFS features like send/receive for efficient snapshot transfers.
   - Speed: LAN transfers are typically faster than writing to external drives, especially for incremental backups.
   - Automation: You can easily set up automated backup scripts on both your main system and the Fedora server.
   - Flexibility: You can configure the server for redundancy (like RAID) for extra data protection.

2. NAS on the LAN:
This is a good second choice, especially if it supports BTRFS:

   - If BTRFS-aware, it can efficiently store and manage snapshots.
   - Offers good speed over LAN.
   - Often comes with built-in backup software and redundancy options.
   - However, not all NAS devices fully support BTRFS features, which might limit efficiency.

3. External SSD:
While portable and fast, this is the least recommended for primary backup storage of BTRFS snapshots:

   - Limited BTRFS support: External drives often use simpler filesystems, potentially losing BTRFS-specific benefits.
   - Manual process: Requires physically connecting the drive, which can be inconvenient for regular backups.
   - Single point of failure: Unless you rotate multiple drives, you lack redundancy.
   - Capacity limitations: SSDs typically have less capacity than network storage solutions.

Recommendation:
Use the Fedora server on the LAN as your primary backup destination. Set it up with BTRFS and use BTRFS send/receive for efficient, incremental backups. This setup allows you to leverage BTRFS features fully, automate the process, and potentially set up a RAID configuration for added data protection.

Use the NAS as a secondary backup location if possible, especially if it supports BTRFS. This provides an additional layer of protection.

Keep the external SSD as an offline backup option. Periodically (e.g., monthly) create a full backup to this drive and store it in a separate location for disaster recovery purposes.

This approach gives you a robust, efficient, and multi-layered backup strategy that takes full advantage of BTRFS capabilities while also providing offline protection.

Citations:
 