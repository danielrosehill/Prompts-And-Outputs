---
title: "How can I find out what kind of RAID if any is running on my Proxmox"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here's what zpool provided:

```
Here's what the zpool provided: zpool status pool: rpool state: ONLINE scan: scrub repaired 0B in 00:03:07 with 0 errors on Sun Sep 8 00:27:08 2024 config: NAME STATE READ WRITE CKSUM rpool ONLINE 0 0 0 raidz1-0 ONLINE 0 0 0 ata-KINGSTON_SA400S37480G_50026B738285A27D-part3 ONLINE 0 0 0 ata-KINGSTON_SA400S37480G_50026B77831DCB8C-part3 ONLINE 0 0 0 ata-KINGSTON_SA400S37480G_50026B7782A92006-part3 ONLINE 0 0 0 ata-KINGSTON_SA400S37480G_50026B738283B120-part3 ONLINE 0 0 0 errors: No known data errors
```

# Output

Based on the output from `zpool status`, you have a **ZFS RAIDZ1** configuration, which is similar to RAID 5. Here’s a breakdown of the information:

- **Pool name**: `rpool`
- **RAID configuration**: RAIDZ1
  - **RAIDZ1** provides single-disk parity, meaning you can lose one drive without losing data. It balances redundancy and storage efficiency.
  
- **Disks**: You have **four** SSDs (Kingston SA400S37480G drives), each contributing to the RAIDZ1 configuration.
  - These disks are listed under the pool as `/dev/ata-KINGSTON_SA400S37480G` with different serial numbers (part3 indicates the partition).
  
- **State**: The pool is **ONLINE** with no known errors.
  
- **Scrub status**: A **scrub** (ZFS's data integrity check) was performed, and no errors were found. The last scrub completed on **Sun, Sep 8, 2024**, and took **3 minutes and 7 seconds** to complete.

#### Summary:
Your Proxmox host is using a **ZFS RAIDZ1** setup with four Kingston SSDs. This configuration offers **single-disk fault tolerance**—you can lose one drive, and the array will still function without data loss. 

Let me know if you need more detailed guidance on ZFS or RAID management!