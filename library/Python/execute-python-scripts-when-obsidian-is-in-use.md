---
title: "Execute Python scripts when Obsidian is in use"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have created several python scripts for running some important automations on my Obsidian Vault. Is there a way that I could set these up to automatically run whenever the program is open (but only then). My desktop OS is Fedora Linux.

# Output

Certainly! Here's a comprehensive guide with all the steps to set up your Python scripts to run automatically whenever Obsidian is open on your Fedora Linux system:

## Step 1: Create the Wrapper Script

1. Open a terminal and create a new file:

```bash
nano ~/obsidian_scripts_runner.sh
```

2. Add the following content to the file:

```bash
#!/bin/bash

while true; do
    if pgrep -x "obsidian" > /dev/null; then
        # Obsidian is running, execute your Python scripts
        python3 /path/to/your/script1.py
        python3 /path/to/your/script2.py
        # Add more scripts as needed
    fi
    sleep 300 # Wait for 5 minutes before checking again
done
```

3. Save the file (Ctrl+X, then Y, then Enter).

4. Make the script executable:

```bash
chmod +x ~/obsidian_scripts_runner.sh
```

## Step 2: Create a Systemd User Service

1. Create a new service file:

```bash
mkdir -p ~/.config/systemd/user
nano ~/.config/systemd/user/obsidian-scripts.service
```

2. Add the following content to the file:

```
[Unit]
Description=Obsidian Scripts Runner
After=graphical-session.target

[Service]
ExecStart=/bin/bash /home/YOUR_USERNAME/obsidian_scripts_runner.sh
Restart=always

[Install]
WantedBy=default.target
```

3. Replace `YOUR_USERNAME` with your actual username.

4. Save the file (Ctrl+X, then Y, then Enter).

## Step 3: Enable and Start the Service

Run the following commands in the terminal:

```bash
systemctl --user daemon-reload
systemctl --user enable obsidian-scripts.service
systemctl --user start obsidian-scripts.service
```

## Step 4: Verify the Service

Check the status of the service:

```bash
systemctl --user status obsidian-scripts.service
```

## Additional Notes:

- Replace `/path/to/your/script1.py` and `/path/to/your/script2.py` in the wrapper script with the actual paths to your Python scripts.
- Adjust the sleep interval (currently 300 seconds or 5 minutes) in the wrapper script if you want to change how frequently the scripts run.
- The scripts will only run when Obsidian is open and will automatically stop when Obsidian is closed.
- The service will start automatically on system boot, so your scripts will run whenever you open Obsidian without needing to manually start anything.

This setup ensures that your Python scripts run periodically as long as Obsidian is open on your Fedora Linux system.

# Follow Up

Is it okay for the script to be in the Obsidian vault itself or should it be stored somewhere else on the OS?

# Output

Based on the information provided in the search results, it's generally fine to store your automation scripts within the Obsidian vault itself. Here are a few key points to consider:

1. Templater plugin support: The Templater plugin for Obsidian allows you to run scripts from a designated folder within your vault. As mentioned in search result [5], you can set up a folder in your Obsidian settings to hold your scripts[5].

2. Folder structure: Many users create a dedicated folder for scripts within their vault. For example, you could create a folder called "Scripts" or "Automations" to store your Python scripts[5].

3. Accessibility: Keeping scripts within the vault makes them easily accessible and portable if you move your vault to another device or location.

4. Version control: If you use version control (like git) for your Obsidian vault, having scripts inside the vault means they'll be included in your backups and version history[1].

5. Separation of concerns: While it's okay to keep scripts in the vault, you might want to consider keeping them separate from your regular notes. This can be achieved by using a dedicated folder within the vault[5].

However, there are a few situations where you might consider storing scripts outside the vault:

1. System-wide scripts: If you have scripts that interact with multiple vaults or perform system-level operations, it might make sense to store them elsewhere on your OS.

2. Security concerns: If your scripts contain sensitive information or API keys, you might prefer to keep them outside the vault for added security.

3. Performance: For very large vaults, keeping scripts separate might marginally improve performance, but this is generally not a significant concern.

In conclusion, storing your automation scripts within your Obsidian vault, preferably in a dedicated folder, is a common and generally acceptable practice. It keeps everything organized and easily accessible within your knowledge management system.

# Input

Is it possible to run the scripts in the same path?

# Output

Yes, if your bash script and the Python scripts it's running are all located in the same folder, you can use relative paths. This approach is simpler and more portable than using absolute paths. Here's how you can modify your setup:

1. Keep your bash script (e.g., `obsidian_scripts_runner.sh`) in the same folder as your Python scripts.

2. In the bash script, use relative paths to refer to the Python scripts.

Here's an updated version of the `obsidian_scripts_runner.sh` script using relative paths:

```bash
#!/bin/bash

while true; do
    if pgrep -x "obsidian" > /dev/null; then
        # Obsidian is running, execute your Python scripts
        python3 ./script1.py
        python3 ./script2.py
        # Add more scripts as needed
    fi
    sleep 300 # Wait for 5 minutes before checking again
done
```

In this script:

- `./script1.py` and `./script2.py` are relative paths, assuming these Python scripts are in the same directory as the bash script.
- The `./` prefix ensures that the scripts are executed from the current directory.

This approach has several advantages:

1. Simplicity: It's easier to understand and maintain.
2. Portability: The script will work regardless of where the folder containing these scripts is located on the system.
3. Consistency: If you move or copy the entire folder, the scripts will still work together without needing to update any paths.

Remember to keep all your scripts (both the bash runner and the Python scripts) in the same folder within your Obsidian vault. This could be a dedicated folder like "Scripts" or "Automations" in your vault.

When setting up the systemd service, make sure to set the `WorkingDirectory` to the folder containing your scripts. This ensures that the relative paths work correctly when the service runs. Here's how you can modify the systemd service file:

```
[Unit]
Description=Obsidian Scripts Runner
After=graphical-session.target

[Service]
ExecStart=/bin/bash /path/to/your/obsidian/vault/Scripts/obsidian_scripts_runner.sh
WorkingDirectory=/path/to/your/obsidian/vault/Scripts
Restart=always

[Install]
WantedBy=default.target
```

Replace `/path/to/your/obsidian/vault/Scripts` with the actual path to the folder containing your scripts within your Obsidian vault.

This setup allows you to keep all your automation scripts together in your Obsidian vault, making them easy to manage and portable if you ever need to move your vault.
## ## Extracted Prompts
[[Prompts/Autocapture/Execute Python scripts when Obsidian is in use.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Execute Python scripts when Obsidian is in use.md#Prompt 1|Prompt 1]]
