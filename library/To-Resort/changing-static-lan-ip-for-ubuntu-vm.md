---
title: "Changing static LAN IP for Ubuntu VM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To change the static IP address of your **Ubuntu 24.04** server to **192.168.1.5**, you'll need to configure **Netplan**, the default network management tool in modern versions of Ubuntu.

Here’s how you can configure it:

### Steps to Change Static IP Address with Netplan

1. **Find the Netplan Configuration File**:
   - Netplan configuration files are stored in the `/etc/netplan/` directory and usually have a `.yaml` extension (e.g., `00-installer-config.yaml`).
   - List the files in the directory to find the correct configuration file:
     ```bash
     ls /etc/netplan/
     ```

2. **Edit the Netplan Configuration**:
   - Open the configuration file with a text editor (e.g., `nano` or `vim`):
     ```bash
     sudo nano /etc/netplan/00-installer-config.yaml
     ```
   - You should see something similar to the following if DHCP is currently enabled:
     ```yaml
     network:
       version: 2
       ethernets:
         ens3:
           dhcp4: true
     ```

3. **Configure the Static IP**:
   - To set a static IP (e.g., `192.168.1.5`), modify the file as follows. Ensure you adjust `ens3` to the correct network interface name (it could be `eth0`, `ens160`, or something else—check by running `ip a` to find the correct interface):
     ```yaml
     network:
       version: 2
       ethernets:
         ens3:  # Replace with your actual interface name if different
           addresses:
             - 192.168.1.5/24
           gateway4: 192.168.1.1  # Replace with your actual gateway
           nameservers:
             addresses:
               - 8.8.8.8
               - 8.8.4.4
           dhcp4: false
     ```

   In this example:
   - `addresses`: Defines the static IP (in CIDR format) that you want to assign.
   - `gateway4`: Specifies the gateway for your network.
   - `nameservers`: Defines the DNS servers to use.

4. **Apply the Configuration**:
   - Once you’ve made the changes, save the file and apply the configuration using Netplan:
     ```bash
     sudo netplan apply
     ```

5. **Verify the IP Change**:
   - Check if the static IP has been applied correctly:
     ```bash
     ip a
     ```
   - You should now see that the interface is using **192.168.1.5**.

6. **Test the Network Connectivity**:
   - Test the connectivity by pinging your gateway or an external site:
     ```bash
     ping 192.168.1.1  # Gateway
     ping google.com  # External site to verify DNS resolution
     ```

### Additional Notes:
- **Backup** your Netplan configuration before making changes by copying the current file:
  ```bash
  sudo cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bak
  ```

- **Network Interface Name**: Make sure the interface name (`ens3`, `eth0`, etc.) is correct by checking the output of:
  ```bash
  ip a
  ```

By following these steps, your **Ubuntu 24.04 VM** will have a static IP address of **192.168.1.5**. Let me know if you need further assistance!