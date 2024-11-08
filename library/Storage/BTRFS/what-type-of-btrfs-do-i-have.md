---
title: "What type of BTRFS do I have"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm using BTRFS on a Fedora Workstation 40 desktop. I have a system set up with an NVME + 2 x SSD drives. I can't remember exactly what type of BTRFS I configured. Is there a way to get this output from the terminal?

# Output

Certainly! You can use several commands to get information about your BTRFS setup on your Fedora Workstation 40 desktop. Here's how you can retrieve the details:

## Filesystem Information

To get an overview of your BTRFS filesystem:

bash

`sudo btrfs filesystem show`

This command will display information about all BTRFS filesystems on your system, including the NVME and SSDs you mentioned[

# Input

Thanks.

Here what I got back:

Label: 'fedora'  uuid: c81772c3-3741-4f50-8498-ce2023eb7123  
       Total devices 3 FS bytes used 226.66GiB  
       devid    1 size 931.51GiB used 81.04GiB path /dev/nvme0n1p1  
       devid    2 size 929.93GiB used 79.00GiB path /dev/sda3  
       devid    3 size 931.51GiB used 81.03GiB path /dev/sdb1

Based on the output you've provided, I can give you a detailed explanation of your BTRFS setup:

## BTRFS Configuration

Your BTRFS filesystem is labeled "fedora" and has a unique identifier (UUID) of c81772c3-3741-4f50-8498-ce2023eb7123.

## Storage Devices

Your setup consists of three devices:

1. **NVME Drive**: `/dev/nvme0n1p1`
   - Size: 931.51GiB
   - Used: 81.04GiB

2. **First SSD**: `/dev/sda3`
   - Size: 929.93GiB
   - Used: 79.00GiB

3. **Second SSD**: `/dev/sdb1`
   - Size: 931.51GiB
   - Used: 81.03GiB

## Usage Statistics

- **Total Space Used**: The filesystem is currently using 226.66GiB of space across all devices.

## BTRFS Configuration Type

Based on this output, your BTRFS setup appears to be using a **multi-device configuration**. However, the specific RAID level or data distribution method isn't explicitly stated in this output.

Given that:
1. You have three devices of similar size
2. The used space is roughly equal across all devices

It's likely that you're using either:

- **RAID0** (striping) for improved performance
- **RAID1** (mirroring) for data redundancy
- A combination of both, which BTRFS calls "RAID10"

To confirm the exact RAID level or data/metadata profile, you would need to run additional commands such as:

```bash
sudo btrfs filesystem df /
```

This command would show you the data and metadata profiles being used, which would definitively answer what type of BTRFS configuration you have.

Remember, BTRFS allows for flexible configurations where data and metadata can use different RAID levels. The exact setup would be visible in the output of the command mentioned above.

# Input

Here's what I got from that command:

```
sudo btrfs filesystem df /  
Data, single: total=227.01GiB, used=220.47GiB  
System, RAID1: total=32.00MiB, used=48.00KiB  
Metadata, RAID1: total=7.00GiB, used=6.19GiB  
GlobalReserve, single: total=512.00MiB, used=0.00B
```

# Output

Thank you for providing that additional information. Now we have a clear picture of your BTRFS configuration:

## BTRFS Configuration Details

Your BTRFS setup uses different profiles for different types of data:

1. **Data**: Single
   - Total: 227.01GiB
   - Used: 220.47GiB

2. **System**: RAID1
   - Total: 32.00MiB
   - Used: 48.00KiB

3. **Metadata**: RAID1
   - Total: 7.00GiB
   - Used: 6.19GiB

4. **GlobalReserve**: Single
   - Total: 512.00MiB
   - Used: 0.00B

## Explanation of Your BTRFS Configuration

1. **Data Profile**: Your file data is stored using a "single" profile. This means that data blocks are written to one device at a time, without any redundancy. This configuration maximizes usable space but doesn't provide data redundancy.

2. **System and Metadata**: Both system and metadata are using RAID1. In BTRFS, RAID1 means that these critical filesystem structures are mirrored across at least two devices. This provides redundancy and protection against device failures for important filesystem structures.

3. **GlobalReserve**: This is a special space reserved by BTRFS for emergency operations. It's using a single profile, which is typical.

## Implications of This Setup

- Your setup prioritizes redundancy for system and metadata while maximizing space for actual file data.
- The RAID1 for system and metadata provides some protection against drive failures, ensuring that filesystem structures remain intact even if one drive fails.
- However, your actual file data (which uses the "single" profile) does not have redundancy. If the device containing a particular data block fails, that data would be lost.

## Recommendations

Given this configuration:

1. **Regular Backups**: Since your file data doesn't have redundancy, it's crucial to maintain regular backups of your important files.

2. **Monitoring**: Keep a close eye on the health of all your drives. You can use tools like `smartctl` for this purpose.

3. **Consider Data Redundancy**: If you have critical data, you might want to consider changing the data profile to RAID1 as well, though this would reduce your total usable space.

This setup balances space efficiency with some level of protection for critical filesystem structures. It's a valid configuration, especially if you have a good backup strategy in place.