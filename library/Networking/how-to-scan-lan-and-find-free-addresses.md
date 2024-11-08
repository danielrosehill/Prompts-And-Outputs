---
title: "How to scan LAN and find free addresses"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To scan your **LAN (192.168.1.0/24 network)** and find unused IPs, you can use a few tools like **nmap** or **ping sweep** commands. These tools will help you identify which IP addresses are in use so you can find the unused ones.

### Option 1: **Using `nmap`**

**`nmap`** is a powerful tool that can scan your network and list active hosts (devices). To find unused IPs, you'll look for the IP addresses **not** shown in the list of active hosts.

#### Steps:
1. **Install `nmap`** if you don't have it installed:
   ```bash
   sudo apt update
   sudo apt install nmap
   ```

2. **Scan your 192.168.1.0/24 network** to find active devices:
   ```bash
   sudo nmap -sn 192.168.1.0/24
   ```

   - The `-sn` option tells `nmap` to perform a "ping scan" and list which IPs are active.
   - **Output** will show the active hosts on your network. Unlisted IPs are likely **unused**.

3. **Check the output**:
   - You'll see a list of active IP addresses like this:
     ```
     Nmap scan report for 192.168.1.2
     Nmap scan report for 192.168.1.5
     Nmap scan report for 192.168.1.10
     ```
   - Any IP addresses that are not listed in the output are likely unused and available for assignment.

### Option 2: **Using `ping` Sweep**
If you prefer a simpler tool, you can run a **ping sweep** to manually check which IPs respond, indicating they are in use.

#### Steps:
1. **Use `fping` for a faster scan**:
   - First, install `fping`:
     ```bash
     sudo apt install fping
     ```

2. **Scan your network for active devices**:
   ```bash
   fping -a -g 192.168.1.0/24 2>/dev/null
   ```

   - The `-a` flag shows only active (alive) hosts, and the `-g` flag generates all addresses within the range.
   - You’ll get a list of active IP addresses that responded to the ping. Any IP addresses not listed are likely unused.

### Option 3: **Check Your Router’s DHCP Lease List**
Your router typically maintains a **DHCP lease table** that lists all devices that have been assigned IP addresses. You can:
1. **Login to your router's web interface**.
2. **Check the DHCP lease list** under **Network settings** or **LAN settings**.
3. **Identify unused IPs** by checking which addresses are not currently leased.

### Option 4: **Using ARP**
You can also use the **ARP table** on your machine to check which IPs have been detected recently.

1. **Run the following command**:
   ```bash
   arp -a
   ```

   This will show you the IP addresses and MAC addresses of devices your machine has communicated with. Any IP not shown is likely unused.

### Summary
- **nmap** is the most thorough tool for discovering active hosts.
- **fping** or a basic **ping sweep** is a quicker alternative.
- You can also check your router's **DHCP lease table** for a list of IPs currently in use.

Once you’ve identified which IPs are in use, you can safely assign an unused one to your new service or container. Let me know if you need help with any part of the process!