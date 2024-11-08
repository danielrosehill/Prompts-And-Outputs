---
title: "LibNFC script with continuous indefinite polling"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To set up **continuous polling** with **libnfc**, you can modify the approach so that your NFC reader keeps checking for tags indefinitely. Here's how you can adjust your setup:

### Step 1: Modify the Polling Script for Continuous Detection
1. Create a modified script:
   ```bash
   #!/bin/bash
   while true; do
       url=$(nfc-poll 2>/dev/null | grep -oP '(?<=URI: ).*')
       if [ ! -z "$url" ]; then
           google-chrome "$url"
       fi
       sleep 1
   done
   ```
2. Save as `nfc-continuous-poll.sh` and make it executable:
   ```bash
   chmod +x nfc-continuous-poll.sh
   ```

### Step 2: Run the Script
```bash
./nfc-continuous-poll.sh
```

### Explanation:
- **`while true; do ... done`**: Keeps the script running indefinitely.
- **`sleep 1`**: Adds a short delay to avoid constant rapid polling that could overuse resources.

### Automate at Boot (Optional)
You can add the script to **systemd** to run it automatically when the system boots, ensuring it's always active:
1. Create a **systemd** service file:
   ```bash
   sudo nano /etc/systemd/system/nfc-poll.service
   ```
2. Add the following:
   ```ini
   [Unit]
   Description=Continuous NFC Polling Service

   [Service]
   ExecStart=/path/to/nfc-continuous-poll.sh
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
3. Enable and start the service:
   ```bash
   sudo systemctl enable nfc-poll.service
   sudo systemctl start nfc-poll.service
   ```

This setup allows for continuous polling, making it possible to read tags and automatically open URLs whenever a tag is detected.