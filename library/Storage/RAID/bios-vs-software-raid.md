---
title: "Pros and Cons: Hardware-Level Versus OS-Managed RAID"
---

When using **BIOS-level RAID** (hardware RAID), it is generally more restrictive in terms of **expandability** and **switching RAID types** compared to software RAID. Here's a breakdown of the limitations and possibilities:

### 1. Switching RAID Types

- **BIOS-level RAID**: Once you've set up a RAID array (e.g., RAID 5), you cannot easily switch to another RAID type (e.g., RAID 1 or RAID 0) without **deleting the existing array**, which will result in data loss. If you want to switch RAID types, you'll need to:
  - Backup all your data.
  - Delete the current array in the BIOS.
  - Recreate a new array with the desired RAID type.
  - Restore your data from the backup.
- **Software RAID (`mdadm`)**: Software RAID offers more flexibility. For example, you can change certain aspects of the array (like adding drives or changing levels) without needing to delete and recreate it. However, switching between different RAID levels still requires careful planning and often involves rebuilding the array.

### 2. Adding Disks and Expanding Capacity

- **BIOS-level RAID**:
  - **Limited Expandability**: While some hardware RAID controllers (like Intel's RST on your MSI B760M-A) allow you to add disks to an existing array, this feature is not always guaranteed for all configurations. For example, expanding a **RAID 5** array might involve adding a disk and then rebuilding the array, but this process can be slow and risky if not handled properly.
  - **Capacity Expansion**: You can increase the capacity of a RAID array by replacing each drive with a larger one, but this process requires rebuilding after each replacement. Only after all drives have been replaced will the additional capacity become available\[5].
- **Software RAID (`mdadm`)**:
  - **More Flexibility in Adding Disks**: With `mdadm`, you can add new drives to an existing array more easily. For example, you can grow a RAID 5 array by adding another drive without needing to delete or recreate the array:
    ```bash
    sudo mdadm --add /dev/md0 /dev/sdX
    sudo mdadm --grow /dev/md0 --raid-devices=4
    ```
    This makes software-based solutions more flexible if you plan to expand your storage over time.

### 3. Performance Considerations

- **BIOS-level RAID**:
  - The performance of adding disks or expanding arrays depends on the capabilities of your motherboard's chipset (Intel Rapid Storage Technology in this case). While it may handle parity calculations efficiently for tasks like rebuilding or expanding, it could still be slower than dedicated hardware RAID controllers.
- **Software RAID (`mdadm`)**:
  - Software-based expansion can take longer since parity calculations are handled by the CPU. However, modern CPUs like your Intel i7-12700F are powerful enough that this may not be a major concern unless you're performing very I/O-intensive operations during expansion.

### 4. Data Safety During Expansion

- **BIOS-level RAID**: Expanding an array or changing its configuration at the BIOS level carries some risk, especially if there's a power failure or system crash during the rebuild process. Always ensure you have backups before attempting any changes.
- **Software RAID (`mdadm`)**: Software-based solutions offer better monitoring tools and finer control over rebuilds and expansions, allowing you to pause and resume operations if needed.

### Conclusion:

- If you prioritize simplicity and don't plan on frequently changing or expanding your storage setup, **BIOS-level RAID** is a good option but comes with more restrictions regarding switching types and expanding arrays.
- If you want more flexibility for future expansions or potential changes in your configuration, **software RAID (`mdadm`)** provides better tools for managing arrays without needing to delete them or lose data.

In either case, always ensure that you have reliable backups before making any significant changes to your storage configuration!

&#x20;
