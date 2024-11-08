---
title: "Can you expand a BTRFS with RAID1?"
---

You asked whether it would still be possible to expand storage or add new drives in the future if you set up **RAID 1** to protect against drive failure. Based on your **OpenSUSE** system and the hardware context you provided, here’s a detailed answer:

### Expanding Storage with RAID 1 (Btrfs)

If you set up **RAID 1** using **Btrfs**, it is indeed possible to expand the storage by adding new drives in the future. **Btrfs** offers a lot of flexibility when it comes to managing RAID arrays, including adding or replacing drives without needing to rebuild the entire array. Here’s how this works:

#### Adding New Drives in Btrfs RAID 1

- **Btrfs RAID 1** does not require all drives to be of the same size, which gives you flexibility when expanding storage.
- When you add a new drive, Btrfs will automatically rebalance the data across all available devices. However, the amount of usable space will still be limited by the smallest drive in the array since RAID 1 mirrors data across two drives.

#### Steps to Add a New Drive:

1. **Add the new drive:**\
   You can add a new drive to your existing RAID 1 setup using this command:
   ```bash
   sudo btrfs device add /dev/sdX /mnt/raid
   ```
   Replace `/dev/sdX` with the actual device name and `/mnt/raid` with your mount point.
2. **Rebalance the array:**\
   After adding a new drive, you need to rebalance the data across all drives:
   ```bash
   sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /mnt/raid
   ```
   This process ensures that data is mirrored correctly across all available drives.

#### Considerations When Expanding Storage:

- **Drive Size Mismatch:** If you add a larger drive, Btrfs will only use space equivalent to the smallest drive for mirroring. For example, if you have two 1TB drives and add a 2TB drive, only 1TB of the new drive will be used for RAID 1 mirroring unless you replace one of the smaller drives later.
- **Balancing:** The rebalance operation can take some time depending on how much data is stored and how large your drives are. It may also cause wear on SSDs due to intensive read/write operations.

### Future Expansion Options:

- You can continue adding more drives as needed, but keep in mind that RAID 1 will always mirror data across two drives, so your total usable storage will be limited by the smallest pair of drives.
- If you want more efficient use of space while maintaining redundancy, you can consider switching to other RAID levels like **RAID 5** or **RAID 10**, but these configurations come with different trade-offs in terms of performance and redundancy.

### Conclusion:

Yes, it is possible to expand your storage in a Btrfs RAID 1 setup by adding new drives. Btrfs provides flexible options for managing RAID arrays, allowing you to add or replace drives without losing data. However, remember that RAID 1 mirrors data across pairs of drives, so your usable space will always be limited by the smallest drive unless you replace smaller ones with larger ones over time.

&#x20;
