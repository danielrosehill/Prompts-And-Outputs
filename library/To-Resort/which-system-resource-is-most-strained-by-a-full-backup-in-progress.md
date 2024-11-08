---
title: "Which system resource is most strained by a full backup in progress"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


When performing a full system backup with Restic onto an SSD, there are several system resources that will come under significant load. Below are the key system resources that are typically impacted, in order of how much "stress" they are likely to experience:

### 1. **Disk I/O (Input/Output Operations)**
   - **What to Expect**: Disk I/O is the **most affected** resource during a full system backup. Restic reads all files from the source disk and writes backup data to the SSD.
   - **Impact**:
     - The source disk will have a lot of read operations since Restic needs to read every file in order to back it up.
     - The destination SSD will experience significant write activity as Restic writes data to the backup repository.
   - **How to Monitor**: You can use tools like `iotop` or `dstat` to monitor disk I/O activity.
     ```bash
     sudo iotop
     ```
   - **Symptoms of Stress**: Slow system responsiveness, longer read/write times for other applications, especially if the system is performing a lot of other read/write-intensive tasks concurrently.

### 2. **CPU Usage**
   - **What to Expect**: Restic uses CPU resources to **process, compress, encrypt, and deduplicate** data before writing it to the backup repository. The load can be significant depending on the size of the files and the level of deduplication and encryption involved.
   - **Impact**:
     - **Encryption**: Restic encrypts data before saving it, which can be computationally intensive.
     - **Compression**: Depending on whether compression is being used, the CPU usage can increase significantly as files are processed.
     - **Deduplication**: Restic also deduplicates data, comparing files and avoiding duplication, which may also increase CPU workload.
   - **How to Monitor**: You can use `htop` or `top` to monitor CPU usage.
     ```bash
     htop
     ```
   - **Symptoms of Stress**: High CPU usage will manifest as slower performance for CPU-bound tasks and general system sluggishness during the backup.

### 3. **Memory (RAM) Usage**
   - **What to Expect**: Restic utilizes memory for managing file indexes, data chunks, and caching during the backup. The amount of memory used can increase significantly if the dataset is large.
   - **Impact**:
     - If the system has enough RAM, you may not notice a severe impact. However, if RAM is limited, Restic could push your system into using swap space, which would in turn put more load on the disks and slow down the overall system performance.
   - **How to Monitor**: Use `free -h` or `htop` to check RAM usage.
     ```bash
     free -h
     ```
   - **Symptoms of Stress**: If the system runs out of available RAM, it could become sluggish, and swapping may occur, leading to slower performance.

### 4. **Network Usage (If Backing Up Remotely)**
   - **What to Expect**: In your case, since you are backing up locally to an SSD, network usage is not a major concern. However, if Restic were backing up to a remote destination, network bandwidth would be a major consideration, and the load would depend on the speed and capacity of the network connection.
   - **Impact**: For local SSD backups, this isn’t relevant, but worth noting if switching to a remote destination in the future.

### Resource Summary:
- **Most Stressed**:
  - **Disk I/O**: Expect heavy reads from the source disk and writes to the SSD.
  - **CPU**: Expect significant usage for encryption, compression, and deduplication.
- **Moderately Stressed**:
  - **Memory (RAM)**: RAM usage can increase depending on the dataset's size, especially if there are many files.
  
### Tips to Reduce Resource Impact:
1. **Limit CPU Usage**: You can limit the impact on CPU by using a tool like `cpulimit` or `nice` to lower the priority of the Restic backup process.
   ```bash
   nice -n 19 restic backup --exclude-file=$EXCLUDES_FILE --one-file-system --verbose -r $REPOSITORY /
   ```
2. **Limit I/O Priority**: Use `ionice` to reduce the I/O priority of the Restic backup, which can help keep the system responsive during the backup.
   ```bash
   ionice -c2 -n7 restic backup --exclude-file=$EXCLUDES_FILE --one-file-system --verbose -r $REPOSITORY /
   ```
3. **Backup During Off-Peak Hours**: Run backups during times when system usage is low, such as overnight or when you are not actively using the computer.

Monitoring and managing these resources can help ensure that your system remains usable while the backup is running, and help minimize any negative impacts on performance during the process.