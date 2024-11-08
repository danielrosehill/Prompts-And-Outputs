---
title: "Setting up bridge mode on the Bezeq router"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Can you provide instructions for configuring bridge mode on the Sagemcom Fast 5670 please?

Based on the settings displayed in your image for the **Sagemcom Fast 5670** router (branded by Bezeq), you have access to some useful information for understanding its current status. Here's how you can proceed to **configure bridge mode** or use this router with your own router for better control.

### Reviewing the Interface
From the **Device Info** section, it appears you can only view basic information about the device, such as:
- **Serial Number**: SMBS0053C760
- **Hardware Version**: 3.00
- **Software Version**: BZ_SGF307
- **WAN MAC Address**: Starts with Bo:BB:E5 (may be useful in identifying the device in your network)
- **CPU and Memory Usage**: Displays load percentages.

### Configuring Bridge Mode
Unfortunately, from the screenshot provided, it doesn't look like you have an obvious **Bridge Mode** configuration option in the visible settings. However, you may still be able to proceed with the following methods:

#### Method 1: Finding Bridge Mode via the Web Interface
1. **Log In to the Web Interface**:
   - You are already logged in, which is a great start.
   - Check under other tabs like **LAN IPv4**, **Maintenance**, or even sub-options under **Device Info** to see if there are any advanced options.
   - Look specifically for something related to **network mode** or **WAN settings**—these are often areas where bridge mode can be activated.

2. **Advanced Settings**:
   - If there’s a tab labeled **Advanced**, **Internet**, or **WAN**, navigate to it. Bridge mode is often hidden in these advanced configurations.

3. **Bridge Mode Option**:
   - If you find it, enable **Bridge Mode**. This will make your ISP-provided router act as a modem, allowing your personal router to handle all networking tasks.

4. **Disable DHCP**:
   - If there is no bridge mode, you can try disabling the **DHCP server** in the router’s settings. Then, let your own router handle DHCP tasks.

#### Method 2: Contact ISP or Check Documentation
If the bridge mode setting isn't available in the interface:
- **Contact Bezeq Support**: Sometimes, ISPs lock down certain options in the router firmware. You can call Bezeq customer support and ask them to **enable bridge mode** remotely.
- **Check Router Documentation**: Look for user manuals online. The documentation might provide details on accessing more advanced settings.

### Using Your Own Router with the Sagemcom Router
If bridge mode is not an option, you can still connect your router behind the Sagemcom and create a **double NAT setup**. Here’s how:
1. **Connect your router’s WAN port** to one of the **LAN ports** of the Sagemcom router.
2. Make sure your router uses a **different subnet** (e.g., if the Sagemcom uses `192.168.1.x`, your router should use `192.168.1.x`).
3. **Disable Wi-Fi** on the Sagemcom router to avoid interference.

### Summary
- Look for **Advanced**, **LAN IPv4**, or **Maintenance** sections to try and locate bridge mode.
- If you can’t find bridge mode, try disabling **DHCP** to use your own router for network management.
- **Contact Bezeq** for assistance in enabling bridge mode if it's not available in your interface.
- As a workaround, consider a **double NAT setup** with a new subnet.

Let me know if you need more specific guidance on any of these steps, or if you need help configuring your new router!