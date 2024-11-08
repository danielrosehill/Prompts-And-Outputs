---
title: "Do you use the bridge or the physical interface when setting up Mac VLAN"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


When setting up a **macvlan** network in Docker, the parent interface you specify should be the **physical Ethernet interface** of the host, not the virtual interface (like a bridge) that the VM is using.

### Explanation

1. **Physical Ethernet Interface**:
   - The parent interface needs to be the physical network interface on the Proxmox host that connects to your LAN. This interface has the actual IP address assigned to it by your network and allows the Docker containers to communicate directly with the local network.

2. **Why Not the Virtual Interface?**:
   - If you use a virtual interface (like a bridge), the Docker containers will not have direct access to the physical network. Instead, they would be isolated to the virtual network created by the bridge, which would restrict their ability to communicate with other devices on the LAN.

### Steps to Identify the Physical Interface

1. **On the Proxmox Host**:
   - You can use the following command to list all network interfaces:
     ```bash
     ip addr
     ```
   - Look for an interface that corresponds to your physical network connection (often named something like `eth0`, `ens18`, or similar).

2. **Create the macvlan Network**:
   - Once you have identified the physical interface, you can create the macvlan network using that interface name:
     ```bash
     docker network create -d macvlan \
     --subnet=192.168.1.0/24 \  # Replace with your LAN subnet
     --gateway=192.168.1.1 \    # Replace with your LAN gateway
     -o parent=<physical_interface_name> my_macvlan
     ```
   - Replace `<physical_interface_name>` with the actual name of your physical network interface.

### Conclusion

Using the physical Ethernet interface as the parent interface for the macvlan network will ensure that your Docker containers have unique IPs directly accessible on your LAN, allowing them to communicate with other devices seamlessly.