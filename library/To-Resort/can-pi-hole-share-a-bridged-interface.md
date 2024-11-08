---
title: "Can Pi Hole share a bridged interface"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, **Pi-hole** can share a **bridged network interface** with another VM on the same **Proxmox host**. This is a very common network configuration in **virtualization environments** like Proxmox, where multiple VMs need to access the LAN via the same physical network card (NIC). Here’s a breakdown of how it works and how to set it up properly.

### **How Bridged Network Interfaces Work in Proxmox**
A **bridged interface** in Proxmox acts like a virtual switch that connects the virtual machines (VMs) to the physical network. All VMs connected to the same bridge interface will have their own IP addresses but will share the physical network card to communicate with other devices on the local network.

For example, if your Proxmox host is connected to a physical router using a NIC, creating a bridge (`vmbr0`) allows any VM attached to `vmbr0` to communicate directly with the rest of the LAN, just like they are physically connected to the same router or switch.

### **Benefits of Using a Bridged Interface for Pi-hole and Another VM**
- **Network Flexibility**: Multiple VMs can communicate with devices on the LAN and use the same network.
- **Simplicity**: No need for complex NAT or internal networking configurations between VMs—each VM has its own IP address on the local network.
- **Efficient Use of Resources**: You only need one physical network connection, and all VMs can utilize it.

### **Setting Up Pi-hole to Share a Bridged Interface in Proxmox**

#### **Step 1: Check Bridge Configuration on Proxmox**
- In **Proxmox**, a bridged interface (e.g., `vmbr0`) should already be configured.
- This bridge (`vmbr0`) is associated with the physical NIC (e.g., `enp0s31f6`).
- You can verify this by accessing **Proxmox's web interface** and navigating to **Datacenter** > **Node** > **Network**.

If `vmbr0` is already configured, it’s typically attached to the physical NIC to provide network access to VMs.

#### **Step 2: Create the Pi-hole VM**
- **Create a New VM** in Proxmox for Pi-hole, as previously described.
- When configuring the network interface for this VM, choose the existing **bridged interface** (`vmbr0`).
- This means the Pi-hole VM will be assigned an IP address on your LAN by the DHCP server (usually your router) or can be manually configured with a static IP.

#### **Step 3: Set Up the Other VM to Use the Same Bridge**
- If you already have another VM, or if you’re creating a new one, ensure that its **network configuration** also uses the same bridged interface (`vmbr0`).
- You can have **multiple VMs** using `vmbr0` without any issues.

#### **Step 4: Assign Static IPs to Both VMs (Recommended)**
- For a stable network setup, it's recommended to assign **static IPs** to the Pi-hole VM and other VMs that share the same bridged interface.
- You can either:
  - **Assign Static IPs in the VM Configuration**: Manually set a static IP within the VM itself (e.g., during the Linux OS setup).
  - **Reserve IP Addresses in Your Router’s DHCP**: If the router allows it, reserve IP addresses for the MAC addresses of the VMs in the router’s DHCP settings. This ensures the VMs always get the same IP.

### **How to Make Pi-hole Accessible to All VMs and LAN Devices**
- **Primary DNS Server**: Once the Pi-hole is set up, you'll want to configure devices on the LAN to use Pi-hole as their **primary DNS server**.
- Since the **Pi-hole VM** is connected via the same bridge (`vmbr0`), it is effectively on the same network segment as all other devices, including other VMs, desktops, and IoT devices.
  
You can:
1. **Manually Set the DNS Server** for each LAN device to the Pi-hole IP address.
2. If the ISP router allows it, **update the DHCP settings** to assign the Pi-hole IP as the DNS server.

### **Network Configuration Example**
- Suppose your LAN uses the IP range **192.168.1.0/24**.
- You have:
  - **Proxmox Host** with `vmbr0` bridged to physical NIC.
  - **Pi-hole VM** with IP address `192.168.1.10`.
  - **Another VM** (e.g., Home Assistant) with IP address `192.168.1.11`.
  
Both VMs are connected to `vmbr0`:
- **Pi-hole** will act as a DNS server for the entire LAN.
- **Home Assistant** (or any other VM) can resolve domain names using the Pi-hole server (`192.168.1.10`).

### **Ensuring Compatibility with the ISP Router**
- Since you mentioned that you cannot change the **DNS settings on the router** itself, you will need to:
  1. **Manually Set DNS**: Set the **Pi-hole IP address** (`192.168.1.10`) as the DNS server on each device that you want filtered by Pi-hole.
  2. **Hosts File Option (For Internal Resolution)**: Alternatively, for specific devices that have issues resolving `ha.testhomewebsite.com` to its local IP, you can add the Pi-hole IP in the **hosts file** of those devices.

### **Firewall Considerations**
- Ensure that the **firewall** on the Proxmox host, Pi-hole VM, and other VMs allows incoming **DNS traffic (port 53)** so that DNS queries are properly handled.
- Allow LAN traffic to flow freely between the VMs that use `vmbr0`.

### **Summary**
- **Yes, Pi-hole and other VMs can share the same bridged interface (`vmbr0`)** in Proxmox. It’s common and efficient to do so.
- **Assign Static IPs** to each VM to avoid potential IP conflicts and make DNS resolution stable.
- Ensure that each device on your LAN is using the **Pi-hole IP as its DNS server**, either manually or via DHCP reservations, depending on what is supported by your router.
- **Network Configuration** should be simple since all VMs and physical devices will be on the same network, with Pi-hole acting as a DNS resolver for all.

Let me know if you need help with configuring anything specific, such as assigning static IPs or setting up a firewall for your Proxmox environment!