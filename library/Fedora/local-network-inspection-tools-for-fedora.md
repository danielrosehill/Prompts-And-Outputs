---
title: "Local network inspection tools for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

are there any tools for fedora that can do local network inspection and find other devices on the LAN

# Output

Yes, there are several tools available for **Fedora** that allow you to inspect the local network and identify other devices on your LAN (Local Area Network). These tools provide varying levels of detail, from basic device discovery to more in-depth network analysis. Here are some of the best tools for this purpose:

### 1. **nmap**
   - **Description**: `nmap` is one of the most powerful and widely used network scanning tools. It can discover devices on your network, check for open ports, and provide details about services running on those devices.
   - **Installation**:
     ```bash
     sudo dnf install nmap
     ```
   - **How to Use**:
     - To scan your local network and list all devices, run:
       ```bash
       nmap -sn 192.168.1.0/24
       ```
       Replace `192.168.1.0/24` with your local network’s IP range.
     - For a more detailed scan that checks for open ports and services:
       ```bash
       nmap -A 192.168.1.0/24
       ```
   - **Features**:
     - Device discovery (IP addresses, hostnames).
     - Port scanning and service identification.
     - OS and version detection.
   - **Recommended for**: Comprehensive network discovery and security auditing.

### 2. **arp-scan**
   - **Description**: `arp-scan` is a lightweight tool that uses ARP (Address Resolution Protocol) requests to discover all devices on the LAN. It’s fast and very effective for identifying devices connected to your network.
   - **Installation**:
     ```bash
     sudo dnf install arp-scan
     ```
   - **How to Use**:
     - To scan your local network for devices:
       ```bash
       sudo arp-scan --localnet
       ```
   - **Features**:
     - Quickly finds all devices on your local network.
     - Identifies MAC addresses and vendors of connected devices.
   - **Recommended for**: Fast, efficient device discovery on the LAN.

### 3. **Netdiscover**
   - **Description**: `Netdiscover` is a passive ARP reconnaissance tool designed for network scanning. It’s particularly useful in situations where you don’t want to actively probe devices but still want to discover hosts on the LAN.
   - **Installation**:
     ```bash
     sudo dnf install netdiscover
     ```
   - **How to Use**:
     - To scan your network in active mode:
       ```bash
       sudo netdiscover -r 192.168.1.0/24
       ```
     - The `-r` option specifies the network range you want to scan.
   - **Features**:
     - Passive ARP scanning to discover devices.
     - Identifies IP addresses and MAC addresses.
   - **Recommended for**: Passive scanning and quick discovery of devices on a network.

### 4. **Angry IP Scanner**
   - **Description**: **Angry IP Scanner** is a user-friendly, cross-platform network scanner. It has a graphical interface (GUI) and is very easy to use, making it suitable for users who prefer not to work with command-line tools.
   - **Installation**:
     - Download the RPM package for Fedora from the [official website](https://angryip.org/download/#linux).
     - Install it via:
       ```bash
       sudo dnf install ./ipscan-X.X.X-1.x86_64.rpm
       ```
   - **How to Use**:
     - After installation, launch Angry IP Scanner from your applications menu. Enter your network range (e.g., `192.168.1.0/24`) and click "Start" to scan.
   - **Features**:
     - GUI-based network scanner.
     - Detects IP addresses, MAC addresses, and open ports.
   - **Recommended for**: Users who prefer a graphical interface for network discovery.

### 5. **Fing**
   - **Description**: **Fing** is a popular network scanner available on Linux, Android, and iOS. It’s widely used for quickly discovering devices on the local network and monitoring network activity.
   - **Installation**:
     - Download and install the RPM package from the [official Fing website](https://www.fing.com/products/development-toolkit).
   - **How to Use**:
     - Launch Fing from the terminal:
       ```bash
       sudo fing
       ```
     - It will automatically scan the network and list all detected devices.
   - **Features**:
     - Quick LAN discovery.
     - Lists IP addresses, hostnames, MAC addresses, and vendors.
   - **Recommended for**: Quick and easy network scanning with a focus on device discovery.

### 6. **Wireshark**
   - **Description**: **Wireshark** is a powerful network protocol analyzer that can capture and inspect traffic on your LAN. While it’s more advanced than a simple network scanner, it allows you to see in-depth details about the devices on your network and the traffic between them.
   - **Installation**:
     ```bash
     sudo dnf install wireshark
     ```
   - **How to Use**:
     - Run Wireshark and select the network interface you want to monitor.
     - Apply a filter to focus on device discovery traffic, such as ARP or ICMP:
       ```bash
       arp or icmp
       ```
   - **Features**:
     - Captures and analyzes network traffic in real-time.
     - Provides detailed information about each device, packet, and protocol.
   - **Recommended for**: Advanced network monitoring and troubleshooting.

### 7. **Avahi (Zeroconf Service Discovery)**
   - **Description**: **Avahi** provides service discovery on a local network using the Zeroconf protocol. It’s mainly used for discovering services (e.g., printers, file shares) rather than devices, but it can give you insights into what’s available on your network.
   - **Installation**:
     ```bash
     sudo dnf install avahi avahi-tools
     ```
   - **How to Use**:
     - Use `avahi-browse` to discover services on your LAN:
       ```bash
       avahi-browse -a
       ```
   - **Features**:
     - Service discovery for printers, file shares, and other network services.
     - Works over mDNS (Multicast DNS) and Zeroconf protocols.
   - **Recommended for**: Discovering services and shared resources on your LAN.

---

### Best Option for You
- **For Simple Device Discovery**: Tools like **nmap**, **arp-scan**, and **Netdiscover** will quickly scan your LAN for connected devices.
- **For Advanced Users**: **Wireshark** provides detailed network traffic analysis and is best if you need in-depth inspection of device communication.
- **For GUI-Based Tools**: **Angry IP Scanner** offers a graphical interface if you prefer not to work with command-line tools.

Each tool is effective for its specific use case, and the choice depends on how detailed you want your network inspection to be. Would you like assistance in setting up or using one of these tools?