---
title: "Making better use of  network storage"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have some great local storage options at home than I'm not really taking advantage of. Those are my NAS and my old desktop which I repurposed as a local server. How can I make those easier to use from my Fedora workstation for the purpose of storing files? I'm thinking specifically that I could store some local LLMs on them so that they don't take up so much space on my local machine. Or other big AI files that I don't need all the time

# Output

To make better use of your **NAS** and **local server** for storing large AI files (like local LLMs), there are several ways to seamlessly integrate these storage options with your **Fedora workstation**. This will allow you to offload storage while maintaining easy access when needed.

### Steps to Set Up Network Storage for Easy Use:

#### 1. **Mounting NAS and Local Server Shares**
   You can mount both your NAS and your repurposed desktop server as **network drives** on your Fedora machine. This way, you can access the files as if they were local folders.

   - **For NAS**:
     If your NAS supports **SMB/CIFS** (common for most NAS devices), you can mount the NAS share on Fedora.
     1. Install the required packages:
        ```
        sudo dnf install cifs-utils
        ```
     2. Create a mount point for the NAS share:
        ```
        sudo mkdir /mnt/nas
        ```
     3. Add the NAS mount to `/etc/fstab` for auto-mounting at boot. The line might look something like this:
        ```
        //nas_ip_address/share_name /mnt/nas cifs username=nas_username,password=nas_password,uid=1000,gid=1000 0 0
        ```
        Replace `nas_ip_address`, `share_name`, `nas_username`, and `nas_password` with your NAS details.

     Alternatively, you can mount it temporarily using the `mount` command:
     ```
     sudo mount -t cifs -o username=nas_username,password=nas_password //nas_ip_address/share_name /mnt/nas
     ```

   - **For Local Server**:
     If your old desktop is running Linux, you can use **NFS** (Network File System) to mount shares from it.
     1. On your local server, install the NFS server:
        ```
        sudo apt install nfs-kernel-server  # For Ubuntu/Debian
        sudo dnf install nfs-utils          # For Fedora
        ```
     2. Edit the NFS exports file (`/etc/exports`) on the server to allow access from your workstation:
        ```
        /path/to/shared/folder 192.168.1.x(rw,sync,no_subtree_check)
        ```
     3. On Fedora, install the NFS client:
        ```
        sudo dnf install nfs-utils
        ```
     4. Create a mount point and mount the NFS share:
        ```
        sudo mkdir /mnt/server
        sudo mount -t nfs server_ip:/path/to/shared/folder /mnt/server
        ```
     5. You can add this to `/etc/fstab` for automatic mounting at boot:
        ```
        server_ip:/path/to/shared/folder /mnt/server nfs defaults 0 0
        ```

#### 2. **Setting Up SSHFS for Remote Access**
   If you prefer using **SSH** for secure access to your local server or NAS, you can mount the remote directories via **SSHFS**.

   1. Install SSHFS on Fedora:
      ```
      sudo dnf install sshfs
      ```
   2. Mount the remote directory:
      ```
      sshfs user@server_ip:/path/to/shared/folder /mnt/server
      ```
   3. You can also add SSHFS mounts to your startup script or **fstab** for persistence:
      ```
      user@server_ip:/path/to/shared/folder /mnt/server fuse.sshfs defaults 0 0
      ```

#### 3. **Using rsync for Backup or Syncing AI Models**
   If you don’t need constant access to the models and files, but you want to **offload** them from your local machine while keeping them synchronized, you can use **rsync** to back them up.

   Example of syncing your AI models folder to your NAS:
   ```
   rsync -avz /local/path/to/models/ user@nas_ip:/path/to/nas/models/
   ```

   You can set this up as a **cron job** or **systemd service** to run automatically at set intervals.

#### 4. **Mounting Using GUI Tools**
   If you prefer not to deal with terminal commands:
   - **GNOME Disks** or **KDE’s Dolphin** (if you're using KDE) can help you mount network drives (SMB/NFS/SSHFS) via the GUI, making it simple to integrate network shares into your system without editing configuration files.

   In **Dolphin** (KDE’s file manager), you can add network shares by going to:
   ```
   Network → Add Network Folder → SMB or NFS
   ```

#### 5. **Optimizing for AI Workflows**
   - **Symbolic Links**: You can use symbolic links to map directories in your NAS or server into your local workspace, making it easier to interact with them in your workflows:
     ```
     ln -s /mnt/nas/models /home/user/models
     ```
   - **Cache Models Locally**: For large AI models that are slow to load over the network, consider setting up **cache directories** where models are loaded from the network and cached locally for faster access.

#### 6. **Security Considerations**
   - Ensure that your NAS and local server are securely configured:
     - **SSH keys** instead of passwords for SSHFS.
     - Use **firewalls** and **VLANs** to isolate these devices from external networks.
     - Use **encrypted storage** for sensitive AI files and backups, especially if models contain proprietary data.

### Conclusion
By mounting your **NAS** and **local server** to your Fedora workstation using **SMB/NFS** or **SSHFS**, you can store large AI models and datasets remotely, freeing up local space while maintaining easy access to these files. Using **rsync** for backups and automating the mounting processes through **fstab** or GUI tools will streamline your workflow, making it easier to work with large files without filling up your local drives.

Let me know if you'd like help with the specifics of setting up any of these configurations!