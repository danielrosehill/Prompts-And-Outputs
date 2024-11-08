---
title: "Setting up a vault on the Ubuntu VM for storing backups"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can configure a dedicated "vault" folder on your Ubuntu server for storing backups and set it up as an NFS share with a separate local IP address. Here’s how you can do it:

### Step 1: Create a Dedicated Network Interface (Optional)
To give the "vault" a separate IP address, you can configure an additional network interface or set up an alias IP on the existing network interface.

1. **Add a New IP Alias**:
   - Edit the Netplan configuration file (assuming Ubuntu uses Netplan):
     ```bash
     sudo nano /etc/netplan/01-netcfg.yaml
     ```
   - Add a new IP alias under your existing network interface:
     ```yaml
     network:
       version: 2
       ethernets:
         enp0s3:
           dhcp4: true
           addresses:
             - 192.168.1.5/24
             - 192.168.1.10/24  # Add this line for the new IP address
     ```
   - Apply the configuration:
     ```bash
     sudo netplan apply
     ```
2. **Verify the New IP Address**:
   ```bash
   ip addr show
   ```

### Step 2: Install and Configure NFS on the Ubuntu Server
1. **Install NFS Server**:
   ```bash
   sudo apt install nfs-kernel-server
   ```

2. **Create the "Vault" Directory**:
   ```bash
   sudo mkdir -p /mnt/backup-vault
   sudo chown nobody:nogroup /mnt/backup-vault
   ```

3. **Configure NFS Exports**:
   - Edit the NFS exports file:
     ```bash
     sudo nano /etc/exports
     ```
   - Add the following line to export the "vault" directory over NFS:
     ```bash
     /mnt/backup-vault 192.168.1.0/24(rw,sync,no_subtree_check)
     ```
     - This allows read-write access from any machine in the `192.168.1.x` network.
     - Adjust the permissions and network range as needed.

4. **Restart NFS Services**:
   ```bash
   sudo exportfs -a
   sudo systemctl restart nfs-kernel-server
   ```

### Step 3: Configure the Fedora Client to Access the NFS Share
1. **Install NFS Client**:
   ```bash
   sudo dnf install nfs-utils
   ```

2. **Mount the NFS Share**:
   - Create a mount point on your Fedora machine:
     ```bash
     sudo mkdir -p /mnt/backup-vault
     ```
   - Add the following line to `/etc/fstab` to automatically mount the NFS share:
     ```bash
     192.168.1.10:/mnt/backup-vault /mnt/backup-vault nfs defaults 0 0
     ```
   - Mount the NFS share:
     ```bash
     sudo mount -a
     ```

### Step 4: Use the NFS Share for Backups
With the NFS share mounted on your Fedora system, you can now direct your backup tools (e.g., Veeam Agent, Duplicati, or BorgBackup) to use `/mnt/backup-vault` as the backup destination.

### Step 5: Additional Tips for Ease of Backup
- **Network Segmentation**: You can configure your network to ensure the backup IP (`192.168.1.10`) is reachable only for backup purposes, adding security.
- **Permissions**: Ensure the correct permissions on `/mnt/backup-vault` to prevent unauthorized access. You can restrict specific IP addresses or hostnames in `/etc/exports`.

### Verification
- Check NFS server status:
  ```bash
  sudo systemctl status nfs-kernel-server
  ```
- Verify if the NFS share is correctly mounted on Fedora:
  ```bash
  df -h | grep backup-vault
  ```

### Benefits:
- **Dedicated Backup IP**: Using a separate IP makes it easier to manage backups and provides flexibility for network configurations or backup routing.
- **Centralized Storage**: The NFS share can act as a centralized backup destination, accessible by multiple machines if needed.
- **Easy Management**: NFS is straightforward to set up and works seamlessly across Linux systems.

By setting up an NFS share with a dedicated IP address, you gain flexibility, centralized storage, and streamlined access for backups across your network.