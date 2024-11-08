---
title: "Enabling WOL for Fedora desktop"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here is the **Wake on LAN (WoL)** setup tutorial customized for your **`enp6s0`** ethernet interface on Fedora:

### 1. **Enable Wake on LAN in BIOS/UEFI:**
   - Restart your computer and access the BIOS/UEFI by pressing a key like `F2`, `F10`, or `DEL` during boot (check your computer's manual for the correct key).
   - In the BIOS/UEFI, navigate to the **Power Management** or **Network** section.
   - Find the option to enable **Wake on LAN** and set it to "Enabled."
   - Save and exit.

### 2. **Check if `enp6s0` Supports WoL:**
   - Open a terminal and run the following command to check if your network interface supports WoL:
     ```bash
     sudo ethtool enp6s0
     ```
   - Look for the line that says `Wake-on:`. If it says `g`, WoL is supported.

### 3. **Enable Wake on LAN for `enp6s0`:**
   - Enable WoL using the following command:
     ```bash
     sudo ethtool -s enp6s0 wol g
     ```
   - Verify the setting by running:
     ```bash
     sudo ethtool enp6s0
     ```
   - You should now see `Wake-on: g` in the output, indicating that WoL is enabled.

### 4. **Make the WoL Setting Persistent Across Reboots:**
   To ensure the WoL setting persists after a reboot, you can create a script that NetworkManager will execute when the network interface is brought up.

   - Create a script in the `/etc/NetworkManager/dispatcher.d/` directory:
     ```bash
     sudo nano /etc/NetworkManager/dispatcher.d/enable-wol
     ```
   - Add the following content to the script:
     ```bash
     #!/bin/bash
     if [ "$1" == "enp6s0" ] && [ "$2" == "up" ]; then
       /usr/sbin/ethtool -s enp6s0 wol g
     fi
     ```
   - Save the file and close the editor.

   - Make the script executable:
     ```bash
     sudo chmod +x /etc/NetworkManager/dispatcher.d/enable-wol
     ```

### 5. **Test Wake on LAN:**
   - Shut down your Fedora computer.
   - From another device on the network, install a tool like `wakeonlan` to send a WoL packet:
     ```bash
     sudo dnf install wakeonlan
     ```
   - Send the WoL packet using your Fedora computer's MAC address:
     ```bash
     wakeonlan <MAC-address-of-enp6s0>
     ```

You can find the MAC address of your `enp6s0` interface by running:
```bash
ip link show enp6s0
```

This will enable Wake on LAN for your **`enp6s0`** interface and make it persist across reboots.