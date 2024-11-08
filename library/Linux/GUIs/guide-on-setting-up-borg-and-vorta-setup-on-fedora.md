---
title: "Guide on setting up Borg and Vorta setup on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Can you write me a guide on how to use Vorta + Borg backup. I'll be backing up onto a local Ubuntu VM (on the LAN). I want to create the most comprehensive backup of my fedora workstation possible that would make restoring as quick as possible .. capturing all installations and config files (flatpaks, dnf, etc)

# Output
**Summary of the prompt:** You are asking for a comprehensive guide on using Vorta + Borg to back up your Fedora Workstation onto a local Ubuntu VM on the LAN. You want the backup to capture all installations, configuration files, and other necessary data (including Flatpaks, DNF packages, etc.) for quick restoration.

### **Guide to Backing Up Fedora Workstation with Vorta + Borg onto a Local Ubuntu VM**

This guide will walk you through setting up **Vorta** (a GUI for Borg) to create a comprehensive backup of your Fedora Workstation to a local **Ubuntu VM** over the LAN, ensuring that all essential system data, configurations, and installed packages are captured for quick restoration.

#### **Step 1: Set Up Borg on Your Ubuntu VM**

1. **Install Borg on the Ubuntu VM:**
   First, log into your Ubuntu VM and install Borg:
   ```bash
   sudo apt update
   sudo apt install borgbackup openssh-server
   ```
   - Ensure that **SSH** is running so you can connect from your Fedora system:
     ```bash
     sudo systemctl enable ssh
     sudo systemctl start ssh
     ```

2. **Create a Backup Repository on the Ubuntu VM:**
   On the Ubuntu VM, create a directory to hold your Borg backups. For example:
   ```bash
   mkdir -p /backup/fedora-workstation
   ```
   - You’ll later use this as the Borg repository.

#### **Step 2: Set Up Vorta + Borg on Your Fedora Workstation**

1. **Install Borg on Fedora:**
   First, install Borg on your Fedora Workstation via DNF:
   ```bash
   sudo dnf install borgbackup
   ```

2. **Install Vorta:**
   Vorta is a GUI frontend for Borg, and it can be installed via Flatpak on Fedora.
   - First, ensure Flatpak is installed:
     ```bash
     sudo dnf install flatpak
     ```
   - Then install Vorta from Flathub:
     ```bash
     flatpak install flathub com.borgbase.Vorta
     ```

#### **Step 3: Configure Vorta to Back Up to the Ubuntu VM**

1. **Open Vorta** from the application menu.

2. **Create a New Borg Backup Repository:**
   - Go to the **Repository** tab in Vorta.
   - Click **Add Repository**.
   - In the repository URL, specify the SSH path to your Ubuntu VM, such as:
     ```
     ssh://user@<ubuntu-vm-ip>:22/backup/fedora-workstation
     ```
   - Authenticate using your SSH credentials (or set up SSH keys for passwordless access).

3. **Initialize the Borg Repository:**
   - Once you add the repository, click **Initialize** to create the Borg repository in the specified directory on the Ubuntu VM.

#### **Step 4: Configure Backup Source and Frequency**

1. **Select What to Backup:**
   - In the **Files** tab, select the directories you want to back up. To create a comprehensive system backup, include the following:
     - `/home` – Your home directory (user data).
     - `/etc` – System configuration files.
     - `/usr/local/bin` – Custom binaries.
     - `/var/lib/flatpak` – Flatpak installations.
     - `/usr/lib/flatpak` – Flatpak runtimes.
     - `/var/lib/dnf` – DNF package data.
     - You may exclude unnecessary directories like `/dev`, `/proc`, `/sys`, or temporary directories such as `/var/tmp`.
  
2. **Schedule Regular Backups:**
   - In the **Schedule** tab, set up automatic backups according to your preferences (daily, weekly, etc.).

3. **Enable Compression and Encryption (Optional):**
   - Under the **Repository** settings, you can enable compression to save space and encryption to protect your backup data.

#### **Step 5: Back Up DNF and Flatpak Package Lists**

1. **Backup DNF Package List:**
   You can create a backup of all DNF-installed packages by running:
   ```bash
   sudo dnf list installed > ~/dnf-packages.txt
   ```
   - Include this file in the list of directories to back up using Vorta.

2. **Backup Flatpak List:**
   You can also back up a list of installed Flatpak applications:
   ```bash
   flatpak list --app > ~/flatpak-apps.txt
   ```
   - Include this file in your backup to make reinstallation easier after restoration.

#### **Step 6: Test and Run Your First Backup**

1. **Test Connectivity:**
   - Ensure you can connect to your Ubuntu VM from Fedora using SSH.
   - Test the repository initialization and ensure everything is configured correctly in Vorta.

2. **Run the First Backup:**
   - In Vorta, manually trigger a backup to ensure everything is working. Go to the **Main** tab and click **Backup Now**.
   - Monitor the progress and ensure that all your selected directories are being backed up to the Ubuntu VM.

#### **Step 7: Restoring from the Backup**

If your Fedora system experiences hardware failure, you can restore everything onto new hardware:

1. **Install Fedora** on new hardware, ensuring that Borg and Vorta are installed as before.

2. **Restore Files Using Vorta:**
   - Reconnect to your backup repository on the Ubuntu VM in Vorta.
   - Use the **Restore** function in Vorta to recover your files, including `/home`, `/etc`, `/usr/local/bin`, etc.

3. **Restore DNF and Flatpak Packages:**
   After restoring your home directory:
   - Reinstall all your previous DNF packages:
     ```bash
     sudo dnf install $(cat ~/dnf-packages.txt)
     ```
   - Reinstall Flatpak applications:
     ```bash
     flatpak install $(cat ~/flatpak-apps.txt)
     ```

#### **Step 8: Automating Key-Based SSH Access (Optional but Recommended)**

To make future backups easier, consider setting up **SSH key-based authentication** between your Fedora Workstation and Ubuntu VM. This removes the need for entering a password each time the backup runs.

1. **Generate an SSH key** on your Fedora system if you haven’t done so:
   ```bash
   ssh-keygen -t rsa
   ```

2. **Copy the SSH key to the Ubuntu VM**:
   ```bash
   ssh-copy-id user@<ubuntu-vm-ip>
   ```

3. **Test Passwordless SSH Access**:
   Ensure that you can now SSH into the Ubuntu VM without needing a password:
   ```bash
   ssh user@<ubuntu-vm-ip>
   ```

### **Conclusion**

Using **Vorta + Borg** for backing up your Fedora Workstation to an Ubuntu VM on your LAN is a robust solution that allows for secure, compressed, and encrypted backups. By backing up critical directories and package lists, you ensure that your system can be quickly restored in case of failure. The combination of **regular automated backups**, **easy restoration via Vorta**, and **SSH key-based authentication** makes this setup comprehensive and reliable for disaster recovery.