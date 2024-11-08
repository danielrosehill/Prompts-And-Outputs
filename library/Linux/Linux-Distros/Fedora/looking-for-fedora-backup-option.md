---
title: "Looking for Fedora backup option"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm trying to find a simple way to back up my Fedora workstation computer. I have storage in b2 that could be used for this purpose and a local NAS. I'd like to back up the list of programs that I have installed and some config files. I don't even need many local files. I'd prefer to use a commercial tool rather than have to get involved in scripting things myself, ideally one that is paid and has good support. Can you think of any options?

# Output

For backing up your Fedora Workstation with a focus on commercial tools and good support, here are some options that could work well with your setup:

1. **Veeam Agent for Linux:**
   - Supports various backup targets, including NAS and cloud storage.
   - Can perform snapshot-based backups for BTRFS and other filesystems.
   - Offers commercial support and is well-regarded for its reliability.

2. **MSP360 (formerly CloudBerry) Backup:**
   - Supports over 20 cloud storage services, including Backblaze B2.
   - Offers features like compression, encryption, scheduled backups, and incremental backups.
   - Provides a user-friendly interface and commercial support.

3. **Duplicacy:**
   - A cross-platform backup tool known for its deduplication capabilities.
   - Supports Backblaze B2 and other cloud storage providers.
   - Offers a GUI version and commercial support options.

4. **Restic with Backblaze B2:**
   - While Restic is open-source, it’s robust and integrates well with Backblaze B2.
   - You can set it up with systemd for automated backups.
   - Consider using a GUI wrapper like Vorta for ease of use.

5. **GoodSync:**
   - Offers file synchronization and backup capabilities.
   - Supports NAS devices and cloud storage like Backblaze B2.
   - Provides a graphical interface and commercial support.

6. **Duplicati:**
   - Easy to use with a web-based interface.
   - Supports encrypted backups to various cloud services, including Backblaze B2.
   - While it’s free, you can find community support and documentation.

### Setting Up Backups

- **Local NAS Backup:** Use tools like Veeam or GoodSync to back up directly to your NAS. Ensure your NAS is configured to accept connections from your Fedora machine.

- **Cloud Backup:** For Backblaze B2, tools like MSP360 or Duplicacy can be configured to back up directly to the cloud. They offer straightforward integration with B2 storage.

These tools should help you efficiently back up your system configurations, installed programs list, and essential files while providing the commercial support you prefer.

 