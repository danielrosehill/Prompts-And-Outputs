---
title: "Batching system scripts around boot events in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

The backup script is great. 

I'm thinking about what the best way to manage a few system scripts like this is. 

Crontab is obvious. Is there a way to perhaps create a master "batch" script that would in turn execute several smaller scripts?

Or a way to set up a batch of scripts that can be executed together at system boot, or wake (from suspend). Or before boot.

# Output

Yes, you can definitely create a **master batch script** that executes several smaller scripts, or you can configure your system to run a batch of scripts at specific events like **system boot**, **wake from suspend**, or even just as part of a **scheduled cron job**.

Here are several ways you can manage and execute multiple scripts together, depending on when and how you want them to run.

### **1. Master Batch Script**

You can create a **master script** that simply runs all of your smaller scripts in sequence.

#### Example: `master_script.sh`

```bash
#!/bin/bash

# Run backup script
echo "[INFO] Running backup script..."
/path/to/backup_script.sh

# Run another script
echo "[INFO] Running sync script..."
/path/to/sync_script.sh

# Run another script
echo "[INFO] Running maintenance script..."
/path/to/maintenance_script.sh

echo "[INFO] All scripts executed."
```

Make this script executable:

```bash
chmod +x /path/to/master_script.sh
```

### **2. Running the Master Script at Boot**
You can configure your system to automatically run your master script when the system **boots** by using systemd or adding it to crontab.

#### Option 1: Using **systemd** for Running at Boot
You can use `systemd` to set up the script to run at boot time.

1. **Create a service file** in `/etc/systemd/system/`:

   ```bash
   sudo nano /etc/systemd/system/master_script.service
   ```

2. **Add the following configuration**:

   ```ini
   [Unit]
   Description=Run master batch script at boot

   [Service]
   Type=oneshot
   ExecStart=/path/to/master_script.sh

   [Install]
   WantedBy=multi-user.target
   ```

3. **Enable the service**:

   ```bash
   sudo systemctl enable master_script.service
   ```

4. **Start the service (for immediate execution)**:

   ```bash
   sudo systemctl start master_script.service
   ```

This will ensure that the master script runs each time the system boots.

#### Option 2: Using **cron** for Running at Boot

You can add the `@reboot` cron option to run the script every time the system boots.

1. Open crontab:

   ```bash
   crontab -e
   ```

2. Add the following line to run your `master_script.sh` at system boot:

   ```bash
   @reboot /path/to/master_script.sh
   ```

### **3. Running the Master Script on Wake from Suspend**
You can run scripts when the system wakes from suspend using **systemd**.

#### Setting up `systemd` for Wake-up Scripts

1. **Create a service file** to trigger on wake-up in `/etc/systemd/system/`:

   ```bash
   sudo nano /etc/systemd/system/wake_script.service
   ```

2. **Add the following configuration**:

   ```ini
   [Unit]
   Description=Run master script on wake from suspend

   [Service]
   Type=oneshot
   ExecStart=/path/to/master_script.sh

   [Install]
   WantedBy=suspend.target
   ```

3. **Enable the service** to run on wake-up:

   ```bash
   sudo systemctl enable wake_script.service
   ```

This will ensure that the script runs whenever the system wakes from suspend.

### **4. Running the Master Script Before Boot (Shutdown, Reboot, etc.)**

If you want to run your script when the system is **shutting down or rebooting**, you can use a similar `systemd` approach but set it to run at these stages.

1. **Create a shutdown service file** in `/etc/systemd/system/`:

   ```bash
   sudo nano /etc/systemd/system/shutdown_script.service
   ```

2. **Add the following configuration**:

   ```ini
   [Unit]
   Description=Run master script before shutdown or reboot

   [Service]
   Type=oneshot
   ExecStart=/path/to/master_script.sh

   [Install]
   WantedBy=halt.target reboot.target shutdown.target
   ```

3. **Enable the service**:

   ```bash
   sudo systemctl enable shutdown_script.service
   ```

Now, the script will run when the system is shutting down or rebooting.

### **5. Combining with Cron for Regular Execution**

If you also want the scripts to run regularly, you can set up a cron job to run the **master script** at specific intervals (e.g., daily or weekly).

1. **Open crontab**:

   ```bash
   crontab -e
   ```

2. **Add the schedule** for your master script. For example, to run it every day at 3 AM:

   ```bash
   0 3 * * * /path/to/master_script.sh
   ```

### **6. Managing Scripts Using a Simple Task Manager**

You can also manage your batch of scripts using a simple tool like **Anacron** (for non-boot systems) or even an automation tool like **Task Spooler** if you want to queue scripts and run them sequentially in the background.

---

### Summary of Approaches:

- **Master Batch Script**: Create a master script that calls smaller scripts in sequence, providing logging and execution management.
- **Systemd**:
  - Run scripts at **boot**, **shutdown**, or **wake** using systemd services.
  - Use `systemd` timers for more control over the scheduling of scripts.
- **Crontab**:
  - Use cron to run the master script at **boot** or **at scheduled times** (e.g., nightly).
- **Task Automation**:
  - Tools like **Task Spooler** or **Anacron** can help manage scheduled or queued tasks if you want more control over parallel or sequential execution.

These options give you flexibility to run and manage your scripts in the most efficient way for your workflow. Let me know if you’d like further customization or assistance with any of these approaches!