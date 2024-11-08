---
title: "Automating Restick backup - options, Cron and more"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



To automate the running of your Restic backup script while retaining the ability to monitor progress in a terminal, you have a couple of options—each with their own benefits. Here are your best options for automation on Fedora:

### 1. **Using `cron` for Scheduled Automation**
   - **Description**: `cron` is a well-established tool for automating tasks in Linux. You can schedule the backup script to run at specific intervals, such as daily or weekly.
   - **How to Set Up**:
     1. **Edit Cron Jobs**:
        ```bash
        crontab -e
        ```
     2. **Add a Cron Job** to run the backup script, e.g., every Sunday at 2 AM:
        ```bash
        0 2 * * 0 /home/daniel/Git/Backup-Tools/desktop/Desktop-LAN-Backups-Restic/desktop-ssd-backups/restic-backup.sh >> /var/log/restic-backup.log 2>&1
        ```
        - **Explanation**:
          - `0 2 * * 0`: Runs at 2:00 AM every Sunday.
          - The output will be redirected to a log file (`/var/log/restic-backup.log`) for monitoring purposes.
     - **Pros**:
       - Fully automated with scheduling capabilities.
       - Easy to implement for recurring backups.
     - **Cons**:
       - Lacks a GUI interface for easy on-demand control.
       - Running the script via cron means there’s no terminal to see progress in real-time. You have to check the log files.

### 2. **Using GNOME's Task Scheduler (With GUI)**
   If you prefer a GUI-based task manager to automate or run tasks as needed, there are options that can also display terminal output.

   - **Option 1: GNOME Task Scheduler (`gnome-schedule`)**:
     - GNOME previously had a tool called **GNOME Schedule**, but it is outdated and not readily available in modern repositories.
     - However, a similar effect can be achieved by creating a `.desktop` launcher that runs in a terminal or by using tools such as **KDE's Plasma System Monitor** or **`gnome-terminal`** itself.

   - **Option 2: `gnome-terminal` Custom Command**:
     - You can create a `.desktop` file that opens a terminal and runs your script whenever you want:
       1. **Create a `.desktop` file**:
          ```bash
          nano ~/.local/share/applications/restic-backup.desktop
          ```
       2. **Add the Following Content**:
          ```ini
          [Desktop Entry]
          Version=1.0
          Name=Restic Backup
          Comment=Run Restic Backup Script
          Exec=gnome-terminal -- /home/daniel/Git/Backup-Tools/desktop/Desktop-LAN-Backups-Restic/desktop-ssd-backups/restic-backup.sh
          Icon=utilities-terminal
          Terminal=false
          Type=Application
          Categories=Utility;Backup;
          ```
       - **Explanation**: This `.desktop` file will allow you to run the script by clicking on the icon, and it will open a terminal window showing real-time output.
     - **Pros**:
       - Provides GUI interaction, allowing you to run the script whenever you wish by simply clicking the launcher.
       - You can monitor the output in real time.
     - **Cons**:
       - Not ideal for unattended scheduled backups. More useful for on-demand, manual execution.

### 3. **Using `systemd` Timer Units**
   - **Description**: `systemd` is the core system and service manager for many Linux distributions, including Fedora. Using `systemd` timers, you can automate the script and configure it to run regularly.
   - **How to Set Up**:
     1. **Create a Systemd Service File**:
        ```bash
        sudo nano /etc/systemd/system/restic-backup.service
        ```
        Add the following content:
        ```ini
        [Unit]
        Description=Restic Backup Service

        [Service]
        ExecStart=/home/daniel/Git/Backup-Tools/desktop/Desktop-LAN-Backups-Restic/desktop-ssd-backups/restic-backup.sh
        User=daniel
        ```
     2. **Create a Timer Unit**:
        ```bash
        sudo nano /etc/systemd/system/restic-backup.timer
        ```
        Add the following content:
        ```ini
        [Unit]
        Description=Run Restic Backup Weekly

        [Timer]
        OnCalendar=weekly
        Persistent=true

        [Install]
        WantedBy=timers.target
        ```
     3. **Enable and Start the Timer**:
        ```bash
        sudo systemctl enable restic-backup.timer
        sudo systemctl start restic-backup.timer
        ```
   - **Pros**:
     - More robust scheduling options.
     - Logs can be monitored with `journalctl`.
   - **Cons**:
     - No GUI, though it's powerful for regular tasks.
     - Similar to `cron`—no real-time progress display unless integrated with logging.

### 4. **Using a GUI-Based Task Scheduler (Like `KTimer`)**
   - **Description**: If you’re using KDE or want a simple GUI tool, **KTimer** can be used to schedule or manually start tasks.
   - **How to Install**:
     ```bash
     sudo dnf install ktimer
     ```
   - **How to Use**:
     - Open **KTimer** and add your backup script to it.
     - You can set up one-time or recurring schedules, and launch it whenever you want.
     - However, this might lack direct integration with terminal output. You’d need to ensure your script opens a terminal window if you need real-time monitoring.
   - **Pros**:
     - Easy to use with a GUI.
     - On-demand task running.
   - **Cons**:
     - Does not natively provide terminal output unless explicitly opened through a terminal emulator like `gnome-terminal`.

### Summary
- **For Regular Scheduled Backups**:
  - Use **`cron`** or **`systemd` timers** for automation without user intervention. Both are robust and efficient but won’t provide real-time output unless you check log files.
- **For On-Demand Backups with GUI**:
  - **Create a `.desktop` launcher** that opens a terminal to run the script.
  - Alternatively, use **`gnome-terminal`** commands directly or something like **KTimer** to provide a GUI while still needing terminal output.
- **Combination of Automation and On-Demand**:
  - You could use **cron/systemd** for scheduled runs and also create a `.desktop` file for when you want to trigger the script manually.

Given your preference for monitoring progress in real-time, a `.desktop` launcher or using a terminal-based approach is likely the best option. It provides you with easy access to run the backups when you wish and see the live progress on your Fedora desktop.