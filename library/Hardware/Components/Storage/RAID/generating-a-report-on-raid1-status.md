---
title: "Generating a report on RAID1 status"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

You may recall that I recently adding RAID1 to my system which is Fedora Workstation 40 and BTRFS.

I would like to generate a periodic report on how my system is performing and assess how well the RAID is working. 

It would be useful to receive this information in some kind of cloud portal? BUt a second best would be receiving the log by email.

Can you think of a way to do this? But first, perhaps you can give me a command (or a script) that I can run manually to generate something like a report? 

In addition to the RAID status, it should list all my current drives, their capacities, and ideally also their manufacturers and product numbers

# Output

You can generate a manual report on your system performance, RAID status, and detailed information about your drives using a combination of tools like `btrfs`, `lsblk`, `smartctl`, and `mdadm`. Here’s a script you can run manually to get all the information you need:

### Script to Generate a RAID and Drive Report
```bash
#!/bin/bash

# Output file for the report
REPORT_FILE=~/raid_report_$(date +%F).txt

# Get system info
echo "=== System Report - $(date) ===" > "$REPORT_FILE"
echo "Hostname: $(hostname)" >> "$REPORT_FILE"
echo "Kernel Version: $(uname -r)" >> "$REPORT_FILE"
echo "Uptime: $(uptime)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# RAID Status (for BTRFS RAID)
echo "=== BTRFS RAID Status ===" >> "$REPORT_FILE"
btrfs filesystem df / >> "$REPORT_FILE"
btrfs device stats / >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# List all block devices and their sizes
echo "=== Drives and Capacities ===" >> "$REPORT_FILE"
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# List manufacturer and product details using smartctl
echo "=== Drive Information (Manufacturer and Model) ===" >> "$REPORT_FILE"
for drive in $(lsblk -nd -o NAME | grep -E "^sd|nvme"); do
    echo "Drive: /dev/$drive" >> "$REPORT_FILE"
    sudo smartctl -i /dev/$drive | grep -E "Device Model|Model Family|Serial Number|Capacity" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
done

# Print output path
echo "Report generated at $REPORT_FILE"
```

### Key Components of the Script:
1. **BTRFS RAID Status**:
   - `btrfs filesystem df /`: Provides usage statistics for your RAID array.
   - `btrfs device stats /`: Displays errors and statistics for the devices in your BTRFS array.

2. **Drive Information**:
   - `lsblk`: Lists all block devices along with their sizes.
   - `smartctl`: Fetches manufacturer and model information for each drive. You’ll need `smartmontools` installed (`sudo dnf install smartmontools`).

### Running the Script:
Save this script as `generate_raid_report.sh`, make it executable:
```bash
chmod +x generate_raid_report.sh
```
Then run it manually:
```bash
./generate_raid_report.sh
```
It will generate a report in your home directory (`~/raid_report_<date>.txt`), which contains detailed RAID status and drive information.

### Setting Up Periodic Reporting:

Now that you have a script to generate a report, here’s how you can automate the process and either upload it to a cloud portal or send it via email.

#### 1. **Email the Report (Using `mailx`)**
Install `mailx` (or any other mail client):
```bash
sudo dnf install mailx
```
Modify the script to email the report:
```bash
mailx -s "RAID and Drive Report - $(date)" your.email@example.com < "$REPORT_FILE"
```

#### 2. **Automating with Cron**
You can automate the script by setting up a cron job that runs the report generation and sends the output daily, weekly, or however often you like.

Example of a cron job that runs daily at 2 AM:
```bash
0 2 * * * /path/to/generate_raid_report.sh
```

#### 3. **Cloud-Based Solution**
If you prefer to store the report on a cloud portal, you can use a tool like `rclone` to upload the generated report to cloud storage services (Google Drive, Dropbox, etc.).

To do this, install `rclone`:
```bash
sudo dnf install rclone
```
Set up `rclone` for your cloud provider, and then modify the script to upload the report to the cloud:
```bash
rclone copy "$REPORT_FILE" remote:your-cloud-folder/
```

Let me know if you'd like further assistance with any specific part of this setup, or if you prefer one of the methods for automating this process!