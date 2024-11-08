---
title: "Fedora Drive syncs with multi drive support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Drives on Fedora Linux? I'm looking for a GUI that can handle mounting a few different drives to my system (ideally as "volumes" rather than mounted in a way that has to sync the entire filesystem to function). Important: these are mostly shared drives. KDE Plasma.

# Output

Here are some KDE Plasma-compatible tools and methods for mounting multiple Google Drives, including shared drives, on Fedora Linux as "volumes" without syncing the entire filesystem:

### 1. **KIO GDrive (KDE Integration)**
   - **Overview**: **KIO GDrive** is a KDE Plasma integration that allows you to mount Google Drive (including shared drives) directly into your file manager (Dolphin).
   - **How it works**: Once installed, you can add your Google account and access your Google Drives (both personal and shared) as mounted "volumes" within Dolphin. It doesn’t sync the entire filesystem; you interact with files as needed.
   - **Installation**:
     - Install via: `sudo dnf install kio-gdrive`
     - Add Google Drive via Dolphin by typing `gdrive:/` in the address bar and configuring the Google account.
   - **Pros**: Seamless KDE Plasma integration, no need to sync files locally, works well with multiple accounts.
   - **Cons**: Limited advanced features compared to standalone tools like Rclone.

### 2. **Rclone with Rclone Browser (GUI)**
   - **Overview**: **Rclone** is a powerful tool that supports mounting Google Drive (including shared drives) without syncing. Combined with **Rclone Browser**, you get a GUI for easier management.
   - **How it works**: You configure Rclone to access multiple Google Drive accounts and shared drives, and then use Rclone Browser to mount them as "volumes" on-demand. It supports accessing shared drives natively.
   - **Installation**:
     - Install Rclone: `sudo dnf install rclone`
     - Install Rclone Browser: Follow [Rclone Browser installation](https://github.com/kapitainsky/RcloneBrowser/releases)
     - Configure Rclone to connect to your Google Drive accounts (including shared drives).
   - **Pros**: Highly flexible, supports many cloud storage services, handles shared drives well, no need to sync, works across desktop environments.
   - **Cons**: Setup can be more complex, though the GUI simplifies day-to-day use.

### 3. **Insync**
   - **Overview**: **Insync** is a premium tool for managing Google Drive accounts, including shared drives. It allows you to mount these as "volumes" without syncing the entire content locally.
   - **How it works**: Insync provides a GUI to manage multiple Google Drive accounts and shared drives. You can set it up to mount these drives as needed without syncing files.
   - **Installation**: Available for download [here](https://www.insynchq.com/downloads). Follow the setup instructions for Fedora Linux.
   - **Pros**: Easy to use, supports multiple accounts and shared drives, polished UI, robust features.
   - **Cons**: Paid software, but offers a free trial to test the features.

### 4. **Google Drive OCamlfuse (with GUI Frontend)**
   - **Overview**: **Google Drive OCamlfuse** is a FUSE-based filesystem that allows mounting Google Drive (including shared drives) as a filesystem. You can combine this with a GUI frontend for easier management.
   - **How it works**: Once configured, OCamlfuse mounts Google Drive (including shared drives) as a filesystem, accessible in your file manager like a local drive. It doesn't sync the entire drive, allowing you to access files as needed.
   - **Installation**:
     - Install via: `sudo dnf install google-drive-ocamlfuse`
     - Set up multiple Google Drive accounts, including shared drives.
   - **Pros**: Lightweight, supports multiple accounts and shared drives, open-source.
   - **Cons**: Requires some setup, less user-friendly than other GUI-based options like Insync.

### 5. **ExpanDrive**
   - **Overview**: **ExpanDrive** is a commercial solution that can mount Google Drive and shared drives as "volumes" on your Linux system.
   - **How it works**: ExpanDrive integrates with the file system, allowing you to treat your Google Drive and shared drives like network drives. You interact with files directly without syncing them.
   - **Installation**: Available for download [here](https://www.expandrive.com/expandrive-for-linux/). It supports Fedora Linux.
   - **Pros**: Advanced features, multiple cloud storage options, great for handling shared drives.
   - **Cons**: Paid software, but there’s a free trial available.

### Recommendation:
For seamless KDE Plasma integration, **KIO GDrive** is a great native option. If you're looking for more advanced features and handling of multiple accounts and shared drives, **Rclone with Rclone Browser** offers the most flexibility and control. If ease of use and polished interface are your priorities, **Insync** or **ExpanDrive** would be excellent, though they are paid solutions.