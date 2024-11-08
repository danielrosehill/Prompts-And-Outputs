---
title: "Utillities for finding free local IPs on the LAN"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Got it! Here are Linux commands for using `nmap` and `arp-scan` to find available IP addresses on your local network:

### Option 1: Using `nmap`
`nmap` is a versatile network scanner that can be used to find active devices on your subnet.

1. **Install `nmap`**:
   ```bash
   sudo apt install nmap
   ```
   or on Fedora:
   ```bash
   sudo dnf install nmap
   ```

2. **Scan the Network**:
   ```bash
   sudo nmap -sn 192.168.1.0/24
   ```
   - **Explanation**:
     - `-sn` (ping scan) lists all the devices on the network without doing a port scan.
     - `192.168.1.0/24` scans the entire subnet (change the IP range as necessary).
   - **Output**:
     - The output will list the IP addresses that are active. Any IP not listed is likely available.

### Option 2: Using `arp-scan`
`arp-scan` allows you to quickly scan your local network for devices, using ARP to discover active IP addresses.

1. **Install `arp-scan`**:
   ```bash
   sudo apt install arp-scan
   ```
   or on Fedora:
   ```bash
   sudo dnf install arp-scan
   ```

2. **Scan the Network**:
   ```bash
   sudo arp-scan --interface=ens18 192.168.1.0/24
   ```
   - **Explanation**:
     - `--interface=ens18`: Replace `ens18` with your actual network interface name (you can find your interface using `ip a`).
     - `192.168.1.0/24`: Scans all IP addresses within the `192.168.1.0` subnet.
   - **Output**:
     - The output will list the IP addresses that are currently in use. If `192.168.1.100` doesn’t appear in the list, that means it's likely available.

### Summary
- **`nmap`**: Provides a list of all devices that responded to ping requests.
- **`arp-scan`**: Uses ARP requests to find devices; useful in environments where ICMP ping may be blocked.

Both methods will give you a good overview of which IP addresses are in use, allowing you to find a free one.