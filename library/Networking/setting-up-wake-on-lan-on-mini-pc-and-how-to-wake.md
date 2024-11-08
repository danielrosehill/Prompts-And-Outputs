---
title: "Setting up wake on LAN on mini PC and how to wake"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# MAC address

The **MAC address** for your **eth0** interface (wired connection) is:

```
00:E0:4C:1C:62:F5
```

This is the address you should use for sending Wake-on-LAN packets.

# How to do a WOL

 To wake your **LibreELEC mini PC** (with MAC address `00:E0:4C:1C:62:F5`) from your **Fedora workstation**, you can use the **Wake-on-LAN (WOL)** tool. Here's how to do it step-by-step:

### Step 1: Install the Wake-on-LAN utility
First, you need to install the **`wol`** tool on your Fedora workstation:

```bash
sudo dnf install wol
```

### Step 2: Send a Wake-on-LAN Packet
Once the **`wol`** tool is installed, you can send the magic packet to wake up your mini PC by running the following command:

```bash
wol 00:E0:4C:1C:62:F5
```

### Step 3: Verify Wake-on-LAN
Your mini PC should wake up after the packet is sent. You can verify this by either checking its status on your network (e.g., by pinging its IP address) or using SSH to connect to it:

```bash
ping 192.168.1.6
```

or

```bash
ssh root@192.168.1.6
```

### Troubleshooting
If the Wake-on-LAN command doesn't work:
- **Ensure the mini PC is properly configured for WOL** (as we covered in previous steps, `ethtool` should show `Wake-on: g`).
- **Check your network setup**: The device needs to be reachable over the network, even in standby mode.
- **Some routers** may block WOL packets, so ensure your router supports forwarding broadcast packets.

Let me know if you encounter any issues or if it works as expected!