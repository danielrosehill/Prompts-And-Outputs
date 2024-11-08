---
title: "Calculate the overhead on various RAID configurations"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here is some information about the BTRFS on my Fedora desktop
	
If I'm not mistaken, I'm not running any type of RAID.

Is it possible to change this?

What would the overhead be?

       Total devices 3 FS bytes used 225.37GiB  
       devid    1 size 931.51GiB used 80.04GiB path /dev/nvme0n1p1  
       devid    2 size 929.93GiB used 80.00GiB path /dev/sda3  
       devid    3 size 931.51GiB used 81.03GiB path /dev/sdb1
```


Data, single: total=227.01GiB, used=219.33GiB  
System, RAID1: total=32.00MiB, used=48.00KiB  
Metadata, RAID1: total=7.00GiB, used=6.04GiB  
GlobalReserve, single: total=512.00MiB, used=0.00B
```

# Output
Based on the information you provided, you are correct that you are not currently running any type of RAID for your data. Your Btrfs filesystem is using a single profile for data storage, while using RAID1 for system and metadata. Here's a breakdown of your current setup and options for changing it:

## Current Configuration

Your Btrfs filesystem is spread across three devices:
1. /dev/nvme0n1p1 (931.51GiB)
2. /dev/sda3 (929.93GiB)
3. /dev/sdb1 (931.51GiB)

The data is currently stored using a single profile, which means it's distributed across the devices without redundancy[8].

## Changing to RAID

Yes, it is possible to change your current configuration to use RAID. Btrfs allows you to convert between different RAID profiles without reformatting[1].

## RAID Options and Overhead

Here are some RAID options you could consider:

1. **RAID0 (Striping)**
   - Improves read/write performance
   - No redundancy
   - Usable space: 100% of total capacity
   - No overhead in terms of storage space

2. **RAID1 (Mirroring)**
   - Provides full redundancy
   - Usable space: 50% of total capacity
   - 100% overhead in terms of storage space

3. **RAID10 (Striping + Mirroring)**
   - Balances performance and redundancy
   - Usable space: 50% of total capacity
   - 100% overhead in terms of storage space

4. **RAID5/6**
   - While available, these are not recommended for Btrfs due to known issues[8]

## Performance Considerations

The performance impact of changing to a RAID configuration depends on the RAID level chosen:

- RAID0 would likely improve both read and write performance[3].
- RAID1 might improve read performance but could slightly decrease write performance[3].
- RAID10 would offer a balance of improved read performance and redundancy[3].

## How to Change

To convert your current single profile to a RAID configuration, you would use the `btrfs balance` command. For example, to convert to RAID1:

```bash
sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /mount/point
```

Replace `/mount/point` with the actual mount point of your Btrfs filesystem[1].

## Recommendation

Given that you mentioned this is a desktop used for gaming/entertainment, and data protection is a low priority, you might consider RAID0 for improved performance[7]. However, be aware that RAID0 offers no data redundancy, so regular backups are crucial.

If you want a balance of performance and some data protection, RAID10 could be a good option, but it would reduce your usable space by half.

Remember to backup your data before making any changes to your filesystem configuration. Also, consider the specific needs of your system and workload when choosing a RAID level.

 
 