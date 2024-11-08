---
title: "Planning Fedora workstation storage system migration"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. I would like you to now suggest a way that I could change my storage system. I don't think that my current system provides sufficient protection against disk failure and other potential things that might "go wrong." Is it possible to alter the setup of the disk storage array on the system? If so, how? And what type of configuration might it be possible to move over to? If it would make more sense to add an additional drive for this purpose, please advise which capacity and type to buy.

# Output

Based on your current BTRFS configuration and the desire for better protection against disk failures, I can suggest a few options to improve your storage system:

1. Convert to RAID1 for data:

Your current setup uses a "single" profile for data, which doesn't provide redundancy. You can convert this to RAID1 for better protection:

```bash
sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /
```

This command will convert both data and metadata to RAID1, providing mirroring across your devices. However, this will reduce your usable space by half.

2. Add more drives:

Given that you have three devices (1 NVMe and 2 SSDs), adding one or two more drives would allow for a more robust RAID configuration. If you add two more drives of similar size (around 1TB), you could set up a RAID10 configuration:

```bash
sudo btrfs balance start -dconvert=raid10 -mconvert=raid1c3 /
```

This would provide better performance and redundancy. For this, I'd recommend purchasing two more SSDs of similar capacity to your existing ones (around 1TB each).

3. Implement RAID1C3 for metadata:

Even without adding new drives, you can increase metadata redundancy:

```bash
sudo btrfs balance start -mconvert=raid1c3 /
```

This ensures your metadata is stored on all three devices, providing better protection against drive failures.

4. Regular scrubbing:

Implement regular scrubbing to detect and correct errors:

```bash
sudo btrfs scrub start /
```

Set this up as a monthly cron job for proactive maintenance.

5. Backup strategy:

Regardless of RAID configuration, implement a robust backup strategy. Use external drives or a network-attached storage device for regular backups.

Recommendation:
Given your current setup, I'd recommend adding two more SSDs (1TB each) to your system. This would allow you to implement a RAID10 configuration for data and RAID1C3 for metadata, providing a good balance of performance, capacity, and redundancy.

After adding the drives:

1. Add them to your BTRFS array:
   ```bash
   sudo btrfs device add /dev/sdX /dev/sdY /
   ```

2. Convert to RAID10 for data and RAID1C3 for metadata:
   ```bash
   sudo btrfs balance start -dconvert=raid10 -mconvert=raid1c3 /
   ```

This setup would provide protection against up to two drive failures (depending on which drives fail) and offer improved read/write performance. Remember, RAID is not a substitute for backups, so maintain a separate backup strategy as well.

 