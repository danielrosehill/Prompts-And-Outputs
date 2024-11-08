---
title: "Whole disc encryption on top of BTRFS"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

You have context of my current OS and BTRFS setup. Would I be able to add on whole disc encryption? And If I were to do so, what kind of performance overhead might I expect?

# Output

Based on your current setup, which includes Fedora Workstation 40 with a **BTRFS file system** and a **multi-drive configuration** using RAID1【6†source】, it is indeed possible to add **whole disk encryption**. Here’s a breakdown of how this would work and the expected performance overhead:

### Adding Whole Disk Encryption on Fedora with BTRFS

Fedora supports whole disk encryption using **LUKS (Linux Unified Key Setup)**. BTRFS can be layered on top of LUKS to provide both encryption and the advanced features of BTRFS, such as snapshots, compression, and RAID. You can encrypt the entire disk or just specific partitions.

### How to Implement LUKS Encryption:
1. **Backup Your Data**: Always create backups before modifying your disk setup.
2. **Reformat with LUKS Encryption**:
   - You would need to reformat the drives or partitions that you want to encrypt. This process typically requires erasing the existing data on the drive, though it is possible to encrypt individual partitions and then move data back.
   - When installing or setting up Fedora, choose the **custom partitioning option**, select **LUKS encryption**, and layer **BTRFS** on top of it.
   
3. **Enable Encryption on Existing BTRFS**:
   - To encrypt existing partitions without wiping them, you would need to create new LUKS-encrypted partitions and migrate the data from your unencrypted BTRFS partition to the encrypted one.

4. **TPM Integration**: Since you are interested in hardware security, you could integrate the **TPM** module to store the encryption keys securely, reducing the need for manual passphrase input during boot.

### Performance Overhead

The performance impact of disk encryption depends on several factors, including the hardware, the encryption algorithm used, and the workload. Given your workstation’s hardware (Intel Core i7-12700F, 32GB of RAM, and an AMD Radeon RX 7700 XT GPU), the performance impact should be manageable, but there will still be some overhead.

Here’s what you can expect in terms of performance:

1. **CPU Impact**: 
   - The i7-12700F supports hardware-accelerated AES encryption (via **AES-NI**), which means encryption and decryption operations will be fast. Most modern CPUs, including yours, minimize the overhead from disk encryption.
   - Performance hit for modern CPUs with AES-NI support is typically around **1–5%**, depending on workload intensity.

2. **Disk I/O Performance**:
   - **Read/Write Latency**: Disk encryption typically adds a small amount of latency due to the need to encrypt and decrypt data on the fly. This could result in **5-10% slower disk I/O** for standard workloads like file transfers, depending on the size of the files.
   - **RAID Configuration**: Your BTRFS RAID1 setup will mirror data between drives. With LUKS, the encryption process happens before BTRFS mirrors the data, so the impact on RAID1 itself should be minimal, but there will be a minor performance overhead related to encryption before the mirroring takes place.

3. **Boot Time**:
   - There will be a slight increase in boot time due to the need for decryption of the root partition. If you use a passphrase, you’ll need to input it at boot, or you can configure the system to automatically unlock using TPM, a USB key, or network-based unlocking.

4. **File System Overhead**:
   - **BTRFS** features such as compression or snapshots might add slight overhead on top of LUKS encryption, but these are generally minimal. If you use features like deduplication, the performance impact could be slightly higher because deduplication needs to work with encrypted blocks, which might reduce deduplication efficiency.

### Summary of Performance Overhead:
- **CPU**: 1–5% overhead due to encryption operations, minimal due to AES-NI support in your CPU.
- **Disk I/O**: 5–10% slower read/write speeds for large file transfers or I/O-heavy tasks.
- **Boot Time**: Slight increase due to decryption during boot.
- **File System**: BTRFS features add minimal extra overhead; no major impact expected with LUKS.

### Alternatives for Minimizing Overhead:
- **Partial Encryption**: Instead of whole-disk encryption, you can opt for encrypting only sensitive partitions (like `/home` or `/var`), which reduces the performance impact on system-critical partitions like `/boot` and `/`.
- **Hardware-based Encryption**: Use of **self-encrypting drives (SEDs)** could offload encryption to the hardware level, further reducing overhead.

Would you like more detailed instructions on setting up LUKS encryption, or suggestions on how to minimize overhead for specific use cases?