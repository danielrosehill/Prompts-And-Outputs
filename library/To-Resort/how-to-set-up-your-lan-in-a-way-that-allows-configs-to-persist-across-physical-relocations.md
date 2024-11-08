---
title: "How to set up your LAN in a way that allows configs to persist across physical relocations"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

My wife and I are preparing to move to a new apartment in a few months. My local netrwork is somewhat "advanced" and has a number of Zigbee devices, among other things. I'd love to set up the LAN in such a way that it's "portable". Ie, that I can retain my local IP assignments. It seems to me that the best way to do this would be to use my own router in addition to my ISP's and keep the ISP router in bridge mode. Is that the case? And can you recommend how I might implement this approach?

# Output

Yes, you're on the right track! Setting up your own router and keeping the ISP router in **bridge mode** is a great approach to create a portable local network. This setup will allow you to retain control over your IP assignments, even if you change ISPs or move to a new location. Here’s how you can implement it:

### 1. **Configure the ISP Router in Bridge Mode**
- **Bridge Mode** effectively disables the routing functionality of your ISP’s router, allowing your personal router to handle all the routing, DHCP, and NAT (Network Address Translation) functions.
- Access your ISP router’s settings and look for the **bridge mode** option. This might be under the **WAN** or **Internet** settings. If bridge mode isn't readily available, contact your ISP, as some routers require the ISP’s help to enable it.
- By putting the ISP router in bridge mode, you will bypass its internal firewall and DHCP server, preventing conflicts with your personal router’s DHCP server.

### 2. **Set Up Your Own Router**
- Purchase and set up a high-quality **router** that will handle your LAN and devices. Popular brands like **Ubiquiti**, **Asus**, or **Netgear** offer routers with advanced features and better customizability.
- **DHCP Configuration**: Configure a static IP range on your personal router. You can retain your current local IP assignments (e.g., 192.168.1.x range) by setting up **static DHCP leases** for key devices like your Zigbee coordinator, NAS, and any other critical devices. This ensures that these devices always get the same IP.
  
  Example:
  - Zigbee Coordinator: 192.168.1.147
  - NAS: 192.168.1.50
  - Home Assistant: 192.168.1.3
  - General Desktop: 192.168.1.132

- **Network Segmentation**: If you have a large network or require additional isolation, you can create **VLANs** (Virtual LANs) to segment devices. This can be helpful if you want to keep IoT devices on a separate network for security purposes.
  
### 3. **Backup Your Router Configuration**
- Most modern routers allow you to **export** the configuration. This means you can save a copy of your router’s setup and reimport it when moving or setting up a new router.
- Make sure your backup includes all static IP assignments, port forwarding rules, VLAN settings, etc.

### 4. **Use Your Router for Zigbee and Smart Home Devices**
- Since you have Zigbee devices, ensure that your router can handle the traffic from your Zigbee network without interference. If your Zigbee network uses **2.4 GHz**, you may want to adjust your Wi-Fi channel to avoid conflicts.
- **Zigbee to MQTT**: Ensure that your **Zigbee coordinator** retains its IP assignment so that it remains seamlessly integrated with your **Home Assistant** or other automation platforms.

### 5. **Make Your LAN “Portable”**
- **Keep the Same IP Range**: By managing your own router, you can maintain the same internal network setup (e.g., 192.168.1.x). This means that regardless of where you move, your local IP assignments will stay the same.
- **Portable DNS**: If you have any local DNS setup (like **Pi-hole** or **Home Assistant**), you can retain these configurations across moves by keeping the router settings the same.

### 6. **When You Move**
- When you move to the new apartment, simply plug your personal router into the ISP's modem (again in bridge mode), and your devices will retain their configurations and IPs.
- Since all devices are assigned IPs by your own router, they should automatically reconnect once the router is up and running.

### 7. **Additional Recommendations**
- **Uninterrupted Power Supply (UPS)**: Consider adding a UPS to your router and key network equipment to ensure your LAN remains stable during power outages.
- **Mesh Wi-Fi**: If your new apartment is large, consider implementing a **mesh Wi-Fi system** to extend the coverage seamlessly.

This approach will keep your network consistent across moves, allowing you to retain local IP assignments and avoid the hassle of reconfiguring devices. Let me know if you need further clarification or suggestions for specific equipment!