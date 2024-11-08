---
title: "Exploring RAID options on my desktop"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Hmm. Even 50% is a big overhead. Is there any form of RAID that would get me some redundancy but cause a less dramatic overhead? How would you assess the riskiness of my current setup?

# Output

Based on your current setup and the desire for redundancy with less overhead, here are some options to consider:

## RAID5-like Option

Btrfs offers a RAID5-like profile that could potentially meet your needs:

**RAID5 (experimental)**
- Provides single disk redundancy
- Usable space: Approximately 66-75% of total capacity (depending on number of disks)
- Lower overhead compared to RAID1
- Warning: Btrfs RAID5 is still considered experimental and not recommended for critical data[4]

## Current Setup Assessment

Your current setup appears to be using a single profile for data storage across three devices:

1. /dev/nvme0n1p1 (931.51GiB)
2. /dev/sda3 (929.93GiB)
3. /dev/sdb1 (931.51GiB)

This configuration offers no redundancy for your data, which presents some risk:

- If any single drive fails, you could lose data stored on that drive
- No protection against bit rot or silent data corruption

## Recommendations

1. **RAID1 with 3 devices**
   - Provides better redundancy than your current setup
   - Usable space: 50% of total capacity
   - Can survive failure of any one drive

2. **RAID10**
   - Balances performance and redundancy
   - Usable space: 50% of total capacity
   - Better performance than RAID1, especially for writes

3. **Consider ZFS**
   - If willing to switch filesystems, ZFS offers robust RAID-Z options
   - RAID-Z1 would provide single disk redundancy with less overhead than Btrfs RAID1[5]

## Risk Mitigation

To reduce risk without changing your RAID setup:

1. Implement a robust backup strategy
2. Use Btrfs's scrub feature regularly to detect and correct errors
3. Monitor drive health with tools like S.M.A.R.T.

Remember, while RAID provides redundancy, it's not a substitute for backups. Regardless of the RAID level you choose, maintaining separate backups is crucial for data protection[1][4].

 