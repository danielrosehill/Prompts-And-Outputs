---
title: "Restic versus Borg for local backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The choice between **Restic** and **Borg** can depend largely on your specific needs and preferences, as both tools are highly capable but have distinct advantages. Here’s a deeper comparison of why **Restic** might be preferred in some situations over **Borg**, as well as what makes Borg attractive. 

### Why I Recommended Restic
1. **Simplicity and Ease of Setup**:
   - **Platform-Independent Setup**: Restic is very straightforward to set up across different platforms, including Linux, macOS, and Windows. It doesn’t require special configurations to set up repositories on various storage backends. Borg, on the other hand, requires the use of **Borgmatic** or similar tools to simplify the setup for more complex backup requirements.
   - **No Special Repositories Needed**: Restic uses simple repository storage that is easy to initialize and doesn’t require the same level of integration as Borg, which relies on a specially structured repository that must be accessed by Borg itself.

2. **Broad Backend Support**:
   - **Multiple Storage Backends**: Restic supports a wide range of storage backends, such as local disks, SFTP, AWS S3, Backblaze B2, Google Cloud Storage, Azure, and many others. It’s particularly popular for **cloud backups**, and it natively integrates well with various cloud storage solutions. Borg, by default, focuses more on local and network storage (using SSH).
   - **Cloud Focus**: If you need to easily integrate cloud storage as a backup target, Restic is often more convenient, whereas Borg would require a remote server or additional setup (e.g., using **rclone** as an intermediary).

3. **Self-Contained Binaries**:
   - **Cross-Platform Support**: Restic is distributed as a self-contained binary, which makes it very easy to install and update on different operating systems without dealing with dependencies. Borg, while powerful, requires additional libraries such as **liblz4**, and installation can sometimes be more complex across platforms.

4. **Efficient Use of Resources**:
   - **Low Memory Usage**: Restic is known for being **lightweight** in terms of memory usage. In some use cases, especially on systems with limited resources, Restic’s design might allow for better performance compared to Borg.
   - **Multithreading**: Restic supports multithreaded backups, which can significantly improve backup speeds, especially when dealing with lots of small files. Borg is single-threaded, which can make it slower in some cases.

### Where Borg Excels (GUI, Features, and Other Advantages)
1. **GUI Support**:
   - **Better GUI Options**: As you noted, **Borg** has better GUI support compared to Restic. **Vorta**, the GUI for Borg, is well-maintained and offers a feature-rich interface for managing backups, scheduling, viewing repositories, and handling restores. If a user-friendly GUI is essential, Borg with Vorta is an attractive option.

2. **Deduplication and Compression**:
   - **Very Efficient Deduplication**: Borg's deduplication is highly efficient, and it’s one of its key strengths. Deduplication occurs across the entire repository, meaning that even small changes between files lead to very little increase in storage usage. Restic also supports deduplication, but some users report that Borg’s deduplication is more effective for very large datasets with lots of repetitive data.
   - **Custom Compression**: Borg offers **different compression methods** (e.g., lz4, zlib, zstd), allowing users to choose the level of compression that best fits their needs. Restic, on the other hand, offers basic compression and is more focused on encryption.

3. **Speed**:
   - **Faster for Local Backups**: Borg can be faster for local backups, especially when using SSH to a remote server. It is optimized for **LAN and local storage** performance, which makes it ideal for backing up between servers or across the local network.
   - **Snapshots**: Borg’s incremental snapshots are very fast since they are based on deduplication at the block level, which reduces both storage usage and backup time.

4. **Compression Efficiency**:
   - **Compression Support**: Borg allows advanced options for compressing backups, making it suitable for environments where storage efficiency is key. This flexibility can be particularly useful for those backing up large amounts of data locally.

### Situations Where Restic Might Be Better:
1. **Cloud Backups**: 
   - If you're planning to back up to cloud storage, **Restic** is generally more straightforward. It has native support for S3, B2, Azure, and many other backends, whereas Borg often requires the use of **rclone** to extend its capabilities for cloud.

2. **Cross-Platform Usage**:
   - Restic’s **cross-platform compatibility** makes it more convenient for users who need to back up different operating systems. It is easy to install and run on **Linux, Windows, and macOS** without complex configurations.

3. **Quick Setup for Simple Needs**:
   - Restic is more **lightweight** and simpler to use for smaller, straightforward backup jobs. It has fewer configuration steps, making it ideal for personal or home use when someone needs a backup solution that’s **easy to implement without complex requirements**.

4. **Encryption Focus**:
   - Restic places strong emphasis on **encryption**, and all backups are encrypted by default. While Borg also supports encryption, Restic's simplicity in dealing with encryption keys, and its ease of use for setting up encrypted backups, makes it a go-to choice for security-conscious users.

### Summary of Trade-offs
- **Restic**:
  - Best for **cloud backups**, easy setup, cross-platform compatibility, multithreading, and built-in encryption.
  - More user-friendly for setting up quick backups and restoring them without complex tools.
  - Often simpler for remote backups with native support for cloud storage services.

- **Borg**:
  - Excellent for **local and LAN backups**, **highly efficient deduplication**, and **compression**.
  - Stronger **GUI support** with tools like **Vorta**.
  - Often faster for **incremental backups** with lots of changes, especially when working with local or SSH storage backends.

Ultimately, I recommended **Restic** because it fits well with your use case of **desktop to SSD backups**, combined with the need for ease of setup, encryption, and flexibility across platforms. Borg, while powerful, does require a bit more setup and dependency management, and its strengths are more evident when dealing with **complex local or LAN backups** with compression requirements and deduplication across multiple clients or data sets. The best choice really depends on your specific priorities—simplicity and cloud support for Restic, or efficiency and GUI support for Borg.