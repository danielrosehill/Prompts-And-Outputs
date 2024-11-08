---
title: "GUIs for ongoing RAID monitoring"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great work. Please add to this whether there are any GUIs that could help me monitor the ongoing health of my RAID1 config. And finally (in a new section) if I wanted to add more storage or move to a different raid config is that would be possible

# Output

Here’s an updated guide that includes information about GUI tools for monitoring RAID arrays and instructions on expanding storage or changing RAID configurations.

---

# Admin Guide: Monitoring RAID1 Setup and Post-Migration Health Checks
 

### GNOME Disks
- **Description**: GNOME Disks is a pre-installed tool on Fedora Workstation that can manage and monitor disk health.
- **Features**: Allows you to view RAID devices, check disk health, and set up SMART data monitoring.
- **How to Use**:
  1. Open **GNOME Disks** from your applications menu.
  2. Select the RAID device from the left panel to view details, including health status and SMART data.

### Cockpit
- **Description**: Cockpit is a web-based GUI for server and system management that includes RAID monitoring capabilities.
- **Installation**:
  ```bash
  sudo dnf install cockpit
  sudo systemctl enable --now cockpit.socket
  ```
- **Access**: Open your browser and go to `http://localhost:9090`. Log in with your admin credentials.
- **RAID Monitoring**: Within Cockpit, navigate to **Storage** to view RAID health and manage disks.

### Webmin
- **Description**: Webmin is a comprehensive system administration tool accessible via a web browser.
- **Installation**: Follow instructions at [Webmin’s website](http://www.webmin.com/) to download and install.
- **RAID Module**: Webmin includes a RAID module for monitoring and configuring RAID arrays.
- **How to Use**: After installing, open `http://localhost:10000` in a web browser, log in, and navigate to **Hardware > RAID** for monitoring.

## 5. Expanding Storage or Changing RAID Configuration

If you decide to add more storage or change your RAID configuration, here’s what you need to know:

### Expanding Storage
- **Add New Disks**: If you have available slots, you can add additional disks to the system.
- **Grow RAID Array**:
  1. Identify the new disk with `lsblk` or `fdisk -l`.
  2. Add the disk to the RAID array with:
     ```bash
     mdadm --add /dev/mdX /dev/sdY
     ```
     Replace `/dev/mdX` with your RAID device and `/dev/sdY` with the new disk.
  3. Grow the RAID1 array to include the new disk:
     ```bash
     mdadm --grow /dev/mdX --raid-devices=N
     ```
     Replace `N` with the new total number of devices in the array.

### Changing RAID Configuration
- **Backup Data**: Always back up your data before making significant changes.
- **Converting to RAID5 or RAID10**:
  1. For RAID5 (requires at least 3 disks) or RAID10 (requires at least 4 disks), use:
     ```bash
     mdadm --grow /dev/mdX --level=5 --raid-devices=3
     ```
     Adjust the RAID level and number of devices as needed.
  2. After reconfiguration, the system will rebuild the RAID array. Monitor the progress with `cat /proc/mdstat`.
  
**Note**: Moving between RAID configurations (e.g., from RAID1 to RAID5) may require rebuilding the array and will involve downtime. Using a tool like `mdadm` on the command line is recommended for advanced RAID operations.

**Additional Consideration**: 
If you want to expand storage without changing RAID levels, consider adding another RAID array to your system, as combining multiple RAID configurations requires expertise and could affect data redundancy.

--- 

Feel free to let me know if you need further customization on these instructions or additional steps for specific RAID types!